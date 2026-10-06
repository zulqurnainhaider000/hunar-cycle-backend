from prisma import Prisma

def seed():
    db = Prisma()
    db.connect()

    print("Fetching Python lesson...")
    python_lesson = db.lesson.find_first(
        where={
            "title": {
                "contains": "Python"
            }
        }
    )

    if not python_lesson:
        print("Error: Python lesson not found!")
        db.disconnect()
        return

    print("Cleaning up old lesson steps for Python...")
    db.lessonstep.delete_many(where={"lessonId": python_lesson.id})

    steps = [
        {
            "order": 1,
            "title": "Welcome to Python!",
            "content": "Python is a high-level, interpreted programming language known for its readability and concise syntax. It was created by Guido van Rossum and first released in 1991.\n\nPython is incredibly versatile, powering everything from web applications and data analysis to artificial intelligence and machine learning.\n\nLet's get ready to write some beautiful code!",
            "codeSnippet": "print('Hello, World!')"
        },
        {
            "order": 2,
            "title": "Variables & Data Types",
            "content": "In Python, you don't need to explicitly declare a variable's type. Variables are created the moment you first assign a value to them.\n\n### Common Data Types:\n- **Integers**: Whole numbers (e.g., `5`, `-3`)\n- **Floats**: Decimal numbers (e.g., `3.14`, `-0.01`)\n- **Strings**: Text enclosed in single or double quotes (e.g., `'Python'`)\n- **Booleans**: `True` or `False`",
            "codeSnippet": "age = 25\nprice = 19.99\nname = 'Alice'\nis_active = True\n\nprint(type(age)) # <class 'int'>"
        },
        {
            "order": 3,
            "title": "Control Flow",
            "content": "Control flow allows your program to make decisions. Python uses `if`, `elif`, and `else` statements.\n\nNotice that Python relies on **indentation** (whitespace) to define the scope of blocks, rather than curly braces `{}` used in many other languages.",
            "codeSnippet": "temperature = 30\n\nif temperature > 25:\n    print('It is a hot day!')\nelif temperature > 15:\n    print('It is a pleasant day.')\nelse:\n    print('It is a cold day.')"
        },
        {
            "order": 4,
            "title": "Lists and Iteration",
            "content": "A list is an ordered, mutable collection of items. You can use a `for` loop to easily iterate over items in a list or characters in a string.\n\nThe `range()` function is also incredibly useful for generating a sequence of numbers.",
            "codeSnippet": "fruits = ['Apple', 'Banana', 'Cherry']\n\nfor fruit in fruits:\n    print(f'I love {fruit}!')\n\n# Using range\nfor i in range(3):\n    print(i) # Prints 0, 1, 2"
        },
        {
            "order": 5,
            "title": "Functions",
            "content": "Functions are reusable blocks of code. You define them using the `def` keyword, followed by the function name and parameters in parentheses.\n\nFunctions keep your code modular, readable, and prevent repetition (DRY principle).",
            "codeSnippet": "def greet(name):\n    return f'Hello, {name}! Welcome to Hunar Cycle.'\n\nmessage = greet('Student')\nprint(message)"
        },
        {
            "order": 6,
            "title": "Ready for Practice?",
            "content": "You've successfully covered the fundamental concepts of Python programming!\n\nNow it's time to put your knowledge to the test. Tap the **Start Quiz** button below to launch into a massive, non-repeating queue of interactive flashcards testing everything from syntax to logic.",
            "codeSnippet": ""
        }
    ]

    print(f"Seeding {len(steps)} steps...")
    
    for step in steps:
        db.lessonstep.create({
            "lessonId": python_lesson.id,
            "order": step["order"],
            "title": step["title"],
            "content": step["content"],
            "codeSnippet": step["codeSnippet"]
        })

    print("Finished seeding Lesson Steps!")
    db.disconnect()

if __name__ == "__main__":
    seed()
