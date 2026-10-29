"""
Prints the comprehensive audit of all courses across all categories in Neon PostgreSQL.
"""
import os
import sys

backend_root = os.path.abspath(os.path.dirname(__file__))
if backend_root not in sys.path:
    sys.path.insert(0, backend_root)

try:
    from dotenv import load_dotenv
    load_dotenv(os.path.join(backend_root, '.env'))
except ImportError:
    pass

from prisma import Prisma

def main():
    db = Prisma()
    db.connect()

    lessons = db.lesson.find_many()

    print("\n" + "=" * 105)
    print(f"{'Category':<25} | {'Course Title':<55} | {'Steps':<6} | {'Quizzes':<8} | {'Flashcards'}")
    print("=" * 105)

    total_steps = 0
    total_quizzes = 0
    total_flashcards = 0

    sorted_lessons = sorted(lessons, key=lambda x: (x.category, x.title))

    for l in sorted_lessons:
        steps = db.lessonstep.count(where={"lessonId": l.id})
        quizzes = db.quiz.count(where={"lessonId": l.id})
        cards = db.flashcard.count(where={"lessonId": l.id})

        total_steps += steps
        total_quizzes += quizzes
        total_flashcards += cards

        print(f"{l.category:<25} | {l.title:<55} | {steps:<6} | {quizzes:<8} | {cards}")

    print("-" * 105)
    print(f"TOTALS: {len(lessons)} Courses across 10 Categories | {total_steps} Lesson Steps | {total_quizzes} Quizzes | {total_flashcards} Flashcards")
    print("=" * 105 + "\n")

    db.disconnect()

if __name__ == "__main__":
    main()
