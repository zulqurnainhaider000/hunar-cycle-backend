from flask import Blueprint, request, jsonify
from app.db import db
from app.auth_middleware import token_required

hub_bp = Blueprint('hub', __name__, url_prefix='/api/hub')

@hub_bp.route('/events', methods=['GET'])
@token_required
def get_events(current_user):
    try:
        events = db.event.find_many(
            include={
                "attendees": True
            },
            order={"date": "asc"}
        )
        
        # Serialize
        events_data = []
        for e in events:
            events_data.append({
                "id": e.id,
                "title": e.title,
                "description": e.description,
                "location": e.location,
                "date": e.date.isoformat(),
                "color": e.color,
                "attendeeCount": len(e.attendees),
                "isAttending": any(u.id == current_user.id for u in e.attendees)
            })
            
        return jsonify(events_data), 200
    except Exception as e:
        print(f"Error fetching events: {e}")
        return jsonify({"error": "Internal server error"}), 500

@hub_bp.route('/events/<event_id>/rsvp', methods=['POST'])
@token_required
def rsvp_event(current_user, event_id):
    try:
        # Check if already attending to toggle
        event = db.event.find_unique(where={"id": event_id}, include={"attendees": True})
        if not event:
            return jsonify({"error": "Event not found"}), 404
            
        is_attending = any(u.id == current_user.id for u in event.attendees)
        
        if is_attending:
            # Disconnect
            db.event.update(
                where={"id": event_id},
                data={
                    "attendees": {
                        "disconnect": [{"id": current_user.id}]
                    }
                }
            )
            return jsonify({"message": "Un-RSVP successful", "attending": False}), 200
        else:
            # Connect
            db.event.update(
                where={"id": event_id},
                data={
                    "attendees": {
                        "connect": [{"id": current_user.id}]
                    }
                }
            )
            return jsonify({"message": "RSVP successful", "attending": True}), 200
            
    except Exception as e:
        print(f"Error RSVPing: {e}")
        return jsonify({"error": "Failed to RSVP"}), 500

@hub_bp.route('/turfs', methods=['GET'])
@token_required
def get_turfs(current_user):
    try:
        turfs = db.turf.find_many(
            include={
                "members": True
            }
        )
        
        # Serialize
        turfs_data = []
        for t in turfs:
            turfs_data.append({
                "id": t.id,
                "name": t.name,
                "description": t.description,
                "color": t.color,
                "memberCount": len(t.members)
            })
            
        return jsonify(turfs_data), 200
    except Exception as e:
        print(f"Error fetching turfs: {e}")
        return jsonify({"error": "Internal server error"}), 500
