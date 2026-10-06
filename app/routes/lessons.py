from flask import Blueprint, request, jsonify
from app.db import db
from app.auth_middleware import token_required
from datetime import datetime, timedelta

lessons_bp = Blueprint('lessons', __name__, url_prefix='/api/lessons')
courses_bp = Blueprint('courses', __name__, url_prefix='/api/courses')

@courses_bp.route('', methods=['GET'])
def get_courses():
    return get_lessons()

@lessons_bp.route('', methods=['GET'])
def get_lessons():
    """
    Fetch all available lessons from PostgreSQL.
    Prioritizes courses with rich daily lesson steps (e.g. Python Mastery).
    """
    try:
        db_lessons = db.lesson.find_many()
        
        raw_counts = db.query_raw('''
            SELECT "lessonId", COUNT(*) as count 
            FROM "Flashcard" 
            GROUP BY "lessonId"
        ''')
        count_map = {row['lessonId']: row['count'] for row in raw_counts} if raw_counts else {}

        raw_step_counts = db.query_raw('''
            SELECT "lessonId", COUNT(*) as count 
            FROM "LessonStep" 
            GROUP BY "lessonId"
        ''')
        step_count_map = {row['lessonId']: row['count'] for row in raw_step_counts} if raw_step_counts else {}

        lessons_data = []
        for l in db_lessons:
            steps_cnt = step_count_map.get(l.id, 0)
            lessons_data.append({
                "id": l.id,
                "title": l.title,
                "category": l.category,
                "description": l.description,
                "color": l.color,
                "totalSteps": steps_cnt,
                "totalFlashcards": count_map.get(l.id, 0),
                "isFeatured": steps_cnt > 0 or "Python" in l.title,
                "flashcards": []
            })

        # Sort so that rich courses with steps (Python Mastery) are presented first
        lessons_data.sort(key=lambda x: (x["totalSteps"], 1 if "Python" in x["title"] else 0), reverse=True)

        return jsonify(lessons_data), 200
    except Exception as e:
        print(f"Error fetching lessons: {e}")
        return jsonify([]), 200

@lessons_bp.route('/<lesson_id>', methods=['GET'])
@token_required
def get_lesson(current_user, lesson_id):
    """
    Fetch a single lesson by ID, including its daily learning steps sequentially ordered.
    Returns the user's unlocked day as well.
    """
    with open('api_logs.txt', 'a') as f:
        f.write(f"Frontend requested get_lesson with lesson_id: {lesson_id}\n")
    try:
        lesson = db.lesson.find_unique(
            where={"id": lesson_id},
            include={"steps": True}
        )
        if not lesson:
            return jsonify({"error": "Lesson not found"}), 404
            
        steps = db.lessonstep.find_many(
            where={"lessonId": lesson_id},
            order={"order": "asc"}
        )
        
        # Get progress
        progress = db.userlessonprogress.find_first(
            where={"userId": current_user.id, "lessonId": lesson_id}
        )
        unlocked_day = progress.unlockedDay if progress else 1
        
        # Check if client requested a specific day/order
        requested_day_str = request.args.get('day') or request.args.get('order')
        active_step = None

        if steps:
            if requested_day_str and requested_day_str.isdigit():
                req_order = int(requested_day_str)
                active_step = next((s for s in steps if s.order == req_order), None)
            
            if not active_step:
                # Target the user's current unlocked day
                active_step = next((s for s in steps if s.order == unlocked_day), steps[0])

        current_content = active_step.content if active_step else (lesson.description or f"# {lesson.title}")
        current_code = active_step.codeSnippet if active_step else ""
        
        lesson_data = {
            "id": lesson.id,
            "title": lesson.title,
            "category": lesson.category,
            "description": lesson.description,
            "color": lesson.color,
            "unlockedDay": unlocked_day,
            "content": current_content,
            "theory": current_content,
            "codeSnippet": current_code,
            "currentStep": {
                "id": active_step.id if active_step else None,
                "order": active_step.order if active_step else 1,
                "title": active_step.title if active_step else lesson.title
            } if active_step else None,
            "steps": [
                {
                    "id": step.id,
                    "order": step.order,
                    "title": step.title,
                    "content": step.content,
                    "codeSnippet": step.codeSnippet
                } for step in steps
            ]
        }
        return jsonify(lesson_data), 200
    except Exception as e:
        print(f"Error fetching lesson {lesson_id}: {e}")
        return jsonify({"error": "Internal server error"}), 500

