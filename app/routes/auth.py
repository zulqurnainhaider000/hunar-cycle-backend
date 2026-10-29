import os
import secrets
import datetime
import jwt
from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from app.db import db
from utils.email_service import send_otp_email_async
from app.auth_middleware import token_required

auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')
SECRET_KEY = os.environ.get('SECRET_KEY') or os.environ.get('JWT_SECRET', 'hunarcircle_super_secret_jwt_key_2026')

def to_utc(dt):
    """Normalize datetime to UTC-aware datetime."""
    if dt is None:
        return None
    if dt.tzinfo is None:
        return dt.replace(tzinfo=datetime.timezone.utc)
    return dt.astimezone(datetime.timezone.utc)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json or {}
    
    username = data.get('username', '').strip()
    email = data.get('email', '').strip().lower()
    password = data.get('password', '')
    raw_role = data.get('role', 'student')
    role = 'teacher' if str(raw_role).lower().strip() == 'teacher' else 'student'
    
    if not username or not email or not password:
        return jsonify({"error": "Missing required fields (username, email, password)"}), 400
        
    try:
        if not db.is_connected():
            db.connect()
            
        # Check if email is already taken
        existing_email = db.user.find_first(where={"email": email})
        if existing_email:
            # If the user already exists and password matches, log them straight in
            if check_password_hash(existing_email.passwordHash, password):
                token = jwt.encode({
                    'user_id': existing_email.id,
                    'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=30)
                }, SECRET_KEY, algorithm="HS256")
                
                return jsonify({
                    "success": True,
                    "message": "Account already exists with this password. Logged in successfully!",
                    "token": token,
                    "user": {
                        "id": existing_email.id,
                        "username": (existing_email.username or "").strip(),
                        "email": existing_email.email,
                        "role": getattr(existing_email, 'role', 'student') or 'student',
                        "level": getattr(existing_email, 'level', 1),
                        "xp": getattr(existing_email, 'xp', 0),
                        "coins": getattr(existing_email, 'coins', 0),
                        "loginStreak": getattr(existing_email, 'loginStreak', 1)
                    }
                }), 200
            
            is_verified = getattr(existing_email, 'isVerified', True)
            if is_verified is False:
                # User exists but is unverified - allow refreshing OTP
                now_utc = datetime.datetime.now(datetime.timezone.utc)
                otp_code = str(secrets.randbelow(900000) + 100000)
                expires_at = now_utc + datetime.timedelta(minutes=10)
                hashed_password = generate_password_hash(password)
                
                update_data = {
                    "username": username,
                    "passwordHash": hashed_password
                }
                if hasattr(existing_email, 'otpCode'):
                    update_data.update({
                        "otpCode": otp_code,
                        "otpExpiresAt": expires_at,
                        "lastOtpSentAt": now_utc
                    })
                
                db.user.update(
                    where={"id": existing_email.id},
                    data=update_data
                )
                
                send_otp_email_async(email, otp_code)
                return jsonify({
                    "success": True,
                    "needsVerification": True,
                    "email": email,
                    "message": "Verification code sent to your email"
                }), 200
            else:
                return jsonify({"error": "Email is already registered. Please log in with your password."}), 400
            
        # Check if username already exists
        existing_username = db.user.find_first(where={"username": username})
        if existing_username:
            return jsonify({"error": "Username already exists. Please choose another username."}), 409
            
        # Hash the password
        hashed_password = generate_password_hash(password)
        now_utc = datetime.datetime.now(datetime.timezone.utc)
        
        # Create user with role
        create_payload = {
            "username": username,
            "email": email,
            "passwordHash": hashed_password,
            "lastLogin": now_utc,
            "loginStreak": 1,
            "coins": 1000
        }
        
        try:
            new_user = db.user.create(data={
                **create_payload,
                "role": role
            })
        except Exception:
            new_user = db.user.create(data=create_payload)
            try:
                db.execute_raw('UPDATE "User" SET "role" = $1 WHERE "id" = $2;', role, new_user.id)
                setattr(new_user, 'role', role)
            except Exception:
                pass
        
        # Issue JWT Token immediately so user gets into app seamlessly
        token = jwt.encode({
            'user_id': new_user.id,
            'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=30)
        }, SECRET_KEY, algorithm="HS256")
        
        return jsonify({
            "success": True,
            "message": "Registration successful!",
            "token": token,
            "user": {
                "id": new_user.id,
                "username": (new_user.username or "").strip(),
                "email": new_user.email,
                "role": getattr(new_user, 'role', role) or role,
                "level": getattr(new_user, 'level', 1),
                "xp": getattr(new_user, 'xp', 0),
                "coins": getattr(new_user, 'coins', 1000),
                "loginStreak": getattr(new_user, 'loginStreak', 1)
            }
        }), 201
        
    except Exception as e:
        print("Registration Error:", str(e))
        return jsonify({"error": "Failed to register user"}), 500

