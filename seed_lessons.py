from prisma import Prisma

def seed():
    db = Prisma()
    db.connect()

    print("Seeding Lessons...")
    
    # 1. Python Module
    python_lesson = db.lesson.create({
        "title": "Python: Strings & Lambdas",
        "category": "TECH",
        "description": "Master string manipulation and lambda functions in Python.",
        "color": "#3B82F6"
    })
    
    db.flashcard.create({
        "question": "How do you reverse a string `s` in Python?",
        "answer": "s[::-1]",
        "lessonId": python_lesson.id
    })
    db.flashcard.create({
        "question": "Write a lambda function to add 10 to a number x.",
        "answer": "lambda x: x + 10",
        "lessonId": python_lesson.id
    })

    # 2. Medical Billing Module
    med_lesson = db.lesson.create({
        "title": "Medical Billing Basics",
        "category": "MEDICAL",
        "description": "Learn the core structures of ICD-10 and CPT codes.",
        "color": "#EF4444"
    })

    db.flashcard.create({
        "question": "What does ICD-10 stand for?",
        "answer": "International Classification of Diseases, 10th Revision",
        "lessonId": med_lesson.id
    })
    db.flashcard.create({
        "question": "What is the primary use of CPT codes?",
        "answer": "To report medical, surgical, and diagnostic procedures and services.",
        "lessonId": med_lesson.id
    })

    # 3. German Language Module
    german_lesson = db.lesson.create({
        "title": "German 101",
        "category": "LANGUAGE",
        "description": "Essential vocabulary for beginners.",
        "color": "#F59E0B"
    })

    db.flashcard.create({
        "question": "Hello (formal)",
        "answer": "Guten Tag",
        "lessonId": german_lesson.id
    })
    db.flashcard.create({
        "question": "Thank you very much",
        "answer": "Vielen Dank",
        "lessonId": german_lesson.id
    })

    print("Seeding complete!")
    db.disconnect()

if __name__ == "__main__":
    seed()
