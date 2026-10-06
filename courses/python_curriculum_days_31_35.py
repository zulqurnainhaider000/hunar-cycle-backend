"""
Days 31 to 35 of Python Mastery (35 Days)
Includes:
- Day 35 Capstone Project: Personal Finance & Expense Tracker CLI
"""

from seeder.course_blueprint import DayBlueprint, QuizQuestionBlueprint, CodingChallengeBlueprint

DAYS_31_TO_35 = [
    # -------------------------------------------------------------
    # DAY 31
    # -------------------------------------------------------------
    DayBlueprint(
        order=31,
        title="Day 31: OOP Inheritance & super() Polymorphism",
        concept="Reusing base class behaviors, extending child subclasses, and overriding methods",
        analogy="Think of biological genetics! A child inherits baseline human traits like having two eyes and breathing air from their parents (Base Class). But the child can also specialize to become an Olympic gymnast or concert pianist (Child Subclass), adding brand-new skills without re-evolving the human heart!",
        theory_sections=[
            {
                "heading": "Base Classes and Derived Subclasses",
                "body": "Inheritance allows a child class to inherit all attributes and methods of a parent class using the syntax `class Child(Parent):`. This promotes code reuse and models hierarchical relationships (e.g. `Developer` is a kind of `Employee`)."
            },
            {
                "heading": "Method Overriding and super()",
                "body": "A subclass can replace (override) a parent method by redefining it with the same name. Using `super().method_name()` allows the child to call the parent's original implementation before extending it with customized behavior."
            }
        ],
        code_snippets=[
            {
                "title": "Basic Inheritance Structure",
                "code": "class Animal:\n    def __init__(self, name: str):\n        self.name = name\n    def speak(self):\n        return 'Generic animal sound'\n\nclass Dog(Animal):\n    def speak(self):\n        return f'{self.name} says: Woof! Woof!'\n\nclass Cat(Animal):\n    def speak(self):\n        return f'{self.name} says: Meow!'\n\npets = [Dog('Buddy'), Cat('Luna')]\nfor p in pets:\n    print(p.speak())"
            },
            {
                "title": "Extending Parent Constructor with super()",
                "code": "class User:\n    def __init__(self, username: str, email: str):\n        self.username = username\n        self.email = email\n        \nclass Admin(User):\n    def __init__(self, username: str, email: str, permissions: list):\n        super().__init__(username, email) # Initialize base attributes\n        self.permissions = permissions\n        \nadmin = Admin('superuser', 'admin@hunar.com', ['READ', 'WRITE', 'DELETE'])\nprint(f'{admin.username} ({admin.email}) has permissions: {admin.permissions}')"
            },
            {
                "title": "Polymorphism Across Heterogeneous Objects",
                "code": "class Shape:\n    def area(self):\n        raise NotImplementedError()\n\nclass Rectangle(Shape):\n    def __init__(self, w, h): self.w, self.h = w, h\n    def area(self): return self.w * self.h\n\nclass Circle(Shape):\n    def __init__(self, r): self.r = r\n    def area(self): return 3.14159 * (self.r ** 2)\n\nshapes = [Rectangle(10, 5), Circle(4)]\nfor s in shapes:\n    print(f'{type(s).__name__} Area: {s.area():.2f}')"
            },
            {
                "title": "Checking Class Hierarchy with issubclass() and isinstance()",
                "code": "print('Is Dog a subclass of Animal?', issubclass(Dog, Animal))\nprint('Is Dog an instance of Animal?', isinstance(Dog('Rex'), Animal))"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Create a Manager Subclass",
            description="Create a base class `Employee(name, salary)` and a subclass `Manager(name, salary, bonus)` that inherits from `Employee` using `super()`. Add a method `total_compensation()` that returns `salary + bonus`. Test with salary 80000, bonus 15000 and print: 'Manager Pay: $95000'.",
            starter_code="# TODO: Implement Employee and Manager classes\n",
            solution_code="class Employee:\n    def __init__(self, name, salary):\n        self.name = name\n        self.salary = salary\n\nclass Manager(Employee):\n    def __init__(self, name, salary, bonus):\n        super().__init__(name, salary)\n        self.bonus = bonus\n    def total_compensation(self):\n        return self.salary + self.bonus\n\nmgr = Manager('Alice', 80000, 15000)\nprint(f'Manager Pay: ${mgr.total_compensation()}')",
            expected_output="Manager Pay: $95000"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What built-in function is used to invoke methods of the parent superclass?",
                options=["super()", "parent()", "base()", "root()"],
                correct_answer="super()",
                explanation="`super()` returns a proxy object delegating method calls to a parent or sibling class."
            ),
            QuizQuestionBlueprint(
                question="What is 'polymorphism' in OOP?",
                options=[
                    "The ability of different classes to respond to the same method interface in their own unique way.",
                    "Creating multiple classes in a single file.",
                    "Converting classes to byte arrays.",
                    "Translating Python into C."
                ],
                correct_answer="The ability of different classes to respond to the same method interface in their own unique way.",
                explanation="Polymorphism lets code treat different objects uniformly through a shared interface."
            ),
            QuizQuestionBlueprint(
                question="How do you declare that class SavingsAccount inherits from class Account?",
                options=["class SavingsAccount(Account):", "class SavingsAccount extends Account:", "class SavingsAccount : Account", "class SavingsAccount inherits Account:"],
                correct_answer="class SavingsAccount(Account):",
                explanation="In Python, base classes are enclosed in parentheses after the subclass name."
            ),
            QuizQuestionBlueprint(
                question="What does issubclass(Child, Parent) return?",
                options=[
                    "True if Child is a direct or indirect subclass of Parent; False otherwise.",
                    "The number of subclasses.",
                    "A tuple of methods.",
                    "An instance of Child."
                ],
                correct_answer="True if Child is a direct or indirect subclass of Parent; False otherwise.",
                explanation="`issubclass()` checks if a class is derived from another class."
            ),
            QuizQuestionBlueprint(
                question="Can a Python class inherit from more than one parent class (Multiple Inheritance)?",
                options=[
                    "Yes, Python natively supports Multiple Inheritance using Method Resolution Order (MRO).",
                    "No, Python strictly allows single inheritance only like Java.",
                    "Only with interfaces.",
                    "Only when using decorators."
                ],
                correct_answer="Yes, Python natively supports Multiple Inheritance using Method Resolution Order (MRO).",
                explanation="Python supports multiple inheritance, resolving lookups via C3 Linearization (MRO)."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 32
    # -------------------------------------------------------------
    DayBlueprint(
        order=32,
        title="Day 32: OOP Magic (Dunder) Methods",
        concept="Customizing Python language protocols using double-underscore hooks (__str__, __len__, __eq__)",
        analogy="Think of a universal TV remote control! It has buttons for Power, Volume Up (+), and Mute. When you press '+', the remote doesn't care whether you own a Sony, Samsung, or LG television—each TV knows how to respond to '+'. That's what Dunder methods do: they let your custom classes respond to Python's universal operators!",
        theory_sections=[
            {
                "heading": "What are Dunder Methods?",
                "body": "Dunder (Double Underscore) or 'magic' methods are special hooks predefined by Python that start and end with two underscores (e.g. `__str__`, `__len__`, `__eq__`, `__add__`). You don't call them directly like `obj.__len__()`; instead, Python invokes them automatically when you use built-in functions or operators like `len(obj)` or `obj1 + obj2`."
            },
            {
                "heading": "Essential Dunders",
                "body": "- `__str__`: Returns an informal, user-friendly string representation for `print()`.\n- `__repr__`: Returns an unambiguous technical representation for debugging.\n- `__len__`: Hook for `len()`.\n- `__eq__`: Hook for `==` equality testing.\n- `__add__`: Hook for the `+` operator (Operator Overloading)."
            }
        ],
        code_snippets=[
            {
                "title": "Implementing __str__ and __repr__",
                "code": "class Book:\n    def __init__(self, title: str, author: str, pages: int):\n        self.title = title\n        self.author = author\n        self.pages = pages\n    \n    def __str__(self):\n        return f'\"{self.title}\" by {self.author}'\n        \n    def __repr__(self):\n        return f'Book(title=\"{self.title}\", author=\"{self.author}\", pages={self.pages})'\n\nbook = Book('Fluent Python', 'Luciano Ramalho', 790)\nprint('Using __str__ via print:', book)\nprint('Using __repr__:', repr(book))"
            },
            {
                "title": "Supporting len() with __len__",
                "code": "class Playlist:\n    def __init__(self, name):\n        self.name = name\n        self.tracks = []\n    def add_track(self, title): self.tracks.append(title)\n    def __len__(self):\n        return len(self.tracks)\n\npl = Playlist('Coding Beats')\npl.add_track('Lo-Fi Coding')\npl.add_track('Synthwave Study')\nprint('Total tracks in playlist:', len(pl))"
            },
            {
                "title": "Operator Overloading: __add__ for Vector Math",
                "code": "class Vector2D:\n    def __init__(self, x, y): self.x, self.y = x, y\n    def __add__(self, other):\n        return Vector2D(self.x + other.x, self.y + other.y)\n    def __repr__(self):\n        return f'Vector2D({self.x}, {self.y})'\n\nv1 = Vector2D(3, 4)\nv2 = Vector2D(1, 2)\nv3 = v1 + v2\nprint('Vector Addition Result:', v3)"
            },
            {
                "title": "Equality Comparison with __eq__",
                "code": "class Coordinate:\n    def __init__(self, x, y): self.x, self.y = x, y\n    def __eq__(self, other):\n        return isinstance(other, Coordinate) and self.x == other.x and self.y == other.y\n\nprint('c1 == c2:', Coordinate(5, 5) == Coordinate(5, 5))\nprint('c1 == c3:', Coordinate(5, 5) == Coordinate(5, 10))"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Implement Money Class with Addition Overloading",
            description="Create a `Money(amount)` class that implements `__add__` to combine amounts, and `__str__` to display `$amount.00`. Test adding $25 and $40, and print: 'Combined: $65.00'.",
            starter_code="# TODO: Implement Money class with __add__ and __str__\n",
            solution_code="class Money:\n    def __init__(self, amount):\n        self.amount = float(amount)\n    def __add__(self, other):\n        return Money(self.amount + other.amount)\n    def __str__(self):\n        return f'${self.amount:.2f}'\n\nm1 = Money(25)\nm2 = Money(40)\nprint('Combined:', m1 + m2)",
            expected_output="Combined: $65.00"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Which magic method is called when an object is passed to print() or str()?",
                options=["__str__", "__repr__", "__display__", "__print__"],
                correct_answer="__str__",
                explanation="`__str__` defines the human-readable string representation of an object."
            ),
            QuizQuestionBlueprint(
                question="What method must a class define to allow calling the built-in len() function on its instances?",
                options=["__len__", "__size__", "__count__", "__length__"],
                correct_answer="__len__",
                explanation="`len(obj)` invokes `obj.__len__()`, which must return a non-negative integer."
            ),
            QuizQuestionBlueprint(
                question="What is 'Operator Overloading' in Python?",
                options=[
                    "Providing custom implementations for standard operators (like +, ==, *) using magic methods.",
                    "Writing too many operators on a single line of code.",
                    "Overriding CPU memory registers.",
                    "Compiling operators in C."
                ],
                correct_answer="Providing custom implementations for standard operators (like +, ==, *) using magic methods.",
                explanation="Operator overloading allows custom classes to define how operators like + or == behave."
            ),
            QuizQuestionBlueprint(
                question="Which method overrides the equality operator (==)?",
                options=["__eq__", "__equals__", "__same__", "__cmp__"],
                correct_answer="__eq__",
                explanation="`a == b` triggers `a.__eq__(b)`."
            ),
            QuizQuestionBlueprint(
                question="What is the conventional goal of the __repr__ method?",
                options=[
                    "To return an unambiguous string that ideally looks like valid Python code to recreate the object.",
                    "To print in full color.",
                    "To export the object to HTML.",
                    "To compress the object into binary."
                ],
                correct_answer="To return an unambiguous string that ideally looks like valid Python code to recreate the object.",
                explanation="`__repr__` is meant for developers and should provide unambiguous reconstruction information."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 33
    # -------------------------------------------------------------
    DayBlueprint(
        order=33,
        title="Day 33: Working with JSON Data & API Payloads",
        concept="Serialization, deserialization, json.dumps(), and json.loads() for web APIs",
        analogy="Think of JSON like flat-packed IKEA furniture! When you buy a desk, you don't transport the giant 3D wooden desk in your tiny car trunk. IKEA disassembles it into a flat cardboard box with instructions (Serialization: `dumps`). When you get home, you assemble the flat pack back into a real 3D desk (Deserialization: `loads`)!",
        theory_sections=[
            {
                "heading": "Why JSON?",
                "body": "JSON (JavaScript Object Notation) is the universal lingua franca of the modern web and REST APIs. Every mobile app, web frontend, and cloud service transmits data over HTTP in JSON format."
            },
            {
                "heading": "Serialization vs Deserialization in Python",
                "body": "- **Serialization (`dumps` / `dump`)**: Converting in-memory Python objects (dicts, lists) into a serialized JSON string or file stream.\n- **Deserialization (`loads` / `load`)**: Parsing a raw JSON string or file stream back into native Python dictionaries and lists.\n(Note: 's' in `loads`/`dumps` stands for String!)."
            }
        ],
        code_snippets=[
            {
                "title": "Python Dict to JSON String (json.dumps)",
                "code": "import json\n\nuser_data = {\n    'user_id': 1001,\n    'username': 'bilalkhan',\n    'is_verified': True,\n    'skills': ['Python', 'Django', 'PostgreSQL'],\n    'rating': 4.95\n}\n\n# Convert to formatted JSON string\njson_string = json.dumps(user_data, indent=2)\nprint('Serialized JSON String:\\n' + json_string)"
            },
            {
                "title": "JSON String to Python Dict (json.loads)",
                "code": "raw_payload = '{\"status\": 200, \"message\": \"OK\", \"data\": [\"Item A\", \"Item B\"]}'\nparsed = json.loads(raw_payload)\nprint('Parsed type:', type(parsed).__name__)\nprint('Status:', parsed['status'])\nprint('Items count:', len(parsed['data']))"
            },
            {
                "title": "Saving & Loading JSON Directly to Disk (dump / load)",
                "code": "config_payload = {'theme': 'dark', 'notifications': True, 'refresh_rate': 60}\n\n# Writing to disk\nwith open('app_settings.json', 'w') as f:\n    json.dump(config_payload, f, indent=4)\n    \n# Reading back from disk\nwith open('app_settings.json', 'r') as f:\n    loaded_settings = json.load(f)\n    \nprint('Loaded settings from disk:', loaded_settings)"
            },
            {
                "title": "Handling Unsupported Types with default serializer",
                "code": "from datetime import datetime\n\nevent = {'title': 'Graduation', 'date': datetime.now()}\n# Providing default=str converts datetime objects to ISO strings\nserialized = json.dumps(event, default=str)\nprint('Serialized with datetime:', serialized)"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Parse JSON API Response",
            description="Given `payload = '{\"users\": [{\"id\": 1, \"active\": true}, {\"id\": 2, \"active\": false}, {\"id\": 3, \"active\": true}]}'`. Parse the JSON string and count how many users have `active == True`. Print: 'Active Users: 2'.",
            starter_code="payload = '{\"users\": [{\"id\": 1, \"active\": true}, {\"id\": 2, \"active\": false}, {\"id\": 3, \"active\": true}]}'\n# TODO: Parse and count active users\n",
            solution_code="import json\npayload = '{\"users\": [{\"id\": 1, \"active\": true}, {\"id\": 2, \"active\": false}, {\"id\": 3, \"active\": true}]}'\ndata = json.loads(payload)\nactive_count = sum(1 for u in data['users'] if u['active'])\nprint('Active Users:', active_count)",
            expected_output="Active Users: 2"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the difference between json.dumps() and json.dump()?",
                options=[
                    "dumps() serializes to a string; dump() writes directly to a file stream.",
                    "dumps() is for arrays; dump() is for dictionaries.",
                    "dumps() is encrypted; dump() is plaintext.",
                    "There is no difference."
                ],
                correct_answer="dumps() serializes to a string; dump() writes directly to a file stream.",
                explanation="The 's' in `dumps` and `loads` signifies operating on Python Strings."
            ),
            QuizQuestionBlueprint(
                question="What data type does json.loads() return when given a valid JSON object string?",
                options=["A Python dictionary (dict)", "A Python list", "A raw bytearray", "A string"],
                correct_answer="A Python dictionary (dict)",
                explanation="A JSON object (`{...}`) deserializes directly into a native Python `dict`."
            ),
            QuizQuestionBlueprint(
                question="How does JSON represent Python's boolean True and None values?",
                options=[
                    "true (lowercase) and null",
                    "True and None",
                    "1 and 0",
                    "TRUE and NIL"
                ],
                correct_answer="true (lowercase) and null",
                explanation="JSON standard uses lowercase `true`, `false`, and `null`."
            ),
            QuizQuestionBlueprint(
                question="What exception is raised if json.loads() encounters malformed or invalid JSON text?",
                options=["json.JSONDecodeError", "ValueError", "MalformedTextError", "SyntaxError"],
                correct_answer="json.JSONDecodeError",
                explanation="`json.JSONDecodeError` (which inherits from `ValueError`) is raised on parsing failures."
            ),
            QuizQuestionBlueprint(
                question="What argument in json.dumps(data, indent=4) makes the output human-readable?",
                options=["indent=4", "format=True", "pretty=4", "readable=True"],
                correct_answer="indent=4",
                explanation="The `indent` argument specifies indentation spacing for pretty-printing."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 34
    # -------------------------------------------------------------
    DayBlueprint(
        order=34,
        title="Day 34: Standard Library & OS System Operations",
        concept="Batteries-included standard modules: os, sys, pathlib, math, and datetime",
        analogy="Think of Python's standard library like a fully loaded Swiss Army knife! When you install Python, you don't just get a blade; you get scissors, a magnifying glass, a compass, and a corkscrew ready in your pocket without having to buy external add-ons!",
        theory_sections=[
            {
                "heading": "Python's 'Batteries Included' Philosophy",
                "body": "Python includes hundreds of robust, battle-tested modules out of the box. No external `pip install` is required to interact with file paths, system arguments, dates, or complex mathematics."
            },
            {
                "heading": "Core Operating System & Utility Modules",
                "body": "- `pathlib.Path`: Modern object-oriented file path manipulation.\n- `os` / `sys`: Working with environment variables, platform parameters, and command line arguments (`sys.argv`).\n- `datetime`: Handling timestamps, timezones, and date arithmetic.\n- `math`: Trigonometry, logarithms, ceiling, and rounding."
            }
        ],
        code_snippets=[
            {
                "title": "Modern File Paths with pathlib.Path",
                "code": "from pathlib import Path\n\ncurrent_dir = Path.cwd()\nprint('Current Directory:', current_dir.name)\n# Path joining with the division operator (/)\nconfig_path = current_dir / 'config' / 'settings.json'\nprint('Constructed Path:', config_path)\nprint('File extension:', config_path.suffix)"
            },
            {
                "title": "Timestamps & Date Math with datetime",
                "code": "from datetime import datetime, timedelta\n\nnow = datetime.now()\nprint('Current time:', now.strftime('%Y-%m-%d %H:%M:%S'))\n\n# Adding 7 days using timedelta\nnext_week = now + timedelta(days=7)\nprint('One week from today:', next_week.strftime('%A, %B %d'))"
            },
            {
                "title": "Mathematical Functions with math",
                "code": "import math\n\nprint('Pi constant:', math.pi)\nprint('Square root of 144:', math.sqrt(144))\nprint('Ceiling of 4.2:', math.ceil(4.2))\nprint('Floor of 4.8:', math.floor(4.8))"
            },
            {
                "title": "System Parameters & Environment with os and sys",
                "code": "import os, sys\n\nprint('Python Version:', sys.version.split()[0])\nprint('Platform OS:', sys.platform)\n# Reading environment variables safely with fallback\napp_env = os.environ.get('APP_ENV', 'development')\nprint('Active Environment:', app_env)"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Calculate Days Until Milestone",
            description="Use `datetime` to calculate the difference in days between `d1 = datetime(2026, 12, 31)` and `d2 = datetime(2026, 12, 25)`. Print: 'Days remaining: 6'.",
            starter_code="from datetime import datetime\nd1 = datetime(2026, 12, 31)\nd2 = datetime(2026, 12, 25)\n# TODO: Calculate difference in days\n",
            solution_code="from datetime import datetime\nd1 = datetime(2026, 12, 31)\nd2 = datetime(2026, 12, 25)\ndiff = (d1 - d2).days\nprint('Days remaining:', diff)",
            expected_output="Days remaining: 6"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Which module in the Python standard library offers modern object-oriented path handling?",
                options=["pathlib", "os.path", "filesys", "filesystem"],
                correct_answer="pathlib",
                explanation="`pathlib` provides an object-oriented API for interacting with filesystem paths."
            ),
            QuizQuestionBlueprint(
                question="What operator is overloaded in pathlib to concatenate paths conveniently?",
                options=["The division operator (/)", "The plus operator (+)", "The pipe operator (|)", "The double dot (..)"],
                correct_answer="The division operator (/)",
                explanation="`path / 'subdir' / 'file.txt'` is pathlib's clean path concatenation syntax."
            ),
            QuizQuestionBlueprint(
                question="What does sys.argv contain in a Python script?",
                options=[
                    "A list of command-line arguments passed to the script, where sys.argv[0] is the script name.",
                    "System environment variables.",
                    "Active CPU registers.",
                    "Database connection parameters."
                ],
                correct_answer="A list of command-line arguments passed to the script, where sys.argv[0] is the script name.",
                explanation="`sys.argv` stores the command-line flags and parameters given to the Python process."
            ),
            QuizQuestionBlueprint(
                question="Which class in the datetime module represents a duration of time (e.g. 5 days or 3 hours)?",
                options=["timedelta", "timeframe", "duration", "timespan"],
                correct_answer="timedelta",
                explanation="`timedelta` represents the difference between two datetime instances."
            ),
            QuizQuestionBlueprint(
                question="How do you safely read an environment variable in Python without throwing a KeyError if it's missing?",
                options=["os.environ.get('KEY', 'default')", "os.environ['KEY']", "sys.env.read('KEY')", "os.get('KEY')"],
                correct_answer="os.environ.get('KEY', 'default')",
                explanation="`os.environ.get()` returns `None` or the fallback default if the key is not defined."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 35 - CAPSTONE PROJECT
    # -------------------------------------------------------------
    DayBlueprint(
        order=35,
        title="Day 35: [CAPSTONE PROJECT] Personal Finance & Expense Tracker CLI",
        concept="The Ultimate Capstone: Engineering a persistent personal finance analytics CLI with OOP, JSON, and statistical reporting",
        analogy="You have reached the summit of Mount Python! 🏔️ All 35 days of knowledge—data types, loops, collections, functions, exceptions, file I/O, OOP, and JSON—now unite to engineer a complete commercial-grade CLI application that real people can use to master their financial lives!",
        is_project_day=True,
        project_name="Personal Finance & Expense Tracker CLI",
        theory_sections=[
            {
                "heading": "Capstone Overview & Feature Specifications",
                "body": "In this final capstone project, we construct the **Personal Finance Tracker CLI**. Key features:\n1. **Expense Recording**: Adding transactions with `id`, `amount`, `category` (Food, Transport, Utilities, Entertainment, Salary), and timestamp.\n2. **JSON Disk Persistence**: Transactions automatically save to and load from `expenses.json`.\n3. **Financial Analytics**: Total expenditure, breakdown by category with percentages, and highest expense identification.\n4. **Budget Alerts**: Warning triggers when spending in a category exceeds defined thresholds."
            },
            {
                "heading": "System Architecture",
                "body": "The project is structured with two core classes:\n- `Expense`: Represents an individual transaction with validation.\n- `FinanceTracker`: Manages the database collection, JSON file I/O, budget limits, and statistical calculation methods."
            }
        ],
        code_snippets=[
            {
                "title": "The Expense Model Class",
                "code": "from datetime import datetime\n\nclass Expense:\n    def __init__(self, expense_id: int, title: str, amount: float, category: str, date: str = None):\n        self.expense_id = expense_id\n        self.title = title.strip()\n        self.amount = float(amount)\n        self.category = category.strip().capitalize()\n        self.date = date or datetime.now().strftime('%Y-%m-%d %H:%M')\n        \n    def to_dict(self):\n        return {\n            'expense_id': self.expense_id,\n            'title': self.title,\n            'amount': self.amount,\n            'category': self.category,\n            'date': self.date\n        }\n        \n    @classmethod\n    def from_dict(cls, data):\n        return cls(data['expense_id'], data['title'], data['amount'], data['category'], data['date'])"
            },
            {
                "title": "The FinanceTracker Engine with JSON Storage",
                "code": "import json\n\nclass FinanceTracker:\n    def __init__(self, filename='expenses.json'):\n        self.filename = filename\n        self.expenses = []\n        self._load_data()\n        \n    def _load_data(self):\n        try:\n            with open(self.filename, 'r', encoding='utf-8') as f:\n                raw_list = json.load(f)\n                self.expenses = [Expense.from_dict(item) for item in raw_list]\n        except (FileNotFoundError, json.JSONDecodeError):\n            self.expenses = []\n            \n    def save_data(self):\n        with open(self.filename, 'w', encoding='utf-8') as f:\n            json.dump([e.to_dict() for e in self.expenses], f, indent=2)\n            \n    def add_expense(self, title: str, amount: float, category: str):\n        new_id = len(self.expenses) + 1\n        exp = Expense(new_id, title, amount, category)\n        self.expenses.append(exp)\n        self.save_data()\n        return f'✅ Added: \"{title}\" (${amount:.2f}) under {exp.category}'"
            },
            {
                "title": "Category Summaries and Financial Analytics",
                "code": "def generate_summary(tracker):\n    if not tracker.expenses:\n        return 'No recorded expenses.'\n    total_spend = sum(e.amount for e in tracker.expenses)\n    \n    category_totals = {}\n    for e in tracker.expenses:\n        category_totals[e.category] = category_totals.get(e.category, 0.0) + e.amount\n        \n    report = ['\\n================ FINANCIAL REPORT ===============']\n    report.append(f'Total Expenditure: ${total_spend:.2f}')\n    report.append('Category Breakdown:')\n    for cat, amt in category_totals.items():\n        pct = (amt / total_spend) * 100\n        report.append(f'  • {cat:<15}: ${amt:>7.2f}  ({pct:>5.1f}%)')\n    report.append('=================================================')\n    return '\\n'.join(report)"
            },
            {
                "title": "Complete Capstone Demonstration Execution",
                "code": "# Initialize tracker with fresh test file\ntracker = FinanceTracker('capstone_expenses.json')\ntracker.expenses = [] # Clear memory for clean demo run\n\ntracker.add_expense('Groceries', 120.50, 'Food')\ntracker.add_expense('Metro Transit Pass', 45.00, 'Transport')\ntracker.add_expense('Coffee & Bakery', 18.25, 'Food')\ntracker.add_expense('Fiber Internet', 65.00, 'Utilities')\n\nprint(generate_summary(tracker))"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Calculate Highest Single Expense Item",
            description="Given `expenses = [{'title': 'Book', 'amount': 15}, {'title': 'Laptop', 'amount': 1200}, {'title': 'Lunch', 'amount': 25}]`. Write code that finds and prints the item with the maximum amount: 'Highest Expense: Laptop ($1200)'.",
            starter_code="expenses = [{'title': 'Book', 'amount': 15}, {'title': 'Laptop', 'amount': 1200}, {'title': 'Lunch', 'amount': 25}]\n# TODO: Find highest expense\n",
            solution_code="expenses = [{'title': 'Book', 'amount': 15}, {'title': 'Laptop', 'amount': 1200}, {'title': 'Lunch', 'amount': 25}]\nhighest = max(expenses, key=lambda x: x['amount'])\nprint(f\"Highest Expense: {highest['title']} (${highest['amount']})\")",
            expected_output="Highest Expense: Laptop ($1200)"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Why is using to_dict() and from_dict() considered a best-practice pattern in Python OOP?",
                options=[
                    "It decouples class instances from serialization formats (like JSON) cleanly.",
                    "It allows classes to execute faster in binary.",
                    "It is mandatory by the Python interpreter.",
                    "It eliminates the need for constructors."
                ],
                correct_answer="It decouples class instances from serialization formats (like JSON) cleanly.",
                explanation="Serialization helper methods provide a clean bridge between domain objects and data interchange formats."
            ),
            QuizQuestionBlueprint(
                question="What Python function finds the item with the maximum value based on a custom attribute key?",
                options=["max(items, key=lambda x: x['amount'])", "items.max('amount')", "maximum(items)", "highest(items)"],
                correct_answer="max(items, key=lambda x: x['amount'])",
                explanation="The built-in `max()` with a `key` function extracts the comparison metric from each element."
            ),
            QuizQuestionBlueprint(
                question="Why is catching (FileNotFoundError, json.JSONDecodeError) helpful when initializing the tracker from disk?",
                options=[
                    "It allows the app to start cleanly with an empty list if running for the first time or if the file is empty.",
                    "It automatically downloads the file from the internet.",
                    "It forces the OS to create an admin account.",
                    "It prevents users from entering negative numbers."
                ],
                correct_answer="It allows the app to start cleanly with an empty list if running for the first time or if the file is empty.",
                explanation="Gracefully catching missing or empty JSON files ensures smooth initial boot on fresh machines."
            ),
            QuizQuestionBlueprint(
                question="What is the advantage of using a classmethod for from_dict(cls, data)?",
                options=[
                    "It acts as an alternative factory constructor that can instantiate the class dynamically.",
                    "It restricts calling to subclasses only.",
                    "It makes the method private.",
                    "It saves memory."
                ],
                correct_answer="It acts as an alternative factory constructor that can instantiate the class dynamically.",
                explanation="`@classmethod` factory constructors receive `cls` and instantiate new objects from external data representations."
            ),
            QuizQuestionBlueprint(
                question="Congratulations on completing the 35-Day Python Mastery curriculum! What is your next recommended step as an engineer?",
                options=[
                    "Build full-stack backend projects with frameworks like FastAPI or Django, connect to databases, and solve real user problems.",
                    "Stop coding and memorize Python source code in C.",
                    "Switch to a different language and abandon Python entirely.",
                    "Avoid using Git or version control."
                ],
                correct_answer="Build full-stack backend projects with frameworks like FastAPI or Django, connect to databases, and solve real user problems.",
                explanation="Applying fundamentals to real backend frameworks and solving real problems cements mastery!"
            )
        ]
    )
]