@auth_bp.route('/verify-otp', methods=['POST'])
def verify_otp():
    data = request.json or {}
    email = data.get('email', '').lower().strip()
    otp = str(data.get('otp') or data.get('otpCode') or '').strip()
    
    if not email or not otp:
        return jsonify({"error": "Email and 6-digit OTP code are required"}), 400
        
    try:
        if not db.is_connected():
            db.connect()
            
        user = db.user.find_first(where={"email": email})
        if not user:
            return jsonify({"error": "User with this email not found"}), 404
            
        is_verified = getattr(user, 'isVerified', True)
        otp_code = getattr(user, 'otpCode', None)
        
        # If already verified or no OTP pending
        if is_verified and not otp_code:
            token = jwt.encode({
                'user_id': user.id,
                'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=30)
            }, SECRET_KEY, algorithm="HS256")
            
            return jsonify({
                "success": True,
                "message": "Email is already verified",
                "token": token,
                "user": {
                    "id": user.id,
                    "username": (user.username or "").strip(),
                    "email": user.email,
                    "level": getattr(user, 'level', 1),
                    "xp": getattr(user, 'xp', 0),
                    "coins": getattr(user, 'coins', 0),
                    "loginStreak": getattr(user, 'loginStreak', 1)
                }
            }), 200
            
        if not otp_code:
            return jsonify({"error": "No pending verification code found. Please request a new code."}), 400
            
        # Check code validity
        if otp_code.strip() != otp:
            return jsonify({"error": "Invalid verification code. Please check and try again."}), 400
            
        # Check expiry
        now_utc = datetime.datetime.now(datetime.timezone.utc)
        otp_exp = getattr(user, 'otpExpiresAt', None)
        expires_at = to_utc(otp_exp) if otp_exp else None
        
        if expires_at and now_utc > expires_at:
            return jsonify({"error": "Verification code has expired. Please request a new code."}), 400
            
        # Success: mark user as verified and clear OTP if fields supported
        update_data = {}
        if hasattr(user, 'isVerified'):
            update_data["isVerified"] = True
        if hasattr(user, 'otpCode'):
            update_data["otpCode"] = None
        if hasattr(user, 'otpExpiresAt'):
            update_data["otpExpiresAt"] = None
            
        if update_data:
            updated_user = db.user.update(
                where={"id": user.id},
                data=update_data
            )
        else:
            updated_user = user
        
        # Issue JWT auth token
        token = jwt.encode({
            'user_id': updated_user.id,
            'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=30)
        }, SECRET_KEY, algorithm="HS256")
        
        return jsonify({
            "success": True,
            "message": "Email verified successfully!",
            "token": token,
            "user": {
                "id": updated_user.id,
                "username": (updated_user.username or "").strip(),
                "email": updated_user.email,
                "role": getattr(updated_user, 'role', 'student') or 'student',
                "level": getattr(updated_user, 'level', 1),
                "xp": getattr(updated_user, 'xp', 0),
                "coins": getattr(updated_user, 'coins', 0),
                "loginStreak": getattr(updated_user, 'loginStreak', 1)
            }
        }), 200
        
    except Exception as e:
        print("Verify OTP Error:", str(e))
        return jsonify({"error": "Failed to verify code"}), 500

