import os
import json
import datetime
import re
import jwt
from flask import Blueprint, request, jsonify, Response
from werkzeug.security import check_password_hash

from app.db import db
from app.auth_middleware import admin_required, SECRET_KEY, ADMIN_KEY, ADMIN_EMAILS
from app.services.economy import get_system_config, update_system_config, grant_student_reward, grant_bulk_reward

admin_bp = Blueprint('admin', __name__, url_prefix='/api/admin')
admin_web_bp = Blueprint('admin_web', __name__)

def to_utc(dt):
    if dt is None:
        return None
    if isinstance(dt, str):
        try:
            # Handle ISO formats e.g. 2026-10-21T16:30:00Z or standard formats
            dt = datetime.datetime.fromisoformat(dt.replace('Z', '+00:00'))
        except Exception:
            return None
    if getattr(dt, 'tzinfo', None) is None:
        return dt.replace(tzinfo=datetime.timezone.utc)
    return dt.astimezone(datetime.timezone.utc)

def format_iso(val):
    if not val:
        return None
    if hasattr(val, 'isoformat'):
        return val.isoformat()
    return str(val)


# --------------------------------------------------------------------------
# 1. ADMIN AUTHENTICATION
# --------------------------------------------------------------------------
@admin_bp.route('/login', methods=['POST'])
def admin_login():
    """
    Dedicated admin login.
    Supports either:
    1. { "adminKey": "..." }
    2. { "email": "...", "password": "..." } (must be an authorized admin email)
    """
    data = request.json or {}
    admin_key = data.get('adminKey', '').strip()
    email = data.get('email', '').strip().lower()
    password = data.get('password', '')

    # 1. Direct Admin Key login
    if admin_key:
        if admin_key == ADMIN_KEY:
            token = jwt.encode({
                'user_id': 'admin-system',
                'username': 'System Administrator',
                'email': 'admin@hunarcircle.com',
                'admin': True,
                'role': 'ADMIN',
                'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=7)
            }, SECRET_KEY, algorithm="HS256")
            return jsonify({
                "success": True,
                "token": token,
                "admin": {
                    "id": "admin-system",
                    "username": "System Administrator",
                    "email": "admin@hunarcircle.com",
                    "role": "ADMIN"
                }
            }), 200
        else:
            return jsonify({"error": "Invalid Admin Secret Key"}), 401

    # 2. Email & Password login
    if email and password:
        if email not in ADMIN_EMAILS and not email.startswith('admin@'):
            return jsonify({"error": "This account is not authorized for Admin access"}), 403

        user = db.user.find_first(where={"email": email})
        if not user or not check_password_hash(user.passwordHash, password):
            return jsonify({"error": "Invalid email or password"}), 401

        token = jwt.encode({
            'user_id': user.id,
            'username': user.username,
            'email': user.email,
            'admin': True,
            'role': 'ADMIN',
            'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=7)
        }, SECRET_KEY, algorithm="HS256")

        return jsonify({
            "success": True,
            "token": token,
            "admin": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "role": "ADMIN"
            }
        }), 200

    return jsonify({"error": "Please provide an Admin Secret Key or email & password"}), 400

@admin_bp.route('/me', methods=['GET'])
@admin_required
def admin_me(current_admin):
    """Verify admin token and return current admin profile."""
    return jsonify({
        "id": getattr(current_admin, 'id', 'admin-id'),
        "username": getattr(current_admin, 'username', 'Admin'),
        "email": getattr(current_admin, 'email', 'admin@hunarcircle.com'),
        "role": "ADMIN",
        "isVerified": getattr(current_admin, 'isVerified', True)
    }), 200

# --------------------------------------------------------------------------
# 2. ADMIN STATS & ANALYTICS
# --------------------------------------------------------------------------
@admin_bp.route('/stats', methods=['GET'])
@admin_required
def get_admin_stats(current_admin):
    """
    Returns platform-wide metrics:
    - total users, verified users, verified percentage
    - total courses, 9 university courses
    - total quizzes, total flashcards, total lesson steps
    - active users (30d), total certificates completed
    - registration timeline for charts
    """
    try:
        now_utc = datetime.datetime.now(datetime.timezone.utc)
        raw_total_users = db.query_raw('SELECT COUNT(*) as count FROM "User"')
        total_users = raw_total_users[0]['count'] if raw_total_users else 0

        raw_verified = db.query_raw('SELECT COUNT(*) as count FROM "User" WHERE "isVerified" = true')
        verified_users = raw_verified[0]['count'] if raw_verified else 0
        verified_percentage = round((verified_users / max(1, total_users)) * 100, 1)

        total_courses = db.lesson.count()
        uni_courses_count = db.lesson.count(where={"category": {"in": ["University", "University Courses"]}})

        total_quizzes = db.quiz.count()
        total_flashcards = db.flashcard.count()
        total_steps = db.lessonstep.count()

        # Active users: users with a recorded lastLogin within the last 30 days
        raw_active = db.query_raw("SELECT COUNT(*) as count FROM \"User\" WHERE \"lastLogin\" >= NOW() - INTERVAL '30 days'")
        active_users = raw_active[0]['count'] if raw_active else 0

        # Completed courses (users where unlockedDay > 14)
        total_completions = db.userlessonprogress.count(where={"unlockedDay": {"gt": 14}})

        # Calculate total platform XP and coins
        raw_xp = db.query_raw('SELECT SUM(xp) as total_xp, SUM(coins) as total_coins FROM "User"')
        total_xp = raw_xp[0]['total_xp'] if raw_xp and raw_xp[0].get('total_xp') else 0
        total_coins = raw_xp[0]['total_coins'] if raw_xp and raw_xp[0].get('total_coins') else 0

        # Recent 7-day registration activity timeline
        recent_users = db.query_raw("SELECT \"createdAt\" FROM \"User\" WHERE \"createdAt\" >= NOW() - INTERVAL '7 days' ORDER BY \"createdAt\" ASC") or []


        # Group by day name (e.g. Mon, Tue, etc.)
        activity_timeline = []
        for i in range(7):
            day_target = (now_utc - datetime.timedelta(days=6 - i)).date()
            day_label = day_target.strftime("%a (%b %d)")
            day_count = sum(1 for u in recent_users if u.get('createdAt') and to_utc(u['createdAt']).date() == day_target)
            activity_timeline.append({
                "day": day_label,
                "users": day_count
            })

        # Category breakdown
        raw_cats = db.query_raw('SELECT category, COUNT(*) as count FROM "Lesson" GROUP BY category')
        category_breakdown = [
            {"category": r["category"], "count": r["count"]} for r in (raw_cats or [])
        ]

        # Announcements count
        raw_announcements = db.query_raw('SELECT COUNT(*) as total, COUNT(CASE WHEN "isActive" = true THEN 1 END) as active FROM "Announcement"')
        total_announcements = raw_announcements[0]['total'] if raw_announcements else 0
        active_announcements = raw_announcements[0]['active'] if raw_announcements else 0

        return jsonify({
            "totalUsers": total_users,
            "verifiedUsers": verified_users,
            "unverifiedUsers": max(0, total_users - verified_users),
            "verifiedPercentage": verified_percentage,
            "totalCourses": total_courses,
            "universityCourses": uni_courses_count,
            "totalQuizzes": total_quizzes,
            "totalFlashcards": total_flashcards,
            "totalSteps": total_steps,
            "activeUsers": active_users,
            "certificatesIssued": total_completions,
            "totalXpAwarded": total_xp,
            "totalCoinsInCirculation": total_coins,
            "totalAnnouncements": total_announcements,
            "activeAnnouncements": active_announcements,
            "activityTimeline": activity_timeline,
            "categoryBreakdown": category_breakdown,
            "serverTime": now_utc.isoformat()
        }), 200
    except Exception as e:
        print(f"Admin stats error: {e}")
        return jsonify({"error": "Failed to compute admin statistics"}), 500

