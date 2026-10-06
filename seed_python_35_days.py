"""
Executable Runner for Seeding Python Mastery (35 Days)
Using the Universal Course Seeder Engine
"""

import sys
import os

# Add backend directory to sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Ensure Windows terminal doesn't crash on UTF-8 / emojis
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

from seeder.universal_seeder import UniversalCourseSeeder
from courses.python_mastery_35_days import PYTHON_MASTERY_COURSE_BLUEPRINT

def main():
    seeder = UniversalCourseSeeder()
    try:
        results = seeder.seed_course(PYTHON_MASTERY_COURSE_BLUEPRINT, verbose=True)
        print("Course Seeding Summary:")
        print(f"  Lesson ID:       {results['lesson_id']}")
        print(f"  Title:           {results['title']}")
        print(f"  Days / Steps:    {results['days_count']}")
        print(f"  Quizzes:         {results['quizzes_count']}")
        print(f"  Flashcards:      {results['flashcards_count']}")
    except Exception as e:
        print(f"❌ Error during seeding: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    finally:
        seeder.disconnect()

if __name__ == "__main__":
    main()
