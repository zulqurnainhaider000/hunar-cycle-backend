from flask import Blueprint, request, jsonify
from app.db import db
from app.auth_middleware import token_required

gigs_bp = Blueprint('gigs', __name__, url_prefix='/api/gigs')

@gigs_bp.route('', methods=['GET'])
@token_required
def get_gigs(current_user):
    """
    Fetch all available gigs from PostgreSQL.
    """
    try:
        gigs = db.gig.find_many(
            include={'poster': True},
            order={'createdAt': 'desc'}
        )
        return jsonify({
            "data": [
                {
                    "id": gig.id,
                    "title": gig.title,
                    "description": gig.description,
                    "category": gig.category,
                    "rewardCoins": gig.rewardCoins,
                    "status": gig.status,
                    "posterId": gig.posterId,
                    "posterName": gig.poster.username if gig.poster else "Anonymous"
                } for gig in gigs
            ]
        }), 200
    except Exception as e:
        print("Error fetching gigs:", str(e))
        return jsonify({"error": "Failed to fetch gigs"}), 500

@gigs_bp.route('/<gig_id>', methods=['GET'])
@token_required
def get_gig_by_id(current_user, gig_id):
    """
    Fetch a specific gig by ID.
    """
    try:
        gig = db.gig.find_unique(
            where={'id': gig_id},
            include={'poster': True, 'acceptedBy': True}
        )
        if not gig:
            return jsonify({"error": "Gig not found"}), 404
            
        return jsonify({
            "data": {
                "id": gig.id,
                "title": gig.title,
                "description": gig.description,
                "category": gig.category,
                "rewardCoins": gig.rewardCoins,
                "status": gig.status,
                "posterId": gig.posterId,
                "posterName": gig.poster.username if gig.poster else "Anonymous",
                "acceptedById": gig.acceptedById,
                "acceptedByName": gig.acceptedBy.username if gig.acceptedBy else None
            }
        }), 200
    except Exception as e:
        print("Error fetching gig:", str(e))
        return jsonify({"error": "Failed to fetch gig"}), 500

@gigs_bp.route('', methods=['POST'])
@token_required
def create_gig(current_user):
    """
    Create a new gig request and save to PostgreSQL.
    """
    data = request.json
    
    if not data or 'title' not in data or 'description' not in data:
        return jsonify({"error": "Missing required fields (title, description)"}), 400
        
    try:
        # Use the authenticated user's ID
        poster_id = current_user.id
            
        new_gig = db.gig.create(
            data={
                "title": data['title'],
                "description": data['description'],
                "category": data.get('category', 'GENERAL'),
                "rewardCoins": data.get('rewardCoins', 0),
                "status": "OPEN",
                "posterId": poster_id
            },
            include={'poster': True}
        )
        
        return jsonify({
            "message": "Gig created successfully!",
            "data": {
                "id": new_gig.id,
                "title": new_gig.title,
                "description": new_gig.description,
                "category": new_gig.category,
                "rewardCoins": new_gig.rewardCoins,
                "status": new_gig.status,
                "posterId": new_gig.posterId,
                "posterName": new_gig.poster.username if new_gig.poster else "Anonymous"
            }
        }), 201
    except Exception as e:
        print("Error creating gig:", str(e))
        return jsonify({"error": "Failed to create gig"}), 500

@gigs_bp.route('/<gig_id>/accept', methods=['POST'])
@token_required
def accept_gig(current_user, gig_id):
    """
    Accept a gig request.
    """
    try:
        # 1. Fetch the gig
        gig = db.gig.find_unique(where={'id': gig_id})
        if not gig:
            return jsonify({"error": "Gig not found"}), 404
            
        # 2. Validations
        if gig.status != "OPEN":
            return jsonify({"error": "Gig is no longer open for acceptance"}), 400
            
        if gig.posterId == current_user.id:
            return jsonify({"error": "You cannot accept your own gig"}), 403
            
        # 3. Update the gig
        updated_gig = db.gig.update(
            where={'id': gig_id},
            data={
                'status': 'IN_PROGRESS',
                'acceptedById': current_user.id
            },
            include={'poster': True, 'acceptedBy': True}
        )
        
        return jsonify({
            "message": "Gig accepted successfully!",
            "data": {
                "id": updated_gig.id,
                "title": updated_gig.title,
                "status": updated_gig.status,
                "acceptedById": updated_gig.acceptedById,
                "acceptedByName": updated_gig.acceptedBy.username if updated_gig.acceptedBy else None
            }
        }), 200
        
    except Exception as e:
        print("Error accepting gig:", str(e))
        return jsonify({"error": "Failed to accept gig"}), 500

