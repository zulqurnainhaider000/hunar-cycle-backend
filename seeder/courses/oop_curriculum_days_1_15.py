"""
Object-Oriented Programming (OOP) - 55-Day Curriculum - Part 1 (Days 1 to 15)
Module 1: OOP Foundation (Basics) (Days 1-7)
Module 2: Encapsulation & Data Hiding (Days 8-12)
Module 3: Inheritance (Code Reusability) (Days 13-15)
"""

from seeder.course_blueprint import DayBlueprint, QuizQuestionBlueprint, CodingChallengeBlueprint

DAYS_1_TO_15 = [
    # -------------------------------------------------------------
    # DAY 1: Intro to OOP (Procedural vs Object-Oriented)
    # -------------------------------------------------------------
    DayBlueprint(
        order=1,
        title="Day 1: Intro to OOP (Procedural vs Object-Oriented)",
        concept="Understanding programming paradigms: Procedural programming (functions and global state) versus Object-Oriented Programming (data and behavior bundled together)",
        analogy="Procedural programming is like a messy kitchen where raw ingredients (global variables) sit on a communal table, and various chefs (functions) wander by and modify them indiscriminately. If soup gets oversalted, nobody knows who touched it. Object-Oriented Programming is like a team of specialized bento-box chefs (Objects) who guard their own private ingredients inside sealed containers and only prepare dishes when you politely ask them via their menu (Methods).",
        theory_sections=[
            {
                "heading": "Procedural vs Object-Oriented Paradigm",
                "body": "In **Procedural Programming** (e.g., C, Pascal, or basic scripting), a program is structured around a sequential list of instructions and functions that operate on separate data structures. As codebases grow, shared global state becomes tangled, leading to spaghetti code and unintended side effects.\n\nIn **Object-Oriented Programming (OOP)**, software is modeled as a collection of interacting **Objects**. Each object bundles together its own private data (**state**) and the procedures that operate on that data (**behavior**). The four core pillars of OOP are **Encapsulation**, **Inheritance**, **Polymorphism**, and **Abstraction**."
            },
            {
                "heading": "Why Modern Software Relies on OOP",
                "body": "OOP mirrors the physical real world. In reality, you interact with nouns (a car, a bank account, an employee). Each noun has attributes (color, balance, job title) and things it can do (accelerate, deposit, compute paycheck). OOP provides:\n- **Modularity**: Self-contained objects can be debugged independently.\n- **Reusability**: Existing classes can be extended via inheritance without rewriting code.\n- **Maintainability**: Internal implementation changes inside a class do not break external consumers."
            }
        ],
        code_snippets=[
            {
                "title": "Procedural Approach (Decoupled Data and Functions)",
                "language": "python",
                "code": "# Procedural style: raw dictionary + separate loose functions\ncar_data = {'speed': 0, 'fuel': 50}\n\ndef accelerate(car, amount):\n    car['speed'] += amount\n    car['fuel'] -= amount * 0.1\n\ndef brake(car, amount):\n    car['speed'] = max(0, car['speed'] - amount)\n\naccelerate(car_data, 30)\nprint('Procedural Car:', car_data)",
                "explanation": "In procedural code, car data can be accidentally modified by any rogue function anywhere in the program."
            },
            {
                "title": "Object-Oriented Approach (Encapsulated State and Behavior)",
                "language": "python",
                "code": "class Car:\n    def __init__(self, fuel: float):\n        self.speed = 0.0\n        self.fuel = fuel\n\n    def accelerate(self, amount: float):\n        if self.fuel <= 0:\n            print('Out of fuel!')\n            return\n        self.speed += amount\n        self.fuel -= amount * 0.1\n\n    def brake(self, amount: float):\n        self.speed = max(0.0, self.speed - amount)\n\nmy_car = Car(fuel=50)\nmy_car.accelerate(30)\nprint(f'Speed: {my_car.speed} km/h, Fuel: {my_car.fuel} L')",
                "explanation": "In OOP, speed and fuel belong exclusively to the Car instance, and only Car methods can manipulate them safely."
            },
            {
                "title": "Multiple Autonomous Objects in OOP",
                "language": "python",
                "code": "# Each instance maintains its own distinct state in memory\nsedan = Car(fuel=40)\nsportscar = Car(fuel=80)\n\nsedan.accelerate(20)\nsportscar.accelerate(90)\nprint('Sedan speed:', sedan.speed)\nprint('Sportscar speed:', sportscar.speed)",
                "explanation": "Multiple objects instantiated from the same class operate completely independently without interfering with each other's state."
            },
            {
                "title": "Python Script: Type Checking Objects vs Primitives",
                "language": "python",
                "code": "car = Car(fuel=25)\nprint('Is my_car an instance of Car?', isinstance(car, Car))\nprint('Car class object type:', type(car))\nprint('Object attributes in memory:', car.__dict__)",
                "explanation": "Demonstrates introspection into Python's underlying object model and instance dictionary."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Procedural to OOP Refactoring",
            description="Refactor procedural counter logic into a class named `Counter`. The class should initialize with a starting value (default 0), provide an `increment()` method, a `decrement()` method (which never drops below 0), and a `get_value()` method.",
            starter_code="class Counter:\n    # Implement the Counter class\n    pass",
            solution_code="class Counter:\n    def __init__(self, initial_value: int = 0):\n        self.value = max(0, initial_value)\n\n    def increment(self):\n        self.value += 1\n\n    def decrement(self):\n        self.value = max(0, self.value - 1)\n\n    def get_value(self) -> int:\n        return self.value",
            expected_output="1\n0\n0"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the foundational difference between Procedural and Object-Oriented Programming?",
                options=[
                    "Procedural focuses on separate functions operating on data; OOP bundles data and behavior together inside cohesive objects",
                    "Procedural programming can only run on 16-bit CPUs, while OOP requires 64-bit CPUs",
                    "Procedural programming does not allow mathematical calculations",
                    "OOP does not allow functions or methods to be written"
                ],
                correct_answer="Procedural focuses on separate functions operating on data; OOP bundles data and behavior together inside cohesive objects",
                explanation="Procedural programming separates functions from data, whereas OOP encapsulates state (attributes) and behavior (methods) inside unified objects."
            ),
            QuizQuestionBlueprint(
                question="Which of the following represents the four primary pillars of Object-Oriented Programming?",
                options=[
                    "Encapsulation, Inheritance, Polymorphism, and Abstraction",
                    "Iteration, Compilation, Recursion, and Serialization",
                    "Input, Output, Memory, and Storage",
                    "Public, Private, Protected, and Default"
                ],
                correct_answer="Encapsulation, Inheritance, Polymorphism, and Abstraction",
                explanation="The four foundational principles of OOP are Encapsulation, Inheritance, Polymorphism, and Abstraction."
            ),
            QuizQuestionBlueprint(
                question="What is a major vulnerability of large procedural codebases compared to OOP?",
                options=[
                    "Uncontrolled shared global state leading to hard-to-trace bugs and side effects",
                    "Inability to print text to the console",
                    "Lack of support for integers and strings",
                    "Compilation time taking weeks for small scripts"
                ],
                correct_answer="Uncontrolled shared global state leading to hard-to-trace bugs and side effects",
                explanation="In procedural systems, global data structures can be mutated by any function, making state tracking difficult and error-prone as systems scale."
            ),
            QuizQuestionBlueprint(
                question="In OOP terminology, what do we call an individual, concrete realization of a class created in memory?",
                options=[
                    "An Object (or Instance)",
                    "A Variable pointer",
                    "A Static header",
                    "A Template file"
                ],
                correct_answer="An Object (or Instance)",
                explanation="An Object (or instance) is a concrete, in-memory entity created according to the specifications defined in a class."
            ),
            QuizQuestionBlueprint(
                question="How does OOP enhance software maintainability across large development teams?",
                options=[
                    "By modularizing software into self-contained objects whose internal code can change without breaking other parts of the application",
                    "By eliminating the need for code reviews and testing",
                    "By automatically converting Python code into machine hardware circuits",
                    "By limiting programs to a maximum of 100 lines"
                ],
                correct_answer="By modularizing software into self-contained objects whose internal code can change without breaking other parts of the application",
                explanation="Encapsulated objects expose clean public interfaces while hiding internal details, enabling safe refactoring without breaking callers."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 2: Classes and Objects (Blueprint vs Instance)
    # -------------------------------------------------------------
    DayBlueprint(
        order=2,
        title="Day 2: Classes and Objects (Blueprint vs Instance)",
        concept="The relationship between a Class and an Object: Classes as user-defined blueprints and Objects as concrete allocated instances in memory",
        analogy="A Class is like the architectural blueprint for a house drawn on paper by an architect: you cannot sleep inside a blueprint, and it takes up almost no space. An Object is the actual physical house built with bricks, mortar, and plumbing at 123 Elm Street. From one single blueprint, you can build 50 houses—each painted a different color and lived in by different families!",
        theory_sections=[
            {
                "heading": "Classes as Blueprints and Types",
                "body": "A **Class** is a user-defined prototype or blueprint from which objects are created. It defines a new data type that specifies what attributes every object of this type will have and what behaviors it can perform. A class definition resides in code memory but allocates no state storage for individual instances until instantiation.\n\nSyntactically in Python, a class is defined using the `class` keyword followed by the CamelCase class name."
            },
            {
                "heading": "Objects: Living Instances in Heap Memory",
                "body": "An **Object** is a concrete instance of a class. When you write `p = Person('Alice')`, the runtime allocates memory on the heap to store Alice's specific attributes. Each object possesses:\n- **Identity**: A unique memory address (retrievable via `id(obj)` in Python).\n- **State**: The specific values stored in its instance attributes.\n- **Behavior**: The methods defined by its class that manipulate its state."
            }
        ],
        code_snippets=[
            {
                "title": "Defining a Class and Creating Multiple Instances",
                "language": "python",
                "code": "class Book:\n    # Class blueprint\n    def __init__(self, title: str, author: str, pages: int):\n        self.title = title\n        self.author = author\n        self.pages = pages\n\n# Creating two distinct book objects\nbook1 = Book('1984', 'George Orwell', 328)\nbook2 = Book('Clean Code', 'Robert C. Martin', 464)\n\nprint(f'{book1.title} by {book1.author}')\nprint(f'{book2.title} by {book2.author}')",
                "explanation": "book1 and book2 are separate objects residing at different memory locations, both created from the Book blueprint."
            },
            {
                "title": "Inspecting Object Identity and Memory Addresses",
                "language": "python",
                "code": "# Objects have distinct memory addresses\nprint('Memory ID of book1:', hex(id(book1)))\nprint('Memory ID of book2:', hex(id(book2)))\nprint('Are they identical?', book1 is book2)",
                "explanation": "The 'is' operator checks if two references point to the exact same object in heap memory."
            },
            {
                "title": "Class vs Instance Namespace Introspection",
                "language": "python",
                "code": "# Inspecting instance attributes vs class attributes\nprint('book1 instance dictionary:', book1.__dict__)\nprint('Book class name:', Book.__name__)\nprint('Is book1 a Book?', isinstance(book1, Book))",
                "explanation": "Each object maintains its own __dict__ storing its unique instance variables."
            },
            {
                "title": "Adding Behavior to the Blueprint",
                "language": "python",
                "code": "class Book:\n    def __init__(self, title: str, pages: int):\n        self.title = title\n        self.pages = pages\n        self.current_page = 1\n\n    def read_pages(self, count: int):\n        self.current_page = min(self.pages, self.current_page + count)\n        return f'Now on page {self.current_page} of {self.pages}'\n\nb = Book('Design Patterns', 395)\nprint(b.read_pages(45))\nprint(b.read_pages(60))",
                "explanation": "Methods define the state transitions permitted on objects of the class."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Create a Smartphone Class and Objects",
            description="Create a class `Smartphone` with attributes `brand`, `model`, and `battery_level` (default 100). Add a method `use_app(app_name: str, battery_cost: int)` that reduces `battery_level` (minimum 0) and returns `f'Used {app_name}, battery now {battery_level}%'`. If battery is 0, return `'Battery depleted, please recharge.'`.",
            starter_code="class Smartphone:\n    # Implement Smartphone class\n    pass",
            solution_code="class Smartphone:\n    def __init__(self, brand: str, model: str, battery_level: int = 100):\n        self.brand = brand\n        self.model = model\n        self.battery_level = max(0, min(100, battery_level))\n\n    def use_app(self, app_name: str, battery_cost: int) -> str:\n        if self.battery_level <= 0:\n            return 'Battery depleted, please recharge.'\n        self.battery_level = max(0, self.battery_level - battery_cost)\n        return f'Used {app_name}, battery now {self.battery_level}%'",
            expected_output="Used Camera, battery now 80%\nBattery depleted, please recharge."
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the relationship between a Class and an Object?",
                options=[
                    "A Class is a conceptual blueprint or template; an Object is a concrete instance of that class allocated in memory",
                    "A Class is a running process; an Object is a text file on disk",
                    "A Class is used only for math, while Objects are used only for text",
                    "They are identical terms and can be used interchangeably without difference"
                ],
                correct_answer="A Class is a conceptual blueprint or template; an Object is a concrete instance of that class allocated in memory",
                explanation="A class defines the blueprint (structure and behavior), while an object is an instantiated entity in memory."
            ),
            QuizQuestionBlueprint(
                question="In Python, which built-in function returns the unique integer memory identity of an object?",
                options=[
                    "id()",
                    "memory()",
                    "pointer()",
                    "hash_code()"
                ],
                correct_answer="id()",
                explanation="The id() function returns the identity of an object, which corresponds to its memory address in CPython."
            ),
            QuizQuestionBlueprint(
                question="If you create three separate objects from the same `Car` class, how many copies of instance variables exist in memory?",
                options=[
                    "Three independent sets of instance variables, one set inside each object",
                    "Only one set shared across all three objects",
                    "Zero, instance variables are stored in the CPU cache only",
                    "Nine sets"
                ],
                correct_answer="Three independent sets of instance variables, one set inside each object",
                explanation="Each instantiated object maintains its own independent state in heap memory."
            ),
            QuizQuestionBlueprint(
                question="What does the expression `isinstance(my_obj, MyClass)` return?",
                options=[
                    "True if my_obj is an instance of MyClass (or a subclass of it), otherwise False",
                    "The byte size of my_obj in memory",
                    "The number of methods inside MyClass",
                    "A copy of my_obj"
                ],
                correct_answer="True if my_obj is an instance of MyClass (or a subclass of it), otherwise False",
                explanation="isinstance() checks whether an object was instantiated from a specific class or one of its subclasses."
            ),
            QuizQuestionBlueprint(
                question="Which naming convention is standard for class names in Python and most modern OOP languages?",
                options=[
                    "PascalCase (CamelCase, e.g., BankAccount, CustomerOrder)",
                    "snake_case (e.g., bank_account)",
                    "SCREAMING_SNAKE_CASE (e.g., BANK_ACCOUNT)",
                    "kebab-case (e.g., bank-account)"
                ],
                correct_answer="PascalCase (CamelCase, e.g., BankAccount, CustomerOrder)",
                explanation="PEP 8 and industry standard conventions dictate PascalCase (UpperCamelCase) for class identifiers."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 3: Attributes (State) and Methods (Behavior)
    # -------------------------------------------------------------
    DayBlueprint(
        order=3,
        title="Day 3: Attributes (State) and Methods (Behavior)",
        concept="The dual anatomy of an Object: Instance Attributes defining state and Instance Methods defining behavior",
        analogy="Think of a superhero like Iron Man: his **Attributes (State)** are his current suit power percentage (85%), flight altitude (2,500 meters), and weapon ammunition count (12 rockets). His **Methods (Behavior)** are the actions he can take: `fly()`, `fire_repulsors()`, or `recharge_arc_reactor()`. Notice that every method changes or depends on his state: you cannot fire repulsors if suit power is 0%!",
        theory_sections=[
            {
                "heading": "Attributes: Capturing Object State",
                "body": "Attributes (also called fields or properties) represent the data or state preserved inside an object. In Python, **Instance Attributes** are bound to a specific instance (usually initialized inside `__init__` with `self.attribute_name = value`).\n\nEach object has its own distinct copy of instance attributes. For example, two `User` objects can have different `email` and `is_logged_in` attributes."
            },
            {
                "heading": "Methods: Defining Object Behavior",
                "body": "Methods are functions defined inside a class that operate on the data belonging to an instance of that class. Methods define the valid operations that can be performed on the object, enforcing business rules and preventing data corruption.\n\nA method's first parameter is always the reference to the current instance (`self`), allowing it to inspect and modify instance attributes directly."
            }
        ],
        code_snippets=[
            {
                "title": "Defining State and Behavior in a BankAccount Class",
                "language": "python",
                "code": "class BankAccount:\n    def __init__(self, owner: str, initial_balance: float = 0.0):\n        # State (Attributes)\n        self.owner = owner\n        self.balance = initial_balance\n\n    # Behavior (Methods)\n    def deposit(self, amount: float):\n        if amount > 0:\n            self.balance += amount\n            return f'Deposited ${amount:.2f}. New Balance: ${self.balance:.2f}'\n        return 'Deposit amount must be positive.'\n\n    def withdraw(self, amount: float):\n        if amount <= 0:\n            return 'Invalid withdrawal amount.'\n        if amount > self.balance:\n            return 'Insufficient funds!'\n        self.balance -= amount\n        return f'Withdrew ${amount:.2f}. Remaining Balance: ${self.balance:.2f}'",
                "explanation": "Methods validate arguments and manipulate the internal state (self.balance) safely."
            },
            {
                "title": "Interacting with Instance State through Methods",
                "language": "python",
                "code": "account = BankAccount('Alice', 100.0)\nprint(account.deposit(50.0))\nprint(account.withdraw(30.0))\nprint(account.withdraw(200.0))  # Should reject due to insufficient funds",
                "explanation": "External callers invoke methods rather than modifying the balance directly."
            },
            {
                "title": "Helper Methods (Internal Behavior)",
                "language": "python",
                "code": "class Thermostat:\n    def __init__(self, target_celsius: float):\n        self.target_celsius = target_celsius\n\n    # Method converting internal state to Fahrenheit\n    def get_target_fahrenheit(self) -> float:\n        return (self.target_celsius * 9/5) + 32\n\nt = Thermostat(20.0)\nprint('Celsius:', t.target_celsius)\nprint('Fahrenheit:', t.get_target_fahrenheit())",
                "explanation": "Methods can compute and return derived views of internal state."
            },
            {
                "title": "Python Script: Dynamically Inspecting Object Methods",
                "language": "python",
                "code": "account = BankAccount('Bob', 50)\n# List all callable methods on the object\nmethods = [m for m in dir(account) if callable(getattr(account, m)) and not m.startswith('__')]\nprint('Available methods on BankAccount:', methods)",
                "explanation": "Uses dir() and callable() introspection to discover the interface exposed by an object."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Build a VideoPlayer Class",
            description="Create a `VideoPlayer` class with attributes `title`, `duration_seconds`, `current_time` (starts at 0), and `is_playing` (starts at False). Implement methods:\n- `play()`: sets `is_playing = True` and returns `'Playing'`. If already playing, returns `'Already playing'`.\n- `pause()`: sets `is_playing = False` and returns `'Paused'`. If not playing, returns `'Already paused'`.\n- `seek(seconds: int)`: updates `current_time` clamped between 0 and `duration_seconds`.",
            starter_code="class VideoPlayer:\n    # Implement VideoPlayer class\n    pass",
            solution_code="class VideoPlayer:\n    def __init__(self, title: str, duration_seconds: int):\n        self.title = title\n        self.duration_seconds = duration_seconds\n        self.current_time = 0\n        self.is_playing = False\n\n    def play(self) -> str:\n        if self.is_playing:\n            return 'Already playing'\n        self.is_playing = True\n        return 'Playing'\n\n    def pause(self) -> str:\n        if not self.is_playing:\n            return 'Already paused'\n        self.is_playing = False\n        return 'Paused'\n\n    def seek(self, seconds: int):\n        self.current_time = max(0, min(self.duration_seconds, seconds))",
            expected_output="Playing\nAlready playing\nPaused"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="In Object-Oriented terminology, what is the key distinction between an Attribute and a Method?",
                options=[
                    "An attribute stores the data/state of an object, while a method defines the behavior/actions an object can execute",
                    "An attribute is a loop, while a method is a conditional statement",
                    "Attributes can only store numbers, while methods can only store text",
                    "There is no distinction; they are synonyms"
                ],
                correct_answer="An attribute stores the data/state of an object, while a method defines the behavior/actions an object can execute",
                explanation="Attributes define what an object *is* or *has* (state), while methods define what an object *does* (behavior)."
            ),
            QuizQuestionBlueprint(
                question="Why is it considered bad practice to let external code modify instance attributes directly without methods?",
                options=[
                    "Because direct modification bypasses validation rules and business invariants, potentially leaving the object in an invalid state",
                    "Because direct modification causes the hard drive to crash",
                    "Because Python prohibits accessing attributes with dot notation",
                    "Because attributes cannot be read outside of the class file"
                ],
                correct_answer="Because direct modification bypasses validation rules and business invariants, potentially leaving the object in an invalid state",
                explanation="Methods act as gatekeepers to ensure data integrity and prevent illegal values (like negative balances or corrupted pointers)."
            ),
            QuizQuestionBlueprint(
                question="What is the first parameter that every instance method in a Python class must accept by convention?",
                options=[
                    "self",
                    "this",
                    "cls",
                    "instance"
                ],
                correct_answer="self",
                explanation="In Python, 'self' is the mandatory first parameter passed to instance methods representing the calling instance."
            ),
            QuizQuestionBlueprint(
                question="Where are instance attributes typically created and initialized in a Python class?",
                options=[
                    "Inside the `__init__` constructor method",
                    "Inside a global config file",
                    "In the terminal command line",
                    "Inside the import statements"
                ],
                correct_answer="Inside the `__init__` constructor method",
                explanation="The `__init__` initializer method is the standard location where instance attributes are assigned to `self`."
            ),
            QuizQuestionBlueprint(
                question="If two objects `player1` and `player2` are instantiated from class `Player`, what happens if `player1.score += 10` is executed?",
                options=[
                    "Only `player1`'s score increases by 10; `player2`'s score remains untouched",
                    "Both players have their score increased by 10",
                    "A syntax error is thrown",
                    "`player2`'s score is reset to 0"
                ],
                correct_answer="Only `player1`'s score increases by 10; `player2`'s score remains untouched",
                explanation="Instance attributes are isolated per object; mutating one instance's state has no impact on other instances."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 4: The `this` or `self` Keyword
    # -------------------------------------------------------------
    DayBlueprint(
        order=4,
        title="Day 4: The `this` or `self` Keyword",
        concept="Understanding the self-referential pointer: `self` in Python and `this` in C++/Java/JavaScript",
        analogy="Imagine an army drill sergeant shouting to a platoon of 100 soldiers: 'Point your gun at **yourself**!' Every single soldier points at their own chest, not their neighbor's. In programming, when a method runs, it needs to know: 'Whose bank balance am I deducting? Alice's or Bob's?' The `self` (or `this`) keyword is the object pointing directly to its own chest: 'Me! Modify *my* balance, not someone else's!'",
        theory_sections=[
            {
                "heading": "Why Do Methods Need `self` or `this`?",
                "body": "When a class is compiled or defined, methods are stored once in shared memory for efficiency. When you call `alice.deposit(50)` and `bob.deposit(50)`, the exact same function body executes.\n\nTo know which object's attributes to manipulate, the runtime passes a reference to the active object into the method. In languages like C++, Java, and JavaScript, this reference is implicitly injected as the keyword `this`. In Python, it is made explicit and passed as the first parameter named `self` by convention."
            },
            {
                "heading": "Python's Syntactic Sugar: Bound Methods vs Functions",
                "body": "When you execute `obj.method(arg)`, Python internally translates this into `Class.method(obj, arg)`.\n\nFor example:\n`my_car.accelerate(20)` is strictly identical to `Car.accelerate(my_car, 20)`.\n\nThis reveals that `self` is not a magic language keyword in Python, but rather a normal parameter bound by Python's descriptor protocol."
            }
        ],
        code_snippets=[
            {
                "title": "Explicit Demonstration of Python's Syntactic Sugar",
                "language": "python",
                "code": "class Dog:\n    def __init__(self, name: str):\n        self.name = name\n\n    def bark(self):\n        return f'{self.name} says Woof!'\n\nd = Dog('Rex')\n# Standard instance invocation:\nprint(d.bark())\n\n# Equivalent explicit class invocation passing instance as self:\nprint(Dog.bark(d))",
                "explanation": "d.bark() automatically translates to Dog.bark(d) under the hood."
            },
            {
                "title": "Disambiguating Shadowed Parameter Names with self",
                "language": "python",
                "code": "class Rectangle:\n    def __init__(self, width: float, height: float):\n        # Parameter 'width' shadows attribute name; 'self.width' disambiguates\n        self.width = width\n        self.height = height\n\n    def area(self) -> float:\n        return self.width * self.height\n\nr = Rectangle(5, 10)\nprint('Area:', r.area())",
                "explanation": "self.width clearly tells the interpreter we are assigning to the instance attribute, not local variable."
            },
            {
                "title": "Chaining Methods by Returning self",
                "language": "python",
                "code": "class QueryBuilder:\n    def __init__(self):\n        self.query = ''\n\n    def select(self, fields: str):\n        self.query += f'SELECT {fields} '\n        return self  # Return current instance to allow chaining\n\n    def from_table(self, table: str):\n        self.query += f'FROM {table} '\n        return self\n\n    def build(self) -> str:\n        return self.query.strip()\n\nq = QueryBuilder().select('id, name').from_table('users').build()\nprint('Generated Query:', q)",
                "explanation": "Returning self enables fluent API method chaining, widely used in modern libraries."
            },
            {
                "title": "Comparison with C++/Java `this` Keyword Concept",
                "language": "python",
                "code": "# In Java / C++:\n# public void setName(String name) {\n#     this.name = name; // 'this' points to current object\n# }\n#\n# In Python:\n# def set_name(self, name):\n#     self.name = name\nprint('Concept is universal: self in Python == this in Java/C++')",
                "explanation": "Demonstrates cross-language parity between Python's self and C++/Java's this."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Fluent Calculator with Method Chaining",
            description="Create a `Calculator` class initialized with a value (default 0.0). Implement methods `add(n)`, `subtract(n)`, `multiply(n)`, and `divide(n)`. Each method must perform the arithmetic on the internal value and **return `self`** so operations can be chained. Add a `get_result()` method returning the final float.",
            starter_code="class Calculator:\n    # Implement fluent Calculator returning self\n    pass",
            solution_code="class Calculator:\n    def __init__(self, value: float = 0.0):\n        self.value = float(value)\n\n    def add(self, n: float):\n        self.value += n\n        return self\n\n    def subtract(self, n: float):\n        self.value -= n\n        return self\n\n    def multiply(self, n: float):\n        self.value *= n\n        return self\n\n    def divide(self, n: float):\n        if n != 0:\n            self.value /= n\n        return self\n\n    def get_result(self) -> float:\n        return self.value",
            expected_output="14.0\n10.0"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the purpose of the `self` parameter in Python methods?",
                options=[
                    "It references the specific instance of the class upon which the method is currently operating",
                    "It imports the Python standard library",
                    "It declares the method as private and hidden",
                    "It forces the method to run in a background worker thread"
                ],
                correct_answer="It references the specific instance of the class upon which the method is currently operating",
                explanation="'self' is the reference to the active instance, allowing access to its specific attributes and other methods."
            ),
            QuizQuestionBlueprint(
                question="What is the Java, C++, and JavaScript equivalent of Python's `self` keyword?",
                options=[
                    "this",
                    "self",
                    "current",
                    "instance"
                ],
                correct_answer="this",
                explanation="C++, Java, and JavaScript use the implicit 'this' keyword to refer to the current object instance."
            ),
            QuizQuestionBlueprint(
                question="If you call `car.drive(60)` in Python, what does the interpreter translate this expression to behind the scenes?",
                options=[
                    "Car.drive(car, 60)",
                    "drive(car, 60)",
                    "Car.drive(60, self)",
                    "car(60).drive()"
                ],
                correct_answer="Car.drive(car, 60)",
                explanation="Instance method calls are syntactic sugar for passing the instance as the first argument to the class function."
            ),
            QuizQuestionBlueprint(
                question="How does returning `self` from an instance method enable 'Method Chaining' (Fluent Interface)?",
                options=[
                    "Because each method returns the object itself, allowing immediate invocation of another method on the result (e.g. obj.a().b().c())",
                    "Because it triggers a reboot of the Python virtual machine",
                    "Because it converts the object into a linked list",
                    "Because it deletes all local variables"
                ],
                correct_answer="Because each method returns the object itself, allowing immediate invocation of another method on the result (e.g. obj.a().b().c())",
                explanation="Returning self hands back the active instance so subsequent method calls can be chained sequentially."
            ),
            QuizQuestionBlueprint(
                question="What happens if you define an instance method in a Python class but omit the `self` parameter in its definition?",
                options=[
                    "Calling the method via an instance will raise a TypeError stating that unexpected positional arguments were given",
                    "The program compiles and runs normally without issue",
                    "The method automatically becomes a global function",
                    "The class deletes itself from memory"
                ],
                correct_answer="Calling the method via an instance will raise a TypeError stating that unexpected positional arguments were given",
                explanation="Python automatically passes the instance as the 1st argument; if the function has no parameters to receive it, a TypeError is raised."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 5: Constructors (Default, Parameterized, Copy)
    # -------------------------------------------------------------
    DayBlueprint(
        order=5,
        title="Day 5: Constructors (Default, Parameterized, Copy)",
        concept="Object Initialization: Default constructors, parameterized constructors, copy constructors, and the lifecycle of object creation",
        analogy="Think of a constructor like the birth certificate and baby starter-kit handed out at a hospital. When a baby is born, the hospital guarantees that baby has a name, blood type, and birthdate assigned before they leave the maternity ward. You would never want an uninitialized baby with no name or records floating around in the system! A Constructor ensures an object never enters the program in a broken, half-formed, or uninitialized state.",
        theory_sections=[
            {
                "heading": "The Role of Constructors in Object Lifecycle",
                "body": "A **Constructor** is a special method called automatically whenever a new object is created. Its primary duty is to allocate and initialize the object's instance variables into a valid initial state.\n\nIn C++ and Java, constructors share the exact name of the class (e.g., `Car()`). In Python, the constructor workflow involves `__new__` (which allocates memory) followed by `__init__` (which initializes the instance attributes)."
            },
            {
                "heading": "Types of Constructors Across Languages",
                "body": "1. **Default Constructor**: Takes no arguments and initializes attributes to default values.\n2. **Parameterized Constructor**: Accepts arguments to initialize attributes with specific custom data.\n3. **Copy Constructor**: Initializes a new object by copying the attributes of an existing object of the same class (common in C++ to control deep vs shallow cloning).\n\nIn Python, default parameter values (e.g., `def __init__(self, name='Unknown'):`) allow a single `__init__` method to serve as both a default and parameterized constructor."
            }
        ],
        code_snippets=[
            {
                "title": "Parameterized Constructor with Default Fallbacks in Python",
                "language": "python",
                "code": "class Point:\n    # Serves as both default (Point()) and parameterized (Point(x, y))\n    def __init__(self, x: float = 0.0, y: float = 0.0):\n        self.x = x\n        self.y = y\n\n    def __repr__(self):\n        return f'Point({self.x}, {self.y})'\n\np_origin = Point()           # Default values used (0.0, 0.0)\np_custom = Point(3.5, 7.2)   # Parameterized values used\nprint('Default:', p_origin)\nprint('Custom:', p_custom)",
                "explanation": "Default parameter values in Python elegantly consolidate default and parameterized constructors."
            },
            {
                "title": "Implementing a Copy Constructor in Python",
                "language": "python",
                "code": "class Point:\n    def __init__(self, x: float = 0.0, y: float = 0.0):\n        self.x = x\n        self.y = y\n\n    @classmethod\n    def from_point(cls, other: 'Point') -> 'Point':\n        # Copy constructor pattern: creates a distinct duplicate\n        return cls(other.x, other.y)\n\np1 = Point(10, 20)\np2 = Point.from_point(p1)  # Clone p1 into p2\nprint('Are p1 and p2 identical?', p1 is p2)  # False, distinct objects\nprint('p2 values:', p2.x, p2.y)",
                "explanation": "Classmethods in Python are widely used to implement alternative constructors, including copy constructors."
            },
            {
                "title": "Constructor Validation and Guard Clauses",
                "language": "python",
                "code": "class Person:\n    def __init__(self, name: str, age: int):\n        # Validate before assigning state\n        if not name or len(name.strip()) == 0:\n            raise ValueError('Name cannot be empty.')\n        if age < 0 or age > 150:\n            raise ValueError(f'Invalid age: {age}')\n        self.name = name.strip()\n        self.age = age\n\nvalid_person = Person('Alice', 25)\nprint('Created:', valid_person.name)",
                "explanation": "Constructors should fail fast if arguments violate domain invariants."
            },
            {
                "title": "C++ Constructor Styles (Conceptual Comparison)",
                "language": "text",
                "code": "// C++ Constructor Variety:\n// class Rectangle {\n// public:\n//     Rectangle();                  // Default Constructor\n//     Rectangle(int w, int h);       // Parameterized Constructor\n//     Rectangle(const Rectangle &r); // Copy Constructor\n// };",
                "explanation": "Contrasts how compiled languages like C++ use function overloading for distinct constructor signatures."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Flexible Configuration Profile Constructor",
            description="Create a `UserProfile` class whose constructor accepts `username: str`, `email: str`, and optional `theme: str` (default 'light') and `notifications_enabled: bool` (default True). Add an alternative constructor classmethod `from_dict(cls, data: dict)` that parses a dictionary to instantiate a `UserProfile`.",
            starter_code="class UserProfile:\n    # Implement UserProfile with standard and alternative constructors\n    pass",
            solution_code="class UserProfile:\n    def __init__(self, username: str, email: str, theme: str = 'light', notifications_enabled: bool = True):\n        self.username = username\n        self.email = email\n        self.theme = theme\n        self.notifications_enabled = notifications_enabled\n\n    @classmethod\n    def from_dict(cls, data: dict) -> 'UserProfile':\n        return cls(\n            username=data.get('username', 'anonymous'),\n            email=data.get('email', 'no-reply@example.com'),\n            theme=data.get('theme', 'light'),\n            notifications_enabled=data.get('notifications_enabled', True)\n        )",
            expected_output="alice_99\nalice@test.com\ndark"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the primary responsibility of a Constructor in Object-Oriented Programming?",
                options=[
                    "To initialize the newly created object's instance variables into a valid starting state",
                    "To delete the object from memory when finished",
                    "To compile source code into machine bytecode",
                    "To create a graphical user interface window"
                ],
                correct_answer="To initialize the newly created object's instance variables into a valid starting state",
                explanation="Constructors ensure that objects are born in a fully valid, initialized state before any methods are called on them."
            ),
            QuizQuestionBlueprint(
                question="In Python, which magic method serves as the instance initializer (constructor body)?",
                options=[
                    "__init__",
                    "__construct__",
                    "__new__",
                    "__create__"
                ],
                correct_answer="__init__",
                explanation="In Python, `__init__` is the initializer method automatically invoked after memory allocation to set up instance attributes."
            ),
            QuizQuestionBlueprint(
                question="What is a 'Copy Constructor'?",
                options=[
                    "A constructor that creates a new object by copying the state of an existing object of the same class",
                    "A constructor that prints multiple copies of source code to paper",
                    "A constructor that can only be used once in an entire program",
                    "A constructor that copies files from one folder to another on disk"
                ],
                correct_answer="A constructor that creates a new object by copying the state of an existing object of the same class",
                explanation="A copy constructor duplicates the member variables of an existing object to produce an identical new instance."
            ),
            QuizQuestionBlueprint(
                question="How does Python support multiple constructor signatures (like having both a default and parameterized constructor) in a single class?",
                options=[
                    "By using default parameter values in `__init__` and defining alternative constructors via `@classmethod`",
                    "By writing multiple `def __init__` blocks with different parameter counts in the same class",
                    "Python does not support parameterized constructors",
                    "By renaming the class for each constructor"
                ],
                correct_answer="By using default parameter values in `__init__` and defining alternative constructors via `@classmethod`",
                explanation="Because Python does not support compile-time method overloading, default arguments and `@classmethod` factory methods provide constructor flexibility."
            ),
            QuizQuestionBlueprint(
                question="What happens if validation logic inside a constructor raises an exception (e.g. `raise ValueError`)?",
                options=[
                    "Object creation fails, preventing a broken or invalid object from ever existing in memory",
                    "The object is created anyway with corrupted data",
                    "The operating system reboots",
                    "The exception is silently ignored"
                ],
                correct_answer="Object creation fails, preventing a broken or invalid object from ever existing in memory",
                explanation="Failing fast in the constructor aborts object creation and ensures broken instances never enter the system."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 6: Destructors and Garbage Collection (Memory cleanup)
    # -------------------------------------------------------------
    DayBlueprint(
        order=6,
        title="Day 6: Destructors and Garbage Collection (Memory Cleanup)",
        concept="Object Destruction and Resource Cleanup: Destructors (`__del__`), Reference Counting, Garbage Collection, and the Context Manager (`with`) pattern",
        analogy="Creating an object is like checking out books from a public library. A Constructor is the librarian stamping your card and handing you the books. When you are done reading, you cannot just abandon the books on a park bench! A Destructor is the return desk that puts the books back on the shelf. In languages like C++, you must return the books by hand (`delete`). In Python and Java, an invisible cleaning robot (**Garbage Collector**) patrols behind you, noticing when you are no longer holding any books and returning them to the shelf automatically!",
        theory_sections=[
            {
                "heading": "Manual Memory Management vs Automated Garbage Collection",
                "body": "In low-level languages like C and C++, developers must manually manage memory: every `new` must have a matching `delete`. Forgetting to delete causes **Memory Leaks**, while deleting too early causes **Dangling Pointers**.\n\nModern languages like Python, Java, C#, and Go utilize **Automatic Garbage Collection (GC)**. Python combines two memory management algorithms:\n1. **Reference Counting**: Every object tracks how many references point to it. The moment reference count drops to 0, its memory is deallocated immediately.\n2. **Cyclic Garbage Collector**: Periodically scans for circular reference islands (where Object A points to Object B, and B points to A, but neither is reachable from root code) and frees them."
            },
            {
                "heading": "Destructors (`__del__`) vs Context Managers (`with`)",
                "body": "Python provides `__del__` as a destructor method, invoked when an object is about to be reclaimed. However, relying on `__del__` for critical resources (like closing network sockets or database transactions) is risky because the exact timing of garbage collection is non-deterministic.\n\nThe industry standard in Python is the **Context Manager** pattern (`with` statement using `__enter__` and `__exit__`), guaranteeing that cleanup happens deterministically the instant a code block finishes."
            }
        ],
        code_snippets=[
            {
                "title": "Observing Object Destruction with __del__ and Reference Counting",
                "language": "python",
                "code": "import sys\n\nclass Resource:\n    def __init__(self, name: str):\n        self.name = name\n        print(f'Resource [{self.name}] acquired.')\n\n    def __del__(self):\n        print(f'Resource [{self.name}] destroyed and cleaned up.')\n\n# Instantiate resource\nr = Resource('DatabaseConnection')\nprint('Reference count:', sys.getrefcount(r) - 1)  # Account for getrefcount temporary ref\n\n# Deleting reference drops count to 0\ndel r\nprint('End of script execution.')",
                "explanation": "When 'del r' reduces the reference count to zero, Python triggers __del__ immediately."
            },
            {
                "title": "Circular References and the Python Garbage Collector",
                "language": "python",
                "code": "import gc\n\nclass Node:\n    def __init__(self, val):\n        self.val = val\n        self.next = None\n\n# Create circular reference: a -> b -> a\na = Node('A')\nb = Node('B')\na.next = b\nb.next = a\n\n# Clear external variables\ndel a\ndel b\n\n# Cyclic GC detects the orphan island and cleans it up\nunreachable_cleaned = gc.collect()\nprint('Garbage Collector freed cycles:', unreachable_cleaned)",
                "explanation": "The cyclic garbage collector runs periodically to detect and free self-referencing islands."
            },
            {
                "title": "Deterministic Cleanup with Context Managers (__enter__ and __exit__)",
                "language": "python",
                "code": "class TempFileManager:\n    def __init__(self, filename: str):\n        self.filename = filename\n\n    def __enter__(self):\n        print(f'Opening file: {self.filename}')\n        return self\n\n    def __exit__(self, exc_type, exc_val, exc_tb):\n        print(f'Closing file: {self.filename} (Guaranteed Cleanup)')\n        return False  # Do not suppress exceptions\n\n# Deterministic cleanup happens immediately when exiting 'with' block\nwith TempFileManager('temp_data.csv') as tf:\n    print('Writing temporary records...')\nprint('Outside with block!')",
                "explanation": "Context managers guarantee cleanup happens even if unhandled exceptions occur."
            },
            {
                "title": "Comparison with C++ RAII Destructors",
                "language": "text",
                "code": "// In C++ (Resource Acquisition Is Initialization - RAII):\n// class FileHandle {\n// public:\n//     FileHandle() { open(); }\n//     ~FileHandle() { close(); } // Destructor guaranteed on stack exit\n// };",
                "explanation": "Contrasts Python's context manager with C++'s deterministic stack-unwinding destructors."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Building a Safe Session Manager Context Manager",
            description="Create a `DatabaseSession` class that tracks `is_active: bool`. When entered via `with`, it sets `is_active = True` and returns itself. When exited, it sets `is_active = False` and logs `'Session closed'`. Implement a method `query(sql: str)` that returns `f'Executed: {sql}'` if active, or raises `RuntimeError('Session inactive')` if closed.",
            starter_code="class DatabaseSession:\n    # Implement context manager for DatabaseSession\n    pass",
            solution_code="class DatabaseSession:\n    def __init__(self):\n        self.is_active = False\n\n    def __enter__(self):\n        self.is_active = True\n        return self\n\n    def __exit__(self, exc_type, exc_val, exc_tb):\n        self.is_active = False\n        print('Session closed')\n        return False\n\n    def query(self, sql: str) -> str:\n        if not self.is_active:\n            raise RuntimeError('Session inactive')\n        return f'Executed: {sql}'",
            expected_output="Executed: SELECT * FROM users\nSession closed"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the primary memory management mechanism used in Python to trigger immediate object deallocation?",
                options=[
                    "Reference Counting",
                    "Manual malloc and free pointers",
                    "Rebooting the CPU after every loop",
                    "Compiling all code to static assembly"
                ],
                correct_answer="Reference Counting",
                explanation="Python's primary memory management system is Reference Counting; when an object's reference counter hits 0, it is deallocated."
            ),
            QuizQuestionBlueprint(
                question="What is a 'Circular Reference' problem in garbage collection?",
                options=[
                    "When two or more objects hold references to each other, preventing their reference counts from ever reaching zero even when unreachable from the rest of the program",
                    "When an infinite loop runs inside a constructor",
                    "When a class inherits from itself",
                    "When a variable name is written in a circle on a whiteboard"
                ],
                correct_answer="When two or more objects hold references to each other, preventing their reference counts from ever reaching zero even when unreachable from the rest of the program",
                explanation="Circular reference islands maintain non-zero reference counts internally, requiring Python's cyclic garbage collector to detect and free them."
            ),
            QuizQuestionBlueprint(
                question="Why is relying on `__del__` discouraged for managing critical external resources like database locks or open file descriptors in Python?",
                options=[
                    "Because garbage collection timing is non-deterministic, so resources may remain locked indefinitely until the collector runs",
                    "Because `__del__` can only be called on Tuesdays",
                    "Because `__del__` deletes the Python interpreter executable",
                    "Because `__del__` requires root admin permissions to execute"
                ],
                correct_answer="Because garbage collection timing is non-deterministic, so resources may remain locked indefinitely until the collector runs",
                explanation="The timing of `__del__` invocation is unpredictable; context managers (`with`) provide deterministic, guaranteed cleanup."
            ),
            QuizQuestionBlueprint(
                question="Which Python statement and protocol guarantees that resources are cleaned up immediately upon exiting a code block?",
                options=[
                    "The `with` statement implementing `__enter__` and `__exit__` context managers",
                    "The `for` loop statement",
                    "The `global` keyword",
                    "The `assert` statement"
                ],
                correct_answer="The `with` statement implementing `__enter__` and `__exit__` context managers",
                explanation="Context managers (`__enter__` and `__exit__`) ensure deterministic resource management regardless of errors."
            ),
            QuizQuestionBlueprint(
                question="What function in Python's standard `gc` module forces an immediate sweep to collect and clean cyclic garbage?",
                options=[
                    "gc.collect()",
                    "gc.delete_all()",
                    "gc.clean_now()",
                    "gc.sweep_memory()"
                ],
                correct_answer="gc.collect()",
                explanation="`gc.collect()` explicitly invokes a full garbage collection cycle to identify and reclaim unreachable cyclic objects."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 7 (Project): Basic Student Management System (Classes & Objects)
    # -------------------------------------------------------------
    DayBlueprint(
        order=7,
        title="Day 7 (Project): Basic Student Management System",
        concept="Hands-on Project Day: Integrating classes, objects, state encapsulation, custom constructors, and interactive domain behaviors into a cohesive student record system",
        analogy="Think of today's project like opening a brand new digital registrar's office for a university. Instead of recording grades on scattered sticky notes, you are constructing an integrated database: individual `Student` objects keep track of their own courses and grades, while a master `Classroom` object manages enrollments, computes GPA rankings, and generates honor roll rosters!",
        is_project_day=True,
        project_name="Basic Student Management System",
        theory_sections=[
            {
                "heading": "Project Architecture & Domain Modeling",
                "body": "In professional software development, projects begin with **Domain Modeling**—identifying the real-world nouns and designing corresponding classes:\n1. **`Student` Class**:\n   - State: `student_id`, `name`, `grades` (dictionary mapping course name to float score).\n   - Behavior: `add_grade(course, grade)`, `calculate_gpa()`, `get_status()`.\n2. **`Classroom` Manager Class**:\n   - State: `classroom_name`, `students` (list of Student objects).\n   - Behavior: `enroll_student(student)`, `find_student_by_id(id)`, `get_class_average()`.\n\nNotice how the `Classroom` class collaborates with `Student` objects, demonstrating object composition."
            },
            {
                "heading": "Defensive Programming in Domain Models",
                "body": "A robust system validates all inputs at the boundary:\n- Student IDs must be non-empty strings.\n- Grades must be between 0.0 and 100.0.\n- Duplicate enrollments must be prevented.\n- Division by zero must be guarded against when calculating GPA for students with zero grades."
            }
        ],
        code_snippets=[
            {
                "title": "Complete Implementation: Student Class",
                "language": "python",
                "code": "class Student:\n    def __init__(self, student_id: str, name: str):\n        if not student_id or not name:\n            raise ValueError('ID and Name are mandatory.')\n        self.student_id = student_id.strip()\n        self.name = name.strip()\n        self.grades = {}\n\n    def add_grade(self, course: str, score: float):\n        if 0.0 <= score <= 100.0:\n            self.grades[course] = score\n            return True\n        return False\n\n    def calculate_average(self) -> float:\n        if not self.grades:\n            return 0.0\n        return sum(self.grades.values()) / len(self.grades)\n\n    def is_passing(self, passing_threshold: float = 60.0) -> bool:\n        return self.calculate_average() >= passing_threshold",
                "explanation": "Encapsulates individual student state, grade addition, and GPA averaging."
            },
            {
                "title": "Complete Implementation: Classroom Manager Class",
                "language": "python",
                "code": "class Classroom:\n    def __init__(self, name: str):\n        self.name = name\n        self.students = []\n\n    def enroll(self, student: Student) -> bool:\n        if any(s.student_id == student.student_id for s in self.students):\n            return False  # Prevent duplicates\n        self.students.append(student)\n        return True\n\n    def get_class_average(self) -> float:\n        if not self.students:\n            return 0.0\n        averages = [s.calculate_average() for s in self.students if s.grades]\n        return sum(averages) / len(averages) if averages else 0.0\n\n    def get_honor_roll(self, threshold: float = 85.0) -> list:\n        return [s.name for s in self.students if s.calculate_average() >= threshold]",
                "explanation": "Manages a collection of student objects and performs aggregated domain queries."
            },
            {
                "title": "Project Test Harness: Enrolling Students & Recording Grades",
                "language": "python",
                "code": "room = Classroom('Computer Science 101')\ns1 = Student('CS01', 'Alice')\ns1.add_grade('Python', 95.0)\ns1.add_grade('Math', 90.0)\n\ns2 = Student('CS02', 'Bob')\ns2.add_grade('Python', 70.0)\ns2.add_grade('Math', 65.0)\n\nroom.enroll(s1)\nroom.enroll(s2)\nprint('Class Average:', room.get_class_average())\nprint('Honor Roll:', room.get_honor_roll())",
                "explanation": "Demonstrates object interaction between Classroom and multiple Student instances."
            },
            {
                "title": "Python Script: JSON Export of System State",
                "language": "python",
                "code": "import json\n\ndef export_student_to_dict(student: Student) -> dict:\n    return {\n        'id': student.student_id,\n        'name': student.name,\n        'grades': student.grades,\n        'average': round(student.calculate_average(), 2)\n    }\n\nprint(json.dumps([export_student_to_dict(s) for s in room.students], indent=2))",
                "explanation": "Shows how object attributes are serialized into standard JSON payloads for API transmission."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Classroom Top Performer Search",
            description="Add a method `get_top_student()` to the `Classroom` class that returns the `Student` object with the highest average score. If the classroom has no students or no students have grades, return `None`.",
            starter_code="class Classroom:\n    # Implement get_top_student() method\n    pass",
            solution_code="class Classroom:\n    def __init__(self, name: str):\n        self.name = name\n        self.students = []\n\n    def enroll(self, student):\n        self.students.append(student)\n\n    def get_top_student(self):\n        graded_students = [s for s in self.students if s.grades]\n        if not graded_students:\n            return None\n        return max(graded_students, key=lambda s: s.calculate_average())",
            expected_output="Top Student: Alice (92.5)"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="In the Student Management System, what is the design relationship between `Classroom` and `Student`?",
                options=[
                    "Composition/Aggregation: Classroom holds and manages a collection of Student objects",
                    "Inheritance: Classroom is a sub-type of Student",
                    "Polymorphism: Student overrides Classroom's method signatures",
                    "Procedural macro replacement"
                ],
                correct_answer="Composition/Aggregation: Classroom holds and manages a collection of Student objects",
                explanation="Classroom *has* students (Aggregation/Composition), demonstrating how higher-level objects coordinate child objects."
            ),
            QuizQuestionBlueprint(
                question="Why is it advantageous to store student grades inside a `Student` instance rather than a separate parallel list in `Classroom`?",
                options=[
                    "It upholds encapsulation: each student's grades belong directly to that student's state",
                    "It reduces RAM consumption by 90%",
                    "Because Python dictionaries can only be defined inside Person classes",
                    "It allows grades to be stored in an SQL database without a network connection"
                ],
                correct_answer="It upholds encapsulation: each student's grades belong directly to that student's state",
                explanation="Encapsulation dictates that an entity's data (grades) should be bundled directly with the entity (Student) rather than maintained in loose external lists."
            ),
            QuizQuestionBlueprint(
                question="What defensive programming practice should be implemented in `calculate_average()` to prevent runtime crashes?",
                options=[
                    "Checking if `self.grades` is empty before dividing by its length to avoid a `ZeroDivisionError`",
                    "Encrypting all grades with SHA-256 before doing addition",
                    "Rebooting the computer if a student gets an F",
                    "Limiting the student's name to 4 characters"
                ],
                correct_answer="Checking if `self.grades` is empty before dividing by its length to avoid a `ZeroDivisionError`",
                explanation="If a student has no recorded grades, dividing by `len(self.grades)` (0) throws a `ZeroDivisionError` unless guarded."
            ),
            QuizQuestionBlueprint(
                question="How does the `enroll()` method prevent the registration of duplicate students?",
                options=[
                    "By verifying that no existing student in the list shares the new student's `student_id` before appending",
                    "By deleting all existing students when a new one arrives",
                    "By converting student names into uppercase",
                    "By storing students in a read-only tuple"
                ],
                correct_answer="By verifying that no existing student in the list shares the new student's `student_id` before appending",
                explanation="Comparing unique identifiers (like `student_id`) before enrollment enforces domain integrity."
            ),
            QuizQuestionBlueprint(
                question="What is the benefit of defining `is_passing(passing_threshold=60.0)` as a method on `Student` rather than calculating it externally?",
                options=[
                    "It centralizes passing criteria logic inside the class so changes to passing rules don't require rewriting code across multiple screens",
                    "It prevents other developers from seeing student names",
                    "It speeds up CPU execution by 10x",
                    "It makes the student exempt from homework"
                ],
                correct_answer="It centralizes passing criteria logic inside the class so changes to passing rules don't require rewriting code across multiple screens",
                explanation="Centralizing logic inside domain classes promotes high cohesion and single source of truth for business rules."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 8: Concept of Encapsulation (Data Binding)
    # -------------------------------------------------------------
    DayBlueprint(
        order=8,
        title="Day 8: Concept of Encapsulation (Data Binding)",
        concept="The First Pillar of OOP: Encapsulation - bundling state and behavior into a protective capsule and controlling access boundaries",
        analogy="Think of a medical medicine capsule: the pharmaceutical powder inside contains complex chemical compounds. The gelatin capsule wraps the medicine into a neat, unified pill that protects the medicine from contamination and protects the patient's throat from bitter chemicals. You swallow the capsule whole without needing to understand or touch the chemical powder directly. Encapsulation wraps data and methods into a clean, protective capsule!",
        theory_sections=[
            {
                "heading": "What is Encapsulation?",
                "body": "**Encapsulation** is the foundational pillar of OOP that bundles related data (attributes) and the methods operating on that data into a single, cohesive unit (the class). At the same time, it establishes boundaries that restrict direct outside access to an object's internal components.\n\nEncapsulation provides two key guarantees:\n1. **Data Binding**: Related data and operations live together in a single conceptual entity.\n2. **Information Hiding**: Internal representation details are shielded from outside tampering, exposing only a well-defined public interface."
            },
            {
                "heading": "The Hazards of Unencapsulated Code",
                "body": "When code is unencapsulated, any script can directly reach into an object's memory and change values without validation. For example, if a `Thermometer` object has its `celsius` variable set to `-500` (below absolute zero), or a `User` has its `age` set to `-42`, the system will crash or produce invalid calculations downstream. Encapsulation guarantees that internal state can only change through validated channels."
            }
        ],
        code_snippets=[
            {
                "title": "Unencapsulated (Fragile) Class vs Encapsulated Class",
                "language": "python",
                "code": "# Bad (Unencapsulated): No protection against illegal state\nclass BrokenClock:\n    def __init__(self):\n        self.hours = 0\n\nc = BrokenClock()\nc.hours = 999  # Invalid time, but nothing stopped it!\n\n# Good (Encapsulated): Guarded state modifications\nclass SecureClock:\n    def __init__(self):\n        self._hours = 0\n\n    def set_hours(self, h: int):\n        if 0 <= h < 24:\n            self._hours = h\n        else:\n            raise ValueError('Hours must be between 0 and 23.')\n\n    def get_hours(self) -> int:\n        return self._hours",
                "explanation": "Encapsulation prevents callers from forcing objects into corrupted or nonsensical states."
            },
            {
                "title": "Encapsulating Complexity: Washing Machine Example",
                "language": "python",
                "code": "class WashingMachine:\n    def __init__(self):\n        self._water_level = 0\n        self._motor_running = False\n\n    def wash_cycle(self):\n        # Outside caller only clicks one button; internal steps are encapsulated\n        self._fill_water()\n        self._start_motor()\n        self._drain()\n        return 'Wash cycle completed!'\n\n    def _fill_water(self):\n        self._water_level = 100\n    def _start_motor(self):\n        self._motor_running = True\n    def _drain(self):\n        self._water_level = 0\n        self._motor_running = False\n\nwm = WashingMachine()\nprint(wm.wash_cycle())",
                "explanation": "The user only interacts with wash_cycle(); internal coordination is shielded."
            },
            {
                "title": "Encapsulating Collections and Invariant Integrity",
                "language": "python",
                "code": "class ShoppingCart:\n    def __init__(self):\n        self._items = []  # Internal list\n\n    def add_item(self, item: str, price: float):\n        if price > 0:\n            self._items.append({'item': item, 'price': price})\n\n    def get_total(self) -> float:\n        return sum(i['price'] for i in self._items)\n\n    def get_items(self) -> list:\n        # Return a copy to prevent external mutation of internal list\n        return list(self._items)",
                "explanation": "Returning defensive copies prevents external callers from bypassing add_item."
            },
            {
                "title": "Python Script: Demonstrating Attribute Protection",
                "language": "python",
                "code": "cart = ShoppingCart()\ncart.add_item('Book', 25.0)\nexternal_list = cart.get_items()\nexternal_list.clear()  # Attacker clears the returned list\nprint('Cart total after external tamper:', cart.get_total())  # Still 25.0!",
                "explanation": "Defensive copies preserve internal encapsulation against rogue callers."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Encapsulated Temperature Converter",
            description="Create an encapsulated `Temperature` class initialized with a Celsius value. Provide `get_celsius()`, `set_celsius(value)` (which raises `ValueError('Below absolute zero')` if value < -273.15), and a read-only `get_fahrenheit()` method that computes `(celsius * 9/5) + 32`.",
            starter_code="class Temperature:\n    # Implement encapsulated Temperature class\n    pass",
            solution_code="class Temperature:\n    def __init__(self, celsius: float = 0.0):\n        self.set_celsius(celsius)\n\n    def get_celsius(self) -> float:\n        return self._celsius\n\n    def set_celsius(self, value: float):\n        if value < -273.15:\n            raise ValueError('Below absolute zero')\n        self._celsius = float(value)\n\n    def get_fahrenheit(self) -> float:\n        return (self._celsius * 9 / 5) + 32",
            expected_output="0.0\n32.0"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What are the two core aspects of Encapsulation in OOP?",
                options=[
                    "Bundling data and operations together, while restricting direct outside access to internal state",
                    "Converting source code to machine code and linking libraries",
                    "Inheriting methods from parent classes and overriding them",
                    "Formatting text files into JSON payloads"
                ],
                correct_answer="Bundling data and operations together, while restricting direct outside access to internal state",
                explanation="Encapsulation bundles state with behavior (data binding) and protects it from unauthorized access (information hiding)."
            ),
            QuizQuestionBlueprint(
                question="Why is exposing raw mutable instance attributes directly to external callers considered dangerous?",
                options=[
                    "External callers can assign invalid or corrupt data without triggering any validation logic",
                    "It deletes all comments from source code",
                    "It slows down Python by a factor of 1000",
                    "It converts integers into strings automatically"
                ],
                correct_answer="External callers can assign invalid or corrupt data without triggering any validation logic",
                explanation="Without encapsulation, outside code can set illegal states (like negative balances or invalid ages) without validation."
            ),
            QuizQuestionBlueprint(
                question="How does returning a copy of an internal list (defensive copying) preserve encapsulation?",
                options=[
                    "It prevents external callers from modifying or clearing the object's internal collection directly",
                    "It doubles the memory capacity of the computer",
                    "It encrypts the list elements with AES-256",
                    "It transforms the list into an immutable string"
                ],
                correct_answer="It prevents external callers from modifying or clearing the object's internal collection directly",
                explanation="Returning a defensive copy prevents callers from using methods like .clear() or .append() to tamper with internal collections."
            ),
            QuizQuestionBlueprint(
                question="In what way does Encapsulation simplify code maintenance for software developers?",
                options=[
                    "Internal implementations can be refactored or optimized without breaking external code that relies on the public interface",
                    "It eliminates the need to compile code",
                    "It ensures that programs never require testing",
                    "It prevents other developers from reading source files"
                ],
                correct_answer="Internal implementations can be refactored or optimized without breaking external code that relies on the public interface",
                explanation="As long as the public method signatures remain stable, internal data structures can be overhauled safely."
            ),
            QuizQuestionBlueprint(
                question="Which real-world analogy best captures the concept of Encapsulation?",
                options=[
                    "A medicine capsule that seals pharmaceutical powders inside a smooth protective shell",
                    "A public park where anyone can plant anything anywhere",
                    "A highway with no speed limits or lanes",
                    "An open book floating in a swimming pool"
                ],
                correct_answer="A medicine capsule that seals pharmaceutical powders inside a smooth protective shell",
                explanation="The medicine capsule wraps the ingredients inside a single unit and shields the interior from outside contamination."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 9: Access Modifiers (Public, Private, Protected)
    # -------------------------------------------------------------
    DayBlueprint(
        order=9,
        title="Day 9: Access Modifiers (Public, Private, Protected)",
        concept="Enforcing Access Boundaries: Public, Protected (`_`), and Private (`__`) access modifiers, and Python's name mangling mechanism",
        analogy="Think of a three-level security building: **Public** is the lobby: anyone from the public street can walk in and sit on the couch. **Protected** is the employee lounge: visitors are asked not to enter, but employees and their family members (subclasses) are welcome. **Private** is the vault in the basement: only the head accountant can open it; even employees and relatives are strictly locked out!",
        theory_sections=[
            {
                "heading": "Access Control in OOP Languages",
                "body": "Access modifiers specify the visibility and accessibility of class members (attributes and methods):\n- **Public**: Accessible from anywhere in the program.\n- **Protected**: Intended to be accessed only within the defining class and its subclasses.\n- **Private**: Accessible strictly within the class where it is declared; hidden from subclasses and external callers.\n\nIn languages like Java and C++, keywords `public`, `protected`, and `private` are enforced strictly by the compiler."
            },
            {
                "heading": "Python's Philosophy & Name Mangling",
                "body": "Python adopts the philosophy: *\"We are all consenting adults here.\"* Access levels are defined by naming conventions:\n- **Public** (`var`): Normal variables; fully accessible.\n- **Protected** (`_var`): Single leading underscore. A strong convention telling developers: *'This is internal; do not touch unless you know what you are doing.'*\n- **Private** (`__var`): Double leading underscore. Triggers **Name Mangling**, rewriting `__var` internally to `_ClassName__var` to prevent accidental overrides in subclasses."
            }
        ],
        code_snippets=[
            {
                "title": "Public, Protected, and Private Members in Python",
                "language": "python",
                "code": "class Employee:\n    def __init__(self, name: str, salary: float, ssn: str):\n        self.name = name          # Public: anyone can access\n        self._salary = salary     # Protected: internal & subclass convention\n        self.__ssn = ssn          # Private: name mangled\n\n    def get_masked_ssn(self) -> str:\n        # Private members are freely accessible inside class methods\n        return f'***-**-{self.__ssn[-4:]}'\n\ne = Employee('Alice', 85000.0, '123-45-6789')\nprint('Public:', e.name)\nprint('Protected (convention):', e._salary)\nprint('Masked SSN:', e.get_masked_ssn())",
                "explanation": "Illustrates the three visibility levels in Python."
            },
            {
                "title": "Demonstrating Python Name Mangling and AttributeError",
                "language": "python",
                "code": "try:\n    # Direct access to private attribute raises AttributeError\n    print(e.__ssn)\nexcept AttributeError as err:\n    print('Direct access blocked:', err)\n\n# Python mangles __ssn to _Employee__ssn\nprint('Mangled attribute access:', e._Employee__ssn)",
                "explanation": "Double underscores mangle the attribute name by prefixing it with _ClassName."
            },
            {
                "title": "Subclass Interaction with Protected vs Private Members",
                "language": "python",
                "code": "class Manager(Employee):\n    def get_salary_info(self) -> str:\n        # Subclasses can safely access protected members by convention\n        return f'Manager {self.name} salary is ${self._salary}'\n\nm = Manager('Bob', 120000.0, '987-65-4321')\nprint(m.get_salary_info())",
                "explanation": "Protected members are designed for use across inheritance hierarchies."
            },
            {
                "title": "Java / C++ Comparison with Explicit Keywords",
                "language": "text",
                "code": "// In Java / C++:\n// public class Employee {\n//     public String name;\n//     protected double salary;\n//     private String ssn; // Enforced at compile-time by compiler error!\n// }",
                "explanation": "Contrasts Python's runtime name mangling with Java/C++ compile-time access enforcement."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Secure Vault with Private Key",
            description="Create a `Vault` class with a public `owner: str`, a protected `_balance: float`, and a private `__access_code: str`. Implement a method `unlock(code: str) -> bool` that verifies the code against `__access_code`, and a method `withdraw(amount: float, code: str)` that deducts from `_balance` only if the code matches and balance is sufficient.",
            starter_code="class Vault:\n    # Implement Vault with public, protected, and private attributes\n    pass",
            solution_code="class Vault:\n    def __init__(self, owner: str, initial_balance: float, access_code: str):\n        self.owner = owner\n        self._balance = float(initial_balance)\n        self.__access_code = str(access_code)\n\n    def unlock(self, code: str) -> bool:\n        return self.__access_code == str(code)\n\n    def withdraw(self, amount: float, code: str) -> str:\n        if not self.unlock(code):\n            return 'Invalid code'\n        if amount > self._balance:\n            return 'Insufficient funds'\n        self._balance -= amount\n        return f'Withdrew ${amount:.2f}, remaining ${self._balance:.2f}'",
            expected_output="True\nWithdrew $50.00, remaining $150.00\nInvalid code"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="How does Python represent a 'Protected' attribute by convention?",
                options=[
                    "With a single leading underscore (e.g., `_salary`)",
                    "With a double leading underscore (e.g., `__salary`)",
                    "With the keyword `protected` before the variable",
                    "With all capital letters"
                ],
                correct_answer="With a single leading underscore (e.g., `_salary`)",
                explanation="A single leading underscore `_var` indicates a protected member intended for class and subclass use only."
            ),
            QuizQuestionBlueprint(
                question="What mechanism does Python execute when an attribute is defined with two leading underscores (e.g., `__pin`)?",
                options=[
                    "Name Mangling: it internally renames the attribute to `_ClassName__attribute` to prevent collisions",
                    "Memory Encryption: it encrypts the value using SHA-256 in RAM",
                    "Process Termination: it prevents any other thread from running",
                    "Static compilation to machine code"
                ],
                correct_answer="Name Mangling: it internally renames the attribute to `_ClassName__attribute` to prevent collisions",
                explanation="Name mangling transforms `__pin` into `_ClassName__pin`, protecting it from accidental override or direct external access."
            ),
            QuizQuestionBlueprint(
                question="Which access modifier allows a member to be accessed freely by any code anywhere in the application?",
                options=[
                    "Public",
                    "Private",
                    "Protected",
                    "Internal"
                ],
                correct_answer="Public",
                explanation="Public members have zero access restrictions and form the public interface of a class."
            ),
            QuizQuestionBlueprint(
                question="In languages like C++ and Java, what happens if an external class tries to access a `private` member directly?",
                options=[
                    "The code fails to compile with a compilation error",
                    "The member returns null",
                    "The member is automatically promoted to public",
                    "A runtime warning is printed to the console"
                ],
                correct_answer="The code fails to compile with a compilation error",
                explanation="C++ and Java enforce access modifiers at compile time; accessing a private member from outside causes a compiler error."
            ),
            QuizQuestionBlueprint(
                question="What is the philosophy behind Python's convention-based protected access (`_var`)?",
                options=[
                    "'We are all consenting adults here': developers respect the leading underscore convention without needing compiler handcuffs",
                    "Python is unable to hide data due to hardware limitations",
                    "Protected variables are faster than public variables",
                    "Underscores make variable names look more stylish"
                ],
                correct_answer="'We are all consenting adults here': developers respect the leading underscore convention without needing compiler handcuffs",
                explanation="Python trusts developers to respect conventions (`_var`) rather than imposing rigid compiler restrictions."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 10: Getters and Setters (Accessor & Mutator)
    # -------------------------------------------------------------
    DayBlueprint(
        order=10,
        title="Day 10: Getters and Setters (Accessor & Mutator)",
        concept="Controlled Attribute Access: Traditional getter/setter methods versus Pythonic `@property` decorators",
        analogy="Imagine an entrance to an upscale movie theater. A traditional direct attribute is like a missing door: anyone can walk in off the street without a ticket. A **Getter** is like a display screen showing the movie title to anyone in the lobby. A **Setter** is the ticket collector standing at the door: before you can set your body into a seat, the collector verifies your ticket, checks your age rating, and denies entry if you try to sneak in without paying!",
        theory_sections=[
            {
                "heading": "Why Use Getters and Setters?",
                "body": "In traditional OOP languages (like Java and C++), raw attributes are declared `private`, and access is exposed strictly via **Getters** (Accessors, e.g., `getSalary()`) and **Setters** (Mutators, e.g., `setSalary(amount)`). This provides:\n- **Validation**: Reject illegal values before they touch state.\n- **Read-Only Attributes**: Providing a getter without a setter makes an attribute immutable from outside.\n- **Transformation & Logging**: Audit who accessed data or transform data on the fly."
            },
            {
                "heading": "Pythonic Properties with `@property`",
                "body": "In Python, writing verbose `get_x()` and `set_x()` calls everywhere is considered un-pythonic. Instead, Python provides the **`@property` decorator**.\n\nThe `@property` decorator allows you to define methods that can be accessed with clean, natural attribute syntax (`obj.x` instead of `obj.get_x()`), while seamlessly executing getter, setter, and deleter logic behind the scenes."
            }
        ],
        code_snippets=[
            {
                "title": "Traditional Java/C++ Style Getters and Setters in Python",
                "language": "python",
                "code": "class PersonTraditional:\n    def __init__(self, age: int):\n        self._age = 0\n        self.set_age(age)\n\n    def get_age(self) -> int:\n        return self._age\n\n    def set_age(self, age: int):\n        if age < 0:\n            raise ValueError('Age cannot be negative.')\n        self._age = age\n\np = PersonTraditional(20)\np.set_age(25)\nprint('Age:', p.get_age())",
                "explanation": "Traditional getter/setter pattern using explicit method calls."
            },
            {
                "title": "Pythonic Getters and Setters using the @property Decorator",
                "language": "python",
                "code": "class PersonPythonic:\n    def __init__(self, age: int):\n        self.age = age  # Automatically triggers the setter validation!\n\n    @property\n    def age(self) -> int:\n        \"\"\"The getter method.\"\"\"\n        return self._age\n\n    @age.setter\n    def age(self, value: int):\n        \"\"\"The setter method with validation.\"\"\"\n        if value < 0:\n            raise ValueError('Age cannot be negative.')\n        self._age = value\n\np = PersonPythonic(30)\nprint('Read via property:', p.age)  # Natural dot syntax\np.age = 35                          # Calls setter seamlessly\nprint('Updated age:', p.age)",
                "explanation": "@property combines clean attribute syntax with full validation and encapsulation."
            },
            {
                "title": "Creating Read-Only Computed Properties",
                "language": "python",
                "code": "class Circle:\n    def __init__(self, radius: float):\n        self.radius = radius\n\n    @property\n    def area(self) -> float:\n        import math\n        return math.pi * (self.radius ** 2)\n\nc = Circle(5.0)\nprint('Area:', round(c.area, 2))\ntry:\n    c.area = 100  # Will fail because no setter is defined!\nexcept AttributeError as e:\n    print('Read-only error:', e)",
                "explanation": "Omitting the setter decorator creates a read-only computed property."
            },
            {
                "title": "Property Deleter Demonstration",
                "language": "python",
                "code": "class UserSession:\n    def __init__(self, token: str):\n        self._token = token\n\n    @property\n    def token(self):\n        return self._token\n\n    @token.deleter\n    def token(self):\n        print('Clearing session token...')\n        self._token = None\n\ns = UserSession('xyz123')\ndel s.token\nprint('Token after delete:', s.token)",
                "explanation": "The @property.deleter hook enables custom cleanup when 'del obj.prop' is executed."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Build a BankAccount with @property Validation",
            description="Create an `Account` class with a private `_balance: float`. Implement a `@property` named `balance` with a getter returning the float and a setter that raises `ValueError('Negative balance rejected')` if the new balance is < 0. Add a read-only property `is_overdrawn` that returns `True` if `_balance == 0`, else `False`.",
            starter_code="class Account:\n    # Implement Account with @property balance and read-only is_overdrawn\n    pass",
            solution_code="class Account:\n    def __init__(self, initial_balance: float = 0.0):\n        self._balance = 0.0\n        self.balance = initial_balance\n\n    @property\n    def balance(self) -> float:\n        return self._balance\n\n    @balance.setter\n    def balance(self, value: float):\n        if value < 0:\n            raise ValueError('Negative balance rejected')\n        self._balance = float(value)\n\n    @property\n    def is_overdrawn(self) -> bool:\n        return self._balance == 0.0",
            expected_output="150.0\nFalse\nTrue"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the primary role of a Setter (mutator) method?",
                options=[
                    "To validate and sanitize incoming data before assigning it to an internal attribute",
                    "To create a duplicate copy of the object on another server",
                    "To permanently lock the computer screen",
                    "To convert the object into an SQL query"
                ],
                correct_answer="To validate and sanitize incoming data before assigning it to an internal attribute",
                explanation="Setters validate arguments against domain rules before mutating internal state, preventing corrupted values."
            ),
            QuizQuestionBlueprint(
                question="How does Python's `@property` decorator improve upon traditional `get_name()` / `set_name()` methods?",
                options=[
                    "It allows getters and setters to be accessed using natural, clean dot syntax (e.g. `obj.name`) without ugly parentheses",
                    "It automatically saves all data to a blockchain",
                    "It doubles the CPU clock frequency",
                    "It eliminates the need to write unit tests"
                ],
                correct_answer="It allows getters and setters to be accessed using natural, clean dot syntax (e.g. `obj.name`) without ugly parentheses",
                explanation="`@property` provides clean attribute syntax (`user.name = 'Bob'`) while executing validation methods under the hood."
            ),
            QuizQuestionBlueprint(
                question="How do you create a read-only property using the `@property` decorator in Python?",
                options=[
                    "Define a method with `@property` but do not define a matching `@name.setter` method",
                    "Add the `readonly` keyword before the class definition",
                    "Write the property name in all lowercase Greek letters",
                    "Call `sys.freeze()` inside `__init__`"
                ],
                correct_answer="Define a method with `@property` but do not define a matching `@name.setter` method",
                explanation="If a property has a getter (`@property`) but no setter (`@prop.setter`), attempting to assign to it raises an AttributeError."
            ),
            QuizQuestionBlueprint(
                question="In a class with a `@property` setter for `email`, what happens when you write `user.email = 'test@example.com'`?",
                options=[
                    "Python automatically redirects the assignment to the `@email.setter` method, passing the string as the value argument",
                    "The setter is ignored and a new public variable is created",
                    "A runtime error is thrown",
                    "The entire class is recompiled"
                ],
                correct_answer="Python automatically redirects the assignment to the `@email.setter` method, passing the string as the value argument",
                explanation="Python's descriptor protocol intercepts attribute assignment and routes it to the designated setter function."
            ),
            QuizQuestionBlueprint(
                question="What is a 'Computed Property'?",
                options=[
                    "A property whose getter dynamically calculates a value on demand (e.g. circle area or full name) rather than storing it statically in memory",
                    "A property stored on an external cloud mainframe",
                    "A property that can only calculate Fibonacci numbers",
                    "A property created by artificial intelligence"
                ],
                correct_answer="A property whose getter dynamically calculates a value on demand (e.g. circle area or full name) rather than storing it statically in memory",
                explanation="Computed properties dynamically calculate their returned values from other existing attributes whenever accessed."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 11: Data Hiding Techniques
    # -------------------------------------------------------------
    DayBlueprint(
        order=11,
        title="Day 11: Data Hiding Techniques",
        concept="Advanced Data Hiding and Immutability: Private attributes, `__slots__` for memory optimization and dynamic attribute prevention, and immutable data objects",
        analogy="Imagine an ATM cash machine. You do not see the mechanical gears, optical dollar-bill sorters, or internal Linux kernel running inside. All you have is a touch screen and a cash dispenser slot. Even if you brought a screwdriver to the ATM, the heavy steel safe protects the cash from being tampered with. Data hiding ensures internal mechanics and sensitive data are completely sealed away from external interference.",
        theory_sections=[
            {
                "heading": "Principles of Data Hiding",
                "body": "**Data Hiding** is the security-focused aspect of Encapsulation. While encapsulation focuses on *bundling*, data hiding focuses on *shielding*. It ensures that internal implementation details, raw data structures, and sensitive credentials cannot be inspected or altered arbitrarily by outside code.\n\nTechniques include:\n- Making sensitive state strictly private.\n- Using property getters that return defensive immutable copies (e.g., returning a `tuple` or copy instead of the internal list).\n- Preventing arbitrary dynamic attribute creation using `__slots__`."
            },
            {
                "heading": "Restricting Dynamic Attributes with `__slots__`",
                "body": "By default, Python objects store their instance attributes in a dynamic dictionary (`__dict__`). While flexible, this consumes significant memory and allows callers to accidentally attach rogue attributes (e.g., typing `user.emial = '...'` due to a typo).\n\nDefining `__slots__ = ('name', 'email')` tells Python to allocate fixed memory slots for only those specific attributes, reducing memory overhead by up to 50% and forbidding the attachment of any undeclared attributes."
            }
        ],
        code_snippets=[
            {
                "title": "Preventing Dynamic Attributes using __slots__",
                "language": "python",
                "code": "class LockedUser:\n    # Restrict attributes to strictly these two slots\n    __slots__ = ('username', 'email')\n\n    def __init__(self, username: str, email: str):\n        self.username = username\n        self.email = email\n\nu = LockedUser('alice', 'alice@test.com')\nprint('Slots user:', u.username, u.email)\n\ntry:\n    # Attempting to assign an unlisted attribute raises AttributeError\n    u.phone = '123-456-7890'\nexcept AttributeError as err:\n    print('Dynamic attribute blocked by __slots__:', err)",
                "explanation": "__slots__ blocks the addition of undeclared attributes, eliminating accidental typo bugs."
            },
            {
                "title": "Memory Consumption Comparison: __dict__ vs __slots__",
                "language": "python",
                "code": "import sys\n\nclass NormalPoint:\n    def __init__(self, x, y): self.x, self.y = x, y\n\nclass SlottedPoint:\n    __slots__ = ('x', 'y')\n    def __init__(self, x, y): self.x, self.y = x, y\n\nnp = NormalPoint(1, 2)\nsp = SlottedPoint(1, 2)\nprint('Normal instance dict exists?', hasattr(np, '__dict__'))\nprint('Slotted instance dict exists?', hasattr(sp, '__dict__'))",
                "explanation": "Slotted objects omit the __dict__ entirely, dramatically reducing heap footprint."
            },
            {
                "title": "Immutable Objects using Frozen Dataclasses",
                "language": "python",
                "code": "from dataclasses import dataclass\n\n@dataclass(frozen=True)\nclass ImmutableApiKey:\n    key_id: str\n    secret_token: str\n\napi = ImmutableApiKey('KEY_101', 'sec_987654321')\nprint('API Key:', api.key_id)\ntry:\n    api.secret_token = 'hacked'  # Frozen dataclass forbids modification!\nexcept Exception as e:\n    print('Mutation blocked:', type(e).__name__)",
                "explanation": "frozen=True enforces complete immutability after construction."
            },
            {
                "title": "Python Script: Hiding Internal State behind Closures",
                "language": "python",
                "code": "def make_secure_vault(secret_val: str):\n    # True un-mangleable private data via lexical closure\n    def get_secret(password: str):\n        return secret_val if password == 'open_sesame' else 'ACCESS DENIED'\n    return get_secret\n\nvault = make_secure_vault('TreasuryGold')\nprint(vault('wrong_pass'))\nprint(vault('open_sesame'))",
                "explanation": "Demonstrates closure-based information hiding where data is completely invisible in instance dicts."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Build an Immutable GPS Coordinate",
            description="Create a class `Coordinate` using `__slots__ = ('_latitude', '_longitude')`. The constructor should take `lat` (-90 to 90) and `lon` (-180 to 180). Expose read-only properties `latitude` and `longitude`. Attempting to set or add any other attribute should fail.",
            starter_code="class Coordinate:\n    # Implement Coordinate with __slots__ and read-only properties\n    pass",
            solution_code="class Coordinate:\n    __slots__ = ('_latitude', '_longitude')\n\n    def __init__(self, lat: float, lon: float):\n        if not (-90 <= lat <= 90):\n            raise ValueError('Latitude must be between -90 and 90')\n        if not (-180 <= lon <= 180):\n            raise ValueError('Longitude must be between -180 and 180')\n        self._latitude = float(lat)\n        self._longitude = float(lon)\n\n    @property\n    def latitude(self) -> float:\n        return self._latitude\n\n    @property\n    def longitude(self) -> float:\n        return self._longitude",
            expected_output="37.7749\n-122.4194"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the primary difference between Encapsulation and Data Hiding?",
                options=[
                    "Encapsulation is the bundling of data and methods together; Data Hiding is the specific shielding of internal state from external tampering",
                    "Encapsulation is for strings; Data Hiding is for numbers",
                    "Data Hiding is only used in procedural languages like C",
                    "There is no difference; they are exact duplicates"
                ],
                correct_answer="Encapsulation is the bundling of data and methods together; Data Hiding is the specific shielding of internal state from external tampering",
                explanation="Encapsulation packages state with behavior, while data hiding restricts visibility to protect internal invariants."
            ),
            QuizQuestionBlueprint(
                question="What is the effect of defining `__slots__` in a Python class?",
                options=[
                    "It allocates fixed memory slots for attributes, prevents the creation of a dynamic `__dict__`, and blocks undeclared attributes",
                    "It converts the class into an online casino slot machine",
                    "It allows the class to inherit from 50 parents simultaneously",
                    "It prevents the object from being instantiated"
                ],
                correct_answer="It allocates fixed memory slots for attributes, prevents the creation of a dynamic `__dict__`, and blocks undeclared attributes",
                explanation="`__slots__` optimizes memory by replacing the per-instance dictionary with a fixed array of pointers and preventing arbitrary attribute assignment."
            ),
            QuizQuestionBlueprint(
                question="What happens if you try to assign an attribute not listed in `__slots__` to an instance?",
                options=[
                    "An `AttributeError` is raised",
                    "The attribute is silently converted to a global variable",
                    "The attribute is added to the class instead",
                    "The computer prints a warning to stderr"
                ],
                correct_answer="An `AttributeError` is raised",
                explanation="Instances of slotted classes lack a `__dict__`, so attempting to assign any undeclared attribute raises an `AttributeError`."
            ),
            QuizQuestionBlueprint(
                question="How does Python's `@dataclass(frozen=True)` enforce data hiding and immutability?",
                options=[
                    "It intercepts any attribute assignment after initialization and raises a FrozenInstanceError",
                    "It stores the data inside the BIOS chip",
                    "It encrypts all data with an RSA 4096-bit private key",
                    "It converts all numbers into floating-point NaN"
                ],
                correct_answer="It intercepts any attribute assignment after initialization and raises a FrozenInstanceError",
                explanation="Setting `frozen=True` on a dataclass makes its fields read-only; attempts to modify fields after instantiation raise an error."
            ),
            QuizQuestionBlueprint(
                question="Why is data hiding critical in financial and security systems?",
                options=[
                    "It prevents accidental or unauthorized tampering with critical states like account balances or cryptographic keys",
                    "It prevents users from taking screenshots",
                    "It ensures that bank databases can never run out of disk space",
                    "It eliminates the need for user passwords"
                ],
                correct_answer="It prevents accidental or unauthorized tampering with critical states like account balances or cryptographic keys",
                explanation="Shielding internal state ensures that monetary balances, cryptographic keys, and authorization flags cannot be directly forged."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 12 (Project): Secure Bank Account System
    # -------------------------------------------------------------
    DayBlueprint(
        order=12,
        title="Day 12 (Project): Secure Bank Account System",
        concept="Hands-on Project Day: Engineering a robust, encapsulated banking engine featuring PIN authentication, transaction audit ledgers, daily transfer limits, and property validation",
        analogy="Think of today's project like constructing a commercial Swiss bank vault. Customers cannot just walk in and grab cash out of the safe. Every transaction requires multi-factor authentication (PIN verification), every dollar moved is audited in an unalterable paper ledger, daily withdrawal limits prevent fraud, and account balances are strictly private and encapsulated!",
        is_project_day=True,
        project_name="Secure Bank Account System",
        theory_sections=[
            {
                "heading": "Banking Engine Architecture & Requirements",
                "body": "In financial technology, security and auditability are non-negotiable. Today's project implements an enterprise-grade `BankAccount`:\n1. **Data Hiding**: Account numbers and balances are strictly private (`_balance`, `__pin_hash`).\n2. **PIN Authentication**: Operations (withdrawals, transfers) require a 4-digit PIN verified via cryptographic hashing (e.g. SHA-256).\n3. **Audit Ledger**: Every deposit, withdrawal, and failed login attempt is recorded in an immutable transaction history.\n4. **Risk Controls**: Daily withdrawal limits are enforced automatically."
            },
            {
                "heading": "State Invariants and Atomic Transactions",
                "body": "A banking system must maintain **ACID-like invariants**:\n- Balance must never become negative (no overdraft unless explicitly authorized).\n- A transfer must be atomic: if deducting from Sender succeeds but crediting Receiver fails, the entire transaction must roll back.\n- Transaction audit timestamps must be ISO-8601 formatted."
            }
        ],
        code_snippets=[
            {
                "title": "Complete Implementation: Secure Bank Account Class",
                "language": "python",
                "code": "import hashlib\nfrom datetime import datetime\n\nclass SecureBankAccount:\n    def __init__(self, account_number: str, owner: str, pin: str, initial_deposit: float = 0.0):\n        if initial_deposit < 0:\n            raise ValueError('Initial deposit cannot be negative.')\n        self.account_number = account_number\n        self.owner = owner\n        self._balance = float(initial_deposit)\n        self.__pin_hash = self._hash_pin(pin)\n        self._ledger = []\n        self._record_transaction('ACCOUNT_CREATED', initial_deposit)\n\n    def _hash_pin(self, pin: str) -> str:\n        return hashlib.sha256(str(pin).encode()).hexdigest()\n\n    def _verify_pin(self, pin: str) -> bool:\n        return self.__pin_hash == self._hash_pin(pin)\n\n    def _record_transaction(self, tx_type: str, amount: float):\n        self._ledger.append({\n            'timestamp': datetime.utcnow().isoformat(),\n            'type': tx_type,\n            'amount': amount,\n            'balance_after': self._balance\n        })",
                "explanation": "Initializes secure account with SHA-256 hashed PIN and an internal transaction ledger."
            },
            {
                "title": "Deposit, Withdrawal, and Audit Ledger Methods",
                "language": "python",
                "code": "    @property\n    def balance(self) -> float:\n        \"\"\"Read-only view of balance.\"\"\"\n        return self._balance\n\n    def deposit(self, amount: float) -> bool:\n        if amount <= 0:\n            return False\n        self._balance += amount\n        self._record_transaction('DEPOSIT', amount)\n        return True\n\n    def withdraw(self, amount: float, pin: str) -> str:\n        if not self._verify_pin(pin):\n            return 'AUTH_FAILED'\n        if amount <= 0:\n            return 'INVALID_AMOUNT'\n        if amount > self._balance:\n            return 'INSUFFICIENT_FUNDS'\n        self._balance -= amount\n        self._record_transaction('WITHDRAWAL', amount)\n        return 'SUCCESS'\n\n    def get_statement(self) -> list:\n        # Return defensive copy of ledger\n        return [dict(tx) for tx in self._ledger]",
                "explanation": "Enforces PIN verification and logs every successful transaction into the ledger."
            },
            {
                "title": "Executing Secure Account Operations and Transfer Flow",
                "language": "python",
                "code": "acc1 = SecureBankAccount('ACC-001', 'Alice', '1234', 500.0)\nacc2 = SecureBankAccount('ACC-002', 'Bob', '9999', 100.0)\n\n# Perform verified transactions\nprint('Withdraw wrong PIN:', acc1.withdraw(50, '0000'))  # AUTH_FAILED\nprint('Withdraw valid PIN:', acc1.withdraw(50, '1234'))  # SUCCESS\n\nacc1.deposit(200.0)\nprint('Alice balance:', acc1.balance)\nprint('Ledger count:', len(acc1.get_statement()))",
                "explanation": "Demonstrates PIN verification, withdrawal guards, and statement generation."
            },
            {
                "title": "Python Script: Atomic Fund Transfer Between Two Accounts",
                "language": "python",
                "code": "def transfer(sender: SecureBankAccount, receiver: SecureBankAccount, amount: float, pin: str) -> bool:\n    status = sender.withdraw(amount, pin)\n    if status == 'SUCCESS':\n        receiver.deposit(amount)\n        return True\n    return False\n\nsuccess = transfer(acc1, acc2, 100.0, '1234')\nprint('Transfer success?', success)\nprint('Alice remaining:', acc1.balance)\nprint('Bob new balance:', acc2.balance)",
                "explanation": "Simulates an atomic inter-account transfer coordinating both encapsulated accounts."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Add Daily Transfer Limit Check",
            description="Extend the `SecureBankAccount` class by adding a `daily_limit: float` (default 1000.0) attribute and tracking total daily withdrawals. If a requested withdrawal amount plus today's previous withdrawals exceeds `daily_limit`, return `'LIMIT_EXCEEDED'` even if balance and PIN are valid.",
            starter_code="class SecureBankAccount:\n    # Implement daily limit tracking in withdraw()\n    pass",
            solution_code="class SecureBankAccount:\n    def __init__(self, balance: float = 0.0, daily_limit: float = 1000.0):\n        self._balance = float(balance)\n        self.daily_limit = float(daily_limit)\n        self.withdrawn_today = 0.0\n\n    def withdraw(self, amount: float) -> str:\n        if self.withdrawn_today + amount > self.daily_limit:\n            return 'LIMIT_EXCEEDED'\n        if amount > self._balance:\n            return 'INSUFFICIENT_FUNDS'\n        self._balance -= amount\n        self.withdrawn_today += amount\n        return 'SUCCESS'",
            expected_output="SUCCESS\nLIMIT_EXCEEDED"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Why is storing password or PIN credentials as SHA-256 hashes inside a class considered standard practice?",
                options=[
                    "Even if an attacker inspects object memory or logs, they cannot easily reverse-engineer the original cleartext PIN",
                    "Hashing speeds up CPU addition by 50%",
                    "Because Python refuses to store strings longer than 3 characters",
                    "It compresses the PIN to 1 bit"
                ],
                correct_answer="Even if an attacker inspects object memory or logs, they cannot easily reverse-engineer the original cleartext PIN",
                explanation="One-way cryptographic hashes protect user credentials against memory dumps, logs, and database leaks."
            ),
            QuizQuestionBlueprint(
                question="What is the purpose of maintaining an internal transaction ledger inside `SecureBankAccount`?",
                options=[
                    "To provide an immutable, verifiable audit trail of every deposit, withdrawal, and balance change for accountability",
                    "To send automatic spam emails to customers",
                    "To delete the account when memory is low",
                    "To calculate currency exchange rates with Mars"
                ],
                correct_answer="To provide an immutable, verifiable audit trail of every deposit, withdrawal, and balance change for accountability",
                explanation="Audit ledgers maintain historical provenance, enabling financial reconciliation and fraud investigation."
            ),
            QuizQuestionBlueprint(
                question="Why is `balance` exposed as a read-only `@property` without a setter?",
                options=[
                    "Because balances should only mutate through audited `deposit()` and `withdraw()` business workflows, not arbitrary assignments",
                    "Because balances cannot be displayed on computer monitors",
                    "Because float numbers are immutable in Python",
                    "Because banks do not allow users to check their balances"
                ],
                correct_answer="Because balances should only mutate through audited `deposit()` and `withdraw()` business workflows, not arbitrary assignments",
                explanation="A read-only property prevents rogue code from arbitrarily writing `acc.balance = 1000000` without depositing funds."
            ),
            QuizQuestionBlueprint(
                question="In the inter-account `transfer` function, what would happen if the sender's withdrawal succeeded but the receiver's deposit failed without error handling?",
                options=[
                    "Money would vanish from the sender without appearing in the receiver's account (broken financial invariant)",
                    "The computer would catch fire",
                    "Both accounts would automatically double their money",
                    "Nothing, because Python automatically rewinds bank accounts"
                ],
                correct_answer="Money would vanish from the sender without appearing in the receiver's account (broken financial invariant)",
                explanation="Without atomic rollback handling, partial failures in multi-step transactions lead to critical financial inconsistencies."
            ),
            QuizQuestionBlueprint(
                question="Why does `get_statement()` return `[dict(tx) for tx in self._ledger]` instead of returning `self._ledger` directly?",
                options=[
                    "It returns defensive copies so external callers cannot mutate or delete entries from the genuine internal ledger",
                    "Because Python cannot print lists",
                    "Because dictionaries take up less memory than lists",
                    "To encrypt the statement with a digital signature"
                ],
                correct_answer="It returns defensive copies so external callers cannot mutate or delete entries from the genuine internal ledger",
                explanation="Returning defensive copies preserves encapsulation and shields internal data structures from external modification."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 13: Intro to Inheritance (IS-A Relationship)
    # -------------------------------------------------------------
    DayBlueprint(
        order=13,
        title="Day 13: Intro to Inheritance (IS-A Relationship)",
        concept="The Second Pillar of OOP: Inheritance - modeling 'IS-A' hierarchies, parent/child relationships, and code reusability",
        analogy="Think of biological genetics: you inherited traits from your parents (like eye color and blood type), but you also have your own unique traits (like your choice of hairstyle or ability to play guitar). In programming, a `Car` is a vehicle, a `Truck` is a vehicle, and a `Motorcycle` is a vehicle. Rather than writing engine, wheels, and speedometer code 3 separate times, you define a parent `Vehicle` class once and let all child classes inherit those features automatically!",
        theory_sections=[
            {
                "heading": "The IS-A Relationship & Code Reusability",
                "body": "**Inheritance** allows a new class (**Child / Subclass / Derived Class**) to inherit the attributes and methods of an existing class (**Parent / Superclass / Base Class**).\n\nInheritance models the **IS-A** relationship:\n- A `Dog` IS-A `Mammal`.\n- A `SavingsAccount` IS-A `BankAccount`.\n- A `Manager` IS-A `Employee`.\n\nInheritance prevents code duplication (DRY principle: Don't Repeat Yourself). Common logic is written and tested once in the parent class; child classes specialize and extend that foundation."
            },
            {
                "heading": "Extending vs Overriding",
                "body": "When a subclass inherits from a superclass, it can:\n1. **Inherit Directly**: Use parent methods as-is without rewriting them.\n2. **Extend**: Add brand-new attributes and methods specific to the child class (e.g., `ElectricCar` adds `battery_capacity`).\n3. **Override**: Re-implement a parent method with specialized child behavior (e.g., `Dog` overrides `speak()` to say 'Woof' instead of generic sound)."
            }
        ],
        code_snippets=[
            {
                "title": "Basic Inheritance Syntax in Python: Parent and Child Classes",
                "language": "python",
                "code": "# Parent (Base) Class\nclass Vehicle:\n    def __init__(self, brand: str, speed: float = 0.0):\n        self.brand = brand\n        self.speed = speed\n\n    def accelerate(self, amount: float):\n        self.speed += amount\n        return f'{self.brand} accelerating to {self.speed} km/h'\n\n# Child (Derived) Class inheriting from Vehicle\nclass Bicycle(Vehicle):\n    def ring_bell(self):\n        return 'Ring ring!'\n\nbike = Bicycle('Schwinn')\n# Bicycle inherits accelerate() from Vehicle\nprint(bike.accelerate(15))\n# Bicycle uses its own unique method\nprint(bike.ring_bell())",
                "explanation": "Bicycle inherits all Vehicle attributes and methods while introducing ring_bell()."
            },
            {
                "title": "Verifying IS-A Relationships with isinstance and issubclass",
                "language": "python",
                "code": "print('Is bike an instance of Bicycle?', isinstance(bike, Bicycle))  # True\nprint('Is bike an instance of Vehicle?', isinstance(bike, Vehicle))  # True! IS-A\nprint('Is Bicycle a subclass of Vehicle?', issubclass(Bicycle, Vehicle))  # True\nprint('Is Vehicle a subclass of Bicycle?', issubclass(Vehicle, Bicycle))  # False",
                "explanation": "isinstance and issubclass confirm the hierarchical IS-A relationship."
            },
            {
                "title": "Extending Attributes in a Subclass",
                "language": "python",
                "code": "class ElectricCar(Vehicle):\n    def __init__(self, brand: str, battery_kwh: float):\n        super().__init__(brand)  # Initialize parent state\n        self.battery_kwh = battery_kwh  # Child-specific state\n\n    def charge(self):\n        return f'Charging {self.battery_kwh} kWh battery...'\n\ntesla = ElectricCar('Tesla Model 3', 75.0)\nprint(tesla.accelerate(50))\nprint(tesla.charge())",
                "explanation": "ElectricCar extends Vehicle with battery_kwh and charge() behavior."
            },
            {
                "title": "Python Script: Inspecting Class MRO (Method Resolution Order)",
                "language": "python",
                "code": "print('Bicycle inheritance lineage:', Bicycle.__mro__)\n# Output: (Bicycle, Vehicle, object)\n# Note: In Python 3, all classes ultimately inherit from the base 'object' class!",
                "explanation": "Reveals the Method Resolution Order (MRO) showing the lineage back to the root object class."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Animal and Dog Inheritance Hierarchy",
            description="Create a base class `Animal` with attribute `name` and method `eat()` returning `f'{self.name} is eating.'`. Create a derived class `Dog` that inherits from `Animal`, adds attribute `breed`, and implements `bark()` returning `f'{self.name} the {self.breed} barks: Woof!'`.",
            starter_code="class Animal:\n    # Implement Animal\n    pass\n\nclass Dog(Animal):\n    # Implement Dog inheriting Animal\n    pass",
            solution_code="class Animal:\n    def __init__(self, name: str):\n        self.name = name\n\n    def eat(self) -> str:\n        return f'{self.name} is eating.'\n\nclass Dog(Animal):\n    def __init__(self, name: str, breed: str):\n        super().__init__(name)\n        self.breed = breed\n\n    def bark(self) -> str:\n        return f'{self.name} the {self.breed} barks: Woof!'",
            expected_output="Buddy is eating.\nBuddy the Golden Retriever barks: Woof!"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What fundamental relationship does Inheritance model between classes?",
                options=[
                    "The 'IS-A' relationship (e.g., a Dog IS-A Animal, a Car IS-A Vehicle)",
                    "The 'HAS-A' relationship (e.g., a Car HAS-A Engine)",
                    "The 'RUNS-ON' relationship",
                    "The 'COMPILED-BY' relationship"
                ],
                correct_answer="The 'IS-A' relationship (e.g., a Dog IS-A Animal, a Car IS-A Vehicle)",
                explanation="Inheritance models the IS-A relationship, where a derived class is a specialized subtype of the base class."
            ),
            QuizQuestionBlueprint(
                question="What is the primary engineering benefit of using Inheritance in large software systems?",
                options=[
                    "Code reusability and eliminating duplication by sharing common state and behavior in a parent class",
                    "Eliminating the need to allocate memory for variables",
                    "Preventing other programmers from reading code",
                    "Doubling the speed of network requests"
                ],
                correct_answer="Code reusability and eliminating duplication by sharing common state and behavior in a parent class",
                explanation="Inheritance centralizes shared logic in base classes, ensuring bug fixes and updates propagate to all subclasses automatically."
            ),
            QuizQuestionBlueprint(
                question="In Python 3, what is the ultimate root base class from which all classes implicitly inherit?",
                options=[
                    "object",
                    "base",
                    "root",
                    "Class"
                ],
                correct_answer="object",
                explanation="In Python 3, every class automatically inherits from the built-in `object` class at the top of the hierarchy."
            ),
            QuizQuestionBlueprint(
                question="If class `Car` inherits from class `Vehicle`, what does `isinstance(my_car, Vehicle)` return?",
                options=[
                    "True",
                    "False",
                    "None",
                    "TypeError"
                ],
                correct_answer="True",
                explanation="Because a Car IS-A Vehicle, any Car instance is also recognized as an instance of Vehicle."
            ),
            QuizQuestionBlueprint(
                question="What built-in Python function checks if one class is a subclass of another class?",
                options=[
                    "issubclass(Child, Parent)",
                    "isinstance(Child, Parent)",
                    "hasparent(Child, Parent)",
                    "inherits_from(Child, Parent)"
                ],
                correct_answer="issubclass(Child, Parent)",
                explanation="`issubclass(sub, sup)` returns True if class `sub` is derived from class `sup`."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 14: Single & Multilevel Inheritance
    # -------------------------------------------------------------
    DayBlueprint(
        order=14,
        title="Day 14: Single & Multilevel Inheritance",
        concept="Inheritance Structures: Single inheritance (A -> B) and Multilevel inheritance chains (A -> B -> C), propagation of state and methods",
        analogy="Think of biological family ancestry: **Single Inheritance** is like a mother passing down traits to her daughter. **Multilevel Inheritance** is a family generational tree: your Grandfather passes traits to your Father, and your Father passes traits to You! You inherit your Grandfather's height, your Father's eye color, and you develop your own musical talent. The further down the chain you go, the more specialized you become!",
        theory_sections=[
            {
                "heading": "Single Inheritance",
                "body": "**Single Inheritance** occurs when a subclass derives from exactly **one** direct parent class (`Class B(A)`). It is the simplest and safest form of inheritance, maintaining a clean 1-to-1 hierarchy free from naming ambiguities."
            },
            {
                "heading": "Multilevel Inheritance Chains",
                "body": "**Multilevel Inheritance** forms an ancestor chain where a class inherits from a parent that is itself a child of another class (`Class C(B)` where `Class B(A)`).\n\nIn this chain:\n- Class `A` is the Grandparent (root base class).\n- Class `B` inherits from `A` and adds its own features.\n- Class `C` inherits from `B`, automatically receiving the cumulative features of both `A` and `B`.\n\nEvery level down the chain represents greater specialization (e.g., `LivingThing` -> `Animal` -> `Mammal` -> `Dog` -> `GoldenRetriever`)."
            }
        ],
        code_snippets=[
            {
                "title": "Single Inheritance Example",
                "language": "python",
                "code": "class Device:\n    def __init__(self, brand: str):\n        self.brand = brand\n    def power_on(self):\n        return f'{self.brand} device powered ON.'\n\n# Single Inheritance: Phone derives from Device\nclass Phone(Device):\n    def make_call(self, number: str):\n        return f'Calling {number} from {self.brand} phone...'\n\np = Phone('Google Pixel')\nprint(p.power_on())   # Inherited from Device\nprint(p.make_call('555-0199'))",
                "explanation": "Phone inherits directly from Device in a clean single-inheritance model."
            },
            {
                "title": "Multilevel Inheritance Chain: LivingThing -> Animal -> Dog",
                "language": "python",
                "code": "# Level 1: Grandparent\nclass LivingThing:\n    def __init__(self, species: str):\n        self.species = species\n    def breathe(self):\n        return f'{self.species} is respiring oxygen.'\n\n# Level 2: Parent\nclass Animal(LivingThing):\n    def __init__(self, species: str, can_move: bool = True):\n        super().__init__(species)\n        self.can_move = can_move\n    def move(self):\n        return f'{self.species} is moving!'\n\n# Level 3: Child inheriting cumulatively from Animal and LivingThing\nclass Dog(Animal):\n    def __init__(self, name: str):\n        super().__init__(species='Canis lupus')\n        self.name = name\n    def bark(self):\n        return f'{self.name} says Woof!'",
                "explanation": "Dog inherits from Animal, which inherits from LivingThing."
            },
            {
                "title": "Testing Cumulative Inheritance Down the Chain",
                "language": "python",
                "code": "rex = Dog('Rex')\n# Method from Grandparent (LivingThing):\nprint(rex.breathe())\n# Method from Parent (Animal):\nprint(rex.move())\n# Method from Child (Dog):\nprint(rex.bark())\n\nprint('Is rex a LivingThing?', isinstance(rex, LivingThing))  # True!",
                "explanation": "The grandchild instance can invoke methods defined across all ancestor levels."
            },
            {
                "title": "Visualizing the Inheritance Chain MRO",
                "language": "python",
                "code": "for index, cls in enumerate(Dog.__mro__):\n    print(f'MRO Step {index}: {cls.__name__}')\n# Output: Dog -> Animal -> LivingThing -> object",
                "explanation": "Python traverses the inheritance chain upwards in strict order."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Three-Tier Multilevel Employee Hierarchy",
            description="Create a 3-tier multilevel inheritance chain:\n1. Base class `Person` with attribute `name`.\n2. Subclass `Employee(Person)` adding `salary: float`.\n3. Subclass `Executive(Employee)` adding `stock_options: int` and a method `get_total_compensation()` returning `salary + (stock_options * 50)`.",
            starter_code="class Person:\n    pass\n\nclass Employee(Person):\n    pass\n\nclass Executive(Employee):\n    pass",
            solution_code="class Person:\n    def __init__(self, name: str):\n        self.name = name\n\nclass Employee(Person):\n    def __init__(self, name: str, salary: float):\n        super().__init__(name)\n        self.salary = float(salary)\n\nclass Executive(Employee):\n    def __init__(self, name: str, salary: float, stock_options: int):\n        super().__init__(name, salary)\n        self.stock_options = int(stock_options)\n\n    def get_total_compensation(self) -> float:\n        return self.salary + (self.stock_options * 50.0)",
            expected_output="CEO Alice compensation: 250000.0"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What characterizes Multilevel Inheritance?",
                options=[
                    "A class inherits from a parent class that is itself a derived child of another ancestor class (e.g. C derives from B, and B derives from A)",
                    "A class inherits from 10 different unrelated classes simultaneously",
                    "A class that cannot have any methods or variables",
                    "A class that runs on multiple computers over the network"
                ],
                correct_answer="A class inherits from a parent class that is itself a derived child of another ancestor class (e.g. C derives from B, and B derives from A)",
                explanation="Multilevel inheritance forms a generational chain where each child inherits the cumulative traits of all ancestors."
            ),
            QuizQuestionBlueprint(
                question="If class `C` inherits from `B`, and `B` inherits from `A`, which methods can an instance of `C` access?",
                options=[
                    "All public and protected methods defined across classes A, B, and C",
                    "Only methods defined inside C",
                    "Only methods defined inside A and C, but not B",
                    "None, inheritance stops at level 2"
                ],
                correct_answer="All public and protected methods defined across classes A, B, and C",
                explanation="The lowest child in a multilevel hierarchy inherits the cumulative sum of public and protected members from all ancestor classes."
            ),
            QuizQuestionBlueprint(
                question="What is a potential architectural risk of creating deeply nested multilevel inheritance chains (e.g. 8+ levels deep)?",
                options=[
                    "Fragile Base Class problem: changes to high-level ancestors can unpredictably break distant subclasses down the tree",
                    "The operating system running out of file handles",
                    "Python automatically converting variables to null",
                    "The code becoming impossible to compile on Tuesdays"
                ],
                correct_answer="Fragile Base Class problem: changes to high-level ancestors can unpredictably break distant subclasses down the tree",
                explanation="Deep inheritance trees create tight coupling where modifying a root class can inadvertently break child classes many levels removed."
            ),
            QuizQuestionBlueprint(
                question="What does the built-in attribute `__mro__` represent on a Python class?",
                options=[
                    "Method Resolution Order: the tuple of classes searched when looking up a method or attribute",
                    "Memory Relocation Offset",
                    "Multi-threading Resource Object",
                    "Module Reference Origin"
                ],
                correct_answer="Method Resolution Order: the tuple of classes searched when looking up a method or attribute",
                explanation="MRO defines the exact sequential order Python searches through ancestor classes when resolving attributes and methods."
            ),
            QuizQuestionBlueprint(
                question="What is the difference between Single Inheritance and Multilevel Inheritance?",
                options=[
                    "Single inheritance has only one parent-child tier (A -> B); Multilevel inheritance chains multiple parent-child tiers (A -> B -> C)",
                    "Single inheritance only works with integers, while Multilevel works with strings",
                    "Single inheritance is forbidden in Python",
                    "Multilevel inheritance requires using C++"
                ],
                correct_answer="Single inheritance has only one parent-child tier (A -> B); Multilevel inheritance chains multiple parent-child tiers (A -> B -> C)",
                explanation="Single inheritance involves a direct child of one parent, while multilevel involves successive generations of inheritance."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 15: Hierarchical & Hybrid Inheritance
    # -------------------------------------------------------------
    DayBlueprint(
        order=15,
        title="Day 15: Hierarchical & Hybrid Inheritance",
        concept="Complex Inheritance Taxonomies: Hierarchical inheritance (one parent with multiple children) and Hybrid inheritance architectures",
        analogy="Think of a car company manufacturing vehicles from a single master chassis blueprint: from one `Vehicle` blueprint, the factory produces Sedans, SUVs, and Pickup Trucks (**Hierarchical Inheritance**). Now imagine an ultra-modern autonomous flying car: it inherits ground-driving systems from an electric car and aerial flight systems from an airplane drone (**Hybrid Inheritance**). Trees can branch out, and branches can recombine!",
        theory_sections=[
            {
                "heading": "Hierarchical Inheritance: One Parent, Many Children",
                "body": "**Hierarchical Inheritance** occurs when multiple distinct subclasses derive from a single common parent class:\n```\n        [ BankAccount ]\n        /             \\\n [ SavingsAccount ]  [ CheckingAccount ]\n```\nBoth `SavingsAccount` and `CheckingAccount` share common banking logic (deposit, balance tracking) from `BankAccount`, but specialize independently:\n- `SavingsAccount` adds interest rate compounding.\n- `CheckingAccount` adds overdraft fee protection."
            },
            {
                "heading": "Hybrid Inheritance: Combining Paradigms",
                "body": "**Hybrid Inheritance** combines two or more different inheritance types (such as combining Multilevel and Hierarchical, or Hierarchical with Multiple inheritance).\n\nWhile powerful for modeling complex domain taxonomies (such as UI component trees or game entity frameworks), hybrid hierarchies must be architected carefully to prevent the infamous **Diamond Problem** (which we will master tomorrow)."
            }
        ],
        code_snippets=[
            {
                "title": "Hierarchical Inheritance: BankAccount Branching into Savings & Checking",
                "language": "python",
                "code": "class BankAccount:\n    def __init__(self, owner: str, balance: float):\n        self.owner = owner\n        self.balance = balance\n    def deposit(self, amount: float):\n        self.balance += amount\n        return self.balance\n\n# Branch 1: SavingsAccount specializes with interest\nclass SavingsAccount(BankAccount):\n    def apply_interest(self, rate: float = 0.05):\n        interest = self.balance * rate\n        self.balance += interest\n        return f'Applied ${interest:.2f} interest.'\n\n# Branch 2: CheckingAccount specializes with overdraft limit\nclass CheckingAccount(BankAccount):\n    def __init__(self, owner: str, balance: float, overdraft_limit: float = 100.0):\n        super().__init__(owner, balance)\n        self.overdraft_limit = overdraft_limit",
                "explanation": "Two independent child classes branch off from a single shared parent class."
            },
            {
                "title": "Testing Independent Sibling Behavior in Hierarchical Trees",
                "language": "python",
                "code": "sav = SavingsAccount('Alice', 1000.0)\nchk = CheckingAccount('Bob', 500.0, overdraft_limit=200.0)\n\nprint(sav.apply_interest())\nprint(f'{chk.owner} checking overdraft limit: ${chk.overdraft_limit}')\n\n# Siblings share parent type, but not sibling types\nprint('Is sav a BankAccount?', isinstance(sav, BankAccount))      # True\nprint('Is sav a CheckingAccount?', isinstance(sav, CheckingAccount))  # False!",
                "explanation": "Siblings share their parent's interface but do not inherit each other's specialized methods."
            },
            {
                "title": "Hybrid Inheritance Example: Device -> Computer -> Laptop & Server",
                "language": "python",
                "code": "class Device:\n    def get_power_status(self): return 'Powered ON'\n\nclass Computer(Device):  # Multilevel step\n    def compute(self): return 'Processing instructions'\n\n# Hierarchical branches from Computer\nclass Laptop(Computer):\n    def get_battery(self): return 'Battery: 85%'\n\nclass Server(Computer):\n    def get_rack_unit(self): return 'Rack Unit: 2U'\n\nmacbook = Laptop()\nprint(macbook.get_power_status())  # From Device\nprint(macbook.compute())           # From Computer\nprint(macbook.get_battery())       # From Laptop",
                "explanation": "Combines multilevel inheritance (Device -> Computer) with hierarchical branching (Laptop & Server)."
            },
            {
                "title": "Python Script: Introspecting Subclasses of a Base Class",
                "language": "python",
                "code": "# Python can discover all direct child branches dynamically:\nsubclasses = BankAccount.__subclasses__()\nprint('Discovered BankAccount subclasses:', [cls.__name__ for cls in subclasses])",
                "explanation": "The __subclasses__() hook discovers all active subclasses branching from a base class."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Hierarchical UI Element Hierarchy",
            description="Create a base class `UIElement` with attributes `x: int` and `y: int`. Create two hierarchical child classes:\n1. `Button` adding attribute `label: str` and method `click()` returning `f'Button {self.label} clicked at ({self.x}, {self.y})'`.\n2. `TextBox` adding attribute `text: str` and method `input_text(new_text: str)` appending to `self.text`.",
            starter_code="class UIElement:\n    pass\n\nclass Button(UIElement):\n    pass\n\nclass TextBox(UIElement):\n    pass",
            solution_code="class UIElement:\n    def __init__(self, x: int, y: int):\n        self.x = int(x)\n        self.y = int(y)\n\nclass Button(UIElement):\n    def __init__(self, x: int, y: int, label: str):\n        super().__init__(x, y)\n        self.label = label\n\n    def click(self) -> str:\n        return f'Button {self.label} clicked at ({self.x}, {self.y})'\n\nclass TextBox(UIElement):\n    def __init__(self, x: int, y: int, initial_text: str = ''):\n        super().__init__(x, y)\n        self.text = initial_text\n\n    def input_text(self, new_text: str):\n        self.text += new_text",
            expected_output="Button Submit clicked at (10, 20)\nHello World"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What defines Hierarchical Inheritance?",
                options=[
                    "Multiple distinct subclasses inherit from a single common parent class",
                    "A class inherits from multiple parents simultaneously",
                    "A class that cannot be inherited from",
                    "A class with no methods"
                ],
                correct_answer="Multiple distinct subclasses inherit from a single common parent class",
                explanation="Hierarchical inheritance occurs when two or more child classes share the same parent class."
            ),
            QuizQuestionBlueprint(
                question="In a Hierarchical inheritance tree where `SavingsAccount` and `CheckingAccount` inherit from `BankAccount`, can a `SavingsAccount` instance call `CheckingAccount`'s methods?",
                options=[
                    "No, sibling classes do not inherit from each other",
                    "Yes, siblings automatically share all methods",
                    "Only if they have the same account balance",
                    "Only if the program is run on Linux"
                ],
                correct_answer="No, sibling classes do not inherit from each other",
                explanation="Sibling classes in a hierarchy are independent branches; they inherit from their parent, not from each other."
            ),
            QuizQuestionBlueprint(
                question="What is Hybrid Inheritance?",
                options=[
                    "A composite architecture combining two or more distinct inheritance forms (such as multilevel and hierarchical)",
                    "Inheritance that runs on gasoline and battery power",
                    "Inheritance that only works on virtual machines",
                    "Inheriting code from an external Python library"
                ],
                correct_answer="A composite architecture combining two or more distinct inheritance forms (such as multilevel and hierarchical)",
                explanation="Hybrid inheritance combines multiple structural patterns, such as chaining multilevel tiers with hierarchical branches."
            ),
            QuizQuestionBlueprint(
                question="Which built-in Python method returns a list of all immediate subclasses currently registered to a parent class?",
                options=[
                    "BaseClass.__subclasses__()",
                    "BaseClass.get_children()",
                    "BaseClass.__children__",
                    "BaseClass.subclass_list()"
                ],
                correct_answer="BaseClass.__subclasses__()",
                explanation="`ParentClass.__subclasses__()` inspects the runtime memory and returns all active direct derived classes."
            ),
            QuizQuestionBlueprint(
                question="Why is Hierarchical Inheritance widely used in Graphical User Interface (GUI) frameworks (like HTML DOM, React Native, or Qt)?",
                options=[
                    "Because hundreds of specific UI controls (Button, Checkbox, Slider, Label) all share common base properties (x, y coordinates, width, height, visibility)",
                    "Because buttons cannot be clicked without inheritance",
                    "Because GUI frameworks are written in procedural assembly code",
                    "Because monitors require hierarchical pixels"
                ],
                correct_answer="Because hundreds of specific UI controls (Button, Checkbox, Slider, Label) all share common base properties (x, y coordinates, width, height, visibility)",
                explanation="GUI components naturally branch hierarchically from a common base UIElement/View sharing bounding boxes, coordinates, and event listeners."
            )
        ]
    )
]
