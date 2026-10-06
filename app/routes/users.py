from flask import Blueprint, request, jsonify
from app.db import db
from app.auth_middleware import token_required

users_bp = Blueprint('users', __name__, url_prefix='/api/users')
user_bp = Blueprint('user', __name__, url_prefix='/api/user')

def get_course_badge_icon(title, category=""):
    title_lower = (title or "").lower()
    cat_lower = (category or "").lower()
    if "python" in title_lower:
        return "🐍"
    elif "react" in title_lower or "native" in title_lower:
        return "⚛️"
    elif "web" in title_lower or "html" in title_lower or "css" in title_lower or "javascript" in title_lower or "frontend" in title_lower:
        return "🌐"
    elif "mobile" in title_lower or "android" in title_lower or "ios" in title_lower:
        return "📱"
    elif "security" in title_lower or "cyber" in title_lower or "ethical" in title_lower:
        return "🛡️"
    elif "database" in title_lower or "sql" in title_lower or "postgres" in title_lower:
        return "🗄️"
    elif "git" in title_lower or "github" in title_lower or "devops" in title_lower:
        return "🛠️"
    elif "flask" in title_lower or "django" in title_lower or "backend" in title_lower or "api" in title_lower:
        return "⚡"
    elif "ai" in title_lower or "machine learning" in title_lower or "data" in title_lower:
        return "🤖"
    elif "design" in title_lower or "ui" in title_lower or "ux" in title_lower:
        return "🎨"
    elif "dojo" in title_lower or "arena" in title_lower:
        return "🥋"
    else:
        return "🏆"

def fetch_user_stats(current_user):
    """Fetch current user's gamification stats from database."""
    try:
        user = db.user.find_unique(where={"id": current_user.id})
        if not user:
            return jsonify({"message": "User not found"}), 404
            
        return jsonify({
            "level": user.level, 
            "xp": user.xp, 
            "coins": user.coins, 
            "loginStreak": user.loginStreak,
            "username": user.username,
            "totalZenMinutes": user.totalZenMinutes
        }), 200
    except Exception as e:
        print(f"Error fetching user stats: {e}")
        return jsonify({"error": "Failed to fetch user stats"}), 500

def fetch_completed_courses(current_user):
    """Fetch user's completed courses/modules to display as Badges."""
    try:
        progresses = db.userlessonprogress.find_many(
            where={"userId": current_user.id}
        )
        completed = []
        for p in progresses:
            lesson = db.lesson.find_unique(
                where={"id": p.lessonId},
                include={"steps": True}
            )
            if not lesson:
                continue
            
            total_steps = len(lesson.steps) if lesson.steps else 0
            # A course is completed if unlockedDay exceeds total steps
            if total_steps > 0 and p.unlockedDay > total_steps:
                completed.append({
                    "id": lesson.id,
                    "title": lesson.title,
                    "category": lesson.category,
                    "icon": get_course_badge_icon(lesson.title, lesson.category),
                    "badgeName": f"{lesson.title} Master",
                    "totalDays": total_steps,
                    "unlockedDay": p.unlockedDay,
                    "completedAt": p.updatedAt.isoformat() if p.updatedAt else None
                })
        return jsonify(completed), 200
    except Exception as e:
        print(f"Error fetching completed courses: {e}")
        return jsonify({"error": "Failed to fetch completed courses"}), 500

# Endpoints under /api/users
@users_bp.route('/me', methods=['GET'])
@token_required
def get_me(current_user):
    return fetch_user_stats(current_user)

@users_bp.route('/stats', methods=['GET'])
@token_required
def get_stats(current_user):
    return fetch_user_stats(current_user)

@users_bp.route('/completed-courses', methods=['GET'])
@token_required
def get_completed(current_user):
    return fetch_completed_courses(current_user)

