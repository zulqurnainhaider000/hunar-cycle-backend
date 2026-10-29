import os
import jwt
from functools import wraps
from flask import request, jsonify
from app.db import db

# Use a secure secret key from environment variables in production
SECRET_KEY = os.environ.get('SECRET_KEY') or os.environ.get('JWT_SECRET', 'hunarcircle_super_secret_jwt_key_2026')
ADMIN_KEY = os.environ.get('ADMIN_KEY', 'hunar_admin_secret_2026')
ADMIN_EMAILS = [
    e.strip().lower()
    for e in os.environ.get(
        'ADMIN_EMAILS',
        'zulqurnainhaider000@gmail.com,admin@hunarcircle.com,admin@hunarcycle.com'
    ).split(',')
    if e.strip()
]

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            token = None
            
            if 'Authorization' in request.headers:
                auth_header = request.headers.get('Authorization', '')
                parts = auth_header.split()
                if len(parts) == 2 and parts[0].lower() == 'bearer':
                    token = parts[1]
            
            if not token:
                return jsonify({"message": "Invalid token"}), 401
                
            # Decode the JWT
            data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            # Fetch the user from the database to ensure they still exist
            current_user = db.user.find_first(where={"id": data['user_id']})
            
            if not current_user:
                return jsonify({"message": "Invalid token"}), 401
                
        except Exception as e:
            print(f"Token decoding error: {e}")
            return jsonify({"message": "Invalid token"}), 401
            
        return f(current_user, *args, **kwargs)
        
    return decorated

def optional_token(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        current_user = None
        try:
            token = None
            if 'Authorization' in request.headers:
                auth_header = request.headers.get('Authorization', '')
                parts = auth_header.split()
                if len(parts) == 2 and parts[0].lower() == 'bearer':
                    token = parts[1]
            if token:
                data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
                if 'user_id' in data:
                    current_user = db.user.find_first(where={"id": data['user_id']})
        except Exception:
            current_user = None
        return f(current_user, *args, **kwargs)
    return decorated

def admin_required(f):

    """
    Restricts access strictly to verified admin accounts or authorized admin keys.
    Supports:
    1. X-Admin-Key header matching ADMIN_KEY
    2. JWT Bearer token with admin claim or matching ADMIN_EMAILS
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        # 1. Check X-Admin-Key header
        admin_key_header = request.headers.get('X-Admin-Key', '').strip()
        if admin_key_header and admin_key_header == ADMIN_KEY:
            class MockAdminUser:
                id = "admin-system-key"
                username = "System Admin"
                email = "admin@hunarcircle.com"
                isVerified = True
                role = "ADMIN"
            return f(MockAdminUser(), *args, **kwargs)

        # 2. Check Bearer token
        token = None
        if 'Authorization' in request.headers:
            auth_header = request.headers.get('Authorization', '')
            parts = auth_header.split()
            if len(parts) == 2 and parts[0].lower() == 'bearer':
                token = parts[1]

        if not token:
            return jsonify({
                "error": "Admin authentication required. Provide Bearer token or X-Admin-Key."
            }), 401

        try:
            data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])

            # Explicit admin token flag
            if data.get('admin') is True or data.get('role') == 'ADMIN':
                class TokenAdminUser:
                    id = data.get('user_id', 'admin-token')
                    username = data.get('username', 'Admin')
                    email = data.get('email', 'admin@hunarcircle.com')
                    isVerified = True
                    role = "ADMIN"
                return f(TokenAdminUser(), *args, **kwargs)

            # Query database for user
            user_id = data.get('user_id')
            if not user_id:
                return jsonify({"error": "Invalid token structure"}), 401

            user = db.user.find_first(where={"id": user_id})
            if not user:
                return jsonify({"error": "Admin account not found"}), 401

            user_email = (user.email or '').strip().lower()
            user_name = (user.username or '').strip().lower()

            if user_email in ADMIN_EMAILS or user_name == 'admin' or user_email.startswith('admin@'):
                user.role = "ADMIN"
                return f(user, *args, **kwargs)

            return jsonify({
                "error": "Access denied: Authorized administrator privileges required."
            }), 403

        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Admin session expired. Please log in again."}), 401
        except Exception as e:
            print(f"Admin auth error: {e}")
            return jsonify({"error": "Invalid admin token"}), 401

    return decorated
