"""
Universal Course Seeder Engine
Enforces the mandatory template for all courses on the platform:
- One Topic Per Day
- Deep ELI5 Theory Content with Real-World Analogy
- 4-5 Progressive Code Snippets
- Daily Coding Challenge (Executable)
- Exactly 5 Multiple-Choice Questions per Day linked to Lesson and LessonStep
- Backwards-compatible Flashcard generation
- Idempotent cleanup and atomic/batch database ingestion
"""

import sys
from typing import Dict, Any, Optional
from prisma import Prisma
from seeder.course_blueprint import CourseBlueprint, DayBlueprint


class UniversalCourseSeeder:
    def __init__(self, db: Optional[Prisma] = None):
        self.db = db or Prisma()
        self._owns_db_connection = db is None

    def connect(self):
        if self._owns_db_connection and not self.db.is_connected():
            self.db.connect()

    def disconnect(self):
        if self._owns_db_connection and self.db.is_connected():
            self.db.disconnect()

    def seed_course(self, blueprint: CourseBlueprint, verbose: bool = True) -> Dict[str, Any]:
        """
        Validates and seeds any course blueprint into PostgreSQL via Prisma.
        Idempotent: cleans up previous steps, quizzes, and flashcards for this course.
        """
        if verbose:
            print(f"\n=======================================================")
            print(f"[*] Starting Universal Seeder for: '{blueprint.title}'")
            print(f"    Category: {blueprint.category} | Days: {len(blueprint.days)}")
            print(f"=======================================================")

        # 1. Strict Blueprint Validation
        if verbose:
            print("[*] Step 1: Validating course blueprint against universal standards...")
        blueprint.validate()
        if verbose:
            print("    [OK] Blueprint validation passed successfully!")

        self.connect()

        # 2. Find or Create Lesson Container
        if verbose:
            print(f"[*] Step 2: Locating or creating Lesson '{blueprint.title}'...")
        lesson = self.db.lesson.find_first(
            where={"title": {"contains": blueprint.title}}
        )

        if not lesson:
            lesson = self.db.lesson.create(
                data={
                    "title": blueprint.title,
                    "category": blueprint.category,
                    "description": blueprint.description,
                    "color": blueprint.color,
                }
            )
            if verbose:
                print(f"    [+] Created new Lesson: ID={lesson.id}")
        else:
            # Update metadata if needed
            lesson = self.db.lesson.update(
                where={"id": lesson.id},
                data={
                    "category": blueprint.category,
                    "description": blueprint.description,
                    "color": blueprint.color,
                }
            )
            if verbose:
                print(f"    [*] Found existing Lesson: ID={lesson.id} (updated metadata)")

        # 3. Clean previous steps, quizzes, and flashcards idempotently
        if verbose:
            print("[*] Step 3: Cleaning existing steps, quizzes, and flashcards for this lesson...")
        deleted_quizzes = self.db.quiz.delete_many(where={"lessonId": lesson.id})
        deleted_flashcards = self.db.flashcard.delete_many(where={"lessonId": lesson.id})
        deleted_steps = self.db.lessonstep.delete_many(where={"lessonId": lesson.id})
        if verbose:
            print(f"    Cleared: {deleted_steps} steps, {deleted_quizzes} quizzes, {deleted_flashcards} flashcards.")

        # 4. Ingest Days, LessonSteps, Quizzes, and Flashcards
        if verbose:
            print("[*] Step 4: Generating and inserting daily lessons, quizzes, and code challenges...")

        total_steps_created = 0
        total_quizzes_created = 0
        total_flashcards_created = 0

        quizzes_batch = []
        flashcards_batch = []

        for day in blueprint.days:
            # Generate the unified, rich Markdown content
            full_markdown_content = day.generate_markdown()
            code_snippet = day.get_consolidated_code_snippet()

            # Create LessonStep
            step = self.db.lessonstep.create(
                data={
                    "lessonId": lesson.id,
                    "order": day.order,
                    "title": day.title,
                    "content": full_markdown_content,
                    "codeSnippet": code_snippet,
                }
            )
            total_steps_created += 1

            # Prepare Quizzes
            for q in day.quizzes:
                quizzes_batch.append({
                    "lessonId": lesson.id,
                    "lessonStepId": step.id,
                    "question": q.question,
                    "options": q.options,
                    "correctAnswer": q.correct_answer,
                    "explanation": q.explanation or f"Correct answer is '{q.correct_answer}' based on Day {day.order} theory."
                })

            # Prepare Flashcards for backwards compatibility
            for q in day.quizzes:
                flashcards_batch.append({
                    "lessonId": lesson.id,
                    "lessonStepId": step.id,
                    "question": q.question,
                    "answer": q.correct_answer,
                })

            if verbose and (day.order % 5 == 0 or day.order == len(blueprint.days)):
                print(f"    -> Seeded Day {day.order}/{len(blueprint.days)}: '{day.title}' ({'Project Day' if day.is_project_day else 'Core Theory'})")

        # 5. Batch Insert Quizzes into DB
        if verbose:
            print(f"[*] Step 5: Ingesting {len(quizzes_batch)} Quizzes in batches...")
        batch_size = 50
        for i in range(0, len(quizzes_batch), batch_size):
            batch = quizzes_batch[i:i + batch_size]
            self.db.quiz.create_many(data=batch)
            total_quizzes_created += len(batch)

        # 6. Batch Insert Flashcards into DB
        if verbose:
            print(f"[*] Step 6: Ingesting {len(flashcards_batch)} Flashcards in batches...")
        for i in range(0, len(flashcards_batch), batch_size):
            batch = flashcards_batch[i:i + batch_size]
            self.db.flashcard.create_many(data=batch)
            total_flashcards_created += len(batch)

        if verbose:
            print(f"\n[OK] Successfully seeded course '{blueprint.title}'!")
            print(f"    * Total Days/Steps: {total_steps_created}")
            print(f"    * Total Quizzes:    {total_quizzes_created}")
            print(f"    * Total Flashcards: {total_flashcards_created}")
            print(f"=======================================================\n")

        return {
            "lesson_id": lesson.id,
            "title": lesson.title,
            "days_count": total_steps_created,
            "quizzes_count": total_quizzes_created,
            "flashcards_count": total_flashcards_created,
        }
