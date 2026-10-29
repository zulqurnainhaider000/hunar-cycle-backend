"""
Non-Destructive Database Seeder Runner for HunarCircle
Safely populates complete course curriculums into Neon PostgreSQL via Prisma.

CRITICAL SAFETY GUARANTEES:
1. SAFE MODE ONLY: Zero destruction of existing user tables, user records,
   authentication states, or credentials.
2. Dynamic configuration: DATABASE_URL is loaded dynamically from the environment.
3. Idempotent: Can be run multiple times safely without duplicate key violations.
"""

import sys
import os
import time
import argparse
from typing import List, Dict, Any, Optional

# Ensure UTF-8 output on Windows console
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

# Ensure backend root is on sys.path
backend_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if backend_root not in sys.path:
    sys.path.insert(0, backend_root)

# Load environment dynamically
try:
    from dotenv import load_dotenv
    env_path = os.path.join(backend_root, '.env')
    if os.path.exists(env_path):
        load_dotenv(dotenv_path=env_path)
    else:
        load_dotenv()
except ImportError:
    pass

from prisma import Prisma
from seeder.course_blueprint import CourseBlueprint
from seeder.universal_seeder import UniversalCourseSeeder

# Import all 10 verified curriculum blueprints
from courses.python_mastery_35_days import PYTHON_MASTERY_COURSE_BLUEPRINT
from seeder.courses.api_mastery_60_days import API_MASTERY_COURSE_BLUEPRINT
from seeder.courses.cybersecurity_mastery_60_days import CYBERSECURITY_MASTERY_COURSE_BLUEPRINT
from seeder.courses.database_mastery_40_days import DATABASE_MASTERY_COURSE_BLUEPRINT
from seeder.courses.debugging_mastery_60_days import DEBUGGING_MASTERY_COURSE_BLUEPRINT
from seeder.courses.flask_mastery_40_days import FLASK_MASTERY_COURSE_BLUEPRINT
from seeder.courses.git_mastery_55_days import GIT_MASTERY_COURSE_BLUEPRINT
from seeder.courses.mobile_mastery_40_days import MOBILE_MASTERY_COURSE_BLUEPRINT
from seeder.courses.networking_mastery_60_days import NETWORKING_MASTERY_COURSE_BLUEPRINT
from seeder.courses.oop_mastery_55_days import OOP_MASTERY_COURSE_BLUEPRINT

# Import category-specific curriculum blueprints for non-tech categories
from seeder.courses.business_mastery import BUSINESS_MASTERY_COURSE_BLUEPRINT
from seeder.courses.language_mastery import LANGUAGE_MASTERY_COURSE_BLUEPRINT
from seeder.courses.design_mastery import DESIGN_MASTERY_COURSE_BLUEPRINT
from seeder.courses.cooking_mastery import COOKING_MASTERY_COURSE_BLUEPRINT
from seeder.courses.medical_billing_mastery import MEDICAL_BILLING_MASTERY_COURSE_BLUEPRINT
from seeder.courses.freelancing_mastery import FREELANCING_MASTERY_COURSE_BLUEPRINT
from seeder.courses.finance_crypto_mastery import FINANCE_CRYPTO_MASTERY_COURSE_BLUEPRINT

ALL_BLUEPRINTS: List[CourseBlueprint] = [
    PYTHON_MASTERY_COURSE_BLUEPRINT,
    API_MASTERY_COURSE_BLUEPRINT,
    CYBERSECURITY_MASTERY_COURSE_BLUEPRINT,
    DATABASE_MASTERY_COURSE_BLUEPRINT,
    DEBUGGING_MASTERY_COURSE_BLUEPRINT,
    FLASK_MASTERY_COURSE_BLUEPRINT,
    GIT_MASTERY_COURSE_BLUEPRINT,
    MOBILE_MASTERY_COURSE_BLUEPRINT,
    NETWORKING_MASTERY_COURSE_BLUEPRINT,
    OOP_MASTERY_COURSE_BLUEPRINT,
    BUSINESS_MASTERY_COURSE_BLUEPRINT,
    LANGUAGE_MASTERY_COURSE_BLUEPRINT,
    DESIGN_MASTERY_COURSE_BLUEPRINT,
    MEDICAL_BILLING_MASTERY_COURSE_BLUEPRINT,
    FREELANCING_MASTERY_COURSE_BLUEPRINT,
    FINANCE_CRYPTO_MASTERY_COURSE_BLUEPRINT,
]


