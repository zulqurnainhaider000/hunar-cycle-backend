import asyncio
import math
from prisma import Prisma

def generate_flashcards():
    flashcards = []
    def add(q, a):
        flashcards.append({"question": q, "answer": str(a)})

    # Basics
    add("What is the difference between a dynamically typed and statically typed language?", "In a dynamically typed language like Python, variable types are checked during execution (runtime), whereas statically typed languages check types during compilation.")
    add("How do you declare a variable in Python?", "You just assign a value to a name using the `=` operator. E.g., `x = 5`. No type declaration is needed.")
    add("What does the `id()` function do?", "It returns the unique identity (memory address in CPython) of an object.")
    
    # Strings
    add("What is the output of `'python'.upper()`?", "`'PYTHON'`")
    add("What is the output of `'  strip me  '.strip()`?", "`'strip me'`")
    add("How do you check if a string starts with 'Py'?", "Using the method `startswith()`: `s.startswith('Py')`")
    
    # Control Flow & Loops
    add("What is the difference between `break` and `continue`?", "`break` exits the loop entirely. `continue` skips the rest of the current iteration and moves to the next.")
    add("What does the `pass` statement do?", "It is a null operation. It does nothing and is used as a placeholder where syntax requires a statement.")
    
    # Data Structures
    add("Are lists mutable or immutable?", "Mutable (they can be changed after creation).")
    add("Are tuples mutable or immutable?", "Immutable (they cannot be changed after creation).")
    add("How do you add an item to the end of a list?", "Using the `append()` method.")
    add("What is the output of `{1, 2, 2, 3}`?", "`{1, 2, 3}` (Sets automatically remove duplicates).")
    
    # Functions
    add("What is the keyword used to define a function?", "`def`")
    add("What are `*args` and `**kwargs`?", "`*args` allows a function to accept any number of positional arguments (as a tuple). `**kwargs` allows it to accept any number of keyword arguments (as a dictionary).")
    add("What is a lambda expression?", "An anonymous, single-line function defined using the `lambda` keyword. Example: `lambda x: x + 1`.")
    
    # OOP & Advanced
    add("What is the `__init__` method?", "It is the constructor method in Python. It is automatically called when a new object of the class is instantiated.")
    add("What does the `self` parameter represent?", "It represents the instance of the class itself, allowing access to its attributes and methods.")
    add("What is Inheritance?", "A mechanism where a new class (child) derives properties and methods from an existing class (parent).")
    add("What is a decorator?", "A function that takes another function and extends its behavior without explicitly modifying it. Denoted by `@decorator_name`.")
    add("What is a generator?", "A special type of function that returns an iterator, using the `yield` keyword instead of `return`.")

    unique_flashcards = []
    seen = set()
    for fc in flashcards:
        if fc["question"] not in seen:
            seen.add(fc["question"])
            unique_flashcards.append(fc)
            
    return unique_flashcards

