from flask import Blueprint, jsonify
from app.services.economy import get_system_config

economy_bp = Blueprint('economy', __name__, url_prefix='/api/economy')

@economy_bp.route('/config', methods=['GET'])
def get_public_economy_config():
    """
    Returns live economy rates for mobile app gamification.
    Lightweight, cached for 60 seconds.
    """
    try:
        config = get_system_config()
        response = jsonify({
            "success": True,
            "config": config
        })
        response.headers['Cache-Control'] = 'public, max-age=60'
        return response, 200
    except Exception as e:
        print(f"[Economy Route] Error: {e}")
        return jsonify({"success": False, "error": "Failed to fetch economy config"}), 500
