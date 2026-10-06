from flask import Blueprint, request, jsonify
import random
import time

dojos_bp = Blueprint('dojos', __name__, url_prefix='/api/dojos')

@dojos_bp.route('/match', methods=['POST'])
def matchmake_dojo():
    """
    Simulate finding an opponent for a Dojo challenge.
    Expects JSON: { category: 'PYTHON_DEBUG' }
    """
    data = request.json
    category = data.get('category') if data else None
    
    if not category:
        return jsonify({"error": "Dojo category is required"}), 400

    # Simulate matchmaking delay
    time.sleep(1)
    
    # Mock finding an opponent
    opponent_names = ["CodeWizard99", "MedStudent_X", "TypeRacer2000"]
    opponent = random.choice(opponent_names)
    
    # Return match session details
    return jsonify({
        "message": "Opponent found!",
        "session": {
            "sessionId": "session-789",
            "category": category,
            "opponent": opponent,
            "startingScore": 0,
            "duration": 120 # 2 minutes
        }
    }), 200
