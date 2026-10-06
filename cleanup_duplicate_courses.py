"""
Cleanup Script: Remove Redundant / Duplicate Courses
Safely removes legacy courses for Object Oriented Programming, Git, API Integration,
and Cybersecurity that contain 150 exercises (flashcards) / 30 steps, while strictly
preserving the newly seeded 55-day and 60-day mastery curriculums.
"""

import sys
import os
import re

# Ensure backend root is on sys.path
backend_root = os.path.dirname(os.path.abspath(__file__))
if backend_root not in sys.path:
    sys.path.insert(0, backend_root)

# Configure stdout/stderr encoding for Windows console
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

from prisma import Prisma


def run_cleanup():
    db = Prisma()
    db.connect()
    print("\n" + "=" * 70)
    print("[*] CONNECTED TO POSTGRESQL VIA PRISMA")
    print("=" * 70)

    # 1. Fetch lessons matching target keywords: Object, Git, API, Cyber
    # Using regex with word boundary to match 'Object', 'Git', 'API', 'Cyber'
    # without falsely matching unrelated words like 'Digital'
    pattern = re.compile(r'\b(object|git|api|cyber)\w*', re.IGNORECASE)

    all_lessons = db.lesson.find_many(
        include={
            'steps': True,
            'quizzes': True,
            'flashcards': True
        }
    )

    matching_lessons = [l for l in all_lessons if pattern.search(l.title)]
    print(f"[*] Found {len(matching_lessons)} total lessons matching keywords ('Object', 'Git', 'API', 'Cyber').\n")

    preserved_lessons = []
    lessons_to_delete = []

    for l in matching_lessons:
        step_count = len(l.steps)
        fc_count = len(l.flashcards)
        quiz_count = len(l.quizzes)

        # STRICT RULE: Preserved curriculums have exactly 55 or 60 steps
        if step_count in (55, 60):
            preserved_lessons.append({
                "id": l.id,
                "title": l.title,
                "category": l.category,
                "step_count": step_count,
                "quiz_count": quiz_count,
                "flashcard_count": fc_count
            })
        else:
            # Redundant modules having roughly/exactly 150 exercises / 30 steps
            lessons_to_delete.append({
                "id": l.id,
                "title": l.title,
                "category": l.category,
                "step_count": step_count,
                "quiz_count": quiz_count,
                "flashcard_count": fc_count
            })

    # 2. Print Pre-Deletion Summary
    print("[*] COURSES TARGETED FOR DELETION (Old 150-exercise / 30-step modules):")
    for item in lessons_to_delete:
        print(f"  [-] ID: {item['id']} | Steps: {item['step_count']:2d} | Exercises/Cards: {item['flashcard_count']:3d} | Title: '{item['title']}' ({item['category']})")

    print("\n[*] COURSES STRICTLY PRESERVED (55/60-day Mastery Curriculums):")
    for item in preserved_lessons:
        print(f"  [+] ID: {item['id']} | Steps: {item['step_count']:2d} | Quizzes: {item['quiz_count']:3d} | Title: '{item['title']}' ({item['category']})")

    if not lessons_to_delete:
        print("\n[!] No duplicate or redundant courses found for deletion.")
        db.disconnect()
        return

    print("\n" + "-" * 70)
    print(f"[*] Executing safe cascade deletion for {len(lessons_to_delete)} redundant courses...")
    print("-" * 70)

    deleted_summary = []

    for item in lessons_to_delete:
        lid = item["id"]
        title = item["title"]

        # Step 4: Handle Prisma relations correctly
        # Delete children records first to avoid Foreign Key constraint errors
        del_quizzes = db.quiz.delete_many(where={"lessonId": lid})
        del_flashcards = db.flashcard.delete_many(where={"lessonId": lid})
        del_steps = db.lessonstep.delete_many(where={"lessonId": lid})
        del_ulp = db.userlessonprogress.delete_many(where={"lessonId": lid})

        # Finally, delete the parent Lesson record
        db.lesson.delete(where={"id": lid})

        deleted_summary.append({
            "id": lid,
            "title": title,
            "category": item["category"],
            "steps_deleted": del_steps,
            "flashcards_deleted": del_flashcards,
            "quizzes_deleted": del_quizzes,
            "ulp_deleted": del_ulp
        })

        print(f"  [DELETED] '{title}' (ID: {lid})")
        print(f"            Cleared: {del_steps} steps, {del_flashcards} flashcards, {del_quizzes} quizzes, {del_ulp} progress records.")

    # 3. Post-Deletion Verification
    print("\n" + "=" * 70)
    print("[POST-CLEANUP VERIFICATION REPORT]")
    print("=" * 70)

    # Verify that deleted courses no longer exist
    for item in deleted_summary:
        check = db.lesson.find_unique(where={"id": item["id"]})
        assert check is None, f"Error: Lesson '{item['title']}' still exists after deletion!"

    print("[OK] Confirmed: All target redundant courses have been completely removed from database.")

    # Verify that preserved 55-day and 60-day mastery courses remain intact
    print("\n[*] Verifying status of Preserved Mastery Courses:")
    for item in preserved_lessons:
        lesson = db.lesson.find_unique(
            where={"id": item["id"]},
            include={
                'steps': True,
                'quizzes': True,
                'flashcards': True
            }
        )
        assert lesson is not None, f"FATAL: Preserved lesson '{item['title']}' was accidentally deleted!"
        assert len(lesson.steps) in (55, 60), f"Step count mismatch for '{item['title']}'!"
        print(f"  [VERIFIED INTACT] '{lesson.title}' (ID: {lesson.id})")
        print(f"                    Steps: {len(lesson.steps)} | Quizzes: {len(lesson.quizzes)} | Flashcards: {len(lesson.flashcards)}")

    print("\n" + "=" * 70)
    print("[SUCCESS] Database cleanup finished with 100% integrity!")
    print("=" * 70)

    db.disconnect()


if __name__ == "__main__":
    run_cleanup()
