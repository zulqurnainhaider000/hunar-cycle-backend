"""
Database Management 40-Day Curriculum - Module 1, Module 2 & Module 3 (Part 1) (Days 1 to 10)
Module 1: Database Fundamentals (Days 1-4)
Module 2: Basic SQL (Days 5-9)
Module 3: Database Design & Architecture (Day 10)
"""

from seeder.course_blueprint import DayBlueprint, QuizQuestionBlueprint, CodingChallengeBlueprint

DAYS_1_TO_10 = [
    # -------------------------------------------------------------
    # DAY 1
    # -------------------------------------------------------------
    DayBlueprint(
        order=1,
        title="Day 1: DBMS vs RDBMS - Core Differences & Use Cases",
        concept="Understanding data persistence, flat-file systems, Database Management Systems (DBMS), and Relational Database Management Systems (RDBMS)",
        analogy="Imagine an unorganized shoebox full of paper receipts (flat files). Finding a grocery receipt from last March means sifting through every single paper. A basic filing cabinet with labeled folders (DBMS) helps you group receipts, but there are no cross-links. An RDBMS is like an intelligent digital accountant sitting at the cabinet: if you point to a customer, it automatically pulls their invoices, receipts, and order dates across tables with zero paper shuffling!",
        theory_sections=[
            {
                "heading": "From Flat Files to Database Management Systems",
                "body": "Early computing stored records in simple comma-separated or plaintext files. Flat files suffer from major limitations: data redundancy, lack of concurrency control (two users saving simultaneously causes data corruption), no built-in security, and no query optimization. A DBMS solves this by providing programmatic interfaces to manage and access data files safely."
            },
            {
                "heading": "What Makes an RDBMS 'Relational'?",
                "body": "An RDBMS (such as PostgreSQL, MySQL, SQLite, or Oracle) organizes data into mathematical relations called tables. Tables consist of rows (records) and columns (attributes). Critically, relations between tables are enforced through primary and foreign keys, supporting the relational algebra formulated by Edgar F. Codd and upholding ACID guarantees."
            }
        ],
        code_snippets=[
            {
                "title": "Flat-File CSV Parsing vs Relational Storage Problem",
                "language": "python",
                "code": "# Reading flat files requires loading the entire file into memory\nimport csv\n\nwith open('users.csv', 'r') as f:\n    reader = csv.DictReader(f)\n    # Linear O(N) search without indexing\n    user = [row for row in reader if row['id'] == '1042']",
                "explanation": "Flat files require manual parsing and lack indexing, meaning queries require slow linear table scans."
            },
            {
                "title": "Creating an RDBMS Table with Relational Integrity",
                "language": "sql",
                "code": "CREATE TABLE customers (\n    id SERIAL PRIMARY KEY,\n    first_name VARCHAR(50) NOT NULL,\n    email VARCHAR(120) UNIQUE NOT NULL,\n    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP\n);\n\nCREATE TABLE orders (\n    id SERIAL PRIMARY KEY,\n    customer_id INT REFERENCES customers(id) ON DELETE CASCADE,\n    amount DECIMAL(10, 2) NOT NULL\n);",
                "explanation": "An RDBMS enforces foreign key constraints (`REFERENCES customers(id)`), ensuring orphaned orders can never exist."
            },
            {
                "title": "Querying with Relational JOIN in RDBMS",
                "language": "sql",
                "code": "SELECT \n    c.first_name,\n    o.id AS order_id,\n    o.amount\nFROM customers c\nINNER JOIN orders o ON c.id = o.customer_id\nWHERE o.amount > 100.00;",
                "explanation": "The RDBMS query engine parses relational connections and retrieves data across tables in microseconds."
            },
            {
                "title": "Verifying Integrity Violations in an RDBMS",
                "language": "sql",
                "code": "-- Attempting to insert an order for a customer that does not exist:\nINSERT INTO orders (customer_id, amount)\nVALUES (9999, 49.99);\n-- ERROR: insert or update on table 'orders' violates foreign key constraint",
                "explanation": "Unlike flat-file DBMSs, an RDBMS rejects invalid data insertions that violate referential integrity."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Database Identifier Validator",
            description="Write a Python function `is_valid_table_name(name: str) -> bool` that verifies a database table name starts with a lowercase letter or underscore, contains only alphanumeric characters and underscores, and is between 1 and 63 characters long.",
            starter_code="def is_valid_table_name(name: str) -> bool:\n    # Return True if valid SQL table identifier\n    pass",
            solution_code="import re\n\ndef is_valid_table_name(name: str) -> bool:\n    if not name or len(name) > 63:\n        return False\n    return bool(re.match(r'^[a-z_][a-z0-9_]*$', name))",
            expected_output="is_valid_table_name('users_2026') == True, is_valid_table_name('123_invalid') == False"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the primary difference between a basic DBMS and an RDBMS?",
                options=[
                    "An RDBMS organizes data into relational tables with enforced foreign key relationships and ACID compliance",
                    "A DBMS is always cloud-hosted while RDBMS only runs on local floppy disks",
                    "An RDBMS does not support queries or indexes",
                    "A DBMS only stores binary audio files"
                ],
                correct_answer="An RDBMS organizes data into relational tables with enforced foreign key relationships and ACID compliance",
                explanation="RDBMS structures data into mathematical tables and enforces relational constraints between entities."
            ),
            QuizQuestionBlueprint(
                question="Who introduced the relational model for database management in 1970?",
                options=[
                    "Edgar F. Codd (E.F. Codd)",
                    "Alan Turing",
                    "Dennis Ritchie",
                    "Guido van Rossum"
                ],
                correct_answer="Edgar F. Codd (E.F. Codd)",
                explanation="E.F. Codd published the pioneering paper 'A Relational Model of Data for Large Shared Data Banks' at IBM in 1970."
            ),
            QuizQuestionBlueprint(
                question="Which of the following is an example of an RDBMS?",
                options=[
                    "PostgreSQL",
                    "Plain CSV file",
                    "Notepad text document",
                    "JSON object in RAM"
                ],
                correct_answer="PostgreSQL",
                explanation="PostgreSQL is a world-class open-source Relational Database Management System."
            ),
            QuizQuestionBlueprint(
                question="What problem occurs when multiple users write to a flat-file database simultaneously without concurrency control?",
                options=[
                    "Data corruption and race conditions where changes overwrite each other",
                    "The computer monitor turns off",
                    "The hard drive size instantly doubles",
                    "The file converts into an executable program"
                ],
                correct_answer="Data corruption and race conditions where changes overwrite each other",
                explanation="Without locking mechanisms and concurrency protocols, simultaneous writes lead to corrupted or lost updates."
            ),
            QuizQuestionBlueprint(
                question="What does 'referential integrity' mean in an RDBMS?",
                options=[
                    "Foreign key references must always point to a valid existing primary key row",
                    "All column names must start with capital letters",
                    "Every table must have at least 1,000 rows",
                    "The database can only be queried using Python"
                ],
                correct_answer="Foreign key references must always point to a valid existing primary key row",
                explanation="Referential integrity ensures child tables never reference non-existent parent rows."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 2
    # -------------------------------------------------------------
    DayBlueprint(
        order=2,
        title="Day 2: Data Models - Hierarchical, Network & Relational",
        concept="Tracing the evolution of data architecture from tree structures and graph networks to modern relational schemas",
        analogy="Think of data models like corporate communication. A Hierarchical model is like a strict monarch: the King talks to the Duke, the Duke talks to the Knight (a 1-to-N tree; a child has only one parent). A Network model is like a cobweb: anyone can talk to anyone with pointers, but it gets hopelessly tangled. The Relational model is like a spreadsheet grid where connections are made by values, making queries flexible and elegant!",
        theory_sections=[
            {
                "heading": "The Hierarchical & Network Data Models",
                "body": "In the 1960s, IBM's IMS introduced the Hierarchical model, organizing records into tree structures where each child record has exactly one parent. The CODASYL Network model improved on this by allowing child records to have multiple parents (many-to-many graph). However, both models required developers to navigate physical disk pointers, making schema modifications extremely difficult."
            },
            {
                "heading": "The Triumph of the Relational Model",
                "body": "The Relational model decoupled the logical data structure from physical disk storage. Users declare *what* data they want using declarative SQL rather than specifying *how* pointers should be traversed across disks. Relationships are formed by matching data values (keys) rather than hardcoded hardware addresses."
            }
        ],
        code_snippets=[
            {
                "title": "Hierarchical Data Representation (JSON / Tree)",
                "language": "json",
                "code": "{\n  \"department\": \"Engineering\",\n  \"manager\": \"Sarah\",\n  \"teams\": [\n    {\n      \"name\": \"Mobile\",\n      \"employees\": [\"Alice\", \"Bob\"]\n    }\n  ]\n}",
                "explanation": "Hierarchical models represent 1-to-many parent-child relationships, but struggle when an employee belongs to multiple departments."
            },
            {
                "title": "Network Model Representation (Graph Connections)",
                "language": "python",
                "code": "# Network model relies on direct pointer references between nodes\nclass MemberNode:\n    def __init__(self, name):\n        self.name = name\n        self.projects = []  # Pointers to multiple projects\n\nclass ProjectNode:\n    def __init__(self, title):\n        self.title = title\n        self.members = []  # Pointers to multiple members",
                "explanation": "Network models support many-to-many relationships, but pointer integrity must be maintained manually."
            },
            {
                "title": "Relational Model Representation (Declarative Tables)",
                "language": "sql",
                "code": "CREATE TABLE employees (\n    emp_id INT PRIMARY KEY,\n    name VARCHAR(50)\n);\n\nCREATE TABLE projects (\n    project_id INT PRIMARY KEY,\n    title VARCHAR(100)\n);\n\n-- Bridge table linking many-to-many relation declaratively\nCREATE TABLE project_assignments (\n    emp_id INT REFERENCES employees(emp_id),\n    project_id INT REFERENCES projects(project_id),\n    assigned_date DATE,\n    PRIMARY KEY (emp_id, project_id)\n);",
                "explanation": "The relational model handles many-to-many links via an intermediate bridge table using standard keys."
            },
            {
                "title": "Declarative Relational Query Without Pointer Traversal",
                "language": "sql",
                "code": "SELECT e.name, p.title\nFROM employees e\nJOIN project_assignments pa ON e.emp_id = pa.emp_id\nJOIN projects p ON pa.project_id = p.project_id\nWHERE p.title = 'Hunar Mobile App';",
                "explanation": "SQL allows retrieving data by logical criteria rather than manually following physical disk pointer chains."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Tree Depth Calculator for Hierarchical Data",
            description="Write a Python function `get_tree_depth(node: dict) -> int` that computes the maximum depth of a hierarchical dictionary containing nested `'children'` lists. A single node with no children has depth 1.",
            starter_code="def get_tree_depth(node: dict) -> int:\n    # Calculate tree depth recursively\n    pass",
            solution_code="def get_tree_depth(node: dict) -> int:\n    if not node or not isinstance(node, dict):\n        return 0\n    children = node.get('children', [])\n    if not children:\n        return 1\n    return 1 + max(get_tree_depth(child) for child in children)",
            expected_output="get_tree_depth({'name': 'root', 'children': [{'name': 'child1', 'children': []}]}) == 2"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="In a Hierarchical data model, how many parent records can a single child record have?",
                options=[
                    "Exactly one parent",
                    "Unlimited parents",
                    "Up to 16 parents",
                    "A child record cannot have any parents"
                ],
                correct_answer="Exactly one parent",
                explanation="The hierarchical model is strictly a tree structure where each child node has exactly one parent node."
            ),
            QuizQuestionBlueprint(
                question="What was a major operational weakness of Network and Hierarchical data models?",
                options=[
                    "They relied on physical disk pointers, making queries and schema modifications brittle and complex",
                    "They were too fast for computers to handle",
                    "They only ran on modern cloud providers",
                    "They could only store text in German"
                ],
                correct_answer="They relied on physical disk pointers, making queries and schema modifications brittle and complex",
                explanation="Modifying record layouts or relations required restructuring pointer chains throughout the database."
            ),
            QuizQuestionBlueprint(
                question="How does the Relational model represent many-to-many (M:N) relationships between entities?",
                options=[
                    "Through a junction/bridge table containing foreign keys to both entity tables",
                    "By storing all data in a single column separated by semicolons",
                    "By duplicating the entire database server",
                    "Many-to-many relationships are impossible in relational databases"
                ],
                correct_answer="Through a junction/bridge table containing foreign keys to both entity tables",
                explanation="A junction (or bridge) table decomposes many-to-many relationships into two clean 1-to-many relations."
            ),
            QuizQuestionBlueprint(
                question="What does 'data independence' mean in the relational database model?",
                options=[
                    "Logical application queries are separated from how physical bytes and files are organized on disk",
                    "Data files can run without an operating system",
                    "The database does not require electricity",
                    "Columns operate without any data types"
                ],
                correct_answer="Logical application queries are separated from how physical bytes and files are organized on disk",
                explanation="Data independence allows changing physical storage or indexes without rewriting application SQL queries."
            ),
            QuizQuestionBlueprint(
                question="Which database query language is declarative, telling the engine *what* to get rather than *how* to loop?",
                options=[
                    "SQL (Structured Query Language)",
                    "C Assembly",
                    "Machine Code",
                    "BASH script"
                ],
                correct_answer="SQL (Structured Query Language)",
                explanation="SQL is a declarative language: you specify the desired output set and the database engine plans execution."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 3
    # -------------------------------------------------------------
    DayBlueprint(
        order=3,
        title="Day 3: Tables, Rows & Columns (Tuples & Attributes)",
        concept="Deconstructing relational schema anatomy: Relations (Tables), Tuples (Rows), Attributes (Columns), and Domains",
        analogy="Think of a database table like an airline passenger manifest. The whole manifest clipboard is the 'Relation' (Table). Each horizontal line on the paper represents an individual passenger (Tuple / Row). Each vertical column lists a specific detail like Passport Number, Seat Number, or Meal Choice (Attribute / Column). The rule that seats must be letters A-F and numbers 1-35 is the 'Domain'!",
        theory_sections=[
            {
                "heading": "Relational Terminology vs Everyday Database Terms",
                "body": "In relational database theory: a **Relation** is a table, an **Attribute** is a column with a named data type, a **Tuple** is an individual row (record), the **Degree** (or Arity) is the total number of columns, and the **Cardinality** is the total number of rows. Each attribute draws values from a defined **Domain** (permitted data types and constraints)."
            },
            {
                "heading": "Properties of Valid Relations",
                "body": "Formal relational rules state that: (1) Every cell must contain an atomic (indivisible) value (1NF foundation); (2) Column order does not matter; (3) Row order does not matter; and (4) Each row must be uniquely identifiable (no exact duplicate rows allowed)."
            }
        ],
        code_snippets=[
            {
                "title": "Defining Attributes and Data Domains in SQL",
                "language": "sql",
                "code": "CREATE TABLE students (\n    student_id INT PRIMARY KEY,         -- Unique integer identifier\n    first_name VARCHAR(50) NOT NULL,   -- String attribute (max 50 chars)\n    gpa DECIMAL(3, 2) CHECK (gpa >= 0.0 AND gpa <= 4.0), -- Domain constrained float\n    enrolled_date DATE NOT NULL        -- Date domain\n);",
                "explanation": "Each column represents an attribute with a strictly enforced domain and constraint boundary."
            },
            {
                "title": "Inserting Tuples (Rows) into the Relation",
                "language": "sql",
                "code": "-- Inserting 3 distinct tuples into the students relation\nINSERT INTO students (student_id, first_name, gpa, enrolled_date)\nVALUES \n    (101, 'Zainab', 3.85, '2026-09-01'),\n    (102, 'Bilal', 3.40, '2026-09-01'),\n    (103, 'Ayesha', 3.95, '2026-09-15');",
                "explanation": "Each tuple represents a complete entity record adhering to the attribute structure of the table."
            },
            {
                "title": "Inspecting Degree and Cardinality via SQL Information Schema",
                "language": "sql",
                "code": "-- Cardinality: Count of tuples (rows)\nSELECT COUNT(*) AS cardinality FROM students;\n\n-- Degree: Count of attributes (columns)\nSELECT COUNT(*) AS degree \nFROM information_schema.columns \nWHERE table_name = 'students';",
                "explanation": "Cardinality measures total rows in the relation; degree measures total columns in the schema."
            },
            {
                "title": "Enforcing Atomic Domain Values (First Normal Form Principle)",
                "language": "sql",
                "code": "-- BAD: Violates atomicity (multiple phone numbers in a single column)\n-- INSERT INTO students VALUES (104, 'Hamza', '0300-111, 0321-222');\n\n-- GOOD: Separate attribute or 1:N phone records\nCREATE TABLE student_phones (\n    id SERIAL PRIMARY KEY,\n    student_id INT REFERENCES students(student_id),\n    phone_number VARCHAR(20) NOT NULL\n);",
                "explanation": "Relational attributes must be atomic; multi-valued fields should be normalized into separate relations."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Relation Cardinality and Degree Calculator",
            description="Write a Python function `measure_relation(table_data: list[dict]) -> tuple[int, int]` that takes a list of row dictionaries and returns a tuple `(cardinality, degree)`. If the table has no rows, degree is 0.",
            starter_code="def measure_relation(table_data: list[dict]) -> tuple[int, int]:\n    # Return (cardinality, degree)\n    pass",
            solution_code="def measure_relation(table_data: list[dict]) -> tuple[int, int]:\n    cardinality = len(table_data)\n    degree = len(table_data[0].keys()) if cardinality > 0 else 0\n    return (cardinality, degree)",
            expected_output="measure_relation([{'id': 1, 'name': 'A'}, {'id': 2, 'name': 'B'}]) == (2, 2)"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="In formal database theory, what is a 'Tuple'?",
                options=[
                    "A single row (record) in a table",
                    "A column header name",
                    "The database connection password",
                    "A physical storage partition on a hard drive"
                ],
                correct_answer="A single row (record) in a table",
                explanation="In Codd's relational algebra, a tuple corresponds to a row or record in a table."
            ),
            QuizQuestionBlueprint(
                question="What is meant by the 'Degree' (or Arity) of a relation?",
                options=[
                    "The total number of columns (attributes) in the table",
                    "The total number of rows in the table",
                    "The temperature of the server room",
                    "The number of index files attached to the table"
                ],
                correct_answer="The total number of columns (attributes) in the table",
                explanation="Degree is the number of attributes (columns); Cardinality is the number of tuples (rows)."
            ),
            QuizQuestionBlueprint(
                question="What is an Attribute Domain in a database schema?",
                options=[
                    "The set of permissible values and data types allowed for that specific column",
                    "The website URL where the database is hosted",
                    "The email domain of the database administrator",
                    "The hard disk sector size"
                ],
                correct_answer="The set of permissible values and data types allowed for that specific column",
                explanation="A domain defines valid data types, sizes, and value boundaries for an attribute."
            ),
            QuizQuestionBlueprint(
                question="Does row ordering or column ordering affect the logical meaning of a relational table?",
                options=[
                    "No, mathematically relations are unordered sets of tuples and attributes",
                    "Yes, rows must always be sorted alphabetically by law",
                    "Yes, reversing column order erases all data",
                    "Only on Windows servers"
                ],
                correct_answer="No, mathematically relations are unordered sets of tuples and attributes",
                explanation="A relation is a mathematical set; tuples have no inherent order until sorted with an ORDER BY clause."
            ),
            QuizQuestionBlueprint(
                question="What does 'atomic value' mean in a relational database cell?",
                options=[
                    "A single, indivisible piece of data (e.g. one phone number instead of a comma-separated list)",
                    "A value created using nuclear physics",
                    "A number that cannot be divided by two",
                    "A password that never expires"
                ],
                correct_answer="A single, indivisible piece of data (e.g. one phone number instead of a comma-separated list)",
                explanation="Atomicity in 1NF means each attribute cell holds exactly one single discrete value."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 4
    # -------------------------------------------------------------
    DayBlueprint(
        order=4,
        title="Day 4: Database Keys - Primary, Foreign, Candidate & Composite",
        concept="Mastering entity identification: Super Keys, Candidate Keys, Primary Keys, Composite Keys, Alternate Keys, and Foreign Keys",
        analogy="Think of database keys like identifying citizens in a country. Your fingerprint or National ID Number (CNIC / SSN) is your Primary Key—it uniquely identifies you and can never belong to anyone else. Your passport number and driver's license are Candidate Keys (eligible identifiers). When you register your car, the DMV links your vehicle to your ID number as a Foreign Key!",
        theory_sections=[
            {
                "heading": "The Hierarchy of Keys",
                "body": "A **Super Key** is any set of one or more columns that uniquely identifies a row. A **Candidate Key** is a minimal Super Key with no redundant attributes. From the candidate keys, the database designer selects one **Primary Key** (which must be unique and NOT NULL). The remaining candidate keys become **Alternate Keys** (often enforced with UNIQUE constraints)."
            },
            {
                "heading": "Composite Keys & Foreign Key Constraints",
                "body": "A **Composite Key** consists of two or more columns that together form a unique identifier (common in many-to-many junction tables like `order_id + product_id`). A **Foreign Key** is an attribute in a child table that points to the primary key of a parent table, guaranteeing referential integrity."
            }
        ],
        code_snippets=[
            {
                "title": "Declaring Primary Key and Candidate Alternate Keys",
                "language": "sql",
                "code": "CREATE TABLE users (\n    user_id SERIAL PRIMARY KEY,              -- Chosen Primary Key\n    cnic_number VARCHAR(15) UNIQUE NOT NULL, -- Candidate / Alternate Key\n    email VARCHAR(100) UNIQUE NOT NULL,      -- Candidate / Alternate Key\n    full_name VARCHAR(100) NOT NULL\n);",
                "explanation": "Here user_id is the primary key, while cnic_number and email are alternate candidate keys."
            },
            {
                "title": "Creating a Composite Primary Key in a Junction Table",
                "language": "sql",
                "code": "CREATE TABLE enrollment (\n    course_id INT NOT NULL,\n    student_id INT NOT NULL,\n    semester VARCHAR(10) NOT NULL,\n    grade CHAR(2),\n    -- Neither course_id nor student_id alone is unique;\n    -- their combination forms the Composite Primary Key\n    PRIMARY KEY (course_id, student_id, semester)\n);",
                "explanation": "A composite key combines multiple columns to enforce uniqueness across grouped attributes."
            },
            {
                "title": "Establishing Foreign Key with Referential Actions (CASCADE, SET NULL)",
                "language": "sql",
                "code": "CREATE TABLE course_materials (\n    material_id SERIAL PRIMARY KEY,\n    course_id INT NOT NULL,\n    title VARCHAR(200) NOT NULL,\n    CONSTRAINT fk_course\n        FOREIGN KEY (course_id)\n        REFERENCES courses(id)\n        ON DELETE CASCADE     -- When parent course is deleted, delete its materials\n        ON UPDATE CASCADE\n);",
                "explanation": "Foreign keys guarantee referential integrity and dictate cascade behaviors upon updates or deletions."
            },
            {
                "title": "Querying Across Parent-Child Key Relationships",
                "language": "sql",
                "code": "SELECT \n    u.full_name,\n    o.order_number,\n    o.total_amount\nFROM users u\nJOIN orders o ON u.user_id = o.user_id -- Joining PK to FK\nWHERE u.user_id = 42;",
                "explanation": "Foreign keys provide the logical glue for joining related tables efficiently in relational queries."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Candidate Key Redundancy Checker",
            description="Write a Python function `is_minimal_candidate_key(key_attrs: set, super_keys: list[set]) -> bool` that verifies whether `key_attrs` is minimal (no proper subset of `key_attrs` exists in `super_keys`).",
            starter_code="def is_minimal_candidate_key(key_attrs: set, super_keys: list[set]) -> bool:\n    # Return False if any proper subset of key_attrs is in super_keys\n    pass",
            solution_code="def is_minimal_candidate_key(key_attrs: set, super_keys: list[set]) -> bool:\n    for other in super_keys:\n        if other < key_attrs:  # Proper subset check\n            return False\n    return True",
            expected_output="is_minimal_candidate_key({'id', 'email'}, [{'id'}]) == False, is_minimal_candidate_key({'id'}, [{'id'}]) == True"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the definition of a Candidate Key in relational database theory?",
                options=[
                    "A minimal super key containing no extraneous attributes that can uniquely identify a row",
                    "A key that can contain duplicate and NULL values",
                    "A key generated by user passwords",
                    "A foreign key that points to another server"
                ],
                correct_answer="A minimal super key containing no extraneous attributes that can uniquely identify a row",
                explanation="A candidate key is a minimal super key; removing any column from it breaks uniqueness."
            ),
            QuizQuestionBlueprint(
                question="Can a Primary Key column contain NULL values in standard SQL?",
                options=[
                    "No, a Primary Key must be strictly unique and NOT NULL",
                    "Yes, up to 50% of the rows can be NULL",
                    "Yes, if the database admin permits it",
                    "Only on weekends"
                ],
                correct_answer="No, a Primary Key must be strictly unique and NOT NULL",
                explanation="By relational rules and SQL standard, primary key attributes cannot contain NULL values."
            ),
            QuizQuestionBlueprint(
                question="What is a Composite Key?",
                options=[
                    "A primary key composed of two or more columns that together guarantee row uniqueness",
                    "A key imported from an Excel file",
                    "A key that stores images instead of numbers",
                    "An encrypted password string"
                ],
                correct_answer="A primary key composed of two or more columns that together guarantee row uniqueness",
                explanation="When no single column is unique, multiple columns combine to form a composite key."
            ),
            QuizQuestionBlueprint(
                question="What does the `ON DELETE CASCADE` clause do when attached to a Foreign Key constraint?",
                options=[
                    "Automatically deletes child rows when the referenced parent row is deleted",
                    "Prevents the parent row from ever being deleted",
                    "Sets the child foreign key value to 0",
                    "Sends an email alert to the database user"
                ],
                correct_answer="Automatically deletes child rows when the referenced parent row is deleted",
                explanation="ON DELETE CASCADE deletes dependent child records automatically, preventing orphaned rows."
            ),
            QuizQuestionBlueprint(
                question="What is an Alternate Key?",
                options=[
                    "Any candidate key that was not chosen as the primary key",
                    "A backup hard drive",
                    "A secondary database user account",
                    "A column that stores temporary calculations"
                ],
                correct_answer="Any candidate key that was not chosen as the primary key",
                explanation="Candidate keys that are not selected as the primary key are known as alternate keys."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 5
    # -------------------------------------------------------------
    DayBlueprint(
        order=5,
        title="Day 5: DDL - Data Definition Language (CREATE, ALTER, DROP, TRUNCATE)",
        concept="Defining, modifying, and destroying database structure and schema objects using DDL statements",
        analogy="Think of DDL like blueprints and demolition equipment on a construction site. DDL does not move furniture inside the rooms; DDL is the architect pouring concrete foundations (`CREATE TABLE`), adding a new balcony (`ALTER TABLE ADD COLUMN`), wiping out all carpets instantly (`TRUNCATE TABLE`), or demolishing the entire building to the ground (`DROP TABLE`)!",
        theory_sections=[
            {
                "heading": "Understanding DDL vs Data Manipulation",
                "body": "Data Definition Language (DDL) commands affect the database catalog and metadata rather than individual data rows. DDL statements include `CREATE`, `ALTER`, `DROP`, `TRUNCATE`, and `RENAME`. In many databases, DDL commands implicitly commit ongoing transactions."
            },
            {
                "heading": "DROP vs TRUNCATE vs DELETE",
                "body": "Understanding the difference is critical: `DROP TABLE` deletes the data rows AND completely destroys the table definition from schema catalog. `TRUNCATE TABLE` empties all rows at high speed by deallocating storage pages while keeping the table structure intact. `DELETE` (which is DML) deletes rows one-by-one with transaction undo logging."
            }
        ],
        code_snippets=[
            {
                "title": "Creating a Table with Constraints (CREATE TABLE)",
                "language": "sql",
                "code": "CREATE TABLE products (\n    product_id SERIAL PRIMARY KEY,\n    sku VARCHAR(30) UNIQUE NOT NULL,\n    title VARCHAR(150) NOT NULL,\n    price DECIMAL(10, 2) NOT NULL DEFAULT 0.00,\n    is_active BOOLEAN DEFAULT TRUE,\n    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP\n);",
                "explanation": "CREATE defines the table name, column attributes, default values, and primary key constraints."
            },
            {
                "title": "Modifying Existing Table Architecture (ALTER TABLE)",
                "language": "sql",
                "code": "-- Add a new column\nALTER TABLE products ADD COLUMN stock_quantity INT NOT NULL DEFAULT 0;\n\n-- Modify an existing column data type\nALTER TABLE products ALTER COLUMN title TYPE VARCHAR(255);\n\n-- Drop a column safely\nALTER TABLE products DROP COLUMN is_active;",
                "explanation": "ALTER TABLE allows evolving schemas in production without losing existing data."
            },
            {
                "title": "Fast Deallocation with TRUNCATE TABLE",
                "language": "sql",
                "code": "-- Empties all records instantaneously and resets auto-increment sequence\nTRUNCATE TABLE products RESTART IDENTITY CASCADE;",
                "explanation": "TRUNCATE is a DDL command that deallocates storage blocks, making it vastly faster than row-by-row DELETE."
            },
            {
                "title": "Removing Schema Objects Completely (DROP TABLE)",
                "language": "sql",
                "code": "-- Safely drops table only if it exists, preventing script errors\nDROP TABLE IF EXISTS products CASCADE;",
                "explanation": "DROP TABLE obliterates both table data and schema definitions from the database dictionary."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="DDL SQL Generator for Table Definition",
            description="Write a Python function `generate_create_table_sql(table_name: str, columns: dict[str, str]) -> str` that produces a valid `CREATE TABLE <name> (<col> <type>, ...);` SQL string.",
            starter_code="def generate_create_table_sql(table_name: str, columns: dict[str, str]) -> str:\n    # Generate CREATE TABLE SQL statement\n    pass",
            solution_code="def generate_create_table_sql(table_name: str, columns: dict[str, str]) -> str:\n    col_defs = [f\"{col} {dtype}\" for col, dtype in columns.items()]\n    return f\"CREATE TABLE {table_name} ({', '.join(col_defs)});\"",
            expected_output="generate_create_table_sql('logs', {'id': 'INT PRIMARY KEY', 'msg': 'TEXT'}) == 'CREATE TABLE logs (id INT PRIMARY KEY, msg TEXT);'"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Which category of SQL commands does `CREATE TABLE` and `ALTER TABLE` belong to?",
                options=[
                    "DDL (Data Definition Language)",
                    "DML (Data Manipulation Language)",
                    "DCL (Data Control Language)",
                    "TCL (Transaction Control Language)"
                ],
                correct_answer="DDL (Data Definition Language)",
                explanation="Commands that define or alter database schema structures are categorized as DDL."
            ),
            QuizQuestionBlueprint(
                question="What is the critical difference between `TRUNCATE TABLE` and `DROP TABLE`?",
                options=[
                    "TRUNCATE removes all rows but preserves table structure; DROP removes all rows AND destroys the table structure",
                    "TRUNCATE deletes the database server while DROP only deletes one row",
                    "There is no difference; they are exact aliases",
                    "DROP only works on numbers"
                ],
                correct_answer="TRUNCATE removes all rows but preserves table structure; DROP removes all rows AND destroys the table structure",
                explanation="TRUNCATE empties the relation but leaves the schema intact; DROP removes the relation definition entirely."
            ),
            QuizQuestionBlueprint(
                question="Why is `TRUNCATE TABLE` typically much faster than `DELETE FROM table`?",
                options=[
                    "It deallocates the entire data pages at once rather than logging each row deletion individually in transaction undo logs",
                    "It compresses the rows into a zip file",
                    "It only deletes the first 5 rows",
                    "It runs on the client device"
                ],
                correct_answer="It deallocates the entire data pages at once rather than logging each row deletion individually in transaction undo logs",
                explanation="TRUNCATE deallocates data pages directly with minimal logging, bypassing row-by-row deletion locks."
            ),
            QuizQuestionBlueprint(
                question="Which DDL command adds a new column `phone` to an existing table `customers`?",
                options=[
                    "ALTER TABLE customers ADD COLUMN phone VARCHAR(20);",
                    "UPDATE TABLE customers INSERT phone VARCHAR(20);",
                    "INSERT INTO customers COLUMN phone VARCHAR(20);",
                    "CREATE COLUMN phone ON customers;"
                ],
                correct_answer="ALTER TABLE customers ADD COLUMN phone VARCHAR(20);",
                explanation="ALTER TABLE table_name ADD COLUMN column_name type is the standard SQL DDL syntax."
            ),
            QuizQuestionBlueprint(
                question="What does the `IF EXISTS` clause prevent when running `DROP TABLE IF EXISTS orders;`?",
                options=[
                    "It prevents the database engine from throwing an error if the table does not exist",
                    "It prevents users from deleting data",
                    "It locks the database permanently",
                    "It forces all users to log out"
                ],
                correct_answer="It prevents the database engine from throwing an error if the table does not exist",
                explanation="IF EXISTS makes scripts idempotent: if the table does not exist, it issues a quiet notice instead of halting execution."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 6
    # -------------------------------------------------------------
    DayBlueprint(
        order=6,
        title="Day 6: DML - Data Manipulation Language (INSERT, UPDATE, DELETE)",
        concept="Manipulating data records inside tables: single/batch inserts, upserts, conditional updates, and transactional deletes",
        analogy="If DDL is building a high-tech robotic warehouse, DML is the crew stocking boxes on the shelves (`INSERT`), sticking price tags or new addresses on existing boxes (`UPDATE`), or throwing damaged boxes into the recycling bin (`DELETE`). The warehouse structure stays the same—only the contents inside change!",
        theory_sections=[
            {
                "heading": "The Core Data Manipulation Operations",
                "body": "DML statements (`INSERT`, `UPDATE`, `DELETE`) operate on table rows. Unlike DDL, DML modifications run within active transaction scopes and can be committed or rolled back. Forgetting a `WHERE` clause on an `UPDATE` or `DELETE` statement is a notorious developer mistake that affects every row in the entire table."
            },
            {
                "heading": "Safe Updates and the UPSERT Pattern",
                "body": "Modern databases provide atomic 'upsert' capabilities (e.g. `INSERT ... ON CONFLICT DO UPDATE` in PostgreSQL or `ON DUPLICATE KEY UPDATE` in MySQL). This allows developers to insert a new row or seamlessly update existing columns if a unique key collision occurs, eliminating race conditions."
            }
        ],
        code_snippets=[
            {
                "title": "Single and Multi-Row Batch INSERT",
                "language": "sql",
                "code": "-- Inserting multiple tuples in a single atomic SQL statement\nINSERT INTO employees (name, department, salary)\nVALUES \n    ('Kashif', 'Engineering', 95000.00),\n    ('Fatima', 'Marketing', 78000.00),\n    ('Usman', 'Design', 82000.00)\nRETURNING id, name, created_at; -- Returns newly generated IDs",
                "explanation": "Batch inserting multiple rows in a single statement minimizes database network roundtrips."
            },
            {
                "title": "Safe Targeted UPDATE with WHERE Clause",
                "language": "sql",
                "code": "-- Increase salary by 10% specifically for Engineering department\nUPDATE employees\nSET \n    salary = salary * 1.10,\n    updated_at = CURRENT_TIMESTAMP\nWHERE department = 'Engineering';\n\n-- CRITICAL: Always verify WHERE clause to avoid mass updates!",
                "explanation": "The WHERE clause restricts modifications to matching rows only."
            },
            {
                "title": "Targeted DELETE vs Accidental Mass Deletion",
                "language": "sql",
                "code": "-- Deleting specific terminated employee records\nDELETE FROM employees\nWHERE status = 'terminated' AND termination_date < '2025-01-01';\n\n-- WARNING: Running 'DELETE FROM employees;' without WHERE deletes ALL rows!",
                "explanation": "DELETE removes tuples matching the criteria while keeping the table structure intact."
            },
            {
                "title": "Atomic UPSERT (INSERT ON CONFLICT)",
                "language": "sql",
                "code": "-- If user with email already exists, update login count instead of failing\nINSERT INTO user_logins (email, login_count, last_login)\nVALUES ('ali@hunar.app', 1, CURRENT_TIMESTAMP)\nON CONFLICT (email)\nDO UPDATE SET \n    login_count = user_logins.login_count + 1,\n    last_login = CURRENT_TIMESTAMP;",
                "explanation": "UPSERT prevents duplicate key exceptions by cleanly falling back to an update."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Safe SQL Update Query Generator",
            description="Write a Python function `build_update_query(table: str, updates: dict, where_col: str, where_val: str) -> str` that produces a parameterized SQL UPDATE statement. Raise a `ValueError` if `where_col` is empty (to protect against accidental mass table updates).",
            starter_code="def build_update_query(table: str, updates: dict, where_col: str, where_val: str) -> str:\n    # Generate safe UPDATE SQL with mandatory WHERE condition\n    pass",
            solution_code="def build_update_query(table: str, updates: dict, where_col: str, where_val: str) -> str:\n    if not where_col or not where_col.strip():\n        raise ValueError('WHERE clause condition is mandatory for safety')\n    set_clause = ', '.join([f\"{k} = '{v}'\" for k, v in updates.items()])\n    return f\"UPDATE {table} SET {set_clause} WHERE {where_col} = '{where_val}';\"",
            expected_output="build_update_query('users', {'status': 'active'}, 'id', '42') == \"UPDATE users SET status = 'active' WHERE id = '42';\""
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What disastrous consequence occurs if an `UPDATE` statement is executed without a `WHERE` clause?",
                options=[
                    "Every single row in the entire table is updated with the new values",
                    "The database server crashes immediately",
                    "The query is rejected automatically by all SQL engines",
                    "Only the first row in the table is updated"
                ],
                correct_answer="Every single row in the entire table is updated with the new values",
                explanation="Without a WHERE filter, the UPDATE statement applies changes to all tuples in the table."
            ),
            QuizQuestionBlueprint(
                question="Which DML command adds new records into an existing table?",
                options=[
                    "INSERT INTO",
                    "CREATE ROW",
                    "ADD DATA",
                    "APPEND TO"
                ],
                correct_answer="INSERT INTO",
                explanation="INSERT INTO is standard SQL syntax to append new tuples into a relation."
            ),
            QuizQuestionBlueprint(
                question="What is an 'UPSERT' operation in modern relational databases?",
                options=[
                    "An atomic operation that inserts a row or updates it if a duplicate unique key is encountered",
                    "An update that converts all text to uppercase",
                    "A tool for uploading databases to cloud storage",
                    "A command that doubles the primary key values"
                ],
                correct_answer="An atomic operation that inserts a row or updates it if a duplicate unique key is encountered",
                explanation="UPSERT (ON CONFLICT DO UPDATE) avoids unique key errors by turning inserts into updates upon collisions."
            ),
            QuizQuestionBlueprint(
                question="What clause in PostgreSQL allows an `INSERT` statement to return generated serial IDs immediately?",
                options=[
                    "RETURNING",
                    "GIMME",
                    "OUTPUT_TO",
                    "FETCH_NEW"
                ],
                correct_answer="RETURNING",
                explanation="`INSERT INTO ... RETURNING id` returns newly created auto-generated keys directly without a second SELECT."
            ),
            QuizQuestionBlueprint(
                question="Can DML statements (`INSERT`, `UPDATE`, `DELETE`) be rolled back inside a transaction block?",
                options=[
                    "Yes, DML operations respect transaction boundaries and can be reversed with ROLLBACK",
                    "No, DML statements permanently modify disk bytes with no rollback possibility",
                    "Only INSERT can be rolled back, never UPDATE",
                    "Rollbacks are only available in NoSQL databases"
                ],
                correct_answer="Yes, DML operations respect transaction boundaries and can be reversed with ROLLBACK",
                explanation="DML operations are fully transactional and can be undone before COMMIT is called."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 7
    # -------------------------------------------------------------
    DayBlueprint(
        order=7,
        title="Day 7: DQL - Data Query Language (SELECT, WHERE, ORDER BY, LIMIT)",
        concept="Retrieving, filtering, sorting, and paginating relational data with precision using the SELECT query pipeline",
        analogy="Think of a SQL query like ordering from a master chef in a restaurant. You don't say 'cook everything in the fridge and put it in a bucket.' You say: 'Bring me chicken dishes (`SELECT`), only those under 500 calories (`WHERE`), put the cheapest ones first (`ORDER BY price ASC`), and just bring me the top 3 (`LIMIT 3`)!' DQL delivers exactly the plate you asked for.",
        theory_sections=[
            {
                "heading": "The Anatomy and Execution Order of a SELECT Query",
                "body": "Although developers write queries starting with `SELECT`, SQL engines execute clauses in a completely different logical order: (1) `FROM` & `JOIN` (identify tables), (2) `WHERE` (filter rows), (3) `SELECT` (pick columns and evaluate expressions), (4) `ORDER BY` (sort results), and (5) `LIMIT` / `OFFSET` (paginate output). Understanding this execution pipeline prevents common alias and scoping errors."
            },
            {
                "heading": "Sorting and Pagination Best Practices",
                "body": "Sorting using `ORDER BY` defaults to ascending (`ASC`), with descending (`DESC`) available for latest-first rankings. In high-traffic production apps, combining `LIMIT` and `OFFSET` for pagination can become slow on deep offsets (e.g. `OFFSET 100000`); modern designs often transition to keyset / cursor pagination."
            }
        ],
        code_snippets=[
            {
                "title": "Selecting Specific Columns and Renaming with Aliases",
                "language": "sql",
                "code": "-- Pick specific columns instead of SELECT * to conserve bandwidth & RAM\nSELECT \n    id AS customer_id,\n    first_name || ' ' || last_name AS full_name,\n    email,\n    created_at::DATE AS signup_date\nFROM customers;",
                "explanation": "Selecting explicit columns and using aliases produces clean, bandwidth-optimized result sets."
            },
            {
                "title": "Filtering with Compound Boolean Logic in WHERE",
                "language": "sql",
                "code": "SELECT product_name, price, stock_quantity\nFROM inventory\nWHERE (price >= 50.00 AND price <= 200.00)\n  AND stock_quantity > 0\n  AND is_discontinued = FALSE;",
                "explanation": "The WHERE clause filters out non-matching tuples before sorting and projection."
            },
            {
                "title": "Multi-Column Sorting with ORDER BY",
                "language": "sql",
                "code": "SELECT student_name, grade_level, gpa\nFROM students\nORDER BY \n    grade_level ASC,  -- First sort by grade (9, 10, 11...)\n    gpa DESC;         -- Within each grade, highest GPA first",
                "explanation": "ORDER BY can sort across multiple columns in varying directions."
            },
            {
                "title": "Pagination with LIMIT and OFFSET",
                "language": "sql",
                "code": "-- Page 3: 10 items per page (Skip first 20 records, take 10)\nSELECT id, title, price\nFROM books\nORDER BY id ASC\nLIMIT 10 OFFSET 20;",
                "explanation": "LIMIT restricts result size and OFFSET specifies the start point for standard UI pagination."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Pagination Offset Calculator",
            description="Write a Python function `get_pagination_clause(page: int, page_size: int) -> str` that calculates the appropriate `LIMIT <N> OFFSET <M>` string for 1-based page numbers. If page is less than 1, treat it as page 1.",
            starter_code="def get_pagination_clause(page: int, page_size: int) -> str:\n    # Return LIMIT and OFFSET clause string\n    pass",
            solution_code="def get_pagination_clause(page: int, page_size: int) -> str:\n    page = max(1, page)\n    offset = (page - 1) * page_size\n    return f\"LIMIT {page_size} OFFSET {offset}\"",
            expected_output="get_pagination_clause(1, 10) == 'LIMIT 10 OFFSET 0', get_pagination_clause(3, 15) == 'LIMIT 15 OFFSET 30'"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the logical execution order of clauses in a standard SELECT query?",
                options=[
                    "FROM -> WHERE -> SELECT -> ORDER BY -> LIMIT",
                    "SELECT -> FROM -> WHERE -> LIMIT -> ORDER BY",
                    "ORDER BY -> LIMIT -> WHERE -> SELECT -> FROM",
                    "WHERE -> SELECT -> FROM -> ORDER BY -> LIMIT"
                ],
                correct_answer="FROM -> WHERE -> SELECT -> ORDER BY -> LIMIT",
                explanation="The SQL engine first loads tables (FROM), filters rows (WHERE), evaluates projections (SELECT), sorts (ORDER BY), and clamps (LIMIT)."
            ),
            QuizQuestionBlueprint(
                question="Why is `SELECT *` discouraged in production web applications?",
                options=[
                    "It retrieves unnecessary columns, wasting network bandwidth, memory, and preventing index-only query optimizations",
                    "It is forbidden syntax and throws a runtime error",
                    "It automatically deletes unselected columns",
                    "It only returns the first 10 rows"
                ],
                correct_answer="It retrieves unnecessary columns, wasting network bandwidth, memory, and preventing index-only query optimizations",
                explanation="SELECT * fetches all data including heavy text/blob columns, increasing memory consumption and database I/O."
            ),
            QuizQuestionBlueprint(
                question="What is the default sort direction when using `ORDER BY column_name` without specifying ASC or DESC?",
                options=[
                    "ASC (Ascending, low to high / A to Z)",
                    "DESC (Descending, high to low)",
                    "Random shuffle",
                    "Alphabetical reversed"
                ],
                correct_answer="ASC (Ascending, low to high / A to Z)",
                explanation="Standard SQL defaults to ascending (ASC) order."
            ),
            QuizQuestionBlueprint(
                question="How do you calculate the `OFFSET` value for page number `P` with `N` items per page (1-indexed)?",
                options=[
                    "(P - 1) * N",
                    "P * N",
                    "P + N",
                    "N / P"
                ],
                correct_answer="(P - 1) * N",
                explanation="Page 1 has offset 0; Page 2 has offset (2-1)*N = N; Page 3 has offset 2N."
            ),
            QuizQuestionBlueprint(
                question="What keyword renames a column in the query output (e.g. `SELECT first_name ___ name`)?",
                options=[
                    "AS",
                    "LIKE",
                    "INTO",
                    "TO"
                ],
                correct_answer="AS",
                explanation="The `AS` keyword introduces an alias for columns or tables."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 8
    # -------------------------------------------------------------
    DayBlueprint(
        order=8,
        title="Day 8: Filtering & Operators (LIKE, IN, BETWEEN, AND, OR, NOT)",
        concept="Mastering SQL pattern matching, set membership, range boundaries, and NULL comparison predicates",
        analogy="Think of SQL filtering operators like airport security checkpoints. `AND` means you must have BOTH a ticket AND a passport to pass. `OR` means either a driver's license OR a national card is accepted. `IN` is checking if your flight destination is on a list of approved cities. `LIKE` is matching names that start with 'Smith%' on the passenger registry. `IS NULL` checks if the baggage tag was left blank!",
        theory_sections=[
            {
                "heading": "Pattern Matching with LIKE & ILIKE",
                "body": "The `LIKE` operator enables wildcard searches: `%` matches zero or more characters (e.g. `'A%'` matches any string starting with A), while `_` matches exactly one character. In PostgreSQL, `ILIKE` performs case-insensitive matching."
            },
            {
                "heading": "Set Membership, Ranges, and Three-Valued Logic (NULL)",
                "body": "The `IN` operator checks if an attribute matches any value in a defined set. `BETWEEN a AND b` checks inclusive ranges. Crucially, SQL uses Three-Valued Logic (`TRUE`, `FALSE`, `UNKNOWN`). Because `NULL` represents an unknown absence of value, writing `WHERE col = NULL` always evaluates to `UNKNOWN` (failing to match). You must use `IS NULL` or `IS NOT NULL`."
            }
        ],
        code_snippets=[
            {
                "title": "Wildcard String Pattern Matching with LIKE & ILIKE",
                "language": "sql",
                "code": "-- Match users whose email ends with @gmail.com\nSELECT id, email FROM users WHERE email LIKE '%@gmail.com';\n\n-- Case-insensitive search for names starting with 'muh'\nSELECT id, full_name FROM users WHERE full_name ILIKE 'muh%';\n\n-- Match 5-letter postal codes starting with '54'\nSELECT * FROM addresses WHERE postal_code LIKE '54___';",
                "explanation": "`%` matches any length; `_` matches a single character. ILIKE ignores uppercase/lowercase differences."
            },
            {
                "title": "Set Membership with IN and NOT IN",
                "language": "sql",
                "code": "-- Clean alternative to multiple OR conditions\nSELECT id, title, status\nFROM support_tickets\nWHERE status IN ('open', 'in_progress', 'pending_customer');\n\n-- Exclude specific administrative roles\nSELECT id, username FROM accounts WHERE role NOT IN ('superadmin', 'auditor');",
                "explanation": "`IN` evaluates set membership cleanly without chaining repetitive OR statements."
            },
            {
                "title": "Inclusive Range Queries with BETWEEN",
                "language": "sql",
                "code": "-- Inclusive range matching: equivalent to (age >= 18 AND age <= 35)\nSELECT user_id, age FROM profiles WHERE age BETWEEN 18 AND 35;\n\n-- Date range filtering\nSELECT order_id, total_amount \nFROM orders \nWHERE order_date BETWEEN '2026-01-01' AND '2026-03-31';",
                "explanation": "BETWEEN checks if a value falls inclusively between lower and upper bounds."
            },
            {
                "title": "The Golden Rule of NULL Comparison: IS NULL vs = NULL",
                "language": "sql",
                "code": "-- WRONG: This query will NEVER return any rows in SQL!\n-- SELECT * FROM employees WHERE phone_number = NULL;\n\n-- CORRECT: Always use IS NULL or IS NOT NULL\nSELECT id, name \nFROM employees \nWHERE phone_number IS NULL OR phone_number = '';",
                "explanation": "NULL cannot equal anything (even another NULL). Always use `IS NULL` or `IS NOT NULL`."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="SQL LIKE Pattern Matcher",
            description="Write a Python function `matches_sql_like(text: str, pattern: str) -> bool` that simulates SQL `LIKE` wildcards `%` (any characters) and `_` (single character).",
            starter_code="def matches_sql_like(text: str, pattern: str) -> bool:\n    # Simulate SQL LIKE matching (% and _)\n    pass",
            solution_code="import re\n\ndef matches_sql_like(text: str, pattern: str) -> bool:\n    # Escape regex characters except % and _\n    regex_pattern = '^' + re.escape(pattern).replace('\\%', '.*').replace('\\_', '.') + '$'\n    return bool(re.match(regex_pattern, text))",
            expected_output="matches_sql_like('karachi_city', 'karachi%') == True, matches_sql_like('abc', 'a_c') == True"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Why does the query `SELECT * FROM users WHERE deleted_at = NULL;` fail to return rows with NULL values?",
                options=[
                    "Because NULL represents an unknown value; any equality comparison with NULL evaluates to UNKNOWN (never TRUE)",
                    "Because NULL is not a valid SQL keyword",
                    "Because deleted_at is a reserved system column",
                    "Because the query must be written in uppercase"
                ],
                correct_answer="Because NULL represents an unknown value; any equality comparison with NULL evaluates to UNKNOWN (never TRUE)",
                explanation="In SQL's three-valued logic, `NULL = NULL` is UNKNOWN. To check for null values, use `IS NULL`."
            ),
            QuizQuestionBlueprint(
                question="What wildcard character in SQL `LIKE` matches exactly one single character?",
                options=[
                    "_ (Underscore)",
                    "% (Percent)",
                    "* (Asterisk)",
                    "? (Question mark)"
                ],
                correct_answer="_ (Underscore)",
                explanation="Underscore `_` matches exactly one character; percent `%` matches zero or more characters."
            ),
            QuizQuestionBlueprint(
                question="Is the range in `WHERE price BETWEEN 10 AND 50` inclusive or exclusive?",
                options=[
                    "Inclusive (it includes both 10 and 50)",
                    "Exclusive (it only matches 11 to 49)",
                    "Includes 10 but excludes 50",
                    "Excludes 10 but includes 50"
                ],
                correct_answer="Inclusive (it includes both 10 and 50)",
                explanation="SQL BETWEEN is inclusive: `BETWEEN 10 AND 50` is identical to `>= 10 AND <= 50`."
            ),
            QuizQuestionBlueprint(
                question="Which operator tests whether a value exists inside a comma-separated list of candidate values?",
                options=[
                    "IN",
                    "EXISTS_IN",
                    "MATCHES",
                    "WITHIN"
                ],
                correct_answer="IN",
                explanation="The `IN` operator tests for set membership against a list or subquery."
            ),
            QuizQuestionBlueprint(
                question="What operator performs case-insensitive LIKE pattern matching in PostgreSQL?",
                options=[
                    "ILIKE",
                    "CASE_LIKE",
                    "CLIKES",
                    "NLIKE"
                ],
                correct_answer="ILIKE",
                explanation="`ILIKE` is PostgreSQL's extension for case-insensitive pattern matching."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 9
    # -------------------------------------------------------------
    DayBlueprint(
        order=9,
        title="Day 9 (Project): Aggregation & Grouping - Basic School Database",
        concept="Calculating summary statistics using COUNT, SUM, AVG, MIN, MAX, GROUP BY, and HAVING in a complete school metrics database",
        analogy="Think of SQL aggregation like a school principal reviewing exam scores. Instead of reading all 500 individual student test papers, the principal asks the department heads: 'Group the papers by classroom (`GROUP BY classroom`), calculate the average test score for each room (`AVG(score)`), and only report classrooms where the average score is under 60% so we can send tutors (`HAVING AVG(score) < 60`)!'",
        theory_sections=[
            {
                "heading": "Aggregate Functions & Grouping Buckets",
                "body": "Aggregate functions (`COUNT`, `SUM`, `AVG`, `MIN`, `MAX`) collapse thousands of individual rows into summary metrics. When combined with `GROUP BY`, rows sharing identical values in specified columns are grouped into distinct buckets, and the aggregate function computes a result per bucket."
            },
            {
                "heading": "The Crucial Difference: WHERE vs HAVING",
                "body": "A classic interview question: `WHERE` filters individual raw rows BEFORE aggregation occurs; `HAVING` filters aggregated group summaries AFTER `GROUP BY` calculation. For instance, filtering out absent students uses `WHERE status = 'present'`, while filtering classes with more than 30 enrolled students requires `HAVING COUNT(*) > 30`."
            }
        ],
        code_snippets=[
            {
                "title": "School Database Schema Setup (SchoolDB.sql)",
                "language": "sql",
                "code": "CREATE TABLE students (\n    student_id SERIAL PRIMARY KEY,\n    name VARCHAR(50) NOT NULL,\n    grade_level INT NOT NULL,\n    enrollment_status VARCHAR(20) DEFAULT 'active'\n);\n\nCREATE TABLE exam_scores (\n    score_id SERIAL PRIMARY KEY,\n    student_id INT REFERENCES students(student_id),\n    subject VARCHAR(50) NOT NULL,\n    score DECIMAL(5, 2) NOT NULL\n);",
                "explanation": "Creates relational tables for students and their exam test scores across subjects."
            },
            {
                "title": "Calculating Grade-Level Statistics with GROUP BY",
                "language": "sql",
                "code": "SELECT \n    grade_level,\n    COUNT(*) AS total_students,\n    COUNT(CASE WHEN enrollment_status = 'active' THEN 1 END) AS active_students\nFROM students\nGROUP BY grade_level\nORDER BY grade_level ASC;",
                "explanation": "Groups students by their grade level and calculates counts per educational tier."
            },
            {
                "title": "Subject Performance Report with HAVING Filter",
                "language": "sql",
                "code": "SELECT \n    subject,\n    COUNT(*) AS exams_taken,\n    ROUND(AVG(score), 2) AS average_score,\n    MIN(score) AS lowest_score,\n    MAX(score) AS highest_score\nFROM exam_scores\nGROUP BY subject\nHAVING AVG(score) >= 70.00 -- Only include high-performing subjects\nORDER BY average_score DESC;",
                "explanation": "HAVING filters aggregated summary buckets, keeping only subjects with an average score of 70% or higher."
            },
            {
                "title": "Combining WHERE and HAVING in a Single Analytical Query",
                "language": "sql",
                "code": "SELECT \n    s.grade_level,\n    e.subject,\n    ROUND(AVG(e.score), 1) AS avg_score\nFROM students s\nJOIN exam_scores e ON s.student_id = e.student_id\nWHERE s.enrollment_status = 'active'  -- WHERE filters individual rows first\nGROUP BY s.grade_level, e.subject\nHAVING AVG(e.score) < 65.0           -- HAVING filters groups needing improvement\nORDER BY avg_score ASC;",
                "explanation": "Demonstrates the complete pipeline: join tables, filter raw rows with WHERE, group, and filter summaries with HAVING."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="SQL Average Aggregator Simulator",
            description="Write a Python function `calculate_group_averages(records: list[dict], group_key: str, val_key: str) -> dict[str, float]` that groups dictionaries by `group_key` and computes the average of `val_key`, rounded to 2 decimals.",
            starter_code="def calculate_group_averages(records: list[dict], group_key: str, val_key: str) -> dict[str, float]:\n    # Group records and calculate averages\n    pass",
            solution_code="def calculate_group_averages(records: list[dict], group_key: str, val_key: str) -> dict[str, float]:\n    groups = {}\n    for r in records:\n        k = str(r[group_key])\n        groups.setdefault(k, []).append(r[val_key])\n    return {k: round(sum(vals) / len(vals), 2) for k, vals in groups.items()}",
            expected_output="calculate_group_averages([{'dept': 'CS', 'score': 80}, {'dept': 'CS', 'score': 90}], 'dept', 'score') == {'CS': 85.0}"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the key difference between the `WHERE` and `HAVING` clauses in SQL?",
                options=[
                    "`WHERE` filters rows before grouping; `HAVING` filters aggregated group buckets after GROUP BY",
                    "`WHERE` only works on numbers; `HAVING` only works on text",
                    "`WHERE` and `HAVING` are interchangeable synonyms",
                    "`HAVING` can only be used on primary key columns"
                ],
                correct_answer="`WHERE` filters rows before grouping; `HAVING` filters aggregated group buckets after GROUP BY",
                explanation="WHERE filters individual rows prior to aggregation; HAVING filters post-aggregation bucket metrics."
            ),
            QuizQuestionBlueprint(
                question="What does `COUNT(*)` return versus `COUNT(column_name)`?",
                options=[
                    "`COUNT(*)` counts all rows including NULLs; `COUNT(column_name)` only counts rows where column_name is NOT NULL",
                    "`COUNT(*)` multiplies all values; `COUNT(col)` divides them",
                    "`COUNT(*)` deletes the rows after counting",
                    "There is no difference in any database"
                ],
                correct_answer="`COUNT(*)` counts all rows including NULLs; `COUNT(column_name)` only counts rows where column_name is NOT NULL",
                explanation="COUNT(column) ignores null entries, whereas COUNT(*) counts total row occurrences."
            ),
            QuizQuestionBlueprint(
                question="What happens if you include a non-aggregated column in `SELECT` that is NOT in the `GROUP BY` clause?",
                options=[
                    "The SQL engine throws an error because it cannot determine which row's value to display for the group",
                    "The database picks a random value from the internet",
                    "The entire table is wiped clean",
                    "The column value is automatically converted to zero"
                ],
                correct_answer="The SQL engine throws an error because it cannot determine which row's value to display for the group",
                explanation="Standard SQL requires every non-aggregate column in the SELECT list to appear in the GROUP BY clause."
            ),
            QuizQuestionBlueprint(
                question="Which aggregate function calculates the arithmetic mean of a numeric column?",
                options=[
                    "AVG()",
                    "MEAN()",
                    "AVERAGE()",
                    "CALC_MID()"
                ],
                correct_answer="AVG()",
                explanation="`AVG()` is the standard ANSI SQL function for calculating arithmetic means."
            ),
            QuizQuestionBlueprint(
                question="Can multiple columns be specified in a single `GROUP BY` clause (e.g. `GROUP BY department, job_title`)?",
                options=[
                    "Yes, it groups rows by unique combinations of both columns",
                    "No, only one column can ever be grouped at a time",
                    "Only on MySQL 5.5",
                    "It causes an infinite loop in the database engine"
                ],
                correct_answer="Yes, it groups rows by unique combinations of both columns",
                explanation="Multi-column GROUP BY partitions rows into sub-buckets based on unique combinations of all specified columns."
            )
        ],
        is_project_day=True,
        project_name="Basic School Database Analytics Project"
    ),

    # -------------------------------------------------------------
    # DAY 10
    # -------------------------------------------------------------
    DayBlueprint(
        order=10,
        title="Day 10: ER Diagrams (Entity-Relationship Visual Blueprints)",
        concept="Visualizing relational database architectures: Entities, Attributes, Relationships, Cardinality, and Crow's Foot Notation",
        analogy="Think of an ER Diagram like an architectural floor plan for a skyscraper. Before bricklayers pour a single pound of concrete or carpenters assemble wooden beams (running `CREATE TABLE` scripts in SQL), the architect draws blueprints showing rooms (Entities), door dimensions (Attributes), and corridors connecting rooms (Relationships). If you skip the blueprint, you end up with stairs that lead into solid walls!",
        theory_sections=[
            {
                "heading": "Core Components of Entity-Relationship Modeling",
                "body": "In ER modeling pioneered by Peter Chen: an **Entity** is a real-world object (e.g. User, Order, Course) represented as a rectangle. An **Attribute** is a property of an entity (e.g. email, price). A **Relationship** defines how entities associate with each other (e.g. User *places* Order), traditionally shown as a diamond or connector lines."
            },
            {
                "heading": "Crow's Foot Notation & Cardinality Constraints",
                "body": "Modern software engineering predominantly uses Crow's Foot notation to depict cardinality and modality: (1) **One-to-One** (1:1), (2) **One-to-Many** (1:N) represented with a three-pronged 'crow's foot', and (3) **Many-to-Many** (M:N). Modality defines whether a relationship is mandatory (solid circle or bar) or optional (open ring)."
            }
        ],
        code_snippets=[
            {
                "title": "Translating an ER Diagram Entity into an SQL Table",
                "language": "sql",
                "code": "-- Entity: Patient\n-- Primary Key: patient_id\n-- Attributes: full_name, dob, gender, contact_phone\nCREATE TABLE patients (\n    patient_id SERIAL PRIMARY KEY,\n    full_name VARCHAR(100) NOT NULL,\n    dob DATE NOT NULL,\n    gender CHAR(1) CHECK (gender IN ('M', 'F', 'O')),\n    contact_phone VARCHAR(20)\n);",
                "explanation": "Translates an ER entity box and its attribute list directly into an SQL table definition."
            },
            {
                "title": "Translating a 1:N Relationship into Foreign Key SQL",
                "language": "sql",
                "code": "-- Relationship: Patient (1) ----< (N) Appointments\n-- A Patient can have Many Appointments; each Appointment belongs to 1 Patient\nCREATE TABLE appointments (\n    appointment_id SERIAL PRIMARY KEY,\n    patient_id INT NOT NULL REFERENCES patients(patient_id),\n    scheduled_time TIMESTAMP NOT NULL,\n    reason TEXT NOT NULL,\n    status VARCHAR(20) DEFAULT 'scheduled'\n);",
                "explanation": "In 1:N relationships, the primary key of the '1' entity is placed as a foreign key on the 'Many' table."
            },
            {
                "title": "Translating an M:N Relationship with an Associative Entity",
                "language": "sql",
                "code": "-- Relationship: Doctors (M) >----< (N) Specializations\n-- Decomposed via Associative Entity / Bridge Table\nCREATE TABLE doctor_specializations (\n    doctor_id INT REFERENCES doctors(id) ON DELETE CASCADE,\n    spec_id INT REFERENCES specializations(id) ON DELETE CASCADE,\n    certified_year INT NOT NULL,\n    PRIMARY KEY (doctor_id, spec_id)\n);",
                "explanation": "Many-to-Many relationships depicted in ER diagrams must be resolved in SQL with an associative junction table."
            },
            {
                "title": "ER Diagram Verification Query (Joining Across Entities)",
                "language": "sql",
                "code": "-- Verifies the complete ER model relationships in a single query\nSELECT \n    p.full_name AS patient,\n    a.scheduled_time,\n    d.full_name AS doctor\nFROM appointments a\nJOIN patients p ON a.patient_id = p.patient_id\nJOIN doctors d ON a.doctor_id = d.doctor_id\nWHERE a.status = 'scheduled';",
                "explanation": "Validates that foreign keys correctly connect all related entities modeled in the ER diagram."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="ER Cardinality Symbol Decoder",
            description="Write a Python function `describe_cardinality(symbol: str) -> str` that maps Crow's foot diagram notation symbols (`'1:1'`, `'1:N'`, `'M:N'`) to human-readable strings: `'One-to-One'`, `'One-to-Many'`, and `'Many-to-Many'`. Return `'Unknown'` for unrecognized symbols.",
            starter_code="def describe_cardinality(symbol: str) -> str:\n    # Return descriptive name of relationship\n    pass",
            solution_code="def describe_cardinality(symbol: str) -> str:\n    mapping = {\n        '1:1': 'One-to-One',\n        '1:N': 'One-to-Many',\n        'M:N': 'Many-to-Many',\n        'N:M': 'Many-to-Many'\n    }\n    return mapping.get(symbol.strip().upper(), 'Unknown')",
            expected_output="describe_cardinality('1:N') == 'One-to-Many', describe_cardinality('M:N') == 'Many-to-Many'"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the primary purpose of creating an Entity-Relationship (ER) Diagram before writing SQL?",
                options=[
                    "To visually plan entities, attributes, relationships, and constraints, preventing structural design flaws before implementation",
                    "To compress database tables into ZIP archives",
                    "To measure the physical speed of the CPU",
                    "To generate CSS styling for web pages"
                ],
                correct_answer="To visually plan entities, attributes, relationships, and constraints, preventing structural design flaws before implementation",
                explanation="ER diagrams are architectural blueprints that clarify business domains and prevent structural schema rework."
            ),
            QuizQuestionBlueprint(
                question="What does the three-pronged 'Crow's Foot' symbol represent on a relationship line in an ER diagram?",
                options=[
                    "The 'Many' side of a relationship",
                    "The 'One' side of a relationship",
                    "A deleted table",
                    "An encrypted column"
                ],
                correct_answer="The 'Many' side of a relationship",
                explanation="In Crow's foot notation, the branching three-pronged symbol denotes a 'Many' cardinality."
            ),
            QuizQuestionBlueprint(
                question="How must a Many-to-Many (M:N) relationship shown on an ER diagram be implemented in an RDBMS?",
                options=[
                    "By creating a third junction (associative) table containing foreign keys pointing to both entities",
                    "By merging both tables into a single column",
                    "By duplicating every row 1,000 times",
                    "Many-to-Many relationships cannot be stored in databases"
                ],
                correct_answer="By creating a third junction (associative) table containing foreign keys pointing to both entities",
                explanation="Relational databases resolve M:N relationships through a junction table with two foreign keys."
            ),
            QuizQuestionBlueprint(
                question="In Peter Chen's original ER diagram notation, what geometric shape represents an Entity?",
                options=[
                    "Rectangle",
                    "Diamond",
                    "Oval / Ellipse",
                    "Triangle"
                ],
                correct_answer="Rectangle",
                explanation="In Chen notation, Rectangles represent Entities, Diamonds represent Relationships, and Ovals represent Attributes."
            ),
            QuizQuestionBlueprint(
                question="Where is the Foreign Key placed when implementing a 1-to-Many (1:N) relationship in SQL?",
                options=[
                    "In the table on the 'Many' side of the relationship",
                    "In the table on the 'One' side of the relationship",
                    "In both tables simultaneously",
                    "In a temporary file on the user desktop"
                ],
                correct_answer="In the table on the 'Many' side of the relationship",
                explanation="The child table on the 'Many' side holds the foreign key referencing the parent table's primary key."
            )
        ]
    )
]
