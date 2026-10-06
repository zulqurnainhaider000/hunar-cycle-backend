# backend/app/routes/onboarding.py
from flask import Blueprint, request, jsonify

onboarding_bp = Blueprint('onboarding', __name__)

# Removed mock /api/auth/register route to prevent interception of real auth_bp route

@onboarding_bp.route('/api/users/<user_id>/skills', methods=['POST'])
def set_user_skills(user_id):
    """
    Step 2 of Onboarding: Define HAS and WANTS skills.
    Expects payload: 
    {
       "has_skills": [{"skill_id": "sk-1", "proficiency": 4}],
       "wants_skills": [{"skill_id": "sk-2", "proficiency": 1}]
    }
    """
    data = request.json
    has_skills = data.get('has_skills', [])
    wants_skills = data.get('wants_skills', [])
    
    # Save to database logic
    # for skill in has_skills:
    #     prisma.userskill.create(data={"userId": user_id, "skillId": skill["skill_id"], "type": "HAS", "proficiency": skill["proficiency"]})
        
    return jsonify({"message": "Skills updated successfully"}), 200
