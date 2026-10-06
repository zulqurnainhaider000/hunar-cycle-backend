from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
import os
from app.db import db

auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')
SECRET_KEY = os.environ.get('SECRET_KEY', 'hunarcircle_super_secret_jwt_key_2026')

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    
    if not data or 'username' not in data or 'email' not in data or 'password' not in data:
        return jsonify({"error": "Missing required fields (username, email, password)"}), 400
        
    try:
        email = data['email'].lower()
        
        # Pre-check if email already exists
        existing_email = db.user.find_first(where={"email": email})
        if existing_email:
            return jsonify({"error": "Email is already registered"}), 400
            
        # Check if username already exists
        existing_username = db.user.find_first(where={"username": data['username']})
        if existing_username:
            return jsonify({"error": "Username already exists"}), 409
            
        # Hash the password
        hashed_password = generate_password_hash(data['password'])
        
        # Create user in DB
        new_user = db.user.create(data={
            "username": data['username'],
            "email": email,
            "passwordHash": hashed_password,
            "lastLogin": datetime.datetime.utcnow(),
            "loginStreak": 1,
            "coins": 1000
        })
        
        # Generate JWT token immediately upon registration
        token = jwt.encode({
            'user_id': new_user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=30)
        }, SECRET_KEY, algorithm="HS256")
        
        return jsonify({
            "message": "User registered successfully",
            "token": token,
            "user": {
                "id": new_user.id,
                "username": new_user.username,
                "email": new_user.email
            }
        }), 201
        
    except Exception as e:
        print("Registration Error:", str(e))
        return jsonify({"error": "Failed to register user"}), 500

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    
    if not data or 'email' not in data or 'password' not in data:
        return jsonify({"error": "Missing required fields (email, password)"}), 400
        
    try:
        email = data['email'].lower()
        user = db.user.find_first(where={"email": email})
        
        if not user or not check_password_hash(user.passwordHash, data['password']):
            return jsonify({"error": "Invalid email or password"}), 401
            
        # Gamification: Update login streak
        now = datetime.datetime.utcnow()
        new_streak = user.loginStreak
        
        if user.lastLogin:
            # Need to handle timezone-aware vs naive datetimes
            # assuming both are UTC naive or aware here
            try:
                delta = now.date() - user.lastLogin.date()
                if delta.days == 1:
                    new_streak += 1
                elif delta.days > 1:
                    new_streak = 1
            except Exception as e:
                print("Date delta error:", e)
                new_streak = 1
        else:
            new_streak = 1
            
        user = db.user.update(
            where={"id": user.id},
            data={
                "lastLogin": now,
                "loginStreak": new_streak
            }
        )
            
        # Generate JWT Token
        token = jwt.encode({
            'user_id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=30)
        }, SECRET_KEY, algorithm="HS256")
        
        return jsonify({
            "message": "Login successful",
            "token": token,
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "level": user.level,
                "xp": user.xp,
                "coins": user.coins,
                "loginStreak": user.loginStreak
            }
        }), 200
        
    except Exception as e:
        print("Login Error:", str(e))
        return jsonify({"error": "Failed to log in"}), 500