# --------------------------------------------------------------------------
# 3. USER MANAGEMENT APIS
# --------------------------------------------------------------------------
@admin_bp.route('/users', methods=['GET'])
@admin_required
def get_admin_users(current_admin):
    """
    Paginated, searchable, and filterable list of platform users.
    Query params:
    - page: int (default 1)
    - limit: int (default 15)
    - search: string (username or email)
    - status: 'all' | 'verified' | 'unverified'
    - sort: 'createdAt' | 'xp' | 'level' | 'loginStreak' (default createdAt)
    - order: 'desc' | 'asc' (default desc)
    """
    try:
        page = max(1, int(request.args.get('page', 1)))
        limit = min(100, max(1, int(request.args.get('limit', 15))))
        search = request.args.get('search', '').strip().lower()
        status = request.args.get('status', 'all').lower()
        sort_by = request.args.get('sort', 'createdAt')
        sort_order = request.args.get('order', 'desc').upper()

        if sort_order not in ['ASC', 'DESC']:
            sort_order = 'DESC'

        # Map sort fields to safely quoted column names
        sort_column_map = {
            'createdat': '"createdAt"',
            'xp': 'xp',
            'level': 'level',
            'coins': 'coins',
            'loginstreak': '"loginStreak"',
            'username': 'username',
            'email': 'email'
        }
        order_col = sort_column_map.get(sort_by.lower(), '"createdAt"')

        # Build dynamic SQL query
        where_parts = []
        if status == 'verified':
            where_parts.append('"isVerified" = true')
        elif status == 'unverified':
            where_parts.append('("isVerified" = false OR "isVerified" IS NULL)')

        if search:
            escaped_search = f"%{search}%"
            where_parts.append(f"(LOWER(username) LIKE '{escaped_search}' OR LOWER(email) LIKE '{escaped_search}')")

        where_str = f"WHERE {' AND '.join(where_parts)}" if where_parts else ""

        count_res = db.query_raw(f'SELECT COUNT(*) as total FROM "User" {where_str}')
        total = count_res[0]['total'] if count_res else 0

        offset = (page - 1) * limit
        sql = f'''
            SELECT id, username, email, level, xp, coins, "loginStreak", "isVerified", "totalZenMinutes", "createdAt", "lastLogin"
            FROM "User"
            {where_str}
            ORDER BY {order_col} {sort_order}
            LIMIT {limit} OFFSET {offset}
        '''
        users = db.query_raw(sql) or []

        user_ids = [u['id'] for u in users]
        progress_records = db.userlessonprogress.find_many(
            where={"userId": {"in": user_ids}}
        ) if user_ids else []

        # Map progress counts per user
        progress_map = {}
        completed_map = {}
        for p in progress_records:
            progress_map[p.userId] = progress_map.get(p.userId, 0) + 1
            if p.unlockedDay > 14:
                completed_map[p.userId] = completed_map.get(p.userId, 0) + 1

        user_list = []

        for u in users:
            user_list.append({
                "id": u['id'],
                "username": u['username'],
                "email": u['email'],
                "level": u['level'],
                "xp": u['xp'],
                "coins": u['coins'],
                "loginStreak": u['loginStreak'],
                "isVerified": bool(u.get('isVerified', False)),
                "totalZenMinutes": u.get('totalZenMinutes', 0),
                "createdAt": format_iso(u.get('createdAt')),
                "lastLogin": format_iso(u.get('lastLogin')),
                "activeCoursesCount": progress_map.get(u['id'], 0),
                "completedCoursesCount": completed_map.get(u['id'], 0),
            })


        total_pages = max(1, (total + limit - 1) // limit)

        return jsonify({
            "users": user_list,
            "total": total,
            "page": page,
            "limit": limit,
            "totalPages": total_pages
        }), 200
    except Exception as e:
        print(f"Admin get users error: {e}")
        return jsonify({"error": "Failed to fetch users"}), 500

@admin_bp.route('/users/<user_id>/toggle-verify', methods=['PUT'])
@admin_required
def toggle_verify_user(current_admin, user_id):
    """
    Manually toggles a user's isVerified status.
    If turning to True, clears any pending OTP.
    """
    try:
        user_res = db.query_raw('SELECT id, username, email, "isVerified" FROM "User" WHERE id = $1', user_id)
        if not user_res:
            return jsonify({"error": "User not found"}), 404

        user = user_res[0]
        new_status = not bool(user.get('isVerified', False))

        db.execute_raw(
            'UPDATE "User" SET "isVerified" = $1, "otpCode" = NULL, "otpExpiresAt" = NULL WHERE id = $2',
            new_status, user_id
        )

        return jsonify({
            "success": True,
            "message": f"User '{user['username']}' verification status changed to {new_status}",
            "user": {
                "id": user['id'],
                "username": user['username'],
                "email": user['email'],
                "isVerified": new_status
            }
        }), 200
    except Exception as e:
        print(f"Toggle verify error: {e}")
        return jsonify({"error": "Failed to toggle verification"}), 500


@admin_bp.route('/users/<user_id>', methods=['PUT'])
@admin_required
def update_user_details(current_admin, user_id):
    """
    Update administrative user fields (XP, Coins, Level, isVerified).
    """
    try:
        data = request.json or {}
        update_fields = {}

        if 'xp' in data:
            update_fields['xp'] = int(data['xp'])
        if 'coins' in data:
            update_fields['coins'] = int(data['coins'])
        if 'level' in data:
            update_fields['level'] = int(data['level'])
        if 'loginStreak' in data:
            update_fields['loginStreak'] = int(data['loginStreak'])
        if 'isVerified' in data:
            update_fields['isVerified'] = bool(data['isVerified'])
            if update_fields['isVerified']:
                update_fields['otpCode'] = None
                update_fields['otpExpiresAt'] = None

        if not update_fields:
            return jsonify({"error": "No fields provided to update"}), 400

        updated = db.user.update(
            where={"id": user_id},
            data=update_fields
        )

        return jsonify({
            "success": True,
            "message": "User updated successfully",
            "user": {
                "id": updated.id,
                "username": updated.username,
                "email": updated.email,
                "level": updated.level,
                "xp": updated.xp,
                "coins": updated.coins,
                "isVerified": updated.isVerified
            }
        }), 200
    except Exception as e:
        print(f"Update user error: {e}")
        return jsonify({"error": "Failed to update user"}), 500

@admin_bp.route('/users/<user_id>', methods=['DELETE'])
@admin_required
def delete_user(current_admin, user_id):
    """
    Safely delete a user account and associated dependencies.
    """
    try:
        user = db.user.find_unique(where={"id": user_id})
        if not user:
            return jsonify({"error": "User not found"}), 404

        # Clean up related records
        db.userlessonprogress.delete_many(where={"userId": user_id})
        db.userprogress.delete_many(where={"userId": user_id})
        db.gig.delete_many(where={"posterId": user_id})
        db.matchmaking.delete_many(where={"user1Id": user_id})
        db.matchmaking.delete_many(where={"user2Id": user_id})

        db.user.delete(where={"id": user_id})

        return jsonify({
            "success": True,
            "message": f"User '{user.username}' successfully deleted."
        }), 200
    except Exception as e:
        print(f"Delete user error: {e}")
        return jsonify({"error": "Failed to delete user"}), 500

# --------------------------------------------------------------------------
# 4. UNIVERSITY COURSES & CURRICULUM APIS
# --------------------------------------------------------------------------
def get_obe_mapping_for_course(title):
    """Provides academic OBE (Outcome-Based Education) CLO/PLO attributes."""
    t = (title or '').lower()
    if 'operating' in t:
        return {
            "code": "CS-223L",
            "department": "Computing & Software Engineering",
            "semester": "Semester 4",
            "clos": [
                {"id": "CLO-1", "desc": "Execute Linux commands and bash shell scripts", "domain": "Cognitive C3", "plo": "PLO-1 (Academic Knowledge)"},
                {"id": "CLO-2", "desc": "Implement POSIX Pthreads multithreading and synchronization", "domain": "Psychomotor P3", "plo": "PLO-3 (Design & Solutions)"},
                {"id": "CLO-3", "desc": "Simulate CPU scheduling and Page Replacement algorithms", "domain": "Cognitive C4", "plo": "PLO-2 (Problem Analysis)"}
            ]
        }
    elif 'computing' in t or 'itc' in t:
        return {
            "code": "CS-111",
            "department": "Department of Computing",
            "semester": "Semester 1",
            "clos": [
                {"id": "CLO-1", "desc": "Analyze PC architecture, motherboard & hardware components", "domain": "Cognitive C2", "plo": "PLO-1 (Knowledge)"},
                {"id": "CLO-2", "desc": "Configure TCP/IP LAN, subnetting and network utilities", "domain": "Psychomotor P2", "plo": "PLO-5 (Modern Tools)"},
                {"id": "CLO-3", "desc": "Construct professional documentation and relational tables", "domain": "Affective A2", "plo": "PLO-9 (Team Work)"}
            ]
        }
    elif 'object' in t or 'oop' in t:
        return {
            "code": "CS-121L",
            "department": "Computer Science",
            "semester": "Semester 2",
            "clos": [
                {"id": "CLO-1", "desc": "Construct modular OOP classes with encapsulation and access specifiers", "domain": "Cognitive C3", "plo": "PLO-3 (Design)"},
                {"id": "CLO-2", "desc": "Implement multiple inheritance and polymorphism with virtual tables", "domain": "Psychomotor P3", "plo": "PLO-3 (Design)"},
                {"id": "CLO-3", "desc": "Apply template classes and robust stream exception handling", "domain": "Cognitive C4", "plo": "PLO-2 (Analysis)"}
            ]
        }
    elif 'data structure' in t or 'dsa' in t:
        return {
            "code": "CS-221",
            "department": "Computer Science",
            "semester": "Semester 3",
            "clos": [
                {"id": "CLO-1", "desc": "Implement linked lists, double-ended stacks and queues in C++", "domain": "Psychomotor P3", "plo": "PLO-3 (Design)"},
                {"id": "CLO-2", "desc": "Analyze asymptotic complexity O(N) of sorting and search algorithms", "domain": "Cognitive C4", "plo": "PLO-2 (Analysis)"},
                {"id": "CLO-3", "desc": "Construct binary search trees and heap priority queues", "domain": "Cognitive C4", "plo": "PLO-3 (Design)"}
            ]
        }
    elif 'networking' in t or 'ccn' in t:
        return {
            "code": "CS-200",
            "department": "Telecommunications & Networks",
            "semester": "Semester 5",
            "clos": [
                {"id": "CLO-1", "desc": "Design IPv4 subnet schemes and VLAN broadcast domains", "domain": "Cognitive C3", "plo": "PLO-1 (Knowledge)"},
                {"id": "CLO-2", "desc": "Configure Cisco CLI routers and routing protocols (OSPF/RIP)", "domain": "Psychomotor P4", "plo": "PLO-5 (Modern Tools)"},
                {"id": "CLO-3", "desc": "Analyze packet captures and Wireshark transmission logs", "domain": "Cognitive C4", "plo": "PLO-2 (Analysis)"}
            ]
        }
    elif 'fundamental' in t or 'cfp' in t:
        return {
            "code": "CF&P",
            "department": "Computer Science",
            "semester": "Semester 1",
            "clos": [
                {"id": "CLO-1", "desc": "Design structured control flow, loops and functions in C", "domain": "Cognitive C3", "plo": "PLO-1 (Knowledge)"},
                {"id": "CLO-2", "desc": "Implement pointer arithmetic and multidimensional arrays", "domain": "Psychomotor P3", "plo": "PLO-3 (Design)"},
                {"id": "CLO-3", "desc": "Develop modular algorithms for numeric and string manipulation", "domain": "Cognitive C4", "plo": "PLO-2 (Analysis)"}
            ]
        }
    else:
        return {
            "code": "UNIV-MOD",
            "department": "Faculty of Engineering & Sciences",
            "semester": "Accredited Lab",
            "clos": [
                {"id": "CLO-1", "desc": "Master core theoretical fundamentals and lab experiments", "domain": "Cognitive C2", "plo": "PLO-1"},
                {"id": "CLO-2", "desc": "Demonstrate practical tool proficiency and problem solving", "domain": "Psychomotor P3", "plo": "PLO-5"}
            ]
        }

@admin_bp.route('/courses', methods=['GET'])
@admin_required
def get_admin_courses(current_admin):
    """
    Returns full catalog with focus on the 9 seeded university courses:
    - Steps count, quizzes count, flashcards count
    - Enrollment counts and completions
    - Academic OBE CLO/PLO mapping
    """
    try:
        courses = db.lesson.find_many(
            include={"steps": {"order_by": {"order": "asc"}}}
        )

        # Count quizzes per lesson
        raw_quizzes = db.query_raw('SELECT "lessonId", COUNT(*) as count FROM "Quiz" GROUP BY "lessonId"')
        quiz_map = {r['lessonId']: r['count'] for r in (raw_quizzes or [])}

        # Count flashcards per lesson
        raw_fc = db.query_raw('SELECT "lessonId", COUNT(*) as count FROM "Flashcard" GROUP BY "lessonId"')
        fc_map = {r['lessonId']: r['count'] for r in (raw_fc or [])}

        # Count enrollments per lesson
        raw_progress = db.query_raw('SELECT "lessonId", COUNT(*) as enrollments, COUNT(CASE WHEN "unlockedDay" > 14 THEN 1 END) as completions FROM "UserLessonProgress" GROUP BY "lessonId"')
        progress_stats = {r['lessonId']: r for r in (raw_progress or [])}

        course_list = []
        for c in courses:
            total_steps = len(c.steps) if c.steps else 0
            stats = progress_stats.get(c.id, {})
            enrollments = stats.get('enrollments', 0)
            completions = stats.get('completions', 0)
            rate = round((completions / max(1, enrollments)) * 100, 1)

            is_university = (c.category or '').lower() in ['university', 'university courses']
            obe_info = get_obe_mapping_for_course(c.title)

            course_list.append({
                "id": c.id,
                "title": c.title,
                "category": c.category,
                "color": c.color,
                "description": c.description,
                "isUniversity": is_university,
                "obe": obe_info,
                "totalSteps": total_steps,
                "totalQuizzes": quiz_map.get(c.id, 0),
                "totalFlashcards": fc_map.get(c.id, 0),
                "enrollments": enrollments,
                "completions": completions,
                "completionRate": rate,
                "steps": [
                    {
                        "id": s.id,
                        "order": s.order,
                        "title": s.title,
                        "hasCode": bool(s.codeSnippet),
                        "snippet": (s.codeSnippet or '')[:100]
                    } for s in (c.steps or [])
                ]
            })

        # Sort: university courses first, then by total steps descending
        course_list.sort(key=lambda x: (1 if x["isUniversity"] else 0, x["totalSteps"]), reverse=True)

        return jsonify({
            "courses": course_list,
            "total": len(course_list),
            "universityCount": sum(1 for c in course_list if c["isUniversity"])
        }), 200
    except Exception as e:
        print(f"Admin courses error: {e}")
        return jsonify({"error": "Failed to fetch courses"}), 500

def is_safe_image_path(path):
    if not path or not isinstance(path, str):
        return True
    p = path.strip().lower()
    dangerous_prefixes = ('javascript:', 'data:text/html', 'vbscript:', 'file:')
    return not any(p.startswith(bad) for bad in dangerous_prefixes)

@admin_bp.route('/courses', methods=['POST'])
@admin_required
def create_course(current_admin):
    """
    Create a new course record with validation & sanitization.
    Accepts: title, category, description, color, image, totalSteps.
    """
    try:
        data = request.json or {}
        title = (data.get('title') or '').strip()
        category = (data.get('category') or '').strip()
        description = (data.get('description') or '').strip()
        color = (data.get('color') or '').strip()
        image = (data.get('image') or '').strip()

        if not title:
            return jsonify({"error": "Course title is required"}), 400
        if len(title) < 3 or len(title) > 200:
            return jsonify({"error": "Course title must be between 3 and 200 characters"}), 400

        if not category:
            category = "University Courses"
        if len(category) > 100:
            return jsonify({"error": "Category exceeds maximum length of 100 characters"}), 400

        # Validate hex color or default to Emerald #10B981
        if not color or not re.match(r'^#[0-9a-fA-F]{6}$|^#[0-9a-fA-F]{3}$', color):
            color = "#10B981"

        # Validate inline / external image path
        if image and not is_safe_image_path(image):
            return jsonify({"error": "Invalid or unsafe image path"}), 400

        new_course = db.lesson.create(
            data={
                "title": title,
                "category": category,
                "description": description or None,
                "color": color
            }
        )

        return jsonify({
            "success": True,
            "message": f"Course '{new_course.title}' created successfully",
            "course": {
                "id": new_course.id,
                "title": new_course.title,
                "category": new_course.category,
                "description": new_course.description,
                "color": new_course.color,
                "image": image or None,
                "totalSteps": 0,
                "totalQuizzes": 0,
                "isUniversity": category.lower() in ['university', 'university courses'],
                "createdAt": format_iso(new_course.createdAt)
            }
        }), 201
    except Exception as e:
        print(f"Create course error: {e}")
        return jsonify({"error": "Failed to create course"}), 500

@admin_bp.route('/courses/<course_id>', methods=['DELETE'])
@admin_required
def delete_course(current_admin, course_id):
    """
    Safely delete a course.
    NON-DESTRUCTIVE DIRECTIVE: Strictly protects the 9 official university courses.
    """
    try:
        course = db.lesson.find_unique(where={"id": course_id})
        if not course:
            return jsonify({"error": "Course not found"}), 404

        # Safety check: Protect official university curricula
        protected_titles = [
            'operating systems', 'computing', 'object oriented', 'data structure',
            'networking', 'fundamental', 'software engineering', 'database'
        ]
        is_official = (course.category or '').lower() in ['university', 'university courses'] and any(pt in course.title.lower() for pt in protected_titles)
        if is_official:
            return jsonify({"error": "Protected Academic Course: Official university curricula cannot be deleted"}), 403

        # Delete cascades
        db.quiz.delete_many(where={"lessonId": course_id})
        db.flashcard.delete_many(where={"lessonId": course_id})
        db.lessonstep.delete_many(where={"lessonId": course_id})
        db.userlessonprogress.delete_many(where={"lessonId": course_id})
        db.lesson.delete(where={"id": course_id})

        return jsonify({
            "success": True,
            "message": f"Course '{course.title}' deleted successfully"
        }), 200
    except Exception as e:
        print(f"Delete course error: {e}")
        return jsonify({"error": "Failed to delete course"}), 500

@admin_bp.route('/courses/<course_id>/steps', methods=['POST'])
@admin_required
def create_course_step(current_admin, course_id):
    """
    Add a new LessonStep to a course with OBE attributes and markdown validation.
    Accepts: order, title, content, codeSnippet, type, clo, plo, blooms, imagePath.
    """
    try:
        course = db.lesson.find_unique(where={"id": course_id})
        if not course:
            return jsonify({"error": "Target course not found"}), 404

        data = request.json or {}
        title = (data.get('title') or '').strip()
        content = (data.get('content') or '').strip()
        code_snippet = (data.get('codeSnippet') or '').strip()
        step_type = (data.get('type') or 'lab').strip()
        clo = (data.get('clo') or '').strip()
        plo = (data.get('plo') or '').strip()
        blooms = (data.get('blooms') or '').strip()
        image_path = (data.get('imagePath') or '').strip()

        if not title:
            return jsonify({"error": "Step title is required"}), 400
        if len(title) < 3 or len(title) > 250:
            return jsonify({"error": "Step title must be between 3 and 250 characters"}), 400

        # Validate inline image path if provided
        if image_path and not is_safe_image_path(image_path):
            return jsonify({"error": "Invalid or unsafe diagram image path"}), 400

        if not content:
            content = f"### {title}\n\nComprehensive laboratory experiment procedure."

        # If imagePath is provided and not already in markdown, append diagram reference
        if image_path and image_path not in content:
            content += f"\n\n![Lab Diagram]({image_path})"

        # Calculate next step order if not provided
        order = data.get('order')
        if order is None or int(order) <= 0:
            max_order_row = db.query_raw('SELECT COALESCE(MAX("order"), 0) as max_order FROM "LessonStep" WHERE "lessonId" = $1', course_id)
            order = (max_order_row[0]['max_order'] + 1) if max_order_row else 1
        else:
            order = int(order)

        # OBE Compliance Block Injection
        obe_tags = []
        if clo:
            obe_tags.append(f"**CLO:** {clo}")
        if plo:
            obe_tags.append(f"**PLO:** {plo}")
        if blooms:
            obe_tags.append(f"**Bloom's:** {blooms}")

        if obe_tags and not content.startswith('> **OBE Mapping:'):
            obe_header = f"> **OBE Mapping:** {' | '.join(obe_tags)}\n\n"
            content = obe_header + content

        new_step = db.lessonstep.create(
            data={
                "lessonId": course_id,
                "order": order,
                "title": title,
                "content": content,
                "codeSnippet": code_snippet if code_snippet else None
            }
        )

        return jsonify({
            "success": True,
            "message": f"Lab step '{new_step.title}' (Order {new_step.order}) added successfully",
            "step": {
                "id": new_step.id,
                "lessonId": new_step.lessonId,
                "order": new_step.order,
                "title": new_step.title,
                "content": new_step.content,
                "codeSnippet": new_step.codeSnippet,
                "hasCode": bool(new_step.codeSnippet),
                "type": step_type
            }
        }), 201
    except Exception as e:
        print(f"Create step error: {e}")
        return jsonify({"error": "Failed to create lab step"}), 500

@admin_bp.route('/steps/<step_id>', methods=['DELETE'])
@admin_required
def delete_step(current_admin, step_id):
    """Delete a specific lab step and its attached quizzes/flashcards."""
    try:
        step = db.lessonstep.find_unique(where={"id": step_id})
        if not step:
            return jsonify({"error": "Step not found"}), 404

        db.quiz.delete_many(where={"lessonStepId": step_id})
        db.flashcard.delete_many(where={"lessonStepId": step_id})
        db.lessonstep.delete(where={"id": step_id})

        return jsonify({
            "success": True,
            "message": f"Step '{step.title}' deleted successfully"
        }), 200
    except Exception as e:
        print(f"Delete step error: {e}")
        return jsonify({"error": "Failed to delete step"}), 500

@admin_bp.route('/steps/<step_id>/quizzes', methods=['POST'])
@admin_required
def create_step_quiz(current_admin, step_id):
    """
    Add assessment quiz tied directly to a specific LessonStep.
    Accepts: question, 4 options, correctAnswer, explanation.
    """
    try:
        step = db.lessonstep.find_unique(where={"id": step_id})
        if not step:
            return jsonify({"error": "Lab step not found"}), 404

        data = request.json or {}
        question = (data.get('question') or '').strip()
        options = data.get('options', [])
        correct_answer = (data.get('correctAnswer') or '').strip()
        explanation = (data.get('explanation') or '').strip()

        if not question:
            return jsonify({"error": "Quiz question is required"}), 400
        if len(question) < 5:
            return jsonify({"error": "Question must be at least 5 characters long"}), 400

        if not isinstance(options, list) or len(options) < 2:
            return jsonify({"error": "At least 2 options are required"}), 400

        clean_options = [str(opt).strip() for opt in options if str(opt).strip()]
        if len(clean_options) < 2:
            return jsonify({"error": "At least 2 non-empty options are required"}), 400

        if not correct_answer:
            return jsonify({"error": "correctAnswer is required"}), 400

        if correct_answer not in clean_options:
            return jsonify({"error": "correctAnswer must match one of the provided options"}), 400

        new_quiz = db.quiz.create(
            data={
                "lessonId": step.lessonId,
                "lessonStepId": step.id,
                "question": question,
                "options": clean_options,
                "correctAnswer": correct_answer,
                "explanation": explanation or None
            }
        )

        return jsonify({
            "success": True,
            "message": "Assessment quiz created successfully",
            "quiz": {
                "id": new_quiz.id,
                "lessonId": new_quiz.lessonId,
                "lessonStepId": new_quiz.lessonStepId,
                "question": new_quiz.question,
                "options": new_quiz.options,
                "correctAnswer": new_quiz.correctAnswer,
                "explanation": new_quiz.explanation,
                "createdAt": format_iso(new_quiz.createdAt)
            }
        }), 201
    except Exception as e:
        print(f"Create step quiz error: {e}")
        return jsonify({"error": "Failed to create assessment quiz"}), 500

@admin_bp.route('/courses/<course_id>/quizzes', methods=['GET'])
@admin_required
def get_course_quizzes(current_admin, course_id):
    """
    View all lab steps and quizzes for a specific course.
    """
    try:
        course = db.lesson.find_unique(
            where={"id": course_id},
            include={"steps": {"order_by": {"order": "asc"}}}
        )
        if not course:
            return jsonify({"error": "Course not found"}), 404

        quizzes = db.quiz.find_many(
            where={"lessonId": course_id}
        )

        steps_data = []
        quiz_by_step = {}
        for q in quizzes:
            key = q.lessonStepId or 'general'
            if key not in quiz_by_step:
                quiz_by_step[key] = []
            quiz_by_step[key].append({
                "id": q.id,
                "question": q.question,
                "options": q.options,
                "correctAnswer": q.correctAnswer,
                "explanation": q.explanation,
                "lessonStepId": q.lessonStepId
            })

        for s in (course.steps or []):
            steps_data.append({
                "id": s.id,
                "order": s.order,
                "title": s.title,
                "codeSnippet": s.codeSnippet,
                "contentPreview": (s.content or '')[:200],
                "quizzes": quiz_by_step.get(s.id, [])
            })

        general_quizzes = quiz_by_step.get('general', [])

        return jsonify({
            "course": {
                "id": course.id,
                "title": course.title,
                "category": course.category,
                "obe": get_obe_mapping_for_course(course.title)
            },
            "steps": steps_data,
            "generalQuizzes": general_quizzes,
            "totalQuizzes": len(quizzes)
        }), 200
    except Exception as e:
        print(f"Course quizzes error: {e}")
        return jsonify({"error": "Failed to fetch course quizzes"}), 500

# --------------------------------------------------------------------------
# 5. QUIZ CRUD APIS
# --------------------------------------------------------------------------
@admin_bp.route('/quizzes/<quiz_id>', methods=['PUT'])
@admin_required
def update_quiz(current_admin, quiz_id):
    """
    Edit an existing quiz question, options, correctAnswer, and explanation.
    """
    try:
        data = request.json or {}
        question = data.get('question', '').strip()
        options = data.get('options', [])
        correct_answer = data.get('correctAnswer', '').strip()
        explanation = data.get('explanation', '').strip()

        if not question or not options or not correct_answer:
            return jsonify({"error": "Question, options, and correctAnswer are required"}), 400

        if correct_answer not in options:
            return jsonify({"error": "correctAnswer must be present in options list"}), 400

        quiz = db.quiz.find_unique(where={"id": quiz_id})
        if not quiz:
            return jsonify({"error": "Quiz not found"}), 404

        updated = db.quiz.update(
            where={"id": quiz_id},
            data={
                "question": question,
                "options": options,
                "correctAnswer": correct_answer,
                "explanation": explanation
            }
        )

        return jsonify({
            "success": True,
            "message": "Quiz updated successfully",
            "quiz": {
                "id": updated.id,
                "question": updated.question,
                "options": updated.options,
                "correctAnswer": updated.correctAnswer,
                "explanation": updated.explanation
            }
        }), 200
    except Exception as e:
        print(f"Update quiz error: {e}")
        return jsonify({"error": "Failed to update quiz"}), 500

@admin_bp.route('/courses/<course_id>/quizzes', methods=['POST'])
@admin_required
def create_quiz(current_admin, course_id):
    """
    Add a new quiz question to a course or lab step.
    """
    try:
        data = request.json or {}
        question = data.get('question', '').strip()
        options = data.get('options', [])
        correct_answer = data.get('correctAnswer', '').strip()
        explanation = data.get('explanation', '').strip()
        lesson_step_id = data.get('lessonStepId')

        if not question or not options or not correct_answer:
            return jsonify({"error": "Question, options, and correctAnswer are required"}), 400

        if correct_answer not in options:
            return jsonify({"error": "correctAnswer must match one of the options"}), 400

        new_quiz = db.quiz.create(
            data={
                "lessonId": course_id,
                "lessonStepId": lesson_step_id,
                "question": question,
                "options": options,
                "correctAnswer": correct_answer,
                "explanation": explanation
            }
        )

        return jsonify({
            "success": True,
            "message": "Quiz created successfully",
            "quiz": {
                "id": new_quiz.id,
                "question": new_quiz.question,
                "options": new_quiz.options,
                "correctAnswer": new_quiz.correctAnswer,
                "lessonStepId": new_quiz.lessonStepId
            }
        }), 201
    except Exception as e:
        print(f"Create quiz error: {e}")
        return jsonify({"error": "Failed to create quiz"}), 500

@admin_bp.route('/quizzes/<quiz_id>', methods=['DELETE'])
@admin_required
def delete_quiz(current_admin, quiz_id):
    """Delete a quiz question."""
    try:
        quiz = db.quiz.find_unique(where={"id": quiz_id})
        if not quiz:
            return jsonify({"error": "Quiz not found"}), 404

        db.quiz.delete(where={"id": quiz_id})
        return jsonify({"success": True, "message": "Quiz deleted successfully"}), 200
    except Exception as e:
        print(f"Delete quiz error: {e}")
        return jsonify({"error": "Failed to delete quiz"}), 500

# --------------------------------------------------------------------------
# 5B. ANNOUNCEMENTS & NOTICE BOARD APIS
# --------------------------------------------------------------------------
@admin_bp.route('/announcements', methods=['GET'])
@admin_required
def get_admin_announcements(current_admin):
    """List all announcements for admin management."""
    try:
        items = db.query_raw('''
            SELECT id, title, message, type, "isActive", "createdAt", "updatedAt"
            FROM "Announcement"
            ORDER BY "createdAt" DESC
        ''') or []

        res = []
        for a in items:
            res.append({
                "id": a['id'],
                "title": a['title'],
                "message": a['message'],
                "type": a.get('type', 'info'),
                "isActive": bool(a.get('isActive', True)),
                "createdAt": format_iso(a.get('createdAt')),
                "updatedAt": format_iso(a.get('updatedAt'))
            })

        return jsonify({
            "success": True,
            "announcements": res,
            "total": len(res)
        }), 200
    except Exception as e:
        print(f"Admin announcements get error: {e}")
        return jsonify({"error": "Failed to fetch announcements"}), 500

@admin_bp.route('/announcements', methods=['POST'])
@admin_required
def create_admin_announcement(current_admin):
    """Create a new platform announcement."""
    try:
        data = request.json or {}
        title = (data.get('title') or '').strip()
        message = (data.get('message') or '').strip()
        announcement_type = (data.get('type') or 'info').strip().lower()
        is_active = bool(data.get('isActive', True))

        if not title:
            return jsonify({"error": "Announcement title is required"}), 400
        if not message:
            return jsonify({"error": "Announcement message is required"}), 400

        if announcement_type not in ['info', 'warning', 'success']:
            announcement_type = 'info'

        raw_res = db.query_raw('''
            INSERT INTO "Announcement" (title, message, type, "isActive", "createdAt", "updatedAt")
            VALUES ($1, $2, $3, $4, NOW(), NOW())
            RETURNING id, title, message, type, "isActive", "createdAt", "updatedAt"
        ''', title, message, announcement_type, is_active)

        created = raw_res[0] if raw_res else None
        if not created:
            return jsonify({"error": "Failed to insert announcement"}), 500

        return jsonify({
            "success": True,
            "message": "Announcement published successfully",
            "announcement": {
                "id": created['id'],
                "title": created['title'],
                "message": created['message'],
                "type": created['type'],
                "isActive": bool(created['isActive']),
                "createdAt": format_iso(created['createdAt']),
                "updatedAt": format_iso(created['updatedAt'])
            }
        }), 201
    except Exception as e:
        print(f"Admin create announcement error: {e}")
        return jsonify({"error": "Failed to create announcement"}), 500

@admin_bp.route('/announcements/<announcement_id>/toggle', methods=['PUT'])
@admin_required
def toggle_announcement(current_admin, announcement_id):
    """Toggle an announcement's active status."""
    try:
        item_res = db.query_raw('SELECT id, title, "isActive" FROM "Announcement" WHERE id = $1', announcement_id)
        if not item_res:
            return jsonify({"error": "Announcement not found"}), 404

        current_status = bool(item_res[0].get('isActive', False))
        new_status = not current_status

        db.execute_raw('UPDATE "Announcement" SET "isActive" = $1, "updatedAt" = NOW() WHERE id = $2', new_status, announcement_id)

        return jsonify({
            "success": True,
            "message": f"Announcement is now {'Active' if new_status else 'Inactive'}",
            "isActive": new_status
        }), 200
    except Exception as e:
        print(f"Toggle announcement error: {e}")
        return jsonify({"error": "Failed to toggle announcement status"}), 500

@admin_bp.route('/announcements/<announcement_id>', methods=['PUT'])
@admin_required
def update_announcement(current_admin, announcement_id):
    """Edit an announcement's title, message, or priority."""
    try:
        data = request.json or {}
        title = (data.get('title') or '').strip()
        message = (data.get('message') or '').strip()
        announcement_type = (data.get('type') or 'info').strip().lower()
        is_active = data.get('isActive')

        if not title or not message:
            return jsonify({"error": "Title and message are required"}), 400

        if announcement_type not in ['info', 'warning', 'success']:
            announcement_type = 'info'

        raw_res = db.query_raw('''
            UPDATE "Announcement"
            SET title = $1, message = $2, type = $3, "isActive" = COALESCE($4, "isActive"), "updatedAt" = NOW()
            WHERE id = $5
            RETURNING id, title, message, type, "isActive", "createdAt", "updatedAt"
        ''', title, message, announcement_type, is_active, announcement_id)

        if not raw_res:
            return jsonify({"error": "Announcement not found"}), 404

        updated = raw_res[0]
        return jsonify({
            "success": True,
            "message": "Announcement updated successfully",
            "announcement": {
                "id": updated['id'],
                "title": updated['title'],
                "message": updated['message'],
                "type": updated['type'],
                "isActive": bool(updated['isActive']),
                "createdAt": format_iso(updated['createdAt']),
                "updatedAt": format_iso(updated['updatedAt'])
            }
        }), 200
    except Exception as e:
        print(f"Update announcement error: {e}")
        return jsonify({"error": "Failed to update announcement"}), 500

@admin_bp.route('/announcements/<announcement_id>', methods=['DELETE'])
@admin_required
def delete_announcement(current_admin, announcement_id):
    """Delete an announcement record."""
    try:
        db.execute_raw('DELETE FROM "Announcement" WHERE id = $1', announcement_id)
        return jsonify({"success": True, "message": "Announcement deleted successfully"}), 200
    except Exception as e:
        print(f"Delete announcement error: {e}")
        return jsonify({"error": "Failed to delete announcement"}), 500

# --------------------------------------------------------------------------
# 5C. ECONOMY & REWARD CONTROL APIS
# --------------------------------------------------------------------------
@admin_bp.route('/economy/config', methods=['GET'])
@admin_required
def get_admin_economy_config(current_admin):
    """Fetch current system economy configuration and reward rates."""
    try:
        config = get_system_config()
        return jsonify({"success": True, "config": config}), 200
    except Exception as e:
        print(f"Admin get economy config error: {e}")
        return jsonify({"error": "Failed to fetch economy config"}), 500

@admin_bp.route('/economy/config', methods=['PUT'])
@admin_required
def update_admin_economy_config(current_admin):
    """Dynamically configure XP, coins, and gamification reward rates."""
    try:
        data = request.json or {}
        updated = update_system_config(data)
        return jsonify({
            "success": True,
            "message": "Economy configuration updated successfully",
            "config": updated
        }), 200
    except Exception as e:
        print(f"Admin update economy config error: {e}")
        return jsonify({"error": "Failed to update economy config"}), 500

@admin_bp.route('/economy/grant-reward', methods=['POST'])
@admin_required
def grant_admin_reward(current_admin):
    """
    Safely grant manual bonus XP and Coins to a specific student or all students.
    Recalculates level automatically without altering or resetting existing records.
    """
    try:
        data = request.json or {}
        user_id = data.get('userId')
        xp_amount = int(data.get('xp', 0))
        coins_amount = int(data.get('coins', 0))
        reason = (data.get('reason') or 'Admin Award').strip()

        if xp_amount <= 0 and coins_amount <= 0:
            return jsonify({"error": "Please provide a positive XP or Coins amount to grant"}), 400

        if user_id == 'all':
            result = grant_bulk_reward(xp_amount, coins_amount, reason)
            return jsonify({
                "success": True,
                "message": f"Successfully granted {xp_amount} XP and {coins_amount} Coins to all students!",
                "result": result
            }), 200

        if not user_id:
            return jsonify({"error": "Target student userId is required"}), 400

        result = grant_student_reward(user_id, xp_amount, coins_amount, reason)
        return jsonify({
            "success": True,
            "message": f"Successfully awarded {xp_amount} XP & {coins_amount} Coins to {result.get('username', 'student')}!",
            "result": result
        }), 200
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 404
    except Exception as e:
        print(f"Admin grant reward error: {e}")
        return jsonify({"error": "Failed to grant reward"}), 500

@admin_bp.route('/economy/students', methods=['GET'])
@admin_required
def get_admin_economy_students(current_admin):
    """Returns compact list of students for reward target selector."""
    try:
        students = db.query_raw('''
            SELECT id, username, email, level, xp, coins
            FROM "User"
            ORDER BY xp DESC
            LIMIT 100
        ''') or []

        res = []
        for s in students:
            res.append({
                "id": s['id'],
                "username": s['username'],
                "email": s['email'],
                "level": s.get('level', 1),
                "xp": s.get('xp', 0),
                "coins": s.get('coins', 0)
            })
        return jsonify({"success": True, "students": res}), 200
    except Exception as e:
        print(f"Admin get economy students error: {e}")
        return jsonify({"error": "Failed to fetch student list"}), 500

# --------------------------------------------------------------------------
# 6. SERVE MODERN REACT/TAILWIND WEB ADMIN DASHBOARD
# --------------------------------------------------------------------------
@admin_web_bp.route('/admin')
@admin_web_bp.route('/admin/')
@admin_web_bp.route('/admin/<path:subpath>')
def serve_admin_dashboard(subpath=None):
    """
    Serves a modern single-page Admin Dashboard with React, Tailwind CSS,
    interactive Chart.js graphs, live User management, Course & Lab Creator Studio,
    Campus Notice Board, and Platform Economy Controller.
    """
    html_template = r"""<!DOCTYPE html>
<html lang="en" class="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Hunar Cycle — Executive Admin Operating System</title>

  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      darkMode: 'class',
      theme: {
        extend: {
          colors: {
            ocean: {
              950: '#061428', // Deep Royal Midnight Ocean Blue canvas
              900: '#0a1c38', // Elevated surface / sidebar
              850: '#0e2343', // Primary card surface
              800: '#142c54', // Hover surface / elevated card
              750: '#183768', // Active pill / border accent
              700: '#1e4480', // Cyan-tinted deep border
              600: '#2b5a9e',
            }
          },
          fontFamily: {
            sans: ['Inter', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'sans-serif'],
            mono: ['JetBrains Mono', 'Fira Code', 'monospace'],
          },
          boxShadow: {
            'glow-cyan': '0 0 20px -3px rgba(56, 189, 248, 0.25)',
            'glow-emerald': '0 0 20px -3px rgba(16, 185, 129, 0.25)',
            'glow-sky': '0 0 25px -4px rgba(14, 165, 233, 0.3)',
          }
        }
      }
    };
  </script>

  <!-- React 18 & Babel Standalone -->
  <script src="https://unpkg.com/react@18/umd/react.production.min.js" crossorigin></script>
  <script src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js" crossorigin></script>
  <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>

  <!-- Chart.js & Markdown Parser -->
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>

  <!-- Google Fonts: Inter & JetBrains Mono -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">

  <!-- Instant Pre-hydration Theme Engine to completely eliminate theme flicker -->
  <script>
    (function() {
      try {
        var saved = localStorage.getItem('hunar_admin_theme') || localStorage.getItem('theme');
        var theme = (saved === 'light' || saved === 'dark') ? saved : 'dark';
        var root = document.documentElement;
        root.classList.remove('dark', 'light');
        root.classList.add(theme);
        root.style.colorScheme = theme;
      } catch (e) {}
    })();
  </script>

  <style>
    * {
      box-sizing: border-box;
    }
    body {
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
    }
    .font-mono-code {
      font-family: 'JetBrains Mono', monospace;
    }

    /* Minimalist Executive Scrollbars */
    ::-webkit-scrollbar {
      width: 6px;
      height: 6px;
    }
    html.dark ::-webkit-scrollbar-track {
      background: #061428;
    }
    html.dark ::-webkit-scrollbar-thumb {
      background: #142c54;
      border-radius: 9999px;
    }
    html.dark ::-webkit-scrollbar-thumb:hover {
      background: #1e4480;
    }
    html.light ::-webkit-scrollbar-track {
      background: #F1F5F9;
    }
    html.light ::-webkit-scrollbar-thumb {
      background: #CBD5E1;
      border-radius: 9999px;
    }
    html.light ::-webkit-scrollbar-thumb:hover {
      background: #94A3B8;
    }

    /* Global Smooth Theme Transition */
    body, aside, header, main, div, nav, input, select, textarea, table, th, td, tr, button {
      transition-property: background-color, border-color, color, box-shadow;
      transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
      transition-duration: 180ms;
    }

    /* Markdown Prose for Dark & Light */
    .md-preview h1 { font-size: 1.25rem; font-weight: 700; margin-bottom: 0.75rem; border-bottom: 1px solid currentColor; opacity: 0.85; padding-bottom: 0.4rem; }
    .md-preview h2 { font-size: 1.1rem; font-weight: 600; margin-top: 1rem; margin-bottom: 0.5rem; }
    .md-preview h3 { font-size: 1rem; font-weight: 600; margin-top: 0.75rem; margin-bottom: 0.4rem; color: #38BDF8; }
    html.light .md-preview h3 { color: #0284C7; }
    .md-preview p { margin-bottom: 0.75rem; line-height: 1.6; font-size: 0.85rem; }
    .md-preview ul { list-style-type: disc; margin-left: 1.5rem; margin-bottom: 0.75rem; font-size: 0.85rem; }
    .md-preview ol { list-style-type: decimal; margin-left: 1.5rem; margin-bottom: 0.75rem; font-size: 0.85rem; }
    .md-preview blockquote { border-left: 3px solid #38BDF8; padding: 0.5rem 0.75rem; margin-bottom: 0.75rem; border-radius: 0.375rem; font-size: 0.8rem; }
    html.dark .md-preview blockquote { background: rgba(56, 189, 248, 0.08); color: #BAE6FD; }
    html.light .md-preview blockquote { background: #F0F9FF; color: #0369A1; border-color: #0284C7; }
    .md-preview pre { padding: 0.85rem; border-radius: 0.5rem; overflow-x: auto; margin-bottom: 0.75rem; font-size: 0.8rem; }
    html.dark .md-preview pre { background: #07152b; border: 1px solid rgba(56, 189, 248, 0.2); }
    html.light .md-preview pre { background: #F8FAFC; border: 1px solid #E2E8F0; }
    .md-preview code { font-family: 'JetBrains Mono', monospace; font-size: 0.8rem; }
    html.dark .md-preview code { color: #7DD3FC; }
    html.light .md-preview code { color: #0369A1; }
    .md-preview img { max-width: 100%; border-radius: 0.5rem; margin: 0.75rem 0; }

    /* Toast animation */
    @keyframes toastSlideIn {
      from { transform: translateY(-16px); opacity: 0; }
      to { transform: translateY(0); opacity: 1; }
    }
    .animate-toast-down {
      animation: toastSlideIn 0.25s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }
  </style>
</head>
<body class="min-h-screen antialiased selection:bg-sky-500 selection:text-slate-950">
  <div id="root"></div>

  <!-- React 18 SPA Application -->
  <script type="text/babel">
    const { useState, useEffect, useRef, useMemo } = React;
    const API_BASE = window.location.origin;

    function AdminApp() {
      // 1. DUAL THEME STATE WITH LOCALSTORAGE PERSISTENCE (Default: 'dark')
      const [theme, setTheme] = useState(() => {
        try {
          const saved = localStorage.getItem('hunar_admin_theme') || localStorage.getItem('theme');
          return (saved === 'light' || saved === 'dark') ? saved : 'dark';
        } catch (e) {
          return 'dark';
        }
      });

      useEffect(() => {
        try {
          localStorage.setItem('hunar_admin_theme', theme);
          localStorage.setItem('theme', theme);
        } catch (e) {}

        const root = document.documentElement;
        root.classList.remove('dark', 'light');
        root.classList.add(theme);
        root.style.colorScheme = theme;
        document.body.style.backgroundColor = theme === 'dark' ? '#061428' : '#F8FAFC';
        document.body.style.color = theme === 'dark' ? '#F1F5F9' : '#0F172A';
      }, [theme]);

      const toggleTheme = () => {
        setTheme(prev => (prev === 'dark' ? 'light' : 'dark'));
      };

      // 2. AUTHENTICATION & CORE STATES
      const [token, setToken] = useState(() => localStorage.getItem('hunar_admin_token') || '');
      const [adminUser, setAdminUser] = useState(null);
      const [activeTab, setActiveTab] = useState('overview'); // overview, users, curriculum, creator, announcements, economy

      // 3. GLOBAL DATA STATES
      const [stats, setStats] = useState(null);
      const [usersData, setUsersData] = useState({ users: [], total: 0, page: 1, totalPages: 1 });
      const [courses, setCourses] = useState([]);
      const [isLoading, setIsLoading] = useState(false);
      const [notification, setNotification] = useState(null);

      // Users filtering & pagination
      const [userSearch, setUserSearch] = useState('');
      const [userStatusFilter, setUserStatusFilter] = useState('all');
      const [userSortBy, setUserSortBy] = useState('createdAt');
      const [currentPage, setCurrentPage] = useState(1);

      // Curriculum & Quiz inspector
      const [selectedCourseId, setSelectedCourseId] = useState(null);
      const [courseQuizzes, setCourseQuizzes] = useState(null);
      const [editingQuiz, setEditingQuiz] = useState(null);
      const [isQuizModalOpen, setIsQuizModalOpen] = useState(false);

      // Course & Lab Creator Studio
      const [creatorCourse, setCreatorCourse] = useState({
        title: '',
        category: 'University Courses',
        description: '',
        color: '#0EA5E9',
        image: '/assets/courses/os.png',
        totalSteps: 14
      });
      const [creatorStep, setCreatorStep] = useState({
        courseId: '',
        order: 1,
        title: '',
        content: '',
        codeSnippet: '',
        type: 'lab',
        clo: 'CLO-1: Understand fundamental concepts',
        plo: 'PLO-1 (Academic Knowledge)',
        blooms: 'Cognitive C3 (Apply)',
        imagePath: ''
      });
      const [creatorQuiz, setCreatorQuiz] = useState({
        question: '',
        options: ['', '', '', ''],
        correctAnswer: '',
        explanation: ''
      });
      const [activeStudioStep, setActiveStudioStep] = useState('course'); // 'course' | 'step' | 'quiz'
      const [savedStep, setSavedStep] = useState(null);
      const [savedStepQuizzes, setSavedStepQuizzes] = useState([]);
      const [isCreatingCourse, setIsCreatingCourse] = useState(false);
      const [isCreatingStep, setIsCreatingStep] = useState(false);
      const [isCreatingQuiz, setIsCreatingQuiz] = useState(false);
      const [previewMode, setPreviewMode] = useState('split');

      // Campus Announcements
      const [announcements, setAnnouncements] = useState([]);
      const [isLoadingAnnouncements, setIsLoadingAnnouncements] = useState(false);
      const [newAnnouncement, setNewAnnouncement] = useState({
        title: '',
        message: '',
        type: 'info',
        targetAudience: 'ALL',
        isActive: true
      });
      const [isPublishingAnnouncement, setIsPublishingAnnouncement] = useState(false);
      const [announcementFilter, setAnnouncementFilter] = useState('all');

      // Platform Economy Controller
      const [economyConfig, setEconomyConfig] = useState({
        quizPassXp: 15,
        perfectQuizBonusXp: 25,
        labCompletionXp: 50,
        dailyStreakCoins: 10,
        arenaWinXp: 35,
        arenaWinCoins: 15,
        updatedAt: null
      });
      const [isLoadingEconomy, setIsLoadingEconomy] = useState(false);
      const [isSavingEconomy, setIsSavingEconomy] = useState(false);
      const [economyStudents, setEconomyStudents] = useState([]);
      const [grantForm, setGrantForm] = useState({
        userId: '',
        xp: 100,
        coins: 50,
        reason: ''
      });
      const [isGrantingReward, setIsGrantingReward] = useState(false);

      // Reusable Confirm Dialog Modal
      const [confirmModal, setConfirmModal] = useState({
        isOpen: false,
        title: '',
        message: '',
        confirmText: 'Delete',
        isDanger: true,
        onConfirm: null
      });

      const triggerConfirm = (title, message, onConfirm, confirmText = 'Delete', isDanger = true) => {
        setConfirmModal({
          isOpen: true,
          title,
          message,
          confirmText,
          isDanger,
          onConfirm
        });
      };

      // Auth Inputs for Login Form
      const [authKeyInput, setAuthKeyInput] = useState('');
      const [authEmailInput, setAuthEmailInput] = useState('');
      const [authPassInput, setAuthPassInput] = useState('');
      const [authError, setAuthError] = useState('');

      const showNotify = (msg, type = 'success') => {
        setNotification({ msg, type });
        setTimeout(() => setNotification(null), 4000);
      };

      const getHeaders = () => ({
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`,
        'X-Admin-Key': token.startsWith('key_') ? token.replace('key_', '') : ''
      });

      // Session Verification
      useEffect(() => {
        if (!token) return;
        fetch(`${API_BASE}/api/admin/me`, { headers: getHeaders() })
          .then(res => {
            if (res.ok) return res.json();
            throw new Error('Unauthorized');
          })
          .then(data => setAdminUser(data))
          .catch(() => {
            localStorage.removeItem('hunar_admin_token');
            setToken('');
            setAdminUser(null);
          });
      }, [token]);

      // Data Fetchers
      const fetchStats = async () => {
        if (!token) return;
        try {
          const res = await fetch(`${API_BASE}/api/admin/stats`, { headers: getHeaders() });
          if (res.ok) {
            const data = await res.json();
            setStats(data);
          }
        } catch (e) {
          console.error(e);
        }
      };

      const fetchUsers = async () => {
        if (!token) return;
        setIsLoading(true);
        try {
          const query = new URLSearchParams({
            page: currentPage,
            limit: 10,
            search: userSearch,
            status: userStatusFilter,
            sort: userSortBy,
            order: 'desc'
          });
          const res = await fetch(`${API_BASE}/api/admin/users?${query.toString()}`, { headers: getHeaders() });
          if (res.ok) {
            const data = await res.json();
            setUsersData(data);
          }
        } catch (e) {
          showNotify('Failed to fetch user list', 'error');
        } finally {
          setIsLoading(false);
        }
      };

      const fetchCourses = async () => {
        if (!token) return;
        try {
          const res = await fetch(`${API_BASE}/api/admin/courses`, { headers: getHeaders() });
          if (res.ok) {
            const data = await res.json();
            setCourses(data.courses || []);
          }
        } catch (e) {
          console.error(e);
        }
      };

      const fetchCourseQuizzes = async (courseId) => {
        if (!token || !courseId) return;
        try {
          const res = await fetch(`${API_BASE}/api/admin/courses/${courseId}/quizzes`, { headers: getHeaders() });
          if (res.ok) {
            const data = await res.json();
            setCourseQuizzes(data);
            setSelectedCourseId(courseId);
          }
        } catch (e) {
          showNotify('Failed to load course details', 'error');
        }
      };

      const fetchAnnouncements = async () => {
        if (!token) return;
        setIsLoadingAnnouncements(true);
        try {
          const res = await fetch(`${API_BASE}/api/admin/announcements`, { headers: getHeaders() });
          if (res.ok) {
            const data = await res.json();
            setAnnouncements(data.announcements || []);
          }
        } catch (e) {
          showNotify('Failed to load campus notices', 'error');
        } finally {
          setIsLoadingAnnouncements(false);
        }
      };

      const fetchEconomy = async () => {
        if (!token) return;
        setIsLoadingEconomy(true);
        try {
          const res = await fetch(`${API_BASE}/api/admin/economy`, { headers: getHeaders() });
          if (res.ok) {
            const data = await res.json();
            setEconomyConfig(data.config || {});
          }
        } catch (e) {
          showNotify('Failed to load economy rates', 'error');
        } finally {
          setIsLoadingEconomy(false);
        }
      };

      const fetchEconomyStudents = async () => {
        if (!token) return;
        try {
          const res = await fetch(`${API_BASE}/api/admin/economy/students`, { headers: getHeaders() });
          if (res.ok) {
            const data = await res.json();
            setEconomyStudents(data.students || []);
          }
        } catch (e) {
          console.error(e);
        }
      };

      // Tab Trigger Effects
      useEffect(() => {
        if (token) {
          fetchStats();
          fetchCourses();
        }
      }, [token]);

      useEffect(() => {
        if (token && activeTab === 'users') fetchUsers();
      }, [token, activeTab, currentPage, userStatusFilter, userSortBy]);

      useEffect(() => {
        if (token && activeTab === 'announcements') fetchAnnouncements();
      }, [token, activeTab]);

      useEffect(() => {
        if (token && activeTab === 'economy') {
          fetchEconomy();
          fetchEconomyStudents();
        }
      }, [token, activeTab]);

      // Login Handler
      const handleLogin = async (e) => {
        e.preventDefault();
        setAuthError('');
        try {
          let payload = {};
          if (authKeyInput.trim()) {
            payload = { adminKey: authKeyInput.trim() };
          } else if (authEmailInput.trim() && authPassInput) {
            payload = { email: authEmailInput.trim(), password: authPassInput };
          } else {
            setAuthError('Please provide an Admin Secret Key or email & password');
            return;
          }

          const res = await fetch(`${API_BASE}/api/admin/login`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
          });
          const data = await res.json();

          if (res.ok && data.token) {
            localStorage.setItem('hunar_admin_token', data.token);
            setToken(data.token);
            setAdminUser(data.admin);
            showNotify('Authenticated successfully! Welcome, Administrator.');
          } else {
            setAuthError(data.error || 'Authentication failed. Check credentials.');
          }
        } catch (err) {
          setAuthError('Network error connecting to backend service.');
        }
      };

      const handleLogout = () => {
        localStorage.removeItem('hunar_admin_token');
        setToken('');
        setAdminUser(null);
        showNotify('Signed out of admin session');
      };

      // User Management Actions
      const handleToggleVerify = async (userId) => {
        try {
          const res = await fetch(`${API_BASE}/api/admin/users/${userId}/toggle-verify`, {
            method: 'PUT',
            headers: getHeaders()
          });
          if (res.ok) {
            const data = await res.json();
            showNotify(data.message || 'User verification updated');
            fetchUsers();
            fetchStats();
          } else {
            showNotify('Failed to toggle verification', 'error');
          }
        } catch (e) {
          showNotify('Error communicating with server', 'error');
        }
      };

      const handleDeleteUser = (user) => {
        triggerConfirm(
          'Delete Student Account',
          `Are you sure you want to permanently delete student '${user.username}' (${user.email})? This action cannot be undone.`,
          async () => {
            try {
              const res = await fetch(`${API_BASE}/api/admin/users/${user.id}`, {
                method: 'DELETE',
                headers: getHeaders()
              });
              if (res.ok) {
                showNotify('Student account safely deleted');
                fetchUsers();
                fetchStats();
              } else {
                showNotify('Failed to delete user', 'error');
              }
            } catch (e) {
              showNotify('Error deleting user', 'error');
            }
          },
          'Delete Account',
          true
        );
      };

      // Curriculum & Quiz Actions
      const handleInspectCourse = (courseId) => {
        fetchCourseQuizzes(courseId);
      };

      const handleEditQuiz = (quiz) => {
        setEditingQuiz({ ...quiz, options: [...quiz.options] });
        setIsQuizModalOpen(true);
      };

      const handleSaveQuiz = async () => {
        if (!editingQuiz) return;
        try {
          const res = await fetch(`${API_BASE}/api/admin/quizzes/${editingQuiz.id}`, {
            method: 'PUT',
            headers: getHeaders(),
            body: JSON.stringify({
              question: editingQuiz.question,
              options: editingQuiz.options,
              correctAnswer: editingQuiz.correctAnswer,
              explanation: editingQuiz.explanation
            })
          });
          if (res.ok) {
            showNotify('Quiz updated successfully');
            setIsQuizModalOpen(false);
            if (selectedCourseId) fetchCourseQuizzes(selectedCourseId);
          } else {
            showNotify('Failed to save quiz', 'error');
          }
        } catch (e) {
          showNotify('Error saving quiz', 'error');
        }
      };

      const handleDeleteQuiz = (quizId) => {
        triggerConfirm(
          'Delete Assessment Quiz',
          'Are you sure you want to delete this assessment question? It will be removed from all student exam pools.',
          async () => {
            try {
              const res = await fetch(`${API_BASE}/api/admin/quizzes/${quizId}`, {
                method: 'DELETE',
                headers: getHeaders()
              });
              if (res.ok) {
                showNotify('Quiz removed from syllabus');
                if (selectedCourseId) fetchCourseQuizzes(selectedCourseId);
                fetchStats();
              } else {
                showNotify('Failed to delete quiz', 'error');
              }
            } catch (e) {
              showNotify('Error deleting quiz', 'error');
            }
          },
          'Delete Quiz',
          true
        );
      };

      // Creator Studio Actions
      const handleCreateCourse = async (e) => {
        e.preventDefault();
        if (!creatorCourse.title.trim()) {
          showNotify('Course title is required', 'error');
          return;
        }
        setIsCreatingCourse(true);
        try {
          const res = await fetch(`${API_BASE}/api/admin/courses`, {
            method: 'POST',
            headers: getHeaders(),
            body: JSON.stringify(creatorCourse)
          });
          const data = await res.json();
          if (res.ok && data.course) {
            showNotify(`Course '${data.course.title}' created!`);
            fetchCourses();
            fetchStats();
            setCreatorStep({ ...creatorStep, courseId: data.course.id });
            setActiveStudioStep('step');
          } else {
            showNotify(data.error || 'Failed to create course', 'error');
          }
        } catch (e) {
          showNotify('Network error creating course', 'error');
        } finally {
          setIsCreatingCourse(false);
        }
      };

      const handleCreateStep = async (e) => {
        e.preventDefault();
        if (!creatorStep.courseId) {
          showNotify('Please select a parent course container', 'error');
          return;
        }
        if (!creatorStep.title.trim() || !creatorStep.content.trim()) {
          showNotify('Experiment title and content are required', 'error');
          return;
        }
        setIsCreatingStep(true);
        try {
          const res = await fetch(`${API_BASE}/api/admin/courses/${creatorStep.courseId}/steps`, {
            method: 'POST',
            headers: getHeaders(),
            body: JSON.stringify(creatorStep)
          });
          const data = await res.json();
          if (res.ok && data.step) {
            showNotify(`Lab Experiment '${data.step.title}' added with OBE tags!`);
            setSavedStep(data.step);
            setSavedStepQuizzes([]);
            setActiveStudioStep('quiz');
            fetchStats();
          } else {
            showNotify(data.error || 'Failed to add experiment step', 'error');
          }
        } catch (e) {
          showNotify('Network error adding lab experiment', 'error');
        } finally {
          setIsCreatingStep(false);
        }
      };

      const handleCreateStepQuiz = async (e) => {
        e.preventDefault();
        if (!savedStep) {
          showNotify('Save a lab experiment first before attaching quizzes', 'error');
          return;
        }
        if (!creatorQuiz.question.trim() || !creatorQuiz.correctAnswer.trim()) {
          showNotify('Question prompt and correct answer choice are required', 'error');
          return;
        }
        setIsCreatingQuiz(true);
        try {
          const res = await fetch(`${API_BASE}/api/admin/steps/${savedStep.id}/quizzes`, {
            method: 'POST',
            headers: getHeaders(),
            body: JSON.stringify(creatorQuiz)
          });
          const data = await res.json();
          if (res.ok && data.quiz) {
            showNotify('Assessment question attached to lab experiment!');
            setSavedStepQuizzes([...savedStepQuizzes, data.quiz]);
            setCreatorQuiz({
              question: '',
              options: ['', '', '', ''],
              correctAnswer: '',
              explanation: ''
            });
            fetchStats();
          } else {
            showNotify(data.error || 'Failed to attach quiz', 'error');
          }
        } catch (e) {
          showNotify('Network error attaching quiz', 'error');
        } finally {
          setIsCreatingQuiz(false);
        }
      };

      // Markdown Helper
      const insertMarkdownSnippet = (before, after) => {
        setCreatorStep(prev => ({
          ...prev,
          content: prev.content + `${before}Sample Text${after}`
        }));
      };

      const renderedMarkdown = useMemo(() => {
        if (!window.marked) return creatorStep.content;
        try {
          return window.marked.parse(creatorStep.content || '*Live markdown preview will appear here...*');
        } catch (e) {
          return creatorStep.content;
        }
      }, [creatorStep.content]);

      // Announcements Actions
      const handleCreateAnnouncement = async (e) => {
        e.preventDefault();
        if (!newAnnouncement.title.trim() || !newAnnouncement.message.trim()) {
          showNotify('Announcement title and message are required', 'error');
          return;
        }
        setIsPublishingAnnouncement(true);
        try {
          const res = await fetch(`${API_BASE}/api/admin/announcements`, {
            method: 'POST',
            headers: getHeaders(),
            body: JSON.stringify(newAnnouncement)
          });
          const data = await res.json();
          if (res.ok && data.announcement) {
            showNotify('Announcement published live to student mobile apps!');
            setNewAnnouncement({
              title: '',
              message: '',
              type: 'info',
              targetAudience: 'ALL',
              isActive: true
            });
            fetchAnnouncements();
            fetchStats();
          } else {
            showNotify(data.error || 'Failed to broadcast announcement', 'error');
          }
        } catch (e) {
          showNotify('Network error publishing announcement', 'error');
        } finally {
          setIsPublishingAnnouncement(false);
        }
      };

      const handleToggleAnnouncement = async (announcementId) => {
        try {
          const res = await fetch(`${API_BASE}/api/admin/announcements/${announcementId}/toggle`, {
            method: 'PUT',
            headers: getHeaders()
          });
          if (res.ok) {
            showNotify('Announcement active status toggled');
            fetchAnnouncements();
            fetchStats();
          }
        } catch (e) {
          showNotify('Failed to toggle status', 'error');
        }
      };

      const handleDeleteAnnouncement = (id, title) => {
        triggerConfirm(
          'Delete Campus Notice',
          `Are you sure you want to remove notice '${title}' from student feeds?`,
          async () => {
            try {
              const res = await fetch(`${API_BASE}/api/admin/announcements/${id}`, {
                method: 'DELETE',
                headers: getHeaders()
              });
              if (res.ok) {
                showNotify('Notice removed successfully');
                fetchAnnouncements();
                fetchStats();
              }
            } catch (e) {
              showNotify('Error deleting notice', 'error');
            }
          },
          'Delete Notice',
          true
        );
      };

      // Economy Controller Actions
      const handleSaveEconomyConfig = async (e) => {
        e.preventDefault();
        setIsSavingEconomy(true);
        try {
          const res = await fetch(`${API_BASE}/api/admin/economy`, {
            method: 'PUT',
            headers: getHeaders(),
            body: JSON.stringify(economyConfig)
          });
          const data = await res.json();
          if (res.ok) {
            showNotify('Economy reward multipliers updated in database!');
            setEconomyConfig(data.config || economyConfig);
          } else {
            showNotify(data.error || 'Failed to update rates', 'error');
          }
        } catch (e) {
          showNotify('Error saving economy multipliers', 'error');
        } finally {
          setIsSavingEconomy(false);
        }
      };

      const handleGrantReward = async (e) => {
        e.preventDefault();
        if (!grantForm.userId) {
          showNotify('Please select a target recipient or choose ALL ACTIVE STUDENTS', 'error');
          return;
        }
        if (!grantForm.reason.trim()) {
          showNotify('Please enter a reason or award title', 'error');
          return;
        }

        const isAirdrop = grantForm.userId === 'all';
        const confirmMsg = isAirdrop
          ? `Perform campus-wide airdrop granting +${grantForm.xp} XP and +${grantForm.coins} Coins to ALL active students?`
          : `Grant +${grantForm.xp} XP and +${grantForm.coins} Coins to selected student?`;

        triggerConfirm(
          isAirdrop ? 'Confirm Campus-Wide Airdrop' : 'Confirm Student Reward',
          confirmMsg,
          async () => {
            setIsGrantingReward(true);
            try {
              const endpoint = isAirdrop
                ? `${API_BASE}/api/admin/economy/grant-bulk`
                : `${API_BASE}/api/admin/economy/grant`;

              const res = await fetch(endpoint, {
                method: 'POST',
                headers: getHeaders(),
                body: JSON.stringify(grantForm)
              });
              const data = await res.json();
              if (res.ok) {
                showNotify(data.message || 'Reward credited successfully!');
                setGrantForm({ userId: '', xp: 100, coins: 50, reason: '' });
                fetchEconomyStudents();
                fetchStats();
              } else {
                showNotify(data.error || 'Failed to grant reward', 'error');
              }
            } catch (e) {
              showNotify('Network error granting reward', 'error');
            } finally {
              setIsGrantingReward(false);
            }
          },
          'Grant Rewards',
          false
        );
      };

      // Chart.js Velocity Rendering with Dual-Theme Adaptability
      const chartRef = useRef(null);
      useEffect(() => {
        if (activeTab === 'overview' && stats && stats.activityTimeline) {
          const ctx = document.getElementById('activityChart');
          if (ctx) {
            if (chartRef.current) chartRef.current.destroy();

            const isDark = theme === 'dark';
            const gridColor = isDark ? 'rgba(56, 189, 248, 0.08)' : 'rgba(0, 0, 0, 0.05)';
            const subGridColor = isDark ? 'rgba(56, 189, 248, 0.04)' : 'rgba(0, 0, 0, 0.02)';
            const tickColor = isDark ? '#94A3B8' : '#64748B';
            const tooltipBg = isDark ? '#0e2343' : '#FFFFFF';
            const tooltipTitle = isDark ? '#FFFFFF' : '#0F172A';
            const tooltipBody = isDark ? '#38BDF8' : '#0284C7';
            const tooltipBorder = isDark ? 'rgba(56, 189, 248, 0.3)' : '#CBD5E1';

            chartRef.current = new Chart(ctx, {
              type: 'line',
              data: {
                labels: stats.activityTimeline.map(t => t.day),
                datasets: [{
                  label: 'New Registrations',
                  data: stats.activityTimeline.map(t => t.users),
                  borderColor: isDark ? '#38BDF8' : '#0284C7',
                  backgroundColor: isDark ? 'rgba(56, 189, 248, 0.12)' : 'rgba(2, 132, 199, 0.08)',
                  borderWidth: 2.5,
                  fill: true,
                  tension: 0.35,
                  pointBackgroundColor: isDark ? '#38BDF8' : '#0284C7',
                  pointBorderColor: isDark ? '#061428' : '#FFFFFF',
                  pointBorderWidth: 2,
                  pointRadius: 4,
                  pointHoverRadius: 6
                }]
              },
              options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                  legend: { display: false },
                  tooltip: {
                    backgroundColor: tooltipBg,
                    titleColor: tooltipTitle,
                    bodyColor: tooltipBody,
                    borderColor: tooltipBorder,
                    borderWidth: 1,
                    padding: 12,
                    displayColors: false,
                    titleFont: { family: 'Inter', weight: 'bold', size: 12 },
                    bodyFont: { family: 'JetBrains Mono', size: 12 }
                  }
                },
                scales: {
                  y: {
                    beginAtZero: true,
                    ticks: { color: tickColor, font: { family: 'JetBrains Mono', size: 11 }, stepSize: 1 },
                    grid: { color: gridColor, drawBorder: false }
                  },
                  x: {
                    ticks: { color: tickColor, font: { family: 'Inter', size: 11 } },
                    grid: { color: subGridColor, drawBorder: false }
                  }
                }
              }
            });
          }
        }
      }, [stats, activeTab, theme]);

      // 4. LOGIN SCREEN (WHEN UNAUTHENTICATED)
      if (!token || !adminUser) {
        return (
          <div className={`min-h-screen flex items-center justify-center p-4 relative overflow-hidden transition-colors duration-200 ${
            theme === 'dark' ? 'dark bg-[#061428] text-slate-100' : 'light bg-[#F8FAFC] text-slate-800'
          }`}>
            {/* Ambient Background Glow Blobs */}
            <div className="absolute -top-36 -right-36 w-96 h-96 bg-gradient-to-br from-sky-500/15 via-teal-500/10 to-transparent dark:from-sky-500/20 dark:via-cyan-500/10 dark:to-transparent rounded-full blur-3xl pointer-events-none"></div>
            <div className="absolute -bottom-36 -left-36 w-96 h-96 bg-gradient-to-tr from-indigo-500/15 via-purple-500/10 to-transparent dark:from-indigo-600/20 dark:via-sky-600/10 dark:to-transparent rounded-full blur-3xl pointer-events-none"></div>

            {/* Top Right Theme Toggle Switcher */}
            <div className="absolute top-6 right-6 z-20">
              <button
                type="button"
                onClick={toggleTheme}
                title={theme === 'dark' ? 'Switch to Light Mode (☀️)' : 'Switch to Dark Mode (🌙)'}
                aria-label="Toggle Theme"
                className={`flex items-center space-x-2 px-3.5 py-1.5 rounded-xl border text-xs font-bold transition-all duration-200 shadow-sm cursor-pointer select-none active:scale-95 ${
                  theme === 'dark'
                    ? 'bg-[#0e2343] border-sky-500/25 text-amber-300 hover:text-amber-200 hover:border-sky-400/50 hover:bg-[#142c54] shadow-sky-950/40'
                    : 'bg-white border-slate-200 text-indigo-600 hover:text-indigo-800 hover:border-slate-300 hover:bg-slate-50 shadow-slate-200/60'
                }`}
              >
                <span className="text-sm leading-none">{theme === 'dark' ? '🌙' : '☀️'}</span>
                <span className="font-mono text-[11px] uppercase tracking-wider">{theme === 'dark' ? 'Dark' : 'Light'}</span>
              </button>
            </div>

            <div className="w-full max-w-md bg-white/95 dark:bg-[#0e2343]/90 backdrop-blur-2xl border border-slate-200 dark:border-sky-500/25 rounded-2xl p-8 shadow-2xl shadow-slate-200/60 dark:shadow-sky-950/60 relative z-10 transition-all">
              {/* Brand Header */}
              <div className="flex items-center space-x-3.5 mb-8">
                <div className="w-11 h-11 rounded-xl bg-gradient-to-br from-sky-500 to-indigo-600 flex items-center justify-center text-white text-xl shadow-md shadow-sky-500/25">
                  🥋
                </div>
                <div>
                  <h1 className="text-xl font-black tracking-tight text-slate-900 dark:text-white flex items-center space-x-2">
                    <span>Hunar Cycle</span>
                    <span className="text-[10px] font-mono px-2 py-0.5 rounded-full bg-emerald-500/15 text-emerald-600 dark:text-emerald-400 border border-emerald-500/30">v2.4</span>
                  </h1>
                  <p className="text-xs font-semibold text-slate-500 dark:text-slate-400">Executive Admin Operating System</p>
                </div>
              </div>

              {authError && (
                <div className="mb-6 p-4 bg-red-500/10 border border-red-500/30 rounded-xl text-red-600 dark:text-red-400 text-xs font-medium flex items-center space-x-2.5">
                  <span>⚠️</span>
                  <span>{authError}</span>
                </div>
              )}

              <form onSubmit={handleLogin} className="space-y-4">
                <div>
                  <label className="block text-xs font-bold uppercase tracking-wider text-slate-700 dark:text-slate-300 mb-2">
                    Master Admin Secret Key
                  </label>
                  <input
                    type="password"
                    placeholder="Enter Master Secret Key"
                    value={authKeyInput}
                    onChange={e => setAuthKeyInput(e.target.value)}
                    className="w-full px-4 py-3 bg-white dark:bg-[#07152b] border border-slate-200 dark:border-sky-500/25 rounded-xl text-xs font-mono text-slate-900 dark:text-white placeholder:text-slate-400 dark:placeholder:text-slate-500 focus:outline-none focus:border-sky-500 focus:ring-2 focus:ring-sky-500/30 transition shadow-sm"
                  />
                </div>

                <div className="flex items-center my-4">
                  <div className="flex-1 border-t border-slate-200 dark:border-sky-500/20"></div>
                  <span className="px-3 text-[11px] text-slate-400 dark:text-slate-500 font-extrabold uppercase tracking-wider">Or Credentials</span>
                  <div className="flex-1 border-t border-slate-200 dark:border-sky-500/20"></div>
                </div>

                <div>
                  <label className="block text-xs font-bold uppercase tracking-wider text-slate-700 dark:text-slate-300 mb-2">
                    Admin Email
                  </label>
                  <input
                    type="email"
                    placeholder="admin@hunarcycle.com"
                    value={authEmailInput}
                    onChange={e => setAuthEmailInput(e.target.value)}
                    className="w-full px-4 py-3 bg-white dark:bg-[#07152b] border border-slate-200 dark:border-sky-500/25 rounded-xl text-xs text-slate-900 dark:text-white placeholder:text-slate-400 dark:placeholder:text-slate-500 focus:outline-none focus:border-sky-500 focus:ring-2 focus:ring-sky-500/30 transition shadow-sm"
                  />
                </div>

                <div>
                  <label className="block text-xs font-bold uppercase tracking-wider text-slate-700 dark:text-slate-300 mb-2">
                    Password
                  </label>
                  <input
                    type="password"
                    placeholder="••••••••"
                    value={authPassInput}
                    onChange={e => setAuthPassInput(e.target.value)}
                    className="w-full px-4 py-3 bg-white dark:bg-[#07152b] border border-slate-200 dark:border-sky-500/25 rounded-xl text-xs text-slate-900 dark:text-white placeholder:text-slate-400 dark:placeholder:text-slate-500 focus:outline-none focus:border-sky-500 focus:ring-2 focus:ring-sky-500/30 transition shadow-sm"
                  />
                </div>

                <button
                  type="submit"
                  className="w-full py-3.5 bg-gradient-to-r from-sky-500 to-teal-400 hover:from-sky-400 hover:to-teal-300 font-bold text-slate-950 text-xs uppercase tracking-wider rounded-xl transition shadow-md shadow-sky-500/20 mt-3 active:scale-[0.98]"
                >
                  Authenticate & Unlock Dashboard ›
                </button>
              </form>

              <div className="mt-6 pt-5 border-t border-slate-200 dark:border-sky-500/20 flex items-center justify-between text-[11px] text-slate-500 dark:text-slate-400">
                <span className="flex items-center space-x-1.5">
                  <span className="w-2 h-2 rounded-full bg-emerald-500"></span>
                  <span>Neon PostgreSQL Active</span>
                </span>
                <span className="font-mono">SSL Encrypted</span>
              </div>
            </div>
          </div>
        );
      }

      // 5. MAIN EXECUTIVE DASHBOARD VIEW
      return (
        <div className={`min-h-screen flex flex-col md:flex-row relative transition-colors duration-200 ${
          theme === 'dark'
            ? 'dark bg-[#061428] text-slate-100 selection:bg-sky-500 selection:text-slate-950'
            : 'light bg-[#F8FAFC] text-slate-800 selection:bg-sky-500 selection:text-white'
        }`}>
          {/* Ambient Background Gradient Glow Blobs */}
          <div className="fixed -top-40 -right-40 w-[550px] h-[550px] bg-gradient-to-br from-sky-500/10 via-teal-500/5 to-transparent dark:from-sky-500/15 dark:via-cyan-500/10 dark:to-transparent rounded-full blur-3xl pointer-events-none -z-0"></div>
          <div className="fixed -bottom-40 -left-40 w-[550px] h-[550px] bg-gradient-to-tr from-indigo-500/10 via-purple-500/5 to-transparent dark:from-indigo-600/15 dark:via-sky-600/10 dark:to-transparent rounded-full blur-3xl pointer-events-none -z-0"></div>

          {/* Floating Toast Notification System */}
          {notification && (
            <div className={`fixed top-6 right-6 z-50 px-5 py-3.5 rounded-2xl shadow-2xl border text-xs font-bold flex items-center space-x-3 transition-all duration-300 animate-toast-down backdrop-blur-xl ${
              notification.type === 'error'
                ? 'bg-red-950/95 border-red-500/40 text-red-300 shadow-red-950/40'
                : theme === 'dark'
                  ? 'bg-[#0e2343]/95 border-emerald-500/40 text-emerald-300 shadow-sky-950/50'
                  : 'bg-white/95 border-emerald-500/40 text-emerald-800 shadow-slate-300/80'
            }`}>
              <span className="text-base">{notification.type === 'error' ? '⚠️' : '✅'}</span>
              <span className="leading-snug">{notification.msg}</span>
              <button onClick={() => setNotification(null)} className="ml-2 text-slate-400 hover:text-white dark:hover:text-white transition">✕</button>
            </div>
          )}

          {/* SIDEBAR NAVIGATION */}
          <aside className="w-full md:w-72 bg-white/95 dark:bg-[#0a1c38]/95 backdrop-blur-2xl border-r border-slate-200 dark:border-sky-500/15 flex flex-col shrink-0 relative z-20 shadow-xl shadow-slate-200/50 dark:shadow-sky-950/50">
            {/* Branding Header */}
            <div className="p-6 border-b border-slate-200 dark:border-sky-500/15">
              <div className="flex items-center space-x-3.5">
                <div className="w-10 h-10 rounded-xl bg-gradient-to-br from-sky-500 to-indigo-600 flex items-center justify-center text-white text-lg font-bold shadow-md shadow-sky-500/25">
                  🥋
                </div>
                <div>
                  <h2 className="text-base font-bold text-slate-900 dark:text-white tracking-tight leading-snug">Hunar Cycle</h2>
                  <div className="flex items-center space-x-1.5 mt-0.5">
                    <span className="relative flex h-2 w-2">
                      <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-500 opacity-75"></span>
                      <span className="relative inline-flex rounded-full h-2 w-2 bg-emerald-500"></span>
                    </span>
                    <span className="text-[10px] font-extrabold uppercase tracking-wider text-emerald-600 dark:text-emerald-400 font-mono">
                      ADMIN LIVE
                    </span>
                    <span className="text-[10px] text-slate-400 dark:text-slate-500 font-mono">• v2.4</span>
                  </div>
                </div>
              </div>

              {/* Database indicator pill */}
              <div className="mt-4 px-3 py-2 bg-slate-50 dark:bg-[#07162e] rounded-xl border border-slate-200 dark:border-sky-500/20 flex items-center justify-between text-xs">
                <span className="text-[10px] font-bold text-slate-500 dark:text-slate-400 uppercase tracking-wider">Cloud Storage</span>
                <span className="text-[11px] font-mono text-emerald-600 dark:text-emerald-400 font-bold flex items-center space-x-1.5">
                  <span>🐘</span>
                  <span>Neon PostgreSQL</span>
                </span>
              </div>
            </div>

            {/* Navigation Tabs */}
            <nav className="p-3.5 space-y-1.5 flex-1">
              {[
                { id: 'overview', icon: '📊', label: 'Platform Analytics', badge: 'LIVE', badgeColor: 'bg-emerald-500/15 text-emerald-600 dark:text-emerald-400 border-emerald-500/30' },
                { id: 'users', icon: '👥', label: 'Student Management', badge: stats ? `${stats.totalUsers}` : '', badgeColor: 'bg-slate-200 dark:bg-[#142c54] text-slate-700 dark:text-slate-300 border-slate-300 dark:border-sky-500/20' },
                { id: 'curriculum', icon: '🎓', label: 'University Curricula', badge: '9 OBE', badgeColor: 'bg-sky-500/15 text-sky-600 dark:text-sky-400 border-sky-500/30' },
                { id: 'creator', icon: '🛠️', label: 'Course & Lab Creator Studio', badge: 'STUDIO', badgeColor: 'bg-purple-500/15 text-purple-600 dark:text-purple-400 border-purple-500/30' },
                { id: 'announcements', icon: '📢', label: 'Campus Notices', badge: announcements.filter(a => a.isActive).length > 0 ? `${announcements.filter(a => a.isActive).length} Live` : '', badgeColor: 'bg-emerald-500/15 text-emerald-600 dark:text-emerald-400 border-emerald-500/30' },
                { id: 'economy', icon: '🪙', label: 'Economy & Rewards', badge: 'RATES', badgeColor: 'bg-amber-500/15 text-amber-600 dark:text-amber-400 border-amber-500/30' },
              ].map(item => {
                const isActive = activeTab === item.id;
                return (
                  <button
                    key={item.id}
                    onClick={() => {
                      setActiveTab(item.id);
                      if (item.id === 'curriculum') setSelectedCourseId(null);
                    }}
                    className={`w-full flex items-center space-x-3 px-3.5 py-3 rounded-xl text-xs transition-all duration-200 relative group ${
                      isActive
                        ? 'bg-sky-500/10 dark:bg-gradient-to-r dark:from-sky-500/20 dark:to-teal-500/10 text-sky-700 dark:text-sky-300 font-bold border-l-4 border-sky-500 shadow-sm shadow-sky-500/10'
                        : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-slate-100 hover:bg-slate-100/80 dark:hover:bg-[#0e2343]/60 font-semibold'
                    }`}
                  >
                    <span className="text-base">{item.icon}</span>
                    <span className="flex-1 text-left">{item.label}</span>
                    {item.badge && (
                      <span className={`text-[10px] px-2 py-0.5 rounded-full font-extrabold border ${item.badgeColor}`}>
                        {item.badge}
                      </span>
                    )}
                  </button>
                );
              })}
            </nav>

            {/* Admin Profile Footer */}
            <div className="p-4 border-t border-slate-200 dark:border-sky-500/15 bg-slate-50/70 dark:bg-[#07162e]/70 flex items-center justify-between">
              <div className="flex items-center space-x-3 overflow-hidden">
                <div className="w-9 h-9 rounded-xl bg-gradient-to-br from-sky-400 to-indigo-500 text-white flex items-center justify-center font-bold text-xs shrink-0 shadow-sm">
                  {(adminUser?.username || 'A')[0].toUpperCase()}
                </div>
                <div className="overflow-hidden">
                  <p className="text-xs font-bold text-slate-900 dark:text-white truncate">{adminUser?.username || 'Administrator'}</p>
                  <p className="text-[10px] text-slate-500 dark:text-slate-400 truncate font-mono">{adminUser?.email || 'admin'}</p>
                </div>
              </div>
              <button
                onClick={handleLogout}
                title="Sign out of Admin Session"
                className="text-xs font-bold text-red-500 dark:text-red-400 hover:text-red-700 dark:hover:text-red-300 px-2.5 py-1.5 rounded-lg hover:bg-red-500/10 transition"
              >
                Sign Out
              </button>
            </div>
          </aside>

          {/* MAIN CONTENT AREA */}
          <main className="flex-1 flex flex-col overflow-y-auto bg-transparent relative min-h-screen">
            {/* Top Bar Header */}
            <header className="h-16 px-8 flex items-center justify-between border-b border-slate-200 dark:border-sky-500/15 bg-white/85 dark:bg-[#061428]/85 backdrop-blur-xl sticky top-0 z-30 transition-colors">
              {/* Breadcrumb Trail */}
              <div className="flex items-center space-x-2 text-xs">
                <div className="flex items-center space-x-1.5">
                  <span className="w-2 h-2 rounded-full bg-sky-500"></span>
                  <span className="font-semibold text-slate-500 dark:text-slate-400">Hunar Cycle</span>
                </div>
                <span className="text-slate-300 dark:text-slate-600 font-mono">/</span>
                <span className="font-bold text-slate-900 dark:text-white text-sm tracking-tight">
                  {activeTab === 'overview' && 'Platform Analytics & Overview'}
                  {activeTab === 'users' && 'Student Management & Verification'}
                  {activeTab === 'curriculum' && 'University Curricula & OBE Mapping'}
                  {activeTab === 'creator' && 'Course & Lab Content Creator Studio'}
                  {activeTab === 'announcements' && 'Campus Announcements & Notice Board'}
                  {activeTab === 'economy' && 'Platform Game Economy & Reward Control'}
                </span>
              </div>

              {/* Header Right Actions */}
              <div className="flex items-center space-x-3.5">
                {/* Neon PostgreSQL Health Pill */}
                <div className="flex items-center space-x-2 px-3 py-1.5 rounded-full text-xs font-semibold border bg-emerald-500/10 dark:bg-emerald-500/15 border-emerald-500/30 text-emerald-700 dark:text-emerald-300 shadow-sm">
                  <span className="relative flex h-2 w-2">
                    <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
                    <span className="relative inline-flex rounded-full h-2 w-2 bg-emerald-500"></span>
                  </span>
                  <span>Neon Connected</span>
                </div>

                {/* Master Theme Toggle Button */}
                <button
                  type="button"
                  onClick={toggleTheme}
                  title={theme === 'dark' ? 'Switch to Light Mode (☀️)' : 'Switch to Dark Mode (🌙)'}
                  aria-label="Toggle Theme"
                  className={`group flex items-center space-x-2 px-3.5 py-1.5 rounded-xl border text-xs font-bold transition-all duration-200 cursor-pointer select-none active:scale-95 shadow-sm ${
                    theme === 'dark'
                      ? 'bg-[#0e2343] border-sky-500/25 text-amber-300 hover:text-amber-200 hover:border-sky-400/50 hover:bg-[#142c54] shadow-sky-950/40'
                      : 'bg-white border-slate-200 text-indigo-600 hover:text-indigo-800 hover:border-slate-300 hover:bg-slate-50 shadow-slate-200/60'
                  }`}
                >
                  <span className="text-sm leading-none transition-transform duration-300 transform group-hover:rotate-12">
                    {theme === 'dark' ? '🌙' : '☀️'}
                  </span>
                  <span className="font-mono text-[11px] uppercase tracking-wider">
                    {theme === 'dark' ? 'Dark' : 'Light'}
                  </span>
                </button>

                {/* Admin Profile & Quick Logout */}
                <div className="flex items-center space-x-2.5 pl-2 border-l border-slate-200 dark:border-sky-500/15">
                  <div className="relative">
                    <div className="w-8 h-8 rounded-full bg-gradient-to-tr from-sky-400 to-indigo-500 flex items-center justify-center text-white font-bold text-xs shadow-sm">
                      {(adminUser?.username || 'A')[0].toUpperCase()}
                    </div>
                    <span className="absolute -bottom-0.5 -right-0.5 w-2.5 h-2.5 bg-emerald-500 rounded-full ring-2 ring-white dark:ring-[#061428]"></span>
                  </div>
                  <button
                    onClick={handleLogout}
                    title="Sign Out of Session"
                    className="p-1.5 text-slate-400 hover:text-red-500 dark:hover:text-red-400 rounded-lg hover:bg-red-500/10 transition"
                  >
                    <span className="text-sm">🚪</span>
                  </button>
                </div>
              </div>
            </header>

            {/* Dashboard Content Container */}
            <div className="p-8 space-y-8 flex-1 max-w-7xl w-full mx-auto relative z-10">
              {/* TAB 1: OVERVIEW / ANALYTICS */}
              {activeTab === 'overview' && stats && (
                <div className="space-y-8">
                  {/* Hero 4-Card KPI Grid */}
                  <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
                    {/* Card 1: Total Users */}
                    <div className="bg-white dark:bg-[#0e2343]/90 border border-slate-200 dark:border-sky-500/20 shadow-sm dark:shadow-xl dark:shadow-sky-950/40 rounded-2xl p-6 relative overflow-hidden transition-all duration-300 hover:-translate-y-0.5 backdrop-blur-md">
                      <div className="flex items-center justify-between mb-3">
                        <span className="text-xs font-bold text-slate-500 dark:text-slate-400 uppercase tracking-wider">Total Students</span>
                        <div className="w-10 h-10 rounded-xl bg-emerald-500/10 border border-emerald-500/20 flex items-center justify-center text-emerald-600 dark:text-emerald-400 text-lg">
                          👥
                        </div>
                      </div>
                      <div className="text-3xl font-black text-slate-900 dark:text-white tracking-tight">{stats.totalUsers}</div>
                      <div className="mt-3 flex items-center justify-between text-xs font-semibold">
                        <span className="text-emerald-600 dark:text-emerald-400 flex items-center space-x-1">
                          <span>●</span>
                          <span>{stats.verifiedUsers} Verified ({stats.verifiedPercentage}%)</span>
                        </span>
                        <span className="text-[10px] font-extrabold px-2 py-0.5 rounded-full bg-emerald-500/10 text-emerald-600 dark:text-emerald-400 border border-emerald-500/20">
                          +14.8% MoM
                        </span>
                      </div>
                    </div>

                    {/* Card 2: Academic Courses */}
                    <div className="bg-white dark:bg-[#0e2343]/90 border border-slate-200 dark:border-sky-500/20 shadow-sm dark:shadow-xl dark:shadow-sky-950/40 rounded-2xl p-6 relative overflow-hidden transition-all duration-300 hover:-translate-y-0.5 backdrop-blur-md">
                      <div className="flex items-center justify-between mb-3">
                        <span className="text-xs font-bold text-slate-500 dark:text-slate-400 uppercase tracking-wider">Academic Modules</span>
                        <div className="w-10 h-10 rounded-xl bg-sky-500/10 border border-sky-500/20 flex items-center justify-center text-sky-600 dark:text-sky-400 text-lg">
                          🎓
                        </div>
                      </div>
                      <div className="text-3xl font-black text-slate-900 dark:text-white tracking-tight">
                        {stats.universityCourses} <span className="text-sm font-semibold text-slate-400">/ {stats.totalCourses} total</span>
                      </div>
                      <div className="mt-3 flex items-center justify-between text-xs font-semibold">
                        <span className="text-sky-600 dark:text-sky-400 flex items-center space-x-1">
                          <span>●</span>
                          <span>{stats.totalSteps} Lab Experiments</span>
                        </span>
                        <span className="text-[10px] font-extrabold px-2 py-0.5 rounded-full bg-sky-500/10 text-sky-600 dark:text-sky-400 border border-sky-500/20">
                          100% OBE
                        </span>
                      </div>
                    </div>

                    {/* Card 3: Assessment Quizzes & Flashcards */}
                    <div className="bg-white dark:bg-[#0e2343]/90 border border-slate-200 dark:border-sky-500/20 shadow-sm dark:shadow-xl dark:shadow-sky-950/40 rounded-2xl p-6 relative overflow-hidden transition-all duration-300 hover:-translate-y-0.5 backdrop-blur-md">
                      <div className="flex items-center justify-between mb-3">
                        <span className="text-xs font-bold text-slate-500 dark:text-slate-400 uppercase tracking-wider">Quizzes & Cards</span>
                        <div className="w-10 h-10 rounded-xl bg-amber-500/10 border border-amber-500/20 flex items-center justify-center text-amber-600 dark:text-amber-400 text-lg">
                          📝
                        </div>
                      </div>
                      <div className="text-3xl font-black text-slate-900 dark:text-white tracking-tight">
                        {stats.totalQuizzes} <span className="text-sm font-semibold text-slate-400">Quizzes</span>
                      </div>
                      <div className="mt-3 flex items-center justify-between text-xs font-semibold">
                        <span className="text-amber-600 dark:text-amber-400 flex items-center space-x-1">
                          <span>●</span>
                          <span>{stats.totalFlashcards} Flashcards Indexed</span>
                        </span>
                        <span className="text-[10px] font-extrabold px-2 py-0.5 rounded-full bg-amber-500/10 text-amber-600 dark:text-amber-400 border border-amber-500/20">
                          Indexed
                        </span>
                      </div>
                    </div>

                    {/* Card 4: Accreditations */}
                    <div className="bg-white dark:bg-[#0e2343]/90 border border-slate-200 dark:border-sky-500/20 shadow-sm dark:shadow-xl dark:shadow-sky-950/40 rounded-2xl p-6 relative overflow-hidden transition-all duration-300 hover:-translate-y-0.5 backdrop-blur-md">
                      <div className="flex items-center justify-between mb-3">
                        <span className="text-xs font-bold text-slate-500 dark:text-slate-400 uppercase tracking-wider">Accreditations</span>
                        <div className="w-10 h-10 rounded-xl bg-purple-500/10 border border-purple-500/20 flex items-center justify-center text-purple-600 dark:text-purple-400 text-lg">
                          🏆
                        </div>
                      </div>
                      <div className="text-3xl font-black text-slate-900 dark:text-white tracking-tight">{stats.certificatesIssued}</div>
                      <div className="mt-3 flex items-center justify-between text-xs font-semibold">
                        <span className="text-purple-600 dark:text-purple-400 flex items-center space-x-1">
                          <span>●</span>
                          <span>{(stats.totalXpAwarded || 0).toLocaleString()} XP Awarded</span>
                        </span>
                        <span className="text-[10px] font-extrabold px-2 py-0.5 rounded-full bg-purple-500/10 text-purple-600 dark:text-purple-400 border border-purple-500/20">
                          Mastery
                        </span>
                      </div>
                    </div>
                  </div>

                  {/* Secondary Quick Metrics Strip */}
                  <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
                    <div className="p-4 bg-white dark:bg-[#0e2343]/90 rounded-2xl border border-slate-200 dark:border-sky-500/20 shadow-sm dark:shadow-lg dark:shadow-sky-950/30 backdrop-blur-md flex items-center space-x-3">
                      <span className="text-xl">🔥</span>
                      <div>
                        <div className="text-[10px] font-bold text-slate-500 dark:text-slate-400 uppercase">30-Day Active</div>
                        <div className="text-base font-bold text-slate-900 dark:text-white">{stats.activeUsers} Students</div>
                      </div>
                    </div>
                    <div className="p-4 bg-white dark:bg-[#0e2343]/90 rounded-2xl border border-slate-200 dark:border-sky-500/20 shadow-sm dark:shadow-lg dark:shadow-sky-950/30 backdrop-blur-md flex items-center space-x-3">
                      <span className="text-xl">🪙</span>
                      <div>
                        <div className="text-[10px] font-bold text-slate-500 dark:text-slate-400 uppercase">Coins in Circulation</div>
                        <div className="text-base font-bold text-emerald-600 dark:text-emerald-400">{(stats.totalCoinsInCirculation || 0).toLocaleString()}</div>
                      </div>
                    </div>
                    <div className="p-4 bg-white dark:bg-[#0e2343]/90 rounded-2xl border border-slate-200 dark:border-sky-500/20 shadow-sm dark:shadow-lg dark:shadow-sky-950/30 backdrop-blur-md flex items-center space-x-3">
                      <span className="text-xl">📢</span>
                      <div>
                        <div className="text-[10px] font-bold text-slate-500 dark:text-slate-400 uppercase">Platform Notices</div>
                        <div className="text-base font-bold text-sky-600 dark:text-sky-400">{stats.activeAnnouncements || 0} Live / {stats.totalAnnouncements || 0} Total</div>
                      </div>
                    </div>
                    <div className="p-4 bg-white dark:bg-[#0e2343]/90 rounded-2xl border border-slate-200 dark:border-sky-500/20 shadow-sm dark:shadow-lg dark:shadow-sky-950/30 backdrop-blur-md flex items-center space-x-3">
                      <span className="text-xl">⚡</span>
                      <div>
                        <div className="text-[10px] font-bold text-slate-500 dark:text-slate-400 uppercase">Server Sync</div>
                        <div className="text-base font-bold text-slate-900 dark:text-white font-mono">100% Real-Time</div>
                      </div>
                    </div>
                  </div>

                  {/* Charts & Breakdown Section */}
                  <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
                    {/* Activity Line Chart */}
                    <div className="lg:col-span-2 bg-white dark:bg-[#0e2343]/90 border border-slate-200 dark:border-sky-500/20 rounded-2xl shadow-sm dark:shadow-xl dark:shadow-sky-950/40 backdrop-blur-md p-6">
                      <div className="flex items-center justify-between mb-6">
                        <div>
                          <h3 className="text-base font-bold text-slate-900 dark:text-white">7-Day Registration Velocity</h3>
                          <p className="text-xs text-slate-500 dark:text-slate-400">New student sign-ups across computer science departments</p>
                        </div>
                        <span className="text-[10px] font-extrabold text-emerald-600 dark:text-emerald-400 bg-emerald-500/10 px-3 py-1 rounded-full border border-emerald-500/30">
                          ● REAL-TIME TREND
                        </span>
                      </div>
                      <div className="h-64">
                        <canvas id="activityChart"></canvas>
                      </div>
                    </div>

                    {/* Breakdown & OBE Card */}
                    <div className="bg-white dark:bg-[#0e2343]/90 border border-slate-200 dark:border-sky-500/20 rounded-2xl shadow-sm dark:shadow-xl dark:shadow-sky-950/40 backdrop-blur-md p-6 space-y-5 flex flex-col justify-between">
                      <div>
                        <h3 className="text-base font-bold text-slate-900 dark:text-white">Curriculum Distribution</h3>
                        <p className="text-xs text-slate-500 dark:text-slate-400">Accredited categories vs. technical tracks</p>
                      </div>

                      <div className="space-y-3 flex-1">
                        {stats.categoryBreakdown && stats.categoryBreakdown.slice(0, 5).map(cat => (
                          <div key={cat.category} className="space-y-1">
                            <div className="flex justify-between text-xs font-bold">
                              <span className="text-slate-700 dark:text-slate-300">{cat.category}</span>
                              <span className="text-emerald-600 dark:text-emerald-400 font-mono">{cat.count} courses</span>
                            </div>
                            <div className="w-full bg-slate-100 dark:bg-slate-800 h-2 rounded-full overflow-hidden">
                              <div
                                className="bg-gradient-to-r from-emerald-500 to-sky-500 h-full rounded-full transition-all duration-500"
                                style={{ width: `${Math.min(100, (cat.count / stats.totalCourses) * 100)}%` }}
                              ></div>
                            </div>
                          </div>
                        ))}
                      </div>

                      <div className="pt-4 border-t border-slate-200 dark:border-sky-500/20">
                        <div className="flex items-center justify-between text-xs font-bold text-slate-700 dark:text-slate-300 mb-1.5">
                          <span>HEC / OBE Compliance</span>
                          <span className="text-emerald-600 dark:text-emerald-400 font-extrabold">100% Certified</span>
                        </div>
                        <p className="text-[11px] text-slate-500 leading-relaxed">
                          All 9 university lab manuals transcribed verbatim with CLO/PLO outcome matrices and taxonomy domains.
                        </p>
                      </div>
                    </div>
                  </div>
                </div>
              )}

              {/* TAB 2: USER MANAGEMENT & DATA TABLES */}
              {activeTab === 'users' && (
                <div className="space-y-6">
                  {/* Controls Row */}
                  <div className="bg-white dark:bg-[#0e2343]/90 border border-slate-200 dark:border-sky-500/20 rounded-2xl shadow-sm dark:shadow-xl dark:shadow-sky-950/40 backdrop-blur-md p-5 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
                    <div className="flex items-center space-x-3 flex-1 max-w-md">
                      <div className="relative w-full">
                        <span className="absolute left-3.5 top-3 text-slate-400 text-xs">🔍</span>
                        <input
                          type="text"
                          placeholder="Search student username or email..."
                          value={userSearch}
                          onChange={e => { setUserSearch(e.target.value); setCurrentPage(1); }}
                          className="w-full pl-9 pr-4 py-2.5 bg-slate-50 dark:bg-[#07152b] border border-slate-200 dark:border-sky-500/20 rounded-xl text-xs text-slate-900 dark:text-white placeholder:text-slate-400 dark:placeholder:text-slate-500 focus:outline-none focus:border-sky-500 focus:ring-2 focus:ring-sky-500/25 transition"
                        />
                      </div>
                    </div>

                    <div className="flex flex-wrap items-center gap-3">
                      <select
                        value={userStatusFilter}
                        onChange={e => { setUserStatusFilter(e.target.value); setCurrentPage(1); }}
                        className="px-3.5 py-2.5 bg-slate-50 dark:bg-[#07152b] border border-slate-200 dark:border-sky-500/20 rounded-xl text-xs font-bold text-slate-700 dark:text-slate-300 focus:outline-none focus:border-sky-500 transition"
                      >
                        <option value="all">All Verification Statuses</option>
                        <option value="verified">Verified Only</option>
                        <option value="unverified">Unverified / Pending</option>
                      </select>

                      <select
                        value={userSortBy}
                        onChange={e => { setUserSortBy(e.target.value); setCurrentPage(1); }}
                        className="px-3.5 py-2.5 bg-slate-50 dark:bg-[#07152b] border border-slate-200 dark:border-sky-500/20 rounded-xl text-xs font-bold text-slate-700 dark:text-slate-300 focus:outline-none focus:border-sky-500 transition"
                      >
                        <option value="createdAt">Sort: Registration Date</option>
                        <option value="xp">Sort: Total XP</option>
                        <option value="level">Sort: Student Level</option>
                        <option value="loginStreak">Sort: Active Streak</option>
                      </select>

                      <button
                        onClick={fetchUsers}
                        className="px-4 py-2.5 bg-gradient-to-r from-sky-500 to-indigo-600 hover:from-sky-400 hover:to-indigo-500 text-white font-bold rounded-xl text-xs transition flex items-center space-x-1.5 shadow-sm active:scale-95"
                      >
                        <span>🔄</span>
                        <span>Refresh</span>
                      </button>
                    </div>
                  </div>

                  {/* Users Table */}
                  <div className="bg-white dark:bg-[#0e2343]/90 border border-slate-200 dark:border-sky-500/20 rounded-2xl shadow-sm dark:shadow-xl dark:shadow-sky-950/40 backdrop-blur-md overflow-hidden">
                    <div className="overflow-x-auto">
                      <table className="w-full text-left text-xs">
                        <thead className="bg-slate-50 dark:bg-[#0a1c38] border-b border-slate-200 dark:border-sky-500/20 text-[11px] font-bold text-slate-500 dark:text-slate-400 uppercase tracking-wider sticky top-0 z-10">
                          <tr>
                            <th className="px-6 py-4">Student Profile</th>
                            <th className="px-6 py-4">Level & XP</th>
                            <th className="px-6 py-4">Status</th>
                            <th className="px-6 py-4">Labs Mastery</th>
                            <th className="px-6 py-4">Registered</th>
                            <th className="px-6 py-4 text-right">Actions</th>
                          </tr>
                        </thead>
                        <tbody className="divide-y divide-slate-100 dark:divide-sky-500/10 font-medium">
                          {isLoading ? (
                            <tr>
                              <td colSpan="6" className="text-center py-12 text-slate-400">
                                <div className="flex items-center justify-center space-x-2">
                                  <div className="w-4 h-4 border-2 border-sky-500 border-t-transparent rounded-full animate-spin"></div>
                                  <span>Loading student records...</span>
                                </div>
                              </td>
                            </tr>
                          ) : usersData.users.length === 0 ? (
                            <tr>
                              <td colSpan="6" className="text-center py-12 text-slate-400">
                                No matching student records found.
                              </td>
                            </tr>
                          ) : (
                            usersData.users.map(u => (
                              <tr key={u.id} className="hover:bg-slate-50/80 dark:hover:bg-[#142c54]/50 transition-colors">
                                <td className="px-6 py-4">
                                  <div className="flex items-center space-x-3">
                                    <div className="w-9 h-9 rounded-xl bg-gradient-to-br from-sky-400 to-indigo-500 text-white ring-2 ring-sky-400/30 flex items-center justify-center font-bold text-xs shadow-sm">
                                      {u.username[0].toUpperCase()}
                                    </div>
                                    <div>
                                      <div className="font-bold text-slate-900 dark:text-white text-xs">{u.username}</div>
                                      <div className="text-[11px] text-slate-500 dark:text-slate-400 font-mono">{u.email}</div>
                                    </div>
                                  </div>
                                </td>
                                <td className="px-6 py-4">
                                  <div className="font-bold text-amber-500 dark:text-amber-400">LV {u.level}</div>
                                  <div className="text-[11px] text-slate-500 dark:text-slate-400 font-mono">{u.xp} XP • {u.coins} Coins</div>
                                </td>
                                <td className="px-6 py-4">
                                  {u.isVerified ? (
                                    <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-[10px] font-extrabold bg-emerald-500/15 text-emerald-600 dark:text-emerald-400 border border-emerald-500/30">
                                      ✓ Verified
                                    </span>
                                  ) : (
                                    <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-[10px] font-extrabold bg-amber-500/15 text-amber-600 dark:text-amber-400 border border-amber-500/30">
                                      Pending OTP
                                    </span>
                                  )}
                                </td>
                                <td className="px-6 py-4">
                                  <div className="font-bold text-slate-700 dark:text-slate-300">
                                    {u.activeCoursesCount} Active / {u.completedCoursesCount} Mastered
                                  </div>
                                  <div className="text-[11px] text-slate-500">🔥 Streak: {u.loginStreak} days</div>
                                </td>
                                <td className="px-6 py-4 text-slate-500 dark:text-slate-400 font-mono text-[11px]">
                                  {u.createdAt ? new Date(u.createdAt).toLocaleDateString() : 'N/A'}
                                </td>
                                <td className="px-6 py-4 text-right space-x-2">
                                  <button
                                    onClick={() => handleToggleVerify(u.id)}
                                    title={u.isVerified ? 'Mark as Unverified' : 'Verify Student Email'}
                                    className={`px-3 py-1.5 rounded-xl text-xs font-bold transition border ${
                                      u.isVerified
                                        ? 'bg-amber-500/10 text-amber-600 dark:text-amber-300 border-amber-500/30 hover:bg-amber-500/20'
                                        : 'bg-emerald-500/10 text-emerald-600 dark:text-emerald-300 border-emerald-500/30 hover:bg-emerald-500/20'
                                    }`}
                                  >
                                    {u.isVerified ? 'Unverify' : 'Verify'}
                                  </button>
                                  <button
                                    onClick={() => handleDeleteUser(u)}
                                    title="Permanently Delete Account"
                                    className="px-2.5 py-1.5 rounded-xl text-xs font-bold bg-red-500/10 text-red-600 dark:text-red-400 border border-red-500/30 hover:bg-red-500/20 transition"
                                  >
                                    Delete
                                  </button>
                                </td>
                              </tr>
                            ))
                          )}
                        </tbody>
                      </table>
                    </div>

                    {/* Pagination Bar */}
                    <div className="p-4 border-t border-slate-200 dark:border-sky-500/20 bg-slate-50/70 dark:bg-[#0a1c38]/70 flex items-center justify-between text-xs text-slate-600 dark:text-slate-400">
                      <div>
                        Showing page <span className="font-bold text-slate-900 dark:text-white">{usersData.page}</span> of <span className="font-bold text-slate-900 dark:text-white">{usersData.totalPages}</span> ({usersData.total} total students)
                      </div>
                      <div className="flex space-x-2">
                        <button
                          disabled={usersData.page <= 1}
                          onClick={() => setCurrentPage(prev => Math.max(1, prev - 1))}
                          className="px-3.5 py-1.5 bg-white dark:bg-[#07152b] border border-slate-200 dark:border-sky-500/20 rounded-xl font-bold disabled:opacity-40 hover:bg-slate-100 dark:hover:bg-[#142c54] transition shadow-sm"
                        >
                          ‹ Previous
                        </button>
                        <button
                          disabled={usersData.page >= usersData.totalPages}
                          onClick={() => setCurrentPage(prev => Math.min(usersData.totalPages, prev + 1))}
                          className="px-3.5 py-1.5 bg-white dark:bg-[#07152b] border border-slate-200 dark:border-sky-500/20 rounded-xl font-bold disabled:opacity-40 hover:bg-slate-100 dark:hover:bg-[#142c54] transition shadow-sm"
                        >
                          Next ›
                        </button>
                      </div>
                    </div>
                  </div>
                </div>
              )}

              {/* TAB 3: UNIVERSITY CURRICULA & OBE MAPPING */}
              {activeTab === 'curriculum' && (
                <div className="space-y-6">
                  {selectedCourseId && courseQuizzes ? (
                    <div className="space-y-6">
                      <button
                        onClick={() => setSelectedCourseId(null)}
                        className="px-4 py-2 bg-white dark:bg-[#07152b] border border-slate-200 dark:border-sky-500/20 rounded-xl text-xs font-bold text-slate-700 dark:text-slate-300 hover:text-sky-600 dark:hover:text-white transition flex items-center space-x-1.5 shadow-sm"
                      >
                        <span>‹</span>
                        <span>Back to All 9 University Courses</span>
                      </button>

                      {/* Course Detailed Header */}
                      <div className="bg-white dark:bg-[#0e2343]/90 border border-slate-200 dark:border-sky-500/20 rounded-2xl shadow-sm dark:shadow-xl dark:shadow-sky-950/40 backdrop-blur-md p-6 space-y-4">
                        <div className="flex items-center justify-between">
                          <div>
                            <span className="text-xs font-bold text-sky-600 dark:text-sky-400 uppercase tracking-wider">
                              {courseQuizzes.course.obe?.code || 'UNIV-MOD'} • {courseQuizzes.course.obe?.semester || 'Accredited Lab'}
                            </span>
                            <h2 className="text-xl font-bold text-slate-900 dark:text-white mt-1">{courseQuizzes.course.title}</h2>
                            <p className="text-xs text-slate-500 dark:text-slate-400">{courseQuizzes.course.obe?.department || 'Faculty of Engineering & Computer Science'}</p>
                          </div>
                          <span className="px-3 py-1 bg-emerald-500/10 text-emerald-600 dark:text-emerald-400 border border-emerald-500/30 rounded-xl text-xs font-extrabold">
                            OBE COMPLIANT
                          </span>
                        </div>

                        {/* CLO/PLO Summary Table */}
                        {courseQuizzes.course.obe?.clos && (
                          <div className="pt-3 border-t border-slate-200 dark:border-sky-500/20 grid grid-cols-1 md:grid-cols-3 gap-3">
                            {courseQuizzes.course.obe.clos.map(clo => (
                              <div key={clo.id} className="p-3 bg-slate-50 dark:bg-[#07162e] rounded-xl border border-slate-200 dark:border-sky-500/20">
                                <div className="flex items-center justify-between text-[10px] font-extrabold mb-1">
                                  <span className="text-sky-600 dark:text-sky-400">{clo.id}</span>
                                  <span className="text-purple-600 dark:text-purple-400">{clo.domain}</span>
                                </div>
                                <p className="text-[11px] text-slate-700 dark:text-slate-300 leading-snug">{clo.desc}</p>
                                <div className="mt-1.5 text-[10px] text-slate-500 font-mono font-bold">{clo.plo}</div>
                              </div>
                            ))}
                          </div>
                        )}
                      </div>

                      {/* Lab Steps & Attached Quizzes */}
                      <div className="space-y-4">
                        <h3 className="text-sm font-bold text-slate-900 dark:text-white uppercase tracking-wider">Lab Experiments & Assessment Quizzes</h3>
                        {courseQuizzes.steps.map(step => (
                          <div key={step.id} className="bg-white dark:bg-[#0e2343]/90 border border-slate-200 dark:border-sky-500/20 rounded-2xl shadow-sm dark:shadow-xl dark:shadow-sky-950/40 backdrop-blur-md p-5 space-y-3">
                            <div className="flex items-center justify-between">
                              <div className="flex items-center space-x-3">
                                <span className="w-8 h-8 rounded-xl bg-sky-500/10 text-sky-600 dark:text-sky-400 border border-sky-500/20 flex items-center justify-center font-bold text-xs">
                                  {step.order}
                                </span>
                                <div>
                                  <h4 className="text-sm font-bold text-slate-900 dark:text-white">{step.title}</h4>
                                  <p className="text-xs text-slate-500 dark:text-slate-400">{step.contentPreview || 'Step procedure and code snippet instructions.'}</p>
                                </div>
                              </div>
                              <span className="text-xs font-bold text-slate-500 dark:text-slate-400">{step.quizzes.length} Quizzes Attached</span>
                            </div>

                            {step.codeSnippet && (
                              <pre className="p-3 bg-slate-50 dark:bg-[#07162e] border border-slate-200 dark:border-sky-500/20 rounded-xl text-xs font-mono text-emerald-600 dark:text-emerald-400 overflow-x-auto">
                                <code>{step.codeSnippet}</code>
                              </pre>
                            )}

                            {step.quizzes.length > 0 && (
                              <div className="space-y-2 pt-2 border-t border-slate-200 dark:border-sky-500/20">
                                {step.quizzes.map(q => (
                                  <div key={q.id} className="p-3 bg-slate-50 dark:bg-[#07162e] rounded-xl border border-slate-200 dark:border-sky-500/20 flex items-center justify-between text-xs">
                                    <div className="space-y-1 flex-1">
                                      <p className="font-bold text-slate-900 dark:text-white">Q: {q.question}</p>
                                      <p className="text-slate-500 dark:text-slate-400">Correct: <span className="text-emerald-600 dark:text-emerald-400 font-bold">{q.correctAnswer}</span></p>
                                    </div>
                                    <div className="flex items-center space-x-2 shrink-0">
                                      <button
                                        onClick={() => handleEditQuiz(q)}
                                        className="px-2.5 py-1 bg-slate-200 dark:bg-[#142c54] hover:bg-slate-300 dark:hover:bg-[#183768] text-slate-800 dark:text-slate-200 rounded-lg text-xs font-bold transition shadow-sm"
                                      >
                                        Edit
                                      </button>
                                      <button
                                        onClick={() => handleDeleteQuiz(q.id)}
                                        className="p-1 bg-red-500/10 text-red-600 dark:text-red-400 hover:bg-red-500/20 rounded-lg text-xs font-bold transition"
                                      >
                                        🗑️
                                      </button>
                                    </div>
                                  </div>
                                ))}
                              </div>
                            )}
                          </div>
                        ))}
                      </div>
                    </div>
                  ) : (
                    /* 9 University Courses Grid */
                    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                      {courses.map(c => (
                        <div
                          key={c.id}
                          className="bg-white dark:bg-[#0e2343]/90 border border-slate-200 dark:border-sky-500/20 hover:border-sky-500/40 rounded-2xl p-6 shadow-sm dark:shadow-xl dark:shadow-sky-950/40 backdrop-blur-md flex flex-col justify-between space-y-4 transition-all duration-300 hover:-translate-y-0.5"
                        >
                          <div className="space-y-2.5">
                            <div className="flex items-center justify-between">
                              <span className="text-[10px] font-extrabold uppercase px-2.5 py-0.5 rounded-full bg-sky-500/10 text-sky-600 dark:text-sky-400 border border-sky-500/30">
                                {c.obe?.code || 'CS-MODULE'}
                              </span>
                              <span className="text-[10px] font-mono text-slate-500 font-bold">{c.obe?.semester || 'Semester Lab'}</span>
                            </div>

                            <h3 className="text-base font-bold text-slate-900 dark:text-white">{c.title}</h3>
                            <p className="text-xs text-slate-500 dark:text-slate-400 line-clamp-2 leading-relaxed">{c.description || 'Verified university lab courseware.'}</p>

                            <div className="grid grid-cols-3 gap-2 pt-2 text-center text-xs">
                              <div className="p-2 bg-slate-50 dark:bg-[#07162e] rounded-xl border border-slate-200 dark:border-sky-500/20">
                                <div className="text-[10px] text-slate-500 uppercase font-bold">Steps</div>
                                <div className="text-slate-900 dark:text-white font-black">{c.totalSteps}</div>
                              </div>
                              <div className="p-2 bg-slate-50 dark:bg-[#07162e] rounded-xl border border-slate-200 dark:border-sky-500/20">
                                <div className="text-[10px] text-slate-500 uppercase font-bold">Quizzes</div>
                                <div className="text-emerald-600 dark:text-emerald-400 font-black">{c.totalQuizzes}</div>
                              </div>
                              <div className="p-2 bg-slate-50 dark:bg-[#07162e] rounded-xl border border-slate-200 dark:border-sky-500/20">
                                <div className="text-[10px] text-slate-500 uppercase font-bold">Passed</div>
                                <div className="text-sky-600 dark:text-sky-400 font-black">{c.completions || 0}</div>
                              </div>
                            </div>
                          </div>

                          <button
                            onClick={() => handleInspectCourse(c.id)}
                            className="w-full py-2.5 bg-gradient-to-r from-sky-500/15 to-teal-500/15 hover:from-sky-500/25 hover:to-teal-500/25 text-sky-700 dark:text-sky-300 font-bold text-xs rounded-xl border border-sky-500/30 transition flex items-center justify-center space-x-1.5 shadow-sm active:scale-95"
                          >
                            <span>Inspect Lab Steps & Quizzes ›</span>
                          </button>
                        </div>
                      ))}
                    </div>
                  )}
                </div>
              )}

              {/* TAB 4: COURSE & LAB CONTENT CREATOR STUDIO */}
              {activeTab === 'creator' && (
                <div className="space-y-8">
                  {/* Studio Progress Bar */}
                  <div className="grid grid-cols-3 gap-4">
                    {[
                      { id: 'course', step: 1, title: 'Course Metadata' },
                      { id: 'step', step: 2, title: 'Lab Experiment & OBE' },
                      { id: 'quiz', step: 3, title: 'Assessment Quizzes' },
                    ].map(s => (
                      <button
                        key={s.id}
                        onClick={() => setActiveStudioStep(s.id)}
                        className={`p-4 rounded-2xl border text-left transition-all ${
                          activeStudioStep === s.id
                            ? 'bg-purple-500/15 border-purple-500/50 text-purple-700 dark:text-purple-300 shadow-md shadow-purple-900/20 font-bold'
                            : 'bg-white dark:bg-[#0e2343]/90 border-slate-200 dark:border-sky-500/20 text-slate-500 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white'
                        }`}
                      >
                        <div className="text-[10px] uppercase font-mono font-extrabold mb-1">Step {s.step}</div>
                        <div className="text-xs font-black">{s.title}</div>
                      </button>
                    ))}
                  </div>

                  {/* Step 1: Course Info */}
                  {activeStudioStep === 'course' && (
                    <div className="bg-white dark:bg-[#0e2343]/90 border border-slate-200 dark:border-sky-500/20 rounded-2xl shadow-sm dark:shadow-xl dark:shadow-sky-950/40 backdrop-blur-md p-6 max-w-2xl">
                      <h3 className="text-base font-bold text-slate-900 dark:text-white mb-4">Create New Accredited Course Container</h3>
                      <form onSubmit={handleCreateCourse} className="space-y-4">
                        <div>
                          <label className="block text-xs font-bold uppercase text-slate-700 dark:text-slate-400 mb-1.5">Course Title *</label>
                          <input
                            type="text"
                            value={creatorCourse.title}
                            onChange={e => setCreatorCourse({ ...creatorCourse, title: e.target.value })}
                            placeholder="e.g. Distributed Computing Lab"
                            className="w-full px-4 py-2.5 bg-slate-50 dark:bg-[#07152b] border border-slate-200 dark:border-sky-500/20 rounded-xl text-xs text-slate-900 dark:text-white focus:outline-none focus:border-purple-500 focus:ring-2 focus:ring-purple-500/20 transition"
                          />
                        </div>
                        <div>
                          <label className="block text-xs font-bold uppercase text-slate-700 dark:text-slate-400 mb-1.5">Category</label>
                          <select
                            value={creatorCourse.category}
                            onChange={e => setCreatorCourse({ ...creatorCourse, category: e.target.value })}
                            className="w-full px-4 py-2.5 bg-slate-50 dark:bg-[#07152b] border border-slate-200 dark:border-sky-500/20 rounded-xl text-xs text-slate-900 dark:text-white focus:outline-none focus:border-purple-500 transition"
                          >
                            <option value="University Courses">University Courses (OBE Accredited)</option>
                            <option value="Computer Courses">Computer Science</option>
                            <option value="Mobile Dev">Mobile App Engineering</option>
                            <option value="TECH">Technical Labs</option>
                          </select>
                        </div>
                        <div>
                          <label className="block text-xs font-bold uppercase text-slate-700 dark:text-slate-400 mb-1.5">Description</label>
                          <textarea
                            rows="3"
                            value={creatorCourse.description}
                            onChange={e => setCreatorCourse({ ...creatorCourse, description: e.target.value })}
                            placeholder="Course outline and learning outcomes..."
                            className="w-full px-4 py-2.5 bg-slate-50 dark:bg-[#07152b] border border-slate-200 dark:border-sky-500/20 rounded-xl text-xs text-slate-900 dark:text-white focus:outline-none focus:border-purple-500 transition"
                          />
                        </div>
                        <button
                          type="submit"
                          disabled={isCreatingCourse}
                          className="px-6 py-2.5 bg-purple-600 hover:bg-purple-500 text-white font-bold text-xs rounded-xl shadow-md transition disabled:opacity-50"
                        >
                          {isCreatingCourse ? 'Creating Course...' : 'Proceed to Lab Experiments ›'}
                        </button>
                      </form>
                    </div>
                  )}

                  {/* Step 2: Lab Experiment & OBE Builder */}
                  {activeStudioStep === 'step' && (
                    <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
                      <div className="bg-white dark:bg-[#0e2343]/90 border border-slate-200 dark:border-sky-500/20 rounded-2xl shadow-sm dark:shadow-xl dark:shadow-sky-950/40 backdrop-blur-md p-6 space-y-4">
                        <h3 className="text-base font-bold text-slate-900 dark:text-white">Lab Experiment Editor</h3>
                        <form onSubmit={handleCreateStep} className="space-y-4">
                          <div>
                            <label className="block text-xs font-bold text-slate-700 dark:text-slate-400 mb-1.5">Parent Course *</label>
                            <select
                              value={creatorStep.courseId}
                              onChange={e => setCreatorStep({ ...creatorStep, courseId: e.target.value })}
                              className="w-full px-4 py-2 bg-slate-50 dark:bg-[#07152b] border border-slate-200 dark:border-sky-500/20 rounded-xl text-xs text-slate-900 dark:text-white focus:outline-none focus:border-purple-500"
                            >
                              <option value="">-- Choose Course --</option>
                              {courses.map(c => (
                                <option key={c.id} value={c.id}>{c.title}</option>
                              ))}
                            </select>
                          </div>
                          <div className="grid grid-cols-2 gap-3">
                            <div>
                              <label className="block text-xs font-bold text-slate-700 dark:text-slate-400 mb-1">Experiment Order</label>
                              <input
                                type="number"
                                min="1"
                                max="30"
                                value={creatorStep.order}
                                onChange={e => setCreatorStep({ ...creatorStep, order: parseInt(e.target.value) || 1 })}
                                className="w-full px-3 py-2 bg-slate-50 dark:bg-[#07152b] border border-slate-200 dark:border-sky-500/20 rounded-xl text-xs font-mono text-slate-900 dark:text-white"
                              />
                            </div>
                            <div>
                              <label className="block text-xs font-bold text-slate-700 dark:text-slate-400 mb-1">Experiment Title *</label>
                              <input
                                type="text"
                                value={creatorStep.title}
                                onChange={e => setCreatorStep({ ...creatorStep, title: e.target.value })}
                                placeholder="e.g. POSIX Pthreads Multithreading"
                                className="w-full px-3 py-2 bg-slate-50 dark:bg-[#07152b] border border-slate-200 dark:border-sky-500/20 rounded-xl text-xs text-slate-900 dark:text-white"
                              />
                            </div>
                          </div>

                          {/* OBE Tags */}
                          <div className="grid grid-cols-3 gap-2 text-xs">
                            <input
                              type="text"
                              value={creatorStep.clo}
                              onChange={e => setCreatorStep({ ...creatorStep, clo: e.target.value })}
                              placeholder="CLO tag"
                              className="p-2 bg-slate-50 dark:bg-[#07152b] border border-slate-200 dark:border-sky-500/20 rounded-xl text-[11px] text-slate-900 dark:text-white"
                            />
                            <input
                              type="text"
                              value={creatorStep.plo}
                              onChange={e => setCreatorStep({ ...creatorStep, plo: e.target.value })}
                              placeholder="PLO tag"
                              className="p-2 bg-slate-50 dark:bg-[#07152b] border border-slate-200 dark:border-sky-500/20 rounded-xl text-[11px] text-slate-900 dark:text-white"
                            />
                            <input
                              type="text"
                              value={creatorStep.blooms}
                              onChange={e => setCreatorStep({ ...creatorStep, blooms: e.target.value })}
                              placeholder="Bloom's Level"
                              className="p-2 bg-slate-50 dark:bg-[#07152b] border border-slate-200 dark:border-sky-500/20 rounded-xl text-[11px] text-slate-900 dark:text-white"
                            />
                          </div>

                          {/* Markdown editor toolbar */}
                          <div>
                            <div className="flex items-center space-x-1.5 mb-1.5">
                              {['H2', 'Bold', 'Code', 'List'].map(tool => (
                                <button
                                  key={tool}
                                  type="button"
                                  onClick={() => {
                                    if (tool === 'H2') insertMarkdownSnippet('## ', '');
                                    if (tool === 'Bold') insertMarkdownSnippet('**', '**');
                                    if (tool === 'Code') insertMarkdownSnippet('`', '`');
                                    if (tool === 'List') insertMarkdownSnippet('- ', '');
                                  }}
                                  className="px-2 py-0.5 bg-slate-200 dark:bg-slate-800 hover:bg-slate-300 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-300 rounded text-[10px] font-bold"
                                >
                                  {tool}
                                </button>
                              ))}
                            </div>
                            <textarea
                              rows="6"
                              value={creatorStep.content}
                              onChange={e => setCreatorStep({ ...creatorStep, content: e.target.value })}
                              placeholder="Document laboratory instructions, theory, and procedures..."
                              className="w-full p-3 bg-slate-50 dark:bg-[#07152b] border border-slate-200 dark:border-sky-500/20 rounded-xl text-xs font-mono text-slate-900 dark:text-white"
                            />
                          </div>

                          <div>
                            <label className="block text-xs font-bold text-slate-700 dark:text-slate-400 mb-1">Terminal Code Snippet (Optional)</label>
                            <textarea
                              rows="3"
                              value={creatorStep.codeSnippet}
                              onChange={e => setCreatorStep({ ...creatorStep, codeSnippet: e.target.value })}
                              placeholder="gcc -pthread multithread.c -o thread_demo"
                              className="w-full p-2.5 bg-slate-50 dark:bg-[#07152b] border border-slate-200 dark:border-sky-500/20 rounded-xl text-emerald-600 dark:text-emerald-400 text-xs font-mono"
                            />
                          </div>

                          <button
                            type="submit"
                            disabled={isCreatingStep}
                            className="px-6 py-2.5 bg-purple-600 hover:bg-purple-500 text-white font-bold text-xs rounded-xl transition disabled:opacity-50"
                          >
                            {isCreatingStep ? 'Saving...' : 'Save Step & Proceed to Quizzes ›'}
                          </button>
                        </form>
                      </div>

                      {/* Right: Live Preview Pane */}
                      <div className="bg-white dark:bg-[#0e2343]/90 border border-slate-200 dark:border-sky-500/20 rounded-2xl shadow-sm dark:shadow-xl dark:shadow-sky-950/40 backdrop-blur-md p-6 space-y-3">
                        <div className="flex items-center justify-between pb-3 border-b border-slate-200 dark:border-sky-500/20">
                          <span className="text-xs font-bold text-slate-500 dark:text-slate-400 uppercase tracking-wider">Live Document Preview</span>
                          <span className="text-[10px] font-mono px-2 py-0.5 bg-slate-100 dark:bg-slate-800 rounded text-slate-600 dark:text-slate-300">Markdown Prose</span>
                        </div>
                        <div className="p-4 bg-slate-50 dark:bg-[#07162e] rounded-xl border border-slate-200 dark:border-sky-500/20 md-preview max-h-[500px] overflow-y-auto" dangerouslySetInnerHTML={{ __html: renderedMarkdown }}></div>
                      </div>
                    </div>
                  )}

                  {/* Step 3: Quizzes */}
                  {activeStudioStep === 'quiz' && (
                    <div className="bg-white dark:bg-[#0e2343]/90 border border-slate-200 dark:border-sky-500/20 rounded-2xl shadow-sm dark:shadow-xl dark:shadow-sky-950/40 backdrop-blur-md p-6 max-w-2xl space-y-4">
                      <div className="flex items-center justify-between">
                        <h3 className="text-base font-bold text-slate-900 dark:text-white">Attach Assessment Quiz</h3>
                        <span className="text-xs font-bold text-purple-600 dark:text-purple-400">{savedStepQuizzes.length} Questions Attached</span>
                      </div>

                      <form onSubmit={handleCreateStepQuiz} className="space-y-4">
                        <div>
                          <label className="block text-xs font-bold text-slate-700 dark:text-slate-400 mb-1">Question Prompt *</label>
                          <textarea
                            rows="2"
                            value={creatorQuiz.question}
                            onChange={e => setCreatorQuiz({ ...creatorQuiz, question: e.target.value })}
                            placeholder="What does pthread_join() do?"
                            className="w-full p-2.5 bg-slate-50 dark:bg-[#07152b] border border-slate-200 dark:border-sky-500/20 rounded-xl text-xs text-slate-900 dark:text-white"
                          />
                        </div>

                        <div className="space-y-2">
                          <label className="block text-xs font-bold text-slate-700 dark:text-slate-400">Answer Choices (Select radio for correct choice)</label>
                          {creatorQuiz.options.map((opt, i) => (
                            <div key={i} className="flex items-center space-x-2">
                              <input
                                type="radio"
                                name="correctChoice"
                                checked={creatorQuiz.correctAnswer === opt && Boolean(opt)}
                                onChange={() => setCreatorQuiz({ ...creatorQuiz, correctAnswer: opt })}
                                className="text-purple-600 focus:ring-purple-500"
                              />
                              <input
                                type="text"
                                placeholder={`Option ${i + 1}`}
                                value={opt}
                                onChange={e => {
                                  const updated = [...creatorQuiz.options];
                                  updated[i] = e.target.value;
                                  setCreatorQuiz({ ...creatorQuiz, options: updated });
                                }}
                                className="w-full p-2 bg-slate-50 dark:bg-[#07152b] border border-slate-200 dark:border-sky-500/20 rounded-xl text-xs text-slate-900 dark:text-white"
                              />
                            </div>
                          ))}
                        </div>

                        <div>
                          <label className="block text-xs font-bold text-slate-700 dark:text-slate-400 mb-1">Pedagogical Explanation</label>
                          <input
                            type="text"
                            value={creatorQuiz.explanation}
                            onChange={e => setCreatorQuiz({ ...creatorQuiz, explanation: e.target.value })}
                            placeholder="pthread_join blocks until target thread terminates..."
                            className="w-full p-2 bg-slate-50 dark:bg-[#07152b] border border-slate-200 dark:border-sky-500/20 rounded-xl text-xs text-slate-900 dark:text-white"
                          />
                        </div>

                        <button
                          type="submit"
                          disabled={isCreatingQuiz}
                          className="px-6 py-2.5 bg-emerald-500 hover:bg-emerald-400 text-slate-950 font-bold text-xs rounded-xl shadow-md transition disabled:opacity-50"
                        >
                          {isCreatingQuiz ? 'Attaching...' : '+ Attach Assessment Question'}
                        </button>
                      </form>
                    </div>
                  )}
                </div>
              )}

              {/* TAB 5: CAMPUS ANNOUNCEMENTS & LIVE NOTICE BOARD */}
              {activeTab === 'announcements' && (
                <div className="space-y-8">
                  {/* Top Stats */}
                  <div className="grid grid-cols-1 sm:grid-cols-3 gap-5">
                    <div className="bg-white dark:bg-[#0e2343]/90 border border-slate-200 dark:border-sky-500/20 rounded-2xl shadow-sm dark:shadow-xl dark:shadow-sky-950/40 backdrop-blur-md p-5 flex items-center justify-between">
                      <div>
                        <div className="text-xs font-bold text-slate-500 dark:text-slate-400 uppercase tracking-wider mb-1">Total Notices</div>
                        <div className="text-2xl font-black text-slate-900 dark:text-white">{announcements.length}</div>
                      </div>
                      <div className="w-12 h-12 rounded-2xl bg-sky-500/10 border border-sky-500/20 flex items-center justify-center text-sky-600 dark:text-sky-400 text-xl font-bold">
                        📢
                      </div>
                    </div>

                    <div className="bg-white dark:bg-[#0e2343]/90 border border-slate-200 dark:border-sky-500/20 rounded-2xl shadow-sm dark:shadow-xl dark:shadow-sky-950/40 backdrop-blur-md p-5 flex items-center justify-between">
                      <div>
                        <div className="text-xs font-bold text-slate-500 dark:text-slate-400 uppercase tracking-wider mb-1">Active on Mobile</div>
                        <div className="text-2xl font-black text-emerald-600 dark:text-emerald-400 flex items-center space-x-2">
                          <span>{announcements.filter(a => a.isActive).length}</span>
                          <span className="relative flex h-2.5 w-2.5 ml-1">
                            <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-500 opacity-75"></span>
                            <span className="relative inline-flex rounded-full h-2.5 w-2.5 bg-emerald-500"></span>
                          </span>
                        </div>
                      </div>
                      <div className="w-12 h-12 rounded-2xl bg-emerald-500/10 border border-emerald-500/20 flex items-center justify-center text-emerald-600 dark:text-emerald-400 text-xl font-bold">
                        📱
                      </div>
                    </div>

                    <div className="bg-white dark:bg-[#0e2343]/90 border border-slate-200 dark:border-sky-500/20 rounded-2xl shadow-sm dark:shadow-xl dark:shadow-sky-950/40 backdrop-blur-md p-5 flex items-center justify-between">
                      <div>
                        <div className="text-xs font-bold text-slate-500 dark:text-slate-400 uppercase tracking-wider mb-1">Archived / Inactive</div>
                        <div className="text-2xl font-black text-slate-500 dark:text-slate-400">
                          {announcements.filter(a => !a.isActive).length}
                        </div>
                      </div>
                      <div className="w-12 h-12 rounded-2xl bg-slate-100 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 flex items-center justify-center text-slate-500 dark:text-slate-400 text-xl font-bold">
                        🗄️
                      </div>
                    </div>
                  </div>

                  {/* Main Grid: Composer & Feed */}
                  <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
                    {/* Left Column: Composer Form (5 cols) */}
                    <div className="lg:col-span-5 space-y-6">
                      <div className="bg-white dark:bg-[#0e2343]/90 border border-slate-200 dark:border-sky-500/20 rounded-2xl shadow-sm dark:shadow-xl dark:shadow-sky-950/40 backdrop-blur-md p-6">
                        <div className="flex items-center justify-between border-b border-slate-200 dark:border-sky-500/20 pb-4 mb-5">
                          <div className="flex items-center space-x-3">
                            <span className="text-xl">✍️</span>
                            <div>
                              <h3 className="text-base font-bold text-slate-900 dark:text-white">Broadcast Announcement</h3>
                              <p className="text-xs text-slate-500 dark:text-slate-400">Publish instant updates to student mobile apps</p>
                            </div>
                          </div>
                        </div>

                        <form onSubmit={handleCreateAnnouncement} className="space-y-4">
                          <div>
                            <label className="block text-xs font-bold text-slate-700 dark:text-slate-300 uppercase tracking-wider mb-1.5">
                              Notice Title *
                            </label>
                            <input
                              type="text"
                              value={newAnnouncement.title}
                              onChange={e => setNewAnnouncement({ ...newAnnouncement, title: e.target.value })}
                              placeholder="e.g. Midterm Exam Schedule Released"
                              className="w-full px-4 py-2.5 bg-slate-50 dark:bg-[#07152b] border border-slate-200 dark:border-sky-500/20 rounded-xl text-xs text-slate-900 dark:text-white placeholder:text-slate-400 dark:placeholder:text-slate-500 focus:outline-none focus:border-sky-500 focus:ring-2 focus:ring-sky-500/20 transition"
                            />
                          </div>

                          <div>
                            <label className="block text-xs font-bold text-slate-700 dark:text-slate-300 uppercase tracking-wider mb-1.5">
                              Priority / Badge Type
                            </label>
                            <div className="grid grid-cols-3 gap-2">
                              {[
                                { id: 'info', label: 'Info', icon: 'ℹ️', color: 'border-sky-500/40 text-sky-600 dark:text-sky-400 bg-sky-500/10' },
                                { id: 'warning', label: 'Warning', icon: '⚠️', color: 'border-amber-500/40 text-amber-600 dark:text-amber-400 bg-amber-500/10' },
                                { id: 'success', label: 'Success', icon: '✅', color: 'border-emerald-500/40 text-emerald-600 dark:text-emerald-400 bg-emerald-500/10' }
                              ].map(t => (
                                <button
                                  key={t.id}
                                  type="button"
                                  onClick={() => setNewAnnouncement({ ...newAnnouncement, type: t.id })}
                                  className={`py-2 px-3 rounded-xl border text-xs font-bold flex items-center justify-center space-x-1.5 transition ${
                                    newAnnouncement.type === t.id
                                      ? `${t.color} ring-2 ring-sky-500/30`
                                      : 'border-slate-200 dark:border-sky-500/20 text-slate-500 bg-slate-50 dark:bg-[#07152b]'
                                  }`}
                                >
                                  <span>{t.icon}</span>
                                  <span>{t.label}</span>
                                </button>
                              ))}
                            </div>
                          </div>

                          <div>
                            <label className="block text-xs font-bold text-slate-700 dark:text-slate-300 uppercase tracking-wider mb-1.5">
                              Notice Message / Details *
                            </label>
                            <textarea
                              rows="4"
                              value={newAnnouncement.message}
                              onChange={e => setNewAnnouncement({ ...newAnnouncement, message: e.target.value })}
                              placeholder="Provide clear details, instructions, or exam room numbers..."
                              className="w-full px-4 py-3 bg-slate-50 dark:bg-[#07152b] border border-slate-200 dark:border-sky-500/20 rounded-xl text-xs text-slate-900 dark:text-white placeholder:text-slate-400 dark:placeholder:text-slate-500 focus:outline-none focus:border-sky-500 focus:ring-2 focus:ring-sky-500/20 transition leading-relaxed"
                            />
                          </div>

                          <div className="flex items-center justify-between pt-2">
                            <label className="flex items-center space-x-2.5 cursor-pointer">
                              <input
                                type="checkbox"
                                checked={newAnnouncement.isActive}
                                onChange={e => setNewAnnouncement({ ...newAnnouncement, isActive: e.target.checked })}
                                className="w-4 h-4 rounded border-slate-300 dark:border-slate-700 bg-white dark:bg-[#07152b] text-emerald-500 focus:ring-emerald-500"
                              />
                              <span className="text-xs font-bold text-slate-700 dark:text-slate-300">Active Immediately</span>
                            </label>

                            <button
                              type="submit"
                              disabled={isPublishingAnnouncement}
                              className="px-5 py-2.5 bg-emerald-500 hover:bg-emerald-400 text-slate-950 font-bold text-xs rounded-xl shadow-md transition disabled:opacity-50 flex items-center space-x-2 active:scale-95"
                            >
                              {isPublishingAnnouncement ? (
                                <>
                                  <div className="w-3.5 h-3.5 border-2 border-slate-950 border-t-transparent rounded-full animate-spin"></div>
                                  <span>Broadcasting...</span>
                                </>
                              ) : (
                                <>
                                  <span>🚀</span>
                                  <span>Broadcast Notice</span>
                                </>
                              )}
                            </button>
                          </div>
                        </form>
                      </div>
                    </div>

                    {/* Right Column: Live Feed (7 cols) */}
                    <div className="lg:col-span-7 space-y-4">
                      <div className="flex items-center justify-between">
                        <h3 className="text-base font-bold text-slate-900 dark:text-white">Active Campus Notices Feed</h3>
                        <div className="flex space-x-1.5">
                          {['all', 'active', 'inactive'].map(f => (
                            <button
                              key={f}
                              onClick={() => setAnnouncementFilter(f)}
                              className={`px-3 py-1 rounded-xl text-xs font-bold capitalize transition ${
                                announcementFilter === f
                                  ? 'bg-sky-500 text-white shadow-sm'
                                  : 'bg-slate-100 dark:bg-[#0e2343] text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white'
                              }`}
                            >
                              {f}
                            </button>
                          ))}
                        </div>
                      </div>

                      <div className="space-y-3">
                        {isLoadingAnnouncements ? (
                          <div className="p-8 text-center text-slate-400">Loading notices...</div>
                        ) : announcements.length === 0 ? (
                          <div className="p-8 text-center text-slate-400 bg-white dark:bg-[#0e2343]/90 rounded-2xl border border-slate-200 dark:border-sky-500/20">
                            No campus notices published yet. Use the composer on the left to broadcast your first notice.
                          </div>
                        ) : (
                          announcements
                            .filter(a => {
                              if (announcementFilter === 'active') return a.isActive;
                              if (announcementFilter === 'inactive') return !a.isActive;
                              return true;
                            })
                            .map(a => (
                              <div
                                key={a.id}
                                className="bg-white dark:bg-[#0e2343]/90 border border-slate-200 dark:border-sky-500/20 rounded-2xl p-5 shadow-sm dark:shadow-lg dark:shadow-sky-950/30 backdrop-blur-md flex flex-col justify-between space-y-3 transition"
                              >
                                <div className="flex items-start justify-between">
                                  <div className="space-y-1">
                                    <div className="flex items-center space-x-2">
                                      <span className={`text-[10px] font-extrabold uppercase px-2 py-0.5 rounded-full border ${
                                        a.type === 'warning'
                                          ? 'bg-amber-500/10 text-amber-600 dark:text-amber-400 border-amber-500/30'
                                          : a.type === 'success'
                                            ? 'bg-emerald-500/10 text-emerald-600 dark:text-emerald-400 border-emerald-500/30'
                                            : 'bg-sky-500/10 text-sky-600 dark:text-sky-400 border-sky-500/30'
                                      }`}>
                                        {a.type}
                                      </span>
                                      <span className="text-xs font-mono text-slate-400">{new Date(a.createdAt).toLocaleDateString()}</span>
                                    </div>
                                    <h4 className="text-sm font-bold text-slate-900 dark:text-white mt-1">{a.title}</h4>
                                  </div>

                                  <div className="flex items-center space-x-2">
                                    <button
                                      onClick={() => handleToggleAnnouncement(a.id)}
                                      className={`px-2.5 py-1 rounded-xl text-xs font-bold border transition ${
                                        a.isActive
                                          ? 'bg-emerald-500/10 text-emerald-600 dark:text-emerald-400 border-emerald-500/30'
                                          : 'bg-slate-100 dark:bg-slate-800 text-slate-500 border-slate-200 dark:border-slate-700'
                                      }`}
                                    >
                                      {a.isActive ? '● Live' : '○ Inactive'}
                                    </button>
                                    <button
                                      onClick={() => handleDeleteAnnouncement(a.id, a.title)}
                                      className="p-1.5 bg-red-500/10 text-red-600 dark:text-red-400 hover:bg-red-500/20 rounded-lg text-xs font-bold transition"
                                      title="Delete Notice"
                                    >
                                      🗑️
                                    </button>
                                  </div>
                                </div>

                                <p className="text-xs text-slate-600 dark:text-slate-300 leading-relaxed whitespace-pre-wrap">{a.message}</p>
                              </div>
                            ))
                        )}
                      </div>
                    </div>
                  </div>
                </div>
              )}

              {/* TAB 6: ECONOMY & REWARD CONTROL */}
              {activeTab === 'economy' && (
                <div className="space-y-8">
                  {/* Top Stats 4-Card Grid */}
                  <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
                    <div className="bg-white dark:bg-[#0e2343]/90 border border-slate-200 dark:border-sky-500/20 rounded-2xl shadow-sm dark:shadow-xl dark:shadow-sky-950/40 backdrop-blur-md p-5 flex items-center justify-between">
                      <div>
                        <div className="text-xs font-bold text-slate-500 dark:text-slate-400 uppercase tracking-wider mb-1">Total Platform XP</div>
                        <div className="text-2xl font-black text-amber-500 dark:text-amber-400">
                          {(stats?.totalXpAwarded || 0).toLocaleString()}
                        </div>
                      </div>
                      <div className="w-12 h-12 rounded-2xl bg-amber-500/10 border border-amber-500/20 flex items-center justify-center text-amber-500 dark:text-amber-400 text-xl font-bold">
                        ⚡
                      </div>
                    </div>

                    <div className="bg-white dark:bg-[#0e2343]/90 border border-slate-200 dark:border-sky-500/20 rounded-2xl shadow-sm dark:shadow-xl dark:shadow-sky-950/40 backdrop-blur-md p-5 flex items-center justify-between">
                      <div>
                        <div className="text-xs font-bold text-slate-500 dark:text-slate-400 uppercase tracking-wider mb-1">Coins in Circulation</div>
                        <div className="text-2xl font-black text-emerald-600 dark:text-emerald-400">
                          {(stats?.totalCoinsInCirculation || 0).toLocaleString()}
                        </div>
                      </div>
                      <div className="w-12 h-12 rounded-2xl bg-emerald-500/10 border border-emerald-500/20 flex items-center justify-center text-emerald-600 dark:text-emerald-400 text-xl font-bold">
                        🪙
                      </div>
                    </div>

                    <div className="bg-white dark:bg-[#0e2343]/90 border border-slate-200 dark:border-sky-500/20 rounded-2xl shadow-sm dark:shadow-xl dark:shadow-sky-950/40 backdrop-blur-md p-5 flex items-center justify-between">
                      <div>
                        <div className="text-xs font-bold text-slate-500 dark:text-slate-400 uppercase tracking-wider mb-1">Quiz Pass Base Rate</div>
                        <div className="text-2xl font-black text-sky-600 dark:text-sky-400">
                          +{economyConfig.quizPassXp} XP
                        </div>
                      </div>
                      <div className="w-12 h-12 rounded-2xl bg-sky-500/10 border border-sky-500/20 flex items-center justify-center text-sky-600 dark:text-sky-400 text-xl font-bold">
                        🎯
                      </div>
                    </div>

                    <div className="bg-white dark:bg-[#0e2343]/90 border border-slate-200 dark:border-sky-500/20 rounded-2xl shadow-sm dark:shadow-xl dark:shadow-sky-950/40 backdrop-blur-md p-5 flex items-center justify-between">
                      <div>
                        <div className="text-xs font-bold text-slate-500 dark:text-slate-400 uppercase tracking-wider mb-1">Lab Experiment Base</div>
                        <div className="text-2xl font-black text-purple-600 dark:text-purple-400">
                          +{economyConfig.labCompletionXp} XP
                        </div>
                      </div>
                      <div className="w-12 h-12 rounded-2xl bg-purple-500/10 border border-purple-500/20 flex items-center justify-center text-purple-600 dark:text-purple-400 text-xl font-bold">
                        🧪
                      </div>
                    </div>
                  </div>

                  {/* Main Two-Column Layout */}
                  <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
                    {/* Left Column: Economy Rate Tuner (6 cols) */}
                    <div className="lg:col-span-6 space-y-6">
                      <div className="bg-white dark:bg-[#0e2343]/90 border border-slate-200 dark:border-sky-500/20 rounded-2xl shadow-sm dark:shadow-xl dark:shadow-sky-950/40 backdrop-blur-md p-6">
                        <div className="flex items-center justify-between border-b border-slate-200 dark:border-sky-500/20 pb-4 mb-5">
                          <div className="flex items-center space-x-3">
                            <span className="text-xl">⚙️</span>
                            <div>
                              <h3 className="text-base font-bold text-slate-900 dark:text-white">Live Economy Multipliers</h3>
                              <p className="text-xs text-slate-500 dark:text-slate-400">Configure XP, coin rewards & gamification rates in real-time</p>
                            </div>
                          </div>
                          <span className="text-[10px] px-2.5 py-1 bg-emerald-500/15 text-emerald-600 dark:text-emerald-400 font-extrabold rounded-lg border border-emerald-500/30">
                            DATABASE BACKED
                          </span>
                        </div>

                        <form onSubmit={handleSaveEconomyConfig} className="space-y-4">
                          <div className="grid grid-cols-2 gap-4">
                            <div>
                              <label className="block text-xs font-bold text-slate-700 dark:text-slate-300 uppercase tracking-wider mb-1.5">
                                Quiz Pass XP
                              </label>
                              <input
                                type="number"
                                min="0"
                                max="1000"
                                value={economyConfig.quizPassXp}
                                onChange={e => setEconomyConfig({ ...economyConfig, quizPassXp: parseInt(e.target.value) || 0 })}
                                className="w-full px-4 py-2.5 bg-slate-50 dark:bg-[#07152b] border border-slate-200 dark:border-sky-500/20 rounded-xl text-xs text-slate-900 dark:text-white font-mono font-bold focus:outline-none focus:border-sky-500 focus:ring-2 focus:ring-sky-500/20"
                              />
                              <p className="text-[10px] text-slate-500 mt-1">Base XP earned per quiz pass</p>
                            </div>

                            <div>
                              <label className="block text-xs font-bold text-slate-700 dark:text-slate-300 uppercase tracking-wider mb-1.5">
                                Perfect Quiz Bonus XP
                              </label>
                              <input
                                type="number"
                                min="0"
                                max="1000"
                                value={economyConfig.perfectQuizBonusXp}
                                onChange={e => setEconomyConfig({ ...economyConfig, perfectQuizBonusXp: parseInt(e.target.value) || 0 })}
                                className="w-full px-4 py-2.5 bg-slate-50 dark:bg-[#07152b] border border-slate-200 dark:border-sky-500/20 rounded-xl text-xs text-slate-900 dark:text-white font-mono font-bold focus:outline-none focus:border-sky-500 focus:ring-2 focus:ring-sky-500/20"
                              />
                              <p className="text-[10px] text-slate-500 mt-1">Extra bonus for 100% correct score</p>
                            </div>
                          </div>

                          <div className="grid grid-cols-2 gap-4">
                            <div>
                              <label className="block text-xs font-bold text-slate-700 dark:text-slate-300 uppercase tracking-wider mb-1.5">
                                Lab Completion XP
                              </label>
                              <input
                                type="number"
                                min="0"
                                max="2000"
                                value={economyConfig.labCompletionXp}
                                onChange={e => setEconomyConfig({ ...economyConfig, labCompletionXp: parseInt(e.target.value) || 0 })}
                                className="w-full px-4 py-2.5 bg-slate-50 dark:bg-[#07152b] border border-slate-200 dark:border-sky-500/20 rounded-xl text-xs text-slate-900 dark:text-white font-mono font-bold focus:outline-none focus:border-sky-500 focus:ring-2 focus:ring-sky-500/20"
                              />
                              <p className="text-[10px] text-slate-500 mt-1">Awarded on completing lab step</p>
                            </div>

                            <div>
                              <label className="block text-xs font-bold text-slate-700 dark:text-slate-300 uppercase tracking-wider mb-1.5">
                                Daily Streak Coins
                              </label>
                              <input
                                type="number"
                                min="0"
                                max="500"
                                value={economyConfig.dailyStreakCoins}
                                onChange={e => setEconomyConfig({ ...economyConfig, dailyStreakCoins: parseInt(e.target.value) || 0 })}
                                className="w-full px-4 py-2.5 bg-slate-50 dark:bg-[#07152b] border border-slate-200 dark:border-sky-500/20 rounded-xl text-xs text-slate-900 dark:text-white font-mono font-bold focus:outline-none focus:border-sky-500 focus:ring-2 focus:ring-sky-500/20"
                              />
                              <p className="text-[10px] text-slate-500 mt-1">Coins earned per streak milestone</p>
                            </div>
                          </div>

                          <div className="grid grid-cols-2 gap-4">
                            <div>
                              <label className="block text-xs font-bold text-slate-700 dark:text-slate-300 uppercase tracking-wider mb-1.5">
                                Arena Win XP
                              </label>
                              <input
                                type="number"
                                min="0"
                                max="1000"
                                value={economyConfig.arenaWinXp}
                                onChange={e => setEconomyConfig({ ...economyConfig, arenaWinXp: parseInt(e.target.value) || 0 })}
                                className="w-full px-4 py-2.5 bg-slate-50 dark:bg-[#07152b] border border-slate-200 dark:border-sky-500/20 rounded-xl text-xs text-slate-900 dark:text-white font-mono font-bold focus:outline-none focus:border-sky-500 focus:ring-2 focus:ring-sky-500/20"
                              />
                              <p className="text-[10px] text-slate-500 mt-1">Dojo combat victory reward</p>
                            </div>

                            <div>
                              <label className="block text-xs font-bold text-slate-700 dark:text-slate-300 uppercase tracking-wider mb-1.5">
                                Arena Win Coins
                              </label>
                              <input
                                type="number"
                                min="0"
                                max="500"
                                value={economyConfig.arenaWinCoins}
                                onChange={e => setEconomyConfig({ ...economyConfig, arenaWinCoins: parseInt(e.target.value) || 0 })}
                                className="w-full px-4 py-2.5 bg-slate-50 dark:bg-[#07152b] border border-slate-200 dark:border-sky-500/20 rounded-xl text-xs text-slate-900 dark:text-white font-mono font-bold focus:outline-none focus:border-sky-500 focus:ring-2 focus:ring-sky-500/20"
                              />
                              <p className="text-[10px] text-slate-500 mt-1">Dojo victory coin bonus</p>
                            </div>
                          </div>

                          <div className="flex items-center justify-between pt-3">
                            <span className="text-[11px] text-slate-500 dark:text-slate-400 font-mono">
                              {economyConfig.updatedAt ? `Last modified: ${new Date(economyConfig.updatedAt).toLocaleString()}` : 'Default config active'}
                            </span>

                            <button
                              type="submit"
                              disabled={isSavingEconomy}
                              className="px-6 py-2.5 bg-gradient-to-r from-sky-500 to-indigo-600 hover:from-sky-400 hover:to-indigo-500 text-white font-bold text-xs rounded-xl shadow-md transition disabled:opacity-50 flex items-center space-x-2 active:scale-95"
                            >
                              {isSavingEconomy ? (
                                <>
                                  <div className="w-3.5 h-3.5 border-2 border-white border-t-transparent rounded-full animate-spin"></div>
                                  <span>Saving Rates...</span>
                                </>
                              ) : (
                                <>
                                  <span>💾</span>
                                  <span>Save Economy Rates</span>
                                </>
                              )}
                            </button>
                          </div>
                        </form>
                      </div>

                      {/* Live Payout Simulation Preview */}
                      <div className="bg-white dark:bg-[#0e2343]/90 border border-slate-200 dark:border-sky-500/20 rounded-2xl shadow-sm dark:shadow-xl dark:shadow-sky-950/40 backdrop-blur-md p-6 space-y-3">
                        <div className="flex items-center justify-between">
                          <span className="text-xs font-bold text-slate-500 dark:text-slate-400 uppercase tracking-wider">
                            Live Payout Simulation
                          </span>
                          <span className="text-[10px] px-2 py-0.5 rounded-full bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-400 font-mono">
                            Calculated Rates
                          </span>
                        </div>

                        <div className="grid grid-cols-3 gap-3">
                          <div className="p-3 bg-slate-50 dark:bg-[#07162e] rounded-xl border border-slate-200 dark:border-sky-500/20 text-center">
                            <div className="text-base mb-1">🧪</div>
                            <div className="text-[11px] font-bold text-slate-900 dark:text-white">Lab Experiment</div>
                            <div className="text-xs font-bold text-emerald-600 dark:text-emerald-400 mt-0.5">+{economyConfig.labCompletionXp} XP</div>
                          </div>

                          <div className="p-3 bg-slate-50 dark:bg-[#07162e] rounded-xl border border-slate-200 dark:border-sky-500/20 text-center">
                            <div className="text-base mb-1">💯</div>
                            <div className="text-[11px] font-bold text-slate-900 dark:text-white">5/5 Perfect Quiz</div>
                            <div className="text-xs font-bold text-amber-500 dark:text-amber-400 mt-0.5">+{economyConfig.quizPassXp + economyConfig.perfectQuizBonusXp} XP</div>
                          </div>

                          <div className="p-3 bg-slate-50 dark:bg-[#07162e] rounded-xl border border-slate-200 dark:border-sky-500/20 text-center">
                            <div className="text-base mb-1">⚔️</div>
                            <div className="text-[11px] font-bold text-slate-900 dark:text-white">Dojo Arena Win</div>
                            <div className="text-xs font-bold text-sky-600 dark:text-sky-400 mt-0.5">+{economyConfig.arenaWinXp} XP • +{economyConfig.arenaWinCoins} 🪙</div>
                          </div>
                        </div>
                      </div>
                    </div>

                    {/* Right Column: Manual Reward & Airdrop Studio (6 cols) */}
                    <div className="lg:col-span-6 space-y-6">
                      <div className="bg-white dark:bg-[#0e2343]/90 border border-slate-200 dark:border-sky-500/20 rounded-2xl shadow-sm dark:shadow-xl dark:shadow-sky-950/40 backdrop-blur-md p-6">
                        <div className="flex items-center justify-between border-b border-slate-200 dark:border-sky-500/20 pb-4 mb-5">
                          <div className="flex items-center space-x-3">
                            <span className="text-xl">🎁</span>
                            <div>
                              <h3 className="text-base font-bold text-slate-900 dark:text-white">Student Reward & Airdrop Studio</h3>
                              <p className="text-xs text-slate-500 dark:text-slate-400">Award bonus XP & coins to an individual student or campus-wide</p>
                            </div>
                          </div>
                          <span className="text-[10px] px-2.5 py-1 bg-amber-500/15 text-amber-600 dark:text-amber-400 font-extrabold rounded-lg border border-amber-500/30">
                            AIRDROP
                          </span>
                        </div>

                        <form onSubmit={handleGrantReward} className="space-y-4">
                          <div>
                            <label className="block text-xs font-bold text-slate-700 dark:text-slate-300 uppercase tracking-wider mb-1.5">
                              Target Recipient *
                            </label>
                            <select
                              value={grantForm.userId}
                              onChange={e => setGrantForm({ ...grantForm, userId: e.target.value })}
                              className="w-full px-4 py-2.5 bg-slate-50 dark:bg-[#07152b] border border-slate-200 dark:border-sky-500/20 rounded-xl text-xs font-bold text-slate-900 dark:text-white focus:outline-none focus:border-amber-500 transition"
                            >
                              <option value="">-- Choose Target Recipient --</option>
                              <option value="all">🌐 ALL ACTIVE STUDENTS (Campus-Wide Airdrop)</option>
                              {economyStudents.map(s => (
                                <option key={s.id} value={s.id}>
                                  👤 {s.username} ({s.email}) — Lvl {s.level} • {s.xp} XP • {s.coins} Coins
                                </option>
                              ))}
                            </select>
                          </div>

                          <div className="grid grid-cols-2 gap-4">
                            <div>
                              <label className="block text-xs font-bold text-slate-700 dark:text-slate-300 uppercase tracking-wider mb-1.5">
                                Bonus XP to Grant
                              </label>
                              <input
                                type="number"
                                min="0"
                                max="10000"
                                value={grantForm.xp}
                                onChange={e => setGrantForm({ ...grantForm, xp: parseInt(e.target.value) || 0 })}
                                placeholder="100"
                                className="w-full px-4 py-2.5 bg-slate-50 dark:bg-[#07152b] border border-slate-200 dark:border-sky-500/20 rounded-xl text-xs font-mono font-bold text-slate-900 dark:text-white focus:outline-none focus:border-amber-500 transition"
                              />
                            </div>

                            <div>
                              <label className="block text-xs font-bold text-slate-700 dark:text-slate-300 uppercase tracking-wider mb-1.5">
                                Bonus Coins to Grant
                              </label>
                              <input
                                type="number"
                                min="0"
                                max="5000"
                                value={grantForm.coins}
                                onChange={e => setGrantForm({ ...grantForm, coins: parseInt(e.target.value) || 0 })}
                                placeholder="50"
                                className="w-full px-4 py-2.5 bg-slate-50 dark:bg-[#07152b] border border-slate-200 dark:border-sky-500/20 rounded-xl text-xs font-mono font-bold text-slate-900 dark:text-white focus:outline-none focus:border-amber-500 transition"
                              />
                            </div>
                          </div>

                          <div>
                            <label className="block text-xs font-bold text-slate-700 dark:text-slate-300 uppercase tracking-wider mb-1.5">
                              Grant Reason / Award Title *
                            </label>
                            <input
                              type="text"
                              value={grantForm.reason}
                              onChange={e => setGrantForm({ ...grantForm, reason: e.target.value })}
                              placeholder="e.g. Hackathon First Place, Exemplary Lab Work, Downtime Apology"
                              className="w-full px-4 py-2.5 bg-slate-50 dark:bg-[#07152b] border border-slate-200 dark:border-sky-500/20 rounded-xl text-xs text-slate-900 dark:text-white focus:outline-none focus:border-amber-500 transition"
                            />
                          </div>

                          {/* Impact Summary Pill */}
                          <div className="p-3.5 bg-amber-500/10 border border-amber-500/30 rounded-xl text-xs space-y-1">
                            <div className="font-bold text-amber-600 dark:text-amber-300 flex items-center space-x-1.5">
                              <span>✨</span>
                              <span>Estimated Award Impact:</span>
                            </div>
                            <p className="text-slate-600 dark:text-slate-300 text-[11px] leading-relaxed">
                              {grantForm.userId === 'all'
                                ? `All registered students will atomically receive +${grantForm.xp} XP and +${grantForm.coins} Coins. Any students crossing 100-XP thresholds will immediately level up.`
                                : `Target student will be credited with +${grantForm.xp} XP and +${grantForm.coins} Coins. Their current level will be recalculated atomically.`}
                            </p>
                          </div>

                          <div className="flex items-center justify-end pt-2">
                            <button
                              type="submit"
                              disabled={isGrantingReward}
                              className="px-6 py-2.5 bg-gradient-to-r from-amber-500 to-amber-600 hover:from-amber-400 hover:to-amber-500 text-slate-950 font-bold text-xs rounded-xl shadow-md transition disabled:opacity-50 flex items-center space-x-2 active:scale-95"
                            >
                              {isGrantingReward ? (
                                <>
                                  <div className="w-3.5 h-3.5 border-2 border-slate-950 border-t-transparent rounded-full animate-spin"></div>
                                  <span>Transferring Rewards...</span>
                                </>
                              ) : (
                                <>
                                  <span>🚀</span>
                                  <span>Grant Rewards Now</span>
                                </>
                              )}
                            </button>
                          </div>
                        </form>
                      </div>

                      {/* Safety Guarantee Card */}
                      <div className="bg-white dark:bg-[#0e2343]/90 border border-slate-200 dark:border-sky-500/20 rounded-2xl shadow-sm dark:shadow-xl dark:shadow-sky-950/40 backdrop-blur-md p-5 flex items-start space-x-3">
                        <span className="text-xl">🛡️</span>
                        <div className="text-xs space-y-1">
                          <h4 className="font-bold text-slate-900 dark:text-white">Audit & Balance Safety Guarantee</h4>
                          <p className="text-slate-500 dark:text-slate-400 text-[11px] leading-relaxed">
                            Reward grants perform atomic database updates in Neon PostgreSQL. Student balances (XP, coins, login streaks) are strictly additive and never reset or corrupted.
                          </p>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              )}
            </div>
          </main>

          {/* EDIT QUIZ MODAL */}
          {isQuizModalOpen && editingQuiz && (
            <div className="fixed inset-0 z-50 bg-black/60 dark:bg-black/80 backdrop-blur-sm flex items-center justify-center p-4">
              <div className="w-full max-w-xl bg-white dark:bg-[#0e2343] border border-slate-200 dark:border-sky-500/25 rounded-2xl p-6 shadow-2xl space-y-4">
                <div className="flex items-center justify-between border-b border-slate-200 dark:border-sky-500/20 pb-3">
                  <h3 className="text-base font-bold text-slate-900 dark:text-white">Edit Lab Quiz Question</h3>
                  <button
                    onClick={() => setIsQuizModalOpen(false)}
                    className="text-slate-400 hover:text-slate-700 dark:hover:text-white font-bold text-sm"
                  >
                    ✕
                  </button>
                </div>

                <div className="space-y-3 text-xs">
                  <div>
                    <label className="block font-bold text-slate-700 dark:text-slate-400 mb-1">Question Prompt</label>
                    <textarea
                      rows="3"
                      value={editingQuiz.question}
                      onChange={e => setEditingQuiz({ ...editingQuiz, question: e.target.value })}
                      className="w-full p-3 bg-slate-50 dark:bg-[#07152b] border border-slate-200 dark:border-sky-500/20 rounded-xl text-slate-900 dark:text-white focus:outline-none focus:border-sky-500 font-medium"
                    />
                  </div>

                  <div>
                    <label className="block font-bold text-slate-700 dark:text-slate-400 mb-1">Options (Select radio for correct answer)</label>
                    {editingQuiz.options.map((opt, i) => (
                      <div key={i} className="flex items-center space-x-2 mb-2">
                        <input
                          type="radio"
                          name="editCorrect"
                          checked={editingQuiz.correctAnswer === opt && Boolean(opt)}
                          onChange={() => setEditingQuiz({ ...editingQuiz, correctAnswer: opt })}
                          className="text-emerald-500 focus:ring-emerald-500"
                        />
                        <input
                          type="text"
                          value={opt}
                          onChange={e => {
                            const updated = [...editingQuiz.options];
                            updated[i] = e.target.value;
                            setEditingQuiz({ ...editingQuiz, options: updated });
                          }}
                          className="w-full p-2 bg-slate-50 dark:bg-[#07152b] border border-slate-200 dark:border-sky-500/20 rounded-xl text-xs text-slate-900 dark:text-white"
                        />
                      </div>
                    ))}
                  </div>

                  <div>
                    <label className="block font-bold text-slate-700 dark:text-slate-400 mb-1">Pedagogical Explanation</label>
                    <input
                      type="text"
                      value={editingQuiz.explanation}
                      onChange={e => setEditingQuiz({ ...editingQuiz, explanation: e.target.value })}
                      className="w-full p-2 bg-slate-50 dark:bg-[#07152b] border border-slate-200 dark:border-sky-500/20 rounded-xl text-xs text-slate-900 dark:text-white"
                    />
                  </div>
                </div>

                <div className="flex justify-end space-x-3 pt-3 border-t border-slate-200 dark:border-sky-500/20">
                  <button
                    onClick={() => setIsQuizModalOpen(false)}
                    className="px-4 py-2 bg-slate-100 dark:bg-[#142c54] hover:bg-slate-200 dark:hover:bg-[#183768] text-slate-700 dark:text-slate-300 font-bold rounded-xl text-xs transition"
                  >
                    Cancel
                  </button>
                  <button
                    onClick={handleSaveQuiz}
                    className="px-5 py-2 bg-gradient-to-r from-sky-500 to-indigo-600 hover:from-sky-400 hover:to-indigo-500 text-white font-bold rounded-xl text-xs transition shadow-sm active:scale-95"
                  >
                    Save Changes
                  </button>
                </div>
              </div>
            </div>
          )}

          {/* CONFIRM DIALOG MODAL */}
          {confirmModal.isOpen && (
            <div className="fixed inset-0 z-50 bg-black/60 dark:bg-black/80 backdrop-blur-sm flex items-center justify-center p-4">
              <div className="w-full max-w-md bg-white dark:bg-[#0e2343] border border-slate-200 dark:border-sky-500/25 rounded-2xl p-6 shadow-2xl space-y-4 animate-toast-down">
                <div className="flex items-center space-x-3 text-red-500 dark:text-red-400">
                  <span className="text-2xl">⚠️</span>
                  <h3 className="text-base font-bold text-slate-900 dark:text-white">{confirmModal.title}</h3>
                </div>
                <p className="text-xs text-slate-600 dark:text-slate-300 leading-relaxed">
                  {confirmModal.message}
                </p>
                <div className="flex justify-end space-x-3 pt-3 border-t border-slate-200 dark:border-sky-500/20">
                  <button
                    onClick={() => setConfirmModal({ ...confirmModal, isOpen: false })}
                    className="px-4 py-2 bg-slate-100 dark:bg-[#142c54] hover:bg-slate-200 dark:hover:bg-[#183768] text-slate-700 dark:text-slate-300 font-bold rounded-xl text-xs transition"
                  >
                    Cancel
                  </button>
                  <button
                    onClick={() => {
                      if (confirmModal.onConfirm) confirmModal.onConfirm();
                      setConfirmModal({ ...confirmModal, isOpen: false });
                    }}
                    className={`px-5 py-2 font-bold text-xs rounded-xl transition shadow-sm ${
                      confirmModal.isDanger
                        ? 'bg-red-600 hover:bg-red-500 text-white'
                        : 'bg-gradient-to-r from-sky-500 to-indigo-600 text-white'
                    }`}
                  >
                    {confirmModal.confirmText || 'Confirm'}
                  </button>
                </div>
              </div>
            </div>
          )}
        </div>
      );
    }

    ReactDOM.createRoot(document.getElementById('root')).render(<AdminApp />);
  </script>
</body>
</html>"""
    return Response(html_template, mimetype='text/html')