@gigs_bp.route('/<gig_id>/complete', methods=['POST'])
@token_required
def complete_gig(current_user, gig_id):
    """
    Mark a gig as COMPLETED and process the coin/XP transactions.
    """
    try:
        gig = db.gig.find_unique(
            where={'id': gig_id},
            include={'acceptedBy': True}
        )
        if not gig:
            return jsonify({"error": "Gig not found"}), 404
            
        if gig.posterId != current_user.id:
            return jsonify({"error": "Only the gig creator can mark it as completed"}), 403
            
        if gig.status != "IN_PROGRESS":
            return jsonify({"error": "Gig must be IN_PROGRESS to complete it"}), 400
            
        if not gig.acceptedById or not gig.acceptedBy:
            return jsonify({"error": "Gig has not been accepted by anyone"}), 400
            
        if current_user.coins < gig.rewardCoins:
            return jsonify({"error": f"Insufficient coins. You need {gig.rewardCoins} coins to complete this gig."}), 400
            
        accepted_user = gig.acceptedBy
        new_xp = accepted_user.xp + 50
        levels_gained = new_xp // 100
        remaining_xp = new_xp % 100
        
        with db.tx() as transaction:
            updated_gig = transaction.gig.update(
                where={'id': gig_id},
                data={'status': 'COMPLETED'},
                include={'poster': True, 'acceptedBy': True}
            )
            
            transaction.user.update(
                where={'id': current_user.id},
                data={'coins': {'decrement': gig.rewardCoins}}
            )
            
            updated_accepted_user = transaction.user.update(
                where={'id': gig.acceptedById},
                data={
                    'coins': {'increment': gig.rewardCoins},
                    'xp': remaining_xp,
                    'level': {'increment': levels_gained}
                }
            )
            
        return jsonify({
            "message": "Gig marked as completed successfully!",
            "gig": {
                "id": updated_gig.id,
                "status": updated_gig.status
            },
            "acceptedUser": {
                "id": updated_accepted_user.id,
                "coins": updated_accepted_user.coins,
                "xp": updated_accepted_user.xp,
                "level": updated_accepted_user.level
            }
        }), 200
        
    except Exception as e:
        print("Error completing gig:", str(e))
        return jsonify({"error": "Failed to complete gig"}), 500

@gigs_bp.route('/<gig_id>/solve', methods=['POST'])
@token_required
def solve_gig(current_user, gig_id):
    """
    Solve a freelance simulator gig and payout reward coins/XP to current_user.
    """
    try:
        data = request.json or {}
        coins_reward = int(data.get('rewardCoins', 200))
        xp_reward = int(data.get('rewardXp', 50))

        try:
            db.gig.update_many(
                where={'id': gig_id},
                data={'status': 'COMPLETED', 'acceptedById': current_user.id}
            )
        except Exception:
            pass

        user = db.user.find_unique(where={"id": current_user.id})
        if not user:
            return jsonify({"error": "User not found"}), 404

        new_coins = user.coins + coins_reward
        new_xp = user.xp + xp_reward
        new_level = max(1, (new_xp // 100) + 1)

        updated_user = db.user.update(
            where={"id": current_user.id},
            data={
                "coins": new_coins,
                "xp": new_xp,
                "level": new_level
            }
        )

        return jsonify({
            "message": "Client satisfied! Payment released.",
            "coins": updated_user.coins,
            "xp": updated_user.xp,
            "level": updated_user.level,
            "earnedCoins": coins_reward,
            "earnedXp": xp_reward
        }), 200
    except Exception as e:
        print("Error solving gig:", str(e))
        return jsonify({"error": "Failed to complete gig"}), 500