@lessons_bp.route('/<lesson_id>/days/<day_id>/complete', methods=['POST'])
@token_required
def complete_day(current_user, lesson_id, day_id):
    """
    Mark a day as completed and unlock the next day.
    """
    try:
        data = request.json or {}
        next_day = data.get('nextDay', 2)
        
        # Upsert user progress to update unlockedDay
        progress = db.userlessonprogress.find_first(
            where={"userId": current_user.id, "lessonId": lesson_id}
        )
        
        if progress:
            if progress.unlockedDay < next_day:
                db.userlessonprogress.update(
                    where={"id": progress.id},
                    data={"unlockedDay": next_day}
                )
        else:
            db.userlessonprogress.create(
                data={
                    "userId": current_user.id,
                    "lessonId": lesson_id,
                    "unlockedDay": next_day
                }
            )
            
        return jsonify({"message": "Day completed successfully", "unlockedDay": next_day}), 200
    except Exception as e:
        print(f"Error completing day: {e}")
        return jsonify({"error": "Failed to complete day"}), 500

@lessons_bp.route('/<lesson_id>/days/<day_id>/flashcards/session', methods=['POST'])
def get_daily_flashcard_session(lesson_id, day_id):
    """
    Fetch a chunk of non-repeating flashcards for a specific day.
    Expects JSON: { "exclude_ids": ["f1", "f2", ...] }
    """
    data = request.json or {}
    exclude_ids = data.get('exclude_ids', [])
    limit = 10 # Chunk size for daily quiz

    try:
        # Fetch total count of flashcards in this day
        total_count = db.flashcard.count(where={"lessonId": lesson_id, "lessonStepId": day_id})

        # Fetch chunk excluding seen ids
        query_where = {
            "lessonId": lesson_id,
            "lessonStepId": day_id,
        }
        if exclude_ids:
            query_where["id"] = {"notIn": exclude_ids}
            
        flashcards = db.flashcard.find_many(
            where=query_where,
            take=limit
        )

        cards_data = [{"id": f.id, "question": f.question, "answer": f.answer} for f in flashcards]

        return jsonify({
            "total_count": total_count,
            "flashcards": cards_data
        }), 200
    except Exception as e:
        print(f"Error fetching session: {e}")
        return jsonify({"total_count": 0, "flashcards": []}), 500

