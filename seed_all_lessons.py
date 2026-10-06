import os
from prisma import Prisma

# We need to extract dummy_lessons from lessons.py, or we can just copy-paste them, but importing is easier.
# We have to parse it out since dummy_lessons is inside the get_lessons function.
# Wait, it's inside the function, so we can't just import it. Let's read the file and extract it via ast or regex,
# or simply we can just use a regex/eval to get it.
import ast

def get_dummy_lessons():
    with open('app/routes/lessons.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract the dummy_lessons list
    start_idx = content.find('dummy_lessons = [')
    if start_idx == -1:
        raise Exception("Could not find dummy_lessons")
    
    start_idx += len('dummy_lessons = ')
    # find the end of the array by matching brackets
    brackets = 0
    end_idx = -1
    for i in range(start_idx, len(content)):
        if content[i] == '[':
            brackets += 1
        elif content[i] == ']':
            brackets -= 1
            if brackets == 0:
                end_idx = i + 1
                break
    
    list_str = content[start_idx:end_idx]
    # some values might use true/false instead of True/False, but it's JSON so let's just use json.loads
    import json
    return json.loads(list_str)


def seed():
    db = Prisma()
    db.connect()

    print("Cleaning up old lessons...")
    db.flashcard.delete_many()
    db.lesson.delete_many()

    print("Extracting dummy_lessons from lessons.py...")
    lessons = get_dummy_lessons()

    print(f"Found {len(lessons)} lessons. Seeding...")

    for l in lessons:
        lesson_id = str(l["id"])
        # Create Lesson
        lesson = db.lesson.create({
            "title": l["title"],
            "category": l["category"],
            "description": l.get("description", ""),
            "color": l.get("color", "#3B82F6")
        })

        # Insert existing flashcards
        for f in l.get("flashcards", []):
            db.flashcard.create({
                "question": f["question"],
                "answer": f["answer"],
                "lessonId": lesson.id
            })
            
        # For the very first lesson (e.g. id "1"), generate 500 more flashcards
        if lesson_id == "1":
            print(f"Generating 500 mock flashcards for {l['title']} to test scaling...")
            for i in range(1, 501):
                db.flashcard.create({
                    "question": f"Scale Test Question {i} - What is {i} + {i}?",
                    "answer": f"The answer is {i + i}. This tests pagination and chunking limits.",
                    "lessonId": lesson.id
                })

    print("Seeding complete! Database is now scaled.")
    db.disconnect()

if __name__ == "__main__":
    seed()