@auth_bp.route('/resend-otp', methods=['POST'])
def resend_otp():
    data = request.json or {}
    email = data.get('email', '').lower().strip()
    
    if not email:
        return jsonify({"error": "Email is required"}), 400
        
    try:
        if not db.is_connected():
            db.connect()
            
        user = db.user.find_first(where={"email": email})
        if not user:
            return jsonify({"error": "User with this email not found"}), 404
            
        is_verified = getattr(user, 'isVerified', True)
        if is_verified and not getattr(user, 'otpCode', None):
            return jsonify({
                "message": "Email is already verified",
                "alreadyVerified": True
            }), 200
            
        now_utc = datetime.datetime.now(datetime.timezone.utc)
        last_sent_val = getattr(user, 'lastOtpSentAt', None)
        
        # 60-second cooldown check
        if last_sent_val:
            last_sent = to_utc(last_sent_val)
            if last_sent:
                elapsed = (now_utc - last_sent).total_seconds()
                if elapsed < 60:
                    remaining = int(60 - elapsed)
                    return jsonify({
                        "error": f"Please wait {remaining} seconds before requesting a new code.",
                        "remainingCooldown": remaining
                    }), 429
                
        # Generate new 6-digit numeric OTP code
        otp_code = str(secrets.randbelow(900000) + 100000)
        expires_at = now_utc + datetime.timedelta(minutes=10)
        
        if hasattr(user, 'otpCode'):
            db.user.update(
                where={"id": user.id},
                data={
                    "otpCode": otp_code,
                    "otpExpiresAt": expires_at,
                    "lastOtpSentAt": now_utc
                }
            )
        
        # Send OTP email asynchronously
        send_otp_email_async(email, otp_code)
        
        return jsonify({
            "success": True,
            "message": "A new 6-digit verification code has been sent to your email.",
            "cooldown": 60
        }), 200
        
    except Exception as e:
        print("Resend OTP Error:", str(e))
        return jsonify({"error": "Failed to resend code"}), 500

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json or {}
    
    email = data.get('email', '').strip().lower()
    password = data.get('password', '')
    
    if not email or not password:
        return jsonify({"error": "Missing required fields (email, password)"}), 400
        
    try:
        if not db.is_connected():
            db.connect()
            
        user = db.user.find_first(where={"email": email})
        
        if not user or not check_password_hash(user.passwordHash, password):
            return jsonify({"error": "Invalid email or password"}), 401
            
        # Security: Only block if isVerified is explicitly False
        is_verified = getattr(user, 'isVerified', True)
        if is_verified is False:
            now_utc = datetime.datetime.now(datetime.timezone.utc)
            should_send_new = True
            
            otp_exp = getattr(user, 'otpExpiresAt', None)
            otp_code = getattr(user, 'otpCode', None)
            if otp_exp and otp_code:
                exp = to_utc(otp_exp)
                if exp and now_utc < exp:
                    should_send_new = False
                    
            if should_send_new:
                otp_code = str(secrets.randbelow(900000) + 100000)
                if hasattr(user, 'otpCode'):
                    db.user.update(
                        where={"id": user.id},
                        data={
                            "otpCode": otp_code,
                            "otpExpiresAt": now_utc + datetime.timedelta(minutes=10),
                            "lastOtpSentAt": now_utc
                        }
                    )
                send_otp_email_async(user.email, otp_code)
                
            return jsonify({
                "error": "Account not verified. A verification code has been sent to your email.",
                "needsVerification": True,
                "email": user.email
            }), 403
            
        # Gamification: Update login streak & lastLogin
        now = datetime.datetime.now(datetime.timezone.utc)
        new_streak = getattr(user, 'loginStreak', 1) or 1
        
        last_login_val = getattr(user, 'lastLogin', None)
        if last_login_val:
            try:
                last_login_date = to_utc(last_login_val).date()
                delta = now.date() - last_login_date
                if delta.days == 1:
                    new_streak += 1
                elif delta.days > 1:
                    new_streak = 1
            except Exception as e:
                print("Date delta error:", e)
                new_streak = 1
        else:
            new_streak = 1
            
        try:
            user = db.user.update(
                where={"id": user.id},
                data={
                    "lastLogin": now,
                    "loginStreak": new_streak
                }
            )
        except Exception as e:
            print("Notice: login streak update bypassed:", e)
            
        # Generate JWT Token
        token = jwt.encode({
            'user_id': user.id,
            'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=30)
        }, SECRET_KEY, algorithm="HS256")
        
        return jsonify({
            "message": "Login successful",
            "token": token,
            "user": {
                "id": user.id,
                "username": (user.username or "").strip(),
                "email": user.email,
                "role": getattr(user, 'role', 'student') or 'student',
                "level": getattr(user, 'level', 1),
                "xp": getattr(user, 'xp', 0),
                "coins": getattr(user, 'coins', 0),
                "loginStreak": getattr(user, 'loginStreak', new_streak)
            }
        }), 200
        
    except Exception as e:
        print("Login Error:", str(e))
        return jsonify({"error": "Failed to log in"}), 500