@lessons_bp.route('/progress', methods=['POST'])
@token_required
def save_progress(current_user):
    """
    Save user progress and calculate next review date based on rating.
    """
    data = request.json
    flashcard_id = data.get('flashcardId')
    rating = data.get('rating') # "Hard", "Good", "Easy"
    
    if not flashcard_id or not rating:
        return jsonify({"error": "Missing flashcardId or rating"}), 400
        
    try:
        # Simple spaced repetition logic mock
        now = datetime.now()
        if rating == "Hard":
            next_review = now + timedelta(minutes=10)
        elif rating == "Good":
            next_review = now + timedelta(days=1)
        else: # "Easy"
            next_review = now + timedelta(days=4)
            
            progress = db.userprogress.create(
            data={
                "userId": current_user.id,
                "flashcardId": flashcard_id,
                "rating": rating,
                "nextReview": next_review
            }
        )
        
        # Gamification: Award 5 XP and 1 Coin for "Good" or "Easy"
        if rating in ["Good", "Easy"]:
            user = db.user.find_unique(where={"id": current_user.id})
            new_xp = user.xp + 5
            new_coins = user.coins + 1
            new_level = max(1, (new_xp // 100) + 1)
            
            db.user.update(
                where={"id": user.id},
                data={
                    "xp": new_xp,
                    "coins": new_coins,
                    "level": new_level
                }
            )
        
        return jsonify({"message": "Progress saved successfully", "id": progress.id}), 201
    except Exception as e:
        print(f"Error saving progress: {e}")
        return jsonify({"error": "Failed to save progress"}), 500

@courses_bp.route('/<lesson_id>/quizzes', methods=['GET'])
@lessons_bp.route('/<lesson_id>/quizzes', methods=['GET'])
@token_required
def get_lesson_quizzes(current_user, lesson_id):
    """
    Fetch exactly 5 quiz questions for a lesson with options.
    Directly queries the Quiz table for the user's active day or requested step.
    """
    try:
        lesson = db.lesson.find_unique(where={"id": lesson_id})
        if not lesson:
            return jsonify({"error": "Lesson not found"}), 404

        step_id = request.args.get('step_id') or request.args.get('lessonStepId')
        day_str = request.args.get('day') or request.args.get('order')

        # If day is specified, locate step by order
        if not step_id and day_str and day_str.isdigit():
            step = db.lessonstep.find_first(
                where={"lessonId": lesson_id, "order": int(day_str)}
            )
            if step:
                step_id = step.id

        # If still no step_id, look up user's current progress
        if not step_id:
            progress = db.userlessonprogress.find_first(
                where={"userId": current_user.id, "lessonId": lesson_id}
            )
            target_order = progress.unlockedDay if progress else 1
            step = db.lessonstep.find_first(
                where={"lessonId": lesson_id, "order": target_order}
            )
            if step:
                step_id = step.id

        # Query Quiz table for this step
        db_quizzes = []
        if step_id:
            db_quizzes = db.quiz.find_many(
                where={"lessonId": lesson_id, "lessonStepId": step_id},
                take=5
            )

        # Fallback to any quizzes for this lesson
        if not db_quizzes:
            db_quizzes = db.quiz.find_many(
                where={"lessonId": lesson_id},
                take=5
            )

        if db_quizzes:
            quizzes_data = [
                {
                    "id": q.id,
                    "question": q.question,
                    "options": q.options,
                    "correctAnswer": q.correctAnswer,
                    "explanation": q.explanation,
                    "lessonStepId": q.lessonStepId
                }
                for q in db_quizzes
            ]
            return jsonify(quizzes_data), 200
        else:
            default_quizzes = [
                {
                    "id": f"{lesson_id}_q1",
                    "question": f"What is the primary objective of studying {lesson.title}?",
                    "options": [
                        f"To master core fundamentals and practical implementation of {lesson.category}.",
                        "To compile code directly into raw assembly without debugging.",
                        "To avoid writing functions and keep everything in global scope.",
                        "To bypass variable initialization rules in memory."
                    ],
                    "correctAnswer": f"To master core fundamentals and practical implementation of {lesson.category}."
                },
                {
                    "id": f"{lesson_id}_q2",
                    "question": "Which of the following is considered best practice when writing clean code?",
                    "options": [
                        "Use meaningful variable names and modular functions.",
                        "Write all logic in a single 1000-line file.",
                        "Avoid writing comments and tests altogether.",
                        "Hardcode configuration and credentials in source files."
                    ],
                    "correctAnswer": "Use meaningful variable names and modular functions."
                },
                {
                    "id": f"{lesson_id}_q3",
                    "question": "How should unexpected runtime errors be handled in robust applications?",
                    "options": [
                        "Catch specific exceptions and gracefully report or recover.",
                        "Ignore all exceptions with bare pass statements.",
                        "Crash the process immediately without logging.",
                        "Disable type checks and compiler assertions."
                    ],
                    "correctAnswer": "Catch specific exceptions and gracefully report or recover."
                },
                {
                    "id": f"{lesson_id}_q4",
                    "question": "What is the key benefit of unit testing in development?",
                    "options": [
                        "It ensures that individual units of code perform as expected and prevents regressions.",
                        "It completely eliminates the need for code reviews.",
                        "It automatically rewrites poorly optimized algorithms.",
                        "It makes the compiled binary file size smaller."
                    ],
                    "correctAnswer": "It ensures that individual units of code perform as expected and prevents regressions."
                },
                {
                    "id": f"{lesson_id}_q5",
                    "question": "Which data structure provides constant-time O(1) average lookup by key?",
                    "options": [
                        "Hash Map / Dictionary (dict in Python)",
                        "Singly Linked List",
                        "Unsorted Array",
                        "Binary Search Tree without balancing"
                    ],
                    "correctAnswer": "Hash Map / Dictionary (dict in Python)"
                }
            ]
            quizzes = default_quizzes
            
        return jsonify(quizzes[:5]), 200
    except Exception as e:
        print(f"Error fetching quizzes for lesson {lesson_id}: {e}")
        return jsonify({"error": "Failed to load quizzes"}), 500

@lessons_bp.route('/<lesson_id>/complete', methods=['POST'])
@token_required
def complete_lesson(current_user, lesson_id):
    """
    Submit quiz results, atomically calculate and update wallet rewards via Prisma transaction.
    Rewards: 10 Coins and 20 XP per correct answer.
    """
    try:
        data = request.json or {}
        correct_answers = int(data.get('correctAnswers', 0))
        correct_answers = max(0, min(5, correct_answers))
        
        coins_earned = correct_answers * 10
        xp_earned = correct_answers * 20
        
        with db.tx() as tx:
            user = tx.user.find_unique(where={"id": current_user.id})
            if not user:
                return jsonify({"error": "User not found"}), 404
                
            new_coins = user.coins + coins_earned
            new_xp = user.xp + xp_earned
            new_level = max(1, (new_xp // 100) + 1)
            
            updated_user = tx.user.update(
                where={"id": current_user.id},
                data={
                    "coins": new_coins,
                    "xp": new_xp,
                    "level": new_level
                }
            )
            
            # Update user lesson progress if lesson exists
            progress = tx.userlessonprogress.find_first(
                where={"userId": current_user.id, "lessonId": lesson_id}
            )
            if progress:
                tx.userlessonprogress.update(
                    where={"id": progress.id},
                    data={"unlockedDay": progress.unlockedDay + 1}
                )
            else:
                tx.userlessonprogress.create(
                    data={
                        "userId": current_user.id,
                        "lessonId": lesson_id,
                        "unlockedDay": 2
                    }
                )

        return jsonify({
            "message": "Lesson completed successfully!",
            "earnedCoins": coins_earned,
            "earnedXp": xp_earned,
            "correctAnswers": correct_answers,
            "totalCoins": updated_user.coins,
            "totalXp": updated_user.xp,
            "level": updated_user.level
        }), 200
    except Exception as e:
        print(f"Error completing lesson {lesson_id}: {e}")
        return jsonify({"error": "Failed to complete lesson and grant rewards"}), 500

