"""
Seeds the 7 new category course blueprints into Neon PostgreSQL.
Safely preserves all user data, authentication state, and existing courses.
"""

import os
import sys

# Ensure UTF-8 output
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

backend_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if backend_root not in sys.path:
    sys.path.insert(0, backend_root)

# Load environment
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
from seeder.universal_seeder import UniversalCourseSeeder
from seeder.courses.business_mastery import BUSINESS_MASTERY_COURSE_BLUEPRINT
from seeder.courses.language_mastery import LANGUAGE_MASTERY_COURSE_BLUEPRINT
from seeder.courses.design_mastery import DESIGN_MASTERY_COURSE_BLUEPRINT
from seeder.courses.cooking_mastery import COOKING_MASTERY_COURSE_BLUEPRINT
from seeder.courses.medical_billing_mastery import MEDICAL_BILLING_MASTERY_COURSE_BLUEPRINT
from seeder.courses.freelancing_mastery import FREELANCING_MASTERY_COURSE_BLUEPRINT
from seeder.courses.finance_crypto_mastery import FINANCE_CRYPTO_MASTERY_COURSE_BLUEPRINT

NEW_BLUEPRINTS = [
    BUSINESS_MASTERY_COURSE_BLUEPRINT,
    LANGUAGE_MASTERY_COURSE_BLUEPRINT,
    DESIGN_MASTERY_COURSE_BLUEPRINT,
    COOKING_MASTERY_COURSE_BLUEPRINT,
    MEDICAL_BILLING_MASTERY_COURSE_BLUEPRINT,
    FREELANCING_MASTERY_COURSE_BLUEPRINT,
    FINANCE_CRYPTO_MASTERY_COURSE_BLUEPRINT,
]

def main():
    print("=" * 70)
    print("SEEDING 7 CATEGORY BLUEPRINTS INTO NEON POSTGRESQL")
    print("=" * 70)

    db = Prisma()
    db.connect()

    initial_users = db.user.count()
    print(f"[*] Baseline user count: {initial_users} (PROTECTED)")

    seeder = UniversalCourseSeeder(db=db)

    for bp in NEW_BLUEPRINTS:
        print(f"\n[*] Seeding {bp.title} (Category: {bp.category})...")
        res = seeder.seed_course(bp, verbose=True)
        print(f"[OK] Seeded {bp.title}: {res['days_count']} steps, {res['quizzes_count']} quizzes, {res['flashcards_count']} cards.")

    post_users = db.user.count()
    if post_users != initial_users:
        print(f"\n[ALERT] User count changed! {initial_users} -> {post_users}")
    else:
        print(f"\n[VERIFIED] User count preserved: {post_users} users intact.")

    print("\n--- ALL LESSONS IN DATABASE ---")
    lessons = db.lesson.find_many()
    for l in lessons:
        step_count = db.lessonstep.count(where={"lessonId": l.id})
        quiz_count = db.quiz.count(where={"lessonId": l.id})
        print(f"  • {l.title:<46} | Category: {l.category:<25} | Steps: {step_count:<3} | Quizzes: {quiz_count}")

    db.disconnect()
    print("\n[SUCCESS] All 7 categories successfully seeded into Neon PostgreSQL!")

if __name__ == "__main__":
    main()