def mask_db_url(url: Optional[str]) -> str:
    """Masks database credentials for safe logging."""
    if not url:
        return "[NOT SET]"
    try:
        from urllib.parse import urlparse
        parsed = urlparse(url)
        netloc = parsed.hostname or "unknown"
        if parsed.port:
            netloc += f":{parsed.port}"
        return f"{parsed.scheme}://***:***@{netloc}{parsed.path}"
    except Exception:
        return "postgresql://***:***@...[masked]"


def audit_database(db: Prisma, stage: str = "CURRENT") -> Dict[str, int]:
    """Inspects and returns counts for all core tables without modifying any data."""
    counts = {
        "users": db.user.count(),
        "lessons": db.lesson.count(),
        "lesson_steps": db.lessonstep.count(),
        "quizzes": db.quiz.count(),
        "flashcards": db.flashcard.count(),
        "user_progress": db.userlessonprogress.count(),
        "events": db.event.count(),
        "turfs": db.turf.count(),
        "gigs": db.gig.count(),
    }
    print(f"\n[{stage} DATABASE STATE AUDIT]")
    print(f"  • Users (Protected):       {counts['users']}")
    print(f"  • Lessons:                  {counts['lessons']}")
    print(f"  • Lesson Steps (Days):      {counts['lesson_steps']}")
    print(f"  • Quizzes:                  {counts['quizzes']}")
    print(f"  • Flashcards:               {counts['flashcards']}")
    print(f"  • User Lesson Progress:     {counts['user_progress']}")
    print(f"  • Events:                   {counts['events']}")
    print(f"  • Turfs:                    {counts['turfs']}")
    print(f"  • Gigs:                     {counts['gigs']}")
    print("-" * 60)
    return counts


