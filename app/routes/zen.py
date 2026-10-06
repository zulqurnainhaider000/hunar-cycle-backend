from flask import Blueprint, request, jsonify
from app.db import db
from app.auth_middleware import token_required
import random

zen_bp = Blueprint('zen', __name__, url_prefix='/api/zen')

QUOTES = [
    "Take a breath, Ninja. Rest is part of the work.",
    "A sharp axe cuts twice as fast. Sharpen your mind.",
    "Focus on the present moment. The code will wait.",
    "Hydration and breathing solve more bugs than caffeine.",
    "You are more than your output. Breathe deeply."
]

@zen_bp.route('', methods=['GET'])
@token_required
def get_zen(current_user):
    try:
        # Fetch current user to get up-to-date zen minutes and streak
        user = db.user.find_unique(where={"id": current_user.id})
        
        return jsonify({
            "quote": random.choice(QUOTES),
            "totalZenMinutes": user.totalZenMinutes,
            "loginStreak": user.loginStreak
        }), 200
    except Exception as e:
        print(f"Error fetching zen data: {e}")
        return jsonify({"error": "Internal server error"}), 500

@zen_bp.route('/complete', methods=['POST'])
@token_required
def complete_zen(current_user):
    try:
        data = request.get_json() or {}
        minutes = int(data.get('minutes', 25))
        
        # Award 50 XP and 20 Coins for Pomodoro completion
        xp_gained = int(data.get('xp', 50))
        coins_gained = int(data.get('coins', 20))
        
        user = db.user.find_unique(where={"id": current_user.id})
        if not user:
            return jsonify({"error": "User not found"}), 404

        new_xp = user.xp + xp_gained
        new_coins = user.coins + coins_gained
        new_zen = (user.totalZenMinutes or 0) + minutes
        
        # Consistent Level calculation (every 100 XP = 1 level)
        new_level = max(1, (new_xp // 100) + 1)
            
        updated_user = db.user.update(
            where={"id": current_user.id},
            data={
                "xp": new_xp,
                "coins": new_coins,
                "level": new_level,
                "totalZenMinutes": new_zen
            }
        )
        
        return jsonify({
            "message": "Focus session completed successfully!",
            "xpGained": xp_gained,
            "coinsGained": coins_gained,
            "totalZenMinutes": updated_user.totalZenMinutes,
            "level": updated_user.level,
            "xp": updated_user.xp,
            "coins": updated_user.coins
        }), 200
    except Exception as e:
        print(f"Error completing zen: {e}")
        return jsonify({"error": "Internal server error"}), 500
