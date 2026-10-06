import os
import jwt
from functools import wraps
from flask import request, jsonify
from app.db import db

# Use a secure secret key from environment variables in production
SECRET_KEY = os.environ.get('SECRET_KEY', 'hunarcircle_super_secret_jwt_key_2026')

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
                
            # Pass the current_user object to the protected route
            # Wait, we must execute the route OUTSIDE the try-except block!
            pass
            
        except Exception as e:
            print(f"Token decoding error: {e}")
            return jsonify({"message": "Invalid token"}), 401
            
    # Execute the route handler outside the try-except block
    # so that any exceptions thrown by the route are correctly propagated as 500s 
    # instead of being swallowed and masked as 401 Unauthorized token errors.
        return f(current_user, *args, **kwargs)
        
    return decorated
