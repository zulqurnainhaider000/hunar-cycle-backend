"""
Object-Oriented Programming (OOP) - 55-Day Curriculum - Part 3 (Days 31 to 42)
Module 6: Object Relationships & Associations (Days 31-35)
Module 7: Advanced OOP Concepts (Days 36-41)
Module 8: OOAD (Day 42)
"""

from seeder.course_blueprint import DayBlueprint, QuizQuestionBlueprint, CodingChallengeBlueprint

DAYS_31_TO_42 = [
    # -------------------------------------------------------------
    # DAY 31: Association (General relationships)
    # -------------------------------------------------------------
    DayBlueprint(
        order=31,
        title="Day 31: Association (General Relationships)",
        concept="Object Relationships: Understanding Association - bidirectional and unidirectional peer relationships between independent objects",
        analogy="Think of a Doctor and a Patient: Doctor Smith treats Patient Alice. Dr. Smith can exist completely independently of Alice (if Alice moves away, Dr. Smith is still a doctor). Alice can exist completely independently of Dr. Smith (she can change doctors or go home). They are two autonomous entities linked by an appointment (**Association**). Neither owns or controls the other's lifespan!",
        theory_sections=[
            {
                "heading": "What is an Association?",
                "body": "**Association** represents a general structural relationship between two or more independent classes where objects communicate through messages or method calls. Unlike Inheritance (IS-A), Association models how peer objects interact.\n\nAssociations can be:\n1. **Unidirectional**: Object A knows about Object B, but B does not know about A (e.g., an Order knows its PaymentMethod, but PaymentMethod has no idea what Order used it).\n2. **Bidirectional**: Both objects hold references to each other (e.g., a Driver has a Car, and the Car knows its assigned Driver).\n3. **Multiplicity / Cardinality**: 1-to-1, 1-to-Many, or Many-to-Many."
            },
            {
                "heading": "Independent Lifetimes in Associations",
                "body": "The defining hallmark of a basic Association is **independent lifecycles**: neither object owns the other. Destroying a `Doctor` object does not delete the `Patient` objects, and vice versa."
            }
        ],
        code_snippets=[
            {
                "title": "Unidirectional Association: Student and Course",
                "language": "python",
                "code": "class Course:\n    def __init__(self, code: str, title: str):\n        self.code = code\n        self.title = title\n\nclass Student:\n    def __init__(self, name: str):\n        self.name = name\n        # Unidirectional association: Student maintains references to Courses\n        self.enrolled_courses = []\n\n    def enroll(self, course: Course):\n        if course not in self.enrolled_courses:\n            self.enrolled_courses.append(course)\n\nmath = Course('MATH101', 'Calculus')\nalice = Student('Alice')\nalice.enroll(math)\nprint(f'{alice.name} is taking {[c.title for c in alice.enrolled_courses]}')",
                "explanation": "Student associates with Course; Course exists independently."
            },
            {
                "title": "Bidirectional Association: Driver and Taxi",
                "language": "python",
                "code": "class Driver:\n    def __init__(self, name: str):\n        self.name = name\n        self.taxi = None  # Reference to Taxi\n\n    def assign_taxi(self, taxi: 'Taxi'):\n        self.taxi = taxi\n        taxi.driver = self\n\nclass Taxi:\n    def __init__(self, plate_number: str):\n        self.plate_number = plate_number\n        self.driver = None  # Reference back to Driver\n\nd = Driver('John')\nt = Taxi('TX-987')\nd.assign_taxi(t)\nprint('Driver taxi:', d.taxi.plate_number)\nprint('Taxi driver:', t.driver.name)",
                "explanation": "Both objects hold mutual references, establishing a two-way link."
            },
            {
                "title": "Many-to-Many Association: Doctors and Patients",
                "language": "python",
                "code": "class Doctor:\n    def __init__(self, name: str):\n        self.name = name\n        self.patients = []\n    def add_patient(self, p: 'Patient'):\n        if p not in self.patients: self.patients.append(p)\n\nclass Patient:\n    def __init__(self, name: str):\n        self.name = name\n        self.doctors = []\n    def consult(self, d: Doctor):\n        if d not in self.doctors: self.doctors.append(d)\n        d.add_patient(self)\n\ndr = Doctor('Dr. Adams')\npt = Patient('Charlie')\npt.consult(dr)\nprint(f'{dr.name} patients: {[p.name for p in dr.patients]}')",
                "explanation": "Demonstrates bidirectional Many-to-Many association modeling."
            },
            {
                "title": "Python Script: Proving Independent Lifetimes",
                "language": "python",
                "code": "# Deleting the doctor does NOT destroy the patient!\ndoc_name = dr.name\ndel dr\nprint('Patient still exists safely:', pt.name)",
                "explanation": "Verifies that associations do not cascade object deletions."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Book and Author Association",
            description="Create an `Author` class (name) and a `Book` class (title, author: Author). Implement a bidirectional link: when `Book(title, author)` is instantiated, it automatically adds itself to the `author.books` list.",
            starter_code="class Author:\n    pass\nclass Book:\n    pass",
            solution_code="class Author:\n    def __init__(self, name: str):\n        self.name = name\n        self.books = []\n\nclass Book:\n    def __init__(self, title: str, author: Author):\n        self.title = title\n        self.author = author\n        if self not in author.books:\n            author.books.append(self)",
            expected_output="Author Orwell has books: ['1984', 'Animal Farm']"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What characterizes an Association relationship in Object-Oriented design?",
                options=[
                    "A peer relationship where objects know about each other and communicate, but have independent lifecycles without ownership",
                    "An inheritance relationship where one class is a subtype of another",
                    "A relationship where deleting one object deletes all connected objects",
                    "A function that runs in a background thread"
                ],
                correct_answer="A peer relationship where objects know about each other and communicate, but have independent lifecycles without ownership",
                explanation="Association models peer interactions where objects are connected without possessing ownership of each other's lifecycles."
            ),
            QuizQuestionBlueprint(
                question="What is the difference between a Unidirectional and a Bidirectional association?",
                options=[
                    "In unidirectional, only one object holds a reference to the other; in bidirectional, both objects hold references to each other",
                    "Unidirectional runs forward in time; bidirectional runs backward in time",
                    "Unidirectional uses strings; bidirectional uses integers",
                    "There is no difference"
                ],
                correct_answer="In unidirectional, only one object holds a reference to the other; in bidirectional, both objects hold references to each other",
                explanation="Unidirectional navigation flows one way; bidirectional allows two-way traversal."
            ),
            QuizQuestionBlueprint(
                question="If Object A is associated with Object B, what happens to Object B when Object A is deleted from memory?",
                options=[
                    "Object B continues to exist normally because their lifecycles are independent",
                    "Object B is automatically deleted by the garbage collector",
                    "Object B throws a NullPointerException",
                    "Object B is converted into an abstract class"
                ],
                correct_answer="Object B continues to exist normally because their lifecycles are independent",
                explanation="In standard associations, objects maintain separate, independent lifetimes."
            ),
            QuizQuestionBlueprint(
                question="Which of the following represents a Many-to-Many association?",
                options=[
                    "Students and Courses: a student takes many courses, and a course has many students",
                    "A Car and its single VIN serial number",
                    "A Person and their single Social Security Number",
                    "A Computer and its single motherboard"
                ],
                correct_answer="Students and Courses: a student takes many courses, and a course has many students",
                explanation="Students and courses link in a classic many-to-many relationship."
            ),
            QuizQuestionBlueprint(
                question="How is an Association typically implemented inside a Python class?",
                options=[
                    "By storing an instance reference (or collection of references) to the other object as an attribute",
                    "By using the `import` statement inside every method",
                    "By creating a static C-struct",
                    "By copying the class file into another directory"
                ],
                correct_answer="By storing an instance reference (or collection of references) to the other object as an attribute",
                explanation="Associations are held as instance variable references pointing to target objects in heap memory."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 32: Aggregation (Weak "HAS-A", e.g., Dept & Teachers)
    # -------------------------------------------------------------
    DayBlueprint(
        order=32,
        title="Day 32: Aggregation (Weak 'HAS-A')",
        concept="Weak Ownership: Aggregation - whole/part relationship where components can exist independently outside the container",
        analogy="Think of a University Department and its Professors: the Computer Science Department HAS professors (**HAS-A**). However, if the University board decides to dissolve the Computer Science Department, the professors do NOT disappear from the Earth! They simply transfer to the Mathematics department or work elsewhere. The Department is the 'whole' and the Professors are the 'parts', but their lifecycles are weakly bound!",
        theory_sections=[
            {
                "heading": "What is Aggregation?",
                "body": "**Aggregation** is a specialized form of Association that represents a **weak 'HAS-A'** (whole/part) relationship.\n\nIn Aggregation:\n- One object (the container or whole) holds references to other objects (the components or parts).\n- The parts are **created externally** and injected into the container.\n- **Independent Lifecycles**: If the container is destroyed, the aggregated components continue to exist."
            },
            {
                "heading": "UML Notation & Identification",
                "body": "In UML class diagrams, Aggregation is represented by an **unfilled (hollow) white diamond** pointing towards the container.\n\nKey test for Aggregation:\n*\"If I delete the container, do the children still have a reason to exist?\"* If YES -> Aggregation (e.g. A Folder and its Files, a Team and its Players)."
            }
        ],
        code_snippets=[
            {
                "title": "Aggregation Example: Department and Professors",
                "language": "python",
                "code": "class Professor:\n    def __init__(self, name: str, field: str):\n        self.name = name\n        self.field = field\n\nclass Department:\n    def __init__(self, dept_name: str):\n        self.dept_name = dept_name\n        self.professors = []  # Aggregation: container holds external objects\n\n    def add_professor(self, prof: Professor):\n        if prof not in self.professors:\n            self.professors.append(prof)\n\n# Professors created independently outside the department\nprof_alice = Professor('Dr. Alice', 'Machine Learning')\nprof_bob = Professor('Dr. Bob', 'Cybersecurity')\n\ncs_dept = Department('Computer Science')\ncs_dept.add_professor(prof_alice)\ncs_dept.add_professor(prof_bob)\nprint('CS Faculty:', [p.name for p in cs_dept.professors])",
                "explanation": "Professors are instantiated externally and passed into Department."
            },
            {
                "title": "Verifying Component Survival After Container Deletion",
                "language": "python",
                "code": "# Dissolve the department\ndel cs_dept\n\n# Professors survive!\nprint('Surviving professor:', prof_alice.name, '| Field:', prof_alice.field)",
                "explanation": "Proves weak ownership: deleting the department does not destroy the professors."
            },
            {
                "title": "Sports Team and Players Aggregation",
                "language": "python",
                "code": "class Player:\n    def __init__(self, name: str, position: str):\n        self.name = name\n        self.position = position\n\nclass Team:\n    def __init__(self, team_name: str, players: list = None):\n        self.team_name = team_name\n        self.players = list(players) if players else []\n\np1 = Player('Messi', 'Forward')\np2 = Player('De Bruyne', 'Midfielder')\nfc_club = Team('All-Stars', [p1, p2])\nprint(f'{fc_club.team_name} roster count: {len(fc_club.players)}')",
                "explanation": "Players can be traded or exist without the specific team container."
            },
            {
                "title": "Python Script: Demonstrating Reference Injection",
                "language": "python",
                "code": "print('Are department references identical to external objects?')\nprint(prof_alice is p1)  # False\nprint('prof_alice ID in memory:', hex(id(prof_alice)))",
                "explanation": "Shows aggregated objects exist in outer scope before container association."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Music Playlist Aggregation",
            description="Create class `Song(title, artist)` and class `Playlist(name)`. Implement methods `add_song(song: Song)` and `remove_song(title: str)` on Playlist. Demonstrate aggregation: creating songs externally, adding them to a playlist, deleting the playlist, and proving the song objects still exist.",
            starter_code="class Song:\n    pass\nclass Playlist:\n    pass",
            solution_code="class Song:\n    def __init__(self, title: str, artist: str):\n        self.title = title\n        self.artist = artist\n\nclass Playlist:\n    def __init__(self, name: str):\n        self.name = name\n        self.songs = []\n\n    def add_song(self, song: Song):\n        self.songs.append(song)\n\n    def remove_song(self, title: str):\n        self.songs = [s for s in self.songs if s.title != title]",
            expected_output="Song Still Exists: Imagine by John Lennon"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the defining attribute of an Aggregation relationship?",
                options=[
                    "A weak 'HAS-A' relationship where the child components can exist independently outside of the container object",
                    "A relationship where children are automatically deleted when the parent is deleted",
                    "A class that inherits from multiple parents",
                    "An abstract class that has no methods"
                ],
                correct_answer="A weak 'HAS-A' relationship where the child components can exist independently outside of the container object",
                explanation="Aggregation represents a weak whole-part relationship with independent component lifespans."
            ),
            QuizQuestionBlueprint(
                question="In UML class diagrams, which symbol represents Aggregation?",
                options=[
                    "A hollow (unfilled) white diamond",
                    "A solid black filled diamond",
                    "A dotted arrow with a triangle",
                    "A double dashed line"
                ],
                correct_answer="A hollow (unfilled) white diamond",
                explanation="A hollow diamond represents weak Aggregation, while a solid black diamond represents strong Composition."
            ),
            QuizQuestionBlueprint(
                question="Which of the following is a classic real-world example of Aggregation?",
                options=[
                    "A Football Team and its Players (if the team disbands, players can join other teams)",
                    "A Human Body and its Brain (the brain cannot live on a park bench alone)",
                    "A House and its physical rooms",
                    "A Book and its bound pages"
                ],
                correct_answer="A Football Team and its Players (if the team disbands, players can join other teams)",
                explanation="Players exist independently of any particular team, making Team-Player an aggregation."
            ),
            QuizQuestionBlueprint(
                question="How are aggregated component objects typically provided to the container class in code?",
                options=[
                    "They are instantiated externally and passed into the container via constructor arguments or setter methods (Dependency Injection)",
                    "The container instantiates them privately inside its own constructor",
                    "By using global variables",
                    "By reading from a hard drive sector directly"
                ],
                correct_answer="They are instantiated externally and passed into the container via constructor arguments or setter methods (Dependency Injection)",
                explanation="Passing externally created objects into the container decouples their lifecycle from the container."
            ),
            QuizQuestionBlueprint(
                question="What happens to the component parts in an Aggregation when the container object is destroyed by garbage collection?",
                options=[
                    "The components remain alive in memory as long as external references still point to them",
                    "The components are immediately wiped from memory",
                    "The components trigger a memory corruption fault",
                    "The components are converted into static methods"
                ],
                correct_answer="The components remain alive in memory as long as external references still point to them",
                explanation="Because external scopes hold references to the components, deleting the container does not deallocate them."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 33: Composition (Strong "PART-OF", e.g., House & Rooms)
    # -------------------------------------------------------------
    DayBlueprint(
        order=33,
        title="Day 33: Composition (Strong 'PART-OF')",
        concept="Strong Ownership: Composition - whole/part relationship where components cannot exist without the container; lifecycle binding",
        analogy="Think of a House and its Rooms (Living Room, Kitchen, Bedroom): the rooms are **PART-OF** the house. You cannot sell the kitchen to a neighbor across the street while leaving the rest of the house behind! If a wrecking ball demolishes the house, the living room and kitchen are demolished at that exact same second. The rooms are born when the house is built and die when the house is destroyed (**Composition**).",
        theory_sections=[
            {
                "heading": "What is Composition?",
                "body": "**Composition** is the strongest form of object relationship, representing a **strong 'PART-OF'** bond. The composite object (the Whole) completely owns the lifecycle of its components (the Parts).\n\nIn Composition:\n- The components are **instantiated internally** inside the composite object's constructor.\n- **Co-dependent Lifecycles**: If the composite whole is destroyed, all its internal components are destroyed along with it.\n- Outside code does not manipulate the components directly; all interactions pass through the composite container."
            },
            {
                "heading": "Favor Composition Over Inheritance",
                "body": "A famous architectural maxim in software engineering states: *\"Favor object composition over class inheritance.\"*\n\nInheritance produces rigid, fragile hierarchies (tight compile-time coupling). Composition produces flexible, loosely coupled systems where behaviors can be swapped dynamically at runtime simply by composing different sub-components."
            }
        ],
        code_snippets=[
            {
                "title": "Composition Example: House Creating and Owning its Rooms",
                "language": "python",
                "code": "class Room:\n    def __init__(self, name: str, square_meters: float):\n        self.name = name\n        self.square_meters = square_meters\n\nclass House:\n    def __init__(self):\n        # Strong composition: House constructs and owns its rooms internally!\n        self.rooms = [\n            Room('Living Room', 30.0),\n            Room('Master Bedroom', 20.0),\n            Room('Kitchen', 15.0)\n        ]\n\n    def get_total_area(self) -> float:\n        return sum(r.square_meters for r in self.rooms)\n\nh = House()\nprint('Total House Floor Area:', h.get_total_area(), 'm²')",
                "explanation": "House creates and encapsulates its own Room instances directly inside __init__."
            },
            {
                "title": "Co-Dependent Lifecycle (Cascading Destruction)",
                "language": "python",
                "code": "class Engine:\n    def __del__(self): print('Engine scrapped.')\n\nclass Automobile:\n    def __init__(self):\n        self._engine = Engine()  # Automobile owns Engine\n    def __del__(self):\n        print('Automobile crushed.')\n\nauto = Automobile()\n# Destroying Automobile cascades down to destroy its composed Engine\ndel auto",
                "explanation": "Demonstrates cascading lifecycle: deleting the container destroys its composed parts."
            },
            {
                "title": "Favoring Composition over Inheritance: Robot with Swappable Tools",
                "language": "python",
                "code": "class Laser:\n    def activate(self): return 'Firing high-energy cutting laser!'\n\nclass Gripper:\n    def activate(self): return 'Gripping heavy industrial pallet.'\n\n# Robot COMPOSES tool behavior rather than inheriting from ToolBase\nclass IndustrialRobot:\n    def __init__(self, tool):\n        self.tool = tool\n    def work(self):\n        return self.tool.activate()\n\nr1 = IndustrialRobot(Laser())\nr2 = IndustrialRobot(Gripper())\nprint('Robot 1:', r1.work())\nprint('Robot 2:', r2.work())",
                "explanation": "Composition allows behaviors to be assembled and swapped dynamically at runtime."
            },
            {
                "title": "UML Notation: Solid Black Diamond",
                "language": "text",
                "code": "// UML Class Diagram:\n// [ House ] *---------1 [ Room ]\n// (Solid black diamond on the House side indicates strong Composition)",
                "explanation": "Contrasts the solid black diamond of Composition with the hollow diamond of Aggregation."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Computer Composing CPU and Memory",
            description="Create a `CPU(cores, clock_ghz)` class and a `RAM(capacity_gb)` class. Create a `Computer` class that composes a `CPU` and `RAM` internally inside its constructor `__init__(cores, clock_ghz, ram_gb)`. Implement `specs()` returning `f'Computer: {cores} cores @ {clock_ghz}GHz with {ram_gb}GB RAM'`.",
            starter_code="class CPU:\n    pass\nclass RAM:\n    pass\nclass Computer:\n    pass",
            solution_code="class CPU:\n    def __init__(self, cores: int, clock_ghz: float):\n        self.cores = cores\n        self.clock_ghz = clock_ghz\n\nclass RAM:\n    def __init__(self, capacity_gb: int):\n        self.capacity_gb = capacity_gb\n\nclass Computer:\n    def __init__(self, cores: int, clock_ghz: float, ram_gb: int):\n        # Strong composition: constructed internally\n        self.cpu = CPU(cores, clock_ghz)\n        self.ram = RAM(ram_gb)\n\n    def specs(self) -> str:\n        return f'Computer: {self.cpu.cores} cores @ {self.cpu.clock_ghz}GHz with {self.ram.capacity_gb}GB RAM'",
            expected_output="Computer: 8 cores @ 3.5GHz with 32GB RAM"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the critical distinction between Aggregation and Composition?",
                options=[
                    "In Composition, the components cannot exist without the container (co-dependent lifecycles); in Aggregation, components exist independently (weak ownership)",
                    "Composition is for strings; Aggregation is for numbers",
                    "Composition only works in Python 2",
                    "Aggregation requires 64-bit processors"
                ],
                correct_answer="In Composition, the components cannot exist without the container (co-dependent lifecycles); in Aggregation, components exist independently (weak ownership)",
                explanation="Composition implies strict ownership and shared lifecycle; destroying the whole destroys the parts."
            ),
            QuizQuestionBlueprint(
                question="In UML notation, what visual symbol represents strong Composition?",
                options=[
                    "A solid black filled diamond",
                    "A hollow white diamond",
                    "A dotted zigzag line",
                    "A circle with an X inside"
                ],
                correct_answer="A solid black filled diamond",
                explanation="A solid black diamond denotes Composition; a hollow diamond denotes Aggregation."
            ),
            QuizQuestionBlueprint(
                question="Why do modern software architects recommend 'Favoring composition over inheritance'?",
                options=[
                    "Composition provides loose coupling and runtime flexibility without creating rigid, brittle class hierarchies",
                    "Inheritance was deprecated by the Python Software Foundation",
                    "Composition eliminates the need to compile code",
                    "Inherited classes use 10 times more electricity"
                ],
                correct_answer="Composition provides loose coupling and runtime flexibility without creating rigid, brittle class hierarchies",
                explanation="Composition allows swapping behaviors dynamically and avoids the Fragile Base Class problem common to deep inheritance."
            ),
            QuizQuestionBlueprint(
                question="Which of the following represents a classic real-world example of Composition?",
                options=[
                    "A Human Body and its Heart (the heart cannot exist as an autonomous living entity outside a body)",
                    "A Library and its Visitors",
                    "A Parking Lot and the Cars parked in it",
                    "A Doctor and their Patients"
                ],
                correct_answer="A Human Body and its Heart (the heart cannot exist as an autonomous living entity outside a body)",
                explanation="A heart is an organic component of a body; destroying the body destroys the heart."
            ),
            QuizQuestionBlueprint(
                question="Where are composed component instances typically created in code to enforce strong composition?",
                options=[
                    "Directly inside the constructor (`__init__`) of the composite container class",
                    "In a global configuration script on another server",
                    "In an external factory function",
                    "In the terminal command line"
                ],
                correct_answer="Directly inside the constructor (`__init__`) of the composite container class",
                explanation="Constructing parts inside the composite's constructor ties their lifecycle directly to the container."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 34: Dependency (Object dependence)
    # -------------------------------------------------------------
    DayBlueprint(
        order=34,
        title="Day 34: Dependency (Object Dependence)",
        concept="Transitory Relationships: Dependency ('USES-A') - temporary method parameter coupling, method-scoped lifecycles, and Dependency Inversion",
        analogy="Think of using a hammer to hang a picture frame: you pick up the hammer, tap the nail into the wall, and immediately put the hammer back in your toolbox. You do NOT weld the hammer to your wrist for the rest of your life! You simply used the hammer for a few seconds (**USES-A**). In programming, a Dependency is a fleeting, temporary relationship where a method accepts an object as a parameter, uses it, and lets it go.",
        theory_sections=[
            {
                "heading": "What is a Dependency ('USES-A')?",
                "body": "**Dependency** is the weakest of all object relationships. Class `A` depends on Class `B` if a change in `B`'s definition could force a change in `A`.\n\nTypically, a dependency occurs when Class `A` **USES** Class `B` temporarily:\n- Class `B` is passed as a **method parameter**.\n- Class `B` is instantiated locally as a temporary variable inside a method.\n- Class `A` does **not** store Class `B` as an ongoing member variable."
            },
            {
                "heading": "Tight Coupling vs Loose Coupling",
                "body": "- **Tight Coupling**: Instantiating concrete dependencies directly inside methods (`db = MySQLDatabase()`). This makes testing impossible and prevents swapping implementations.\n- **Loose Coupling (Dependency Injection)**: Passing dependencies in from the outside as interfaces or parameters (`def sync(self, db: DatabaseInterface)`). This enables trivial mock testing and architectural flexibility."
            }
        ],
        code_snippets=[
            {
                "title": "Demonstration of Method Dependency (USES-A)",
                "language": "python",
                "code": "class Printer:\n    def print_document(self, text: str):\n        return f'Printing: {text}'\n\nclass Document:\n    def __init__(self, content: str):\n        self.content = content\n\n    # Temporary dependency: Document USES a Printer in this method only!\n    def send_to_print(self, printer: Printer) -> str:\n        # printer is not stored in self; it is a transitory parameter\n        return printer.print_document(self.content)\n\ndoc = Document('Quarterly Financial Summary')\np = Printer()\nprint(doc.send_to_print(p))",
                "explanation": "Document depends on Printer temporarily during the send_to_print method execution."
            },
            {
                "title": "Tight Coupling (Anti-Pattern) vs Dependency Injection",
                "language": "python",
                "code": "# Tightly Coupled (Bad): Hardcoded dependency\nclass ReportGeneratorBad:\n    def generate(self):\n        # Hardcoded concrete dependency; cannot be mocked or swapped!\n        import sqlite3\n        conn = sqlite3.connect(':memory:')\n\n# Loosely Coupled (Good): Dependency injected via parameter\nclass ReportGeneratorGood:\n    def generate(self, db_connection):\n        # Works with SQLite, PostgreSQL, or a Mock test database seamlessly!\n        return db_connection.execute('SELECT 1')",
                "explanation": "Injecting dependencies prevents hardcoded coupling to specific concrete implementations."
            },
            {
                "title": "Mocking Dependencies for Unit Testing",
                "language": "python",
                "code": "class MockEmailService:\n    def __init__(self):\n        self.sent_messages = []\n    def send_email(self, recipient: str, body: str):\n        self.sent_messages.append({'to': recipient, 'body': body})\n        return True\n\nclass UserNotifier:\n    # Depends on email_service temporarily\n    def alert_user(self, email_service, user_email: str):\n        return email_service.send_email(user_email, 'Security alert')\n\n# Test execution with mock dependency\nmock = MockEmailService()\nUserNotifier().alert_user(mock, 'alice@test.com')\nprint('Test verified message sent:', mock.sent_messages)",
                "explanation": "Loose dependencies allow trivial substitution with test doubles."
            },
            {
                "title": "UML Notation: Dashed Arrow with Open Arrowhead",
                "language": "text",
                "code": "// UML Class Diagram:\n// [ Document ] - - - > [ Printer ]\n// (Dashed line with open arrowhead indicates dependency / USES relationship)",
                "explanation": "UML depicts dependencies with a dashed directional arrow."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Payment Processor Dependency Injection",
            description="Create an `Order` class with attributes `order_id` and `amount`. Implement a method `pay(self, payment_service)` where `payment_service` has a method `process(amount)`. Return the result of calling `payment_service.process(self.amount)`.",
            starter_code="class Order:\n    pass\nclass CreditCardService:\n    pass",
            solution_code="class Order:\n    def __init__(self, order_id: str, amount: float):\n        self.order_id = order_id\n        self.amount = float(amount)\n\n    def pay(self, payment_service) -> str:\n        return payment_service.process(self.amount)\n\nclass CreditCardService:\n    def process(self, amount: float) -> str:\n        return f'Charged ${amount:.2f} via Credit Card'",
            expected_output="Charged $120.50 via Credit Card"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What characterizes a Dependency relationship in Object-Oriented design?",
                options=[
                    "A transitory 'USES-A' relationship where one class temporarily utilizes another class as a method parameter or local variable without storing it long-term",
                    "A permanent parent-child inheritance link",
                    "A class containing 50 static variables",
                    "A database table with foreign key constraints"
                ],
                correct_answer="A transitory 'USES-A' relationship where one class temporarily utilizes another class as a method parameter or local variable without storing it long-term",
                explanation="Dependency is a short-lived relationship where an object relies on another object during method execution."
            ),
            QuizQuestionBlueprint(
                question="In UML class diagrams, how is a Dependency represented?",
                options=[
                    "A dashed line with an open arrow pointing to the dependency (`- - - >`)",
                    "A solid line with a black diamond",
                    "A double thick red line",
                    "A circle with a lightning bolt"
                ],
                correct_answer="A dashed line with an open arrow pointing to the dependency (`- - - >`)",
                explanation="UML standardizes dependency relationships as dashed arrows pointing toward the depended-upon element."
            ),
            QuizQuestionBlueprint(
                question="Why is hardcoding concrete class instantiations inside methods (tight coupling) considered an anti-pattern?",
                options=[
                    "It prevents unit testing with mock objects and makes it impossible to swap implementations without modifying existing code",
                    "It causes the computer screen to flicker",
                    "Because Python forbids instantiating classes inside functions",
                    "It converts numbers to strings"
                ],
                correct_answer="It prevents unit testing with mock objects and makes it impossible to swap implementations without modifying existing code",
                explanation="Hardcoded dependencies make code rigid, fragile, and difficult to test in isolation."
            ),
            QuizQuestionBlueprint(
                question="What software technique solves tight coupling by passing required helper objects into a class from the outside?",
                options=[
                    "Dependency Injection",
                    "Binary Compilation",
                    "Recursive Looping",
                    "Global State Allocation"
                ],
                correct_answer="Dependency Injection",
                explanation="Dependency Injection supplies collaborator objects from the outside, achieving loose coupling."
            ),
            QuizQuestionBlueprint(
                question="Which relationship ranking correctly orders object coupling strength from WEAKEST to STRONGEST?",
                options=[
                    "Dependency -> Association -> Aggregation -> Composition -> Inheritance",
                    "Inheritance -> Composition -> Aggregation -> Association -> Dependency",
                    "Aggregation -> Dependency -> Inheritance -> Composition",
                    "Association -> Dependency -> Inheritance"
                ],
                correct_answer="Dependency -> Association -> Aggregation -> Composition -> Inheritance",
                explanation="Dependency is the weakest (transitory), followed by Association (peer link), Aggregation (weak has-a), Composition (strong part-of), and Inheritance (tightest IS-A bond)."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 35 (Project): Complete Library Management (Books, Authors, Shelves)
    # -------------------------------------------------------------
    DayBlueprint(
        order=35,
        title="Day 35 (Project): Complete Library Management",
        concept="Hands-on Project Day: Integrating Association (Authors & Books), Composition (Shelves inside Library), and Aggregation (Books on Shelves) into an enterprise Library System",
        analogy="Think of today's project like managing the famous Library of Alexandria: individual `Authors` write `Books` (**Association**). A `Library` physically constructs and owns its architectural `Shelves` (**Composition: if the library burns, the shelves burn**). `Books` are placed on those shelves, loaned out to readers, and returned (**Aggregation: books exist independently of whether they are on a shelf or in a patron's backpack**). All four OOP relationships working in harmony!",
        is_project_day=True,
        project_name="Complete Library Management",
        theory_sections=[
            {
                "heading": "Architectural Synthesis of Object Relationships",
                "body": "Today's project combines all four object relationship models into a comprehensive domain system:\n1. **Association**: `Book` has an `Author` reference. Both can exist independently.\n2. **Composition**: A `Library` owns and creates its `Bookshelf` units internally. If the library is deleted, its shelves are destroyed.\n3. **Aggregation**: `Bookshelf` holds a collection of `Book` objects. If a shelf is removed, the books are simply moved to another shelf or checked out.\n4. **Dependency**: A `LoanService` takes a `Book` and a `Member` as method parameters to issue a checkout receipt."
            },
            {
                "heading": "System Operations & Invariants",
                "body": "- Search books by title, author name, or ISBN.\n- Check book availability status (`is_checked_out`).\n- Enforce bookshelf capacity limits (e.g. max 50 books per shelf)."
            }
        ],
        code_snippets=[
            {
                "title": "Author and Book Classes (Association)",
                "language": "python",
                "code": "class Author:\n    def __init__(self, name: str, nationality: str):\n        self.name = name\n        self.nationality = nationality\n\nclass Book:\n    def __init__(self, isbn: str, title: str, author: Author):\n        self.isbn = isbn\n        self.title = title\n        self.author = author  # Association: holds reference to Author\n        self.is_checked_out = False\n\n    def __repr__(self):\n        return f'Book(\"{self.title}\" by {self.author.name})'",
                "explanation": "Book associates with Author without lifecycle ownership."
            },
            {
                "title": "Bookshelf and Library Classes (Composition & Aggregation)",
                "language": "python",
                "code": "class Bookshelf:\n    def __init__(self, shelf_id: str, capacity: int = 10):\n        self.shelf_id = shelf_id\n        self.capacity = capacity\n        self.books = []  # Aggregation: books exist independently\n\n    def add_book(self, book: Book) -> bool:\n        if len(self.books) < self.capacity and book not in self.books:\n            self.books.append(book)\n            return True\n        return False\n\nclass Library:\n    def __init__(self, name: str):\n        self.name = name\n        # Composition: Library constructs and manages its own internal bookshelves\n        self.shelves = [\n            Bookshelf('SHELF-A', capacity=5),\n            Bookshelf('SHELF-B', capacity=5)\n        ]\n\n    def find_book(self, title: str):\n        for shelf in self.shelves:\n            for book in shelf.books:\n                if book.title.lower() == title.lower():\n                    return book\n        return None",
                "explanation": "Library composes Bookshelves, which in turn aggregate Books."
            },
            {
                "title": "Loan Service Execution (Method Dependency)",
                "language": "python",
                "code": "class Member:\n    def __init__(self, member_id: str, name: str):\n        self.member_id = member_id\n        self.name = name\n\nclass LoanService:\n    # Dependency: LoanService USES Book and Member temporarily\n    def checkout(self, book: Book, member: Member) -> str:\n        if book.is_checked_out:\n            return f'Sorry, {book.title} is already checked out.'\n        book.is_checked_out = True\n        return f'Success: \"{book.title}\" loaned to {member.name} (ID: {member.member_id})'",
                "explanation": "LoanService demonstrates method dependency parameters."
            },
            {
                "title": "Full System Integration Test",
                "language": "python",
                "code": "# 1. Create Authors and Books\norwell = Author('George Orwell', 'British')\nb1 = Book('ISBN-01', '1984', orwell)\nb2 = Book('ISBN-02', 'Animal Farm', orwell)\n\n# 2. Add to Library\nlib = Library('City Central Library')\nlib.shelves[0].add_book(b1)\nlib.shelves[0].add_book(b2)\n\n# 3. Process Loan\nloan_desk = LoanService()\nuser = Member('MEM-99', 'Alice')\nprint(loan_desk.checkout(b1, user))\nprint(loan_desk.checkout(b1, user))  # Attempt double checkout",
                "explanation": "Simulates complete end-to-end library workflow."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Library Inventory Report",
            description="Add a method `inventory_report(self) -> dict` to the `Library` class that returns a dictionary summary: `{'total_shelves': int, 'total_books': int, 'available_books': int, 'checked_out_books': int}`.",
            starter_code="class Library:\n    # Implement inventory_report()\n    pass",
            solution_code="class Library:\n    def __init__(self, name: str):\n        self.name = name\n        self.shelves = []\n\n    def inventory_report(self) -> dict:\n        all_books = [b for shelf in self.shelves for b in shelf.books]\n        checked_out = sum(1 for b in all_books if b.is_checked_out)\n        return {\n            'total_shelves': len(self.shelves),\n            'total_books': len(all_books),\n            'available_books': len(all_books) - checked_out,\n            'checked_out_books': checked_out\n        }",
            expected_output="{'total_shelves': 2, 'total_books': 2, 'available_books': 1, 'checked_out_books': 1}"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="In the Library system, what relationship exists between `Library` and its `Bookshelf` units?",
                options=[
                    "Composition: The library creates and owns the physical shelves internally",
                    "Inheritance: Bookshelf is a subclass of Library",
                    "Polymorphic Operator Overloading",
                    "Procedural Function Macro"
                ],
                correct_answer="Composition: The library creates and owns the physical shelves internally",
                explanation="The shelves are constructed and lifecycle-managed directly by the library container (Composition)."
            ),
            QuizQuestionBlueprint(
                question="In the Library system, what relationship exists between `Bookshelf` and `Book`?",
                options=[
                    "Aggregation: A shelf holds books, but if the shelf is broken, the books survive independently",
                    "Inheritance: Book is a child of Bookshelf",
                    "Tight coupling",
                    "Destructor binding"
                ],
                correct_answer="Aggregation: A shelf holds books, but if the shelf is broken, the books survive independently",
                explanation="Books are external entities aggregated onto shelves; deleting a shelf leaves the books intact."
            ),
            QuizQuestionBlueprint(
                question="What relationship exists between `LoanService` and `Book`?",
                options=[
                    "Dependency: LoanService temporarily receives a Book as a method parameter to process a checkout transaction",
                    "Inheritance: LoanService IS-A Book",
                    "Composition: LoanService creates books in memory",
                    "Aggregation: LoanService stores books permanently in a list"
                ],
                correct_answer="Dependency: LoanService temporarily receives a Book as a method parameter to process a checkout transaction",
                explanation="LoanService does not store books as member state; it merely uses them temporarily during the checkout method."
            ),
            QuizQuestionBlueprint(
                question="Why is modeling `Author` as a separate class from `Book` superior to storing author as a simple string?",
                options=[
                    "It allows storing author metadata (nationality, biography, bibliography) and linking multiple books to the same author instance",
                    "Because Python forbids strings in class attributes",
                    "It makes code compile 10x faster",
                    "Because strings cannot be printed to console"
                ],
                correct_answer="It allows storing author metadata (nationality, biography, bibliography) and linking multiple books to the same author instance",
                explanation="Domain modeling elevates authors into first-class entities with their own attributes and relationships."
            ),
            QuizQuestionBlueprint(
                question="If the `Library` instance is deleted, which objects continue to exist in memory if referenced by the main program?",
                options=[
                    "The `Author`, `Book`, and `Member` objects (their lifecycles are independent of the library container)",
                    "Only the Library's name string",
                    "No objects survive; Python deletes the entire program",
                    "Only the Bookshelf instances"
                ],
                correct_answer="The `Author`, `Book`, and `Member` objects (their lifecycles are independent of the library container)",
                explanation="Because of aggregation and association, independent domain entities survive the container's destruction."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 36: Static Members (Variables & Methods)
    # -------------------------------------------------------------
    DayBlueprint(
        order=36,
        title="Day 36: Static Members (Variables & Methods)",
        concept="Class-Level State and Logic: Class variables vs instance variables, `@classmethod` for factory constructors, and `@staticmethod` for utility functions",
        analogy="Think of a large family with 5 children. Each child has their own individual savings piggy bank (**Instance Variable**): Timmy has $5, Sarah has $20. But there is also one single communal refrigerator in the kitchen (**Class / Static Variable**): every child shares the exact same refrigerator. If Timmy eats the last chocolate pudding from the fridge, the pudding is gone for Sarah and all other children too!",
        theory_sections=[
            {
                "heading": "Class Variables vs Instance Variables",
                "body": "- **Instance Variables** (`self.x`): Bound to a specific instance. Each object maintains its own independent copy.\n- **Class (Static) Variables**: Defined directly inside the class body outside any method. Shared by **every instance** of the class. Modifying a class variable via `ClassName.var = value` immediately updates it across all existing and future instances."
            },
            {
                "heading": "`@classmethod` vs `@staticmethod` in Python",
                "body": "1. **`@classmethod`**: Receives the class itself as its first argument (`cls`). Can inspect or modify class-level state and is frequently used for **Alternative Factory Constructors**.\n2. **`@staticmethod`**: Receives neither `self` nor `cls`. Behaves like an ordinary utility function that has a logical home inside the class namespace. Cannot modify instance or class state."
            }
        ],
        code_snippets=[
            {
                "title": "Class Variable Tracking Instance Count across Objects",
                "language": "python",
                "code": "class User:\n    # Class-level static variable\n    total_users_count = 0\n\n    def __init__(self, username: str):\n        self.username = username\n        # Increment shared class counter\n        User.total_users_count += 1\n\nu1 = User('alice')\nu2 = User('bob')\nu3 = User('carol')\nprint('Total active users created:', User.total_users_count)  # 3\nprint('Accessible via instance too:', u1.total_users_count)    # 3",
                "explanation": "total_users_count is shared across all User instances."
            },
            {
                "title": "@classmethod as Alternative Factory Constructor",
                "language": "python",
                "code": "class Date:\n    def __init__(self, year: int, month: int, day: int):\n        self.year, self.month, self.day = year, month, day\n\n    @classmethod\n    def from_string(cls, date_str: str) -> 'Date':\n        # Alternative factory constructor: parses \"YYYY-MM-DD\"\n        year, month, day = map(int, date_str.split('-'))\n        return cls(year, month, day)  # Instantiate via cls\n\nd1 = Date(2026, 9, 30)\nd2 = Date.from_string('2026-12-25')\nprint('Standard date:', d1.year, d1.month)\nprint('Factory date:', d2.year, d2.month)",
                "explanation": "@classmethod receives cls, allowing clean factory instantiation."
            },
            {
                "title": "@staticmethod as Pure Utility Function",
                "language": "python",
                "code": "class TemperatureConverter:\n    @staticmethod\n    def c_to_f(celsius: float) -> float:\n        return (celsius * 9 / 5) + 32\n\n    @staticmethod\n    def f_to_c(fahrenheit: float) -> float:\n        return (fahrenheit - 32) * 5 / 9\n\nprint('100 C in F:', TemperatureConverter.c_to_f(100))\nprint('32 F in C:', TemperatureConverter.f_to_c(32))",
                "explanation": "@staticmethod operates purely on inputs without touching class or instance state."
            },
            {
                "title": "Java / C++ Static Keyword Comparison",
                "language": "text",
                "code": "// In Java / C++:\n// public class User {\n//     public static int userCount = 0;\n//     public static void resetCount() { userCount = 0; }\n// }",
                "explanation": "Contrasts Python's decorators with Java's static keyword."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Database Connection Pool with Static Counter",
            description="Create a `Connection` class with a class variable `active_connections: int` (default 0) and max limit `MAX_CONNECTIONS = 3`. The `__init__` should increment `active_connections` only if below `MAX_CONNECTIONS`, otherwise raise `RuntimeError('Connection limit reached')`. Add a method `close()` that decrements `active_connections`.",
            starter_code="class Connection:\n    # Implement Connection pool limits\n    pass",
            solution_code="class Connection:\n    active_connections = 0\n    MAX_CONNECTIONS = 3\n\n    def __init__(self):\n        if Connection.active_connections >= Connection.MAX_CONNECTIONS:\n            raise RuntimeError('Connection limit reached')\n        Connection.active_connections += 1\n        self._is_closed = False\n\n    def close(self):\n        if not self._is_closed:\n            Connection.active_connections = max(0, Connection.active_connections - 1)\n            self._is_closed = True",
            expected_output="Active: 3\nRuntimeError caught successfully"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the difference between a Class Variable and an Instance Variable in Python?",
                options=[
                    "A Class Variable is shared across all instances of the class; an Instance Variable is unique to a single object instance",
                    "Class variables can only store numbers; instance variables can only store strings",
                    "Class variables are deleted after 5 minutes",
                    "There is no difference"
                ],
                correct_answer="A Class Variable is shared across all instances of the class; an Instance Variable is unique to a single object instance",
                explanation="Class variables are attached to the class namespace and shared by all instances; instance variables reside in each object's `__dict__`."
            ),
            QuizQuestionBlueprint(
                question="What is the first parameter automatically passed to a method decorated with `@classmethod`?",
                options=[
                    "cls (the class object itself)",
                    "self (the instance)",
                    "this",
                    "super"
                ],
                correct_answer="cls (the class object itself)",
                explanation="Class methods receive the class (`cls`) as their first parameter, enabling access to class attributes and factory constructors."
            ),
            QuizQuestionBlueprint(
                question="What characterizes a method decorated with `@staticmethod`?",
                options=[
                    "It takes neither `self` nor `cls` as an automatic first argument and behaves like an isolated utility function grouped inside the class namespace",
                    "It cannot return any value",
                    "It causes the class to become immutable",
                    "It can only be called from inside a while loop"
                ],
                correct_answer="It takes neither `self` nor `cls` as an automatic first argument and behaves like an isolated utility function grouped inside the class namespace",
                explanation="Static methods do not receive implicit instance or class arguments, serving as namespaced utility functions."
            ),
            QuizQuestionBlueprint(
                question="What common design pattern heavily utilizes `@classmethod` in Python?",
                options=[
                    "Alternative Factory Constructors (e.g. `Date.from_string()`, `User.from_json()`)",
                    "The Anti-Pattern",
                    "Spaghetti Code",
                    "The Circular Reference Loop"
                ],
                correct_answer="Alternative Factory Constructors (e.g. `Date.from_string()`, `User.from_json()`)",
                explanation="Classmethods are standard in Python for building alternative constructors that instantiate objects from different formats."
            ),
            QuizQuestionBlueprint(
                question="What happens if you execute `instance.class_var = 100` on an instance when `class_var` was defined on the class?",
                options=[
                    "Python creates a new instance variable on `instance` that shadows the class variable, leaving the class variable unchanged for other instances",
                    "The class variable is updated globally for all instances",
                    "A syntax error is thrown",
                    "The instance is deleted"
                ],
                correct_answer="Python creates a new instance variable on `instance` that shadows the class variable, leaving the class variable unchanged for other instances",
                explanation="Assigning via an instance creates a local instance attribute that shadows the class attribute without mutating the class-level value."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 37: Final / Const Keywords (Preventing overrides/changes)
    # -------------------------------------------------------------
    DayBlueprint(
        order=37,
        title="Day 37: Final / Const Keywords (Preventing Overrides)",
        concept="Immutability and Inheritance Freezing: Preventing method overrides and subclassing using `typing.final`, C++ `const`/`final`, and Java `final`",
        analogy="Think of a legal document like the United States Constitution's Bill of Rights or a certified Last Will and Testament. You are allowed to add supplemental notes or comments (**Derived Classes**), but the core foundational clauses are stamped **FINAL**: no judge or lawyer is allowed to alter, override, or edit those words. The `final` keyword freezes classes and methods against tampering or accidental modification!",
        theory_sections=[
            {
                "heading": "The Purpose of `final` and `const`",
                "body": "In software architecture, you sometimes need to guarantee that a security-critical algorithm or foundational class cannot be overridden or tampered with by downstream developers:\n- **Final Class**: Forbids any other class from inheriting from it.\n- **Final Method**: Allows a class to be inherited, but forbids derived subclasses from overriding that specific method.\n- **Const / Final Variables**: Constants that cannot be reassigned after initialization."
            },
            {
                "heading": "Implementation Across Languages",
                "body": "- **Java**: Uses the `final` keyword for classes, methods, and variables (e.g. `public final class String`).\n- **C++**: Uses `final` on classes/virtual methods and `const` for immutability.\n- **Python (PEP 591 / Python 3.8+)**: Introduced `@typing.final` decorator and `Final` type annotation. Static type checkers (Mypy, Pyright) enforce that decorated classes cannot be subclassed and decorated methods cannot be overridden."
            }
        ],
        code_snippets=[
            {
                "title": "Using @typing.final to Prevent Subclassing in Python",
                "language": "python",
                "code": "from typing import final\n\n@final\nclass SecurityHasher:\n    def hash_password(self, pw: str) -> str:\n        import hashlib\n        return hashlib.sha256(pw.encode()).hexdigest()\n\n# Static type checkers (Mypy) flag this inheritance as an error!\n# class RogueHasher(SecurityHasher):  # ERROR: Base class 'SecurityHasher' is marked final\n#     pass\n\nh = SecurityHasher()\nprint('Hashed output:', h.hash_password('secret123')[:16], '...')",
                "explanation": "@final decorator instructs static checkers to forbid inheritance."
            },
            {
                "title": "Using @typing.final on Specific Methods",
                "language": "python",
                "code": "class BasePaymentProcessor:\n    # Child classes can inherit, but CANNOT override this security check\n    @final\n    def verify_fraud_check(self, ip_address: str) -> bool:\n        return not ip_address.startswith('198.51.')\n\n    def execute_charge(self, amount: float):\n        pass  # Overridable by children\n\nclass CustomProcessor(BasePaymentProcessor):\n    # Static checker error if verify_fraud_check is defined here!\n    def execute_charge(self, amount: float):\n        return f'Charged ${amount}'",
                "explanation": "Individual critical methods can be locked while leaving others overridable."
            },
            {
                "title": "Final Constants with typing.Final",
                "language": "python",
                "code": "from typing import Final\n\nMAX_LOGIN_ATTEMPTS: Final[int] = 5\n# MAX_LOGIN_ATTEMPTS = 10  # Mypy Error: Cannot assign to final name 'MAX_LOGIN_ATTEMPTS'\nprint('Enforced constant:', MAX_LOGIN_ATTEMPTS)",
                "explanation": "Final type annotation marks identifiers as un-reassignable constants."
            },
            {
                "title": "Java and C++ Final Syntax Comparison",
                "language": "text",
                "code": "// Java:\n// public final class ImmutableString { ... } // Cannot be extended\n// public final void lockAccount() { ... }     // Cannot be overridden\n//\n// C++:\n// class Base final { ... };                  // Cannot be derived from\n// virtual void process() final;               // Cannot be overridden",
                "explanation": "Contrasts Python's type annotations with compiler-enforced keywords in Java and C++."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Enforcing Immutability with Final",
            description="Create a class `SecurityToken` marked with `@final`. It should initialize with `token_id: str` and `expires_in: int`. Implement a read-only property `token` returning `token_id`. Attempting to subclass `SecurityToken` should be documented with a check.",
            starter_code="from typing import final\n# Implement final SecurityToken\npass",
            solution_code="from typing import final\n\n@final\nclass SecurityToken:\n    def __init__(self, token_id: str, expires_in: int):\n        self._token_id = token_id\n        self.expires_in = expires_in\n\n    @property\n    def token(self) -> str:\n        return self._token_id",
            expected_output="Token: tok_998811 (expires 3600s)"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the effect of marking a class as `final`?",
                options=[
                    "No other class is permitted to inherit from or extend it",
                    "The class is automatically deleted at the end of the script",
                    "The class cannot have any methods",
                    "The class can only be instantiated on Sundays"
                ],
                correct_answer="No other class is permitted to inherit from or extend it",
                explanation="A final class cannot be extended; it terminates that branch of the inheritance hierarchy."
            ),
            QuizQuestionBlueprint(
                question="What is the effect of marking a specific method as `final` in an inheritable base class?",
                options=[
                    "Subclasses can inherit the method, but are strictly forbidden from overriding it",
                    "The method cannot be called by external code",
                    "The method takes 0 seconds to run",
                    "The method must be written in assembly language"
                ],
                correct_answer="Subclasses can inherit the method, but are strictly forbidden from overriding it",
                explanation="A final method locks its implementation so derived subclasses cannot alter its behavior."
            ),
            QuizQuestionBlueprint(
                question="Which module in the Python standard library provides the `@final` decorator and `Final` type annotation?",
                options=[
                    "typing",
                    "abc",
                    "functools",
                    "sys"
                ],
                correct_answer="typing",
                explanation="PEP 591 introduced `@final` and `Final` inside Python's `typing` module."
            ),
            QuizQuestionBlueprint(
                question="In Java, what built-in class is famously declared as `public final class` to prevent tampering with security and immutability?",
                options=[
                    "java.lang.String",
                    "java.util.ArrayList",
                    "java.io.File",
                    "java.lang.Object"
                ],
                correct_answer="java.lang.String",
                explanation="Java's `String` is final to preserve immutability, thread safety, and string pool caching invariants."
            ),
            QuizQuestionBlueprint(
                question="Why do security frameworks apply `final` to cryptographic verification methods?",
                options=[
                    "To prevent malicious or buggy subclasses from bypassing authentication or fraud check routines",
                    "To compress cryptographic keys into fewer bytes",
                    "Because final methods run faster on GPUs",
                    "Because final methods do not require electricity"
                ],
                correct_answer="To prevent malicious or buggy subclasses from bypassing authentication or fraud check routines",
                explanation="Locking security algorithms with final prevents derived classes from stubbing out authentication checks."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 38: Exception Handling in OOP (Try, Catch, Throw)
    # -------------------------------------------------------------
    DayBlueprint(
        order=38,
        title="Day 38: Exception Handling in OOP (Try, Catch, Throw)",
        concept="Object-Oriented Error Handling: Custom exception class hierarchies, raising/catching exceptions, the `finally` block, and domain error modeling",
        analogy="Think of a warning light system in a modern commercial jet airliner: if engine 1 overheats, the flight computer doesn't just crash the plane into the ground silently. Instead, it creates an emergency alert object (**Exception Object**) packed with details (temperature=1050C, engine=1) and broadcasts it up the cockpit chain. The master caution alarm catches the alert (**Catch/Except**), flashes a red light, and activates emergency fire extinguishers (**Handler**). OOP treats errors as rich, typed objects!",
        theory_sections=[
            {
                "heading": "Exceptions as First-Class Objects",
                "body": "In OOP, errors are not primitive numeric codes (like C return `-1`). **Exceptions are full-fledged objects** instantiated from class hierarchies rooted at `Exception`.\n\nBecause exceptions are objects:\n- They encapsulate rich context (error message, timestamps, failed inputs, stack traces).\n- They participate in polymorphic inheritance: catching a base exception type (like `LookupError`) automatically catches all its specialized derived subclasses (`KeyError`, `IndexError`)."
            },
            {
                "heading": "Designing Custom Domain Exceptions",
                "body": "In enterprise systems, creating domain-specific custom exception classes (inheriting from `Exception`) is standard practice:\n```python\nclass BankException(Exception): pass\nclass InsufficientFundsError(BankException): pass\nclass AccountLockedError(BankException): pass\n```\nThis allows calling code to catch high-level domain failures cleanly."
            }
        ],
        code_snippets=[
            {
                "title": "Custom Domain Exception Hierarchy in Python",
                "language": "python",
                "code": "# Root domain exception\nclass BankingError(Exception):\n    \"\"\"Base exception for all banking failures.\"\"\"\n    pass\n\n# Specialized derived exceptions\nclass InsufficientFundsError(BankingError):\n    def __init__(self, requested: float, available: float):\n        super().__init__(f'Cannot withdraw ${requested:.2f}. Available balance: ${available:.2f}')\n        self.requested = requested\n        self.available = available\n\nclass AccountLockedError(BankingError):\n    pass",
                "explanation": "Builds a domain exception hierarchy inheriting from Python's Exception."
            },
            {
                "title": "Raising and Catching Polymorphic Exceptions",
                "language": "python",
                "code": "def withdraw_funds(balance: float, amount: float):\n    if amount > balance:\n        # Instantiate and raise custom exception object\n        raise InsufficientFundsError(amount, balance)\n    return balance - amount\n\ntry:\n    new_bal = withdraw_funds(100.0, 250.0)\nexcept InsufficientFundsError as e:\n    print('Targeted Catch:', e)\n    print(f'Shortfall: ${e.requested - e.available:.2f}')\nexcept BankingError as e:\n    print('General Banking Catch:', e)",
                "explanation": "Demonstrates raising rich exception objects and inspecting their custom attributes."
            },
            {
                "title": "The Full try / except / else / finally Lifecycle",
                "language": "python",
                "code": "try:\n    print('1. Attempting critical operation...')\n    val = 10 / 2\nexcept ZeroDivisionError:\n    print('2. Error caught!')\nelse:\n    print(f'2. Success! Result is {val} (runs ONLY if no exception occurred)')\nfinally:\n    print('3. Cleanup: finally ALWAYS executes unconditionally!')",
                "explanation": "Illustrates the complete 4-part exception handling control flow."
            },
            {
                "title": "C++ / Java Exception Terminology Comparison",
                "language": "text",
                "code": "// Cross-Language Terminology:\n// Python:  try  / except  / raise  / finally\n// Java:    try  / catch   / throw  / finally\n// C++:     try  / catch   / throw  / (RAII destructors)",
                "explanation": "Maps exception terminology across Python, Java, and C++."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Custom Validation Exception Hierarchy",
            description="Create a base `ValidationError(Exception)` and two subclasses: `TooShortError(ValidationError)` and `NoSpecialCharError(ValidationError)`. Write a function `validate_password(pw: str)` that raises `TooShortError('Minimum 8 chars')` if len < 8, raises `NoSpecialCharError('Missing special char')` if no `!@#$%` is present, or returns `'Valid'`.",
            starter_code="class ValidationError(Exception):\n    pass\nclass TooShortError(ValidationError):\n    pass\nclass NoSpecialCharError(ValidationError):\n    pass\ndef validate_password(pw: str):\n    pass",
            solution_code="class ValidationError(Exception): pass\nclass TooShortError(ValidationError): pass\nclass NoSpecialCharError(ValidationError): pass\n\ndef validate_password(pw: str) -> str:\n    if len(pw) < 8:\n        raise TooShortError('Minimum 8 chars')\n    special_chars = set('!@#$%')\n    if not any(c in special_chars for c in pw):\n        raise NoSpecialCharError('Missing special char')\n    return 'Valid'",
            expected_output="Caught TooShortError: Minimum 8 chars\nCaught NoSpecialCharError: Missing special char\nValid"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Why is modeling errors as Objects superior to returning integer error codes (like `-1` or `500`)?",
                options=[
                    "Exception objects encapsulate rich diagnostic context, stack traces, and participate in polymorphic catch hierarchies",
                    "Because integer error codes consume 50GB of RAM",
                    "Because Python cannot compare integers",
                    "Exception objects prevent bugs from ever existing"
                ],
                correct_answer="Exception objects encapsulate rich diagnostic context, stack traces, and participate in polymorphic catch hierarchies",
                explanation="Exceptions carry rich state (messages, timestamps, attributes) and allow hierarchical catching of error categories."
            ),
            QuizQuestionBlueprint(
                question="In Python's exception handling, what is the purpose of the `finally` block?",
                options=[
                    "To execute cleanup logic unconditionally, regardless of whether an exception was raised, caught, or not",
                    "To terminate the entire computer system",
                    "To suppress all future errors forever",
                    "To restart the program from line 1"
                ],
                correct_answer="To execute cleanup logic unconditionally, regardless of whether an exception was raised, caught, or not",
                explanation="The `finally` block is guaranteed to execute regardless of whether exceptions were raised or handled."
            ),
            QuizQuestionBlueprint(
                question="If class `SubError` inherits from `BaseError`, what happens if a `try` block raises `SubError` and is followed by `except BaseError:`?",
                options=[
                    "The `except BaseError:` block catches the `SubError` because of polymorphic inheritance (SubError IS-A BaseError)",
                    "The exception is ignored and lost",
                    "A fatal crash occurs",
                    "The computer prompts the user for a password"
                ],
                correct_answer="The `except BaseError:` block catches the `SubError` because of polymorphic inheritance (SubError IS-A BaseError)",
                explanation="Because of inheritance, catching a superclass exception catches all derived subclass exceptions."
            ),
            QuizQuestionBlueprint(
                question="What keyword in Python is used to instantiate and trigger an exception object into the call stack?",
                options=[
                    "raise",
                    "throw",
                    "emit",
                    "trigger"
                ],
                correct_answer="raise",
                explanation="Python uses the `raise` keyword to throw exception objects up the call stack."
            ),
            QuizQuestionBlueprint(
                question="When does the `else` block execute in a `try / except / else / finally` statement?",
                options=[
                    "Exclusively when the `try` block completes successfully without raising any exceptions",
                    "Only when an exception is caught",
                    "Every single time",
                    "Only if the computer has an active internet connection"
                ],
                correct_answer="Exclusively when the `try` block completes successfully without raising any exceptions",
                explanation="The `else` clause in a try block runs only if no exceptions were thrown in the try block."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 39: Enumerations (Enums)
    # -------------------------------------------------------------
    DayBlueprint(
        order=39,
        title="Day 39: Enumerations (Enums)",
        concept="Type-Safe Constants: Python `enum.Enum`, auto-values, integer enums, and replacing dangerous magic strings/numbers",
        analogy="Imagine an online order status: if developers use raw strings, one developer writes `'pending'`, another writes `'PENDING'`, and a third makes a typo `'pnding'`. The shipping robot crashes because of the typo! An **Enumeration (Enum)** is like an official, sealed dropdown menu on a ballot: there are strictly 4 choices: `OrderState.PENDING`, `OrderState.PROCESSING`, `OrderState.SHIPPED`, and `OrderState.DELIVERED`. Nobody can invent a 5th option or make a spelling mistake!",
        theory_sections=[
            {
                "heading": "Why Use Enumerations?",
                "body": "An **Enum** (Enumeration) is a symbolic name for a set of related, distinct constant values. Using Enums eliminates **Magic Strings** and **Magic Numbers** from codebases, providing:\n- **Type Safety**: Functions only accept valid enum members, catching invalid values before runtime.\n- **Self-Documentation**: Code becomes readable and intention-revealing (`UserRole.ADMIN` vs `role == 1`).\n- **Refactoring Ease**: Changing an underlying enum value does not break callers referencing the symbolic name."
            },
            {
                "heading": "Python's `enum` Module",
                "body": "Python 3.4+ provides the standard library `enum` module:\n- `Enum`: Standard base class for symbolic names.\n- `IntEnum`: Values behave as integers (can be compared with `<` and `>`).\n- `auto()`: Automatically assigns sequential integer values, eliminating manual counting."
            }
        ],
        code_snippets=[
            {
                "title": "Defining and Using an Enum in Python",
                "language": "python",
                "code": "from enum import Enum, auto\n\nclass OrderStatus(Enum):\n    PENDING = auto()\n    PROCESSING = auto()\n    SHIPPED = auto()\n    DELIVERED = auto()\n    CANCELLED = auto()\n\nclass Order:\n    def __init__(self, order_id: str):\n        self.order_id = order_id\n        self.status = OrderStatus.PENDING\n\n    def advance(self):\n        if self.status == OrderStatus.PENDING:\n            self.status = OrderStatus.PROCESSING\n        elif self.status == OrderStatus.PROCESSING:\n            self.status = OrderStatus.SHIPPED\n\no = Order('ORD-101')\no.advance()\nprint('Order status name:', o.status.name)\nprint('Order status value:', o.status.value)",
                "explanation": "Enums enforce strict symbolic state transitions."
            },
            {
                "title": "Enum Equality and Identity Comparison",
                "language": "python",
                "code": "# Enums are singletons: compare using 'is' or '=='\nprint('Is status SHIPPED?', o.status is OrderStatus.SHIPPED)    # False\nprint('Is status PROCESSING?', o.status == OrderStatus.PROCESSING) # True\n\n# Lookup enum member by value\nlookup_status = OrderStatus(1)\nprint('Lookup by value 1:', lookup_status.name)",
                "explanation": "Enum members are unique singletons compared using the 'is' operator."
            },
            {
                "title": "String Enums for Clean JSON Serialization",
                "language": "python",
                "code": "class Priority(str, Enum):\n    LOW = 'LOW'\n    MEDIUM = 'MEDIUM'\n    HIGH = 'HIGH'\n    CRITICAL = 'CRITICAL'\n\n# Inheriting str allows direct JSON serialization and string comparison\nprint('Is HIGH equal to string \"HIGH\"?', Priority.HIGH == 'HIGH')\nprint('Serialized to JSON:', {'ticket_id': 99, 'priority': Priority.CRITICAL})",
                "explanation": "Combining str with Enum allows effortless JSON serialization."
            },
            {
                "title": "Iterating Over All Enum Members",
                "language": "python",
                "code": "print('All available OrderStatus options:')\nfor member in OrderStatus:\n    print(f'  -> {member.name} (Value: {member.value})')",
                "explanation": "Enums are fully iterable containers of all valid options."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="HTTP Status Code Enum",
            description="Create an `IntEnum` named `HTTPStatus` with members `OK = 200`, `CREATED = 201`, `BAD_REQUEST = 400`, `UNAUTHORIZED = 401`, and `NOT_FOUND = 404`. Write a function `is_client_error(status: HTTPStatus) -> bool` that returns `True` if status is in the 400 range, else `False`.",
            starter_code="from enum import IntEnum\n# Implement HTTPStatus and is_client_error\npass",
            solution_code="from enum import IntEnum\n\nclass HTTPStatus(IntEnum):\n    OK = 200\n    CREATED = 201\n    BAD_REQUEST = 400\n    UNAUTHORIZED = 401\n    NOT_FOUND = 404\n\ndef is_client_error(status: HTTPStatus) -> bool:\n    return 400 <= status.value < 500",
            expected_output="True\nFalse"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the primary benefit of using Enumerations (Enums) over raw strings or numbers?",
                options=[
                    "Enums prevent typos, eliminate magic values, provide autocomplete, and restrict variables to valid symbolic options",
                    "Enums compress data by 80%",
                    "Enums make code run on mobile phones without compilation",
                    "Enums eliminate the need for operating systems"
                ],
                correct_answer="Enums prevent typos, eliminate magic values, provide autocomplete, and restrict variables to valid symbolic options",
                explanation="Enums provide type-safe, self-documenting symbols that eliminate spelling errors and magic numbers."
            ),
            QuizQuestionBlueprint(
                question="In Python's `enum.Enum`, how do you access the human-readable identifier of a member (e.g. `'PENDING'`)?",
                options=[
                    "member.name",
                    "member.value",
                    "member.identifier",
                    "member.string"
                ],
                correct_answer="member.name",
                explanation="Every enum member exposes `.name` for its symbolic string and `.value` for its underlying raw value."
            ),
            QuizQuestionBlueprint(
                question="What does the `auto()` helper function do when defining Enum members in Python?",
                options=[
                    "It automatically assigns sequential integer values to each member so you don't have to number them manually",
                    "It automatically creates a car object",
                    "It converts the enum into an automated bot",
                    "It triggers automated testing"
                ],
                correct_answer="It automatically assigns sequential integer values to each member so you don't have to number them manually",
                explanation="`auto()` automatically generates sequential integer values for enum members."
            ),
            QuizQuestionBlueprint(
                question="Why is comparing Enum members with the `is` operator (e.g. `status is Status.ACTIVE`) safe and recommended?",
                options=[
                    "Because each Enum member is a unique singleton instance in memory",
                    "Because `is` runs 500 times faster than `==`",
                    "Because `==` is not supported on enums",
                    "Because Python forces you to use `is`"
                ],
                correct_answer="Because each Enum member is a unique singleton instance in memory",
                explanation="Enum members are singletons, making reference identity comparison (`is`) fast and safe."
            ),
            QuizQuestionBlueprint(
                question="What specialized enum class from Python's standard library allows enum members to be compared directly with integer numbers?",
                options=[
                    "enum.IntEnum",
                    "enum.NumberEnum",
                    "enum.DigitEnum",
                    "enum.MathEnum"
                ],
                correct_answer="enum.IntEnum",
                explanation="`IntEnum` subclasses both `int` and `Enum`, allowing members to behave as integers in numeric comparisons."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 40: Anonymous Classes and Inner/Nested Classes
    # -------------------------------------------------------------
    DayBlueprint(
        order=40,
        title="Day 40: Anonymous Classes & Inner/Nested Classes",
        concept="Scoped and Transient Classes: Defining Inner/Nested classes for helper encapsulation, Java Anonymous Classes, and Python callable closures / lambdas",
        analogy="Think of a Car and its Engine: the Engine is so intimately tied to the car that nobody buys a standalone car engine to sit on their living room carpet. Nesting the `Engine` class **inside** the `Car` class (**Inner Class**) keeps the engine tucked away where only the Car can see and configure it. An Anonymous class is like a temporary paper papercraft stencil: you fold it for 10 seconds to trace a shape onto wood, and toss it in the recycling bin immediately after!",
        theory_sections=[
            {
                "heading": "Inner (Nested) Classes",
                "body": "An **Inner Class** is a class defined entirely inside the body of another enclosing class. Why nest classes?\n- **Logical Grouping**: If a helper class (e.g., `Node` inside `LinkedList`, `Header` inside `Email`) is used exclusively by one outer class, nesting it keeps the global namespace clean.\n- **Enhanced Encapsulation**: Inner classes can access private members of the outer enclosing class in languages like Java.\n- **Maintainability**: Groups closely coupled helper logic directly alongside the primary domain model."
            },
            {
                "heading": "Anonymous Classes across Languages",
                "body": "- **In Java**: Anonymous Inner Classes allow defining and instantiating an ad-hoc class on the fly without giving it a formal name (commonly used for GUI event listeners like `button.addActionListener(new ActionListener() { ... })`).\n- **In Python**: Python achieves anonymous transient behavior using **Lambda Functions** (`lambda x: x * 2`), **Closures**, and the `type()` dynamic class creation function."
            }
        ],
        code_snippets=[
            {
                "title": "Defining an Inner Class in Python: Order and Item",
                "language": "python",
                "code": "class Order:\n    # Inner Class: scoped strictly within Order namespace\n    class Item:\n        def __init__(self, name: str, price: float):\n            self.name = name\n            self.price = price\n\n    def __init__(self, order_id: str):\n        self.order_id = order_id\n        self.items = []\n\n    def add_item(self, name: str, price: float):\n        # Instantiate inner class directly\n        item = Order.Item(name, price)\n        self.items.append(item)\n\n    def get_total(self) -> float:\n        return sum(item.price for item in self.items)\n\no = Order('ORD-55')\no.add_item('Keyboard', 75.0)\no.add_item('Mouse', 25.0)\nprint('Order Total:', o.get_total())",
                "explanation": "Item is logically scoped inside Order, preventing namespace pollution."
            },
            {
                "title": "Accessing Inner Classes from External Code",
                "language": "python",
                "code": "# Inner classes can still be referenced via OuterClass.InnerClass\nstandalone_item = Order.Item('Monitor', 300.0)\nprint('Item created via outer namespace:', standalone_item.name)",
                "explanation": "Inner classes reside within the outer class namespace."
            },
            {
                "title": "Dynamic Anonymous Classes in Python using type()",
                "language": "python",
                "code": "# Python's dynamic 3-argument type() creates an anonymous class at runtime!\n# type(name, bases, dict)\nAnonymousHandler = type('TempHandler', (object,), {\n    'handle': lambda self, msg: f'Handled: {msg}'\n})\n\nhandler = AnonymousHandler()\nprint(handler.handle('Event packet 404'))",
                "explanation": "type() constructs dynamic, on-the-fly anonymous classes at runtime."
            },
            {
                "title": "Java Anonymous Inner Class (Conceptual Comparison)",
                "language": "text",
                "code": "// In Java:\n// Runnable r = new Runnable() {\n//     @Override\n//     public void run() { System.out.println(\"Running in anonymous class!\"); }\n// };",
                "explanation": "Shows Java's classic anonymous class syntax used before lambdas."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="LinkedList with Nested Node Class",
            description="Create a `LinkedList` class containing an inner class `Node(value)`. Implement a method `append(val)` that wraps `val` in a new `Node` and chains it to the end of the list, and a `to_list()` method returning a list of all node values.",
            starter_code="class LinkedList:\n    # Implement LinkedList with inner Node class\n    pass",
            solution_code="class LinkedList:\n    class Node:\n        def __init__(self, value):\n            self.value = value\n            self.next = None\n\n    def __init__(self):\n        self.head = None\n\n    def append(self, val):\n        new_node = LinkedList.Node(val)\n        if not self.head:\n            self.head = new_node\n            return\n        curr = self.head\n        while curr.next:\n            curr = curr.next\n        curr.next = new_node\n\n    def to_list(self) -> list:\n        res = []\n        curr = self.head\n        while curr:\n            res.append(curr.value)\n            curr = curr.next\n        return res",
            expected_output="[10, 20, 30]"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the primary motivation for defining an Inner (Nested) class?",
                options=[
                    "To logically group helper classes that belong strictly to the outer class and keep the global namespace clean",
                    "To speed up hard drive read speeds",
                    "Because Python forbids creating classes in global scope",
                    "To encrypt the inner class with a password"
                ],
                correct_answer="To logically group helper classes that belong strictly to the outer class and keep the global namespace clean",
                explanation="Inner classes group helper logic close to its consumer, preventing pollution of the top-level module namespace."
            ),
            QuizQuestionBlueprint(
                question="How do you instantiate an inner class `Inner` defined inside `Outer` from outside code in Python?",
                options=[
                    "Outer.Inner()",
                    "Inner.Outer()",
                    "new Outer->Inner()",
                    "import Inner from Outer"
                ],
                correct_answer="Outer.Inner()",
                explanation="Inner classes are attributes of the outer class object, accessed via dot notation: `Outer.Inner()`."
            ),
            QuizQuestionBlueprint(
                question="What is an 'Anonymous Class' in Java?",
                options=[
                    "A class defined and instantiated simultaneously in a single expression without giving it an explicit class name",
                    "A class created by hackers on the dark web",
                    "A class with no methods or variables",
                    "A class that cannot be viewed in text editors"
                ],
                correct_answer="A class defined and instantiated simultaneously in a single expression without giving it an explicit class name",
                explanation="Anonymous classes define and instantiate an inline one-off class without assigning a formal type identifier."
            ),
            QuizQuestionBlueprint(
                question="Which Python built-in function can be used to dynamically synthesize anonymous class objects at runtime?",
                options=[
                    "type(name, bases, dict)",
                    "class()",
                    "create_class()",
                    "struct.make()"
                ],
                correct_answer="type(name, bases, dict)",
                explanation="The 3-argument form of `type()` dynamically builds classes at runtime."
            ),
            QuizQuestionBlueprint(
                question="What is a classic data structure example where Inner Classes are universally utilized?",
                options=[
                    "Linked lists and Trees: defining a private `Node` class inside the `LinkedList` or `BinaryTree` container",
                    "A simple integer variable",
                    "A print statement",
                    "A for loop"
                ],
                correct_answer="Linked lists and Trees: defining a private `Node` class inside the `LinkedList` or `BinaryTree` container",
                explanation="`Node` helper classes are famously nested inside graph, tree, and linked-list data structures."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 41: Object Cloning (Shallow vs Deep Copy)
    # -------------------------------------------------------------
    DayBlueprint(
        order=41,
        title="Day 41: Object Cloning (Shallow vs Deep Copy)",
        concept="Memory Cloning Mechanics: Reference assignment vs Shallow copy (`copy.copy`) vs Deep copy (`copy.deepcopy`), and recursive pointer graphs",
        analogy="Imagine an address book containing sticky notes pointing to your friends' house keys. **Reference Assignment** is just handing someone your glasses: there is still only 1 address book. **Shallow Copy** is photocopying the pages of the address book: you now have 2 physical address books, but they both point to the *exact same physical house keys* (if someone melts the key, both books lose out!). **Deep Copy** is duplicating the address book AND manufacturing a brand new duplicate set of houses, doors, and keys from scratch!",
        theory_sections=[
            {
                "heading": "The Hazards of Reference Assignment",
                "body": "In Python, writing `b = a` **does not copy the object**! It merely creates a second reference (pointer) pointing to the exact same memory address. Mutating `b` silently mutates `a`."
            },
            {
                "heading": "Shallow Copy vs Deep Copy",
                "body": "Python's `copy` module provides two cloning modes:\n1. **Shallow Copy (`copy.copy(obj)`)**: Constructs a new compound object, but populates it with references to the child objects found in the original. If the object contains nested mutable collections (lists, dictionaries, child objects), the nested objects are **shared** between original and clone.\n2. **Deep Copy (`copy.deepcopy(obj)`)**: Recursively copies the compound object AND all nested child objects down to the leaves of the reference tree. The clone is 100% completely isolated from the original."
            }
        ],
        code_snippets=[
            {
                "title": "Reference Assignment vs Shallow Copy vs Deep Copy",
                "language": "python",
                "code": "import copy\n\nclass Address:\n    def __init__(self, city: str): self.city = city\n\nclass Person:\n    def __init__(self, name: str, city: str):\n        self.name = name\n        self.address = Address(city)\n\norig = Person('Alice', 'New York')\n\n# 1. Shallow Copy\nshallow_clone = copy.copy(orig)\n# 2. Deep Copy\ndeep_clone = copy.deepcopy(orig)\n\n# Mutate nested Address object in original\norig.address.city = 'London'\n\nprint('Original City:', orig.address.city)          # London\nprint('Shallow Clone City:', shallow_clone.address.city)  # London! (Shared pointer)\nprint('Deep Clone City:', deep_clone.address.city)        # New York! (Isolated clone)",
                "explanation": "Shallow copy shares nested Address; deep copy duplicates the entire object graph."
            },
            {
                "title": "Customizing Cloning with __copy__ and __deepcopy__",
                "language": "python",
                "code": "class CustomResource:\n    def __init__(self, identifier: str):\n        self.identifier = identifier\n\n    def __deepcopy__(self, memo):\n        # Custom cloning logic to ensure unique clone IDs\n        return CustomResource(f'{self.identifier}_CLONE')\n\nres = CustomResource('RES-100')\ncloned_res = copy.deepcopy(res)\nprint('Original ID:', res.identifier)\nprint('Cloned ID:', cloned_res.identifier)",
                "explanation": "Dunder methods __copy__ and __deepcopy__ customize cloning behavior."
            },
            {
                "title": "Circular References Handled Safely by deepcopy",
                "language": "python",
                "code": "# Python's deepcopy tracks visited objects in the 'memo' dict to avoid infinite loops\na = []\nb = [a]\na.append(b)\n\ncloned_a = copy.deepcopy(a)\nprint('Circular reference cloned successfully without stack overflow!')",
                "explanation": "deepcopy internally uses a memo dictionary to safely clone circular graphs."
            },
            {
                "title": "C++ Copy Constructors vs Python Cloning",
                "language": "text",
                "code": "// In C++:\n// MyClass(const MyClass& other) { // Copy constructor dictates deep vs shallow copy\n//     this->data = new int(*other.data); // Allocate fresh memory for deep copy\n// }",
                "explanation": "Contrasts Python's copy module with C++'s explicit copy constructor mechanics."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Deep Copy of Game Inventory",
            description="Create an `Inventory` class with an attribute `items: list`. Implement a method `clone()` using `copy.deepcopy()` so that modifying the cloned inventory's items list never affects the original inventory.",
            starter_code="import copy\nclass Inventory:\n    # Implement Inventory with clone()\n    pass",
            solution_code="import copy\nclass Inventory:\n    def __init__(self, items: list = None):\n        self.items = list(items) if items else []\n\n    def clone(self) -> 'Inventory':\n        return copy.deepcopy(self)",
            expected_output="Original items count: 2\nCloned items count: 3"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What happens when you execute `obj2 = obj1` in Python?",
                options=[
                    "A new reference pointing to the exact same object in memory is created (no object is copied)",
                    "A deep copy of the object is created",
                    "A shallow copy is created",
                    "The object is deleted"
                ],
                correct_answer="A new reference pointing to the exact same object in memory is created (no object is copied)",
                explanation="Simple assignment copies the memory pointer, not the underlying object."
            ),
            QuizQuestionBlueprint(
                question="What is the critical difference between a Shallow Copy and a Deep Copy?",
                options=[
                    "A Shallow Copy duplicates the top-level object but shares references to nested child objects; a Deep Copy recursively duplicates all nested objects",
                    "A Shallow Copy is for numbers; a Deep Copy is for text",
                    "Shallow copies take longer to execute than deep copies",
                    "Deep copy cannot be used on classes"
                ],
                correct_answer="A Shallow Copy duplicates the top-level object but shares references to nested child objects; a Deep Copy recursively duplicates all nested objects",
                explanation="Shallow copies duplicate the outermost container while sharing nested pointers; deep copies clone the full graph."
            ),
            QuizQuestionBlueprint(
                question="Which standard library module in Python provides `copy()` and `deepcopy()`?",
                options=[
                    "copy",
                    "clone",
                    "sys",
                    "memory"
                ],
                correct_answer="copy",
                explanation="The built-in `copy` module contains shallow `copy()` and recursive `deepcopy()`."
            ),
            QuizQuestionBlueprint(
                question="How does Python's `copy.deepcopy()` prevent infinite recursion when cloning objects that contain circular references (A -> B -> A)?",
                options=[
                    "It maintains an internal `memo` dictionary tracking already-copied memory IDs",
                    "It crashes after 100 iterations",
                    "It ignores circular references",
                    "It deletes the circular object"
                ],
                correct_answer="It maintains an internal `memo` dictionary tracking already-copied memory IDs",
                explanation="The `memo` dictionary maps original object IDs to their clones, preventing circular loops."
            ),
            QuizQuestionBlueprint(
                question="Which dunder method can you implement on a class to customize how `copy.deepcopy()` duplicates its instances?",
                options=[
                    "__deepcopy__(self, memo)",
                    "__clone__(self)",
                    "__duplicate__(self)",
                    "__copy_all__(self)"
                ],
                correct_answer="__deepcopy__(self, memo)",
                explanation="Implementing `__deepcopy__(self, memo)` allows custom control over recursive cloning."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 42: UML Basics & Class Diagrams
    # -------------------------------------------------------------
    DayBlueprint(
        order=42,
        title="Day 42: UML Basics & Class Diagrams",
        concept="Object-Oriented Analysis & Design (OOAD): Unified Modeling Language (UML) class diagram notations, visibility markers (+, -, #), and relationship arrows",
        analogy="Before a civil engineer pours tons of concrete to build a suspension bridge, they draw an architectural blueprint using standardized engineering symbols that any builder in the world can understand. **UML (Unified Modeling Language)** is the global architectural blueprint for software engineers: with standard 3-box rectangles, plus signs, and arrows, you can visualize an entire 500-class software architecture on a whiteboard before writing a single line of code!",
        theory_sections=[
            {
                "heading": "Anatomy of a UML Class Box",
                "body": "In a UML Class Diagram, every class is represented as a **3-Compartment Rectangle**:\n1. **Top Compartment**: Class Name (italicized if Abstract).\n2. **Middle Compartment**: Attributes with visibility markers and types:\n   - `+` : Public\n   - `-` : Private\n   - `#` : Protected\n   - `~` : Package/Internal\n   - Example: `- balance: float`\n3. **Bottom Compartment**: Methods with parameter types and return types:\n   - Example: `+ withdraw(amount: float): bool`"
            },
            {
                "heading": "Standard UML Relationship Connectors",
                "body": "- **Inheritance (Generalization)**: Solid line with **large hollow closed triangle arrow** pointing to parent.\n- **Interface Implementation (Realization)**: Dashed line with **large hollow triangle arrow**.\n- **Association**: Solid line with simple arrow or no arrow.\n- **Aggregation**: Solid line with **hollow white diamond** at container end.\n- **Composition**: Solid line with **solid black filled diamond** at container end.\n- **Dependency**: Dashed line with open arrow (`- - - >`)."
            }
        ],
        code_snippets=[
            {
                "title": "Textual Representation of a Standard UML Class Box",
                "language": "text",
                "code": "+-------------------------------------------+\n|                BankAccount                | <-- Class Name\n+-------------------------------------------+\n| - account_number: str                     | <-- Attributes\n| - _balance: float                         |     (- private, + public)\n| # owner_id: str                           |     (# protected)\n+-------------------------------------------+\n| + deposit(amount: float): bool            | <-- Methods\n| + withdraw(amount: float): bool           |\n| + get_balance(): float                    |\n+-------------------------------------------+",
                "explanation": "Visualizes the standard 3-compartment UML class specification."
            },
            {
                "title": "Converting UML Class Notation directly to Python Code",
                "language": "python",
                "code": "# Python implementation directly corresponding to the UML box above:\nclass BankAccount:\n    def __init__(self, account_number: str, owner_id: str, initial_balance: float = 0.0):\n        self.__account_number = account_number  # - private\n        self._balance = initial_balance          # - private / protected\n        self._owner_id = owner_id               # # protected\n\n    def deposit(self, amount: float) -> bool:   # + public\n        if amount > 0: self._balance += amount; return True\n        return False\n\n    def withdraw(self, amount: float) -> bool:  # + public\n        if 0 < amount <= self._balance: self._balance -= amount; return True\n        return False",
                "explanation": "Demonstrates 1-to-1 mapping from UML diagram specification to Python code."
            },
            {
                "title": "UML Relationship Connector Reference Chart",
                "language": "text",
                "code": "Relationship       Line Style    Arrowhead at Target\n----------------------------------------------------\nInheritance        Solid         Hollow Triangle (----|>)\nRealization        Dashed        Hollow Triangle (-- -|>)\nComposition        Solid         Solid Diamond   (*----)\nAggregation        Solid         Hollow Diamond  (o----)\nDependency         Dashed        Open Arrow      (-- ->)",
                "explanation": "Reference chart for reading and drawing standard UML connector lines."
            },
            {
                "title": "PlantUML Syntax for Automated Class Diagram Generation",
                "language": "text",
                "code": "@startuml\nclass Vehicle {\n  + speed: float\n  + accelerate(amount: float): void\n}\nclass Car {\n  + num_doors: int\n}\nVehicle <|-- Car : Inheritance\n@enduml",
                "explanation": "PlantUML markup format commonly used in CI/CD and engineering documentation."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Implement Class from UML Specification",
            description="Implement the class `Customer` from this UML specification:\n`+-------------------------+`\n`| Customer                |`\n`+-------------------------+`\n`| - _customer_id: str     |`\n`| + name: str             |`\n`| - _loyalty_points: int  |`\n`+-------------------------+`\n`| + add_points(pts: int)  |`\n`| + get_points(): int     |`\n`+-------------------------+`",
            starter_code="class Customer:\n    # Implement Customer based on UML spec\n    pass",
            solution_code="class Customer:\n    def __init__(self, customer_id: str, name: str, loyalty_points: int = 0):\n        self._customer_id = customer_id\n        self.name = name\n        self._loyalty_points = int(loyalty_points)\n\n    def add_points(self, pts: int):\n        if pts > 0:\n            self._loyalty_points += pts\n\n    def get_points(self) -> int:\n        return self._loyalty_points",
            expected_output="Customer Alice points: 150"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What do the three vertical compartments of a standard UML class box represent from top to bottom?",
                options=[
                    "Top: Class Name, Middle: Attributes/Fields, Bottom: Operations/Methods",
                    "Top: Author, Middle: Code, Bottom: License",
                    "Top: Variables, Middle: Loops, Bottom: Tests",
                    "Top: URL, Middle: IP address, Bottom: Port"
                ],
                correct_answer="Top: Class Name, Middle: Attributes/Fields, Bottom: Operations/Methods",
                explanation="Standard UML class boxes contain Name (top), Attributes (middle), and Methods (bottom)."
            ),
            QuizQuestionBlueprint(
                question="In UML notation, what does a minus sign (`-`) preceding an attribute name signify?",
                options=[
                    "Private visibility",
                    "Public visibility",
                    "Negative numeric value",
                    "Deleted attribute"
                ],
                correct_answer="Private visibility",
                explanation="`-` signifies Private, `+` signifies Public, and `#` signifies Protected."
            ),
            QuizQuestionBlueprint(
                question="In UML notation, what does a hash symbol (`#`) preceding a member signify?",
                options=[
                    "Protected visibility",
                    "A Python comment",
                    "Twitter hashtag",
                    "Public visibility"
                ],
                correct_answer="Protected visibility",
                explanation="In UML, `#` indicates Protected access (accessible by class and subclasses)."
            ),
            QuizQuestionBlueprint(
                question="What line style and arrow symbol represents Inheritance (Generalization) in UML?",
                options=[
                    "A solid line with a large hollow closed triangle pointing to the parent class",
                    "A solid line with a solid black diamond",
                    "A dashed line with an open arrow",
                    "A double red line"
                ],
                correct_answer="A solid line with a large hollow closed triangle pointing to the parent class",
                explanation="Generalization (Inheritance) uses a solid line terminating in a hollow closed triangle pointing upward."
            ),
            QuizQuestionBlueprint(
                question="Why are UML diagrams valuable during the architectural design phase of an enterprise project?",
                options=[
                    "They allow developers and architects to visualize, model, and critique system relationships before writing code, catching design flaws early",
                    "They eliminate the need to write unit tests",
                    "They speed up CPU processing by 200%",
                    "They make Python run on quantum computers"
                ],
                correct_answer="They allow developers and architects to visualize, model, and critique system relationships before writing code, catching design flaws early",
                explanation="UML enables collaborative architectural review and domain modeling before committing to code implementation."
            )
        ]
    )
]