def seed():
    db = Prisma()
    db.connect()

    print("Fetching Python lesson...")
    python_lesson = db.lesson.find_first(where={"title": {"contains": "Python"}})

    if not python_lesson:
        python_lesson = db.lesson.create({
            "title": "Python Programming Fundamentals",
            "category": "TECH",
            "description": "Master the basics and advanced concepts of Python programming.",
            "color": "#3B82F6"
        })

    print("Cleaning up old lesson steps and flashcards for Python...")
    db.flashcard.delete_many(where={"lessonId": python_lesson.id})
    db.lessonstep.delete_many(where={"lessonId": python_lesson.id})

    # The 30 Day Curriculum
    steps = [
        {"order": 1, "title": "Day 1: Introduction & Setup", "content": "Welcome to the 30-Day Python Mastery Course! Python is a high-level, interpreted language known for its readability. Today, we focus on setting up your environment (like installing Python and an IDE like VS Code) and writing your very first program.", "codeSnippet": "print('Hello, World!')"},
        {"order": 2, "title": "Day 2: Variables & Basic Types", "content": "Variables store data. Python has several built-in types: integers (whole numbers), floats (decimals), booleans (True/False), and strings (text). You don't need to declare types explicitly.", "codeSnippet": "name = 'Alice'\nage = 25\nheight = 5.6\nis_student = True\nprint(type(name)) # <class 'str'>"},
        {"order": 3, "title": "Day 3: Arithmetic Operators", "content": "Python supports standard arithmetic operations: addition (+), subtraction (-), multiplication (*), division (/), floor division (//), modulo (%), and exponentiation (**).", "codeSnippet": "x = 10\ny = 3\nprint(x // y)  # 3 (Floor division)\nprint(x % y)   # 1 (Remainder)\nprint(x ** y)  # 1000 (Exponent)"},
        {"order": 4, "title": "Day 4: String Methods", "content": "Strings are sequences of characters. They come with built-in methods to manipulate text easily, such as converting to uppercase, replacing substrings, or splitting text into a list.", "codeSnippet": "text = ' Python is Awesome '\nprint(text.strip())       # Removes whitespace\nprint(text.lower())       # ' python is awesome '\nprint(text.replace('o','0'))"},
        {"order": 5, "title": "Day 5: Lists Basics", "content": "A list is an ordered, mutable collection. You can add items, remove items, and access items via their index (starting at 0). Lists are created using square brackets [].", "codeSnippet": "fruits = ['apple', 'banana', 'cherry']\nfruits.append('orange')\nfruits[1] = 'blueberry'\nprint(fruits[-1]) # 'orange'"},
        {"order": 6, "title": "Day 6: Tuples and Sets", "content": "Tuples are like lists but immutable (cannot be changed), created with parentheses (). Sets are unordered collections of unique items, created with curly braces {}.", "codeSnippet": "coordinates = (10, 20) # Tuple\n\nmy_set = {1, 2, 2, 3}  # Set\nprint(my_set) # {1, 2, 3}"},
        {"order": 7, "title": "Day 7: Dictionaries", "content": "Dictionaries store data in key-value pairs. They are optimized for retrieving values when you know the key. Keys must be immutable types (like strings or numbers).", "codeSnippet": "user = {'name': 'Alice', 'age': 25}\nprint(user['name'])\n\nuser['city'] = 'New York' # Adding a key\nprint(user.keys())"},
        {"order": 8, "title": "Day 8: If/Elif/Else", "content": "Control flow allows your program to make decisions. Python uses `if`, `elif` (else if), and `else` statements. Indentation defines the scope of the blocks.", "codeSnippet": "score = 85\nif score >= 90:\n    print('A')\nelif score >= 80:\n    print('B')\nelse:\n    print('C')"},
        {"order": 9, "title": "Day 9: Logical & Comparison Operators", "content": "Comparison operators (==, !=, >, <) return booleans. Logical operators (`and`, `or`, `not`) combine multiple conditions together.", "codeSnippet": "age = 20\nhas_license = True\nif age >= 18 and has_license:\n    print('You can drive!')"},
        {"order": 10, "title": "Day 10: The For Loop", "content": "The `for` loop in Python iterates over the items of any sequence (a list, a string, a dictionary, etc.). The `range()` function generates sequences of numbers.", "codeSnippet": "for i in range(5):\n    print(i) # 0, 1, 2, 3, 4\n\nwords = ['cat', 'dog']\nfor w in words:\n    print(len(w))"},
        {"order": 11, "title": "Day 11: The While Loop", "content": "A `while` loop executes a block of code as long as its condition remains True. Be careful to ensure the condition eventually becomes False to avoid infinite loops.", "codeSnippet": "count = 3\nwhile count > 0:\n    print(count)\n    count -= 1\nprint('Blastoff!')"},
        {"order": 12, "title": "Day 12: Break, Continue, Pass", "content": "`break` exits the nearest enclosing loop. `continue` skips the rest of the loop block and goes to the next iteration. `pass` does nothing (a placeholder).", "codeSnippet": "for i in range(5):\n    if i == 2:\n        continue # Skip 2\n    if i == 4:\n        break    # Stop at 4\n    print(i) # Prints 0, 1, 3"},
        {"order": 13, "title": "Day 13: Functions Introduction", "content": "Functions are reusable blocks of code. Define them using the `def` keyword. Functions can accept arguments and return values using `return`.", "codeSnippet": "def greet(name, greeting='Hello'):\n    return f'{greeting}, {name}!'\n\nprint(greet('Alice'))\nprint(greet('Bob', 'Hi'))"},
        {"order": 14, "title": "Day 14: *args and **kwargs", "content": "Sometimes you don't know how many arguments will be passed to your function. `*args` allows you to pass a variable number of positional arguments. `**kwargs` allows variable keyword arguments.", "codeSnippet": "def order_pizza(size, *toppings, **details):\n    print(f'Size: {size}')\n    print(f'Toppings: {toppings}')\n    print(f'Details: {details}')\n\norder_pizza('Large', 'Pepperoni', 'Olives', delivery=True)"},
        {"order": 15, "title": "Day 15: Scope and Lambda Functions", "content": "Variables defined inside a function have local scope. Lambdas are small anonymous functions defined with the `lambda` keyword, often used for short, throwaway operations.", "codeSnippet": "x = 10 # Global\n\nadd_ten = lambda a: a + 10\nprint(add_ten(5)) # 15\n\npoints = [(1, 2), (3, 1), (5, 0)]\npoints.sort(key=lambda p: p[1]) # Sort by Y"},
        {"order": 16, "title": "Day 16: List Comprehensions", "content": "List comprehensions provide a concise way to create lists. They can replace multi-line for-loops and map/filter functions with a single readable line.", "codeSnippet": "squares = [x**2 for x in range(5)]\nprint(squares) # [0, 1, 4, 9, 16]\n\nevens = [x for x in range(10) if x % 2 == 0]"},
        {"order": 17, "title": "Day 17: Error Handling (Try/Except)", "content": "Use `try` and `except` blocks to handle errors gracefully rather than letting the program crash. You can also use `finally` to run cleanup code.", "codeSnippet": "try:\n    result = 10 / 0\nexcept ZeroDivisionError:\n    print('Cannot divide by zero!')\nfinally:\n    print('Execution finished.')"},
        {"order": 18, "title": "Day 18: File I/O", "content": "Python can read from and write to files. Using the `with` statement (a context manager) ensures that the file is properly closed after its suite finishes.", "codeSnippet": "with open('data.txt', 'w') as f:\n    f.write('Hello World')\n\nwith open('data.txt', 'r') as f:\n    content = f.read()\n    print(content)"},
        {"order": 19, "title": "Day 19: Classes and Objects (OOP)", "content": "Object-Oriented Programming models real-world entities. A Class is a blueprint, and an Object is an instance of a class. `__init__` initializes the object.", "codeSnippet": "class Dog:\n    def __init__(self, name):\n        self.name = name\n    def bark(self):\n        print(f'{self.name} says Woof!')\n\nd = Dog('Rex')\nd.bark()"},
        {"order": 20, "title": "Day 20: OOP - Inheritance", "content": "Inheritance allows a class (child) to inherit attributes and methods from another class (parent). This promotes code reuse.", "codeSnippet": "class Animal:\n    def speak(self):\n        pass\n\nclass Cat(Animal):\n    def speak(self):\n        return 'Meow'\n\nc = Cat()\nprint(c.speak())"},
        {"order": 21, "title": "Day 21: OOP - Magic Methods", "content": "Magic (Dunder) methods like `__str__`, `__len__`, or `__add__` allow you to define how your objects interact with built-in Python operators and functions.", "codeSnippet": "class Point:\n    def __init__(self, x, y):\n        self.x, self.y = x, y\n    def __str__(self):\n        return f'({self.x}, {self.y})'\n\np = Point(2, 3)\nprint(p) # (2, 3)"},
        {"order": 22, "title": "Day 22: Modules and Imports", "content": "Modules are files containing Python code. You can import modules to use their functions. The Standard Library comes with many useful modules like `math` and `datetime`.", "codeSnippet": "import math\nfrom datetime import datetime\n\nprint(math.sqrt(16)) # 4.0\nprint(datetime.now())"},
        {"order": 23, "title": "Day 23: Iterators & Generators", "content": "Generators are functions that return an iterator and use the `yield` keyword. They are incredibly memory efficient for processing large sequences of data.", "codeSnippet": "def count_up_to(max):\n    count = 1\n    while count <= max:\n        yield count\n        count += 1\n\nfor num in count_up_to(3):\n    print(num) # 1, 2, 3"},
        {"order": 24, "title": "Day 24: Decorators", "content": "Decorators modify the behavior of a function without changing its source code. They are widely used in frameworks like Flask or Django.", "codeSnippet": "def uppercase_decorator(func):\n    def wrapper():\n        result = func()\n        return result.upper()\n    return wrapper\n\n@uppercase_decorator\ndef say_hi():\n    return 'hi there'\n\nprint(say_hi()) # 'HI THERE'"},
        {"order": 25, "title": "Day 25: Regular Expressions", "content": "The `re` module allows you to use regular expressions to match, search, and replace patterns in text, like validating an email address.", "codeSnippet": "import re\ntext = 'Contact me at admin@example.com'\nmatch = re.search(r'[\\w.-]+@[\\w.-]+', text)\nif match:\n    print(match.group()) # admin@example.com"},
        {"order": 26, "title": "Day 26: Virtual Environments & pip", "content": "Virtual environments (`venv`) isolate your project's dependencies from other projects. `pip` is the package installer for Python, used to download third-party libraries.", "codeSnippet": "# Run in terminal:\n# python -m venv myenv\n# source myenv/bin/activate (Mac/Linux)\n# pip install requests"},
        {"order": 27, "title": "Day 27: Working with JSON & APIs", "content": "The `json` module parses JSON strings into dictionaries. External libraries like `requests` let you easily make HTTP requests to fetch data from web APIs.", "codeSnippet": "import json\n\njson_str = '{\"name\": \"Alice\", \"age\": 25}'\ndata = json.loads(json_str)\nprint(data['name']) # Alice"},
        {"order": 28, "title": "Day 28: Introduction to Web Scraping", "content": "Web scraping involves extracting data from websites. Libraries like BeautifulSoup parse HTML, allowing you to find elements by their tags or classes.", "codeSnippet": "# Conceptual example using bs4\n# from bs4 import BeautifulSoup\n# soup = BeautifulSoup('<h1>Title</h1>', 'html.parser')\n# print(soup.h1.text)"},
        {"order": 29, "title": "Day 29: Introduction to Databases", "content": "Python includes `sqlite3` natively, which allows you to interact with a lightweight SQL database directly from your code.", "codeSnippet": "import sqlite3\nconn = sqlite3.connect(':memory:')\ncursor = conn.cursor()\ncursor.execute('CREATE TABLE users (id INTEGER, name TEXT)')\nconn.commit()\nconn.close()"},
        {"order": 30, "title": "Day 30: The Journey Ahead", "content": "Congratulations! You have completed the 30-Day Python Mastery Course. You've learned everything from basic syntax to advanced OOP, decorators, and APIs. The next step is to build real-world projects!", "codeSnippet": "def mastery():\n    print('You are now a Pythonista!')\n    return True\n\nmastery()"}
    ]

    print(f"Seeding {len(steps)} steps...")
    
    created_steps = []
    for step in steps:
        s = db.lessonstep.create({
            "lessonId": python_lesson.id,
            "order": step["order"],
            "title": step["title"],
            "content": step["content"],
            "codeSnippet": step["codeSnippet"]
        })
        created_steps.append(s)

    print("Generating flashcards...")
    flashcards = generate_flashcards()
    
    # Divide flashcards among steps
    cards_per_step = math.ceil(len(flashcards) / len(created_steps))
    
    print(f"Inserting {len(flashcards)} flashcards into database... (~{cards_per_step} per day)")
    
    data_to_insert = []
    for idx, fc in enumerate(flashcards):
        step_idx = idx // cards_per_step
        if step_idx >= len(created_steps):
            step_idx = len(created_steps) - 1
        
        step_id = created_steps[step_idx].id
        
        data_to_insert.append({
            "question": fc["question"], 
            "answer": fc["answer"], 
            "lessonId": python_lesson.id,
            "lessonStepId": step_id
        })
        
    # Insert in batches
    batch_size = 50
    for i in range(0, len(data_to_insert), batch_size):
        batch = data_to_insert[i:i+batch_size]
        db.flashcard.create_many(data=batch)

    print("Finished seeding NEW 30-DAY Python curriculum with linked days!")
    db.disconnect()

if __name__ == "__main__":
    seed()
