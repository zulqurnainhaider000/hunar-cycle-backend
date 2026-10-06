"""
Executable Runner for Seeding Debugging & Problem Solving (60 Days)
Using the Universal Course Seeder Engine
"""

import sys
import os

# Ensure backend root is on sys.path
backend_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if backend_root not in sys.path:
    sys.path.insert(0, backend_root)

# Ensure Windows terminal doesn't crash on UTF-8 / emojis
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

from seeder.universal_seeder import UniversalCourseSeeder
from seeder.courses.debugging_mastery_60_days import DEBUGGING_MASTERY_COURSE_BLUEPRINT

def main():
    seeder = UniversalCourseSeeder()
    try:
        results = seeder.seed_course(DEBUGGING_MASTERY_COURSE_BLUEPRINT, verbose=True)
        print("Course Seeding Summary:")
        print(f"  Lesson ID:       {results['lesson_id']}")
        print(f"  Title:           {results['title']}")
        print(f"  Days / Steps:    {results['days_count']}")
        print(f"  Quizzes:         {results['quizzes_count']}")
        print(f"  Flashcards:      {results['flashcards_count']}")
        return results
    except Exception as e:
        print(f"Error during seeding: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    finally:
        seeder.disconnect()

if __name__ == "__main__":
    main()