@auth_bp.route('/me', methods=['GET'])
@token_required
def get_auth_me(current_user):
    """
    Returns current authenticated user details including role.
    """
    try:
        user = db.user.find_unique(where={"id": current_user.id}) or current_user
        resolved_name = (getattr(user, 'username', '') or getattr(user, 'name', '') or '').strip()
        role = getattr(user, 'role', 'student') or 'student'
        return jsonify({
            "id": user.id,
            "username": resolved_name,
            "name": resolved_name,
            "email": user.email,
            "role": role,
            "avatarUrl": getattr(user, 'avatarUrl', None),
            "avatar": getattr(user, 'avatarUrl', None),
            "location": getattr(user, 'location', 'Islamabad, PK') or 'Islamabad, PK',
            "headline": getattr(user, 'headline', 'Creative Technologist & Learner') or 'Creative Technologist & Learner',
            "level": getattr(user, 'level', 1),
            "xp": getattr(user, 'xp', 0),
            "coins": getattr(user, 'coins', 0),
            "loginStreak": getattr(user, 'loginStreak', 1),
            "totalZenMinutes": getattr(user, 'totalZenMinutes', 0)
        }), 200
    except Exception as e:
        print(f"Error fetching auth /me: {e}")
        return jsonify({"error": "Failed to fetch user profile"}), 500

@auth_bp.route('/forgot-password', methods=['POST'])
def forgot_password():
    """
    Initiates password reset by sending a 6-digit OTP code to the user's email.
    Uses generic response to protect against user enumeration attacks.
    """
    data = request.json or {}
    email = data.get('email', '').strip().lower()

    if not email:
        return jsonify({"error": "Email address is required"}), 400

    try:
        if not db.is_connected():
            db.connect()

        user = db.user.find_first(where={"email": email})
        now_utc = datetime.datetime.now(datetime.timezone.utc)

        if user:
            last_sent_val = getattr(user, 'lastOtpSentAt', None)
            if last_sent_val:
                last_sent = to_utc(last_sent_val)
                if last_sent:
                    elapsed = (now_utc - last_sent).total_seconds()
                    if elapsed < 30:
                        remaining = int(30 - elapsed)
                        return jsonify({
                            "error": f"Please wait {remaining}s before requesting a new code.",
                            "remainingCooldown": remaining
                        }), 429

            # Generate 6-digit OTP code
            otp_code = str(secrets.randbelow(900000) + 100000)
            expires_at = now_utc + datetime.timedelta(minutes=15)

            if hasattr(user, 'otpCode'):
                db.user.update(
                    where={"id": user.id},
                    data={
                        "otpCode": otp_code,
                        "otpExpiresAt": expires_at,
                        "lastOtpSentAt": now_utc
                    }
                )

            # Send OTP email asynchronously
            send_otp_email_async(email, otp_code)

        # Always return generic success response to prevent email harvesting/enumeration
        return jsonify({
            "success": True,
            "message": "If an account exists with this email, a 6-digit reset code has been sent.",
            "cooldown": 30
        }), 200

    except Exception as e:
        print("Forgot Password Error:", str(e))
        return jsonify({"error": "Failed to process password reset request"}), 500