def seed_courses(
    selected_blueprints: List[CourseBlueprint],
    verbose: bool = True
) -> List[Dict[str, Any]]:
    """
    Executes the seeding workflow using Prisma and UniversalCourseSeeder.
    Verifies connections, ensures user data protection, and handles errors safely.
    """
    raw_db_url = os.environ.get("DATABASE_URL")
    if not raw_db_url:
        raise ValueError("CRITICAL: DATABASE_URL environment variable is not defined.")

    print("\n" + "=" * 70)
    print("HUNARCIRCLE - UNIVERSAL DATABASE SEEDER RUNNER")
    print(f"Target Database: {mask_db_url(raw_db_url)}")
    print("Mode: SAFE NON-DESTRUCTIVE EXECUTION")
    print("=" * 70)

    db = Prisma()
    start_time = time.time()
    results: List[Dict[str, Any]] = []

    try:
        print("[*] Connecting to Neon PostgreSQL via Prisma...")
        db.connect()
        if not db.is_connected():
            raise ConnectionError("Failed to establish active connection to Neon PostgreSQL.")
        print("[OK] Successfully connected to Neon PostgreSQL!")

        # Step 1: Capture pre-seeding baseline to guarantee zero data loss
        baseline = audit_database(db, stage="PRE-SEEDING BASELINE")
        initial_user_count = baseline["users"]

        # Step 2: Initialize universal seeder instance sharing active connection
        seeder = UniversalCourseSeeder(db=db)

        # Step 3: Iterate and seed each course blueprint
        total_courses = len(selected_blueprints)
        print(f"\n[*] Preparing to seed {total_courses} course blueprint(s)...")

        for idx, bp in enumerate(selected_blueprints, start=1):
            course_start = time.time()
            print(f"\n>>> [{idx}/{total_courses}] Processing Course: '{bp.title}' ({bp.category})")
            print(f"    Expected Days/Steps: {len(bp.days)} | Quizzes: {len(bp.days) * 5} | Flashcards: {len(bp.days) * 5}")

            try:
                # Execute standard idempotent course seeding
                seed_result = seeder.seed_course(bp, verbose=verbose)
                course_elapsed = time.time() - course_start

                # Post-insert verification for this course
                lesson_id = seed_result["lesson_id"]
                actual_steps = db.lessonstep.count(where={"lessonId": lesson_id})
                actual_quizzes = db.quiz.count(where={"lessonId": lesson_id})
                actual_flashcards = db.flashcard.count(where={"lessonId": lesson_id})

                verification_passed = (
                    actual_steps == len(bp.days) and
                    actual_quizzes == len(bp.days) * 5 and
                    actual_flashcards == len(bp.days) * 5
                )

                status = "SUCCESS" if verification_passed else "MISMATCH"
                print(f"    [VERIFIED] Lesson ID: {lesson_id}")
                print(f"    [VERIFIED] Steps: {actual_steps}/{len(bp.days)} | Quizzes: {actual_quizzes} | Flashcards: {actual_flashcards}")
                print(f"    [TIME] Completed in {course_elapsed:.2f}s | Status: {status}")

                results.append({
                    "title": bp.title,
                    "category": bp.category,
                    "days": actual_steps,
                    "quizzes": actual_quizzes,
                    "flashcards": actual_flashcards,
                    "status": status,
                    "lesson_id": lesson_id,
                    "elapsed_s": course_elapsed
                })

            except Exception as course_err:
                course_elapsed = time.time() - course_start
                print(f"    [ERROR] Failed to seed course '{bp.title}': {course_err}")
                import traceback
                traceback.print_exc()
                results.append({
                    "title": bp.title,
                    "category": bp.category,
                    "days": 0,
                    "quizzes": 0,
                    "flashcards": 0,
                    "status": f"FAILED: {course_err}",
                    "lesson_id": None,
                    "elapsed_s": course_elapsed
                })

        # Step 4: Capture post-seeding database state
        post_audit = audit_database(db, stage="POST-SEEDING STATE")

        # Step 5: Verification of user preservation directive
        if post_audit["users"] != initial_user_count:
            print("\n[CRITICAL WARNING] User count discrepancy detected!")
            print(f"  Baseline Users: {initial_user_count} | Post-seed Users: {post_audit['users']}")
        else:
            print(f"\n[OK] USER DATA PRESERVATION CONFIRMED: All {initial_user_count} user record(s) intact.")

        # Step 6: Print consolidated execution summary table
        total_time = time.time() - start_time
        print("\n" + "=" * 80)
        print("SEEDING EXECUTION SUMMARY")
        print("=" * 80)
        header = f"{'#':<3} | {'Course Title':<42} | {'Category':<10} | {'Days':<5} | {'Quizzes':<7} | {'Cards':<7} | {'Status'}"
        print(header)
        print("-" * 80)

        total_days = 0
        total_quizzes = 0
        total_flashcards = 0

        for idx, r in enumerate(results, start=1):
            short_title = (r['title'][:39] + '...') if len(r['title']) > 42 else r['title']
            print(f"{idx:<3} | {short_title:<42} | {r['category']:<10} | {r['days']:<5} | {r['quizzes']:<7} | {r['flashcards']:<7} | {r['status']}")
            total_days += r['days']
            total_quizzes += r['quizzes']
            total_flashcards += r['flashcards']

        print("-" * 80)
        print(f"TOTALS: {len(results)} Courses | {total_days} Days/Steps | {total_quizzes} Quizzes | {total_flashcards} Flashcards")
        print(f"Total Elapsed Time: {total_time:.2f}s")
        print("=" * 80 + "\n")

        return results

    finally:
        if db.is_connected():
            print("[*] Gracefully disconnecting Prisma from Neon PostgreSQL...")
            db.disconnect()
            print("[OK] Prisma connection closed.")


def main():
    parser = argparse.ArgumentParser(description="HunarCircle Non-Destructive Course Seeder")
    parser.add_argument(
        "--course",
        type=str,
        default=None,
        help="Optional case-insensitive substring filter to seed specific course(s) only."
    )
    parser.add_argument(
        "--verify-only",
        action="store_true",
        help="Inspect database state without seeding any courses."
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Reduce logging verbosity during day-by-day insertion."
    )
    args = parser.parse_args()

    if args.verify_only:
        db = Prisma()
        db.connect()
        try:
            audit_database(db, stage="VERIFY-ONLY")
        finally:
            db.disconnect()
        return

    selected = ALL_BLUEPRINTS
    if args.course:
        query = args.course.lower()
        selected = [bp for bp in ALL_BLUEPRINTS if query in bp.title.lower() or query in bp.category.lower()]
        if not selected:
            print(f"[!] No blueprints match filter '{args.course}'.")
            print("Available courses:")
            for bp in ALL_BLUEPRINTS:
                print(f"  • {bp.title} ({bp.category})")
            sys.exit(1)

    seed_courses(selected, verbose=not args.quiet)


if __name__ == "__main__":
    main()
