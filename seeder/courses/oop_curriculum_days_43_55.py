"""
Object-Oriented Programming (OOP) - 55-Day Curriculum - Part 4 (Days 43 to 55)
Module 8: OOAD Continued (Days 43-44)
Module 9: SOLID Principles (Days 45-50)
Module 10: Design Patterns (Days 51-55)
"""

from seeder.course_blueprint import DayBlueprint, QuizQuestionBlueprint, CodingChallengeBlueprint

DAYS_43_TO_55 = [
    # -------------------------------------------------------------
    # DAY 43: Object & Use Case Diagrams
    # -------------------------------------------------------------
    DayBlueprint(
        order=43,
        title="Day 43: Object & Use Case Diagrams",
        concept="Dynamic and Behavioral Modeling: Object Diagrams (runtime snapshots of instantiated memory) and Use Case Diagrams (actor interactions and system boundaries)",
        analogy="Think of a movie production: a Class Diagram is the cast character descriptions on the script ('Detective, age 40, owns a badge'). An **Object Diagram** is taking a freeze-frame photograph during Scene 4: it shows Detective Miller sitting in Car #12 at 10:42 PM holding a warm cup of coffee. A **Use Case Diagram** is the storyboard showing who interacts with what: the Bank Robber holds up the Bank, the Teller presses the Silent Alarm, and the Police Officer responds to the Call!",
        theory_sections=[
            {
                "heading": "Object Diagrams: Runtime Snapshots",
                "body": "While a Class Diagram models static structure at compile time, an **Object Diagram** models a **runtime snapshot** of specific objects in memory at an exact moment in time.\n\nKey elements:\n- **Instance Notation**: Underlined name: `alice: Customer` or `:Order` (anonymous).\n- **State Values**: Displays actual current variable values (e.g., `balance = $250.00`, `status = SHIPPED`).\n- **Links**: Concrete instances of associations connecting objects."
            },
            {
                "heading": "Use Case Diagrams: Actors and System Boundaries",
                "body": "**Use Case Diagrams** capture functional requirements from the perspective of external users (**Actors**):\n- **Actors (Stick figures)**: External entities (Human user, Payment Gateway API, Cron scheduler) that initiate interactions.\n- **Use Cases (Ovals)**: Specific goal-oriented actions (e.g., *Login*, *Search Catalog*, *Checkout*).\n- **System Boundary (Rectangle)**: Encapsulates the scope of the application.\n- **`<<include>>`**: Mandatory sub-step (e.g., *Checkout* `<<includes>>` *Process Payment*).\n- **`<<extend>>`**: Optional conditional behavior (e.g., *Apply Coupon Code* `<<extends>>` *Checkout*)."
            }
        ],
        code_snippets=[
            {
                "title": "Mapping a Use Case Diagram to Service Methods",
                "language": "python",
                "code": "class ECommerceSystem:\n    # Actor: Customer\n    def search_catalog(self, query: str) -> list:\n        return [f'Result for {query}']\n\n    # Use Case: Checkout (<<includes>> process_payment)\n    def checkout(self, cart_id: str, payment_token: str) -> dict:\n        self._validate_cart(cart_id)\n        # Mandatory included use case step\n        tx = self._process_payment(payment_token)\n        return {'status': 'ORDER_PLACED', 'transaction': tx}\n\n    def _validate_cart(self, c_id): pass\n    def _process_payment(self, tok): return 'TX-9988'",
                "explanation": "Demonstrates code mapping for use cases and included sub-steps."
            },
            {
                "title": "Textual Representation of an Object Diagram Snapshot",
                "language": "text",
                "code": "+-----------------------------+       +-----------------------------+\n|   alice: Customer           | ----> |   order101: Order           |\n+-----------------------------+       +-----------------------------+\n| id = \"C-42\"                 |       | id = \"ORD-101\"              |\n| name = \"Alice\"              |       | total = 149.99              |\n+-----------------------------+       | status = \"PROCESSING\"       |\n                                      +-----------------------------+",
                "explanation": "Illustrates runtime object diagram showing specific attribute states and links."
            },
            {
                "title": "Use Case <<include>> vs <<extend>> in Code Flow",
                "language": "python",
                "code": "def checkout_flow(cart, coupon_code=None):\n    # Mandatory <<include>>: Calculate taxes\n    tax = cart.total * 0.08\n    # Optional <<extend>>: Apply coupon if provided\n    if coupon_code:\n        discount = 15.0\n        print(f'<<extend>> Applied coupon: -${discount}')\n    return cart.total + tax",
                "explanation": "Contrasts mandatory includes with optional conditional extends."
            },
            {
                "title": "Python Script: Capturing a Runtime Object Snapshot",
                "language": "python",
                "code": "class OrderSnapshot:\n    def __init__(self, order_id, total):\n        self.order_id, self.total = order_id, total\n\nsnap = OrderSnapshot('ORD-99', 54.0)\nprint('Runtime Object Snapshot:', snap.__dict__)",
                "explanation": "Inspects instance state representing an object diagram point-in-time snapshot."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Use Case Order Processor with <<include>> & <<extend>>",
            description="Create an `OrderProcessor` class with method `process_order(amount: float, promo_code: str = None) -> float`. It must always add a mandatory 5% tax (`<<include>>`). If `promo_code == 'SAVE10'`, it conditionally deducts 10.0 before tax (`<<extend>>`). Return the final total float.",
            starter_code="class OrderProcessor:\n    # Implement process_order with mandatory tax and optional promo\n    pass",
            solution_code="class OrderProcessor:\n    def process_order(self, amount: float, promo_code: str = None) -> float:\n        subtotal = float(amount)\n        if promo_code == 'SAVE10':\n            subtotal = max(0.0, subtotal - 10.0)\n        total = subtotal * 1.05\n        return round(total, 2)",
            expected_output="105.0\n94.5"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the difference between a Class Diagram and an Object Diagram in UML?",
                options=[
                    "A Class Diagram shows static blueprint structure; an Object Diagram captures a runtime snapshot of specific instances with concrete values",
                    "A Class Diagram is for Python; an Object Diagram is for JavaScript",
                    "An Object Diagram contains no text",
                    "They are identical diagrams with different colors"
                ],
                correct_answer="A Class Diagram shows static blueprint structure; an Object Diagram captures a runtime snapshot of specific instances with concrete values",
                explanation="Class diagrams show structural types; object diagrams capture point-in-time runtime instances and their variable states."
            ),
            QuizQuestionBlueprint(
                question="In a UML Use Case diagram, what does a stick figure symbol represent?",
                options=[
                    "An Actor (an external user, device, or third-party system that interacts with the software)",
                    "A variable name",
                    "A deleted function",
                    "An infinite loop"
                ],
                correct_answer="An Actor (an external user, device, or third-party system that interacts with the software)",
                explanation="Actors represent external entities (people, APIs, background jobs) that trigger use cases."
            ),
            QuizQuestionBlueprint(
                question="What is the difference between `<<include>>` and `<<extend>>` in a Use Case diagram?",
                options=[
                    "`<<include>>` represents a mandatory sub-step that always runs; `<<extend>>` represents an optional conditional extension",
                    "`<<include>>` is for math; `<<extend>>` is for strings",
                    "`<<include>>` is used in C++; `<<extend>>` is used in Python",
                    "There is no difference"
                ],
                correct_answer="`<<include>>` represents a mandatory sub-step that always runs; `<<extend>>` represents an optional conditional extension",
                explanation="Included use cases are mandatory core sub-steps; extended use cases execute conditionally under specific triggers."
            ),
            QuizQuestionBlueprint(
                question="How are instance names formatted inside an Object Diagram to distinguish them from class names?",
                options=[
                    "They are underlined and written as `instanceName : ClassName`",
                    "They are written in all bold Greek letters",
                    "They are preceded by a dollar sign",
                    "They are written backwards"
                ],
                correct_answer="They are underlined and written as `instanceName : ClassName`",
                explanation="UML convention mandates underlining instance names (e.g. `_alice: Customer_`) in object diagrams."
            ),
            QuizQuestionBlueprint(
                question="What does the rectangular box surrounding use case ovals represent in a Use Case diagram?",
                options=[
                    "The System Boundary: defining what functionality is inside the software versus external to it",
                    "The computer monitor screen size",
                    "The firewall blocking hacker attacks",
                    "The database primary key"
                ],
                correct_answer="The System Boundary: defining what functionality is inside the software versus external to it",
                explanation="The system boundary box demarcates the internal scope of the application from external actors."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 44: Sequence Diagrams
    # -------------------------------------------------------------
    DayBlueprint(
        order=44,
        title="Day 44: Sequence Diagrams",
        concept="Dynamic Interaction Modeling: Sequence Diagrams - Lifelines, activation boxes, synchronous/asynchronous messages, return values, and chronological call flows",
        analogy="Think of a Broadway musical script: along the top of the page, the characters stand in order: `Actor`, `Cashier`, `Bank Computer`. Going down the page vertically represents the flow of time: 10:00:00 Actor hands check to Cashier -> 10:00:02 Cashier types into Computer -> 10:00:04 Computer beeps approval -> 10:00:05 Cashier hands cash to Actor. A Sequence Diagram is the chronological script of how objects pass messages back and forth in real time!",
        theory_sections=[
            {
                "heading": "Anatomy of a UML Sequence Diagram",
                "body": "A **Sequence Diagram** models dynamic object interactions ordered chronologically across time:\n- **Participants / Lifelines**: Represented as boxes along the top with vertical dashed lines flowing downwards (representing the passage of time).\n- **Activation Bar**: A thin vertical rectangle on the lifeline indicating that the object is actively processing a method.\n- **Synchronous Call (Solid line with filled arrow `--->`)**: The sender blocks waiting for a response.\n- **Return Message (Dashed line with open arrow `<---`)**: Hands back the return value.\n- **Asynchronous Call (Solid line with open arrow `--->`)**: Non-blocking message (like queuing a task in RabbitMQ or dispatching a background thread)."
            },
            {
                "heading": "Control Logic: `alt`, `opt`, and `loop` Blocks",
                "body": "Sequence diagrams handle algorithmic branching with combined fragments:\n- **`alt` (Alternative)**: Equivalent to `if/else` logic.\n- **`opt` (Optional)**: Equivalent to an `if` statement without an `else`.\n- **`loop`**: Represents `for` and `while` loops."
            }
        ],
        code_snippets=[
            {
                "title": "Textual Sequence Diagram of an Authentication Flow",
                "language": "text",
                "code": "User                 AuthController               AuthService               Database\n |                         |                           |                       |\n |--- login(u, p) -------->|                           |                       |\n |                         |--- verify(u, p) --------->|                       |\n |                         |                           |--- find_user(u) ----->|\n |                         |                           |<-- return user -------|\n |                         |                           |                       |\n |                         |                           |-- hash check (opt) -- |\n |                         |<-- token / error ---------|                       |\n |<-- 200 OK / 401 --------|                           |                       |\n |                         |                           |                       |",
                "explanation": "Chronological trace of method calls passing between four distinct architectural tiers."
            },
            {
                "title": "Python Implementation Corresponding to Sequence Diagram",
                "language": "python",
                "code": "class Database:\n    def find_user(self, username: str) -> dict:\n        return {'username': username, 'pw_hash': 'hash123'}\n\nclass AuthService:\n    def __init__(self, db: Database):\n        self.db = db\n    def verify(self, user: str, pw: str) -> str:\n        # Synchronous call down to database\n        record = self.db.find_user(user)\n        if record and pw == 'secret':\n            return 'JWT_TOKEN_ABC'\n        return 'AUTH_FAIL'\n\nclass AuthController:\n    def __init__(self, auth: AuthService):\n        self.auth = auth\n    def login(self, u: str, p: str) -> tuple:\n        token = self.auth.verify(u, p)\n        return (200, token) if token != 'AUTH_FAIL' else (401, 'Unauthorized')",
                "explanation": "Clean code structure directly executing the chronological sequence diagram steps."
            },
            {
                "title": "Simulating Synchronous vs Asynchronous Sequence Messages",
                "language": "python",
                "code": "import queue\n\n# Asynchronous message delivery: sender does not block waiting for return\nevent_queue = queue.Queue()\n\ndef send_async_event(event_name: str):\n    print(f'Sender: Enqueueing event \"{event_name}\" and proceeding immediately!')\n    event_queue.put(event_name)\n\nsend_async_event('ORDER_SUBMITTED')",
                "explanation": "Asynchronous sequence messages place payloads on queues without blocking sender execution."
            },
            {
                "title": "PlantUML Sequence Diagram Code",
                "language": "text",
                "code": "@startuml\nautonumber\nClient -> API: GET /products\nAPI -> Cache: check_cache()\nCache --> API: cache_miss\nAPI -> DB: SELECT * FROM products\nDB --> API: rows\nAPI --> Client: 200 OK [JSON]\n@enduml",
                "explanation": "Declarative sequence diagram syntax using PlantUML."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Implement Sequence Interaction Controller",
            description="Implement a 3-tier sequence flow: `Validator`, `PaymentService`, and `OrderController`. `OrderController.place_order(card, amt)` must first call `Validator.is_valid(card)`. If valid, it calls `PaymentService.charge(amt)` and returns `'SUCCESS'`. If invalid, it returns `'INVALID_CARD'` without calling the payment service.",
            starter_code="class Validator:\n    pass\nclass PaymentService:\n    pass\nclass OrderController:\n    pass",
            solution_code="class Validator:\n    def is_valid(self, card: str) -> bool:\n        return len(card) == 16\n\nclass PaymentService:\n    def charge(self, amt: float) -> str:\n        return f'Charged ${amt:.2f}'\n\nclass OrderController:\n    def __init__(self, val: Validator, pay: PaymentService):\n        self.val = val\n        self.pay = pay\n\n    def place_order(self, card: str, amt: float) -> str:\n        if not self.val.is_valid(card):\n            return 'INVALID_CARD'\n        self.pay.charge(amt)\n        return 'SUCCESS'",
            expected_output="SUCCESS\nINVALID_CARD"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What does the vertical dimension (from top to bottom) represent in a UML Sequence Diagram?",
                options=[
                    "The chronological passage of time",
                    "The byte size of the object in memory",
                    "The number of CPU registers",
                    "The lines of code in the file"
                ],
                correct_answer="The chronological passage of time",
                explanation="In sequence diagrams, time strictly flows downwards along the vertical lifelines."
            ),
            QuizQuestionBlueprint(
                question="What does a thin vertical rectangle placed on an object's lifeline indicate?",
                options=[
                    "An Activation Bar (indicating the object is actively executing a method)",
                    "A memory leak",
                    "A breakpoint in the debugger",
                    "A compiler warning"
                ],
                correct_answer="An Activation Bar (indicating the object is actively executing a method)",
                explanation="The activation bar represents the period of time during which an object is executing an operation."
            ),
            QuizQuestionBlueprint(
                question="How is a synchronous method call distinguished from a return message in a Sequence Diagram?",
                options=[
                    "A synchronous call is a solid line with a filled arrow; a return is a dashed line with an open arrow",
                    "A synchronous call is written in red; a return is written in blue",
                    "A synchronous call is a circle; a return is a square",
                    "There is no visual difference"
                ],
                correct_answer="A synchronous call is a solid line with a filled arrow; a return is a dashed line with an open arrow",
                explanation="Calls are solid directional arrows; return replies are dashed lines with open arrowheads."
            ),
            QuizQuestionBlueprint(
                question="In UML Sequence fragments, which keyword represents conditional `if / else` branching?",
                options=[
                    "alt (Alternative)",
                    "opt (Optional)",
                    "loop",
                    "break"
                ],
                correct_answer="alt (Alternative)",
                explanation="The `alt` fragment designates mutually exclusive alternative execution paths (if/else)."
            ),
            QuizQuestionBlueprint(
                question="What is the primary benefit of drawing a Sequence Diagram before writing multi-service code?",
                options=[
                    "It maps out the exact sequence of network requests, method calls, and responses across microservices to prevent architectural deadlocks and race conditions",
                    "It automatically creates a mobile app",
                    "It eliminates the need for unit testing",
                    "It makes Python run without a virtual environment"
                ],
                correct_answer="It maps out the exact sequence of network requests, method calls, and responses across microservices to prevent architectural deadlocks and race conditions",
                explanation="Sequence diagrams clarify cross-boundary timing, message payloads, and call orders across complex architectures."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 45: Single Responsibility Principle (SRP)
    # -------------------------------------------------------------
    DayBlueprint(
        order=45,
        title="Day 45: Single Responsibility Principle (SRP)",
        concept="SOLID Principles - The 'S': Single Responsibility Principle (SRP) - 'A class should have one, and only one, reason to change'",
        analogy="Think of a Swiss Army Knife with 45 blades: it has scissors, a fish scaler, a magnifying glass, a toothpick, and a corkscrew. It tries to do everything, so it does nothing well: the scissors are too dull to cut cardboard, the screwdriver is too awkward to turn, and if the main hinge bends, all 45 tools break simultaneously! A master chef uses a dedicated Japanese Chef's Knife for cutting, a dedicated cutting board, and a dedicated timer. Each tool has **One Single Responsibility**!",
        theory_sections=[
            {
                "heading": "What is the Single Responsibility Principle?",
                "body": "The **Single Responsibility Principle (SRP)**, formulated by Robert C. Martin (Uncle Bob), states:\n> *\"A class should have one, and only one, reason to change.\"*\n\nEvery class should be responsible for a single part of the software's functionality, and that responsibility should be entirely encapsulated by the class.\n\nA common anti-pattern is the **God Object (Monster Class)**: a class that manages database queries, calculates business profits, validates credit cards, and formats HTML emails all in one 2,000-line monster. If the database schema changes, the God Object changes. If the email template changes, the God Object changes. If tax rules change, the God Object changes. This creates massive fragility."
            },
            {
                "heading": "Identifying and Refactoring SRP Violations",
                "body": "Ask: *\"Who are the actors requesting changes to this class?\"*\n- If accountants ask for changes to tax logic, marketers ask for changes to email templates, and DBAs ask for changes to SQL schemas, all targeting the same class -> **SRP is violated**.\n\nRefactor by splitting into cohesive collaborators:\n1. `Order` (manages items and pricing).\n2. `OrderRepository` (saves/loads from database).\n3. `InvoiceFormatter` (renders receipts/HTML).\n4. `NotificationService` (sends emails/SMS)."
            }
        ],
        code_snippets=[
            {
                "title": "Violating SRP: The 'God Class' Anti-Pattern",
                "language": "python",
                "code": "# BAD: This class has THREE distinct reasons to change!\nclass BadUser:\n    def __init__(self, username: str, email: str):\n        self.username = username\n        self.email = email\n\n    # Reason 1: Business validation rules change\n    def validate_email(self) -> bool:\n        return '@' in self.email\n\n    # Reason 2: Database schema or SQL changes\n    def save_to_database(self):\n        print(f'SQL: INSERT INTO users VALUES (\"{self.username}\", \"{self.email}\")')\n\n    # Reason 3: Email template design changes\n    def send_welcome_email(self):\n        print(f'SMTP: Sending \"Welcome {self.username}!\" to {self.email}')",
                "explanation": "BadUser mixes domain state, database persistence, and network email formatting."
            },
            {
                "title": "Refactoring to SRP: Distinct Cohesive Classes",
                "language": "python",
                "code": "# 1. Domain Model: Only holds user identity and core domain invariants\nclass User:\n    def __init__(self, username: str, email: str):\n        self.username = username\n        self.email = email\n\n# 2. Persistence Layer: Only changes if database schema or driver changes\nclass UserRepository:\n    def save(self, user: User):\n        print(f'DATABASE: Saving {user.username} to PostgreSQL...')\n\n# 3. Notification Service: Only changes if communication channel changes\nclass EmailService:\n    def send_welcome(self, user: User):\n        print(f'EMAIL: Sending welcome email to {user.email}...')\n\nu = User('alice', 'alice@test.com')\nUserRepository().save(u)\nEmailService().send_welcome(u)",
                "explanation": "Each class has exactly one responsibility and one reason to change."
            },
            {
                "title": "Cohesive Collaborators in Business Workflows",
                "language": "python",
                "code": "class RegistrationWorkflow:\n    def __init__(self, repo: UserRepository, notifier: EmailService):\n        self.repo = repo\n        self.notifier = notifier\n\n    def register_new_user(self, username: str, email: str):\n        user = User(username, email)\n        self.repo.save(user)\n        self.notifier.send_welcome(user)\n        return user\n\nworkflow = RegistrationWorkflow(UserRepository(), EmailService())\nworkflow.register_new_user('bob', 'bob@test.com')",
                "explanation": "High-level workflow coordinates single-responsibility collaborators cleanly."
            },
            {
                "title": "Python Script: Unit Testing Single-Responsibility Classes",
                "language": "python",
                "code": "# SRP classes are trivial to test in complete isolation!\ndef test_user_creation():\n    u = User('test_user', 'test@test.com')\n    assert u.username == 'test_user'\n    print('User unit test passed in 0.001s without needing a real database!')\n\ntest_user_creation()",
                "explanation": "SRP enables blazing fast unit tests decoupled from external I/O."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Refactor Invoice God Class to SRP",
            description="Refactor a bad `Invoice` class that calculates totals AND prints receipts AND saves to disk. Split it into: `Invoice(items, amounts)` with `get_total()`, `InvoicePrinter` with `render_text(invoice)`, and `InvoiceStorage` with `save_to_file(invoice, filename)`.",
            starter_code="# Refactor Invoice God Class into 3 SRP classes\npass",
            solution_code="class Invoice:\n    def __init__(self, items: list, amounts: list):\n        self.items = items\n        self.amounts = amounts\n    def get_total(self) -> float:\n        return sum(self.amounts)\n\nclass InvoicePrinter:\n    def render_text(self, inv: Invoice) -> str:\n        return f'Total: ${inv.get_total():.2f}'\n\nclass InvoiceStorage:\n    def save_to_file(self, inv: Invoice, filename: str) -> str:\n        return f'Saved invoice (${inv.get_total():.2f}) to {filename}'",
            expected_output="Total: $120.00\nSaved invoice ($120.00) to invoice_101.txt"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the precise definition of the Single Responsibility Principle (SRP)?",
                options=[
                    "A class should have one, and only one, reason to change",
                    "A class should only contain a single line of code",
                    "A program should only have a single class",
                    "A method should take only one parameter"
                ],
                correct_answer="A class should have one, and only one, reason to change",
                explanation="Robert C. Martin defines SRP as: 'A class should have one, and only one, reason to change', meaning it serves one actor/purpose."
            ),
            QuizQuestionBlueprint(
                question="What is the 'God Object' anti-pattern?",
                options=[
                    "A monolithic class that knows too much and does too much, accumulating dozens of disparate responsibilities into a fragile blob",
                    "A class that cannot be deleted",
                    "A class that uses cloud storage",
                    "A class with 100% test coverage"
                ],
                correct_answer="A monolithic class that knows too much and does too much, accumulating dozens of disparate responsibilities into a fragile blob",
                explanation="A God Object centralizes too much responsibility, becoming brittle and hard to maintain."
            ),
            QuizQuestionBlueprint(
                question="If a class handles database SQL queries AND calculates payroll taxes AND formats HTML emails, how many responsibilities does it violate?",
                options=[
                    "At least 3 distinct responsibilities, and it should be split into 3 separate cohesive classes",
                    "Zero, this is optimal OOP design",
                    "Only 1 responsibility: running the company",
                    "None, as long as it has comments"
                ],
                correct_answer="At least 3 distinct responsibilities, and it should be split into 3 separate cohesive classes",
                explanation="Persistence, tax business logic, and UI email formatting are three completely separate reasons to change."
            ),
            QuizQuestionBlueprint(
                question="How does adhering to the Single Responsibility Principle improve automated unit testing?",
                options=[
                    "Classes with a single responsibility have minimal dependencies, making them fast and trivial to test in isolation without heavy mocks",
                    "It automatically generates test scripts without human writing",
                    "It prevents compiler syntax errors",
                    "It makes unit tests run on the GPU"
                ],
                correct_answer="Classes with a single responsibility have minimal dependencies, making them fast and trivial to test in isolation without heavy mocks",
                explanation="Small, focused classes can be tested rapidly in isolation without spinning up databases or network sockets."
            ),
            QuizQuestionBlueprint(
                question="What does the acronym 'SOLID' stand for in software engineering?",
                options=[
                    "Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion",
                    "Sequential Operation, Linked Inheritance, Dynamic Polymorphism, Iterative Design",
                    "Syntax, Output, Logic, Input, Data",
                    "Security, Organization, Logging, Identity, Debugging"
                ],
                correct_answer="Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion",
                explanation="SOLID stands for SRP, OCP, LSP, ISP, and DIP—the foundational five principles of Object-Oriented Design."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 46: Open/Closed Principle (OCP)
    # -------------------------------------------------------------
    DayBlueprint(
        order=46,
        title="Day 46: Open/Closed Principle (OCP)",
        concept="SOLID Principles - The 'O': Open/Closed Principle (OCP) - 'Software entities should be open for extension, but closed for modification'",
        analogy="Think of a modern smartphone: if you want your phone to play guitar chords or track your running pace, you do NOT take a soldering iron to the phone's motherboard to rewire the microchips! The phone is **Closed for modification**. Instead, you download an App from the App Store. The phone provides a plugin framework that is **Open for extension**. You add brand-new behavior without touching existing hardware or operating system code!",
        theory_sections=[
            {
                "heading": "What is the Open/Closed Principle?",
                "body": "The **Open/Closed Principle (OCP)**, originally formulated by Bertrand Meyer, states:\n> *\"Software entities (classes, modules, functions) should be open for extension, but closed for modification.\"*\n\n- **Open for Extension**: You should be able to introduce brand-new features, algorithms, or behaviors to the system effortlessly.\n- **Closed for Modification**: You should achieve this extension **without altering pre-existing, tested, and deployed source code**."
            },
            {
                "heading": "The Danger of Massive `if/elif/else` Ladders",
                "body": "The primary symptom of an OCP violation is a massive switch or `if/elif/else` ladder checking object types:\n```python\nif type == 'CREDIT_CARD': ...\nelif type == 'PAYPAL': ...\nelif type == 'BITCOIN': ...  # Every new payment type modifies this function!\n```\nEvery new option requires opening the file, editing the function, risking introducing regressions, and re-testing everything. OCP solves this by using **Polymorphism and Strategy Patterns**."
            }
        ],
        code_snippets=[
            {
                "title": "Violating OCP: Fragile if/else Type Ladder",
                "language": "python",
                "code": "# BAD: Adding a new shape forces editing calculate_total_area!\nclass BadAreaCalculator:\n    def calculate_total_area(self, shapes: list) -> float:\n        total = 0.0\n        for s in shapes:\n            if s['type'] == 'circle':\n                total += 3.14159 * (s['radius'] ** 2)\n            elif s['type'] == 'rectangle':\n                total += s['width'] * s['height']\n            # If we add Triangle, we MUST modify this function! (Violates OCP)\n        return total",
                "explanation": "Every new shape requires modifying the tested calculate_total_area function."
            },
            {
                "title": "Refactoring to OCP using Polymorphism",
                "language": "python",
                "code": "from abc import ABC, abstractmethod\n\n# 1. Closed for modification: Core interface\nclass Shape(ABC):\n    @abstractmethod\n    def area(self) -> float: pass\n\n# 2. Open for extension: Add any shape without touching AreaCalculator!\nclass Circle(Shape):\n    def __init__(self, r: float): self.r = r\n    def area(self) -> float: return 3.14159 * (self.r ** 2)\n\nclass Rectangle(Shape):\n    def __init__(self, w: float, h: float): self.w, self.h = w, h\n    def area(self) -> float: return self.w * self.h\n\n# 3. Consumer is 100% closed: never needs to be edited again!\nclass AreaCalculator:\n    def calculate_total_area(self, shapes: list) -> float:\n        return sum(s.area() for s in shapes)",
                "explanation": "AreaCalculator never changes, but supports infinite new shapes."
            },
            {
                "title": "Extending the System with Zero Modifications to Existing Classes",
                "language": "python",
                "code": "# We can create a brand new Triangle in a separate file:\nclass Triangle(Shape):\n    def __init__(self, base: float, height: float):\n        self.base, self.height = base, height\n    def area(self) -> float: return 0.5 * self.base * self.height\n\n# Works immediately with existing AreaCalculator!\ncalc = AreaCalculator()\nprint('Total Area:', calc.calculate_total_area([Circle(10), Rectangle(5, 4), Triangle(6, 8)]))",
                "explanation": "Adding Triangle required zero changes to existing tested code."
            },
            {
                "title": "OCP with Strategy Function Decorators",
                "language": "python",
                "code": "DISCOUNT_STRATEGIES = {}\n\ndef register_discount(code):\n    def decorator(fn):\n        DISCOUNT_STRATEGIES[code] = fn\n        return fn\n    return decorator\n\n@register_discount('VIP')\ndef vip_discount(amt): return amt * 0.8\n\n@register_discount('SUMMER')\ndef summer_discount(amt): return amt * 0.9\n\nprint('VIP Discount on $100:', DISCOUNT_STRATEGIES['VIP'](100))",
                "explanation": "Plugin registries allow new discount strategies to be registered without touching existing code."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="OCP Discount Strategy Engine",
            description="Create an abstract class `DiscountStrategy(ABC)` with abstract method `apply(amount: float) -> float`. Implement `FlatDiscount(discount_amount)` and `PercentageDiscount(percent)`. Create an `Order(amount, strategy: DiscountStrategy)` that has a method `get_final_price()` returning the discounted price.",
            starter_code="from abc import ABC, abstractmethod\nclass DiscountStrategy(ABC):\n    pass\nclass FlatDiscount(DiscountStrategy):\n    pass\nclass PercentageDiscount(DiscountStrategy):\n    pass\nclass Order:\n    pass",
            solution_code="from abc import ABC, abstractmethod\n\nclass DiscountStrategy(ABC):\n    @abstractmethod\n    def apply(self, amount: float) -> float: pass\n\nclass FlatDiscount(DiscountStrategy):\n    def __init__(self, discount: float): self.discount = float(discount)\n    def apply(self, amount: float) -> float: return max(0.0, amount - self.discount)\n\nclass PercentageDiscount(DiscountStrategy):\n    def __init__(self, percent: float): self.percent = float(percent)\n    def apply(self, amount: float) -> float: return amount * (1.0 - (self.percent / 100.0))\n\nclass Order:\n    def __init__(self, amount: float, strategy: DiscountStrategy):\n        self.amount = float(amount)\n        self.strategy = strategy\n    def get_final_price(self) -> float: return self.strategy.apply(self.amount)",
            expected_output="Final Price (Flat): 80.0\nFinal Price (10%): 90.0"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the core rule of the Open/Closed Principle (OCP)?",
                options=[
                    "Software entities should be open for extension, but closed for modification",
                    "Classes should be open for anyone to edit, but closed on weekends",
                    "Files must be opened with `open()` and closed with `close()`",
                    "Functions can only accept open-source libraries"
                ],
                correct_answer="Software entities should be open for extension, but closed for modification",
                explanation="OCP mandates designing code so new behaviors can be added without modifying existing source code."
            ),
            QuizQuestionBlueprint(
                question="What programming construct is a major indicator of an Open/Closed Principle violation?",
                options=[
                    "Large `if/elif/else` or `switch` statements checking explicit type names to decide what algorithm to run",
                    "A class with two private variables",
                    "A function returning a boolean",
                    "A while loop"
                ],
                correct_answer="Large `if/elif/else` or `switch` statements checking explicit type names to decide what algorithm to run",
                explanation="Hardcoded type switches violate OCP because every new type forces modifying the switch statement."
            ),
            QuizQuestionBlueprint(
                question="What primary OOP technique enables code to satisfy the Open/Closed Principle?",
                options=[
                    "Polymorphism and Abstraction: writing consumers against abstract interfaces and extending via concrete subclasses",
                    "Global variable mutation",
                    "Writing 10,000 lines of procedural script in one file",
                    "Encrypting the source files"
                ],
                correct_answer="Polymorphism and Abstraction: writing consumers against abstract interfaces and extending via concrete subclasses",
                explanation="Polymorphic interfaces allow adding new concrete implementations without altering existing consumer code."
            ),
            QuizQuestionBlueprint(
                question="Why is modifying existing, battle-tested production code risky compared to extending it via new classes?",
                options=[
                    "Modifying working code risks introducing accidental regressions and breaking existing customer workflows",
                    "It causes the computer hard drive to overheat",
                    "Because Git prohibits modifying existing files",
                    "It deletes the commit history"
                ],
                correct_answer="Modifying working code risks introducing accidental regressions and breaking existing customer workflows",
                explanation="Editing tested code introduces regression risks and demands extensive re-testing across all consumers."
            ),
            QuizQuestionBlueprint(
                question="Which real-world hardware design perfectly illustrates the Open/Closed Principle?",
                options=[
                    "A computer USB port: the motherboard USB port is closed for modification, but open for extension by plugging in keyboards, mice, or cameras",
                    "A solid block of concrete with wires permanently encased inside",
                    "A wooden door with no handle or keyhole",
                    "A disposable plastic straw"
                ],
                correct_answer="A computer USB port: the motherboard USB port is closed for modification, but open for extension by plugging in keyboards, mice, or cameras",
                explanation="A USB port provides a fixed, closed hardware interface that supports unlimited external device extensions."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 47: Liskov Substitution Principle (LSP)
    # -------------------------------------------------------------
    DayBlueprint(
        order=47,
        title="Day 47: Liskov Substitution Principle (LSP)",
        concept="SOLID Principles - The 'L': Liskov Substitution Principle (LSP) - 'Subtypes must be substitutable for their base types without altering program correctness'",
        analogy="Imagine you rent a car and drive off the lot. If you press the foot brake, the car stops. If you rent a different car (say an electric sedan), you expect that pressing the foot brake also stops the car! What if an electric car manufacturer designed their brake pedal to honk the horn and accelerate instead? You would crash! The **Liskov Substitution Principle** guarantees that any subclass can be substituted in place of its parent class without breaking user expectations or causing crashes!",
        theory_sections=[
            {
                "heading": "What is the Liskov Substitution Principle?",
                "body": "The **Liskov Substitution Principle (LSP)**, formulated by Turing Award winner Barbara Liskov in 1987, states:\n> *\"If $S$ is a subtype of $T$, then objects of type $T$ may be replaced with objects of type $S$ without altering any of the desirable properties of the program (correctness, task performed, etc.).\"*\n\nIn plain English: **A subclass must honor the contract of its base class.** It must not:\n1. Violate base class invariants.\n2. Strengthen preconditions (demand more strict inputs than the parent).\n3. Weaken postconditions (deliver less than the parent promised).\n4. Throw unexpected exceptions that the base class never declared."
            },
            {
                "heading": "The Classic Square-Rectangle Anti-Pattern",
                "body": "In elementary mathematics, a Square is a Rectangle with equal sides. However, in OOP, modeling `Square` as a subclass of `Rectangle` catastrophically violates LSP:\n- In `Rectangle`, changing `width` leaves `height` untouched.\n- In `Square`, changing `width` mutates `height` to keep sides equal.\n- Any function expecting a generic `Rectangle` and testing `rect.set_width(5); rect.set_height(4); assert rect.area() == 20` will **fail** when given a `Square`! Therefore, mathematically a Square is a rectangle, but behaviorally in OOP, it is not."
            }
        ],
        code_snippets=[
            {
                "title": "Violating LSP: The Infamous Square-Rectangle Dilemma",
                "language": "python",
                "code": "class Rectangle:\n    def __init__(self, width: float, height: float):\n        self._width = width\n        self._height = height\n    def set_width(self, w: float): self._width = w\n    def set_height(self, h: float): self._height = h\n    def area(self) -> float: return self._width * self._height\n\n# Bad Subclass: Square violates Rectangle's behavioral invariants!\nclass Square(Rectangle):\n    def set_width(self, w: float):\n        self._width = self._height = w  # Mutating height violates caller expectations!\n    def set_height(self, h: float):\n        self._width = self._height = h\n\ndef client_code(rect: Rectangle):\n    rect.set_width(5)\n    rect.set_height(4)\n    # Caller expects 5 * 4 = 20\n    assert rect.area() == 20, f'LSP VIOLATED! Got area {rect.area()}'\n\ntry:\n    client_code(Square(0, 0))\nexcept AssertionError as err:\n    print(err)",
                "explanation": "Square cannot be substituted for Rectangle without breaking client assertions."
            },
            {
                "title": "Refactoring to LSP Compliance via Common Shape Interface",
                "language": "python",
                "code": "from abc import ABC, abstractmethod\n\nclass Shape(ABC):\n    @abstractmethod\n    def area(self) -> float: pass\n\nclass Rectangle(Shape):\n    def __init__(self, w: float, h: float): self.w, self.h = w, h\n    def area(self) -> float: return self.w * self.h\n\nclass Square(Shape):\n    def __init__(self, side: float): self.side = side\n    def area(self) -> float: return self.side ** 2\n\n# Subtypes are 100% substitutable for Shape!\ndef print_area(s: Shape):\n    print('Area:', s.area())\n\nprint_area(Rectangle(5, 4))\nprint_area(Square(5))",
                "explanation": "Separating Square and Rectangle into peer subtypes of Shape restores LSP."
            },
            {
                "title": "Another Common Violation: Subclasses Throwing Unexpected Exceptions",
                "language": "python",
                "code": "# Bad: Ostrich inherits from Bird, but breaks fly() contract by throwing error!\nclass Bird:\n    def fly(self): return 'Flying high!'\n\nclass Ostrich(Bird):\n    def fly(self): raise NotImplementedError('Ostriches cannot fly!')\n\n# Solution: Extract FlyingBird(Bird) or use a Flyable Interface (ISP)!",
                "explanation": "Subclasses must not throw unexpected exceptions that base class callers cannot handle."
            },
            {
                "title": "Python Script: Verifying Substitutability across Subtypes",
                "language": "python",
                "code": "shapes: list[Shape] = [Rectangle(10, 2), Square(4)]\nprint('Total area of substitutable shapes:', sum(s.area() for s in shapes))",
                "explanation": "Demonstrates seamless polymorphic substitution conforming to LSP."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Fix LSP Violation in Banking System",
            description="Fix an LSP violation where `ReadOnlyAccount` inherits `Account` and raises an exception on `deposit()`. Refactor by creating a base `AccountView` with `get_balance()` and a writable subclass `StandardAccount(AccountView)` with `deposit(amount)`. Demonstrate safe substitution with a function `read_balance(acc: AccountView)`.",
            starter_code="# Refactor Account hierarchy to obey LSP\npass",
            solution_code="class AccountView:\n    def __init__(self, balance: float):\n        self._balance = float(balance)\n    def get_balance(self) -> float: return self._balance\n\nclass StandardAccount(AccountView):\n    def deposit(self, amount: float):\n        if amount > 0: self._balance += amount\n\ndef read_balance(acc: AccountView) -> float:\n    return acc.get_balance()",
            expected_output="Account balance: 150.0"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the core principle behind the Liskov Substitution Principle (LSP)?",
                options=[
                    "Subclasses must be substitutable for their base classes without altering the correctness or behavior of the program",
                    "All classes must be named after Barbara Liskov",
                    "Subclasses must always execute faster than parent classes",
                    "Classes cannot inherit from more than one parent"
                ],
                correct_answer="Subclasses must be substitutable for their base classes without altering the correctness or behavior of the program",
                explanation="LSP mandates that derived classes must honor base class contracts so callers can use them interchangeably without regressions."
            ),
            QuizQuestionBlueprint(
                question="Why is modeling `Square` as a subclass of `Rectangle` considered a classic violation of LSP in OOP?",
                options=[
                    "Because Rectangle allows width and height to change independently; forcing equal sides in Square mutates the other dimension, breaking caller expectations",
                    "Because squares are mathematically round",
                    "Because Python does not allow 4-sided shapes",
                    "Because Square has more bytes than Rectangle"
                ],
                correct_answer="Because Rectangle allows width and height to change independently; forcing equal sides in Square mutates the other dimension, breaking caller expectations",
                explanation="Callers using a Rectangle reference expect independent width and height mutations; Square breaks that invariant."
            ),
            QuizQuestionBlueprint(
                question="What happens when an `Ostrich` subclass inherits from `Bird` and raises an exception in `fly()`?",
                options=[
                    "It violates LSP because callers expecting a generic Bird will crash when calling `bird.fly()`",
                    "It automatically converts the ostrich into an airplane",
                    "It is fine, Python recommends raising errors in subclasses",
                    "It disables the compiler"
                ],
                correct_answer="It violates LSP because callers expecting a generic Bird will crash when calling `bird.fly()`",
                explanation="Throwing unexpected errors where the base class contract promises valid execution violates LSP."
            ),
            QuizQuestionBlueprint(
                question="In terms of preconditions and postconditions, what does LSP dictate for derived subclasses?",
                options=[
                    "Subclasses cannot strengthen preconditions (demand stricter inputs) and cannot weaken postconditions (deliver less output)",
                    "Subclasses must delete all preconditions",
                    "Subclasses must reverse the order of postconditions",
                    "Preconditions must be written in uppercase"
                ],
                correct_answer="Subclasses cannot strengthen preconditions (demand stricter inputs) and cannot weaken postconditions (deliver less output)",
                explanation="LSP requires subclasses to accept at least what the parent accepts (contravariance) and return at least what the parent promises (covariance)."
            ),
            QuizQuestionBlueprint(
                question="Who was the computer scientist who formulated the Liskov Substitution Principle?",
                options=[
                    "Barbara Liskov (Turing Award Laureate)",
                    "Alan Turing",
                    "Grace Hopper",
                    "Ada Lovelace"
                ],
                correct_answer="Barbara Liskov (Turing Award Laureate)",
                explanation="Barbara Liskov introduced this behavioral subtyping principle in her 1987 keynote speech."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 48: Interface Segregation Principle (ISP)
    # -------------------------------------------------------------
    DayBlueprint(
        order=48,
        title="Day 48: Interface Segregation Principle (ISP)",
        concept="SOLID Principles - The 'I': Interface Segregation Principle (ISP) - 'Clients should not be forced to depend on interfaces they do not use'",
        analogy="Imagine an all-in-one restaurant drive-thru ordering microphone that forces every single customer to order a Giant Family Value Feast: 4 burgers, 3 milkshakes, 2 orders of chicken nuggets, and an apple pie. If all you wanted was a small coffee, you are still forced to pay for and carry the entire 15-pound feast! The **Interface Segregation Principle** says: do not create fat, bloated, all-in-one interfaces. Break them up into small, specialized menus (Coffee Menu, Burger Menu, Dessert Menu) so clients only order what they actually need!",
        theory_sections=[
            {
                "heading": "What is the Interface Segregation Principle?",
                "body": "The **Interface Segregation Principle (ISP)** states:\n> *\"Clients should not be forced to depend upon interfaces that they do not use.\"*\n\nInstead of creating one 'Fat / Bloated Interface' that declares 25 methods for every possible use case, create many small, cohesive, role-specific interfaces (`Printable`, `Scannable`, `Faxable`).\n\nWhen an interface is bloated, implementing classes are forced to write dummy placeholder methods (`raise NotImplementedError` or `pass`) for methods they don't support, introducing dead code and coupling."
            },
            {
                "heading": "Smells and Symptoms of ISP Violations",
                "body": "- Classes contain methods that raise `NotImplementedError` or return `None` because they don't support the feature.\n- A change to a method required by Client A forces recompilation or retesting of Client B, even though Client B never calls that method.\n- Interfaces containing 'and' in their responsibilities (`IPrinterAndScannerAndFax`)."
            }
        ],
        code_snippets=[
            {
                "title": "Violating ISP: The Bloated Multi-Function Interface",
                "language": "python",
                "code": "from abc import ABC, abstractmethod\n\n# BAD: Fat bloated interface forcing all devices to support printing, scanning, and faxing\nclass MultiFunctionDevice(ABC):\n    @abstractmethod\n    def print_doc(self, doc: str): pass\n    @abstractmethod\n    def scan_doc(self) -> str: pass\n    @abstractmethod\n    def fax_doc(self, doc: str): pass\n\n# A cheap budget printer only knows how to print, but is forced to implement scan and fax!\nclass CheapPrinter(MultiFunctionDevice):\n    def print_doc(self, doc: str): print(f'Printing: {doc}')\n    def scan_doc(self) -> str: raise NotImplementedError('No scanner hardware!')\n    def fax_doc(self, doc: str): raise NotImplementedError('No telephone fax modem!')",
                "explanation": "CheapPrinter is polluted with dummy methods raising errors."
            },
            {
                "title": "Refactoring to ISP: Small, Role-Specific Interfaces",
                "language": "python",
                "code": "# GOOD: Segregated, focused role interfaces\nclass Printer(ABC):\n    @abstractmethod\n    def print_doc(self, doc: str): pass\n\nclass Scanner(ABC):\n    @abstractmethod\n    def scan_doc(self) -> str: pass\n\nclass Fax(ABC):\n    @abstractmethod\n    def fax_doc(self, doc: str): pass\n\n# 1. Simple device implements ONLY what it actually supports!\nclass SimplePrinter(Printer):\n    def print_doc(self, doc: str): print(f'Simple printing: {doc}')\n\n# 2. Enterprise machine combines multiple interfaces cleanly!\nclass OfficeAllInOne(Printer, Scanner, Fax):\n    def print_doc(self, doc: str): print(f'Office printing: {doc}')\n    def scan_doc(self) -> str: return 'Office scanned document'\n    def fax_doc(self, doc: str): print(f'Faxing {doc} over telecom')",
                "explanation": "Classes implement only the specific interfaces they genuinely support."
            },
            {
                "title": "Consumer Functions Depend Only on Segregated Needs",
                "language": "python",
                "code": "# Consumer strictly requires a Printer, nothing more\ndef print_quarterly_report(printer: Printer, report: str):\n    printer.print_doc(report)\n\nprint_quarterly_report(SimplePrinter(), 'Q3 Financials')\nprint_quarterly_report(OfficeAllInOne(), 'Q3 Financials')",
                "explanation": "Client functions depend exclusively on narrow, tailored interfaces."
            },
            {
                "title": "Python Script: Inspecting Protocol Segregation",
                "language": "python",
                "code": "print('SimplePrinter interfaces:', [b.__name__ for b in SimplePrinter.__bases__])\nprint('OfficeAllInOne interfaces:', [b.__name__ for b in OfficeAllInOne.__bases__])",
                "explanation": "Reveals clean modular interface composition without dead methods."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Segregate Worker Interfaces",
            description="Refactor a bloated `Worker(ABC)` interface (`work()`, `eat()`, `sleep()`) to obey ISP. Break it into `Workable(ABC)` with `work()` and `Eatable(ABC)` with `eat()`. Create a `HumanWorker` implementing both, and a `RobotWorker` implementing only `Workable`.",
            starter_code="# Implement Workable, Eatable, HumanWorker, and RobotWorker\npass",
            solution_code="from abc import ABC, abstractmethod\n\nclass Workable(ABC):\n    @abstractmethod\n    def work(self) -> str: pass\n\nclass Eatable(ABC):\n    @abstractmethod\n    def eat(self) -> str: pass\n\nclass HumanWorker(Workable, Eatable):\n    def work(self) -> str: return 'Human working'\n    def eat(self) -> str: return 'Human eating lunch'\n\nclass RobotWorker(Workable):\n    def work(self) -> str: return 'Robot working 24/7'",
            expected_output="Human working\nHuman eating lunch\nRobot working 24/7"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the core directive of the Interface Segregation Principle (ISP)?",
                options=[
                    "Clients should not be forced to depend on interfaces they do not use",
                    "All interfaces must have at least 20 methods",
                    "Interfaces can only be implemented by classes in the same file",
                    "Interfaces should be deleted after compiling"
                ],
                correct_answer="Clients should not be forced to depend on interfaces they do not use",
                explanation="ISP dictates breaking fat interfaces into small, cohesive contracts so clients only implement what they need."
            ),
            QuizQuestionBlueprint(
                question="What is a major code smell indicating an Interface Segregation Principle violation?",
                options=[
                    "Classes implementing an interface with dummy stubs that raise `NotImplementedError` or return `None`",
                    "A class having more than two comments",
                    "A method returning an integer",
                    "A class whose name starts with 'User'"
                ],
                correct_answer="Classes implementing an interface with dummy stubs that raise `NotImplementedError` or return `None`",
                explanation="Throwing `NotImplementedError` or leaving empty stubs is a classic sign that an interface forced unneeded methods onto a class."
            ),
            QuizQuestionBlueprint(
                question="What is a 'Fat Interface'?",
                options=[
                    "An interface that attempts to do too many unrelated things, forcing implementers to accept methods they don't care about",
                    "An interface with high memory byte size",
                    "An interface written in C++",
                    "An interface that contains image files"
                ],
                correct_answer="An interface that attempts to do too many unrelated things, forcing implementers to accept methods they don't care about",
                explanation="Fat interfaces bundle disparate responsibilities together, violating cohesion and coupling implementers to unused code."
            ),
            QuizQuestionBlueprint(
                question="How does Interface Segregation relate to the Single Responsibility Principle (SRP)?",
                options=[
                    "ISP is essentially SRP applied to interfaces: interfaces should have small, cohesive, single responsibilities",
                    "ISP directly contradicts SRP",
                    "They are for two different programming languages",
                    "There is no relationship"
                ],
                correct_answer="ISP is essentially SRP applied to interfaces: interfaces should have small, cohesive, single responsibilities",
                explanation="ISP applies the concept of single responsibility to interfaces, keeping contracts minimal and focused."
            ),
            QuizQuestionBlueprint(
                question="How does Python's support for multiple inheritance and multiple Protocols support ISP?",
                options=[
                    "Classes can implement multiple fine-grained Protocols (e.g. `Printable`, `Closeable`, `Serializable`) cleanly without bloat",
                    "It automatically deletes unused code at runtime",
                    "It makes Python compile in parallel",
                    "It converts protocols into assembly code"
                ],
                correct_answer="Classes can implement multiple fine-grained Protocols (e.g. `Printable`, `Closeable`, `Serializable`) cleanly without bloat",
                explanation="Multiple interface/protocol conformance lets classes cherry-pick the exact capabilities they support."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 49: Dependency Inversion Principle (DIP)
    # -------------------------------------------------------------
    DayBlueprint(
        order=49,
        title="Day 49: Dependency Inversion Principle (DIP)",
        concept="SOLID Principles - The 'D': Dependency Inversion Principle (DIP) - 'High-level modules should not depend on low-level modules; both should depend on abstractions'",
        analogy="Think of plugging a lamp into a standard electrical wall outlet: your expensive lamp (**High-Level Module**) does NOT solder its wires directly to the regional coal power plant's copper turbine generator (**Low-Level Module**)! If the power company switches from coal to solar panels or nuclear energy, your lamp still plugs in without a scratch. Both the lamp and the power company depend on a standardized wall socket (**The Abstraction**)!",
        theory_sections=[
            {
                "heading": "What is the Dependency Inversion Principle?",
                "body": "The **Dependency Inversion Principle (DIP)** states two crucial rules:\n1. **High-level modules should not depend on low-level modules. Both should depend on abstractions.**\n2. **Abstractions should not depend on details. Details should depend on abstractions.**\n\n- **High-level modules**: Contain policy and core business logic (e.g., `OrderProcessor`, `UserAuthenticator`).\n- **Low-level modules**: Contain plumbing and technical implementation details (e.g., `MySQLDriver`, `SMTPSender`, `FileLogger`).\n\nTraditional design points dependencies downwards (High -> Low). DIP **inverts** the dependency so both layers point toward a shared abstract contract."
            },
            {
                "heading": "DIP vs Dependency Injection (DI) vs Inversion of Control (IoC)",
                "body": "- **DIP (Principle)**: The high-level architectural goal (depend on interfaces, not concretions).\n- **DI (Pattern)**: The tactical mechanism used to fulfill DIP (passing helper objects in via constructors).\n- **IoC (Framework)**: The container or framework that automates DI (e.g. Spring, Angular, FastAPI dependency injection)."
            }
        ],
        code_snippets=[
            {
                "title": "Violating DIP: High-Level Class Bound to Low-Level Concrete Database",
                "language": "python",
                "code": "# Low-level module\nclass MySQLDatabase:\n    def execute_sql(self, sql: str):\n        return f'MySQL executed: {sql}'\n\n# High-level business logic VIOLATING DIP:\nclass UserManagerBad:\n    def __init__(self):\n        # Direct tight dependency on concrete MySQLDatabase!\n        self.db = MySQLDatabase()\n\n    def register_user(self, username: str):\n        # Tied to MySQLDatabase syntax; cannot be tested without MySQL!\n        return self.db.execute_sql(f'INSERT INTO users VALUES (\"{username}\")')",
                "explanation": "UserManager is tightly coupled to MySQL; swapping to MongoDB or a mock requires editing UserManager."
            },
            {
                "title": "Refactoring to DIP Compliance: Depend on Abstractions",
                "language": "python",
                "code": "from abc import ABC, abstractmethod\n\n# 1. The Abstraction that both high-level and low-level modules depend upon\nclass DatabaseInterface(ABC):\n    @abstractmethod\n    def save(self, table: str, data: dict) -> bool: pass\n\n# 2. Low-level concrete implementations depend on the abstraction\nclass MySQLDatabase(DatabaseInterface):\n    def save(self, table: str, data: dict) -> bool:\n        print(f'MySQL: Stored {data} into table [{table}]')\n        return True\n\nclass MongoDatabase(DatabaseInterface):\n    def save(self, table: str, data: dict) -> bool:\n        print(f'MongoDB: Inserted document {data} into collection [{table}]')\n        return True\n\n# 3. High-level business logic depends ONLY on the abstraction!\nclass UserManagerGood:\n    def __init__(self, db: DatabaseInterface):\n        # Injected dependency\n        self.db = db\n\n    def register_user(self, username: str):\n        return self.db.save('users', {'username': username})",
                "explanation": "UserManager depends on DatabaseInterface; concrete databases can be swapped effortlessly."
            },
            {
                "title": "Effortless Unit Testing with Mock Injections",
                "language": "python",
                "code": "class MockDatabase(DatabaseInterface):\n    def __init__(self): self.saved = []\n    def save(self, table: str, data: dict) -> bool:\n        self.saved.append((table, data))\n        return True\n\n# Test runs in milliseconds in memory with no database server running!\nmock = MockDatabase()\nmanager = UserManagerGood(mock)\nmanager.register_user('alice')\nprint('Test verified saved record:', mock.saved)",
                "explanation": "Dependency Inversion enables instant, isolated in-memory unit testing."
            },
            {
                "title": "Dependency Inversion Architecture Flowchart",
                "language": "text",
                "code": "Traditional (Tight Coupling):\n  [ High-Level Module ] --------> [ Low-Level Module (MySQL) ]\n\nInverted (DIP):\n  [ High-Level Module ] --------> [ Database Abstraction ] <-------- [ Low-Level Module ]",
                "explanation": "Visualizes how both layers point toward the central abstraction."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="DIP Notification Dispatcher",
            description="Create an abstract class `MessageSender(ABC)` with abstract method `send(msg: str) -> str`. Implement `SMSMessageSender` and `EmailMessageSender`. Create `AlertManager(sender: MessageSender)` that implements `alert(msg)` calling `self.sender.send(msg)`.",
            starter_code="from abc import ABC, abstractmethod\nclass MessageSender(ABC):\n    pass\nclass AlertManager:\n    pass",
            solution_code="from abc import ABC, abstractmethod\n\nclass MessageSender(ABC):\n    @abstractmethod\n    def send(self, msg: str) -> str: pass\n\nclass SMSMessageSender(MessageSender):\n    def send(self, msg: str) -> str: return f'SMS: {msg}'\n\nclass EmailMessageSender(MessageSender):\n    def send(self, msg: str) -> str: return f'Email: {msg}'\n\nclass AlertManager:\n    def __init__(self, sender: MessageSender):\n        self.sender = sender\n    def alert(self, msg: str) -> str:\n        return self.sender.send(msg)",
            expected_output="SMS: High CPU\nEmail: High CPU"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the central rule of the Dependency Inversion Principle (DIP)?",
                options=[
                    "High-level modules should not depend on low-level modules; both should depend on abstractions",
                    "Subclasses should inherit from low-level modules first",
                    "Functions should be written upside down",
                    "Variables should be assigned in reverse order"
                ],
                correct_answer="High-level modules should not depend on low-level modules; both should depend on abstractions",
                explanation="DIP breaks tight coupling by ensuring high-level policy code and low-level detail code both depend on interfaces."
            ),
            QuizQuestionBlueprint(
                question="What is the difference between a 'High-Level Module' and a 'Low-Level Module'?",
                options=[
                    "High-level modules encapsulate core business logic and policies; low-level modules handle mechanical plumbing (databases, networks, disk I/O)",
                    "High-level modules are written in Python; low-level modules are written in HTML",
                    "High-level modules are stored at the top of the file",
                    "There is no difference"
                ],
                correct_answer="High-level modules encapsulate core business logic and policies; low-level modules handle mechanical plumbing (databases, networks, disk I/O)",
                explanation="High-level modules dictate business rules, while low-level modules handle technical I/O implementation."
            ),
            QuizQuestionBlueprint(
                question="What practical design pattern is commonly used to implement the Dependency Inversion Principle in code?",
                options=[
                    "Constructor Dependency Injection (passing interface implementations into `__init__`)",
                    "Global state mutation",
                    "Hardcoded class instantiation",
                    "Copy-paste programming"
                ],
                correct_answer="Constructor Dependency Injection (passing interface implementations into `__init__`)",
                explanation="Injecting dependencies via constructor parameters satisfies DIP by passing abstractions in from the outside."
            ),
            QuizQuestionBlueprint(
                question="Why does Dependency Inversion make software vastly easier to unit test?",
                options=[
                    "Because high-level business logic can be tested using fast, lightweight mock objects instead of spinning up live external databases or servers",
                    "Because it deletes all bugs automatically",
                    "Because it forces unit tests to pass without checking assertions",
                    "Because it compiles tests to machine code"
                ],
                correct_answer="Because high-level business logic can be tested using fast, lightweight mock objects instead of spinning up live external databases or servers",
                explanation="Depending on abstractions allows injecting test doubles (mocks) without touching external network or database infrastructure."
            ),
            QuizQuestionBlueprint(
                question="In DIP, what does the second clause ('Abstractions should not depend on details. Details should depend on abstractions') mean?",
                options=[
                    "Interfaces should be defined by business needs without containing vendor-specific parameters (e.g. no `sql_query` inside a generic Storage interface)",
                    "Interfaces must be private",
                    "Details should be printed to console",
                    "Abstractions must be written in C"
                ],
                correct_answer="Interfaces should be defined by business needs without containing vendor-specific parameters (e.g. no `sql_query` inside a generic Storage interface)",
                explanation="Interfaces should reflect domain needs rather than being biased by the low-level implementation details of a specific vendor."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 50 (Project): Refactoring Bad Code using SOLID, DRY, and KISS
    # -------------------------------------------------------------
    DayBlueprint(
        order=50,
        title="Day 50 (Project): Refactoring Bad Code using SOLID, DRY, and KISS",
        concept="Hands-on Project Day: Identifying design smells, breaking down God Objects, applying DRY (Don't Repeat Yourself) and KISS (Keep It Simple, Stupid), and refactoring legacy code into elegant SOLID architecture",
        analogy="Imagine an old hoarder's attic crammed with 40 years of tangled wires, broken furniture, open paint cans, and old newspapers. If you try to find a flashlight, everything collapses on your head. **Refactoring** is cleaning out the attic: sorting items into labeled boxes, recycling the junk, organizing tools onto pegboards, and ensuring every single item has a clear, accessible home. The room still holds all your gear, but now finding and using anything is effortless!",
        is_project_day=True,
        project_name="Refactoring Bad Code using SOLID, DRY, and KISS",
        theory_sections=[
            {
                "heading": "Core Engineering Maxims: DRY and KISS",
                "body": "Before diving into architectural patterns, great engineers live by two foundational rules:\n1. **DRY (Don't Repeat Yourself)**: Every piece of knowledge or logic must have a single, unambiguous representation in a system. Duplicate copy-pasted code means bug fixes must be manually applied in 5 places.\n2. **KISS (Keep It Simple, Stupid)**: Systems work best if they are kept simple rather than made complicated. Avoid over-engineering; don't build a distributed microservice cluster when a simple 20-line class solves the problem."
            },
            {
                "heading": "The Refactoring Recipe",
                "body": "When refactoring legacy code:\n1. Write automated characterization tests first to guarantee safety.\n2. Identify SRP violations (separate persistence from business logic from formatting).\n3. Replace hardcoded `if/else` ladders with OCP polymorphic strategies.\n4. Ensure derived classes obey LSP.\n5. Segregate fat interfaces (ISP).\n6. Inject dependencies via constructors (DIP)."
            }
        ],
        code_snippets=[
            {
                "title": "The Legacy 'Bad Code' Smelly Monolith",
                "language": "python",
                "code": "# SMELLY MONOLITH: Violates SRP, OCP, DIP, and DRY!\nclass LegacyOrderSystem:\n    def process(self, order_type, items, card_num, email):\n        # 1. Duplicate price math (Violates DRY)\n        subtotal = sum(i['price'] for i in items)\n        # 2. Hardcoded type switch (Violates OCP)\n        if order_type == 'STANDARD': tax = subtotal * 0.10\n        elif order_type == 'EXPRESS': tax = subtotal * 0.15\n        else: tax = 0.0\n        total = subtotal + tax\n        # 3. Direct hardcoded card processing (Violates DIP)\n        print(f'CHARGING CARD {card_num}: ${total}')\n        # 4. Mixed email formatting (Violates SRP)\n        print(f'SENDING EMAIL to {email}: Your order of ${total} is processed!')",
                "explanation": "A fragile legacy class combining business rules, taxes, payment, and notifications."
            },
            {
                "title": "Refactored Clean SOLID Architecture: Domain and Tax Strategies",
                "language": "python",
                "code": "from abc import ABC, abstractmethod\n\n# 1. Clean Domain Model (SRP)\nclass OrderItem:\n    def __init__(self, name: str, price: float):\n        self.name = name\n        self.price = float(price)\n\n# 2. OCP: Tax Calculation Strategy\nclass TaxStrategy(ABC):\n    @abstractmethod\n    def calculate_tax(self, subtotal: float) -> float: pass\n\nclass StandardTax(TaxStrategy):\n    def calculate_tax(self, subtotal: float) -> float: return subtotal * 0.10\n\nclass ExpressTax(TaxStrategy):\n    def calculate_tax(self, subtotal: float) -> float: return subtotal * 0.15",
                "explanation": "Separates domain items from pluggable OCP tax calculation strategies."
            },
            {
                "title": "Refactored Payment and Notification Abstractions (DIP & ISP)",
                "language": "python",
                "code": "class PaymentService(ABC):\n    @abstractmethod\n    def charge(self, amount: float) -> bool: pass\n\nclass NotificationService(ABC):\n    @abstractmethod\n    def notify(self, recipient: str, message: str): pass\n\nclass CreditCardPayment(PaymentService):\n    def __init__(self, card_num: str): self.card_num = card_num\n    def charge(self, amount: float) -> bool:\n        print(f'CreditCard [{self.card_num}] charged: ${amount:.2f}')\n        return True\n\nclass EmailNotifier(NotificationService):\n    def notify(self, recipient: str, message: str):\n        print(f'Email sent to [{recipient}]: {message}')",
                "explanation": "Low-level I/O services implement clean, focused interfaces."
            },
            {
                "title": "Clean High-Level Coordinator (Refactored OrderEngine)",
                "language": "python",
                "code": "class OrderEngine:\n    def __init__(self, tax: TaxStrategy, pay: PaymentService, notify: NotificationService):\n        self.tax = tax\n        self.pay = pay\n        self.notify = notify\n\n    def checkout(self, items: list, customer_email: str) -> float:\n        subtotal = sum(item.price for item in items)\n        total = subtotal + self.tax.calculate_tax(subtotal)\n        if self.pay.charge(total):\n            self.notify.notify(customer_email, f'Order confirmed! Total: ${total:.2f}')\n        return total\n\n# Execution: Clean, modular, decoupled\nengine = OrderEngine(StandardTax(), CreditCardPayment('4111-2222'), EmailNotifier())\ntotal = engine.checkout([OrderItem('Book', 30.0), OrderItem('Pen', 10.0)], 'alice@test.com')",
                "explanation": "The refactored OrderEngine coordinates collaborators adhering to all 5 SOLID principles."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Refactor Monolithic Report Generator",
            description="Refactor a bad `ReportManager` that computes averages AND formats text AND sends emails. Split into: `GradeStats(scores)` with `average()`, `ReportFormatter` with `format_report(avg)`, and `Sender(ABC)` with `send(text)`.",
            starter_code="# Refactor monolithic ReportManager to obey SRP\npass",
            solution_code="class GradeStats:\n    def __init__(self, scores: list):\n        self.scores = scores\n    def average(self) -> float:\n        return sum(self.scores) / len(self.scores) if self.scores else 0.0\n\nclass ReportFormatter:\n    def format_report(self, avg: float) -> str:\n        return f'Class Average: {avg:.1f}'\n\nclass EmailSender:\n    def send(self, text: str) -> str:\n        return f'Sent report: {text}'",
            expected_output="Sent report: Class Average: 85.0"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What does the DRY engineering maxim stand for?",
                options=[
                    "Don't Repeat Yourself: every piece of logic must have a single, unambiguous representation",
                    "Do Run Yesterday",
                    "Delete Redundant Yields",
                    "Disable Runtime Y-coordinates"
                ],
                correct_answer="Don't Repeat Yourself: every piece of logic must have a single, unambiguous representation",
                explanation="DRY eliminates duplicate logic across a codebase, reducing maintenance overhead."
            ),
            QuizQuestionBlueprint(
                question="What does the KISS engineering maxim stand for?",
                options=[
                    "Keep It Simple, Stupid: avoid unnecessary complexity and over-engineering",
                    "Key Identity Security Service",
                    "Kernel Instruction Set Standard",
                    "Keyboard Input Shift System"
                ],
                correct_answer="Keep It Simple, Stupid: avoid unnecessary complexity and over-engineering",
                explanation="KISS advises developers to choose straightforward solutions over complex abstractions."
            ),
            QuizQuestionBlueprint(
                question="What is the primary sign that a legacy class violates the Single Responsibility Principle?",
                options=[
                    "It mixes domain logic, database operations, and user presentation formatting all inside one file",
                    "It has more than 5 methods",
                    "It imports the math module",
                    "It uses PascalCase for its name"
                ],
                correct_answer="It mixes domain logic, database operations, and user presentation formatting all inside one file",
                explanation="Mixing data models, persistence, and UI formatting gives the class multiple reasons to change."
            ),
            QuizQuestionBlueprint(
                question="How does replacing an `if/elif/else` type switch with Polymorphic Strategies satisfy the Open/Closed Principle?",
                options=[
                    "New options can be added by writing new strategy subclasses without modifying the existing execution engine",
                    "It makes the if statement run faster",
                    "It automatically deletes invalid inputs",
                    "It converts the code into C"
                ],
                correct_answer="New options can be added by writing new strategy subclasses without modifying the existing execution engine",
                explanation="Polymorphic strategies allow adding new options without modifying existing code."
            ),
            QuizQuestionBlueprint(
                question="What is the first step a professional software engineer takes before refactoring legacy code?",
                options=[
                    "Ensures automated test coverage exists to detect any unintended behavioral changes during refactoring",
                    "Deletes all existing files immediately",
                    "Changes the programming language",
                    "Renames all variables to single letters"
                ],
                correct_answer="Ensures automated test coverage exists to detect any unintended behavioral changes during refactoring",
                explanation="Automated tests act as a safety net to ensure refactoring does not alter system behavior."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 51: Creational Patterns (Singleton, Factory Method)
    # -------------------------------------------------------------
    DayBlueprint(
        order=51,
        title="Day 51: Creational Patterns (Singleton & Factory Method)",
        concept="Design Patterns: Gang of Four (GoF) Creational Patterns - Singleton (single shared instance in memory) and Factory Method (deferring instantiation to subclasses)",
        analogy="Think of a country's President: at any given moment, there can only ever be **one** active President (**Singleton**). Everyone in the nation points to the exact same leader; you cannot accidentally spawn a second president in your kitchen! Now think of ordering at a bakery: you ask the baker for 'fresh bread'. You do not operate the mixing vat or oven yourself; the baker (**Factory Method**) decides whether to bake sourdough, rye, or brioche based on your order!",
        theory_sections=[
            {
                "heading": "What are Creational Design Patterns?",
                "body": "Creational design patterns abstract the instantiation process, making systems independent of how their objects are created, composed, and represented.\n\nToday we master two foundational patterns:\n1. **Singleton Pattern**: Ensures that a class has only one instance in memory and provides a global access point to it.\n2. **Factory Method Pattern**: Defines an interface for creating an object, but lets subclasses decide which class to instantiate."
            },
            {
                "heading": "Thread Safety and the Python Singleton",
                "body": "In Python, a Singleton can be implemented via:\n- Overriding `__new__` (intercepting memory allocation).\n- Using a metaclass.\n- Python Modules (modules in Python are naturally singletons because they are cached in `sys.modules`)."
            }
        ],
        code_snippets=[
            {
                "title": "Implementing the Singleton Pattern via __new__ in Python",
                "language": "python",
                "code": "class DatabaseConnection:\n    _instance = None  # Class-level holder for single instance\n\n    def __new__(cls, *args, **kwargs):\n        if cls._instance is None:\n            # Allocate memory only on the first call\n            cls._instance = super().__new__(cls)\n            cls._instance.initialized = False\n        return cls._instance\n\n    def __init__(self, db_url: str = 'localhost:5432'):\n        if not self.initialized:\n            self.db_url = db_url\n            self.initialized = True\n\n# Creating multiple instances points to the exact same object in memory!\ndb1 = DatabaseConnection('prod.db')\ndb2 = DatabaseConnection('staging.db')\nprint('Are db1 and db2 the exact same object?', db1 is db2)  # True\nprint('Shared URL:', db1.db_url)",
                "explanation": "Overriding __new__ guarantees only one instance ever exists on the heap."
            },
            {
                "title": "Factory Method Pattern: Pluggable Document Creator",
                "language": "python",
                "code": "from abc import ABC, abstractmethod\n\n# Product Interface\nclass Document(ABC):\n    @abstractmethod\n    def render(self) -> str: pass\n\n# Concrete Products\nclass PDFDoc(Document):\n    def render(self) -> str: return 'Rendering PDF binary pages'\n\nclass WordDoc(Document):\n    def render(self) -> str: return 'Rendering Word DOCX document'\n\n# Creator Interface with Factory Method\nclass Application(ABC):\n    @abstractmethod\n    def create_document(self) -> Document: pass\n\n    def open_document(self) -> str:\n        # Relies on factory method\n        doc = self.create_document()\n        return f'App opened: {doc.render()}'\n\n# Concrete Creators\nclass PDFApp(Application):\n    def create_document(self) -> Document: return PDFDoc()\n\nclass WordApp(Application):\n    def create_document(self) -> Document: return WordDoc()\n\nprint(PDFApp().open_document())\nprint(WordApp().open_document())",
                "explanation": "Subclasses decide which concrete product to create via the factory method."
            },
            {
                "title": "Simple Parameterized Factory Pattern",
                "language": "python",
                "code": "class LogisticsFactory:\n    @staticmethod\n    def get_transport(mode: str):\n        if mode == 'sea': return 'CargoShip Transport'\n        elif mode == 'road': return 'SemiTruck Transport'\n        elif mode == 'air': return 'CargoPlane Transport'\n        raise ValueError(f'Unknown transport mode: {mode}')\n\nprint(LogisticsFactory.get_transport('sea'))\nprint(LogisticsFactory.get_transport('air'))",
                "explanation": "Parameterized static factory encapsulates object selection logic."
            },
            {
                "title": "Python Script: Proving Singleton Identity via id()",
                "language": "python",
                "code": "print('Hex memory ID of db1:', hex(id(db1)))\nprint('Hex memory ID of db2:', hex(id(db2)))\nassert id(db1) == id(db2)",
                "explanation": "Verifies both variables share the identical memory address."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Thread-Safe Logger Singleton",
            description="Create a `Logger` class implementing the Singleton pattern. It should maintain an `entries: list` initialized to empty. Add a method `log(msg: str)` that appends to `entries`. Verify that two separate instances share the same log history.",
            starter_code="class Logger:\n    # Implement Logger Singleton\n    pass",
            solution_code="class Logger:\n    _instance = None\n    def __new__(cls):\n        if cls._instance is None:\n            cls._instance = super().__new__(cls)\n            cls._instance.entries = []\n        return cls._instance\n\n    def log(self, msg: str):\n        self.entries.append(msg)",
            expected_output="Log count: 2 (Entries: ['Error 404', 'System rebooted'])"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the primary intent of the Singleton Pattern?",
                options=[
                    "To ensure that a class has only one instance in memory and provide a global point of access to it",
                    "To create a new instance on every function call",
                    "To prevent classes from having any variables",
                    "To run code on a single CPU core"
                ],
                correct_answer="To ensure that a class has only one instance in memory and provide a global point of access to it",
                explanation="Singleton restricts instantiation of a class to one single shared object."
            ),
            QuizQuestionBlueprint(
                question="Which special Python magic method is overridden to control memory allocation in a Singleton?",
                options=[
                    "__new__",
                    "__init__",
                    "__call__",
                    "__repr__"
                ],
                correct_answer="__new__",
                explanation="`__new__` is responsible for memory allocation and returning the instance before `__init__` runs."
            ),
            QuizQuestionBlueprint(
                question="What is the intent of the Factory Method Pattern?",
                options=[
                    "To define an interface for creating objects, but let subclasses decide which concrete class to instantiate",
                    "To manufacture physical electronics on an assembly line",
                    "To delete unused objects automatically",
                    "To compile Python into bytecode"
                ],
                correct_answer="To define an interface for creating objects, but let subclasses decide which concrete class to instantiate",
                explanation="Factory Method delegates object creation to subclasses, decoupling creators from concrete products."
            ),
            QuizQuestionBlueprint(
                question="Why are Python modules naturally considered singletons?",
                options=[
                    "Because Python caches imported modules in `sys.modules`; importing a module multiple times always returns the exact same module instance",
                    "Because modules can only contain one function",
                    "Because modules cannot be imported twice without an error",
                    "Because modules do not consume memory"
                ],
                correct_answer="Because Python caches imported modules in `sys.modules`; importing a module multiple times always returns the exact same module instance",
                explanation="Python's import caching mechanism treats modules as singletons across the entire runtime."
            ),
            QuizQuestionBlueprint(
                question="What is a major criticism or drawback of overusing the Singleton Pattern?",
                options=[
                    "It acts like a disguised global variable, making unit testing difficult and introducing hidden state dependencies across unrelated modules",
                    "It increases hard drive temperature",
                    "It slows down Python by 1000%",
                    "It prevents files from being saved"
                ],
                correct_answer="It acts like a disguised global variable, making unit testing difficult and introducing hidden state dependencies across unrelated modules",
                explanation="Singletons introduce global state, making tests interdependent and masking architecture coupling."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 52: Creational Patterns (Builder, Prototype, Abstract Factory)
    # -------------------------------------------------------------
    DayBlueprint(
        order=52,
        title="Day 52: Creational Patterns (Builder, Prototype, Abstract Factory)",
        concept="Advanced Creational Patterns: Builder (step-by-step construction of complex objects), Prototype (cloning existing prototypes), and Abstract Factory (families of related objects)",
        analogy="Think of dining at a high-end restaurant: **Builder** is Subway or Chipotle: you stand at the counter and step-by-step customize your burrito ('Add black beans, add guacamole, toast bread'). **Prototype** is photocopying an artist's master print: instead of painting from scratch, you clone the original template and tweak one color. **Abstract Factory** is ordering an entire interior design suite: you choose 'Victorian Furniture' (and get a Victorian Chair, Victorian Table, Victorian Sofa) or 'Modern Minimalist' (and get matching modern items)!",
        theory_sections=[
            {
                "heading": "The Builder Pattern",
                "body": "The **Builder Pattern** separates the construction of a complex object from its representation, allowing the same construction process to create different representations.\n\nUse Builder when an object requires 10+ constructor arguments, many of which are optional, eliminating the **Telescoping Constructor** anti-pattern."
            },
            {
                "heading": "Prototype & Abstract Factory Patterns",
                "body": "- **Prototype Pattern**: Creates new objects by cloning a prototypical instance (using deep copy), avoiding costly standard initialization.\n- **Abstract Factory Pattern**: Provides an interface for creating **families of related or dependent objects** without specifying their concrete classes (e.g. creating Windows UI buttons/dialogs vs macOS UI buttons/dialogs)."
            }
        ],
        code_snippets=[
            {
                "title": "The Builder Pattern with Fluent Method Chaining",
                "language": "python",
                "code": "class Computer:\n    def __init__(self):\n        self.cpu = None\n        self.ram = None\n        self.gpu = None\n        self.storage = None\n\n    def __repr__(self):\n        return f'Computer(CPU={self.cpu}, RAM={self.ram}, GPU={self.gpu}, Storage={self.storage})'\n\nclass ComputerBuilder:\n    def __init__(self):\n        self.computer = Computer()\n\n    def set_cpu(self, cpu: str): self.computer.cpu = cpu; return self\n    def set_ram(self, ram: str): self.computer.ram = ram; return self\n    def set_gpu(self, gpu: str): self.computer.gpu = gpu; return self\n    def set_storage(self, s: str): self.computer.storage = s; return self\n    def build(self) -> Computer: return self.computer\n\n# Build custom gaming rig step-by-step fluently\ngaming_pc = (ComputerBuilder()\n             .set_cpu('Intel i9 14900K')\n             .set_ram('64GB DDR5')\n             .set_gpu('NVIDIA RTX 4090')\n             .set_storage('2TB NVMe SSD')\n             .build())\nprint(gaming_pc)",
                "explanation": "Builder avoids messy constructors with 10 positional arguments."
            },
            {
                "title": "The Prototype Pattern (Object Cloning Template)",
                "language": "python",
                "code": "import copy\n\nclass MonsterPrototype:\n    def __init__(self, name: str, health: int, weapon: str):\n        self.name, self.health, self.weapon = name, health, weapon\n\n    def clone(self) -> 'MonsterPrototype':\n        return copy.deepcopy(self)\n\n# Create base template prototype\ngoblin_template = MonsterPrototype('Goblin Minion', 50, 'Rusty Dagger')\n\n# Clone 100 goblins cheaply without heavy initialization\ngoblin1 = goblin_template.clone()\ngoblin2 = goblin_template.clone()\ngoblin2.weapon = 'Flaming Axe'  # Mutate clone without affecting template\nprint('Goblin 1 weapon:', goblin1.weapon)\nprint('Goblin 2 weapon:', goblin2.weapon)",
                "explanation": "Clones pre-configured prototypes rather than executing expensive creation logic."
            },
            {
                "title": "The Abstract Factory Pattern (UI Families)",
                "language": "python",
                "code": "from abc import ABC, abstractmethod\n\n# Abstract Factory\nclass GUIFactory(ABC):\n    @abstractmethod\n    def create_button(self): pass\n    @abstractmethod\n    def create_checkbox(self): pass\n\n# Concrete Factory 1: Dark Mode Suite\nclass DarkThemeFactory(GUIFactory):\n    def create_button(self): return 'Dark Slate Button'\n    def create_checkbox(self): return 'Dark Checkbox'\n\n# Concrete Factory 2: Light Mode Suite\nclass LightThemeFactory(GUIFactory):\n    def create_button(self): return 'Light Clean Button'\n    def create_checkbox(self): return 'Light Checkbox'\n\ndef render_ui(factory: GUIFactory):\n    print('Rendered:', factory.create_button(), 'and', factory.create_checkbox())\n\nrender_ui(DarkThemeFactory())\nrender_ui(LightThemeFactory())",
                "explanation": "Abstract Factory produces consistent families of related objects."
            },
            {
                "title": "Python Script: Verifying Prototype Independence",
                "language": "python",
                "code": "print('Are goblin prototypes identical in memory?', goblin1 is goblin_template)\nassert goblin1 is not goblin_template",
                "explanation": "Confirms prototypes clone into completely isolated memory locations."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Fluent SQL Query Builder",
            description="Create a `QueryBuilder` class with methods `table(name)`, `select(*columns)`, and `where(condition)`. Each method must return `self`. The `build()` method should return the completed SQL string: `SELECT {columns} FROM {table} WHERE {condition}`.",
            starter_code="class QueryBuilder:\n    # Implement fluent QueryBuilder\n    pass",
            solution_code="class QueryBuilder:\n    def __init__(self):\n        self._table = ''\n        self._columns = '*'\n        self._where = ''\n\n    def table(self, name: str):\n        self._table = name\n        return self\n\n    def select(self, *columns):\n        self._columns = ', '.join(columns) if columns else '*'\n        return self\n\n    def where(self, condition: str):\n        self._where = condition\n        return self\n\n    def build(self) -> str:\n        sql = f'SELECT {self._columns} FROM {self._table}'\n        if self._where:\n            sql += f' WHERE {self._where}'\n        return sql",
            expected_output="SELECT id, name FROM users WHERE active = 1"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What problem does the Builder Pattern solve?",
                options=[
                    "The Telescoping Constructor anti-pattern, allowing step-by-step construction of complex objects with many optional parameters",
                    "Building physical brick houses",
                    "Running SQL migrations automatically",
                    "Deleting objects from memory"
                ],
                correct_answer="The Telescoping Constructor anti-pattern, allowing step-by-step construction of complex objects with many optional parameters",
                explanation="Builder avoids unwieldy constructors containing dozens of parameters by building objects incrementally."
            ),
            QuizQuestionBlueprint(
                question="What is the core mechanism of the Prototype Pattern?",
                options=[
                    "Creating new objects by cloning an existing configured prototypical instance",
                    "Writing code on paper prototypes before coding",
                    "Inheriting from 10 abstract base classes",
                    "Using prototype variables in JavaScript only"
                ],
                correct_answer="Creating new objects by cloning an existing configured prototypical instance",
                explanation="Prototype duplicates existing template instances (via deep copy) to avoid costly reconstruction."
            ),
            QuizQuestionBlueprint(
                question="What is the intent of the Abstract Factory Pattern?",
                options=[
                    "To provide an interface for creating entire families of related or dependent objects without specifying their concrete classes",
                    "To create a single object only",
                    "To compile abstract methods into bytecode",
                    "To replace all classes with functions"
                ],
                correct_answer="To provide an interface for creating entire families of related or dependent objects without specifying their concrete classes",
                explanation="Abstract Factory creates consistent suites of matching objects (e.g. DarkTheme UI components vs LightTheme UI components)."
            ),
            QuizQuestionBlueprint(
                question="What design feature allows Builder pattern methods to be chained like `builder.set_a().set_b().build()`?",
                options=[
                    "Each builder configuration method returns `self`",
                    "Python automatically chains all functions",
                    "The `break` statement",
                    "The `goto` statement"
                ],
                correct_answer="Each builder configuration method returns `self`",
                explanation="Returning `self` passes the builder instance back to the caller for fluent method chaining."
            ),
            QuizQuestionBlueprint(
                question="Which category of Gang of Four (GoF) design patterns do Builder, Prototype, and Abstract Factory belong to?",
                options=[
                    "Creational Patterns",
                    "Structural Patterns",
                    "Behavioral Patterns",
                    "Architectural Patterns"
                ],
                correct_answer="Creational Patterns",
                explanation="Creational patterns deal specifically with object instantiation and creation mechanisms."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 53: Structural Patterns (Adapter, Decorator, Facade)
    # -------------------------------------------------------------
    DayBlueprint(
        order=53,
        title="Day 53: Structural Patterns (Adapter, Decorator, Facade)",
        concept="Structural Design Patterns: Adapter (bridging incompatible interfaces), Decorator (dynamic runtime feature wrapping), and Facade (simplified front door to complex subsystems)",
        analogy="Think of traveling abroad with electronics: **Adapter** is the foreign electrical plug converter that lets your US 2-prong laptop plug into a European 3-prong wall outlet. **Decorator** is putting on winter clothing: you are still an ordinary human, but you put on a sweater (warmth feature), then a raincoat (waterproof feature), dynamically layering behaviors! **Facade** is a luxury hotel concierge: you just say 'Book me dinner and a theater show'; you don't call 5 restaurants, negotiate theater ticket brokers, or hire a taxi yourself!",
        theory_sections=[
            {
                "heading": "Adapter Pattern: Bridging Incompatible Interfaces",
                "body": "The **Adapter Pattern** converts the interface of a class into another interface that clients expect. It allows classes with incompatible interfaces to collaborate seamlessly without modifying either class's source code."
            },
            {
                "heading": "Decorator & Facade Patterns",
                "body": "- **Decorator Pattern**: Attaches additional responsibilities and features to an object dynamically at runtime. Decorators provide a flexible alternative to subclassing for extending functionality.\n- **Facade Pattern**: Provides a unified, simplified, high-level interface to a complex subsystem of interacting classes, masking underlying complexity."
            }
        ],
        code_snippets=[
            {
                "title": "The Adapter Pattern: Adapting Legacy XML to Modern JSON",
                "language": "python",
                "code": "# Incompatible legacy service returning XML\nclass LegacyXMLService:\n    def get_xml_data(self) -> str:\n        return '<user><id>42</id><name>Alice</name></user>'\n\n# Modern client expects JSON\nclass TargetClientInterface:\n    def get_json_data(self) -> dict: pass\n\n# The Adapter bridges the gap\nclass XMLToJSONAdapter(TargetClientInterface):\n    def __init__(self, xml_service: LegacyXMLService):\n        self.xml_service = xml_service\n\n    def get_json_data(self) -> dict:\n        raw_xml = self.xml_service.get_xml_data()\n        # Simple parsing simulation\n        return {'id': 42, 'name': 'Alice'}\n\nadapter = XMLToJSONAdapter(LegacyXMLService())\nprint('Adapted JSON output:', adapter.get_json_data())",
                "explanation": "Adapter translates calls from TargetClientInterface to LegacyXMLService."
            },
            {
                "title": "The Decorator Pattern: Layering Coffee Features",
                "language": "python",
                "code": "from abc import ABC, abstractmethod\n\nclass Coffee(ABC):\n    @abstractmethod\n    def cost(self) -> float: pass\n    @abstractmethod\n    def description(self) -> str: pass\n\nclass SimpleCoffee(Coffee):\n    def cost(self) -> float: return 2.0\n    def description(self) -> str: return 'Simple Coffee'\n\n# Base Decorator wraps a Coffee object\nclass MilkDecorator(Coffee):\n    def __init__(self, coffee: Coffee): self._coffee = coffee\n    def cost(self) -> float: return self._coffee.cost() + 0.5\n    def description(self) -> str: return self._coffee.description() + ', with Milk'\n\nclass SugarDecorator(Coffee):\n    def __init__(self, coffee: Coffee): self._coffee = coffee\n    def cost(self) -> float: return self._coffee.cost() + 0.2\n    def description(self) -> str: return self._coffee.description() + ', with Sugar'\n\n# Dynamically stack decorators\nmy_brew = SugarDecorator(MilkDecorator(SimpleCoffee()))\nprint(f'{my_brew.description()} costs ${my_brew.cost():.2f}')",
                "explanation": "Decorators wrap components dynamically to add features without class explosion."
            },
            {
                "title": "The Facade Pattern: Home Theater Simplified",
                "language": "python",
                "code": "class DVDPlayer: def on(self): return 'DVD ON'\nclass Projector: def on(self): return 'Projector ON'\nclass SoundSystem: def on(self): return 'Surround 5.1 ON'\n\n# Facade provides simple 1-click interface\nclass HomeTheaterFacade:\n    def __init__(self):\n        self.dvd = DVDPlayer()\n        self.proj = Projector()\n        self.sound = SoundSystem()\n\n    def watch_movie(self):\n        return f'{self.proj.on()} | {self.sound.on()} | {self.dvd.on()} -> Movie Playing!'\n\nprint(HomeTheaterFacade().watch_movie())",
                "explanation": "Facade masks complex multi-class choreography behind a single method."
            },
            {
                "title": "Python Script: Checking Decorator Type Hierarchy",
                "language": "python",
                "code": "print('Is decorated brew still Coffee?', isinstance(my_brew, Coffee))  # True\nprint('Total stacked decorators:', 2)",
                "explanation": "Confirms decorators maintain full polymorphic substitutability."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Text Formatter Decorator",
            description="Create a `Text(ABC)` with method `render() -> str`. Create `PlainText(content)` returning `content`. Create `BoldDecorator(text: Text)` that wraps `text` and returns `f'<b>{text.render()}</b>'`, and `ItalicDecorator(text: Text)` returning `f'<i>{text.render()}</i>'`. Demonstrate layering both.",
            starter_code="from abc import ABC, abstractmethod\n# Implement PlainText, BoldDecorator, ItalicDecorator\npass",
            solution_code="from abc import ABC, abstractmethod\n\nclass Text(ABC):\n    @abstractmethod\n    def render(self) -> str: pass\n\nclass PlainText(Text):\n    def __init__(self, content: str): self.content = content\n    def render(self) -> str: return self.content\n\nclass BoldDecorator(Text):\n    def __init__(self, text: Text): self.text = text\n    def render(self) -> str: return f'<b>{self.text.render()}</b>'\n\nclass ItalicDecorator(Text):\n    def __init__(self, text: Text): self.text = text\n    def render(self) -> str: return f'<i>{self.text.render()}</i>'",
            expected_output="<i><b>Hello World</b></i>"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the primary purpose of the Adapter Pattern?",
                options=[
                    "To convert the interface of an existing class into another interface that clients expect, enabling incompatible classes to collaborate",
                    "To change power voltage in electrical circuits",
                    "To convert Python files into HTML",
                    "To delete old classes from Git"
                ],
                correct_answer="To convert the interface of an existing class into another interface that clients expect, enabling incompatible classes to collaborate",
                explanation="Adapter translates incompatible interfaces so disparate classes can communicate without modifying their code."
            ),
            QuizQuestionBlueprint(
                question="How does the Decorator Pattern extend object functionality compared to traditional subclassing?",
                options=[
                    "It wraps objects dynamically at runtime, allowing features to be added or stacked flexibly without creating an explosion of subclasses",
                    "It modifies the Python C source code",
                    "It runs all functions in background threads",
                    "It requires no memory allocation"
                ],
                correct_answer="It wraps objects dynamically at runtime, allowing features to be added or stacked flexibly without creating an explosion of subclasses",
                explanation="Decorators wrap objects at runtime, avoiding the combinatorial explosion of subclasses."
            ),
            QuizQuestionBlueprint(
                question="What is the intent of the Facade Pattern?",
                options=[
                    "To provide a simplified, high-level interface that masks the complexity of an intricate subsystem of classes",
                    "To disguise malware as a harmless class",
                    "To draw 3D graphics on the screen",
                    "To compile code into machine language"
                ],
                correct_answer="To provide a simplified, high-level interface that masks the complexity of an intricate subsystem of classes",
                explanation="Facade presents a simple 'front door' method coordinating multiple complex subsystem classes."
            ),
            QuizQuestionBlueprint(
                question="Which category of Gang of Four (GoF) design patterns do Adapter, Decorator, and Facade belong to?",
                options=[
                    "Structural Patterns",
                    "Creational Patterns",
                    "Behavioral Patterns",
                    "Concurrency Patterns"
                ],
                correct_answer="Structural Patterns",
                explanation="Structural patterns focus on how classes and objects are composed to form larger, cohesive structures."
            ),
            QuizQuestionBlueprint(
                question="What real-world object best models the Facade pattern?",
                options=[
                    "A hotel front-desk concierge who coordinates dining, baggage, tickets, and taxis behind a single request",
                    "A wooden baseball bat",
                    "A pair of reading glasses",
                    "A blank sheet of paper"
                ],
                correct_answer="A hotel front-desk concierge who coordinates dining, baggage, tickets, and taxis behind a single request",
                explanation="The concierge acts as a facade, coordinating diverse hotel subsystems on behalf of the guest."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 54: Behavioral Patterns (Observer, Strategy, State)
    # -------------------------------------------------------------
    DayBlueprint(
        order=54,
        title="Day 54: Behavioral Patterns (Observer, Strategy, State)",
        concept="Behavioral Design Patterns: Observer (publish-subscribe event notification), Strategy (interchangeable algorithms), and State (finite state machine encapsulation)",
        analogy="Think of a YouTube channel and a vending machine: **Observer** is hitting the 'Subscribe & Bell Icon' button: whenever the creator uploads a new video (**Subject**), YouTube immediately sends an alert to all 10,000 subscribers (**Observers**) automatically! **Strategy** is choosing Google Maps navigation: Driving, Walking, or Subway transit (swapping routing algorithms). **State** is a Vending Machine: when it has 'No Money Inserted', pushing a soda button does nothing; when it transitions to 'Money Inserted', that exact same button dispenses a soda!",
        theory_sections=[
            {
                "heading": "What are Behavioral Patterns?",
                "body": "Behavioral patterns focus on **algorithms and the assignment of responsibilities between objects**. They characterize complex control flows that are difficult to anticipate at compile time."
            },
            {
                "heading": "Observer, Strategy, and State Patterns",
                "body": "1. **Observer Pattern**: Defines a 1-to-Many dependency. When the Subject changes state, all registered Observers are notified and updated automatically (foundation of event-driven architectures, GUI listeners, and RxJS/Reactive streams).\n2. **Strategy Pattern**: Encapsulates a family of algorithms, making them interchangeable inside a client at runtime.\n3. **State Pattern**: Allows an object to alter its behavior when its internal state changes, appearing to change its class (encapsulates Finite State Machines into separate state classes)."
            }
        ],
        code_snippets=[
            {
                "title": "The Observer Pattern: Event Notification Hub",
                "language": "python",
                "code": "from abc import ABC, abstractmethod\n\nclass Observer(ABC):\n    @abstractmethod\n    def update(self, event_data: str): pass\n\nclass NewsAgency:\n    def __init__(self):\n        self._subscribers = []\n\n    def subscribe(self, obs: Observer): self._subscribers.append(obs)\n    def unsubscribe(self, obs: Observer): self._subscribers.remove(obs)\n\n    def publish_news(self, headline: str):\n        print(f'\\n[AGENCY BROADCAST]: {headline}')\n        for sub in self._subscribers:\n            sub.update(headline)\n\nclass NewsChannel(Observer):\n    def __init__(self, name: str): self.name = name\n    def update(self, headline: str):\n        print(f'{self.name} received breaking news: \"{headline}\"')\n\nagency = NewsAgency()\ncnn = NewsChannel('CNN')\nbbc = NewsChannel('BBC')\nagency.subscribe(cnn)\nagency.subscribe(bbc)\nagency.publish_news('Tech Market Reaches All-Time High!')",
                "explanation": "Subject notifies all registered observers automatically when state updates."
            },
            {
                "title": "The State Pattern: Vending Machine FSM",
                "language": "python",
                "code": "class VendingState(ABC):\n    @abstractmethod\n    def insert_coin(self, context) -> str: pass\n    @abstractmethod\n    def press_button(self, context) -> str: pass\n\nclass NoCoinState(VendingState):\n    def insert_coin(self, context):\n        context.state = HasCoinState()\n        return 'Coin accepted.'\n    def press_button(self, context):\n        return 'Please insert a coin first!'\n\nclass HasCoinState(VendingState):\n    def insert_coin(self, context): return 'Coin already inserted.'\n    def press_button(self, context):\n        context.state = NoCoinState()\n        return 'Soda dispensed! Enjoy!'\n\nclass VendingMachine:\n    def __init__(self):\n        self.state = NoCoinState()  # Initial state\n    def insert_coin(self): return self.state.insert_coin(self)\n    def press_button(self): return self.state.press_button(self)\n\nvm = VendingMachine()\nprint(vm.press_button())  # Please insert coin first!\nprint(vm.insert_coin())   # Coin accepted.\nprint(vm.press_button())  # Soda dispensed! Transitions back to NoCoinState.",
                "explanation": "State pattern eliminates complex switch statements by encapsulating states as objects."
            },
            {
                "title": "The Strategy Pattern: Pluggable Compression Algorithms",
                "language": "python",
                "code": "class CompressionStrategy(ABC):\n    @abstractmethod\n    def compress(self, file_data: str) -> str: pass\n\nclass ZipCompression(CompressionStrategy):\n    def compress(self, data): return f'ZIP_COMPRESSED({len(data)} chars)'\n\nclass RarCompression(CompressionStrategy):\n    def compress(self, data): return f'RAR_COMPRESSED({len(data)} chars)'\n\nclass ArchiveEngine:\n    def __init__(self, strategy: CompressionStrategy): self.strategy = strategy\n    def execute(self, text): return self.strategy.compress(text)\n\nprint(ArchiveEngine(ZipCompression()).execute('Big Log Data'))",
                "explanation": "Strategy encapsulates interchangeable algorithms behind a common contract."
            },
            {
                "title": "Python Script: Dynamic Strategy Swapping at Runtime",
                "language": "python",
                "code": "archiver = ArchiveEngine(ZipCompression())\narchiver.strategy = RarCompression()  # Swapped algorithm at runtime!\nprint(archiver.execute('Database Dump'))",
                "explanation": "Confirms strategies can be swapped on the fly without reconstructing context."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Observer Pattern Stock Ticker",
            description="Create an `Observer(ABC)` with `notify(symbol, price)`. Create a `StockTicker` subject with `register(observer)` and `set_price(symbol, price)` that broadcasts to all registered observers. Create a `MobileAlert` observer that prints `f'Alert: {symbol} is ${price}'`.",
            starter_code="from abc import ABC, abstractmethod\n# Implement Observer and StockTicker\npass",
            solution_code="from abc import ABC, abstractmethod\n\nclass Observer(ABC):\n    @abstractmethod\n    def notify(self, symbol: str, price: float): pass\n\nclass StockTicker:\n    def __init__(self):\n        self.observers = []\n    def register(self, obs: Observer):\n        self.observers.append(obs)\n    def set_price(self, symbol: str, price: float):\n        for obs in self.observers:\n            obs.notify(symbol, price)\n\nclass MobileAlert(Observer):\n    def notify(self, symbol: str, price: float):\n        print(f'Alert: {symbol} is ${price}')",
            expected_output="Alert: AAPL is $185.5"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the intent of the Observer Pattern?",
                options=[
                    "To define a 1-to-Many dependency so that when one object updates its state, all its registered dependents are notified automatically",
                    "To spy on users' private passwords",
                    "To serialize objects into binary files",
                    "To prevent other classes from being created"
                ],
                correct_answer="To define a 1-to-Many dependency so that when one object updates its state, all its registered dependents are notified automatically",
                explanation="Observer decouples subjects from listeners, enabling event-driven publish-subscribe architectures."
            ),
            QuizQuestionBlueprint(
                question="How does the State Pattern eliminate massive, error-prone `if/elif/else` ladders in state machines?",
                options=[
                    "By encapsulating each individual state into its own distinct class that implements state-specific behaviors and transitions",
                    "By deleting all state transitions from code",
                    "By forcing all states into a single string",
                    "By executing code in parallel threads"
                ],
                correct_answer="By encapsulating each individual state into its own distinct class that implements state-specific behaviors and transitions",
                explanation="The State pattern represents states as objects, replacing state switches with polymorphic dispatch."
            ),
            QuizQuestionBlueprint(
                question="What is the primary difference between the Strategy Pattern and the State Pattern?",
                options=[
                    "Strategy encapsulates interchangeable algorithms chosen by the client; State encapsulates internal lifecycle transitions that the object moves through autonomously",
                    "Strategy is for numbers; State is for strings",
                    "State only works in C++",
                    "There is no difference; they are exact duplicates"
                ],
                correct_answer="Strategy encapsulates interchangeable algorithms chosen by the client; State encapsulates internal lifecycle transitions that the object moves through autonomously",
                explanation="Strategy is client-directed algorithm selection; State is autonomous internal lifecycle mutation."
            ),
            QuizQuestionBlueprint(
                question="Which category of Gang of Four (GoF) design patterns do Observer, Strategy, and State belong to?",
                options=[
                    "Behavioral Patterns",
                    "Creational Patterns",
                    "Structural Patterns",
                    "Hardware Patterns"
                ],
                correct_answer="Behavioral Patterns",
                explanation="Behavioral patterns govern communication, responsibilities, and algorithms between objects."
            ),
            QuizQuestionBlueprint(
                question="What modern architectural paradigm is fundamentally built on the Observer pattern?",
                options=[
                    "Event-Driven Architecture (EDA) and Reactive Programming (RxJS, Event Listeners)",
                    "Monolithic Procedural Scripting",
                    "Relational Database Table Normalization",
                    "Punch Card Processing"
                ],
                correct_answer="Event-Driven Architecture (EDA) and Reactive Programming (RxJS, Event Listeners)",
                explanation="Event-driven systems and GUI listeners are direct architectural evolutions of the Observer pattern."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 55 (Capstone): Complete E-Commerce Architecture using Design Patterns
    # -------------------------------------------------------------
    DayBlueprint(
        order=55,
        title="Day 55: Complete E-Commerce Architecture & OOP Capstone",
        concept="Grand Capstone Review: Synthesizing the 4 Pillars of OOP, SOLID Principles, and GoF Design Patterns into a unified enterprise E-Commerce platform",
        analogy="Think of building an empire like Amazon: you have unified product classes (**Encapsulation**), specialized product subtypes like Electronics and Groceries (**Inheritance**), pluggable payment processors (**Polymorphism & Strategy**), abstract order workflows (**Abstraction**), decoupled notification listeners (**Observer**), single database access points (**Singleton**), and modular order building (**Builder**). Today, we combine all 55 days of mastery into a production-grade software architecture!",
        is_project_day=True,
        project_name="Complete E-Commerce Architecture Capstone",
        theory_sections=[
            {
                "heading": "Capstone Platform Architecture",
                "body": "Today's grand capstone project demonstrates the full synthesis of Object-Oriented Software Engineering:\n1. **Creational**: `Database` (Singleton), `OrderBuilder` (Builder).\n2. **Structural**: `LegacyPaymentAdapter` (Adapter), `GiftWrapDecorator` (Decorator).\n3. **Behavioral**: `Discounts` (Strategy), `InventoryTracker` (Observer).\n4. **SOLID Enforcement**: Clean single responsibilities, open extension, substitutable contracts, segregated interfaces, and dependency inversion throughout."
            },
            {
                "heading": "55-Day Journey of Object-Oriented Mastery",
                "body": "Congratulations on completing 55 days of intensive engineering! Let us review the ten mastery modules:\n1. **Foundation (Days 1-7)**: Paradigms, Classes, State/Behavior, `self`/`this`, Constructors, Garbage Collection, Student System.\n2. **Encapsulation (Days 8-12)**: Data Binding, Modifiers (`_`, `__`), `@property` Getters/Setters, Data Hiding, Secure Bank.\n3. **Inheritance (Days 13-19)**: IS-A, Single/Multilevel/Hierarchical/Hybrid, Diamond Problem, `super()`, Constructor Chaining, Corporate Hierarchy.\n4. **Polymorphism (Days 20-25)**: Overloading, Operator Overloading (`+`, `==`), Overriding, Virtual Tables, Up/Downcasting, CAD Shapes.\n5. **Abstraction (Days 26-30)**: Abstract Base Classes (`abc`), Protocols, Interface Segregation, Payment Gateways.\n6. **Relationships (Days 31-35)**: Association, Aggregation (weak), Composition (strong), Dependency, Library System.\n7. **Advanced OOP (Days 36-41)**: Static members, `final` immutability, Custom Exceptions, Enums, Inner Classes, Deep Copying.\n8. **OOAD (Days 42-44)**: UML Class Boxes, Visibility (`+`, `-`, `#`), Use Case Diagrams, Sequence Diagrams.\n9. **SOLID (Days 45-50)**: SRP, OCP, LSP, ISP, DIP, Refactoring Legacy Monoliths.\n10. **Design Patterns (Days 51-55)**: Singleton, Factory Method, Builder, Prototype, Adapter, Decorator, Facade, Observer, Strategy, State."
            }
        ],
        code_snippets=[
            {
                "title": "Capstone: Product Hierarchy and Strategy Discounts",
                "language": "python",
                "code": "from abc import ABC, abstractmethod\n\n# Product Hierarchy (Encapsulation & Inheritance)\nclass Product:\n    def __init__(self, sku: str, title: str, price: float):\n        self.sku = sku\n        self.title = title\n        self._price = float(price)\n    @property\n    def price(self) -> float: return self._price\n\n# Strategy Pattern: Pluggable Discounts\nclass DiscountStrategy(ABC):\n    @abstractmethod\n    def calculate(self, total: float) -> float: pass\n\nclass PercentageDiscount(DiscountStrategy):\n    def __init__(self, pct: float): self.pct = pct\n    def calculate(self, total: float) -> float: return total * (1.0 - (self.pct / 100.0))",
                "explanation": "Combines encapsulated domain state with strategy pattern discounts."
            },
            {
                "title": "Capstone: Builder Pattern Order Construction",
                "language": "python",
                "code": "class Order:\n    def __init__(self):\n        self.items = []\n        self.discount_strategy = None\n    def get_total(self) -> float:\n        subtotal = sum(item.price for item in self.items)\n        if self.discount_strategy:\n            return self.discount_strategy.calculate(subtotal)\n        return subtotal\n\nclass OrderBuilder:\n    def __init__(self):\n        self._order = Order()\n    def add_item(self, product: Product): self._order.items.append(product); return self\n    def apply_discount(self, strat: DiscountStrategy): self._order.discount_strategy = strat; return self\n    def build(self) -> Order: return self._order",
                "explanation": "Builder fluently composes products and discount strategies into orders."
            },
            {
                "title": "Capstone: Observer Event Notifications on Order Placement",
                "language": "python",
                "code": "class OrderObserver(ABC):\n    @abstractmethod\n    def on_order_placed(self, order: Order): pass\n\nclass EmailService(OrderObserver):\n    def on_order_placed(self, order: Order):\n        print(f'EMAIL: Order of ${order.get_total():.2f} confirmed!')\n\nclass OrderDispatcher:\n    def __init__(self):\n        self.observers = []\n    def register(self, obs: OrderObserver): self.observers.append(obs)\n    def dispatch(self, order: Order):\n        for obs in self.observers: obs.on_order_placed(order)\n\n# Assemble full capstone workflow\norder = (OrderBuilder()\n         .add_item(Product('SKU-1', 'Laptop', 1200))\n         .add_item(Product('SKU-2', 'Mouse', 50))\n         .apply_discount(PercentageDiscount(10))\n         .build())\n\ndispatcher = OrderDispatcher()\ndispatcher.register(EmailService())\ndispatcher.dispatch(order)",
                "explanation": "Executes integrated order building and observer dispatching."
            },
            {
                "title": "Python Script: 55-Day Course Completion Certificate",
                "language": "python",
                "code": "print('=== 55-DAY OBJECT-ORIENTED PROGRAMMING COURSE COMPLETE ===')\nprint('Total Lessons: 55 | Total Quizzes: 275 | Mastery: 100%')\nprint('Skills Acquired: OOP Pillars, SOLID Principles, GoF Design Patterns, OOAD UML')",
                "explanation": "Outputs course milestone summary and engineering competencies mastered."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Capstone Platform Integration Test",
            description="Create a `PaymentProcessor(ABC)` with `pay(amount)`. Implement `MockPayment(PaymentProcessor)` that records payments. Connect `Order.checkout(payment_processor)` to charge the order's `get_total()` and return `'PAID'`.",
            starter_code="from abc import ABC, abstractmethod\n# Implement MockPayment and Order.checkout\npass",
            solution_code="from abc import ABC, abstractmethod\n\nclass PaymentProcessor(ABC):\n    @abstractmethod\n    def pay(self, amount: float) -> bool: pass\n\nclass MockPayment(PaymentProcessor):\n    def __init__(self):\n        self.total_paid = 0.0\n    def pay(self, amount: float) -> bool:\n        self.total_paid += amount\n        return True\n\nclass Order:\n    def __init__(self, amount: float):\n        self.amount = float(amount)\n    def checkout(self, processor: PaymentProcessor) -> str:\n        if processor.pay(self.amount):\n            return 'PAID'\n        return 'FAILED'",
            expected_output="Checkout Result: PAID (Total charged: $1125.00)"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What are the four foundational pillars of Object-Oriented Programming synthesized in this capstone?",
                options=[
                    "Encapsulation, Inheritance, Polymorphism, and Abstraction",
                    "Input, Output, Storage, and Processing",
                    "Variables, Loops, Functions, and Classes",
                    "Public, Private, Protected, and Static"
                ],
                correct_answer="Encapsulation, Inheritance, Polymorphism, and Abstraction",
                explanation="The four core pillars underpinning all Object-Oriented design are Encapsulation, Inheritance, Polymorphism, and Abstraction."
            ),
            QuizQuestionBlueprint(
                question="How does combining the Builder Pattern with the Strategy Pattern benefit order processing in an e-commerce platform?",
                options=[
                    "Builder allows fluent, readable step-by-step assembly of the order, while Strategy permits swapping discount algorithms dynamically",
                    "It converts orders into cryptocurrencies",
                    "It eliminates the need to pay for items",
                    "It runs Python code inside the browser with no server"
                ],
                correct_answer="Builder allows fluent, readable step-by-step assembly of the order, while Strategy permits swapping discount algorithms dynamically",
                explanation="Combining Builder with Strategy allows modular object composition alongside flexible algorithmic policy selection."
            ),
            QuizQuestionBlueprint(
                question="What role does the Observer pattern play when an order checkout completes in an enterprise e-commerce platform?",
                options=[
                    "It decouples order checkout from side-effects: inventory tracking, warehouse fulfillment, analytics, and customer emails all react independently",
                    "It blocks user credit cards",
                    "It encrypts the order in a secret folder",
                    "It prevents refunds"
                ],
                correct_answer="It decouples order checkout from side-effects: inventory tracking, warehouse fulfillment, analytics, and customer emails all react independently",
                explanation="Observer decouples checkout completion from secondary downstream listeners like billing, shipping, and email services."
            ),
            QuizQuestionBlueprint(
                question="Why is Dependency Injection utilized when providing `PaymentProcessor` to the `Order.checkout` method?",
                options=[
                    "It satisfies the Dependency Inversion Principle (DIP), allowing checkout logic to remain decoupled from volatile payment gateway vendors and enabling test mocking",
                    "It makes credit cards charge zero fees",
                    "It runs payment transactions on the GPU",
                    "It prevents customers from entering invalid card numbers"
                ],
                correct_answer="It satisfies the Dependency Inversion Principle (DIP), allowing checkout logic to remain decoupled from volatile payment gateway vendors and enabling test mocking",
                explanation="Injecting payment dependencies decouples domain logic from vendor APIs and simplifies automated testing."
            ),
            QuizQuestionBlueprint(
                question="Across the complete 55-day course, what is the ultimate objective of Object-Oriented Design, SOLID, and Design Patterns?",
                options=[
                    "To build scalable, maintainable, modular, and testable software that gracefully accommodates changing business requirements over time",
                    "To write as many lines of code as humanly possible",
                    "To make code impossible for other engineers to understand",
                    "To replace human software engineers with algorithms"
                ],
                correct_answer="To build scalable, maintainable, modular, and testable software that gracefully accommodates changing business requirements over time",
                explanation="Professional software engineering strives for maintainable, decoupled architectures that evolve smoothly without accumulating technical debt."
            )
        ]
    )
]
