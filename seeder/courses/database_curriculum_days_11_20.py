"""
Database Management 40-Day Curriculum - Module 3 (Part 2), Module 4 & Module 5 (Part 1) (Days 11 to 20)
Module 3: Database Design & Architecture (Days 11-14)
Module 4: Advanced SQL Queries (Days 15-19)
Module 5: Database Programmability (Day 20)
"""

from seeder.course_blueprint import DayBlueprint, QuizQuestionBlueprint, CodingChallengeBlueprint

DAYS_11_TO_20 = [
    # -------------------------------------------------------------
    # DAY 11
    # -------------------------------------------------------------
    DayBlueprint(
        order=11,
        title="Day 11: Database Relationships (1:1, 1:N, M:N)",
        concept="Architecting one-to-one, one-to-many, and many-to-many relationships with foreign key integrity and junction tables",
        analogy="Think of relationships like social and physical connections in daily life. A person having exactly one passport is a **1:1 relationship** (one human, one document). A mother having multiple biological children is a **1:N relationship** (one mother, many kids; but each kid has one biological mother). Students enrolling in multiple college classes, where each class also has dozens of students, is a **M:N relationship** (requiring an enrollment roster / junction table)!",
        theory_sections=[
            {
                "heading": "The Three Cardinal Relationship Types",
                "body": "In relational schemas, relationships reflect real-world business dependencies: **1:1 (One-to-One)** shares a unique foreign key between two tables (often used for sensitive data isolation like user auth vs profile); **1:N (One-to-Many)** is the most common, placing the parent primary key as a foreign key on the child; **M:N (Many-to-Many)** requires an intermediate junction/bridge table."
            },
            {
                "heading": "Cascade Rules and Referential Integrity",
                "body": "When establishing relationships, foreign key actions dictate lifecycle rules: `ON DELETE CASCADE` removes child rows if the parent is deleted; `ON DELETE RESTRICT` (or `NO ACTION`) blocks deletion of parent rows that have active child references; `ON DELETE SET NULL` clears the foreign key attribute while preserving child records."
            }
        ],
        code_snippets=[
            {
                "title": "One-to-One Relationship (1:1) with UNIQUE Foreign Key",
                "language": "sql",
                "code": "CREATE TABLE users (\n    user_id SERIAL PRIMARY KEY,\n    username VARCHAR(50) NOT NULL\n);\n\n-- 1:1 relationship enforced by adding UNIQUE constraint to the foreign key\nCREATE TABLE user_profiles (\n    profile_id SERIAL PRIMARY KEY,\n    user_id INT UNIQUE NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,\n    bio TEXT,\n    avatar_url VARCHAR(255)\n);",
                "explanation": "Adding `UNIQUE` to the foreign key guarantees that a user can have at most one profile row."
            },
            {
                "title": "One-to-Many Relationship (1:N)",
                "language": "sql",
                "code": "CREATE TABLE departments (\n    dept_id SERIAL PRIMARY KEY,\n    name VARCHAR(50) NOT NULL\n);\n\n-- 1:N: One department has Many employees\nCREATE TABLE employees (\n    emp_id SERIAL PRIMARY KEY,\n    dept_id INT REFERENCES departments(dept_id) ON DELETE RESTRICT,\n    full_name VARCHAR(100) NOT NULL\n);",
                "explanation": "Placing dept_id in employees allows many employees to reference the same department."
            },
            {
                "title": "Many-to-Many Relationship (M:N) via Junction Table",
                "language": "sql",
                "code": "CREATE TABLE students (student_id SERIAL PRIMARY KEY, name VARCHAR(50));\nCREATE TABLE courses (course_id SERIAL PRIMARY KEY, title VARCHAR(100));\n\n-- Junction Table / Associative Entity resolving M:N\nCREATE TABLE course_enrollments (\n    student_id INT REFERENCES students(student_id) ON DELETE CASCADE,\n    course_id INT REFERENCES courses(course_id) ON DELETE CASCADE,\n    enrolled_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,\n    PRIMARY KEY (student_id, course_id)\n);",
                "explanation": "The junction table stores pairs of foreign keys, enabling students and courses to link many-to-many."
            },
            {
                "title": "Querying Across M:N Junction Tables",
                "language": "sql",
                "code": "SELECT s.name AS student_name, c.title AS course_title\nFROM students s\nJOIN course_enrollments ce ON s.student_id = ce.student_id\nJOIN courses c ON ce.course_id = c.course_id\nWHERE c.title = 'Database Management';",
                "explanation": "Joining across the junction table reconstructs the many-to-many business relationships."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Relationship Foreign Key Placement Validator",
            description="Write a Python function `get_fk_placement_strategy(rel_type: str) -> str` that returns `'Child table with UNIQUE'`, `'Child table (Many side)'`, or `'Separate junction table'` for `'1:1'`, `'1:N'`, and `'M:N'` respectively.",
            starter_code="def get_fk_placement_strategy(rel_type: str) -> str:\n    # Return description of where foreign key belongs\n    pass",
            solution_code="def get_fk_placement_strategy(rel_type: str) -> str:\n    mapping = {\n        '1:1': 'Child table with UNIQUE',\n        '1:N': 'Child table (Many side)',\n        'M:N': 'Separate junction table'\n    }\n    return mapping.get(rel_type.strip().upper(), 'Invalid relationship type')",
            expected_output="get_fk_placement_strategy('1:N') == 'Child table (Many side)'"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="How is a true One-to-One (1:1) relationship enforced in an RDBMS using foreign keys?",
                options=[
                    "By adding a UNIQUE constraint on the foreign key column in the dependent table",
                    "By storing all data in a single text string",
                    "By creating 10 copies of the parent table",
                    "A 1:1 relationship requires no constraints or keys"
                ],
                correct_answer="By adding a UNIQUE constraint on the foreign key column in the dependent table",
                explanation="A UNIQUE foreign key prevents multiple child records from referencing the same parent row, enforcing 1:1."
            ),
            QuizQuestionBlueprint(
                question="Why is a junction table necessary to implement a Many-to-Many (M:N) relationship?",
                options=[
                    "Because relational tables cannot store multi-valued arrays without violating First Normal Form",
                    "Because SQL engines crash if a table has more than 5 columns",
                    "Because foreign keys are not allowed in parent tables",
                    "It is only required when running on Linux"
                ],
                correct_answer="Because relational tables cannot store multi-valued arrays without violating First Normal Form",
                explanation="Junction tables split an M:N relationship into two 1:N relations, preserving atomicity and normalization."
            ),
            QuizQuestionBlueprint(
                question="What foreign key action prevents deleting a parent department if employees are still assigned to it?",
                options=[
                    "ON DELETE RESTRICT (or NO ACTION)",
                    "ON DELETE CASCADE",
                    "ON DELETE SET NULL",
                    "ON DELETE RANDOM"
                ],
                correct_answer="ON DELETE RESTRICT (or NO ACTION)",
                explanation="RESTRICT prevents accidental deletion of parents when dependent child rows exist."
            ),
            QuizQuestionBlueprint(
                question="In a blogging application where each Post has Many Comments, where does the foreign key belong?",
                options=[
                    "In the Comments table referencing the Post ID",
                    "In the Posts table referencing the Comment ID",
                    "In an external Excel file",
                    "In both tables simultaneously with duplicate columns"
                ],
                correct_answer="In the Comments table referencing the Post ID",
                explanation="The child entity (Comments) on the 'Many' side holds the foreign key to the parent (Posts)."
            ),
            QuizQuestionBlueprint(
                question="What is the primary key of a standard junction table typically made of?",
                options=[
                    "A composite key consisting of both foreign key IDs (e.g. PRIMARY KEY(student_id, course_id))",
                    "A random floating point number",
                    "The current time in milliseconds only",
                    "The user's home address"
                ],
                correct_answer="A composite key consisting of both foreign key IDs (e.g. PRIMARY KEY(student_id, course_id))",
                explanation="A composite primary key combining both foreign keys prevents duplicate associations."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 12
    # -------------------------------------------------------------
    DayBlueprint(
        order=12,
        title="Day 12: Database Normalization (1NF, 2NF, 3NF & BCNF)",
        concept="Eliminating data redundancy and update/delete anomalies using standard Normal Forms: 1NF, 2NF, 3NF, and Boyce-Codd Normal Form",
        analogy="Think of database normalization like organizing an overstuffed, chaotic wardrobe. In an unorganized closet, you have shirts crumpled into pockets with socks, shoes, and jewelry (0NF - unnormalized). 1NF means putting items into separate single compartments. 2NF means removing sports gear from the shoe rack. 3NF means ensuring dress ties don't depend on what shoe you wear. Every item is in its dedicated drawer—no duplicates, no mess!",
        theory_sections=[
            {
                "heading": "Why We Normalize: Insertion, Update & Deletion Anomalies",
                "body": "Unnormalized tables suffer from three catastrophic anomalies: (1) **Insertion Anomaly** (you cannot add a new course without having an enrolled student); (2) **Update Anomaly** (changing an instructor's phone number requires updating 500 rows, risking inconsistencies if one fails); (3) **Deletion Anomaly** (deleting the last enrolled student accidentally deletes all information about the course itself)."
            },
            {
                "heading": "The Progressive Hierarchy of Normal Forms",
                "body": "**1NF**: All column values must be atomic (no comma-separated lists), with unique rows. **2NF**: Must be in 1NF AND have no partial dependency (every non-key attribute must depend on the *whole* composite primary key). **3NF**: Must be in 2NF AND have no transitive dependency (non-key attributes must not depend on other non-key attributes). **BCNF**: Every determinant must be a candidate key."
            }
        ],
        code_snippets=[
            {
                "title": "Unnormalized Table (0NF) with Non-Atomic Values & Anomalies",
                "language": "sql",
                "code": "-- UNNORMALIZED (0NF): Comma-separated values, repeated instructor details\n-- StudentCourses(student_id, student_name, course_codes, instructor_name, instructor_phone)\n-- 101 | 'Ali' | 'CS101, MATH201' | 'Dr. Tariq' | '0300-1234567'",
                "explanation": "Storing lists in single cells violates 1NF; repeating instructor phone numbers creates update anomalies."
            },
            {
                "title": "First Normal Form (1NF): Atomic Values & Primary Key",
                "language": "sql",
                "code": "-- 1NF: Every cell is atomic; composite PK (student_id, course_code)\nCREATE TABLE student_courses_1nf (\n    student_id INT,\n    student_name VARCHAR(50),\n    course_code VARCHAR(10),\n    instructor_name VARCHAR(50),\n    instructor_phone VARCHAR(20),\n    PRIMARY KEY (student_id, course_code)\n);\n-- Note: student_name depends only on student_id (Partial Dependency -> violates 2NF!)",
                "explanation": "1NF ensures atomicity, but non-key columns depending on part of the composite key violate 2NF."
            },
            {
                "title": "Second Normal Form (2NF): Eliminating Partial Dependencies",
                "language": "sql",
                "code": "-- 2NF: Decomposed into separate tables with no partial dependencies\nCREATE TABLE students (\n    student_id INT PRIMARY KEY,\n    student_name VARCHAR(50)\n);\n\nCREATE TABLE courses_2nf (\n    course_code VARCHAR(10) PRIMARY KEY,\n    instructor_name VARCHAR(50),\n    instructor_phone VARCHAR(20) -- Depends on instructor_name (Transitive Dependency -> violates 3NF!)\n);\n\nCREATE TABLE enrollments (\n    student_id INT REFERENCES students(student_id),\n    course_code INT REFERENCES courses_2nf(course_code),\n    PRIMARY KEY (student_id, course_code)\n);",
                "explanation": "2NF removes partial key dependencies, isolating students from courses."
            },
            {
                "title": "Third Normal Form (3NF): Eliminating Transitive Dependencies",
                "language": "sql",
                "code": "-- 3NF: No non-key attribute depends on another non-key attribute\nCREATE TABLE instructors (\n    instructor_id SERIAL PRIMARY KEY,\n    name VARCHAR(50) NOT NULL,\n    phone VARCHAR(20)\n);\n\nCREATE TABLE courses (\n    course_code VARCHAR(10) PRIMARY KEY,\n    title VARCHAR(100) NOT NULL,\n    instructor_id INT REFERENCES instructors(instructor_id) -- Clean FK\n);",
                "explanation": "3NF moves instructor phone numbers into an instructors table, eliminating transitive dependency."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="1NF Atomicity Validator",
            description="Write a Python function `is_1nf_compliant(rows: list[dict], check_col: str) -> bool` that verifies whether all values in `check_col` across all rows are single scalar strings/numbers with no commas or lists.",
            starter_code="def is_1nf_compliant(rows: list[dict], check_col: str) -> bool:\n    # Return False if check_col contains commas or lists\n    pass",
            solution_code="def is_1nf_compliant(rows: list[dict], check_col: str) -> bool:\n    for r in rows:\n        val = r.get(check_col)\n        if isinstance(val, (list, tuple, set)):\n            return False\n        if isinstance(val, str) and ',' in val:\n            return False\n    return True",
            expected_output="is_1nf_compliant([{'id': 1, 'phone': '0300, 0321'}], 'phone') == False, is_1nf_compliant([{'id': 1, 'phone': '0300'}], 'phone') == True"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the foundational requirement for a table to achieve First Normal Form (1NF)?",
                options=[
                    "Every attribute cell must hold a single atomic (indivisible) value, with unique rows and a defined primary key",
                    "The table must have at least 10 foreign keys",
                    "All column names must be uppercase",
                    "The table must be hosted on an SSD drive"
                ],
                correct_answer="Every attribute cell must hold a single atomic (indivisible) value, with unique rows and a defined primary key",
                explanation="1NF requires atomic values (no lists or repeating groups) and a primary key for unique row identification."
            ),
            QuizQuestionBlueprint(
                question="What type of dependency is eliminated when moving a table from 1NF to Second Normal Form (2NF)?",
                options=[
                    "Partial Functional Dependency (where a non-key attribute depends on only part of a composite primary key)",
                    "Transitive Dependency",
                    "Internet connection dependency",
                    "Hardware driver dependency"
                ],
                correct_answer="Partial Functional Dependency (where a non-key attribute depends on only part of a composite primary key)",
                explanation="2NF eliminates partial dependencies: every non-key column must depend on the full primary key."
            ),
            QuizQuestionBlueprint(
                question="What type of dependency is eliminated when moving from 2NF to Third Normal Form (3NF)?",
                options=[
                    "Transitive Dependency (where a non-key attribute depends on another non-key attribute)",
                    "Partial Dependency",
                    "Foreign Key constraints",
                    "NULL values"
                ],
                correct_answer="Transitive Dependency (where a non-key attribute depends on another non-key attribute)",
                explanation="3NF removes transitive dependencies: non-key attributes must depend solely on the primary key ('the key, the whole key, and nothing but the key')."
            ),
            QuizQuestionBlueprint(
                question="What is an 'Update Anomaly' in an unnormalized database?",
                options=[
                    "When changing a duplicated piece of data in one place fails to update all other places, causing inconsistent data records",
                    "When the computer software requests an OS update",
                    "When an INSERT query runs too fast",
                    "When a password is forgotten"
                ],
                correct_answer="When changing a duplicated piece of data in one place fails to update all other places, causing inconsistent data records",
                explanation="Redundancy leads to update anomalies where data discrepancies emerge between repeated entries."
            ),
            QuizQuestionBlueprint(
                question="What is Boyce-Codd Normal Form (BCNF)?",
                options=[
                    "A stricter version of 3NF where every determinant (X in X -> Y) must be a Candidate Key",
                    "A normalization format designed exclusively for binary files",
                    "A database system invented by Microsoft",
                    "A method to delete all tables at once"
                ],
                correct_answer="A stricter version of 3NF where every determinant (X in X -> Y) must be a Candidate Key",
                explanation="BCNF resolves anomalies that 3NF misses by requiring that every determinant in a functional dependency be a candidate key."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 13
    # -------------------------------------------------------------
    DayBlueprint(
        order=13,
        title="Day 13: Denormalization - Performance Strategies & Trade-offs",
        concept="Strategic intentional redundancy: when and how to denormalize for high-throughput read workloads, caching counts, and reporting dashboards",
        analogy="Think of normalization like buying flat-pack furniture from IKEA: every screw and plank is neatly packaged in separate boxes with zero wasted space (efficient storage, no duplicates). But if you run an emergency hospital, you don't build a stretcher from flat-pack pieces during a crisis—you keep fully assembled stretchers ready in the hallway (denormalization). You trade extra floor space for instantaneous life-saving speed!",
        theory_sections=[
            {
                "heading": "Why Intentional Redundancy is Sometimes Necessary",
                "body": "While 3NF guarantees zero update anomalies, heavily normalized schemas require 8-way or 10-way `JOIN` operations to assemble a single customer screen. On systems serving 50,000 read requests per second, multi-table joins exhaust CPU cycles and disk I/O. Denormalization strategically introduces redundant columns (e.g. `comment_count` on a post) to turn complex aggregations into O(1) row lookups."
            },
            {
                "heading": "The Golden Rule: Managing the Write Penalty",
                "body": "Denormalization is a deliberate trade-off: **faster reads at the cost of slower, more complex writes**. Whenever a comment is inserted or deleted, the application must update the parent post's `comment_count` (via database triggers or application transactions) to prevent data drift."
            }
        ],
        code_snippets=[
            {
                "title": "Normalized Read Query Requiring Expensive JOIN & Aggregation",
                "language": "sql",
                "code": "-- 3NF Normalized: Calculates comment count on every page view\n-- Under heavy traffic, this table scan/index aggregate spikes database CPU\nSELECT \n    p.id, \n    p.title,\n    COUNT(c.id) AS total_comments\nFROM posts p\nLEFT JOIN comments c ON p.id = c.post_id\nWHERE p.id = 1042\nGROUP BY p.id, p.title;",
                "explanation": "In 3NF, calculating counts dynamically requires scanning and aggregating comment records on each request."
            },
            {
                "title": "Denormalized Schema with Stored Pre-Calculated Counter",
                "language": "sql",
                "code": "-- Denormalized: Pre-stores author_name and comment_count directly on posts\nCREATE TABLE posts (\n    id SERIAL PRIMARY KEY,\n    author_id INT REFERENCES authors(id),\n    author_name VARCHAR(100),       -- Redundant copy to avoid JOIN with authors\n    title VARCHAR(200) NOT NULL,\n    comment_count INT DEFAULT 0     -- Pre-calculated summary metric\n);",
                "explanation": "Pre-storing author_name and comment_count allows reading posts with zero joins."
            },
            {
                "title": "Blazing Fast O(1) Denormalized Read Query",
                "language": "sql",
                "code": "-- Single row lookup: Instantaneous response with NO joins and NO aggregates\nSELECT id, title, author_name, comment_count\nFROM posts\nWHERE id = 1042;",
                "explanation": "The read query becomes a simple primary key point lookup, returning in sub-millisecond time."
            },
            {
                "title": "Maintaining Denormalized Consistency via Database Trigger",
                "language": "sql",
                "code": "CREATE OR REPLACE FUNCTION increment_post_comment_count()\nRETURNS TRIGGER AS $$\nBEGIN\n    UPDATE posts \n    SET comment_count = comment_count + 1 \n    WHERE id = NEW.post_id;\n    RETURN NEW;\nEND;\n$$ LANGUAGE plpgsql;\n\nCREATE TRIGGER after_comment_insert\nAFTER INSERT ON comments\nFOR EACH ROW\nEXECUTE FUNCTION increment_post_comment_count();",
                "explanation": "Triggers automatically synchronize denormalized counters whenever new comments are inserted."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Read-to-Write Ratio Classifier",
            description="Write a Python function `recommend_architecture(read_ratio: float) -> str` that returns `'Denormalize for Read Performance'` if `read_ratio >= 0.90` (90% or more reads), `'Normalize for Transaction Integrity'` if `read_ratio <= 0.50`, and `'Hybrid / Normalized with Caching'` otherwise.",
            starter_code="def recommend_architecture(read_ratio: float) -> str:\n    # Recommend architectural approach based on read workload\n    pass",
            solution_code="def recommend_architecture(read_ratio: float) -> str:\n    if read_ratio >= 0.90:\n        return 'Denormalize for Read Performance'\n    elif read_ratio <= 0.50:\n        return 'Normalize for Transaction Integrity'\n    return 'Hybrid / Normalized with Caching'",
            expected_output="recommend_architecture(0.95) == 'Denormalize for Read Performance', recommend_architecture(0.3) == 'Normalize for Transaction Integrity'"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the primary motivation for denormalizing a relational database schema?",
                options=[
                    "To dramatically speed up read queries and reports by reducing or eliminating complex multi-table JOINs",
                    "To save hard drive space",
                    "To eliminate the need for primary keys",
                    "To ensure ACID compliance"
                ],
                correct_answer="To dramatically speed up read queries and reports by reducing or eliminating complex multi-table JOINs",
                explanation="Denormalization trades storage and write complexity for ultra-fast read performance by minimizing joins."
            ),
            QuizQuestionBlueprint(
                question="What is the primary risk or disadvantage of denormalization?",
                options=[
                    "Data inconsistency risks and increased complexity during INSERT, UPDATE, and DELETE operations",
                    "Queries can no longer use WHERE clauses",
                    "Tables are limited to 10 rows maximum",
                    "SQL will no longer compile"
                ],
                correct_answer="Data inconsistency risks and increased complexity during INSERT, UPDATE, and DELETE operations",
                explanation="When data is duplicated across columns, failure to update all copies causes data corruption."
            ),
            QuizQuestionBlueprint(
                question="Which workload profile is the best candidate for denormalization?",
                options=[
                    "Read-heavy systems with high queries-per-second and infrequent writes (e.g. social media feeds, analytics)",
                    "Write-heavy core financial banking transactions",
                    "Medical prescription dispensers requiring strict zero-redundancy",
                    "Real-time sensor logs streaming 100,000 writes per second"
                ],
                correct_answer="Read-heavy systems with high queries-per-second and infrequent writes (e.g. social media feeds, analytics)",
                explanation="Read-heavy workloads benefit enormously from pre-calculated columns and reduced joins."
            ),
            QuizQuestionBlueprint(
                question="How can database consistency be maintained automatically when storing pre-calculated counters (like comment_count)?",
                options=[
                    "Using database Triggers or transactional application service layers",
                    "By restarting the server every hour",
                    "By running DROP TABLE every night",
                    "Databases automatically detect and synchronize all duplicated text without code"
                ],
                correct_answer="Using database Triggers or transactional application service layers",
                explanation="Triggers or atomic application transactions ensure counters update synchronously with modifications."
            ),
            QuizQuestionBlueprint(
                question="In data warehousing and analytical databases (OLAP), which popular denormalized schema pattern is widely used?",
                options=[
                    "Star Schema and Snowflake Schema",
                    "Circular Schema",
                    "Infinite Loop Schema",
                    "Binary Tree Schema"
                ],
                correct_answer="Star Schema and Snowflake Schema",
                explanation="Star schemas feature denormalized dimension tables surrounding a central fact table for high-speed reporting."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 14
    # -------------------------------------------------------------
    DayBlueprint(
        order=14,
        title="Day 14 (Project): Constraints (NOT NULL, UNIQUE, CHECK) - Library Management Schema",
        concept="Enforcing bulletproof data integrity rules: PRIMARY KEY, FOREIGN KEY, NOT NULL, UNIQUE, CHECK, and DEFAULT in a production Library Schema",
        analogy="Think of database constraints like strict airport security gates. You cannot board without a passenger ticket (`NOT NULL`). You cannot have two passengers claiming the same boarding seat number (`UNIQUE`). Children under 18 cannot sit in emergency exit rows (`CHECK (age >= 18)`). If you leave the meal selection blank, you get the standard sandwich (`DEFAULT 'standard'`). The database protects its own integrity automatically!",
        theory_sections=[
            {
                "heading": "Database-Level Constraints vs Application Validation",
                "body": "Never rely solely on frontend or API code to validate data. If an admin runs a manual SQL migration, an API has a validation bug, or a background worker imports a CSV, invalid records will infiltrate the database. Database constraints serve as the final, immutable line of defense."
            },
            {
                "heading": "The Power of the CHECK Constraint",
                "body": "`CHECK` constraints allow evaluating boolean expressions across columns before any row is inserted or updated. They validate pricing ranges (`CHECK (price > 0)`), status enumerations (`CHECK (status IN ('available', 'borrowed'))`), and date chronologies (`CHECK (return_date >= borrow_date)`)."
            }
        ],
        code_snippets=[
            {
                "title": "Complete Library Management Database Schema (LibraryDB.sql)",
                "language": "sql",
                "code": "CREATE TABLE members (\n    member_id SERIAL PRIMARY KEY,\n    membership_no VARCHAR(20) UNIQUE NOT NULL,\n    full_name VARCHAR(100) NOT NULL,\n    email VARCHAR(120) UNIQUE NOT NULL,\n    age INT NOT NULL CHECK (age >= 5 AND age <= 120),\n    is_active BOOLEAN NOT NULL DEFAULT TRUE,\n    joined_date DATE NOT NULL DEFAULT CURRENT_DATE\n);\n\nCREATE TABLE books (\n    book_id SERIAL PRIMARY KEY,\n    isbn VARCHAR(17) UNIQUE NOT NULL,\n    title VARCHAR(200) NOT NULL,\n    total_copies INT NOT NULL CHECK (total_copies >= 0),\n    available_copies INT NOT NULL CHECK (available_copies >= 0),\n    CONSTRAINT chk_copies_consistency CHECK (available_copies <= total_copies)\n);",
                "explanation": "Implements NOT NULL, UNIQUE, and cross-column CHECK constraints on books and members."
            },
            {
                "title": "Loan Tracking Table with Multi-Column CHECK and Foreign Keys",
                "language": "sql",
                "code": "CREATE TABLE book_loans (\n    loan_id SERIAL PRIMARY KEY,\n    book_id INT NOT NULL REFERENCES books(book_id) ON DELETE RESTRICT,\n    member_id INT NOT NULL REFERENCES members(member_id) ON DELETE RESTRICT,\n    borrow_date DATE NOT NULL DEFAULT CURRENT_DATE,\n    due_date DATE NOT NULL,\n    return_date DATE,\n    fine_amount DECIMAL(6, 2) NOT NULL DEFAULT 0.00 CHECK (fine_amount >= 0.00),\n    -- Chronological constraint\n    CONSTRAINT chk_due_date CHECK (due_date >= borrow_date),\n    CONSTRAINT chk_return_date CHECK (return_date IS NULL OR return_date >= borrow_date)\n);",
                "explanation": "Ensures return and due dates are chronologically valid and fines cannot be negative."
            },
            {
                "title": "Testing Constraint Violations (Expected Rejections)",
                "language": "sql",
                "code": "-- Attempt 1: Violates CHECK (age >= 5)\n-- INSERT INTO members (membership_no, full_name, email, age) VALUES ('M01', 'Baby', 'b@h.app', 2);\n-- ERROR: new row for relation 'members' violates check constraint 'members_age_check'\n\n-- Attempt 2: Violates CHECK (available_copies <= total_copies)\n-- INSERT INTO books (isbn, title, total_copies, available_copies) VALUES ('123', 'SQL', 5, 8);\n-- ERROR: check constraint 'chk_copies_consistency' violated",
                "explanation": "Demonstrates how PostgreSQL automatically halts invalid insertions at the storage engine level."
            },
            {
                "title": "Verifying Valid Circulation Transactions",
                "language": "sql",
                "code": "-- Valid insertion respecting all constraint boundaries\nINSERT INTO members (membership_no, full_name, email, age)\nVALUES ('LIB-2026-001', 'Hamza Khan', 'hamza@hunar.app', 24);\n\nINSERT INTO books (isbn, title, total_copies, available_copies)\nVALUES ('978-0134494166', 'Clean Architecture', 10, 10);\n\nINSERT INTO book_loans (book_id, member_id, due_date)\nVALUES (1, 1, CURRENT_DATE + INTERVAL '14 days');",
                "explanation": "Clean data insertion executing successfully through all constraints."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="SQL Constraint Definition Builder",
            description="Write a Python function `build_check_constraint(constraint_name: str, expression: str) -> str` that formats a valid SQL table constraint definition.",
            starter_code="def build_check_constraint(constraint_name: str, expression: str) -> str:\n    # Return formatted CONSTRAINT string\n    pass",
            solution_code="def build_check_constraint(constraint_name: str, expression: str) -> str:\n    return f\"CONSTRAINT {constraint_name} CHECK ({expression})\"",
            expected_output="build_check_constraint('chk_price', 'price > 0') == 'CONSTRAINT chk_price CHECK (price > 0)'"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Why is relying exclusively on frontend UI validation considered dangerous for database integrity?",
                options=[
                    "Because malicious actors, API scripts, CSV imports, or backend bugs can bypass frontend forms and write corrupted data directly into tables",
                    "Because web browsers cannot read JavaScript",
                    "Because HTML forms are only supported on desktop computers",
                    "Frontend validation is completely sufficient in all modern applications"
                ],
                correct_answer="Because malicious actors, API scripts, CSV imports, or backend bugs can bypass frontend forms and write corrupted data directly into tables",
                explanation="Frontend code can be bypassed easily; database constraints guarantee integrity regardless of client entry point."
            ),
            QuizQuestionBlueprint(
                question="What does the `CHECK (age >= 18)` constraint do when inserting a row with age = 15?",
                options=[
                    "The database engine rejects the insertion and throws a check constraint violation error",
                    "It automatically rounds the age up to 18",
                    "It changes the user's password",
                    "It accepts the row but prints a warning in terminal"
                ],
                correct_answer="The database engine rejects the insertion and throws a check constraint violation error",
                explanation="CHECK constraints strictly reject any DML transaction that evaluates to FALSE."
            ),
            QuizQuestionBlueprint(
                question="What is the difference between a `PRIMARY KEY` constraint and a `UNIQUE` constraint?",
                options=[
                    "A table can have only one Primary Key and it CANNOT contain NULLs; a table can have multiple UNIQUE columns and they typically permit NULLs",
                    "UNIQUE only works on numbers; Primary Key only works on text",
                    "There is no difference in SQL",
                    "Primary keys can only be created by root administrators"
                ],
                correct_answer="A table can have only one Primary Key and it CANNOT contain NULLs; a table can have multiple UNIQUE columns and they typically permit NULLs",
                explanation="Each table has exactly one Primary Key (strictly NOT NULL); multiple columns can have UNIQUE constraints."
            ),
            QuizQuestionBlueprint(
                question="What constraint clause automatically assigns a default timestamp when no value is provided on INSERT?",
                options=[
                    "DEFAULT CURRENT_TIMESTAMP",
                    "AUTO_FILL NOW",
                    "BLANK_DATE",
                    "TIMESTAMP_STATIC"
                ],
                correct_answer="DEFAULT CURRENT_TIMESTAMP",
                explanation="DEFAULT provides fallback values for omitted columns during INSERT operations."
            ),
            QuizQuestionBlueprint(
                question="Can a single `CHECK` constraint compare two different columns in the same row (e.g. `CHECK (end_date >= start_date)`)?",
                options=[
                    "Yes, table-level CHECK constraints can validate mathematical and logical comparisons between multiple columns in that row",
                    "No, CHECK can only inspect single literals like > 0",
                    "Only on SQLite",
                    "Multi-column comparisons require custom C++ extensions"
                ],
                correct_answer="Yes, table-level CHECK constraints can validate mathematical and logical comparisons between multiple columns in that row",
                explanation="Table-level CHECK constraints can validate multi-column logic such as dates and numerical bounds."
            )
        ],
        is_project_day=True,
        project_name="Library Management Schema Integrity Project"
    ),

    # -------------------------------------------------------------
    # DAY 15
    # -------------------------------------------------------------
    DayBlueprint(
        order=15,
        title="Day 15: SQL JOINs - INNER, LEFT, RIGHT, FULL & CROSS",
        concept="Mastering relational set joining: Venn diagram mechanics, matching keys, handling unmatched rows with OUTER joins, and Cartesian products",
        analogy="Think of SQL JOINs like a school dance where Students invite Guests. An **INNER JOIN** only admits couples who both showed up together (matching records on both sides). A **LEFT JOIN** admits all students: if a student brought a guest, the guest comes along; if the student came alone, their guest seat is empty (`NULL`). A **FULL OUTER JOIN** admits everyone—students with or without guests, plus unassigned guests!",
        theory_sections=[
            {
                "heading": "The Inner vs Outer Join Mechanics",
                "body": "Relational queries correlate multiple tables through predicate matches (usually `ON tableA.pk = tableB.fk`). **INNER JOIN** returns only rows where matching keys exist in both sets. **LEFT OUTER JOIN** preserves 100% of rows from the left table, populating right-table columns with `NULL` where no match exists. **RIGHT JOIN** mirrors this for the right table."
            },
            {
                "heading": "FULL OUTER & CROSS JOIN (Cartesian Products)",
                "body": "**FULL OUTER JOIN** returns all records from both tables, filling mismatches on either side with `NULL`. **CROSS JOIN** computes the Cartesian product (combining every row of Table A with every row of Table B). If Table A has 100 rows and Table B has 50 rows, a CROSS JOIN produces 5,000 output tuples."
            }
        ],
        code_snippets=[
            {
                "title": "INNER JOIN: Only Matching Customers and Orders",
                "language": "sql",
                "code": "-- Returns only customers who have placed at least one order\nSELECT \n    c.id AS customer_id,\n    c.name,\n    o.id AS order_id,\n    o.amount\nFROM customers c\nINNER JOIN orders o ON c.id = o.customer_id;",
                "explanation": "INNER JOIN filters out customers without orders and orders without valid customer IDs."
            },
            {
                "title": "LEFT JOIN: Preserving All Customers (Even Those Without Orders)",
                "language": "sql",
                "code": "-- Returns ALL customers. If no order placed, order_id is NULL\nSELECT \n    c.id AS customer_id,\n    c.name,\n    COALESCE(o.amount, 0.00) AS order_amount\nFROM customers c\nLEFT JOIN orders o ON c.id = o.customer_id\nORDER BY c.id ASC;",
                "explanation": "LEFT JOIN guarantees every left-table record appears in the final result set."
            },
            {
                "title": "Anti-Join Pattern: Finding Customers Who Have NEVER Placed an Order",
                "language": "sql",
                "code": "-- The classic 'Anti-Join' pattern: LEFT JOIN + WHERE right_col IS NULL\nSELECT c.id, c.name, c.email\nFROM customers c\nLEFT JOIN orders o ON c.id = o.customer_id\nWHERE o.id IS NULL;",
                "explanation": "Filtering for `o.id IS NULL` after a LEFT JOIN extracts orphaned left records with unmatched keys."
            },
            {
                "title": "CROSS JOIN: Generating Combinations (Sizes x Colors)",
                "language": "sql",
                "code": "-- Generates all product variant combinations (e.g. 3 sizes * 4 colors = 12 SKUs)\nSELECT \n    s.size_name,\n    c.color_name\nFROM sizes s\nCROSS JOIN colors c;",
                "explanation": "CROSS JOIN produces all pairwise permutations between two relations."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Cartesian Product Size Calculator",
            description="Write a Python function `calculate_cross_join_size(table_a_count: int, table_b_count: int) -> int` that calculates the total number of rows produced by a CROSS JOIN. Return 0 if either table count is negative or zero.",
            starter_code="def calculate_cross_join_size(table_a_count: int, table_b_count: int) -> int:\n    # Calculate Cartesian product size\n    pass",
            solution_code="def calculate_cross_join_size(table_a_count: int, table_b_count: int) -> int:\n    if table_a_count <= 0 or table_b_count <= 0:\n        return 0\n    return table_a_count * table_b_count",
            expected_output="calculate_cross_join_size(100, 50) == 5000, calculate_cross_join_size(0, 100) == 0"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What records are returned by an `INNER JOIN` between Table A and Table B?",
                options=[
                    "Only rows where the join condition matches in BOTH Table A and Table B",
                    "All rows from Table A regardless of matches",
                    "All rows from Table B regardless of matches",
                    "All possible mathematical permutations"
                ],
                correct_answer="Only rows where the join condition matches in BOTH Table A and Table B",
                explanation="INNER JOIN strictly retains intersection rows that meet the `ON` condition in both relations."
            ),
            QuizQuestionBlueprint(
                question="What appears in columns from Table B when a `LEFT JOIN` encounters a Table A row with no match?",
                options=[
                    "NULL values",
                    "The number 0",
                    "Empty strings ''",
                    "An error that terminates the query"
                ],
                correct_answer="NULL values",
                explanation="LEFT JOIN fills non-matching right-table attributes with NULL."
            ),
            QuizQuestionBlueprint(
                question="How do you write an 'Anti-Join' in SQL to find all users who have zero registered devices?",
                options=[
                    "SELECT u.* FROM users u LEFT JOIN devices d ON u.id = d.user_id WHERE d.id IS NULL;",
                    "SELECT u.* FROM users u INNER JOIN devices d ON u.id = d.user_id;",
                    "SELECT u.* FROM users u CROSS JOIN devices d;",
                    "DELETE FROM users WHERE devices = 0;"
                ],
                correct_answer="SELECT u.* FROM users u LEFT JOIN devices d ON u.id = d.user_id WHERE d.id IS NULL;",
                explanation="A LEFT JOIN paired with `WHERE right_table.pk IS NULL` isolates unmatched parent records."
            ),
            QuizQuestionBlueprint(
                question="What does a `CROSS JOIN` between a table with 20 rows and a table with 5 rows produce?",
                options=[
                    "100 rows (Cartesian product 20 * 5)",
                    "25 rows (20 + 5)",
                    "15 rows (20 - 5)",
                    "4 rows (20 / 5)"
                ],
                correct_answer="100 rows (Cartesian product 20 * 5)",
                explanation="A CROSS JOIN combines every row from the first table with every row from the second (20 * 5 = 100)."
            ),
            QuizQuestionBlueprint(
                question="Which JOIN type returns all records when there is a match in either left OR right table?",
                options=[
                    "FULL OUTER JOIN",
                    "INNER JOIN",
                    "NATURAL JOIN",
                    "SELF JOIN"
                ],
                correct_answer="FULL OUTER JOIN",
                explanation="FULL OUTER JOIN retains all records from both tables, filling unmatched columns on either side with NULL."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 16
    # -------------------------------------------------------------
    DayBlueprint(
        order=16,
        title="Day 16: SQL Subqueries (Nested & Correlated Queries)",
        concept="Nesting SQL statements: scalar subqueries, IN/NOT IN subqueries, EXISTS vs IN, and correlated execution loops",
        analogy="Think of a subquery like answering a question with a question. If someone asks: 'Who won the marathon?', you can't just shout a name if you don't know the fastest time yet. First, your brain asks a sub-question: 'What was the lowest running time?' (Inner query returns 2 hours 4 minutes). Then you answer the outer question: 'Show me the runner whose time equals 2 hours 4 minutes!'",
        theory_sections=[
            {
                "heading": "Scalar, Multi-Row & Table Subqueries",
                "body": "Subqueries (or nested queries) are `SELECT` statements placed inside parentheses within an outer query. A **Scalar Subquery** returns exactly one value (one row, one column) and can be used anywhere an expression is valid. A **Multi-Row Subquery** returns a list of values for use with `IN`, `ANY`, or `ALL`."
            },
            {
                "heading": "Correlated Subqueries and the EXISTS Operator",
                "body": "In a non-correlated subquery, the inner query executes once independently. In a **Correlated Subquery**, the inner query references columns from the outer query row, executing once for every candidate row evaluated by the outer query. The `EXISTS` operator tests whether a correlated subquery returns at least one row, stopping immediately upon finding a match (short-circuit optimization)."
            }
        ],
        code_snippets=[
            {
                "title": "Scalar Subquery in WHERE Clause",
                "language": "sql",
                "code": "-- Find all employees earning more than the company average salary\nSELECT id, name, salary\nFROM employees\nWHERE salary > (\n    SELECT AVG(salary) FROM employees -- Inner query returns a single scalar float\n);",
                "explanation": "The inner query calculates the company average once; the outer query filters employees exceeding it."
            },
            {
                "title": "Multi-Row Subquery with IN Operator",
                "language": "sql",
                "code": "-- Find customers who purchased products in the 'Electronics' category\nSELECT id, name, email\nFROM customers\nWHERE id IN (\n    SELECT DISTINCT customer_id\n    FROM orders\n    WHERE category = 'Electronics'\n);",
                "explanation": "The inner query generates a set of customer IDs; the outer query selects matching records."
            },
            {
                "title": "Correlated Subquery with EXISTS (High Performance)",
                "language": "sql",
                "code": "-- Select authors who have written at least one book with > 10,000 sales\nSELECT a.id, a.name\nFROM authors a\nWHERE EXISTS (\n    SELECT 1 \n    FROM books b \n    WHERE b.author_id = a.id   -- Correlated reference to outer author row\n      AND b.sales_count > 10000\n);",
                "explanation": "EXISTS short-circuits as soon as one matching book is discovered for each author."
            },
            {
                "title": "Subquery in the FROM Clause (Inline Derived Table)",
                "language": "sql",
                "code": "-- Querying against an aggregated derived table\nSELECT \n    dept_summary.department,\n    dept_summary.avg_salary\nFROM (\n    SELECT department, ROUND(AVG(salary), 2) AS avg_salary\n    FROM employees\n    GROUP BY department\n) AS dept_summary\nWHERE dept_summary.avg_salary > 80000.00;",
                "explanation": "Derived tables allow nesting aggregation logic inside the FROM clause with an alias."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Subquery String Formatter",
            description="Write a Python function `wrap_as_subquery(sql: str, alias: str) -> str` that strips whitespace, encloses the SQL string in parentheses, and attaches the specified table alias.",
            starter_code="def wrap_as_subquery(sql: str, alias: str) -> str:\n    # Wrap SQL string as aliased derived table\n    pass",
            solution_code="def wrap_as_subquery(sql: str, alias: str) -> str:\n    clean_sql = sql.strip().rstrip(';')\n    return f\"({clean_sql}) AS {alias.strip()}\"",
            expected_output="wrap_as_subquery('SELECT id FROM users;', 'u_sub') == '(SELECT id FROM users) AS u_sub'"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is a 'Correlated Subquery'?",
                options=[
                    "A subquery that references columns from the outer query and must be evaluated for each outer row",
                    "A subquery that connects to two different database servers",
                    "A subquery that runs only on weekends",
                    "A subquery with syntax errors"
                ],
                correct_answer="A subquery that references columns from the outer query and must be evaluated for each outer row",
                explanation="Correlated subqueries depend on values from the outer query row, executing iteratively."
            ),
            QuizQuestionBlueprint(
                question="Why is `EXISTS (SELECT 1 ...)` generally faster than `IN (SELECT col ...)` on large tables?",
                options=[
                    "EXISTS short-circuits and stops scanning as soon as the first matching row is found, without building a full in-memory list",
                    "EXISTS disables all database security checks",
                    "IN only works on tables with fewer than 10 rows",
                    "There is no performance difference"
                ],
                correct_answer="EXISTS short-circuits and stops scanning as soon as the first matching row is found, without building a full in-memory list",
                explanation="EXISTS returns boolean TRUE immediately upon finding the first matching tuple."
            ),
            QuizQuestionBlueprint(
                question="What is a Scalar Subquery?",
                options=[
                    "A subquery that returns exactly one row and one column (a single value)",
                    "A subquery that measures physical server temperature",
                    "A subquery that returns at least 1,000 rows",
                    "A query written without the SELECT keyword"
                ],
                correct_answer="A subquery that returns exactly one row and one column (a single value)",
                explanation="A scalar subquery evaluates to a single discrete value, making it valid inside expressions."
            ),
            QuizQuestionBlueprint(
                question="What happens if a scalar subquery used in `WHERE salary > (SELECT ...)` returns 5 rows instead of 1?",
                options=[
                    "The database throws a runtime error stating that more than one row was returned by a subquery used as an expression",
                    "The database averages all 5 values automatically",
                    "The database picks the smallest value",
                    "The computer crashes"
                ],
                correct_answer="The database throws a runtime error stating that more than one row was returned by a subquery used as an expression",
                explanation="Comparison operators like `>` expect a single scalar operand; returning multiple rows throws an error."
            ),
            QuizQuestionBlueprint(
                question="What must always be provided when writing a subquery in the `FROM` clause (derived table)?",
                options=[
                    "A table alias (e.g. `AS sub_table`)",
                    "A semicolon inside the parentheses",
                    "A DROP command",
                    "A password"
                ],
                correct_answer="A table alias (e.g. `AS sub_table`)",
                explanation="ANSI SQL requires every derived table in the FROM clause to have an alias."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 17
    # -------------------------------------------------------------
    DayBlueprint(
        order=17,
        title="Day 17: SQL Set Operations (UNION, UNION ALL, INTERSECT, EXCEPT)",
        concept="Combining query results using mathematical set operations: Union, Intersection, and Difference across compatible relations",
        analogy="Think of SQL set operations like combining contact lists on your smartphone. `UNION` merges your personal contacts and work contacts into one list, deleting exact duplicates. `UNION ALL` stacks both lists together without checking, leaving duplicate contacts intact (much faster!). `INTERSECT` only shows people who are both personal friends AND work colleagues. `EXCEPT` gives you personal contacts who are NOT work colleagues!",
        theory_sections=[
            {
                "heading": "Set Operations vs Table Joins",
                "body": "While JOINs combine tables **horizontally** (adding columns side-by-side), Set Operations combine results **vertically** (stacking rows on top of each other). To be union-compatible, both queries must have: (1) The exact same number of columns, and (2) Compatible data types in matching column positions."
            },
            {
                "heading": "UNION vs UNION ALL Performance",
                "body": "`UNION` performs an implicit deduplication sort (equivalent to `DISTINCT`), which consumes memory and disk I/O. `UNION ALL` simply appends rows without sorting. In production systems, if you know datasets are mutually exclusive or duplicate retention is acceptable, always prefer `UNION ALL` for maximum speed."
            }
        ],
        code_snippets=[
            {
                "title": "UNION vs UNION ALL: Combining Active & Archived Customers",
                "language": "sql",
                "code": "-- UNION: Merges and removes duplicate records (Sort/Unique step)\nSELECT email, first_name FROM active_users\nUNION\nSELECT email, first_name FROM archived_users;\n\n-- UNION ALL: Blazing fast vertical concatenation (No deduplication)\nSELECT email, 'active' AS source FROM active_users\nUNION ALL\nSELECT email, 'archived' AS source FROM archived_users;",
                "explanation": "UNION ALL bypasses sorting, making it significantly faster than UNION on large datasets."
            },
            {
                "title": "INTERSECT: Finding Common Records Across Datasets",
                "language": "sql",
                "code": "-- Find customers who purchased in BOTH 2025 AND 2026\nSELECT customer_id FROM orders_2025\nINTERSECT\nSELECT customer_id FROM orders_2026;",
                "explanation": "INTERSECT returns only records present in both query result sets."
            },
            {
                "title": "EXCEPT / MINUS: Finding Difference Between Sets",
                "language": "sql",
                "code": "-- Find students enrolled in Physics who are NOT enrolled in Chemistry\nSELECT student_id FROM physics_enrollments\nEXCEPT\nSELECT student_id FROM chemistry_enrollments;",
                "explanation": "EXCEPT (called MINUS in Oracle) subtracts the second result set from the first."
            },
            {
                "title": "Union Compatibility Requirement Violation and Fix",
                "language": "sql",
                "code": "-- ERROR: Column count or type mismatch\n-- SELECT id, email FROM users UNION SELECT id FROM admins;\n\n-- FIXED: Exact matching column count and data types\nSELECT id, email, 'user' AS role FROM users\nUNION ALL\nSELECT id, email, 'admin' AS role FROM admins;",
                "explanation": "Set operations require identical column degrees and matching data types in corresponding positions."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Set Operation Compatibility Validator",
            description="Write a Python function `are_union_compatible(schema_a: list[str], schema_b: list[str]) -> bool` that verifies whether two lists of data type strings have identical length and identical types in order.",
            starter_code="def are_union_compatible(schema_a: list[str], schema_b: list[str]) -> bool:\n    # Return True if schemas can be combined with UNION\n    pass",
            solution_code="def are_union_compatible(schema_a: list[str], schema_b: list[str]) -> bool:\n    if len(schema_a) != len(schema_b):\n        return False\n    return [t.upper() for t in schema_a] == [t.upper() for t in schema_b]",
            expected_output="are_union_compatible(['INT', 'VARCHAR'], ['INT', 'VARCHAR']) == True, are_union_compatible(['INT'], ['INT', 'TEXT']) == False"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the critical performance difference between `UNION` and `UNION ALL`?",
                options=[
                    "`UNION` sorts the combined rows to remove duplicates (expensive), while `UNION ALL` concatenates rows directly without sorting (fast)",
                    "`UNION` only works on numbers; `UNION ALL` only works on text",
                    "`UNION ALL` deletes duplicate tables from disk",
                    "There is no difference; they are exact aliases"
                ],
                correct_answer="`UNION` sorts the combined rows to remove duplicates (expensive), while `UNION ALL` concatenates rows directly without sorting (fast)",
                explanation="UNION runs an internal sort to eliminate duplicates; UNION ALL appends rows instantly without deduplication."
            ),
            QuizQuestionBlueprint(
                question="What prerequisite must two queries satisfy to be 'Union Compatible'?",
                options=[
                    "They must select the exact same number of columns with compatible data types in corresponding positions",
                    "They must query the exact same physical table",
                    "Both tables must have fewer than 100 rows",
                    "They must be written by the same database user"
                ],
                correct_answer="They must select the exact same number of columns with compatible data types in corresponding positions",
                explanation="Union compatibility demands equal degree and matching positional data types."
            ),
            QuizQuestionBlueprint(
                question="Which SQL set operation returns only the rows that exist in BOTH query results?",
                options=[
                    "INTERSECT",
                    "UNION",
                    "EXCEPT",
                    "CROSS"
                ],
                correct_answer="INTERSECT",
                explanation="INTERSECT computes the mathematical intersection, retaining rows present in both sets."
            ),
            QuizQuestionBlueprint(
                question="What does Query A `EXCEPT` Query B return in standard SQL (or `MINUS` in Oracle)?",
                options=[
                    "Rows from Query A that do NOT appear in Query B",
                    "All rows from both queries",
                    "Only duplicate rows",
                    "An empty table"
                ],
                correct_answer="Rows from Query A that do NOT appear in Query B",
                explanation="EXCEPT subtracts matching rows of Query B from the results of Query A."
            ),
            QuizQuestionBlueprint(
                question="Do JOINs and Set Operations combine data in the same directional dimension?",
                options=[
                    "No; JOINs combine data horizontally (columns side-by-side), while Set Operations combine data vertically (rows stacked)",
                    "Yes; they are identical operations",
                    "JOINs delete rows, while Set Operations delete columns",
                    "Set Operations only work on CSV files"
                ],
                correct_answer="No; JOINs combine data horizontally (columns side-by-side), while Set Operations combine data vertically (rows stacked)",
                explanation="JOINs add columns horizontally based on keys; Set operations stack rows vertically."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 18
    # -------------------------------------------------------------
    DayBlueprint(
        order=18,
        title="Day 18: CTEs - Common Table Expressions (The WITH Clause)",
        concept="Writing clean, modular, and maintainable SQL using CTEs and tackling hierarchical data structures with Recursive CTEs",
        analogy="Think of a Common Table Expression (CTE) like preparing chopped ingredients in small bowls before cooking a gourmet meal. Instead of trying to chop onions, dice garlic, peel tomatoes, and season meat all inside a boiling soup pot at the same time (a monstrous unreadable 5-level nested subquery), you prep the ingredients first: `WITH chopped_onions AS (...), diced_tomatoes AS (...)`. Then your main query cooks them cleanly!",
        theory_sections=[
            {
                "heading": "Readability and Modularity with WITH Clauses",
                "body": "A Common Table Expression (CTE) defines a temporary, named result set that exists only during the execution scope of a single SQL statement. CTEs drastically improve query readability over deeply nested subqueries, allowing complex multi-step transformations to be read sequentially from top to bottom."
            },
            {
                "heading": "Recursive CTEs for Hierarchical Graphs and Trees",
                "body": "A **Recursive CTE** references its own output, making it uniquely capable of traversing hierarchical structures like organizational reporting lines (Manager -> Employee -> Intern), category trees, and bill-of-materials graphs that standard iterative SQL cannot query."
            }
        ],
        code_snippets=[
            {
                "title": "Simplifying Nested Queries with Standard CTE",
                "language": "sql",
                "code": "-- Step-by-step readable pipeline with CTEs\nWITH HighValueOrders AS (\n    SELECT customer_id, SUM(amount) AS total_spent\n    FROM orders\n    WHERE status = 'completed'\n    GROUP BY customer_id\n    HAVING SUM(amount) > 1000.00\n),\nEligibleCustomers AS (\n    SELECT c.id, c.name, c.email, hvo.total_spent\n    FROM customers c\n    JOIN HighValueOrders hvo ON c.id = hvo.customer_id\n)\nSELECT name, email, total_spent\nFROM EligibleCustomers\nORDER BY total_spent DESC;",
                "explanation": "Breaks complex aggregations into clean, named blocks read sequentially from top to bottom."
            },
            {
                "title": "Recursive CTE: Traversing an Organization Hierarchy Tree",
                "language": "sql",
                "code": "WITH RECURSIVE OrgChart AS (\n    -- Anchor Member: Find the CEO (who has no manager)\n    SELECT emp_id, name, manager_id, 1 AS level\n    FROM employees\n    WHERE manager_id IS NULL\n    \n    UNION ALL\n    \n    -- Recursive Member: Find employees reporting to previous level\n    SELECT e.emp_id, e.name, e.manager_id, o.level + 1\n    FROM employees e\n    JOIN OrgChart o ON e.manager_id = o.emp_id\n)\nSELECT level, name, manager_id FROM OrgChart ORDER BY level, emp_id;",
                "explanation": "A recursive CTE starts with an anchor query and recursively unions child rows until the tree is traversed."
            },
            {
                "title": "Generating a Date Series with Recursive CTE",
                "language": "sql",
                "code": "WITH RECURSIVE DaysOfMonth AS (\n    SELECT DATE '2026-09-01' AS calendar_date -- Anchor\n    UNION ALL\n    SELECT calendar_date + INTERVAL '1 day'   -- Recursive increment\n    FROM DaysOfMonth\n    WHERE calendar_date < DATE '2026-09-30'\n)\nSELECT calendar_date FROM DaysOfMonth;",
                "explanation": "Recursion can generate sequences and calendars directly inside SQL without external script loops."
            },
            {
                "title": "Writable CTE (Modifying Rows & Using Output in Same Query)",
                "language": "sql",
                "code": "-- Moves deleted users into an archive table atomically in one query!\nWITH DeletedUsers AS (\n    DELETE FROM users\n    WHERE status = 'banned'\n    RETURNING id, username, email, CURRENT_TIMESTAMP AS deleted_at\n)\nINSERT INTO user_audit_archive (id, username, email, deleted_at)\nSELECT id, username, email, deleted_at FROM DeletedUsers;",
                "explanation": "PostgreSQL data-modifying CTEs allow piping deleted rows directly into archive tables in a single statement."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="CTE Header Formatter",
            description="Write a Python function `build_cte_prefix(ctes: dict[str, str]) -> str` that formats a valid SQL `WITH name AS (query), ...` header block.",
            starter_code="def build_cte_prefix(ctes: dict[str, str]) -> str:\n    # Generate WITH clause string from dictionary of CTEs\n    pass",
            solution_code="def build_cte_prefix(ctes: dict[str, str]) -> str:\n    if not ctes:\n        return ''\n    parts = [f\"{name} AS ({query.strip().rstrip(';')})\" for name, query in ctes.items()]\n    return 'WITH ' + ',\\n'.join(parts)",
            expected_output="build_cte_prefix({'t1': 'SELECT 1'}) == 'WITH t1 AS (SELECT 1)'"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What keyword introduces a Common Table Expression (CTE) in SQL?",
                options=[
                    "WITH",
                    "DEFINE",
                    "TEMP_TABLE",
                    "DECLARE"
                ],
                correct_answer="WITH",
                explanation="The `WITH` keyword declares Common Table Expressions."
            ),
            QuizQuestionBlueprint(
                question="What is the primary advantage of using a CTE over a deeply nested subquery?",
                options=[
                    "It dramatically improves readability, modularity, and maintainability by structuring logic sequentially",
                    "It automatically creates physical tables on the hard drive",
                    "It bypasses all user authentication",
                    "It converts SQL into Python"
                ],
                correct_answer="It dramatically improves readability, modularity, and maintainability by structuring logic sequentially",
                explanation="CTEs break convoluted queries into named steps that read cleanly from top to bottom."
            ),
            QuizQuestionBlueprint(
                question="What are the two mandatory parts of a Recursive CTE?",
                options=[
                    "An Anchor Member (base query) and a Recursive Member (query referencing the CTE) connected by UNION ALL",
                    "A SELECT query and an ALTER TABLE command",
                    "A Python script and a CSV file",
                    "Two PRIMARY KEY constraints"
                ],
                correct_answer="An Anchor Member (base query) and a Recursive Member (query referencing the CTE) connected by UNION ALL",
                explanation="Recursive CTEs require an initial anchor query and a recursive member that references the CTE itself."
            ),
            QuizQuestionBlueprint(
                question="How long does a CTE exist in the database?",
                options=[
                    "Only for the duration of the single query statement in which it is written",
                    "Permanently until dropped with DROP TABLE",
                    "Until the server is rebooted",
                    "For exactly 24 hours"
                ],
                correct_answer="Only for the duration of the single query statement in which it is written",
                explanation="CTEs are temporary query-scoped constructs that dissolve immediately after query execution."
            ),
            QuizQuestionBlueprint(
                question="Can multiple CTEs be defined in a single `WITH` clause separated by commas?",
                options=[
                    "Yes, you can chain multiple CTEs (e.g. `WITH a AS (...), b AS (...)`) and CTE 'b' can even reference CTE 'a'",
                    "No, only one CTE is allowed per database instance",
                    "Only on MySQL",
                    "It requires writing code in C++"
                ],
                correct_answer="Yes, you can chain multiple CTEs (e.g. `WITH a AS (...), b AS (...)`) and CTE 'b' can even reference CTE 'a'",
                explanation="Multiple CTEs can be chained sequentially in a single WITH statement, referencing preceding CTEs."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 19
    # -------------------------------------------------------------
    DayBlueprint(
        order=19,
        title="Day 19: SQL Window Functions (OVER, ROW_NUMBER, RANK, LEAD, LAG)",
        concept="Performing advanced analytics across row partitions without collapsing rows: numbering, ranking, offsets, and running totals",
        analogy="Think of a Window Function like a floating camera drone hovering over marathon runners. A normal `GROUP BY` is like taking all 1,000 runners and crushing them into a single summary box showing 'Average Speed: 12 mph' (all individual runner identities are destroyed!). A Window Function keeps every single runner on the screen, but the drone camera calculates each runner's current rank and distance behind the runner ahead of them (`LEAD` / `LAG`) in real time!",
        theory_sections=[
            {
                "heading": "The Power of the OVER() Clause",
                "body": "Window functions perform calculations across a set of table rows that are related to the current row, without collapsing the result set into a single row like `GROUP BY` does. The `OVER()` clause defines the window: `PARTITION BY` divides rows into groups, and `ORDER BY` defines the logical calculation order within each partition."
            },
            {
                "heading": "Ranking & Offset Functions (ROW_NUMBER, RANK, DENSE_RANK, LAG, LEAD)",
                "body": "`ROW_NUMBER()` assigns sequential integers. `RANK()` leaves gaps on ties (1, 2, 2, 4). `DENSE_RANK()` leaves no gaps on ties (1, 2, 2, 3). `LAG(col, 1)` accesses data from the previous row; `LEAD(col, 1)` peers into the following row—indispensable for calculating period-over-period growth without self-joins."
            }
        ],
        code_snippets=[
            {
                "title": "Row Numbering and Ranking within Department Partitions",
                "language": "sql",
                "code": "SELECT \n    id,\n    name,\n    department,\n    salary,\n    ROW_NUMBER() OVER(PARTITION BY department ORDER BY salary DESC) AS row_num,\n    RANK() OVER(PARTITION BY department ORDER BY salary DESC) AS salary_rank,\n    DENSE_RANK() OVER(PARTITION BY department ORDER BY salary DESC) AS dense_rank\nFROM employees;",
                "explanation": "Calculates row numbers and salary ranks partitioned by department without collapsing rows."
            },
            {
                "title": "Finding the Top N Rows Per Group (Top 2 Earners per Department)",
                "language": "sql",
                "code": "WITH RankedSalaries AS (\n    SELECT \n        id, name, department, salary,\n        DENSE_RANK() OVER(PARTITION BY department ORDER BY salary DESC) AS ranking\n    FROM employees\n)\nSELECT department, ranking, name, salary\nFROM RankedSalaries\nWHERE ranking <= 2\nORDER BY department, ranking;",
                "explanation": "CTEs paired with window ranking functions solve the classic 'Top N items per category' problem."
            },
            {
                "title": "Calculating Month-over-Month Growth with LAG()",
                "language": "sql",
                "code": "SELECT \n    sales_month,\n    revenue,\n    LAG(revenue, 1) OVER(ORDER BY sales_month) AS prev_month_revenue,\n    ROUND(((revenue - LAG(revenue, 1) OVER(ORDER BY sales_month)) / \n           LAG(revenue, 1) OVER(ORDER BY sales_month)) * 100, 2) AS mom_growth_percent\nFROM monthly_sales;",
                "explanation": "LAG retrieves preceding row values, enabling period-over-period financial growth calculations."
            },
            {
                "title": "Running Cumulative Total with SUM() OVER()",
                "language": "sql",
                "code": "SELECT \n    order_date,\n    amount,\n    -- Computes running total of revenue ordered by date\n    SUM(amount) OVER(ORDER BY order_date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS cumulative_revenue\nFROM daily_orders;",
                "explanation": "Calculates running cumulative totals across time without nested loop subqueries."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="DENSE_RANK Simulation Algorithm",
            description="Write a Python function `dense_rank_scores(scores: list[float]) -> list[int]` that takes a list of scores, sorts them descending, and returns their 1-based dense ranks (ties share rank, no gaps).",
            starter_code="def dense_rank_scores(scores: list[float]) -> list[int]:\n    # Return dense rank for each score in input order\n    pass",
            solution_code="def dense_rank_scores(scores: list[float]) -> list[int]:\n    unique_sorted = sorted(list(set(scores)), reverse=True)\n    rank_map = {score: rank + 1 for rank, score in enumerate(unique_sorted)}\n    return [rank_map[s] for s in scores]",
            expected_output="dense_rank_scores([100, 90, 90, 80]) == [1, 2, 2, 3]"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the primary difference between a Window Function and a `GROUP BY` aggregation?",
                options=[
                    "Window functions compute metrics across related rows while preserving all individual row identities; GROUP BY collapses rows into a single summary row",
                    "Window functions delete the table after running",
                    "GROUP BY only works on numbers; Window functions only work on strings",
                    "There is no difference"
                ],
                correct_answer="Window functions compute metrics across related rows while preserving all individual row identities; GROUP BY collapses rows into a single summary row",
                explanation="Window functions do not collapse rows, allowing individual row data and group calculations to coexist."
            ),
            QuizQuestionBlueprint(
                question="What is the difference between `RANK()` and `DENSE_RANK()` when a tie occurs?",
                options=[
                    "`RANK()` skips subsequent rank numbers after ties (e.g. 1, 2, 2, 4); `DENSE_RANK()` leaves no gaps (e.g. 1, 2, 2, 3)",
                    "`RANK()` only works on dates; `DENSE_RANK()` only works on prices",
                    "`DENSE_RANK()` deletes tied rows",
                    "`RANK()` is forbidden in PostgreSQL"
                ],
                correct_answer="`RANK()` skips subsequent rank numbers after ties (e.g. 1, 2, 2, 4); `DENSE_RANK()` leaves no gaps (e.g. 1, 2, 2, 3)",
                explanation="RANK leaves numeric gaps following tied values; DENSE_RANK assigns consecutive numbers without gaps."
            ),
            QuizQuestionBlueprint(
                question="Which window function accesses attribute values from the immediately preceding row in the window?",
                options=[
                    "LAG()",
                    "LEAD()",
                    "PREV_ROW()",
                    "BEFORE()"
                ],
                correct_answer="LAG()",
                explanation="`LAG(col, offset)` peers backward into earlier rows within the partition."
            ),
            QuizQuestionBlueprint(
                question="What clause inside `OVER(...)` divides rows into separate calculation buckets (similar to GROUP BY)?",
                options=[
                    "PARTITION BY",
                    "SPLIT BY",
                    "CHUNK_ON",
                    "BUCKET_KEY"
                ],
                correct_answer="PARTITION BY",
                explanation="`PARTITION BY` divides rows into partitions where window calculations restart independently."
            ),
            QuizQuestionBlueprint(
                question="Can window functions be placed directly inside a `WHERE` clause (e.g. `WHERE ROW_NUMBER() = 1`)?",
                options=[
                    "No, because WHERE executes before window functions; you must wrap the query in a CTE or subquery first",
                    "Yes, window functions can be placed anywhere",
                    "Only in MySQL 8.0",
                    "Only on columns with primary keys"
                ],
                correct_answer="No, because WHERE executes before window functions; you must wrap the query in a CTE or subquery first",
                explanation="Window functions evaluate after WHERE in SQL query pipeline; filtering on them requires wrapping in a CTE."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 20
    # -------------------------------------------------------------
    DayBlueprint(
        order=20,
        title="Day 20: SQL Views (Virtual Tables & Materialized Views)",
        concept="Encapsulating complex queries, securing sensitive columns, and boosting read performance with Views and Materialized Views",
        analogy="Think of an SQL View like a stained-glass security window into a bank vault. When customers look through the window, they can only see the teller desks and promotional flyers; they cannot see the private vault safe boxes, passwords, or customer balance ledgers hidden behind the frosted glass. A **Materialized View** is like taking a snapshot photo of that view every morning at 8:00 AM so you don't even have to walk up to the glass to see who is on duty!",
        theory_sections=[
            {
                "heading": "Standard Views: Saved Virtual Queries",
                "body": "A standard **View** is a saved SQL query that acts as a virtual table. It stores zero physical data on disk; whenever a user queries `SELECT * FROM my_view`, the database engine rewrites the query, executing the underlying definition on the fly. Views simplify complex schemas and provide column-level access control (e.g. hiding `password_hash` and `salary`)."
            },
            {
                "heading": "Materialized Views: Physical Caching for High-Speed Analytics",
                "body": "A **Materialized View** physically persists the query result set to disk and can be indexed just like a standard table. It provides lightning-fast reads on multi-million row analytical reports. Because it does not update automatically on base table writes, it must be periodically refreshed using `REFRESH MATERIALIZED VIEW`."
            }
        ],
        code_snippets=[
            {
                "title": "Creating a Security-Restricted User View (Hiding Sensitive Columns)",
                "language": "sql",
                "code": "-- Base table contains sensitive salary and password hashes\nCREATE VIEW public_employee_directory AS\nSELECT \n    id,\n    first_name || ' ' || last_name AS full_name,\n    email,\n    department\nFROM employees\nWHERE is_active = TRUE;\n\n-- Junior developers or API tokens are granted SELECT on the VIEW only\n-- GRANT SELECT ON public_employee_directory TO app_user;",
                "explanation": "Views mask sensitive columns from unauthorized application users while providing a clean query interface."
            },
            {
                "title": "Querying and Filtering a Virtual View",
                "language": "sql",
                "code": "-- Queries against views are rewritten by the query optimizer on the fly\nSELECT full_name, email\nFROM public_employee_directory\nWHERE department = 'Engineering'\nORDER BY full_name ASC;",
                "explanation": "Views behave exactly like regular tables in SELECT queries, abstracting complex joins and filters."
            },
            {
                "title": "Creating an Indexed Materialized View for Heavy Analytics",
                "language": "sql",
                "code": "-- Materialized views physically write query results to disk\nCREATE MATERIALIZED VIEW mv_monthly_sales_summary AS\nSELECT \n    DATE_TRUNC('month', order_date) AS sales_month,\n    category,\n    COUNT(*) AS total_orders,\n    SUM(amount) AS total_revenue\nFROM orders\nGROUP BY DATE_TRUNC('month', order_date), category\nWITH DATA;\n\n-- Create an index directly on the materialized view for ultra-fast lookup\nCREATE UNIQUE INDEX idx_mv_sales ON mv_monthly_sales_summary (sales_month, category);",
                "explanation": "Materialized views persist heavy aggregation outputs to disk and can have indexes attached directly."
            },
            {
                "title": "Refreshing a Materialized View Concurrently",
                "language": "sql",
                "code": "-- Refreshes the materialized view data without locking read queries\nREFRESH MATERIALIZED VIEW CONCURRENTLY mv_monthly_sales_summary;",
                "explanation": "`REFRESH MATERIALIZED VIEW CONCURRENTLY` updates cached records in the background without blocking readers."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="View Definition SQL Generator",
            description="Write a Python function `create_view_sql(view_name: str, select_query: str, materialized: bool = False) -> str` that produces a valid `CREATE [MATERIALIZED] VIEW` statement.",
            starter_code="def create_view_sql(view_name: str, select_query: str, materialized: bool = False) -> str:\n    # Generate CREATE VIEW or CREATE MATERIALIZED VIEW statement\n    pass",
            solution_code="def create_view_sql(view_name: str, select_query: str, materialized: bool = False) -> str:\n    view_type = 'MATERIALIZED VIEW' if materialized else 'VIEW'\n    clean_query = select_query.strip().rstrip(';')\n    return f\"CREATE {view_type} {view_name} AS {clean_query};\"",
            expected_output="create_view_sql('v_active', 'SELECT * FROM users') == 'CREATE VIEW v_active AS SELECT * FROM users;'"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Does a standard SQL View consume physical storage space for its data rows on disk?",
                options=[
                    "No, a standard View is a virtual table that executes its underlying query dynamically whenever requested",
                    "Yes, it duplicates all data rows onto disk",
                    "Yes, but only 50% of the data",
                    "It consumes disk space only on Sundays"
                ],
                correct_answer="No, a standard View is a virtual table that executes its underlying query dynamically whenever requested",
                explanation="Standard views store only the query definition in the data dictionary, consuming no row storage."
            ),
            QuizQuestionBlueprint(
                question="What is the critical difference between a standard View and a Materialized View?",
                options=[
                    "A Materialized View physically saves the query result set to disk and can be indexed, requiring periodic refreshes",
                    "A Materialized View cannot use the SELECT keyword",
                    "A standard View only works on numbers",
                    "There is no difference in any SQL dialect"
                ],
                correct_answer="A Materialized View physically saves the query result set to disk and can be indexed, requiring periodic refreshes",
                explanation="Materialized views store physical rows on disk for instant reading, requiring manual or scheduled refreshes."
            ),
            QuizQuestionBlueprint(
                question="What security benefit do Views provide in production database management?",
                options=[
                    "They allow granting access to specific columns and filtered rows without exposing sensitive columns (like password hashes or salaries) to app users",
                    "They encrypt the server's hard drive automatically",
                    "They prevent users from using weak passwords",
                    "They block all hacker IP addresses"
                ],
                correct_answer="They allow granting access to specific columns and filtered rows without exposing sensitive columns (like password hashes or salaries) to app users",
                explanation="Views provide robust column and row-level security boundaries, masking sensitive data."
            ),
            QuizQuestionBlueprint(
                question="What SQL command updates the data stored inside a PostgreSQL Materialized View?",
                options=[
                    "REFRESH MATERIALIZED VIEW",
                    "UPDATE VIEW_DATA",
                    "RELOAD CACHE",
                    "SYNC VIEW"
                ],
                correct_answer="REFRESH MATERIALIZED VIEW",
                explanation="`REFRESH MATERIALIZED VIEW view_name` recalculates and stores the updated query results."
            ),
            QuizQuestionBlueprint(
                question="What does the `CONCURRENTLY` flag achieve when running `REFRESH MATERIALIZED VIEW CONCURRENTLY` in PostgreSQL?",
                options=[
                    "It refreshes the view without locking it against incoming SELECT read queries",
                    "It doubles the CPU speed of the server",
                    "It converts the view into an Excel spreadsheet",
                    "It deletes all old tables"
                ],
                correct_answer="It refreshes the view without locking it against incoming SELECT read queries",
                explanation="CONCURRENTLY updates the cached view without taking exclusive read locks, keeping production APIs fast."
            )
        ]
    )
]
