"""
Object-Oriented Programming (OOP) - 55-Day Curriculum - Part 2 (Days 16 to 30)
Module 3: Inheritance Continued (Days 16-19)
Module 4: Polymorphism (Many Forms) (Days 20-25)
Module 5: Abstraction (Hiding Complexity) (Days 26-30)
"""

from seeder.course_blueprint import DayBlueprint, QuizQuestionBlueprint, CodingChallengeBlueprint

DAYS_16_TO_30 = [
    # -------------------------------------------------------------
    # DAY 16: Multiple Inheritance & The Diamond Problem
    # -------------------------------------------------------------
    DayBlueprint(
        order=16,
        title="Day 16: Multiple Inheritance & The Diamond Problem",
        concept="Multiple Inheritance: Inheriting from two or more parent classes, the Diamond of Death ambiguity, and Python's C3 Linearization (MRO)",
        analogy="Imagine a student named Charlie who has two music tutors: Coach Alice and Coach Bob. Coach Alice insists: 'Whenever you start a concert, bow to the audience first!' Coach Bob insists: 'Whenever you start a concert, clap your hands first!' When Charlie steps on stage, what should he do? Bow or clap? This dilemma is the famous **Diamond Problem**: when a child class inherits from two parents that provide conflicting versions of the exact same method, which one takes priority?",
        theory_sections=[
            {
                "heading": "What is Multiple Inheritance?",
                "body": "**Multiple Inheritance** allows a class to inherit attributes and methods from more than one parent class (`Class C(A, B)`).\n\nWhile languages like Java and C# ban multiple class inheritance to avoid ambiguity (allowing it only via Interfaces), languages like Python and C++ fully support it. Multiple inheritance is powerful for creating **Mixins**—small, focused classes that provide modular utility methods across unrelated domain classes."
            },
            {
                "heading": "The Diamond Problem & C3 Linearization (MRO)",
                "body": "The **Diamond Problem** occurs when class `D` inherits from both `B` and `C`, and both `B` and `C` inherit from a common ancestor `A`:\n```\n       [ A ]\n      /     \\\n   [ B ]   [ C ]\n      \\     /\n       [ D ]\n```\nIf `A` defines a method `ping()`, and both `B` and `C` override it, which version does `D` execute when calling `self.ping()`?\n\nPython solves this deterministically using the **C3 Linearization Algorithm** to construct a **Method Resolution Order (MRO)**. It enforces three rules:\n1. Children precede parents.\n2. Left-to-right parent declaration order is respected.\n3. Monotonicity: no class appears more than once in the search chain."
            }
        ],
        code_snippets=[
            {
                "title": "Basic Multiple Inheritance and Mixins in Python",
                "language": "python",
                "code": "# Mixin classes providing targeted modular features\nclass JSONSerializableMixin:\n    def to_json(self):\n        import json\n        return json.dumps(self.__dict__)\n\nclass AuditLogMixin:\n    def log(self, message: str):\n        print(f'[AUDIT LOG]: {message}')\n\n# User inherits from two independent parents\nclass User(JSONSerializableMixin, AuditLogMixin):\n    def __init__(self, username: str, email: str):\n        self.username = username\n        self.email = email\n\nu = User('alice', 'alice@test.com')\nu.log('User created successfully.')\nprint('Serialized JSON:', u.to_json())",
                "explanation": "Mixins demonstrate clean, non-conflicting multiple inheritance."
            },
            {
                "title": "The Classic Diamond Problem in Python",
                "language": "python",
                "code": "class A:\n    def greet(self):\n        return 'Hello from Root A'\n\nclass B(A):\n    def greet(self):\n        return 'Hello from Branch B'\n\nclass C(A):\n    def greet(self):\n        return 'Hello from Branch C'\n\n# D inherits from both B and C (Diamond shape)\nclass D(B, C):\n    pass\n\nd = D()\nprint('Resolved greet():', d.greet())  # B precedes C in left-to-right declaration!",
                "explanation": "Because D is declared D(B, C), Python's MRO resolves B's greet() first."
            },
            {
                "title": "Inspecting Python's C3 Linearization MRO",
                "language": "python",
                "code": "print('D Method Resolution Order:')\nfor idx, cls in enumerate(D.__mro__):\n    print(f'  {idx}: {cls.__name__}')\n# Output: D -> B -> C -> A -> object",
                "explanation": "Inspects the exact search path Python follows when resolving methods on D."
            },
            {
                "title": "Handling Incompatible MROs (TypeError)",
                "language": "python",
                "code": "# Python proactively rejects invalid diamond hierarchies that violate monotonicity\ntry:\n    class X: pass\n    class Y(X): pass\n    # Attempting to inherit X before its own child Y causes MRO failure\n    class Broken(X, Y): pass\nexcept TypeError as e:\n    print('MRO Conflict Detected:', e)",
                "explanation": "Python detects and rejects ambiguous inheritance orders during class creation."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Multimedia Player Multiple Inheritance",
            description="Create class `AudioPlayer` with method `play_audio()` returning `'Playing audio'`. Create class `VideoDisplay` with method `show_video()` returning `'Rendering video'`. Create class `SmartphonePlayer(AudioPlayer, VideoDisplay)` that adds a method `stream_movie()` returning `f'{self.play_audio()} and {self.show_video()}'`.",
            starter_code="class AudioPlayer:\n    pass\n\nclass VideoDisplay:\n    pass\n\nclass SmartphonePlayer(AudioPlayer, VideoDisplay):\n    pass",
            solution_code="class AudioPlayer:\n    def play_audio(self) -> str:\n        return 'Playing audio'\n\nclass VideoDisplay:\n    def show_video(self) -> str:\n        return 'Rendering video'\n\nclass SmartphonePlayer(AudioPlayer, VideoDisplay):\n    def stream_movie(self) -> str:\n        return f'{self.play_audio()} and {self.show_video()}'",
            expected_output="Playing audio and Rendering video"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the 'Diamond Problem' in Object-Oriented Programming?",
                options=[
                    "An ambiguity that arises when a child class inherits from two parent classes that both derive from a common ancestor and override the same method",
                    "A problem when classes consume more than 100 carats of diamond RAM",
                    "A hardware failure in the CPU floating point unit",
                    "A syntax error caused by using diamond brackets in Python"
                ],
                correct_answer="An ambiguity that arises when a child class inherits from two parent classes that both derive from a common ancestor and override the same method",
                explanation="The diamond problem refers to the ambiguity of deciding which parent's implementation to call when class D inherits from B and C, which both derive from A."
            ),
            QuizQuestionBlueprint(
                question="How does Python solve the Diamond Problem deterministically?",
                options=[
                    "Using the C3 Linearization Algorithm to compute a strict Method Resolution Order (MRO)",
                    "By picking a parent randomly using random.choice()",
                    "By crashing the program immediately with a DiamondException",
                    "By executing both parent methods simultaneously on two CPU cores"
                ],
                correct_answer="Using the C3 Linearization Algorithm to compute a strict Method Resolution Order (MRO)",
                explanation="Python uses the C3 Linearization algorithm to calculate a consistent, monotonic Method Resolution Order (MRO)."
            ),
            QuizQuestionBlueprint(
                question="Why did languages like Java, C#, and Go choose to disallow multiple inheritance of classes?",
                options=[
                    "To prevent the complexity, ambiguity, and fragile code associated with the Diamond Problem",
                    "Because computers in the 1990s lacked color screens",
                    "Because multiple inheritance is mathematically impossible",
                    "To force developers to write all code in a single file"
                ],
                correct_answer="To prevent the complexity, ambiguity, and fragile code associated with the Diamond Problem",
                explanation="Java and C# banned multiple class inheritance to avoid the diamond problem, opting for single class inheritance with multiple interfaces instead."
            ),
            QuizQuestionBlueprint(
                question="If class `Child(ParentA, ParentB)` is defined in Python, which parent is searched first for an inherited method according to MRO rules?",
                options=[
                    "ParentA (left-to-right order is prioritized)",
                    "ParentB",
                    "Whichever parent has the shorter name",
                    "The parent defined latest in the file"
                ],
                correct_answer="ParentA (left-to-right order is prioritized)",
                explanation="In Python's MRO, parents declared in class arguments are searched in strict left-to-right order."
            ),
            QuizQuestionBlueprint(
                question="What is a 'Mixin' in Python multiple inheritance?",
                options=[
                    "A small, focused class designed to provide specific reusable methods to other classes without being meant for standalone instantiation",
                    "A function that mixes strings and integers together",
                    "A Python package downloaded from PyPI",
                    "A class constructor that takes 100 arguments"
                ],
                correct_answer="A small, focused class designed to provide specific reusable methods to other classes without being meant for standalone instantiation",
                explanation="Mixins provide plug-and-play functionality across unrelated classes via multiple inheritance without forming deep parent hierarchies."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 17: `super` or `base` Keyword
    # -------------------------------------------------------------
    DayBlueprint(
        order=17,
        title="Day 17: `super` or `base` Keyword",
        concept="Delegating to ancestors: The `super()` proxy object in Python, cooperative multiple inheritance, and avoiding hardcoded parent references",
        analogy="Imagine an assistant chef preparing a gourmet burger. The head chef already has a master recipe for seasoning and grilling the beef patty (`Parent.cook()`). The assistant chef doesn't want to reinvent how to grill beef! Instead, the assistant says: 'Hey Head Chef, do your master cooking step (`super().cook()`), and then I will add my secret truffle mayo on top!' The `super` keyword is the respectful call to the master recipe before or after adding your own special touch.",
        theory_sections=[
            {
                "heading": "The Purpose of `super()`",
                "body": "When a subclass overrides a parent's method, it frequently needs to preserve and build upon the parent's existing behavior rather than completely discarding it. The `super()` built-in returns a **proxy object** that delegates method calls to a parent or sibling class in the class's Method Resolution Order (MRO).\n\nWhy use `super()` instead of direct parent naming (e.g. `ParentClass.method(self)`):\n1. **Maintainability**: If the parent class is renamed or the inheritance hierarchy is refactored, you don't need to rewrite method calls across all subclasses.\n2. **Cooperative Multiple Inheritance**: In complex multi-parent diamond hierarchies, `super()` guarantees that every ancestor in the MRO chain is called exactly once."
            },
            {
                "heading": "How `super()` Traverses the MRO Chain",
                "body": "In Python 3, zero-argument `super()` automatically looks up the current class and instance context. It does not simply jump to the immediate parent; rather, it looks at the **next class in the instance's MRO**.\n\nThis behavior is what makes cooperative multiple inheritance possible, allowing sibling classes in a diamond to chain their initializers and methods harmoniously."
            }
        ],
        code_snippets=[
            {
                "title": "Using super() to Extend a Parent Method",
                "language": "python",
                "code": "class Employee:\n    def __init__(self, name: str, salary: float):\n        self.name = name\n        self.salary = salary\n\n    def get_details(self) -> str:\n        return f'Employee: {self.name}, Base Salary: ${self.salary:.2f}'\n\nclass Manager(Employee):\n    def __init__(self, name: str, salary: float, bonus: float):\n        # Delegate name and salary initialization to Employee superclass\n        super().__init__(name, salary)\n        self.bonus = bonus\n\n    def get_details(self) -> str:\n        # Extend parent string representation with manager-specific bonus\n        base_details = super().get_details()\n        return f'{base_details} + Bonus: ${self.bonus:.2f}'\n\nm = Manager('Alice', 100000.0, 25000.0)\nprint(m.get_details())",
                "explanation": "Manager calls super().get_details() to reuse the base string before appending bonus data."
            },
            {
                "title": "Hardcoded Parent vs super() Maintenance Difference",
                "language": "python",
                "code": "# Fragile (Hardcoded parent name):\n# class Child(Parent):\n#     def __init__(self): Parent.__init__(self)  # Breaks if Parent changes!\n#\n# Robust (super()):\n# class Child(Parent):\n#     def __init__(self): super().__init__()     # Seamlessly tracks hierarchy",
                "explanation": "super() decouples derived classes from the exact name of their immediate superclass."
            },
            {
                "title": "Cooperative Multiple Inheritance with super()",
                "language": "python",
                "code": "class Base:\n    def act(self):\n        print('Base act')\n\nclass Step1(Base):\n    def act(self):\n        print('Step 1')\n        super().act()  # Calls next in MRO, which is Step2!\n\nclass Step2(Base):\n    def act(self):\n        print('Step 2')\n        super().act()\n\nclass Combined(Step1, Step2):\n    def act(self):\n        print('Combined start')\n        super().act()\n\nCombined().act()",
                "explanation": "Notice how Step1's super().act() calls Step2! super() follows the instance's MRO dynamically."
            },
            {
                "title": "Python Script: Printing MRO of Cooperative Hierarchy",
                "language": "python",
                "code": "print('MRO for Combined:', [c.__name__ for c in Combined.__mro__])\n# Order: Combined -> Step1 -> Step2 -> Base -> object",
                "explanation": "Confirms how super() steps through each class in the MRO sequentially."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Decorating Logger with super()",
            description="Create a base class `SimpleLogger` with method `log(msg: str)` that returns `f'[INFO]: {msg}'`. Create a derived class `TimestampLogger` that uses `super().log(msg)` and prepends `'[2026-09-30] '` to the parent output.",
            starter_code="class SimpleLogger:\n    # Implement SimpleLogger\n    pass\n\nclass TimestampLogger(SimpleLogger):\n    # Implement TimestampLogger using super()\n    pass",
            solution_code="class SimpleLogger:\n    def log(self, msg: str) -> str:\n        return f'[INFO]: {msg}'\n\nclass TimestampLogger(SimpleLogger):\n    def log(self, msg: str) -> str:\n        parent_log = super().log(msg)\n        return f'[2026-09-30] {parent_log}'",
            expected_output="[2026-09-30] [INFO]: System online"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What does the `super()` function return in Python 3?",
                options=[
                    "A proxy object that delegates attribute and method lookups to the next class in the Method Resolution Order (MRO)",
                    "A reference to the root CPU register",
                    "A duplicate copy of the instance in memory",
                    "A boolean flag indicating if the class has a parent"
                ],
                correct_answer="A proxy object that delegates attribute and method lookups to the next class in the Method Resolution Order (MRO)",
                explanation="`super()` creates a proxy object that routes method calls to the next class in the instance's MRO chain."
            ),
            QuizQuestionBlueprint(
                question="Why is using `super().__init__(...)` superior to hardcoding `ParentClass.__init__(self, ...)`?",
                options=[
                    "It decouples the child from the parent's exact name and guarantees correct execution in multiple inheritance hierarchies",
                    "It makes the code execute 100 times faster",
                    "Because Python bans direct calls to parent classes",
                    "It prevents the parent constructor from allocating memory"
                ],
                correct_answer="It decouples the child from the parent's exact name and guarantees correct execution in multiple inheritance hierarchies",
                explanation="super() avoids hardcoding class names and correctly traverses complex diamond hierarchies via the MRO."
            ),
            QuizQuestionBlueprint(
                question="What is the C# and C++ equivalent keyword concept for Python's `super`?",
                options=[
                    "`base` in C# and explicit class scope resolution `Parent::` in C++",
                    "`parent` in C#",
                    "`this` in C++",
                    "`root` in C#"
                ],
                correct_answer="`base` in C# and explicit class scope resolution `Parent::` in C++",
                explanation="C# uses the `base` keyword to access base class members, while C++ uses explicit scope resolution (`Base::method()`)."
            ),
            QuizQuestionBlueprint(
                question="In cooperative multiple inheritance, does `super().method()` always call the immediate parent declared in the class definition?",
                options=[
                    "No, it calls the NEXT class in the instance's overall MRO, which may be a sibling class",
                    "Yes, it always strictly calls the first parent",
                    "No, it calls a random ancestor",
                    "Yes, but only in Python 2"
                ],
                correct_answer="No, it calls the NEXT class in the instance's overall MRO, which may be a sibling class",
                explanation="In diamond hierarchies, super() follows the C3 MRO chain of the instantiated object, which can resolve to a sibling class."
            ),
            QuizQuestionBlueprint(
                question="What syntax is required to invoke a parent's `render()` method without arguments in Python 3?",
                options=[
                    "super().render()",
                    "super(render)",
                    "parent.render()",
                    "super.render(self)"
                ],
                correct_answer="super().render()",
                explanation="In Python 3, `super().method_name()` is the standard, clean syntax."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 18: Constructor Chaining in Inheritance
    # -------------------------------------------------------------
    DayBlueprint(
        order=18,
        title="Day 18: Constructor Chaining in Inheritance",
        concept="Constructor Chaining: Propagating initialization parameters upwards through inheritance tiers and initializing base state before derived state",
        analogy="Think of building a 3-story house: you cannot build the 2nd-floor bedrooms until the 1st-floor foundation and walls are poured. And you cannot install the 3rd-floor rooftop garden until the 2nd floor is solid. Constructor chaining guarantees that when a grandchild object is born, the grandparent initializes its foundation first, the parent initializes the middle tier second, and the child adds its finishing touches last!",
        theory_sections=[
            {
                "heading": "What is Constructor Chaining?",
                "body": "**Constructor Chaining** is the orderly sequence where a derived class constructor automatically or explicitly invokes the constructor of its superclass before executing its own specific setup logic.\n\nIn languages like Java and C++, the base class constructor is automatically called before the child constructor body runs. In Python, explicit invocation via `super().__init__(...)` is required. Failing to chain constructors results in a child object whose inherited attributes are uninitialized (leading to `AttributeError` when parent methods are called)."
            },
            {
                "heading": "Handling Variable Arguments with `*args` and `**kwargs`",
                "body": "In large inheritance hierarchies where different tiers require different parameters, flexible constructors utilize `**kwargs`:\n```python\nclass Child(Parent):\n    def __init__(self, child_arg, **kwargs):\n        super().__init__(**kwargs)  # Pass remaining kwargs to ancestors\n        self.child_arg = child_arg\n```\nThis enables clean parameter passing across arbitrary levels without rigid coupling."
            }
        ],
        code_snippets=[
            {
                "title": "Clean Constructor Chaining across Three Generations",
                "language": "python",
                "code": "class Grandparent:\n    def __init__(self, family_name: str):\n        self.family_name = family_name\n        print(f'1. Grandparent initialized with family: {self.family_name}')\n\nclass Parent(Grandparent):\n    def __init__(self, family_name: str, home_city: str):\n        super().__init__(family_name)  # Chain to Grandparent\n        self.home_city = home_city\n        print(f'2. Parent initialized with city: {self.home_city}')\n\nclass Child(Parent):\n    def __init__(self, family_name: str, home_city: str, favorite_hobby: str):\n        super().__init__(family_name, home_city)  # Chain to Parent\n        self.favorite_hobby = favorite_hobby\n        print(f'3. Child initialized with hobby: {self.favorite_hobby}')\n\nc = Child('Smith', 'Chicago', 'Chess')",
                "explanation": "Executes in top-down order: Grandparent -> Parent -> Child."
            },
            {
                "title": "The Hazard of Omitting Constructor Chaining (AttributeError)",
                "language": "python",
                "code": "class BaseAccount:\n    def __init__(self, balance: float):\n        self.balance = balance\n\nclass BrokenSavings(BaseAccount):\n    def __init__(self, interest_rate: float):\n        # Forgot super().__init__(...)! self.balance was never created!\n        self.interest_rate = interest_rate\n\nb = BrokenSavings(0.05)\ntry:\n    print(b.balance)  # Raises AttributeError!\nexcept AttributeError as e:\n    print('Uninitialized state error:', e)",
                "explanation": "Demonstrates how omitting constructor chaining leaves inherited state missing."
            },
            {
                "title": "Flexible Parameter Chaining using **kwargs",
                "language": "python",
                "code": "class Shape:\n    def __init__(self, color: str = 'red', **kwargs):\n        super().__init__(**kwargs)\n        self.color = color\n\nclass BorderedShape(Shape):\n    def __init__(self, border_width: int = 1, **kwargs):\n        super().__init__(**kwargs)\n        self.border_width = border_width\n\nclass Square(BorderedShape):\n    def __init__(self, side_length: float, **kwargs):\n        super().__init__(**kwargs)\n        self.side_length = side_length\n\ns = Square(side_length=10, border_width=3, color='blue')\nprint(f'Square: side={s.side_length}, border={s.border_width}, color={s.color}')",
                "explanation": "kwargs passes arguments cleanly up cooperative constructor chains."
            },
            {
                "title": "Java vs Python Constructor Chaining",
                "language": "text",
                "code": "// In Java:\n// public Child(String name, int age) {\n//     super(name); // Must be the VERY FIRST line of constructor in Java!\n//     this.age = age;\n// }",
                "explanation": "Contrasts Java's strict first-line super() requirement with Python's procedural flexibility."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Three-Tier Vehicle Hardware Chaining",
            description="Create 3 classes:\n1. `Engine(power_hp: int)` initializing `self.power_hp`.\n2. `Chassis(power_hp: int, wheels: int)` calling `super().__init__(power_hp)` and initializing `self.wheels`.\n3. `Car(power_hp: int, wheels: int, model: str)` calling `super().__init__(power_hp, wheels)` and initializing `self.model`.",
            starter_code="class Engine:\n    pass\n\nclass Chassis(Engine):\n    pass\n\nclass Car(Chassis):\n    pass",
            solution_code="class Engine:\n    def __init__(self, power_hp: int):\n        self.power_hp = int(power_hp)\n\nclass Chassis(Engine):\n    def __init__(self, power_hp: int, wheels: int):\n        super().__init__(power_hp)\n        self.wheels = int(wheels)\n\nclass Car(Chassis):\n    def __init__(self, power_hp: int, wheels: int, model: str):\n        super().__init__(power_hp, wheels)\n        self.model = model",
            expected_output="Car Model: Mustang (450 HP, 4 wheels)"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is Constructor Chaining in Object-Oriented Programming?",
                options=[
                    "The practice of a derived class constructor calling its parent class constructor to ensure base attributes are properly initialized",
                    "Locking a constructor with a cryptographic password",
                    "Creating 50 objects inside a single while loop",
                    "Linking multiple database tables with foreign keys"
                ],
                correct_answer="The practice of a derived class constructor calling its parent class constructor to ensure base attributes are properly initialized",
                explanation="Constructor chaining ensures that ancestor initialization logic executes to set up base state before child setup occurs."
            ),
            QuizQuestionBlueprint(
                question="What happens in Python if a subclass defines `__init__` but forgets to call `super().__init__(...)`?",
                options=[
                    "The parent class `__init__` is NOT called, leaving all parent instance attributes uninitialized and causing AttributeErrors",
                    "Python calls the parent constructor automatically at program exit",
                    "The subclass is permanently converted to an abstract interface",
                    "The compiler generates a syntax error"
                ],
                correct_answer="The parent class `__init__` is NOT called, leaving all parent instance attributes uninitialized and causing AttributeErrors",
                explanation="Unlike Java, Python does not automatically invoke the base class `__init__`; you must explicitly invoke `super().__init__()`."
            ),
            QuizQuestionBlueprint(
                question="In what sequential order does constructor state initialization take place in a properly chained hierarchy?",
                options=[
                    "Top-down: base/ancestor constructors initialize first, followed sequentially by derived/child constructors",
                    "Bottom-up: the child initializes first and the root base class initializes last",
                    "Simultaneously in parallel threads",
                    "In alphabetical order of class names"
                ],
                correct_answer="Top-down: base/ancestor constructors initialize first, followed sequentially by derived/child constructors",
                explanation="Foundational base state must be established before specialized derived state is built on top of it."
            ),
            QuizQuestionBlueprint(
                question="How does passing `**kwargs` into `super().__init__(**kwargs)` benefit deep or cooperative inheritance hierarchies?",
                options=[
                    "It allows arbitrary named parameters to bubble up through the MRO chain without tightly coupling each subclass to its parent's exact signature",
                    "It doubles the memory capacity of every integer",
                    "It enables classes to bypass all security firewalls",
                    "It converts arguments into a binary string"
                ],
                correct_answer="It allows arbitrary named parameters to bubble up through the MRO chain without tightly coupling each subclass to its parent's exact signature",
                explanation="`**kwargs` propagation enables flexible parameter routing through complex multi-tier inheritance trees."
            ),
            QuizQuestionBlueprint(
                question="In Java, what strict syntactic rule governs the invocation of `super(...)` inside a derived constructor?",
                options=[
                    "`super(...)` must be the absolute very first statement inside the constructor body",
                    "`super(...)` must be called inside a try/catch block",
                    "`super(...)` can only be called if the method is static",
                    "`super(...)` must be written in lowercase Roman numerals"
                ],
                correct_answer="`super(...)` must be the absolute very first statement inside the constructor body",
                explanation="Java enforces that the superclass constructor invocation `super(...)` must be the first line of the child constructor."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 19 (Project): Employee & Manager Hierarchy System
    # -------------------------------------------------------------
    DayBlueprint(
        order=19,
        title="Day 19 (Project): Employee & Manager Hierarchy System",
        concept="Hands-on Project Day: Designing an enterprise corporate personnel hierarchy with base employees, specialized engineers, sales reps with commissions, and managers directing teams",
        analogy="Think of today's project like organizing a large corporate enterprise: at the foundation, every worker is an `Employee` with an ID, name, and base salary. `SoftwareEngineers` specialize with programming languages. `SalesReps` specialize with commission percentages. `Managers` sit atop teams of employees, approving budgets and calculating payroll bonuses based on team productivity!",
        is_project_day=True,
        project_name="Employee & Manager Hierarchy System",
        theory_sections=[
            {
                "heading": "Corporate Domain Model Hierarchy",
                "body": "Today's project builds an enterprise workforce management system using a clean inheritance tree:\n```\n                  [ Employee ]\n                 /     |      \\\n  [ Engineer ]  [ SalesRep ]  [ Manager ]\n```\n- **`Employee` (Base)**: Common state (`emp_id`, `name`, `base_salary`) and interface (`calculate_pay()`).\n- **`Engineer`**: Adds `tech_stack` and overtime pay.\n- **`SalesRep`**: Adds `sales_volume` and `commission_rate`.\n- **`Manager`**: Directs a list of `Employee` subordinates and receives team performance bonuses."
            },
            {
                "heading": "Polymorphic Payroll Processing",
                "body": "A critical advantage of inheritance is that a master payroll processor can iterate over a mixed list containing Engineers, SalesReps, and Managers, call `.calculate_pay()` on each worker, and compute total payroll polymorphically without needing ugly `if/else` type checking."
            }
        ],
        code_snippets=[
            {
                "title": "Base Employee and Specialized Worker Subclasses",
                "language": "python",
                "code": "class Employee:\n    def __init__(self, emp_id: str, name: str, base_salary: float):\n        self.emp_id = emp_id\n        self.name = name\n        self.base_salary = float(base_salary)\n\n    def calculate_pay(self) -> float:\n        return self.base_salary\n\nclass Engineer(Employee):\n    def __init__(self, emp_id: str, name: str, base_salary: float, overtime_hours: float = 0.0, hourly_rate: float = 50.0):\n        super().__init__(emp_id, name, base_salary)\n        self.overtime_hours = overtime_hours\n        self.hourly_rate = hourly_rate\n\n    def calculate_pay(self) -> float:\n        return self.base_salary + (self.overtime_hours * self.hourly_rate)\n\nclass SalesRep(Employee):\n    def __init__(self, emp_id: str, name: str, base_salary: float, sales_volume: float, commission_rate: float = 0.10):\n        super().__init__(emp_id, name, base_salary)\n        self.sales_volume = sales_volume\n        self.commission_rate = commission_rate\n\n    def calculate_pay(self) -> float:\n        return self.base_salary + (self.sales_volume * self.commission_rate)",
                "explanation": "Specialized employees override calculate_pay() with custom compensation formulas."
            },
            {
                "title": "Manager Subclass Managing Teams of Employees",
                "language": "python",
                "code": "class Manager(Employee):\n    def __init__(self, emp_id: str, name: str, base_salary: float, bonus_percentage: float = 0.15):\n        super().__init__(emp_id, name, base_salary)\n        self.bonus_percentage = bonus_percentage\n        self.team = []  # List of managed Employee objects\n\n    def add_team_member(self, employee: Employee):\n        if employee not in self.team and employee is not self:\n            self.team.append(employee)\n\n    def calculate_pay(self) -> float:\n        # Base salary + bonus based on base salary + team size bonus\n        team_bonus = len(self.team) * 500.0\n        return self.base_salary * (1 + self.bonus_percentage) + team_bonus",
                "explanation": "Manager combines inheritance (is an Employee) with composition (has team members)."
            },
            {
                "title": "Executing Corporate Payroll Simulation",
                "language": "python",
                "code": "# Instantiate corporate staff\neng1 = Engineer('E-01', 'Alice', 90000, overtime_hours=10)\nsales1 = SalesRep('S-01', 'Bob', 50000, sales_volume=100000)\nmgr = Manager('M-01', 'Carol', 120000)\nmgr.add_team_member(eng1)\nmgr.add_team_member(sales1)\n\ncompany_roster = [eng1, sales1, mgr]\n\nprint('=== CORPORATE PAYROLL REPORT ===')\nfor emp in company_roster:\n    print(f'{emp.emp_id} | {emp.name:6} | Pay: ${emp.calculate_pay():,.2f}')\nprint(f'Total Payroll: ${sum(e.calculate_pay() for e in company_roster):,.2f}')",
                "explanation": "Iterates over diverse subclasses polymorphically to compute corporate payroll."
            },
            {
                "title": "Python Script: Department Budget Introspection",
                "language": "python",
                "code": "def print_manager_roster(manager: Manager):\n    print(f'Manager: {manager.name} (Direct Reports: {len(manager.team)})')\n    for report in manager.team:\n        print(f'  -> {report.name} ({type(report).__name__})')\n\nprint_manager_roster(mgr)",
                "explanation": "Inspects dynamic team relationships and employee concrete types."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Department Budget Calculator",
            description="Add a method `get_team_total_payroll(self) -> float` to the `Manager` class that calculates and returns the sum of `calculate_pay()` for all members of the manager's team (excluding the manager's own pay). Return 0.0 if team is empty.",
            starter_code="class Manager(Employee):\n    # Implement get_team_total_payroll()\n    pass",
            solution_code="class Manager(Employee):\n    def __init__(self, emp_id: str, name: str, base_salary: float):\n        super().__init__(emp_id, name, base_salary)\n        self.team = []\n\n    def add_team_member(self, emp):\n        self.team.append(emp)\n\n    def get_team_total_payroll(self) -> float:\n        return sum(member.calculate_pay() for member in self.team)",
            expected_output="Team Total Payroll: 150500.0"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Why is it beneficial that `Engineer`, `SalesRep`, and `Manager` all inherit from `Employee` in the payroll system?",
                options=[
                    "A payroll loop can iterate through any mix of workers and call `calculate_pay()` without caring about their specific type",
                    "It makes all employees earn the exact same salary",
                    "It prevents employees from resigning",
                    "It automatically generates IRS tax forms"
                ],
                correct_answer="A payroll loop can iterate through any mix of workers and call `calculate_pay()` without caring about their specific type",
                explanation="Inheriting a common interface allows polymorphic payroll processing where each specialized class calculates its own compensation."
            ),
            QuizQuestionBlueprint(
                question="In the `Manager` class, what OOP design principle is shown by maintaining `self.team = []`?",
                options=[
                    "Composition/Aggregation: A Manager HAS-A team of Employee objects",
                    "Multiple Inheritance: Manager inherits from Team",
                    "Data Tampering",
                    "Memory fragmentation"
                ],
                correct_answer="Composition/Aggregation: A Manager HAS-A team of Employee objects",
                explanation="The team list is an aggregation relationship (a Manager HAS-A collection of employees)."
            ),
            QuizQuestionBlueprint(
                question="What defensive check should be included in `add_team_member()`?",
                options=[
                    "Preventing an employee from adding themselves as their own subordinate (`employee is not self`) and preventing duplicates",
                    "Checking if the employee has a college degree",
                    "Verifying the employee's horoscope",
                    "Checking if the employee's name contains a vowel"
                ],
                correct_answer="Preventing an employee from adding themselves as their own subordinate (`employee is not self`) and preventing duplicates",
                explanation="Guarding against self-reporting avoids circular managerial loops and duplicate roster assignments."
            ),
            QuizQuestionBlueprint(
                question="How does `SalesRep.calculate_pay()` modify the base employee compensation?",
                options=[
                    "It adds `sales_volume * commission_rate` to the base salary",
                    "It divides the salary by zero",
                    "It subtracts corporate tax from the company bank account",
                    "It replaces base salary with stock options"
                ],
                correct_answer="It adds `sales_volume * commission_rate` to the base salary",
                explanation="Derived classes specialize inherited behavior by layering domain-specific calculations over base state."
            ),
            QuizQuestionBlueprint(
                question="If a new role `Contractor` is added to the company tomorrow, how does the inheritance architecture accommodate it?",
                options=[
                    "By simply deriving `Contractor(Employee)` and implementing its custom `calculate_pay()`, without modifying existing employee classes",
                    "By rewriting the entire codebase from scratch",
                    "By deleting all existing managers",
                    "By converting Python into C++"
                ],
                correct_answer="By simply deriving `Contractor(Employee)` and implementing its custom `calculate_pay()`, without modifying existing employee classes",
                explanation="This exemplifies the Open/Closed Principle: the system is open for extension (adding Contractor) without modifying existing code."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 20: Concept of Polymorphism
    # -------------------------------------------------------------
    DayBlueprint(
        order=20,
        title="Day 20: Concept of Polymorphism",
        concept="The Third Pillar of OOP: Polymorphism ('Many Forms') - unified interfaces with specialized underlying implementations",
        analogy="Think of the universal 'Play' button on your TV remote, your car's CD player, your smartphone's Spotify app, and your YouTube tab. You press the exact same triangle icon button (**Unified Interface**), but how each device fulfills that command is radically different: the phone streams Wi-Fi packets, the car spins a physical disc with a laser, and the TV sends an HDMI command. Polymorphism means: **One Interface, Many Implementations**!",
        theory_sections=[
            {
                "heading": "What is Polymorphism?",
                "body": "**Polymorphism** originates from the Greek words *poly* (many) and *morph* (form). In programming, it refers to the ability of different classes to respond to the same method call in their own unique way.\n\nPolymorphism allows code to be written against a high-level, generic interface (e.g. `shape.draw()`), while the actual behavior executed at runtime depends dynamically on the concrete object being processed (e.g., drawing a Circle vs drawing a Triangle)."
            },
            {
                "heading": "Compile-Time vs Run-Time Polymorphism",
                "body": "Polymorphism is categorized into two major forms:\n1. **Compile-Time (Static) Polymorphism**: Method Overloading and Operator Overloading. Resolved by the compiler before execution.\n2. **Run-Time (Dynamic) Polymorphism**: Method Overriding via inheritance and dynamic dispatch. Resolved at runtime based on the actual object instance in memory.\n\nIn Python, **Duck Typing** is also a major expression of polymorphism: *\"If it walks like a duck and quacks like a duck, it's a duck!\"*"
            }
        ],
        code_snippets=[
            {
                "title": "Classic Polymorphism: Diverse Animals Responding to speak()",
                "language": "python",
                "code": "class Dog:\n    def speak(self) -> str: return 'Woof!'\n\nclass Cat:\n    def speak(self) -> str: return 'Meow!'\n\nclass Cow:\n    def speak(self) -> str: return 'Moo!'\n\n# Polymorphic function: doesn't care about concrete class, only interface!\ndef animal_chorus(animals: list):\n    for a in animals:\n        print(f'{type(a).__name__} says: {a.speak()}')\n\nzoo = [Dog(), Cat(), Cow(), Dog()]\nanimal_chorus(zoo)",
                "explanation": "animal_chorus operates on any object that responds to speak(), demonstrating pure polymorphism."
            },
            {
                "title": "Polymorphism through Common Base Class",
                "language": "python",
                "code": "class Shape:\n    def render(self):\n        raise NotImplementedError('Subclass must implement abstract render')\n\nclass Circle(Shape):\n    def render(self): return 'Drawing Circle (O)'\n\nclass Square(Shape):\n    def render(self): return 'Drawing Square ([])'\n\nfor s in [Circle(), Square()]:\n    print(s.render())",
                "explanation": "Shapes share the same interface contract while delivering distinct implementations."
            },
            {
                "title": "Duck Typing in Python (Interface without Inheritance)",
                "language": "python",
                "code": "class AudioFile:\n    def play(self): return 'Streaming MP3 audio'\n\nclass VideoClip:\n    def play(self): return 'Rendering MP4 frames'\n\nclass StreamingRadio:\n    def play(self): return 'Tuning internet radio frequency'\n\ndef start_media(media_player):\n    # Python doesn't require media_player to inherit from MediaBase!\n    print('Playing media:', media_player.play())\n\nstart_media(AudioFile())\nstart_media(VideoClip())",
                "explanation": "Duck typing enables polymorphism based on capability rather than formal class lineage."
            },
            {
                "title": "Python Script: Dynamic Dispatch Introspection",
                "language": "python",
                "code": "obj = Cat()\nmethod = getattr(obj, 'speak')\nprint('Dynamic dispatch execution:', method())",
                "explanation": "Demonstrates runtime dynamic dispatch retrieving and executing bound methods."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Polymorphic Document Exporter",
            description="Create 3 classes: `PDFDocument`, `HTMLDocument`, and `TextDocument`. Each must implement an `export(content: str) -> str` method returning `f'PDF: {content}'`, `f'<html>{content}</html>'`, and `f'TXT: {content}'` respectively. Write a function `export_all(docs, text)` that returns a list of all exported strings.",
            starter_code="class PDFDocument:\n    pass\nclass HTMLDocument:\n    pass\nclass TextDocument:\n    pass\ndef export_all(docs, text):\n    pass",
            solution_code="class PDFDocument:\n    def export(self, content: str) -> str: return f'PDF: {content}'\nclass HTMLDocument:\n    def export(self, content: str) -> str: return f'<html>{content}</html>'\nclass TextDocument:\n    def export(self, content: str) -> str: return f'TXT: {content}'\n\ndef export_all(docs: list, text: str) -> list:\n    return [d.export(text) for d in docs]",
            expected_output="['PDF: Report', '<html>Report</html>', 'TXT: Report']"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the core meaning of Polymorphism in Object-Oriented Programming?",
                options=[
                    "One Interface, Many Implementations: the ability of different classes to respond to the same method call in their own unique way",
                    "Writing code in multiple programming languages simultaneously",
                    "Encrypting source code with multiple private keys",
                    "Converting a class into multiple threads"
                ],
                correct_answer="One Interface, Many Implementations: the ability of different classes to respond to the same method call in their own unique way",
                explanation="Polymorphism allows disparate objects to expose a uniform interface while implementing specialized underlying behaviors."
            ),
            QuizQuestionBlueprint(
                question="What are the two major categories of Polymorphism in OOP?",
                options=[
                    "Compile-Time (Static) Polymorphism and Run-Time (Dynamic) Polymorphism",
                    "Public Polymorphism and Private Polymorphism",
                    "Synchronous Polymorphism and Asynchronous Polymorphism",
                    "Linear Polymorphism and Binary Polymorphism"
                ],
                correct_answer="Compile-Time (Static) Polymorphism and Run-Time (Dynamic) Polymorphism",
                explanation="Polymorphism is divided into Compile-Time (Overloading) and Run-Time (Overriding / Dynamic Dispatch)."
            ),
            QuizQuestionBlueprint(
                question="What is 'Duck Typing' in Python?",
                options=[
                    "A dynamic typing philosophy where an object's suitability is determined by the presence of certain methods, rather than its inheritance hierarchy",
                    "A special library for audio synthesis of bird sounds",
                    "A compiler bug that causes incorrect math calculations",
                    "A method that can only be called in wetlands"
                ],
                correct_answer="A dynamic typing philosophy where an object's suitability is determined by the presence of certain methods, rather than its inheritance hierarchy",
                explanation="'Duck Typing' means if an object implements the required interface (quacks like a duck), Python accepts it regardless of its explicit inheritance."
            ),
            QuizQuestionBlueprint(
                question="How does Polymorphism improve code scalability when adding new features?",
                options=[
                    "New classes can be added without modifying existing consumer functions, as long as they implement the expected interface",
                    "It compresses source files by 50%",
                    "It prevents memory leaks automatically",
                    "It eliminates the need for software licenses"
                ],
                correct_answer="New classes can be added without modifying existing consumer functions, as long as they implement the expected interface",
                explanation="Consumer code written against a generic interface automatically supports new derived classes without modification."
            ),
            QuizQuestionBlueprint(
                question="Which real-world analogy best represents Polymorphism?",
                options=[
                    "A universal remote control whose 'Power' button turns on TVs, DVD players, and air conditioners in different ways",
                    "A box of identical wooden toothpicks",
                    "A locked padlock with no keyhole",
                    "A single piece of blank printer paper"
                ],
                correct_answer="A universal remote control whose 'Power' button turns on TVs, DVD players, and air conditioners in different ways",
                explanation="The universal remote provides a single interface (Power button) that triggers different actions on different devices."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 21: Compile-Time (Method Overloading)
    # -------------------------------------------------------------
    DayBlueprint(
        order=21,
        title="Day 21: Compile-Time (Method Overloading)",
        concept="Compile-Time Polymorphism: Method Overloading principles, parameter signature differentiation, and Pythonic emulation via default arguments and `functools.singledispatch`",
        analogy="Imagine walking up to an airport baggage check-in desk. You say: 'Check in my luggage.' If you hand the clerk 1 bag, they charge you $30. If you hand the clerk 1 bag + 1 surfboard, they apply the oversize sporting rate. If you hand the clerk a VIP gold badge + 3 bags, they waive all fees! It is the exact same action (**Check-In**), but the behavior changes based on **what combination of items you hand over**!",
        theory_sections=[
            {
                "heading": "What is Method Overloading?",
                "body": "**Method Overloading** is a form of compile-time (static) polymorphism where a class defines multiple methods sharing the **exact same name**, but differing in their **parameter signatures** (number of parameters, parameter types, or parameter order).\n\nIn statically typed languages like Java and C++:\n```java\nint add(int a, int b) { return a + b; }\ndouble add(double a, double b) { return a + b; }\nint add(int a, int b, int c) { return a + b + c; }\n```\nThe compiler determines at compile time exactly which function to execute based on argument types."
            },
            {
                "heading": "Why Python Doesn't Support Traditional Overloading & How to Emulate It",
                "body": "Because Python is dynamically typed and arguments are evaluated at runtime, defining multiple `def func()` with the same name simply overwrites the previous definition (the last one defined wins).\n\nIn Python, method overloading is emulated through:\n1. **Default & Optional Arguments** (`def add(a, b, c=0)`).\n2. **Variable-length Arguments** (`*args`, `**kwargs`).\n3. **Type-checking logic** (`isinstance()`).\n4. **`functools.singledispatchmethod`**: Decorator from standard library that dispatches methods based on the first argument's type."
            }
        ],
        code_snippets=[
            {
                "title": "Method Overloading Emulation with Default Arguments in Python",
                "language": "python",
                "code": "class Calculator:\n    # Emulate overloading add(a, b) and add(a, b, c)\n    def add(self, a, b, c=None):\n        if c is not None:\n            return a + b + c\n        return a + b\n\ncalc = Calculator()\nprint('Two arguments:', calc.add(5, 10))\nprint('Three arguments:', calc.add(5, 10, 20))",
                "explanation": "Default arguments handle varying parameter counts in a single function."
            },
            {
                "title": "Overloading with Variable-Length Arguments (*args)",
                "language": "python",
                "code": "class MathUtil:\n    def multiply(self, *args):\n        if not args:\n            return 0\n        total = 1\n        for num in args:\n            total *= num\n        return total\n\nm = MathUtil()\nprint('2 numbers:', m.multiply(4, 5))\nprint('4 numbers:', m.multiply(2, 3, 4, 5))",
                "explanation": "*args allows a single method to accept any arbitrary number of parameters."
            },
            {
                "title": "Type-Based Overloading using functools.singledispatchmethod",
                "language": "python",
                "code": "from functools import singledispatchmethod\n\nclass Formatter:\n    @singledispatchmethod\n    def format_data(self, data):\n        return f'Generic: {data}'\n\n    @format_data.register(int)\n    def _(self, data: int):\n        return f'Integer: {data:,}'\n\n    @format_data.register(list)\n    def _(self, data: list):\n        return f'List of {len(data)} items: {\", \".join(str(x) for x in data)}'\n\nf = Formatter()\nprint(f.format_data(1000000))\nprint(f.format_data(['apple', 'banana', 'cherry']))\nprint(f.format_data(3.14159))",
                "explanation": "singledispatchmethod provides true type-based method overloading in modern Python."
            },
            {
                "title": "Java Method Overloading Syntax (Conceptual)",
                "language": "text",
                "code": "// Java Compile-Time Overloading:\n// public void print(int i) { System.out.println(\"Integer: \" + i); }\n// public void print(String s) { System.out.println(\"String: \" + s); }\n// Dispatched strictly at compile time based on parameter type signature!",
                "explanation": "Contrasts Python's runtime dispatch with Java's compile-time signature matching."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Overloaded Area Calculator",
            description="Create an `AreaCalculator` class with a method `area(self, *args)` that computes geometric area based on argument count:\n- 1 argument `r`: Circle area `3.14159 * r * r`\n- 2 arguments `w, h`: Rectangle area `w * h`\n- 3 arguments `a, b, c`: Triangle area using Heron's formula `sqrt(s*(s-a)*(s-b)*(s-c))` where `s = (a+b+c)/2`\n- Otherwise raise `ValueError('Invalid arguments')`.",
            starter_code="class AreaCalculator:\n    # Implement overloaded area(*args)\n    pass",
            solution_code="class AreaCalculator:\n    def area(self, *args) -> float:\n        import math\n        if len(args) == 1:\n            r = args[0]\n            return 3.14159 * r * r\n        elif len(args) == 2:\n            w, h = args\n            return float(w * h)\n        elif len(args) == 3:\n            a, b, c = args\n            s = (a + b + c) / 2.0\n            return math.sqrt(s * (s - a) * (s - b) * (s - c))\n        raise ValueError('Invalid arguments')",
            expected_output="78.53975\n50.0\n6.0"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What constitutes Method Overloading?",
                options=[
                    "Defining multiple methods in the same class with the same name but different parameter signatures (types, counts, or order)",
                    "Redefining a parent class method in a child class with the exact same signature",
                    "Writing an infinite recursive function",
                    "Overloading the electrical circuit breaker in a server rack"
                ],
                correct_answer="Defining multiple methods in the same class with the same name but different parameter signatures (types, counts, or order)",
                explanation="Method Overloading means multiple methods share the same name within a single class but differentiate via parameter signatures."
            ),
            QuizQuestionBlueprint(
                question="Why does standard Python not support multiple `def my_method(...)` declarations with different parameter counts in the same class?",
                options=[
                    "Because Python is dynamically interpreted; defining a method with the same name simply overwrites the previous definition in the class dictionary",
                    "Because Python does not support functions",
                    "Because overloading requires 128-bit CPUs",
                    "Because Python only allows one method per class"
                ],
                correct_answer="Because Python is dynamically interpreted; defining a method with the same name simply overwrites the previous definition in the class dictionary",
                explanation="In Python, functions are first-class objects; a subsequent `def` with the same name replaces the prior reference in the class namespace."
            ),
            QuizQuestionBlueprint(
                question="Which standard library module in Python provides `@singledispatchmethod` for type-based method overloading?",
                options=[
                    "functools",
                    "itertools",
                    "collections",
                    "sys"
                ],
                correct_answer="functools",
                explanation="`functools.singledispatchmethod` enables type-driven method overloading in Python classes."
            ),
            QuizQuestionBlueprint(
                question="In languages with native compile-time overloading (like C++ or Java), when is the exact target method resolved?",
                options=[
                    "At compile time, based on the static types of arguments passed by the caller",
                    "At runtime, by querying a database",
                    "When the user clicks a button",
                    "During operating system shutdown"
                ],
                correct_answer="At compile time, based on the static types of arguments passed by the caller",
                explanation="Compile-time polymorphism resolves method bindings during compilation by analyzing argument types."
            ),
            QuizQuestionBlueprint(
                question="How do Python developers most commonly emulate method overloading for varying argument counts in daily practice?",
                options=[
                    "Using default parameter values (e.g. `def connect(host, port=80, timeout=10)`) or `*args`",
                    "By renaming methods to `method1()`, `method2()`, `method3()`",
                    "By writing the method in C and importing it",
                    "By creating 10 different classes"
                ],
                correct_answer="Using default parameter values (e.g. `def connect(host, port=80, timeout=10)`) or `*args`",
                explanation="Default parameter values and `*args` cleanly accommodate varying parameter counts within a single Python method."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 22: Compile-Time (Operator Overloading)
    # -------------------------------------------------------------
    DayBlueprint(
        order=22,
        title="Day 22: Compile-Time (Operator Overloading)",
        concept="Operator Overloading: Customizing mathematical and comparison operators (`+`, `-`, `*`, `==`, `<`, `len()`) using Python dunder magic methods",
        analogy="Think of the plus sign `+`. What does `+` mean? If you give it numbers (`2 + 3`), it calculates `5` (arithmetic addition). If you give it words (`'hot' + 'dog'`), it calculates `'hotdog'` (string concatenation). If you give it lists (`[1, 2] + [3, 4]`), it merges them into `[1, 2, 3, 4]`. The `+` operator changes its behavior depending on who is using it. Operator Overloading allows you to teach Python how to use `+`, `-`, `*`, and `==` on your own custom objects (like adding two bank balances or two vectors)!",
        theory_sections=[
            {
                "heading": "What is Operator Overloading?",
                "body": "**Operator Overloading** allows standard language operators (such as `+`, `-`, `*`, `==`, `<`, `[]`) to have user-defined meanings when applied to custom objects.\n\nWithout operator overloading, adding two 2D vectors would require clunky method calls like `v1.add_vector(v2)`. With operator overloading, you write natural, mathematical expressions: `v3 = v1 + v2`."
            },
            {
                "heading": "Python's Magic (Dunder) Methods",
                "body": "In Python, operator overloading is achieved by implementing special **Dunder** (Double Underscore) methods:\n- `a + b` calls `a.__add__(b)`\n- `a - b` calls `a.__sub__(b)`\n- `a * b` calls `a.__mul__(b)`\n- `a == b` calls `a.__eq__(b)`\n- `a < b` calls `a.__lt__(b)`\n- `len(a)` calls `a.__len__()`\n- `str(a)` calls `a.__str__()`\n- `repr(a)` calls `a.__repr__()`"
            }
        ],
        code_snippets=[
            {
                "title": "Overloading Arithmetic Operators (+) in a 2D Vector Class",
                "language": "python",
                "code": "class Vector2D:\n    def __init__(self, x: float, y: float):\n        self.x = float(x)\n        self.y = float(y)\n\n    # Overload '+' operator\n    def __add__(self, other: 'Vector2D') -> 'Vector2D':\n        if isinstance(other, Vector2D):\n            return Vector2D(self.x + other.x, self.y + other.y)\n        return NotImplemented\n\n    def __repr__(self):\n        return f'Vector2D({self.x}, {self.y})'\n\nv1 = Vector2D(2, 5)\nv2 = Vector2D(3, 1)\nv3 = v1 + v2  # Triggers v1.__add__(v2)\nprint('Vector Addition:', v3)",
                "explanation": "Implementing __add__ enables natural mathematical syntax with Vector2D instances."
            },
            {
                "title": "Overloading Equality (==) and Comparison (<) Operators",
                "language": "python",
                "code": "class Money:\n    def __init__(self, amount: float, currency: str = 'USD'):\n        self.amount = float(amount)\n        self.currency = currency\n\n    def __eq__(self, other: 'Money') -> bool:\n        if isinstance(other, Money):\n            return self.amount == other.amount and self.currency == other.currency\n        return False\n\n    def __lt__(self, other: 'Money') -> bool:\n        if isinstance(other, Money) and self.currency == other.currency:\n            return self.amount < other.amount\n        raise ValueError('Cannot compare different currencies')\n\nm1 = Money(100, 'USD')\nm2 = Money(100, 'USD')\nm3 = Money(250, 'USD')\nprint('m1 == m2:', m1 == m2)  # True\nprint('m1 < m3:', m1 < m3)    # True",
                "explanation": "Overloading __eq__ and __lt__ allows domain objects to be compared and sorted."
            },
            {
                "title": "Overloading len() and Indexing ([]) Container Operators",
                "language": "python",
                "code": "class PlayList:\n    def __init__(self, name: str):\n        self.name = name\n        self.songs = []\n\n    def add_song(self, song: str):\n        self.songs.append(song)\n\n    def __len__(self) -> int:\n        return len(self.songs)\n\n    def __getitem__(self, index: int) -> str:\n        return self.songs[index]\n\npl = PlayList('Rock Classics')\npl.add_song('Bohemian Rhapsody')\npl.add_song('Stairway to Heaven')\nprint('Playlist length:', len(pl))\nprint('First song:', pl[0])",
                "explanation": "__len__ and __getitem__ make custom objects behave like native Python sequences."
            },
            {
                "title": "C++ Operator Overloading Syntax Comparison",
                "language": "text",
                "code": "// In C++:\n// Vector2D operator+(const Vector2D& other) const {\n//     return Vector2D(this->x + other.x, this->y + other.y);\n// }",
                "explanation": "Contrasts Python's dunder method conventions with C++'s operator keyword syntax."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Complex Number Addition and Multiplication",
            description="Create a `ComplexNumber` class with `real` and `imag` attributes. Overload `__add__` (returns new `ComplexNumber(r1+r2, i1+i2)`), `__mul__` (returns new `ComplexNumber(r1*r2 - i1*i2, r1*i2 + r2*i1)`), and `__repr__` (returns `f'{real}+{imag}i'` or `f'{real}{imag}i'` if imag is negative).",
            starter_code="class ComplexNumber:\n    # Implement ComplexNumber with __add__ and __mul__\n    pass",
            solution_code="class ComplexNumber:\n    def __init__(self, real: float, imag: float):\n        self.real = float(real)\n        self.imag = float(imag)\n\n    def __add__(self, other: 'ComplexNumber') -> 'ComplexNumber':\n        return ComplexNumber(self.real + other.real, self.imag + other.imag)\n\n    def __mul__(self, other: 'ComplexNumber') -> 'ComplexNumber':\n        r = (self.real * other.real) - (self.imag * other.imag)\n        i = (self.real * other.imag) + (self.imag * other.real)\n        return ComplexNumber(r, i)\n\n    def __repr__(self) -> str:\n        sign = '+' if self.imag >= 0 else ''\n        return f'{self.real}{sign}{self.imag}i'",
            expected_output="3.0+5.0i\n-5.0+10.0i"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is Operator Overloading?",
                options=[
                    "Providing custom implementations for standard language operators (like `+`, `-`, `==`, `<`) when applied to user-defined objects",
                    "Running CPU operations above 100% capacity",
                    "Preventing operators from performing math",
                    "Deleting operators from the compiler"
                ],
                correct_answer="Providing custom implementations for standard language operators (like `+`, `-`, `==`, `<`) when applied to user-defined objects",
                explanation="Operator overloading allows custom types to use native operators (+, -, *, ==) naturally."
            ),
            QuizQuestionBlueprint(
                question="Which Python dunder magic method is invoked behind the scenes when the expression `a + b` is executed?",
                options=[
                    "a.__add__(b)",
                    "a.__plus__(b)",
                    "a.__sum__(b)",
                    "a.__append__(b)"
                ],
                correct_answer="a.__add__(b)",
                explanation="The `+` operator maps directly to the `__add__` magic method on the left-hand operand."
            ),
            QuizQuestionBlueprint(
                question="Which magic method must be implemented on a class so that calling `len(my_obj)` returns an integer count?",
                options=[
                    "__len__",
                    "__size__",
                    "__count__",
                    "__length__"
                ],
                correct_answer="__len__",
                explanation="The built-in `len()` function calls the `__len__` method on the target object."
            ),
            QuizQuestionBlueprint(
                question="What does returning `NotImplemented` from an operator method like `__add__` signal to Python?",
                options=[
                    "It tells Python that this type doesn't know how to add the right-hand operand, allowing Python to try `other.__radd__(self)`",
                    "It immediately halts the computer with a Kernel Panic",
                    "It sets the variable to 0",
                    "It converts the operands into strings"
                ],
                correct_answer="It tells Python that this type doesn't know how to add the right-hand operand, allowing Python to try `other.__radd__(self)`",
                explanation="Returning `NotImplemented` enables Python's fallback to the reflected operator (`__radd__`) on the other operand."
            ),
            QuizQuestionBlueprint(
                question="Which magic method overloads the square bracket indexing operator (e.g. `obj[key]` or `obj[index]`)?",
                options=[
                    "__getitem__",
                    "__index__",
                    "__slice__",
                    "__lookup__"
                ],
                correct_answer="__getitem__",
                explanation="`__getitem__` handles square bracket indexing (`obj[i]`), enabling dictionary-like or list-like access."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 23: Run-Time (Method Overriding & Virtual/Magic Methods)
    # -------------------------------------------------------------
    DayBlueprint(
        order=23,
        title="Day 23: Run-Time (Method Overriding & Virtual/Magic Methods)",
        concept="Run-Time Polymorphism: Method Overriding, late dynamic binding (vtable), virtual functions, and overriding standard object dunder methods (`__str__`, `__repr__`)",
        analogy="Imagine a generic recipe for 'Morning Drink': the base recipe says: 'Pour liquid into a mug and drink.' If you are a Coffee Lover, you override that step: 'Grind dark espresso beans, brew with 9-bar pressure, and steam whole milk.' If you are a Tea Enthusiast, you override it: 'Steep Earl Grey leaves in boiling water for 4 minutes.' Both people are executing the exact same morning routine (**drink()**), but how it is performed is decided at runtime by who is standing in the kitchen!",
        theory_sections=[
            {
                "heading": "What is Method Overriding?",
                "body": "**Method Overriding** occurs when a derived subclass provides its own specific implementation of a method that is already defined in its parent superclass. Both methods share the exact same name, return type, and parameters.\n\nAt runtime, when the method is invoked on an instance, the system executes the **subclass version**, not the parent version. This is the cornerstone of **Run-Time Polymorphism** (Dynamic Binding)."
            },
            {
                "heading": "Virtual Methods and the VTable Concept",
                "body": "In compiled languages like C++ and C#, methods are non-virtual by default (bound at compile time). To enable runtime overriding, developers must mark methods with the `virtual` keyword. The compiler builds a **Virtual Method Table (VTable)** storing function pointers for dynamic dispatch.\n\nIn Python and Java, **all methods are virtual by default**. Python resolves method lookups dynamically at runtime through its descriptor protocol and dictionary lookup."
            }
        ],
        code_snippets=[
            {
                "title": "Method Overriding with Dynamic Dispatch in Python",
                "language": "python",
                "code": "class Notification:\n    def send(self, recipient: str, message: str) -> str:\n        return f'Generic notification to {recipient}: {message}'\n\nclass EmailNotification(Notification):\n    def send(self, recipient: str, message: str) -> str:\n        # Override with email-specific protocol\n        return f'Sending SMTP Email to [{recipient}] with subject \"Alert\": {message}'\n\nclass SMSNotification(Notification):\n    def send(self, recipient: str, message: str) -> str:\n        # Override with SMS gateway protocol\n        return f'Dispatching SMS cellular packet to [{recipient}]: {message}'\n\nnotifications = [EmailNotification(), SMSNotification()]\nfor n in notifications:\n    print(n.send('alice@test.com', 'System update scheduled'))",
                "explanation": "Each child class overrides send(), invoked polymorphically at runtime."
            },
            {
                "title": "Overriding __str__ (Human-Readable) and __repr__ (Debug)",
                "language": "python",
                "code": "class Product:\n    def __init__(self, sku: str, price: float):\n        self.sku = sku\n        self.price = price\n\n    # __repr__ is for developers / debugging (unambiguous code representation)\n    def __repr__(self) -> str:\n        return f'Product(sku={self.sku!r}, price={self.price!r})'\n\n    # __str__ is for end-user display (str(p) or print(p))\n    def __str__(self) -> str:\n        return f'Product {self.sku} (${self.price:.2f})'\n\np = Product('SKU-9921', 49.99)\nprint('Using str() / print():', str(p))\nprint('Using repr():', repr(p))",
                "explanation": "Overriding __str__ and __repr__ customizes string formatting across Python."
            },
            {
                "title": "Preventing Accidental Overwrite via super()",
                "language": "python",
                "code": "class AuditedEmail(EmailNotification):\n    def send(self, recipient: str, message: str) -> str:\n        result = super().send(recipient, message)\n        return f'[LOGGED AT RUNTIME] {result}'\n\nprint(AuditedEmail().send('bob@corp.com', 'Hello'))",
                "explanation": "Overriding methods can wrap and augment parent implementations using super()."
            },
            {
                "title": "C++ Virtual Table Concept Comparison",
                "language": "text",
                "code": "// In C++:\n// class Base {\n// public:\n//     virtual void render() { ... } // Enables dynamic dispatch via vtable pointer\n// };",
                "explanation": "Contrasts Python's always-virtual model with C++'s explicit virtual keyword."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Overriding Tax Calculator",
            description="Create a base class `TaxCalculator` with method `calculate_tax(income: float)` returning `income * 0.10` (10% flat tax). Create two subclasses:\n1. `ProgressiveTaxCalculator` overriding it to charge 10% on the first 50,000, and 20% on any amount above 50,000.\n2. `ZeroTaxCalculator` returning 0.0.",
            starter_code="class TaxCalculator:\n    pass\nclass ProgressiveTaxCalculator(TaxCalculator):\n    pass\nclass ZeroTaxCalculator(TaxCalculator):\n    pass",
            solution_code="class TaxCalculator:\n    def calculate_tax(self, income: float) -> float:\n        return float(income) * 0.10\n\nclass ProgressiveTaxCalculator(TaxCalculator):\n    def calculate_tax(self, income: float) -> float:\n        inc = float(income)\n        if inc <= 50000.0:\n            return inc * 0.10\n        return (50000.0 * 0.10) + ((inc - 50000.0) * 0.20)\n\nclass ZeroTaxCalculator(TaxCalculator):\n    def calculate_tax(self, income: float) -> float:\n        return 0.0",
            expected_output="10000.0\n15000.0\n0.0"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the difference between Method Overloading and Method Overriding?",
                options=[
                    "Overloading happens in the same class with different signatures (compile-time); Overriding re-implements a parent's method in a child class with the same signature (run-time)",
                    "Overloading is for integers; Overriding is for strings",
                    "Overriding happens only in procedural programming",
                    "They are identical synonyms"
                ],
                correct_answer="Overloading happens in the same class with different signatures (compile-time); Overriding re-implements a parent's method in a child class with the same signature (run-time)",
                explanation="Overloading is static same-class signature variation; overriding is dynamic subclass re-implementation of an inherited method."
            ),
            QuizQuestionBlueprint(
                question="In Python, which methods in a class are 'virtual' (dynamically dispatched at runtime)?",
                options=[
                    "All standard instance methods are virtual by default",
                    "Only methods decorated with `@virtual`",
                    "Only methods that return integers",
                    "None, Python does not support virtual dispatch"
                ],
                correct_answer="All standard instance methods are virtual by default",
                explanation="In Python, all instance methods are bound dynamically at runtime, making them virtual by default."
            ),
            QuizQuestionBlueprint(
                question="What is the purpose of overriding `__repr__` on a Python class?",
                options=[
                    "To provide an unambiguous, developer-focused code representation of the object (often executable to recreate the object)",
                    "To reboot the Python virtual machine",
                    "To calculate the square root of the object",
                    "To delete the object from memory"
                ],
                correct_answer="To provide an unambiguous, developer-focused code representation of the object (often executable to recreate the object)",
                explanation="`__repr__` is intended for developers, providing detailed, unambiguous representations for debugging and logging."
            ),
            QuizQuestionBlueprint(
                question="In C++, what keyword must be placed before a member function in the base class to permit runtime dynamic overriding?",
                options=[
                    "virtual",
                    "override",
                    "dynamic",
                    "abstract"
                ],
                correct_answer="virtual",
                explanation="C++ requires the `virtual` keyword on base class methods to generate VTable entries for dynamic dispatch."
            ),
            QuizQuestionBlueprint(
                question="If a child class overrides a parent method, how can it still invoke the original parent version from within the override?",
                options=[
                    "By calling `super().method_name()`",
                    "By calling `this.parent()`",
                    "By rewriting the code from scratch",
                    "It is impossible once a method is overridden"
                ],
                correct_answer="By calling `super().method_name()`",
                explanation="`super().method_name()` allows an overriding subclass method to execute the ancestor implementation."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 24: Upcasting and Downcasting (Type Conversion)
    # -------------------------------------------------------------
    DayBlueprint(
        order=24,
        title="Day 24: Upcasting and Downcasting (Type Conversion)",
        concept="Polymorphic Type Conversion: Upcasting (safe widening to general base type) versus Downcasting (narrowing to specific subtype with type checks)",
        analogy="Think of a specialized vehicle like a fire engine: **Upcasting** is treating the fire engine as a generic 'Vehicle'. Anyone can safely say: 'A fire engine IS A vehicle; it can park in a standard garage stall.' Upcasting is always 100% safe. **Downcasting** is taking a generic mystery vehicle parked in the garage and attempting to use its water cannon! That is only safe IF that vehicle is *actually* a fire engine. If it is an ordinary bicycle, pressing the water cannon button will crash!",
        theory_sections=[
            {
                "heading": "Upcasting: Treating Derived Objects as Base Types",
                "body": "**Upcasting** is casting an object reference from a derived class to one of its base classes (widening up the inheritance tree). In statically typed languages (Java, C++, C#), upcasting is implicit and completely safe because an instance of `Dog` is guaranteed to satisfy all contracts of `Animal`.\n\nUpcasting enables writing generic functions that operate on collections of base references (e.g. `List<Animal>`)."
            },
            {
                "heading": "Downcasting & Type Safety",
                "body": "**Downcasting** is casting a base class reference down to a specialized derived class (narrowing down the tree). Downcasting is risky because a generic `Animal` reference might point to a `Cat`, in which case downcasting to `Dog` and calling `dog.fetch_ball()` will cause a fatal runtime crash (e.g., `ClassCastException` in Java).\n\nSafe downcasting requires **Type Checking** (using `isinstance()` in Python, `instanceof` in Java, or `dynamic_cast` in C++) before invoking subtype-specific behavior."
            }
        ],
        code_snippets=[
            {
                "title": "Upcasting and Downcasting Demonstration in Python",
                "language": "python",
                "code": "class Shape:\n    def get_name(self): return 'Generic Shape'\n\nclass Circle(Shape):\n    def get_name(self): return 'Circle'\n    def get_radius(self): return 5.0\n\n# Upcasting: Passing Circle into a function expecting generic Shape\ndef inspect_shape(s: Shape):\n    print('Upcasted access:', s.get_name())\n    \n    # Downcasting check: is it actually a Circle?\n    if isinstance(s, Circle):\n        # Safe downcast: access Circle-specific method\n        print('Downcasted access radius:', s.get_radius())\n    else:\n        print('Not a circle, cannot read radius.')\n\ninspect_shape(Circle())\ninspect_shape(Shape())",
                "explanation": "inspect_shape accepts general Shapes and safely downcasts only after verification."
            },
            {
                "title": "Hazard of Unchecked Downcasting",
                "language": "python",
                "code": "class Square(Shape):\n    def get_name(self): return 'Square'\n\ndef unsafe_downcast(s: Shape):\n    try:\n        # Unchecked access assumes s is a Circle!\n        print(s.get_radius())\n    except AttributeError as e:\n        print('Failed downcast error:', e)\n\nunsafe_downcast(Square())  # Crashes without guard check!",
                "explanation": "Accessing subtype-specific methods on an incompatible object raises AttributeError."
            },
            {
                "title": "Java Explicit Casting Syntax (Conceptual Comparison)",
                "language": "text",
                "code": "// In Java:\n// Animal a = new Dog();         // Upcasting: implicit and safe\n// Dog d = (Dog) a;             // Downcasting: explicit cast\n// if (a instanceof Dog) { ... } // Safe downcast guard",
                "explanation": "Shows Java's static explicit cast syntax compared to Python's dynamic isinstance."
            },
            {
                "title": "Python Script: Filtering Objects by Subtype from a Mixed Collection",
                "language": "python",
                "code": "shapes = [Circle(), Shape(), Square(), Circle()]\n# Downcast filter: collect only Circles\nall_circles = [s for s in shapes if isinstance(s, Circle)]\nprint(f'Found {len(all_circles)} Circle instances in collection.')",
                "explanation": "List comprehensions combined with isinstance perform clean polymorphic downcasting."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Safe Vehicle Downcast Dispatcher",
            description="Create a base class `Vehicle(brand)` and subclasses `Airplane(brand, altitude)` with method `fly()` and `Boat(brand, knots)` with method `sail()`. Write a function `dispatch_vehicle(v: Vehicle) -> str` that returns `f'Flying at {v.altitude} ft'` if v is an Airplane, `f'Sailing at {v.knots} knots'` if v is a Boat, and `'Generic vehicle on ground'` otherwise.",
            starter_code="class Vehicle:\n    pass\nclass Airplane(Vehicle):\n    pass\nclass Boat(Vehicle):\n    pass\ndef dispatch_vehicle(v: Vehicle) -> str:\n    pass",
            solution_code="class Vehicle:\n    def __init__(self, brand: str): self.brand = brand\n\nclass Airplane(Vehicle):\n    def __init__(self, brand: str, altitude: int):\n        super().__init__(brand)\n        self.altitude = altitude\n\nclass Boat(Vehicle):\n    def __init__(self, brand: str, knots: int):\n        super().__init__(brand)\n        self.knots = knots\n\ndef dispatch_vehicle(v: Vehicle) -> str:\n    if isinstance(v, Airplane):\n        return f'Flying at {v.altitude} ft'\n    elif isinstance(v, Boat):\n        return f'Sailing at {v.knots} knots'\n    return 'Generic vehicle on ground'",
            expected_output="Flying at 30000 ft\nSailing at 25 knots\nGeneric vehicle on ground"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the difference between Upcasting and Downcasting?",
                options=[
                    "Upcasting treats a specialized derived object as its general base type (always safe); Downcasting casts a general reference to a specific subtype (requires checks)",
                    "Upcasting increases the font size of code; Downcasting decreases it",
                    "Upcasting is used only in Python; Downcasting is used only in HTML",
                    "There is no difference"
                ],
                correct_answer="Upcasting treats a specialized derived object as its general base type (always safe); Downcasting casts a general reference to a specific subtype (requires checks)",
                explanation="Upcasting widens to an ancestor type safely; downcasting narrows to a specific derived type and requires runtime safety verification."
            ),
            QuizQuestionBlueprint(
                question="Why is Upcasting considered inherently safe in Object-Oriented Programming?",
                options=[
                    "Because by inheritance rules (IS-A), a derived class is guaranteed to satisfy every attribute and method contract exposed by its parent",
                    "Because upcasting deletes all data inside the object",
                    "Because upcasting converts the object into a string",
                    "Because upcasting runs on the GPU"
                ],
                correct_answer="Because by inheritance rules (IS-A), a derived class is guaranteed to satisfy every attribute and method contract exposed by its parent",
                explanation="The Liskov substitution principle ensures that any child object fulfills all contracts expected of its parent."
            ),
            QuizQuestionBlueprint(
                question="What exception is thrown in Java if an invalid downcast is attempted (e.g. casting a Cat object to a Dog)?",
                options=[
                    "ClassCastException",
                    "NullPointerException",
                    "DowncastError",
                    "StackOverflowError"
                ],
                correct_answer="ClassCastException",
                explanation="In Java, casting an object to an incompatible type throws a runtime ClassCastException."
            ),
            QuizQuestionBlueprint(
                question="What Python function should always be called before performing a downcast to verify an object's concrete type?",
                options=[
                    "isinstance(obj, TargetClass)",
                    "type(obj) == 'TargetClass'",
                    "obj.is_a(TargetClass)",
                    "obj.has_parent(TargetClass)"
                ],
                correct_answer="isinstance(obj, TargetClass)",
                explanation="`isinstance(obj, TargetClass)` safely checks if the instance is compatible with the target subtype before invoking specialized methods."
            ),
            QuizQuestionBlueprint(
                question="Why is excessive downcasting often considered a 'code smell' in OOP architecture?",
                options=[
                    "It often indicates poor polymorphic design, where the base class should have defined a virtual method instead of forcing callers to manually inspect types",
                    "It causes physical damage to RAM chips",
                    "It slows down internet connection speeds",
                    "Because downcasting was banned by the W3C"
                ],
                correct_answer="It often indicates poor polymorphic design, where the base class should have defined a virtual method instead of forcing callers to manually inspect types",
                explanation="Frequent type checking and downcasting usually means behavior should have been modeled polymorphically in the base class interface."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 25 (Project): Geometric Shape Area Calculator
    # -------------------------------------------------------------
    DayBlueprint(
        order=25,
        title="Day 25 (Project): Geometric Shape Area Calculator",
        concept="Hands-on Project Day: Polymorphic Geometric Engine with dynamic method overriding, perimeter/area calculations, and heterogeneous collection processing",
        analogy="Think of today's project like a computer-aided drafting (CAD) software engine (like AutoCAD or Blender). The user draws 50 different shapes on screen: circles, rectangles, triangles, and ellipses. When the user clicks the master 'Calculate Total Canvas Area' button, the engine does not care what shapes are on the board: it loops through the collection polymorphically, asking each shape to compute its own area, and sums the total instantly!",
        is_project_day=True,
        project_name="Geometric Shape Area Calculator",
        theory_sections=[
            {
                "heading": "CAD Geometry Engine Design",
                "body": "Today's project builds a polymorphic 2D geometry engine:\n1. **Base Class `Shape`**: Defines common attributes (`color`, `name`) and declares abstract polymorphic method contracts: `area()` and `perimeter()`.\n2. **`Circle`**: Implements area (`pi * r^2`) and perimeter (`2 * pi * r`).\n3. **`Rectangle`**: Implements area (`width * height`) and perimeter (`2 * (width + height)`).\n4. **`Triangle`**: Implements area using Heron's formula and perimeter as sum of 3 sides.\n5. **`Canvas` Manager**: Aggregates a mixed collection of shapes, computing total surface area and rendering ASCII descriptions."
            },
            {
                "heading": "Polymorphic Canvas Operations",
                "body": "The `Canvas` class demonstrates pure runtime polymorphism: it has no knowledge of circle radius or rectangle dimensions. It simply interacts with the uniform `Shape` interface: `s.area()` and `s.perimeter()`."
            }
        ],
        code_snippets=[
            {
                "title": "Base Shape Class and Concrete Subclasses",
                "language": "python",
                "code": "import math\n\nclass Shape:\n    def __init__(self, color: str = 'black'):\n        self.color = color\n\n    def area(self) -> float:\n        raise NotImplementedError('Subclasses must implement area()')\n\n    def perimeter(self) -> float:\n        raise NotImplementedError('Subclasses must implement perimeter()')\n\nclass Circle(Shape):\n    def __init__(self, radius: float, color: str = 'red'):\n        super().__init__(color)\n        self.radius = float(radius)\n    def area(self) -> float: return math.pi * (self.radius ** 2)\n    def perimeter(self) -> float: return 2 * math.pi * self.radius\n\nclass Rectangle(Shape):\n    def __init__(self, width: float, height: float, color: str = 'blue'):\n        super().__init__(color)\n        self.width = float(width)\n        self.height = float(height)\n    def area(self) -> float: return self.width * self.height\n    def perimeter(self) -> float: return 2 * (self.width + self.height)",
                "explanation": "Defines base Shape and concrete Circle and Rectangle implementations."
            },
            {
                "title": "Triangle Implementation using Heron's Formula",
                "language": "python",
                "code": "class Triangle(Shape):\n    def __init__(self, a: float, b: float, c: float, color: str = 'green'):\n        super().__init__(color)\n        self.a, self.b, self.c = float(a), float(b), float(c)\n    def perimeter(self) -> float:\n        return self.a + self.b + self.c\n    def area(self) -> float:\n        s = self.perimeter() / 2.0\n        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))",
                "explanation": "Triangle calculates area via Heron's formula based on 3 sides."
            },
            {
                "title": "Canvas Manager: Polymorphic Total Area and Reports",
                "language": "python",
                "code": "class Canvas:\n    def __init__(self):\n        self.shapes = []\n\n    def add_shape(self, shape: Shape):\n        if isinstance(shape, Shape):\n            self.shapes.append(shape)\n\n    def get_total_area(self) -> float:\n        return sum(s.area() for s in self.shapes)\n\n    def get_total_perimeter(self) -> float:\n        return sum(s.perimeter() for s in self.shapes)\n\n    def generate_report(self):\n        print('=== CANVAS INVENTORY ===')\n        for idx, s in enumerate(self.shapes, 1):\n            print(f'{idx}. {s.color.capitalize()} {type(s).__name__}: Area={s.area():.2f}, Perim={s.perimeter():.2f}')\n        print(f'Total Area: {self.get_total_area():.2f}')",
                "explanation": "Canvas aggregates diverse shapes and queries their metrics polymorphically."
            },
            {
                "title": "Running the Shape Engine Simulation",
                "language": "python",
                "code": "canvas = Canvas()\ncanvas.add_shape(Circle(5.0, 'red'))\ncanvas.add_shape(Rectangle(4.0, 6.0, 'blue'))\ncanvas.add_shape(Triangle(3.0, 4.0, 5.0, 'green'))\ncanvas.generate_report()",
                "explanation": "Executes the CAD canvas simulation across heterogeneous shapes."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Largest Shape Filter on Canvas",
            description="Add a method `get_largest_shape(self) -> Shape` to the `Canvas` class that returns the `Shape` object with the maximum `area()`. If the canvas has no shapes, return `None`.",
            starter_code="class Canvas:\n    # Implement get_largest_shape() method\n    pass",
            solution_code="class Canvas:\n    def __init__(self):\n        self.shapes = []\n    def add_shape(self, s):\n        self.shapes.append(s)\n    def get_largest_shape(self):\n        if not self.shapes:\n            return None\n        return max(self.shapes, key=lambda s: s.area())",
            expected_output="Largest Shape: Circle with area 78.54"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="In the Geometric Shape project, why does `Canvas.get_total_area()` work seamlessly across Circles, Rectangles, and Triangles?",
                options=[
                    "Because every shape overrides the uniform `area()` method contract defined on the base `Shape` class (Polymorphism)",
                    "Because all shapes have the same width and height",
                    "Because Python converts all shapes into squares",
                    "Because the canvas runs on a graphics card"
                ],
                correct_answer="Because every shape overrides the uniform `area()` method contract defined on the base `Shape` class (Polymorphism)",
                explanation="Polymorphism guarantees that each concrete shape implements `area()`, allowing the canvas to compute totals generically."
            ),
            QuizQuestionBlueprint(
                question="Why does the base `Shape` class raise `NotImplementedError` in its default `area()` method?",
                options=[
                    "To enforce that concrete subclasses must override and provide a genuine mathematical formula for area",
                    "Because the computer does not know how to do math",
                    "To crash the program whenever a shape is drawn",
                    "Because base classes cannot contain letters"
                ],
                correct_answer="To enforce that concrete subclasses must override and provide a genuine mathematical formula for area",
                explanation="Raising `NotImplementedError` establishes an abstract interface contract requiring derived classes to provide implementations."
            ),
            QuizQuestionBlueprint(
                question="If you add a new `Hexagon` shape class to the project tomorrow, what changes are required inside `Canvas.get_total_area()`?",
                options=[
                    "Zero changes; the existing canvas loop will call `area()` on Hexagon automatically without modification",
                    "The Canvas class must be completely rewritten",
                    "A new if/else branch checking for Hexagon must be hardcoded",
                    "The operating system must be reinstalled"
                ],
                correct_answer="Zero changes; the existing canvas loop will call `area()` on Hexagon automatically without modification",
                explanation="Polymorphism adheres to the Open/Closed Principle: new shapes integrate without modifying existing consumer code."
            ),
            QuizQuestionBlueprint(
                question="Which formula is used by the `Triangle` class to calculate area from its three side lengths?",
                options=[
                    "Heron's Formula: `sqrt(s * (s - a) * (s - b) * (s - c))` where `s` is semi-perimeter",
                    "Pythagorean Theorem: `a^2 + b^2 = c^2`",
                    "Einstein's formula: `E = mc^2`",
                    "Ohm's Law: `V = I * R`"
                ],
                correct_answer="Heron's Formula: `sqrt(s * (s - a) * (s - b) * (s - c))` where `s` is semi-perimeter",
                explanation="Heron's formula computes triangle area directly from the lengths of its three sides."
            ),
            QuizQuestionBlueprint(
                question="What design relationship exists between `Canvas` and `Shape`?",
                options=[
                    "Aggregation/Composition: Canvas HAS-A collection of Shape objects",
                    "Inheritance: Canvas IS-A Shape",
                    "Operator Overloading",
                    "Procedural Macro"
                ],
                correct_answer="Aggregation/Composition: Canvas HAS-A collection of Shape objects",
                explanation="Canvas aggregates and coordinates a collection of Shape instances."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 26: Concept of Abstraction
    # -------------------------------------------------------------
    DayBlueprint(
        order=26,
        title="Day 26: Concept of Abstraction",
        concept="The Fourth Pillar of OOP: Abstraction - hiding background complexity and exposing essential interface features",
        analogy="Think of driving a modern automobile: to drive, you interact with three simple controls: the steering wheel, the gas pedal, and the brake pedal (**The Clean Abstraction**). You do NOT need to know how the fuel injectors vaporize gasoline at 2,000 PSI, how the anti-lock brake microcontrollers pulse hydraulic calipers 15 times a second, or how the automatic transmission shifts planetary gearsets. Abstraction hides the terrifying mechanical complexity so you can focus on driving!",
        theory_sections=[
            {
                "heading": "What is Abstraction?",
                "body": "**Abstraction** is the process of hiding internal implementation details and showing only the essential features of an object to the user. It answers the question: *'What does this object do?'* while hiding *'How does it do it?'*\n\nAbstraction reduces cognitive load: a software engineer calling `database.connect()` or `stripe.charge_card()` does not need to understand network socket handshakes or TLS cryptographic padding."
            },
            {
                "heading": "Abstraction vs Encapsulation (Key Difference)",
                "body": "Students often confuse these two concepts:\n- **Encapsulation** is about **protection and packaging**: bundling data and methods inside a capsule and shielding access via private variables (Data Hiding).\n- **Abstraction** is about **simplification and hiding complexity**: defining high-level contracts and blueprints while concealing complex algorithmic mechanics."
            }
        ],
        code_snippets=[
            {
                "title": "Abstract High-Level Interface vs Low-Level Mechanical Details",
                "language": "python",
                "code": "class CarEngine:\n    def start(self) -> str:\n        # Clean public abstraction: user just calls .start()\n        self._engage_starter_motor()\n        self._ignite_spark_plugs()\n        self._pump_fuel()\n        return 'Engine purring smoothly!'\n\n    # Complex internal details are hidden behind the scenes\n    def _engage_starter_motor(self): print('Starter motor engaged...')\n    def _ignite_spark_plugs(self): print('Spark plugs firing at 1-3-4-2 order...')\n    def _pump_fuel(self): print('High-pressure direct injection active...')\n\ncar = CarEngine()\nprint(car.start())",
                "explanation": "The caller invokes a simple start() command without managing spark plugs or fuel pumps."
            },
            {
                "title": "Abstracting Cloud Storage Providers",
                "language": "python",
                "code": "class CloudUploader:\n    def upload_file(self, destination: str, data: bytes):\n        # Abstraction hides whether storage is AWS S3, Google Cloud, or Azure\n        print(f'Encrypting {len(data)} bytes...')\n        print(f'Streaming payload to cloud endpoint [{destination}]...')\n        return 'UPLOAD_SUCCESS_200'\n\nuploader = CloudUploader()\nuploader.upload_file('s3://my-bucket/data.csv', b'id,name\\n1,Alice')",
                "explanation": "Callers interact with high-level file upload operations agnostic of cloud infrastructure."
            },
            {
                "title": "Abstracting Database Connection Pooling",
                "language": "python",
                "code": "class DatabaseConnectionPool:\n    def execute(self, sql: str):\n        conn = self._acquire_socket()\n        result = f'Result of [{sql}] via socket {conn}'\n        self._release_socket(conn)\n        return result\n\n    def _acquire_socket(self): return 'socket_fd_4'\n    def _release_socket(self, sock): pass\n\ndb = DatabaseConnectionPool()\nprint(db.execute('SELECT count(*) FROM users'))",
                "explanation": "Socket pooling and memory lifecycle are abstracted away from query execution."
            },
            {
                "title": "Python Script: Demonstrating Conceptual Simplicity",
                "language": "python",
                "code": "# Python's built-in sorted() is a masterclass in abstraction:\n# Behind the scenes, it runs TimSort (hybrid merge/insertion sort).\n# To the user, it is simply sorted(list)!\nprint('Sorted numbers:', sorted([45, 12, 89, 3, 27]))",
                "explanation": "Shows how built-in Python tools abstract sophisticated algorithms behind clean functions."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Abstract Coffee Machine",
            description="Create a `CoffeeMachine` class with a single public method `make_coffee(coffee_type: str) -> str`. Hide private helper methods `_boil_water()`, `_grind_beans(coffee_type)`, and `_brew()`. The public method should coordinate all three helpers and return `f'Delicious cup of {coffee_type} ready!'`.",
            starter_code="class CoffeeMachine:\n    # Implement CoffeeMachine abstraction\n    pass",
            solution_code="class CoffeeMachine:\n    def make_coffee(self, coffee_type: str) -> str:\n        self._boil_water()\n        self._grind_beans(coffee_type)\n        self._brew()\n        return f'Delicious cup of {coffee_type} ready!'\n\n    def _boil_water(self): pass\n    def _grind_beans(self, coffee_type: str): pass\n    def _brew(self): pass",
            expected_output="Delicious cup of Espresso ready!"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the primary objective of Abstraction in Object-Oriented Programming?",
                options=[
                    "Hiding complex implementation details and presenting only essential, high-level features to the user",
                    "Encrypting source code on GitHub",
                    "Making variables accessible from anywhere without security checks",
                    "Writing code that cannot be understood by humans"
                ],
                correct_answer="Hiding complex implementation details and presenting only essential, high-level features to the user",
                explanation="Abstraction hides low-level complexity behind intuitive high-level interfaces, reducing cognitive overhead."
            ),
            QuizQuestionBlueprint(
                question="What is the difference between Abstraction and Encapsulation?",
                options=[
                    "Abstraction focuses on hiding complexity (what an object does); Encapsulation focuses on hiding data and bundling state (protecting how it does it)",
                    "Abstraction is for Java; Encapsulation is for Python",
                    "Abstraction is a compile-time bug; Encapsulation is a runtime error",
                    "There is no difference"
                ],
                correct_answer="Abstraction focuses on hiding complexity (what an object does); Encapsulation focuses on hiding data and bundling state (protecting how it does it)",
                explanation="Abstraction presents simplified conceptual models; encapsulation bundles and shields internal state."
            ),
            QuizQuestionBlueprint(
                question="Which real-world scenario represents an Abstraction?",
                options=[
                    "Pressing the gas pedal in a car without understanding engine fuel injection timing",
                    "Opening a watch with a screwdriver to count the physical gears",
                    "Reading raw binary transistor voltages directly off a microchip",
                    "Manually digging an oil well to fuel your lawnmower"
                ],
                correct_answer="Pressing the gas pedal in a car without understanding engine fuel injection timing",
                explanation="The gas pedal is a classic abstraction: a simple pedal that conceals complex powertrain mechanics."
            ),
            QuizQuestionBlueprint(
                question="How does Abstraction protect callers when a library upgrades its internal algorithm?",
                options=[
                    "Because callers interact only with the abstract interface, internal algorithms can be upgraded without breaking caller code",
                    "By automatically converting Python code into C",
                    "By locking library files against editing",
                    "It does not protect callers"
                ],
                correct_answer="Because callers interact only with the abstract interface, internal algorithms can be upgraded without breaking caller code",
                explanation="Stable abstractions allow internal implementations to be overhauled without breaking consumer contracts."
            ),
            QuizQuestionBlueprint(
                question="In Python, what is an example of built-in high-level abstraction?",
                options=[
                    "The `print()` function: it abstracts operating system file descriptors, buffer flushes, and string encoding into a single command",
                    "Writing raw hex numbers into RAM",
                    "Configuring CPU clock multipliers",
                    "Modifying motherboard voltage"
                ],
                correct_answer="The `print()` function: it abstracts operating system file descriptors, buffer flushes, and string encoding into a single command",
                explanation="`print()` abstracts complex I/O system calls and stream flushes behind a simple, intuitive function."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 27: Abstract Classes and Methods
    # -------------------------------------------------------------
    DayBlueprint(
        order=27,
        title="Day 27: Abstract Classes and Methods",
        concept="Enforcing Architectural Contracts: The `abc` module, `@abstractmethod`, prohibiting instantiation of incomplete classes, and concrete subclass contracts",
        analogy="Think of a franchise legal agreement: McDonald's corporate headquarters issues a Master Franchise Agreement (**Abstract Class**). It mandates: 'Every restaurant must implement `prepare_burgers()`, `serve_fries()`, and `clean_store()` (**Abstract Methods**).' You cannot eat lunch inside a legal agreement (**Cannot instantiate an Abstract Class**). To open a restaurant, you must build an actual physical building (**Concrete Class**) that fulfills every single mandated rule in the contract!",
        theory_sections=[
            {
                "heading": "What is an Abstract Base Class (ABC)?",
                "body": "An **Abstract Class** is a class that cannot be directly instantiated. Its sole purpose is to serve as a formal template or architectural blueprint for subclasses.\n\nAn **Abstract Method** is a method declared in an abstract class with a signature but no concrete implementation body. Concrete subclasses **must** override and implement all abstract methods before Python permits them to be instantiated."
            },
            {
                "heading": "Python's `abc` Module & `@abstractmethod`",
                "body": "In Python, abstract classes are defined by inheriting from `abc.ABC` and decorating abstract methods with `@abstractmethod`:\n```python\nfrom abc import ABC, abstractmethod\n\nclass PaymentProcessor(ABC):\n    @abstractmethod\n    def process_payment(self, amount: float):\n        pass\n```\nIf a developer attempts to instantiate `PaymentProcessor()`, Python immediately raises `TypeError: Can't instantiate abstract class with abstract methods`."
            }
        ],
        code_snippets=[
            {
                "title": "Defining an Abstract Base Class with Python's abc Module",
                "language": "python",
                "code": "from abc import ABC, abstractmethod\n\nclass DatabaseDriver(ABC):\n    @abstractmethod\n    def connect(self) -> str:\n        \"\"\"Establish connection to database server.\"\"\"\n        pass\n\n    @abstractmethod\n    def query(self, sql: str) -> list:\n        \"\"\"Execute SQL query and return rows.\"\"\"\n        pass\n\n# Attempting to instantiate DatabaseDriver directly fails:\ntry:\n    driver = DatabaseDriver()\nexcept TypeError as e:\n    print('Instantiation blocked:', e)",
                "explanation": "Python strictly forbids instantiating abstract base classes with unfulfilled abstract methods."
            },
            {
                "title": "Implementing a Concrete Subclass",
                "language": "python",
                "code": "class PostgreSQLDriver(DatabaseDriver):\n    def __init__(self, host: str):\n        self.host = host\n        self.is_connected = False\n\n    def connect(self) -> str:\n        self.is_connected = True\n        return f'Connected to PostgreSQL at {self.host}'\n\n    def query(self, sql: str) -> list:\n        if not self.is_connected:\n            raise ConnectionError('Not connected!')\n        return [{'result': f'Executed [{sql}] on {self.host}'}]\n\npg = PostgreSQLDriver('localhost:5432')\nprint(pg.connect())\nprint(pg.query('SELECT version();'))",
                "explanation": "PostgreSQLDriver implements all abstract methods, making it fully instantiable."
            },
            {
                "title": "Abstract Classes with Mixed Concrete and Abstract Methods",
                "language": "python",
                "code": "class DataParser(ABC):\n    # Concrete template method sharing common logic\n    def process(self, raw_data: str):\n        cleaned = raw_data.strip()\n        return self.parse(cleaned)\n\n    # Abstract hook method specialized by subclasses\n    @abstractmethod\n    def parse(self, text: str):\n        pass\n\nclass CSVParser(DataParser):\n    def parse(self, text: str):\n        return text.split(',')\n\nprint('Parsed CSV:', CSVParser().process('  apple,banana,cherry  '))",
                "explanation": "Abstract classes can provide shared concrete template methods alongside abstract hooks."
            },
            {
                "title": "Python Script: Checking issubclass and abc registry",
                "language": "python",
                "code": "print('Is PostgreSQLDriver an ABC subclass?', issubclass(PostgreSQLDriver, DatabaseDriver))\nprint('Is pg an instance of DatabaseDriver?', isinstance(pg, DatabaseDriver))",
                "explanation": "Concrete implementations register as valid subclasses of the abstract contract."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Abstract Vehicle Transmission Contract",
            description="Create an abstract class `Vehicle(ABC)` with an abstract method `start_engine() -> str` and a concrete method `honk() -> str` returning `'Beep beep!'`. Create two concrete subclasses: `ElectricCar` returning `'Silent motor started'` and `GasolineCar` returning `'Vroom engine started'`.",
            starter_code="from abc import ABC, abstractmethod\nclass Vehicle(ABC):\n    pass\nclass ElectricCar(Vehicle):\n    pass\nclass GasolineCar(Vehicle):\n    pass",
            solution_code="from abc import ABC, abstractmethod\n\nclass Vehicle(ABC):\n    @abstractmethod\n    def start_engine(self) -> str: pass\n    def honk(self) -> str: return 'Beep beep!'\n\nclass ElectricCar(Vehicle):\n    def start_engine(self) -> str: return 'Silent motor started'\n\nclass GasolineCar(Vehicle):\n    def start_engine(self) -> str: return 'Vroom engine started'",
            expected_output="Silent motor started\nVroom engine started\nBeep beep!"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What happens if you attempt to instantiate an Abstract Base Class that has unfulfilled `@abstractmethod` decorators in Python?",
                options=[
                    "Python raises a `TypeError` indicating that the abstract class cannot be instantiated",
                    "The object is created with empty null values",
                    "The program reboots the operating system",
                    "The methods are filled in with random numbers"
                ],
                correct_answer="Python raises a `TypeError` indicating that the abstract class cannot be instantiated",
                explanation="Python's ABCMeta metaclass intercepts instantiation and raises a TypeError if any abstract methods remain un-implemented."
            ),
            QuizQuestionBlueprint(
                question="Which module in the Python standard library provides the `ABC` base class and the `@abstractmethod` decorator?",
                options=[
                    "abc",
                    "abstract",
                    "oop",
                    "typing"
                ],
                correct_answer="abc",
                explanation="The `abc` (Abstract Base Classes) module provides the tools for defining formal interface contracts."
            ),
            QuizQuestionBlueprint(
                question="Can an Abstract Base Class contain concrete methods with actual implementation code?",
                options=[
                    "Yes, an abstract class can contain a mix of concrete methods and abstract methods (Template Method Pattern)",
                    "No, abstract classes are strictly forbidden from having any implementation code",
                    "Only if the methods are written in C",
                    "Only if the class has no variables"
                ],
                correct_answer="Yes, an abstract class can contain a mix of concrete methods and abstract methods (Template Method Pattern)",
                explanation="Abstract classes frequently provide shared concrete helper/template methods alongside abstract hooks."
            ),
            QuizQuestionBlueprint(
                question="What must a concrete subclass do before Python permits it to be instantiated?",
                options=[
                    "It must override and implement every single abstract method declared in its parent abstract class",
                    "It must be registered with the United States Copyright Office",
                    "It must delete its parent class",
                    "It must disable garbage collection"
                ],
                correct_answer="It must override and implement every single abstract method declared in its parent abstract class",
                explanation="A subclass remains abstract and un-instantiable until all inherited abstract methods are concretely implemented."
            ),
            QuizQuestionBlueprint(
                question="What architectural value do Abstract Classes provide in enterprise software development?",
                options=[
                    "They enforce strict API contracts across large teams, guaranteeing that all plugins and drivers provide required methods",
                    "They speed up internet download speeds",
                    "They eliminate the need to write unit tests",
                    "They prevent code from being compiled"
                ],
                correct_answer="They enforce strict API contracts across large teams, guaranteeing that all plugins and drivers provide required methods",
                explanation="Abstract classes guarantee uniform interfaces across multi-developer projects and plugin architectures."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 28: Interfaces (Pure Abstraction)
    # -------------------------------------------------------------
    DayBlueprint(
        order=28,
        title="Day 28: Interfaces (Pure Abstraction)",
        concept="Pure Interfaces: Contracts with zero implementation state, Java/C# `interface` keyword, Python Protocols (`typing.Protocol`), and Interface Segregation",
        analogy="Think of a standard wall power outlet: the outlet does not care whether you plug in a high-powered gaming PC, a bedside lamp, an electric guitar amplifier, or a toaster. As long as your appliance has a matching standard 3-prong plug (**The Interface**), electricity will flow seamlessly. An Interface is a 100% pure contract: zero internal implementation, just a strict promise of what plugs and sockets must look like!",
        theory_sections=[
            {
                "heading": "What is an Interface?",
                "body": "In Object-Oriented design, an **Interface** is a completely pure abstract contract. It contains **no instance state** (no variables) and **no implementation bodies** (no method code)—only method signatures.\n\nIn languages like Java, C#, and TypeScript, `interface` is a dedicated keyword. Classes use the `implements` keyword to guarantee they fulfill the contract. Because interfaces contain no implementation code, a class can safely implement **multiple interfaces** without ever triggering the Diamond Problem."
            },
            {
                "heading": "Python's Evolution: ABCs vs `typing.Protocol`",
                "body": "In Python, pure interfaces were historically modeled as Abstract Base Classes containing 100% abstract methods.\n\nModern Python 3.8+ introduced **Structural Subtyping** via `typing.Protocol` (PEP 544). With Protocols, a class does not even need to explicitly inherit from the Protocol! If it implements the matching method signatures, it satisfies the interface automatically (static duck typing)."
            }
        ],
        code_snippets=[
            {
                "title": "Defining a Pure Interface using typing.Protocol",
                "language": "python",
                "code": "from typing import Protocol\n\n# Pure Interface defining printable contract\nclass Printable(Protocol):\n    def print_preview(self) -> str:\n        \"\"\"Interface method signature with zero implementation.\"\"\"\n        ...\n\n# Unrelated classes fulfilling the contract without explicit inheritance\nclass Invoice:\n    def __init__(self, inv_id: str, amount: float):\n        self.inv_id = inv_id\n        self.amount = amount\n    def print_preview(self) -> str:\n        return f'Invoice #{self.inv_id}: ${self.amount:.2f}'\n\nclass Photo:\n    def __init__(self, filename: str):\n        self.filename = filename\n    def print_preview(self) -> str:\n        return f'Image: [{self.filename}] rendered at 300 DPI'",
                "explanation": "Invoice and Photo fulfill the Printable protocol without explicit inheritance."
            },
            {
                "title": "Polymorphic Consumer Operating on the Protocol",
                "language": "python",
                "code": "def send_to_printer(item: Printable):\n    # Consumer relies strictly on the interface\n    print('PRINT SPOOLER:', item.print_preview())\n\nsend_to_printer(Invoice('INV-500', 1250.0))\nsend_to_printer(Photo('family_vacation.jpg'))",
                "explanation": "send_to_printer accepts any object satisfying the Printable protocol."
            },
            {
                "title": "Multiple Interface Implementation in Java (Conceptual)",
                "language": "text",
                "code": "// In Java / C#:\n// public interface Serializable { void serialize(); }\n// public interface Loggable { void log(); }\n// public class Document implements Serializable, Loggable {\n//     public void serialize() { ... }\n//     public void log() { ... }\n// }",
                "explanation": "Contrasts Python protocols with Java's explicit interface implementation."
            },
            {
                "title": "Python Script: Runtime Protocol Validation with runtime_checkable",
                "language": "python",
                "code": "from typing import runtime_checkable\n\n@runtime_checkable\nclass AutoCloseable(Protocol):\n    def close(self) -> None: ...\n\nclass CustomSocket:\n    def close(self): print('Socket closed.')\n\nprint('Does CustomSocket satisfy AutoCloseable?', isinstance(CustomSocket(), AutoCloseable))",
                "explanation": "@runtime_checkable allows isinstance checks against structural protocols."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Notification Sender Protocol",
            description="Create a Protocol `NotificationSender(Protocol)` declaring `send(recipient: str, msg: str) -> bool`. Create two independent classes `EmailSender` and `TelegramSender` that fulfill this protocol without inheriting from it. Write a function `dispatch_alert(sender: NotificationSender, user: str, msg: str)` that invokes `send()`.",
            starter_code="from typing import Protocol\nclass NotificationSender(Protocol):\n    pass\nclass EmailSender:\n    pass\nclass TelegramSender:\n    pass\ndef dispatch_alert(sender: NotificationSender, user: str, msg: str):\n    pass",
            solution_code="from typing import Protocol\n\nclass NotificationSender(Protocol):\n    def send(self, recipient: str, msg: str) -> bool: ...\n\nclass EmailSender:\n    def send(self, recipient: str, msg: str) -> bool:\n        print(f'Email to {recipient}: {msg}')\n        return True\n\nclass TelegramSender:\n    def send(self, recipient: str, msg: str) -> bool:\n        print(f'Telegram to {recipient}: {msg}')\n        return True\n\ndef dispatch_alert(sender: NotificationSender, user: str, msg: str) -> bool:\n    return sender.send(user, msg)",
            expected_output="Email to user@test.com: Server Alert\nTelegram to @telegram_user: Server Alert"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the defining characteristic of a 'Pure Interface' in Object-Oriented design?",
                options=[
                    "It contains method declarations and signatures only, with zero state (variables) and zero implementation code",
                    "It has a graphical user interface window",
                    "It is written entirely in binary machine code",
                    "It can only be used once per project"
                ],
                correct_answer="It contains method declarations and signatures only, with zero state (variables) and zero implementation code",
                explanation="A pure interface is an unadulterated contract declaring *what* operations must exist without implementing any of them."
            ),
            QuizQuestionBlueprint(
                question="Why can a class in Java or C# implement 10 different interfaces without triggering the Diamond Problem?",
                options=[
                    "Because interfaces contain no implementation code bodies, eliminating any possibility of conflicting code execution",
                    "Because Java compiles code directly to quantum circuits",
                    "Because interfaces are converted into comments by the compiler",
                    "Because Java only runs on computers with 10 CPU cores"
                ],
                correct_answer="Because interfaces contain no implementation code bodies, eliminating any possibility of conflicting code execution",
                explanation="Because interfaces specify only signatures without implementations, multiple interfaces cannot create conflicting method bodies."
            ),
            QuizQuestionBlueprint(
                question="What feature introduced in Python 3.8 (PEP 544) allows structural subtyping (compile-time duck typing interfaces)?",
                options=[
                    "typing.Protocol",
                    "abc.PureInterface",
                    "sys.interface",
                    "struct.contract"
                ],
                correct_answer="typing.Protocol",
                explanation="`typing.Protocol` enables formal structural typing (interfaces) where classes satisfy contracts by shape rather than explicit inheritance."
            ),
            QuizQuestionBlueprint(
                question="How does an Interface differ from an Abstract Class?",
                options=[
                    "An Abstract Class can contain concrete methods and instance variables; an Interface contains only method signatures and contracts",
                    "An Interface can only be written in French",
                    "Abstract classes cannot have names",
                    "Interfaces cannot be imported into Python files"
                ],
                correct_answer="An Abstract Class can contain concrete methods and instance variables; an Interface contains only method signatures and contracts",
                explanation="Abstract classes can mix concrete implementations with abstract methods, whereas pure interfaces contain zero implementation."
            ),
            QuizQuestionBlueprint(
                question="What decorator makes a Python `typing.Protocol` checkable at runtime using `isinstance()`?",
                options=[
                    "@runtime_checkable",
                    "@interface_validate",
                    "@is_protocol",
                    "@dynamic_check"
                ],
                correct_answer="@runtime_checkable",
                explanation="Decorating a Protocol with `@runtime_checkable` allows Python's `isinstance(obj, MyProtocol)` to verify structural compliance."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 29: Abstract Class vs Interface (When to use what)
    # -------------------------------------------------------------
    DayBlueprint(
        order=29,
        title="Day 29: Abstract Class vs Interface (When to Use What)",
        concept="Architectural Decision Matrix: Comparing Abstract Classes vs Pure Interfaces, code sharing vs role capability contracts, and hybrid architectures",
        analogy="Think of building military aircraft: a **Base Abstract Class** is `Airplane`—it provides physical wings, jet fuel tanks, and hydraulic landing gear code that all planes share. An **Interface** is a role-based certification: `CanFlyAtNight`, `CanLandOnWater`, or `HasEjectionSeat`. A plane inherits its core physical foundation from `Airplane`, but implements multiple capability interfaces (`CanFlyAtNight`, `CanLandOnWater`).",
        theory_sections=[
            {
                "heading": "Abstract Class vs Interface: The Core Differences",
                "body": "| Dimension | Abstract Class | Interface / Protocol |\n| :--- | :--- | :--- |\n| **Relationship** | **IS-A** identity (e.g. Dog IS-A Animal) | **CAN-DO** capability (e.g. Duck CAN-DO Flyable) |\n| **State** | Can hold instance variables & constructors | Strictly no state or variables |\n| **Implementation** | Can provide shared concrete helper methods | Method signatures only |\n| **Multiple Inheritance** | Prohibited in Java/C#, complex in Python | Safe across all languages |"
            },
            {
                "heading": "Decision Matrix: When to Use What?",
                "body": "- **Use an Abstract Class when**:\n  - You want to share common code, state variables, or utility methods across closely related subclasses.\n  - You expect derived classes to share a common conceptual ancestor.\n  - You are using the **Template Method Pattern**.\n- **Use an Interface / Protocol when**:\n  - You want to define a specific role or capability (`Serializable`, `Comparable`, `Closeable`) implemented by completely unrelated classes.\n  - You want structural decoupling and multiple contract conformance."
            }
        ],
        code_snippets=[
            {
                "title": "Combining an Abstract Class (Core State) with Interfaces (Capabilities)",
                "language": "python",
                "code": "from abc import ABC, abstractmethod\nfrom typing import Protocol, runtime_checkable\n\n# Role Capability Interface (CAN-DO)\n@runtime_checkable\nclass Flyable(Protocol):\n    def fly(self) -> str: ...\n\n# Base Abstract Class (IS-A identity + shared state)\nclass Bird(ABC):\n    def __init__(self, species: str):\n        self.species = species\n    @abstractmethod\n    def lay_eggs(self) -> int: pass\n\n# Duck is a Bird (inherits eggs) AND implements Flyable\nclass Duck(Bird):\n    def lay_eggs(self) -> int: return 4\n    def fly(self) -> str: return f'{self.species} flying in V-formation!'\n\n# Penguin is a Bird, but CANNOT fly\nclass Penguin(Bird):\n    def lay_eggs(self) -> int: return 1\n\nduck = Duck('Mallard')\npenguin = Penguin('Emperor')\nprint('Is duck Flyable?', isinstance(duck, Flyable))        # True\nprint('Is penguin Flyable?', isinstance(penguin, Flyable))  # False!",
                "explanation": "Cleanly decouples class identity (Bird) from optional capability roles (Flyable)."
            },
            {
                "title": "Software Architecture Example: Data Source and Closable Interface",
                "language": "python",
                "code": "class StorageSource(ABC):\n    def __init__(self, uri: str):\n        self.uri = uri\n    @abstractmethod\n    def read_block(self) -> bytes: pass\n\nclass Closeable(Protocol):\n    def close(self) -> None: ...\n\nclass FileStorage(StorageSource):\n    def read_block(self) -> bytes: return b'data'\n    def close(self): print('File handle closed')",
                "explanation": "Illustrates how enterprise storage classes combine base identity with lifecycle protocols."
            },
            {
                "title": "Anti-Pattern: Polluting Base Classes with Unused Methods",
                "language": "python",
                "code": "# Bad: Putting fly() in Bird forces Penguins and Ostriches to throw exceptions!\n# class BadBird(ABC):\n#     @abstractmethod\n#     def fly(self): pass  # Violates Liskov Substitution Principle!\n#\n# Solution: Keep Bird clean; extract Flyable into an independent Interface!",
                "explanation": "Shows how interfaces prevent base class pollution and LSP violations."
            },
            {
                "title": "Python Script: Architectural Contract Verification",
                "language": "python",
                "code": "print('Duck MRO:', [c.__name__ for c in Duck.__mro__])\nprint('Duck satisfies Flyable capability without MRO pollution!')",
                "explanation": "Confirms structural protocols provide capability guarantees without deep inheritance chains."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Game Entity Architecture (Abstract Base + Interfaces)",
            description="Create an abstract class `GameEntity(ABC)` with attribute `name: str` and abstract method `update()`. Create a Protocol `Damageable(Protocol)` declaring `take_damage(amount: int)`. Implement concrete class `Monster(GameEntity)` with `health: int` that implements both `update()` and `take_damage(amount: int)`.",
            starter_code="from abc import ABC, abstractmethod\nfrom typing import Protocol\nclass GameEntity(ABC):\n    pass\nclass Damageable(Protocol):\n    pass\nclass Monster(GameEntity):\n    pass",
            solution_code="from abc import ABC, abstractmethod\nfrom typing import Protocol\n\nclass GameEntity(ABC):\n    def __init__(self, name: str):\n        self.name = name\n    @abstractmethod\n    def update(self) -> str: pass\n\nclass Damageable(Protocol):\n    def take_damage(self, amount: int) -> int: ...\n\nclass Monster(GameEntity):\n    def __init__(self, name: str, health: int):\n        super().__init__(name)\n        self.health = int(health)\n\n    def update(self) -> str:\n        return f'{self.name} patrol AI active'\n\n    def take_damage(self, amount: int) -> int:\n        self.health = max(0, self.health - amount)\n        return self.health",
            expected_output="Goblin patrol AI active\nRemaining Health: 70"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What rule of thumb distinguishes when to use an Abstract Class versus an Interface?",
                options=[
                    "Use Abstract Classes for core 'IS-A' identity and sharing implementation code; use Interfaces for peripheral 'CAN-DO' capabilities across unrelated classes",
                    "Abstract Classes are for math; Interfaces are for graphics",
                    "Use Interfaces on Linux and Abstract Classes on Windows",
                    "Always use Abstract Classes because Interfaces are deprecated"
                ],
                correct_answer="Use Abstract Classes for core 'IS-A' identity and sharing implementation code; use Interfaces for peripheral 'CAN-DO' capabilities across unrelated classes",
                explanation="Abstract classes model core identity and shared state (IS-A); interfaces model orthogonal capabilities (CAN-DO)."
            ),
            QuizQuestionBlueprint(
                question="Why is placing an optional capability method like `fly()` inside a base `Bird` abstract class considered a design defect?",
                options=[
                    "Because flightless birds (like Penguins and Ostriches) would inherit a method they cannot perform, forcing them to raise dummy errors",
                    "Because birds cannot be modeled in code",
                    "Because Python does not support wings",
                    "Because bird feathers take up too much memory"
                ],
                correct_answer="Because flightless birds (like Penguins and Ostriches) would inherit a method they cannot perform, forcing them to raise dummy errors",
                explanation="Forcing subclasses to inherit methods they cannot fulfill violates the Interface Segregation and Liskov Substitution principles."
            ),
            QuizQuestionBlueprint(
                question="Can an Interface hold concrete member variables (like `self.balance = 100`)?",
                options=[
                    "No, pure interfaces are strictly stateless contracts containing method signatures only",
                    "Yes, interfaces always hold all variables",
                    "Only if the variable is a boolean",
                    "Yes, in Python 2 only"
                ],
                correct_answer="No, pure interfaces are strictly stateless contracts containing method signatures only",
                explanation="Interfaces are purely behavioral contracts; they do not hold instance state or allocate memory for fields."
            ),
            QuizQuestionBlueprint(
                question="Which design pattern commonly combines abstract base classes with template methods?",
                options=[
                    "The Template Method Pattern",
                    "The Anti-Pattern",
                    "The Spaghetti Pattern",
                    "The Copy-Paste Pattern"
                ],
                correct_answer="The Template Method Pattern",
                explanation="The Template Method pattern defines an algorithm's skeleton in an abstract class, deferring specific steps to subclasses."
            ),
            QuizQuestionBlueprint(
                question="How does combining an Abstract Class with multiple Protocol interfaces enhance software architecture?",
                options=[
                    "It gives objects a single stable parent identity while allowing them to fulfill multiple diverse roles across different subsystems safely",
                    "It eliminates the need for software testing",
                    "It makes code compile in 0 seconds",
                    "It doubles the computer's CPU clock frequency"
                ],
                correct_answer="It gives objects a single stable parent identity while allowing them to fulfill multiple diverse roles across different subsystems safely",
                explanation="Combining base classes with interfaces provides the benefits of code reuse without sacrificing flexibility or modular role adherence."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 30 (Project): Payment Gateway Interface Simulation
    # -------------------------------------------------------------
    DayBlueprint(
        order=30,
        title="Day 30 (Project): Payment Gateway Interface Simulation",
        concept="Hands-on Project Day: Engineering a pluggable multi-vendor payment gateway architecture using Abstract Classes, Protocol Interfaces, and unified transaction processing",
        analogy="Think of an e-commerce checkout page: the shopper can choose to pay with Credit Card (Stripe), PayPal, or Crypto (Bitcoin). The shopping cart checkout button does not care which vendor you pick! The checkout code calls `payment_gateway.process_transaction(amount)` on a uniform **PaymentGateway Interface**. Behind the scenes, Stripe talks to credit card networks, PayPal opens an OAuth modal, and Bitcoin creates a blockchain address. The checkout engine remains 100% clean and decoupled!",
        is_project_day=True,
        project_name="Payment Gateway Interface Simulation",
        theory_sections=[
            {
                "heading": "Pluggable Architecture Design",
                "body": "In commercial software, hardcoding vendor APIs directly into business logic is a catastrophic anti-pattern. If you hardcode PayPal, switching to Stripe requires rewriting thousands of lines of code.\n\nA **Pluggable Payment Gateway** decouples business logic from vendor APIs:\n1. **`PaymentGateway` Interface / ABC**: Declares universal contracts: `authenticate()`, `charge(amount)`, `refund(transaction_id)`.\n2. **Concrete Gateways**:\n   - `StripeGateway`: Validates card token and charges via simulated Stripe API.\n   - `PayPalGateway`: Authenticates client credentials and transfers via simulated PayPal API.\n   - `CryptoGateway`: Generates public blockchain address and awaits confirmations.\n3. **`CheckoutService`**: Accepts orders and coordinates payment through whichever gateway is injected."
            },
            {
                "heading": "Standardized Transaction Receipts",
                "body": "Every concrete gateway must translate disparate vendor responses into a single, standardized `TransactionReceipt` object containing:\n- `status`: `'SUCCESS'` or `'FAILED'`\n- `transaction_id`: Unique tracking string\n- `amount_charged`: Float\n- `gateway_name`: String identifier"
            }
        ],
        code_snippets=[
            {
                "title": "TransactionReceipt Data Model and Abstract PaymentGateway",
                "language": "python",
                "code": "from abc import ABC, abstractmethod\nfrom dataclasses import dataclass\nimport uuid\n\n@dataclass\nclass TransactionReceipt:\n    transaction_id: str\n    gateway_name: str\n    amount: float\n    status: str\n    message: str\n\nclass PaymentGateway(ABC):\n    def __init__(self, api_key: str):\n        self.api_key = api_key\n\n    @abstractmethod\n    def authenticate(self) -> bool:\n        \"\"\"Verify API credentials.\"\"\"\n        pass\n\n    @abstractmethod\n    def charge(self, amount: float) -> TransactionReceipt:\n        \"\"\"Execute credit or debit charge.\"\"\"\n        pass",
                "explanation": "Defines standardized receipt structure and abstract payment gateway contract."
            },
            {
                "title": "Concrete Implementations: Stripe and PayPal Gateways",
                "language": "python",
                "code": "class StripeGateway(PaymentGateway):\n    def authenticate(self) -> bool:\n        return self.api_key.startswith('stripe_key_')\n\n    def charge(self, amount: float) -> TransactionReceipt:\n        if not self.authenticate():\n            return TransactionReceipt(str(uuid.uuid4())[:8], 'Stripe', amount, 'FAILED', 'Invalid API key')\n        if amount <= 0:\n            return TransactionReceipt(str(uuid.uuid4())[:8], 'Stripe', amount, 'FAILED', 'Invalid amount')\n        tx_id = f'ch_stripe_{str(uuid.uuid4())[:8]}'\n        return TransactionReceipt(tx_id, 'Stripe', amount, 'SUCCESS', 'Card charged via Stripe network')\n\nclass PayPalGateway(PaymentGateway):\n    def authenticate(self) -> bool:\n        return len(self.api_key) >= 10\n\n    def charge(self, amount: float) -> TransactionReceipt:\n        if not self.authenticate():\n            return TransactionReceipt(str(uuid.uuid4())[:8], 'PayPal', amount, 'FAILED', 'OAuth failed')\n        tx_id = f'PAYPAL-TX-{str(uuid.uuid4())[:8]}'\n        return TransactionReceipt(tx_id, 'PayPal', amount, 'SUCCESS', 'Funds transferred via PayPal account')",
                "explanation": "Concrete gateways implement authentications and return standardized receipts."
            },
            {
                "title": "Checkout Service: Decoupled Gateway Injection",
                "language": "python",
                "code": "class CheckoutService:\n    def __init__(self, gateway: PaymentGateway):\n        self.gateway = gateway\n\n    def process_order(self, customer_name: str, total_amount: float) -> TransactionReceipt:\n        print(f'Initiating checkout for {customer_name} via {type(self.gateway).__name__}...')\n        receipt = self.gateway.charge(total_amount)\n        print(f'Payment Outcome: {receipt.status} | TX ID: {receipt.transaction_id}')\n        return receipt\n\n# Swap gateways with zero changes to CheckoutService logic!\ncheckout_stripe = CheckoutService(StripeGateway('stripe_key_998877'))\nreceipt1 = checkout_stripe.process_order('Alice', 149.99)\n\ncheckout_paypal = CheckoutService(PayPalGateway('PAYPAL_CLIENT_SECRET_KEY'))\nreceipt2 = checkout_paypal.process_order('Bob', 79.50)",
                "explanation": "CheckoutService processes payments polymorphically without knowing gateway vendor details."
            },
            {
                "title": "Python Script: Verifying Payment Audit History",
                "language": "python",
                "code": "audit_log = [receipt1, receipt2]\nfor r in audit_log:\n    print(f'Audit: Gateway={r.gateway_name} | Amount=${r.amount} | Status={r.status}')",
                "explanation": "Iterates over uniform transaction receipts produced across different vendors."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Add Crypto Payment Gateway",
            description="Implement a concrete `CryptoGateway(PaymentGateway)` where `authenticate()` returns `True` if `api_key.startswith('wallet_')`. The `charge(amount)` method returns a `TransactionReceipt` with `gateway_name='Crypto'`, status `'SUCCESS'`, and transaction_id `f'0x{uuid}'` if authenticated, else `'FAILED'`.",
            starter_code="class CryptoGateway(PaymentGateway):\n    # Implement CryptoGateway\n    pass",
            solution_code="class CryptoGateway(PaymentGateway):\n    def authenticate(self) -> bool:\n        return self.api_key.startswith('wallet_')\n\n    def charge(self, amount: float) -> TransactionReceipt:\n        if not self.authenticate():\n            return TransactionReceipt('0x0', 'Crypto', amount, 'FAILED', 'Invalid wallet key')\n        import uuid\n        tx_id = f'0x{str(uuid.uuid4())[:8]}'\n        return TransactionReceipt(tx_id, 'Crypto', amount, 'SUCCESS', 'Blockchain transaction confirmed')",
            expected_output="Outcome: SUCCESS | Gateway: Crypto"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Why is decoupling `CheckoutService` from specific payment gateways using an abstract interface considered a best practice?",
                options=[
                    "It allows adding or switching payment vendors (Stripe, PayPal, Apple Pay) without modifying any checkout business logic",
                    "It eliminates credit card transaction fees",
                    "It allows customers to get free products",
                    "Because credit card numbers cannot be stored in Python"
                ],
                correct_answer="It allows adding or switching payment vendors (Stripe, PayPal, Apple Pay) without modifying any checkout business logic",
                explanation="Dependency Inversion and Abstraction decouple core checkout workflows from volatile third-party vendor APIs."
            ),
            QuizQuestionBlueprint(
                question="What role does `TransactionReceipt` play in the payment gateway architecture?",
                options=[
                    "It standardizes disparate vendor response structures into a uniform, consistent object for accounting and auditing",
                    "It generates paper printouts on a physical receipt printer",
                    "It acts as a malware scanner",
                    "It resets the customer's password"
                ],
                correct_answer="It standardizes disparate vendor response structures into a uniform, consistent object for accounting and auditing",
                explanation="A standardized receipt normalizes differing vendor payloads into a single schema for the rest of the application."
            ),
            QuizQuestionBlueprint(
                question="What design pattern is demonstrated by passing the specific `PaymentGateway` instance into `CheckoutService.__init__(gateway)`?",
                options=[
                    "Dependency Injection",
                    "Singleton",
                    "God Object",
                    "Spaghetti Pattern"
                ],
                correct_answer="Dependency Injection",
                explanation="Injecting the gateway dependency via the constructor allows flexible configuration and trivial mock testing."
            ),
            QuizQuestionBlueprint(
                question="What happens if a developer creates a new `ApplePayGateway(PaymentGateway)` but forgets to implement `charge()`?",
                options=[
                    "Python raises a `TypeError` and blocks instantiation when `ApplePayGateway()` is called",
                    "Apple Pay charges $1000 automatically",
                    "The checkout button disappears",
                    "The method is filled in with random credit card numbers"
                ],
                correct_answer="Python raises a `TypeError` and blocks instantiation when `ApplePayGateway()` is called",
                explanation="Because `charge()` is an `@abstractmethod`, Python enforces its implementation before allowing instantiation."
            ),
            QuizQuestionBlueprint(
                question="How does the Payment Gateway project embody the Open/Closed Principle (OCP)?",
                options=[
                    "The system is open for extension (new payment gateways can be created), but closed for modification (CheckoutService never needs to be edited)",
                    "The bank account is open on weekdays and closed on weekends",
                    "Files are opened with `open()` and closed with `close()`",
                    "The project requires no password to download"
                ],
                correct_answer="The system is open for extension (new payment gateways can be created), but closed for modification (CheckoutService never needs to be edited)",
                explanation="OCP allows adding new gateways freely without touching existing, tested checkout logic."
            )
        ]
    )
]
