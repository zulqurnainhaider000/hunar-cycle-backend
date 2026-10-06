import time
from prisma import Prisma

def generate_flashcards_for_day(lesson_id, step_id, day, title, category):
    # Dummy flashcards based on day
    return [
        {
            "lessonId": lesson_id,
            "lessonStepId": step_id,
            "question": f"What is the main focus of Day {day} in {title}?",
            "answer": f"The main focus is understanding the core principles of {title}."
        },
        {
            "lessonId": lesson_id,
            "lessonStepId": step_id,
            "question": f"How do you apply {category} skills learned in Day {day}?",
            "answer": "By practicing the provided blueprints and code examples."
        }
    ]

def get_day_content(day, title, category):
    title_low = title.lower()
    
    if day == 1:
        return f"Day 1: Introduction to {title}", f"Welcome to Day 1! Today we lay the groundwork for {title}.", f"print('Hello Day 1 of {title}')" if 'python' in title_low else None
    elif day == 2:
        return f"Day 2: Core Concepts", f"Now that you know the basics, let's dive into the core concepts of {title}.", None
    elif day == 3:
        return f"Day 3: Practical Application", f"Time to apply what we've learned in {title}.", "/* Day 3 Practice */"
    elif day == 4:
        return f"Day 4: Deep Dive", f"Let's explore advanced topics in {title}.", None
    else:
        return f"Day 5: Final Review", f"Congratulations on reaching Day 5! Review everything before your final quiz.", None

def seed():
    db = Prisma()
    db.connect()

    print("Fetching all lessons...")
    lessons = db.lesson.find_many()

    if not lessons:
        print("No lessons found. Exiting.")
        db.disconnect()
        return

    print("Cleaning up old steps and flashcards...")
    db.flashcard.delete_many()
    db.lessonstep.delete_many()

    print("Generating Day-wise curriculum...")
    for lesson in lessons:
        for day in range(1, 6):
            title, content, code = get_day_content(day, lesson.title, lesson.category)
            
            # Create the Day (LessonStep)
            step = db.lessonstep.create(
                data={
                    "lessonId": lesson.id,
                    "order": day,
                    "title": title,
                    "content": content,
                    "codeSnippet": code
                }
            )
            
            # Create Flashcards for the Day
            cards = generate_flashcards_for_day(lesson.id, step.id, day, lesson.title, lesson.category)
            db.flashcard.create_many(data=cards)

    print("Successfully seeded Day-wise curriculum and daily quizzes!")
    db.disconnect()

if __name__ == "__main__":
    seed()
