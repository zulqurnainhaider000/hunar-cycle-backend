from prisma import Prisma

def audit():
    db = Prisma()
    db.connect()
    try:
        lessons = db.lesson.find_many(
            where={"category": "University"},
            include={
                "steps": {
                    "include": {
                        "quizzes": True,
                        "flashcards": True
                    },
                    "order_by": {"order": "asc"}
                }
            }
        )
        if not lessons:
            print("[ERROR] No university lessons found!")
            return

        print("=" * 95)
        print(f"UNIVERSITY COURSES AUDIT REPORT ({len(lessons)} Courses Found)")
        print("=" * 95)

        for lesson in lessons:
            print(f"\nCourse: {lesson.title}")
            print(f"Lesson ID: {lesson.id} | Category: {lesson.category} | Total Steps: {len(lesson.steps)}")
            print("-" * 95)
            print(f"{'Lab #':<6} | {'Order':<5} | {'Lab Title':<48} | {'Quizzes':<8} | {'Flashcards':<10}")
            print("-" * 95)

            for s in lesson.steps:
                print(f"Lab {s.order:<2} | {s.order:<5} | {s.title[:48]:<48} | {len(s.quizzes):<8} | {len(s.flashcards):<10}")

            total_q = sum(len(s.quizzes) for s in lesson.steps)
            total_fc = sum(len(s.flashcards) for s in lesson.steps)
            print("-" * 95)
            print(f"TOTAL: {len(lesson.steps)} Steps | {total_q} Quizzes | {total_fc} Flashcards")
        print("=" * 95)
    finally:
        db.disconnect()

if __name__ == "__main__":
    audit()
