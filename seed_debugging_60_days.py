"""
Root Runner for Seeding Debugging & Problem Solving (60 Days)
"""
import sys
import os

backend_root = os.path.dirname(os.path.abspath(__file__))
if backend_root not in sys.path:
    sys.path.insert(0, backend_root)

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
        print("\n Seeding Complete Successfully!")
        print(f"  Lesson ID:       {results['lesson_id']}")
        print(f"  Title:           {results['title']}")
        print(f"  Days / Steps:    {results['days_count']}")
        print(f"  Quizzes:         {results['quizzes_count']}")
        print(f"  Flashcards:      {results['flashcards_count']}")
    except Exception as e:
        print(f" Error during seeding: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    finally:
        seeder.disconnect()

if __name__ == "__main__":
    main()
