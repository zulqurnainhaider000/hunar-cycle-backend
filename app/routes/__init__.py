from flask import Blueprint

# Core API Blueprints (Skeleton for remaining modules)
auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')
learn_bp = Blueprint('learn', __name__, url_prefix='/api/learn')
matches_bp = Blueprint('matches', __name__, url_prefix='/api/matches')
hub_bp = Blueprint('hub', __name__, url_prefix='/api/hub')
zen_bp = Blueprint('zen', __name__, url_prefix='/api/zen')

@learn_bp.route('/audio-lessons', methods=['GET'])
def get_audio_lessons():
    return {"message": "Audio lessons endpoint"}