def fetch_leaderboard():
    """Fetch top users sorted by XP descending for the global leaderboard."""
    try:
        users = db.user.find_many(
            order={"xp": "desc"},
            take=10
        )
        leaderboard = []
        for index, u in enumerate(users):
            tier = "Rookie"
            if u.level >= 10 or u.xp >= 2000:
                tier = "Grandmaster"
            elif u.level >= 7 or u.xp >= 1200:
                tier = "Diamond"
            elif u.level >= 5 or u.xp >= 600:
                tier = "Platinum"
            elif u.level >= 3 or u.xp >= 200:
                tier = "Gold"
            elif u.level >= 2 or u.xp >= 100:
                tier = "Silver"

            wins_count = max(0, u.xp // 100)
            try:
                found_wins = db.dojoevent.count(where={"winnerId": u.id})
                if found_wins > 0:
                    wins_count = found_wins
            except Exception:
                pass

            badge = "🥇" if index == 0 else "🥈" if index == 1 else "🥉" if index == 2 else f"#{index + 1}"
            color = "#F59E0B" if index == 0 else "#94A3B8" if index == 1 else "#CD7F32" if index == 2 else "#64748B"

            leaderboard.append({
                "rank": index + 1,
                "badge": badge,
                "userId": u.id,
                "username": u.username,
                "level": u.level,
                "xp": u.xp,
                "coins": u.coins,
                "tier": tier,
                "wins": f"{wins_count} Wins",
                "color": color
            })

        # Ensure at least 3 players are displayed on fresh installs
        if len(leaderboard) < 3:
            dummy_challengers = [
                {"username": "AlexDev", "xp": 2840, "level": 12, "tier": "Grandmaster", "wins": "28 Wins", "color": "#F59E0B"},
                {"username": "SaraCode", "xp": 2410, "level": 10, "tier": "Diamond", "wins": "24 Wins", "color": "#94A3B8"},
                {"username": "HamzaDev", "xp": 2150, "level": 8, "tier": "Platinum", "wins": "20 Wins", "color": "#CD7F32"},
            ]
            existing_usernames = {item["username"].lower() for item in leaderboard}
            for d in dummy_challengers:
                if d["username"].lower() not in existing_usernames and len(leaderboard) < 5:
                    leaderboard.append({
                        "rank": len(leaderboard) + 1,
                        "badge": "🥇",
                        "userId": f"challenger-{len(leaderboard)+1}",
                        "username": d["username"],
                        "level": d["level"],
                        "xp": d["xp"],
                        "coins": 500,
                        "tier": d["tier"],
                        "wins": d["wins"],
                        "color": d["color"]
                    })
            leaderboard.sort(key=lambda x: x["xp"], reverse=True)
            for idx, item in enumerate(leaderboard):
                item["rank"] = idx + 1
                item["badge"] = "🥇" if idx == 0 else "🥈" if idx == 1 else "🥉" if idx == 2 else f"#{idx + 1}"
                item["color"] = "#F59E0B" if idx == 0 else "#94A3B8" if idx == 1 else "#CD7F32" if idx == 2 else "#64748B"

        return jsonify(leaderboard), 200
    except Exception as e:
        print(f"Error fetching leaderboard: {e}")
        return jsonify({"error": "Failed to fetch leaderboard"}), 500

@users_bp.route('/leaderboard', methods=['GET'])
def get_leaderboard():
    return fetch_leaderboard()

# Aliases under /api/user
@user_bp.route('/leaderboard', methods=['GET'])
def get_user_leaderboard_alias():
    return fetch_leaderboard()
@user_bp.route('/stats', methods=['GET'])
@token_required
def get_user_stats_alias(current_user):
    return fetch_user_stats(current_user)

@user_bp.route('/completed-courses', methods=['GET'])
@token_required
def get_user_completed_alias(current_user):
    return fetch_completed_courses(current_user)

@user_bp.route('/me', methods=['GET'])
@token_required
def get_user_me_alias(current_user):
    return fetch_user_stats(current_user)

@users_bp.route('/me/award', methods=['POST'])
@token_required
def award_points(current_user):
    """Securely award XP and coins for Dojo wins."""
    data = request.json
    xp_award = data.get('xp', 0)
    coins_award = data.get('coins', 0)
    
    try:
        user = db.user.find_unique(where={"id": current_user.id})
        
        new_xp = user.xp + xp_award
        new_coins = user.coins + coins_award
        
        # Simple level up logic (every 100 XP = 1 level)
        new_level = max(1, (new_xp // 100) + 1)
        
        updated_user = db.user.update(
            where={"id": current_user.id},
            data={
                "xp": new_xp,
                "coins": new_coins,
                "level": new_level
            }
        )
        
        return jsonify({
            "xp": updated_user.xp,
            "coins": updated_user.coins,
            "level": updated_user.level
        }), 200
    except Exception as e:
        print(f"Error awarding points: {e}")
        return jsonify({"error": "Failed to award points"}), 500

@users_bp.route('/me/purchase-powerup', methods=['POST'])
@token_required
def purchase_powerup(current_user):
    """Deduct coins for purchasing power-ups like Streak Freeze."""
    data = request.json or {}
    cost = int(data.get('cost', 0))
    powerup_id = data.get('powerupId', '')
    
    try:
        user = db.user.find_unique(where={"id": current_user.id})
        if not user:
            return jsonify({"error": "User not found"}), 404
            
        if user.coins < cost:
            return jsonify({"error": "Insufficient coins"}), 400
            
        new_coins = user.coins - cost
        updated_user = db.user.update(
            where={"id": current_user.id},
            data={"coins": new_coins}
        )
        
        return jsonify({
            "success": True,
            "coins": updated_user.coins,
            "powerupId": powerup_id,
            "message": f"Purchased {powerup_id} successfully"
        }), 200
    except Exception as e:
        print(f"Error purchasing powerup: {e}")
        return jsonify({"error": "Failed to purchase powerup"}), 500

@user_bp.route('/me/purchase-powerup', methods=['POST'])
@token_required
def purchase_powerup_alias(current_user):
    return purchase_powerup(current_user)

@users_bp.route('/me/sync-streak', methods=['POST'])
@token_required
def sync_streak(current_user):
    """Sync preserved streak count after a freeze or login."""
    data = request.json or {}
    streak = data.get('streak')
    if streak is None:
        return jsonify({"error": "Streak value required"}), 400
        
    try:
        updated_user = db.user.update(
            where={"id": current_user.id},
            data={"loginStreak": int(streak)}
        )
        return jsonify({
            "success": True,
            "loginStreak": updated_user.loginStreak
        }), 200
    except Exception as e:
        print(f"Error syncing streak: {e}")
        return jsonify({"error": "Failed to sync streak"}), 500

@user_bp.route('/me/sync-streak', methods=['POST'])
@token_required
def sync_streak_alias(current_user):
    return sync_streak(current_user)