@auth_bp.route('/verify-reset-otp', methods=['POST'])
def verify_reset_otp():
    """
    Verifies that the provided OTP for password reset is valid and unexpired.
    """
    data = request.json or {}
    email = data.get('email', '').strip().lower()
    otp = str(data.get('otp', '')).strip()

    if not email or not otp:
        return jsonify({"error": "Email and verification code are required"}), 400

    try:
        if not db.is_connected():
            db.connect()

        user = db.user.find_first(where={"email": email})
        if not user:
            return jsonify({"error": "Invalid verification code"}), 400

        stored_otp = getattr(user, 'otpCode', None)
        if not stored_otp or stored_otp.strip() != otp:
            return jsonify({"error": "Invalid verification code. Please check and try again."}), 400

        now_utc = datetime.datetime.now(datetime.timezone.utc)
        otp_exp = getattr(user, 'otpExpiresAt', None)
        expires_at = to_utc(otp_exp) if otp_exp else None

        if expires_at and now_utc > expires_at:
            return jsonify({"error": "Verification code has expired. Please request a new code."}), 400

        return jsonify({
            "success": True,
            "message": "Code verified successfully."
        }), 200

    except Exception as e:
        print("Verify Reset OTP Error:", str(e))
        return jsonify({"error": "Failed to verify code"}), 500

@auth_bp.route('/reset-password', methods=['POST'])
def reset_password():
    """
    Resets the user's password after validating the OTP.
    """
    data = request.json or {}
    email = data.get('email', '').strip().lower()
    otp = str(data.get('otp', '')).strip()
    new_password = data.get('newPassword', '')

    if not email or not otp or not new_password:
        return jsonify({"error": "Missing required fields (email, otp, newPassword)"}), 400

    if len(new_password) < 8:
        return jsonify({"error": "Password must be at least 8 characters long"}), 400

    try:
        if not db.is_connected():
            db.connect()

        user = db.user.find_first(where={"email": email})
        if not user:
            return jsonify({"error": "Invalid password reset request"}), 400

        stored_otp = getattr(user, 'otpCode', None)
        if not stored_otp or stored_otp.strip() != otp:
            return jsonify({"error": "Invalid or expired verification code"}), 400

        now_utc = datetime.datetime.now(datetime.timezone.utc)
        otp_exp = getattr(user, 'otpExpiresAt', None)
        expires_at = to_utc(otp_exp) if otp_exp else None

        if expires_at and now_utc > expires_at:
            return jsonify({"error": "Verification code has expired. Please request a new code."}), 400

        # Update password hash and clear OTP fields
        hashed = generate_password_hash(new_password)
        update_data = {"passwordHash": hashed}
        if hasattr(user, 'otpCode'):
            update_data["otpCode"] = None
        if hasattr(user, 'otpExpiresAt'):
            update_data["otpExpiresAt"] = None

        db.user.update(
            where={"id": user.id},
            data=update_data
        )

        return jsonify({
            "success": True,
            "message": "Password updated successfully! You can now log in with your new password."
        }), 200

    except Exception as e:
        print("Reset Password Error:", str(e))
        return jsonify({"error": "Failed to reset password"}), 500

