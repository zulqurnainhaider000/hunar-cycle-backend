import json
import os
from prisma import Prisma

def seed():
    db = Prisma()
    db.connect()

    print("Fetching Python lesson...")
    python_lesson = db.lesson.find_first(where={"title": {"contains": "Python"}})

    if not python_lesson:
        python_lesson = db.lesson.create({
            "title": "Python Programming Fundamentals",
            "category": "TECH",
            "description": "A massive, comprehensive 30-day course covering from Python basics to advanced capstone projects, designed for complete beginners.",
            "color": "#3B82F6"
        })

    print("Cleaning up old lesson steps and flashcards for Python...")
    db.flashcard.delete_many(where={"lessonId": python_lesson.id})
    db.lessonstep.delete_many(where={"lessonId": python_lesson.id})

    # Load data from the 3 JSON files
    all_days_data = []
    
    files = ["data_days_1_10.json", "data_days_11_20.json", "data_days_21_30.json"]
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    for filename in files:
        filepath = os.path.join(base_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            all_days_data.extend(json.load(f))
            
    print(f"Loaded {len(all_days_data)} days of curriculum data.")

    # Seed LessonSteps
    print("Seeding Lesson Steps...")
    created_steps_map = {} # Map order/day to step ID
    for day in all_days_data:
        s = db.lessonstep.create({
            "lessonId": python_lesson.id,
            "order": day["order"],
            "title": day["title"],
            "content": day["content"],
            "codeSnippet": day["codeSnippet"]
        })
        created_steps_map[day["order"]] = s.id

    # Seed Flashcards
    print("Seeding Flashcards...")
    flashcards_to_insert = []
    
    for day in all_days_data:
        step_id = created_steps_map[day["order"]]
        for fc in day["flashcards"]:
            flashcards_to_insert.append({
                "question": fc["q"], 
                "answer": fc["a"], 
                "lessonId": python_lesson.id,
                "lessonStepId": step_id
            })

    # Insert flashcards in batches
    batch_size = 50
    for i in range(0, len(flashcards_to_insert), batch_size):
        batch = flashcards_to_insert[i:i+batch_size]
        db.flashcard.create_many(data=batch)

    print(f"Successfully seeded {len(all_days_data)} lesson steps and {len(flashcards_to_insert)} flashcards!")
    db.disconnect()

if __name__ == "__main__":
    seed()
