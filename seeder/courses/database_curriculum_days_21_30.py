"""
Database Management 40-Day Curriculum - Module 5 (Part 2), Module 6 & Module 7 (Part 1) (Days 21 to 30)
Module 5: Database Programmability (Days 21-23)
Module 6: Transactions & Concurrency (Days 24-28)
Module 7: Performance Tuning & Optimization (Days 29-30)
"""

from seeder.course_blueprint import DayBlueprint, QuizQuestionBlueprint, CodingChallengeBlueprint

DAYS_21_TO_30 = [
    # -------------------------------------------------------------
    # DAY 21
    # -------------------------------------------------------------
    DayBlueprint(
        order=21,
        title="Day 21: Stored Procedures - Pre-Compiled SQL Execution",
        concept="Encapsulating complex multi-step business logic, parameters, transaction management, and execution security inside the database engine",
        analogy="Think of a Stored Procedure like a programmable microwave button labeled 'Popcorn'. Instead of manually setting the power to 80%, setting the timer to 2 minutes 30 seconds, turning on the turntable, and listening for popping sounds every single time you want a snack, you simply press the 'Popcorn' button (`CALL make_popcorn()`). The microwave runs the pre-programmed steps automatically!",
        theory_sections=[
            {
                "heading": "Why Use Stored Procedures?",
                "body": "Stored Procedures are compiled, reusable routines stored directly in the database catalog. They offer major architectural advantages: (1) **Reduced Network Traffic**: A single procedure call replaces 20 individual SQL roundtrips between the web backend and database server; (2) **Security**: Applications can be granted execute permissions on specific procedures without granting direct access to underlying tables; (3) **Pre-Compilation**: The database parses, optimizes, and caches the execution plan."
            },
            {
                "heading": "Procedures vs Functions",
                "body": "In modern SQL (ANSI / PostgreSQL / MySQL), the key difference between a Procedure and a Function is transaction control: **Stored Procedures can control transactions internally** (`COMMIT` and `ROLLBACK`), whereas scalar functions cannot manage independent transaction blocks and are primarily intended to compute and return a value within expressions."
            }
        ],
        code_snippets=[
            {
                "title": "Creating a Stored Procedure in PostgreSQL (PL/pgSQL)",
                "language": "sql",
                "code": "CREATE OR REPLACE PROCEDURE transfer_funds(\n    sender_id INT,\n    receiver_id INT,\n    transfer_amount DECIMAL(10, 2)\n)\nLANGUAGE plpgsql\nAS $$\nBEGIN\n    -- Deduct from sender with balance check\n    UPDATE accounts \n    SET balance = balance - transfer_amount \n    WHERE id = sender_id AND balance >= transfer_amount;\n\n    IF NOT FOUND THEN\n        RAISE EXCEPTION 'Insufficient funds in sender account %', sender_id;\n    END IF;\n\n    -- Credit receiver account\n    UPDATE accounts \n    SET balance = balance + transfer_amount \n    WHERE id = receiver_id;\n\n    -- Procedures can explicitly control transactions!\n    COMMIT;\nEND;\n$$;",
                "explanation": "Stored procedures encapsulate multi-statement workflows and error handling directly inside the database."
            },
            {
                "title": "Executing a Stored Procedure with CALL",
                "language": "sql",
                "code": "-- Invoke the procedure passing positional arguments\nCALL transfer_funds(101, 204, 250.00);\n\n-- Inspect account balances after procedure execution\nSELECT id, balance FROM accounts WHERE id IN (101, 204);",
                "explanation": "Stored procedures are invoked using the `CALL` statement with arguments."
            },
            {
                "title": "Procedure with INOUT Parameters (Returning Status)",
                "language": "sql",
                "code": "CREATE OR REPLACE PROCEDURE register_user(\n    IN p_username VARCHAR,\n    IN p_email VARCHAR,\n    OUT p_user_id INT,\n    OUT p_status VARCHAR\n)\nLANGUAGE plpgsql\nAS $$\nBEGIN\n    INSERT INTO users (username, email)\n    VALUES (p_username, p_email)\n    RETURNING id INTO p_user_id;\n    \n    p_status := 'SUCCESS';\nEXCEPTION\n    WHEN unique_violation THEN\n        p_status := 'DUPLICATE_EMAIL';\n        p_user_id := NULL;\nEND;\n$$;",
                "explanation": "Procedures can output multiple variables using `OUT` or `INOUT` parameters."
            },
            {
                "title": "Calling Stored Procedure from Python Backend (Psycopg2 / SQLAlchemy)",
                "language": "python",
                "code": "import psycopg2\n\nconn = psycopg2.connect('dbname=bank user=postgres')\ncur = conn.cursor()\n\n# Safely call database stored procedure via parameterized driver\ncur.execute('CALL transfer_funds(%s, %s, %s);', (101, 204, 250.00))\nconn.commit()\ncur.close()\nconn.close()",
                "explanation": "Application backends invoke procedures cleanly, shielding API servers from raw table SQL."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Stored Procedure SQL Call Formatter",
            description="Write a Python function `build_call_procedure_sql(proc_name: str, args: list) -> str` that formats a valid SQL `CALL <name>(<args>);` string, formatting strings in single quotes and numbers as raw literals.",
            starter_code="def build_call_procedure_sql(proc_name: str, args: list) -> str:\n    # Format CALL procedure SQL statement\n    pass",
            solution_code="def build_call_procedure_sql(proc_name: str, args: list) -> str:\n    formatted_args = []\n    for a in args:\n        if isinstance(a, str):\n            formatted_args.append(f\"'{a}'\")\n        else:\n            formatted_args.append(str(a))\n    return f\"CALL {proc_name}({', '.join(formatted_args)});\"",
            expected_output="build_call_procedure_sql('send_alert', ['user1', 42]) == \"CALL send_alert('user1', 42);\""
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What SQL statement is used to execute a Stored Procedure?",
                options=[
                    "CALL procedure_name(arguments);",
                    "SELECT procedure_name(arguments);",
                    "EXECUTE_TABLE procedure_name;",
                    "RUN procedure_name;"
                ],
                correct_answer="CALL procedure_name(arguments);",
                explanation="In standard SQL and PostgreSQL, stored procedures are executed using the `CALL` keyword."
            ),
            QuizQuestionBlueprint(
                question="What is a major architectural advantage of using Stored Procedures?",
                options=[
                    "They reduce network latency by bundling multiple queries into a single database trip and provide strict execution security",
                    "They eliminate the need for hard drives",
                    "They make all queries run on the user's mobile browser",
                    "They allow writing SQL without learning syntax"
                ],
                correct_answer="They reduce network latency by bundling multiple queries into a single database trip and provide strict execution security",
                explanation="Stored procedures minimize network roundtrips between backend and database while isolating table permissions."
            ),
            QuizQuestionBlueprint(
                question="What is the critical capability that Stored Procedures have which User-Defined Functions (UDFs) typically lack?",
                options=[
                    "The ability to manage and commit transactions (COMMIT and ROLLBACK) internally",
                    "The ability to use numbers",
                    "The ability to run on Linux servers",
                    "The ability to use uppercase letters"
                ],
                correct_answer="The ability to manage and commit transactions (COMMIT and ROLLBACK) internally",
                explanation="Procedures can initiate and commit transactions; standard functions cannot contain COMMIT/ROLLBACK blocks."
            ),
            QuizQuestionBlueprint(
                question="Where are Stored Procedures stored and pre-compiled?",
                options=[
                    "Directly inside the database server's system catalog / dictionary",
                    "In the user's browser localStorage",
                    "On a USB stick",
                    "Inside a CSS file"
                ],
                correct_answer="Directly inside the database server's system catalog / dictionary",
                explanation="Stored procedures are compiled and maintained within the database engine's system catalog."
            ),
            QuizQuestionBlueprint(
                question="What type of parameter allows a stored procedure to return values back to the calling client?",
                options=[
                    "OUT or INOUT parameters",
                    "STATIC parameters",
                    "CONST parameters",
                    "IMPORT parameters"
                ],
                correct_answer="OUT or INOUT parameters",
                explanation="OUT and INOUT parameters allow procedures to populate and pass return values back to callers."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 22
    # -------------------------------------------------------------
    DayBlueprint(
        order=22,
        title="Day 22: User-Defined Functions (UDFs - Scalar & Table-Valued)",
        concept="Writing reusable procedural functions: Scalar UDFs, Table-Valued Functions (TVFs), determinism, and performance implications",
        analogy="Think of a User-Defined Function (UDF) like a custom formula in an Excel spreadsheet. If Excel doesn't have a built-in button for 'Calculate Pakistani Income Tax with Rebate', you write your own custom macro: `=CALCULATE_TAX(salary)`. You can now drop that formula into 10,000 cells across your spreadsheet (`SELECT name, CALCULATE_TAX(salary) FROM employees`), computing results instantly!",
        theory_sections=[
            {
                "heading": "Scalar vs Table-Valued Functions (TVFs)",
                "body": "A **Scalar UDF** accepts input arguments and returns a single discrete value (e.g. formatting a phone number or calculating sales tax). It can be used anywhere an expression is valid (SELECT list, WHERE clause). A **Table-Valued Function (TVF)** returns an entire set of rows (a virtual relation) that can be queried like a table or joined using `LATERAL` joins."
            },
            {
                "heading": "Determinism: IMMUTABLE, STABLE, and VOLATILE",
                "body": "In PostgreSQL and modern engines, function optimization depends on volatility: (1) `IMMUTABLE` functions always produce the identical output for identical inputs (e.g. `celsius_to_fahrenheit(x)`) and can be indexed! (2) `STABLE` functions cannot modify data and produce consistent results within a single transaction scan (e.g. reading current exchange rates). (3) `VOLATILE` functions can change at any instant (e.g. `random()` or `clock_timestamp()`)."
            }
        ],
        code_snippets=[
            {
                "title": "Creating an IMMUTABLE Scalar Function (Tax Calculator)",
                "language": "sql",
                "code": "CREATE OR REPLACE FUNCTION calculate_sales_tax(\n    net_amount DECIMAL,\n    tax_rate DECIMAL DEFAULT 0.15\n)\nRETURNS DECIMAL\nLANGUAGE plpgsql\nIMMUTABLE -- Informs optimizer that output depends purely on inputs\nAS $$\nBEGIN\n    IF net_amount <= 0 THEN\n        RETURN 0.00;\n    END IF;\n    RETURN ROUND(net_amount * tax_rate, 2);\nEND;\n$$;",
                "explanation": "An IMMUTABLE scalar function returning a single calculated numerical result."
            },
            {
                "title": "Using a Scalar Function in SELECT Queries",
                "language": "sql",
                "code": "-- Calling custom scalar UDF directly inside the SELECT projection\nSELECT \n    id,\n    product_name,\n    price,\n    calculate_sales_tax(price, 0.16) AS tax_amount,\n    price + calculate_sales_tax(price, 0.16) AS gross_total\nFROM products;",
                "explanation": "Scalar functions evaluate for each row, seamlessly integrating into SQL expressions."
            },
            {
                "title": "Table-Valued Function (TVF) Returning a Set of Rows",
                "language": "sql",
                "code": "CREATE OR REPLACE FUNCTION get_high_earners_by_dept(dept_name VARCHAR)\nRETURNS TABLE(\n    emp_id INT,\n    full_name VARCHAR,\n    monthly_salary DECIMAL\n)\nLANGUAGE plpgsql\nAS $$\nBEGIN\n    RETURN QUERY\n    SELECT id, name, salary\n    FROM employees\n    WHERE department = dept_name AND salary > 75000.00;\nEND;\n$$;",
                "explanation": "A Table-Valued Function returns an active table result set that can be queried."
            },
            {
                "title": "Querying and Joining a Table-Valued Function",
                "language": "sql",
                "code": "-- Querying a TVF like a real physical table\nSELECT * FROM get_high_earners_by_dept('Engineering');\n\n-- Joining with LATERAL\nSELECT d.dept_name, e.full_name, e.monthly_salary\nFROM departments d\nCROSS JOIN LATERAL get_high_earners_by_dept(d.dept_name) e;",
                "explanation": "TVFs can be queried directly in the FROM clause or combined via LATERAL joins."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Scalar UDF Determinism Classifier",
            description="Write a Python function `classify_function_volatility(is_pure_math: bool, accesses_clock: bool, accesses_db_state: bool) -> str` that returns `'IMMUTABLE'` if pure math with no clock or db state, `'STABLE'` if accesses db state but no clock, and `'VOLATILE'` if accesses clock.",
            starter_code="def classify_function_volatility(is_pure_math: bool, accesses_clock: bool, accesses_db_state: bool) -> str:\n    # Return PostgreSQL volatility classification\n    pass",
            solution_code="def classify_function_volatility(is_pure_math: bool, accesses_clock: bool, accesses_db_state: bool) -> str:\n    if accesses_clock:\n        return 'VOLATILE'\n    if accesses_db_state:\n        return 'STABLE'\n    if is_pure_math:\n        return 'IMMUTABLE'\n    return 'VOLATILE'",
            expected_output="classify_function_volatility(True, False, False) == 'IMMUTABLE', classify_function_volatility(False, True, False) == 'VOLATILE'"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the difference between a Scalar UDF and a Table-Valued Function (TVF)?",
                options=[
                    "A Scalar UDF returns a single discrete value; a TVF returns an entire table (set of rows)",
                    "A Scalar UDF only works on text; a TVF only works on numbers",
                    "A TVF can only be used by database administrators",
                    "There is no difference"
                ],
                correct_answer="A Scalar UDF returns a single discrete value; a TVF returns an entire table (set of rows)",
                explanation="Scalar functions return one value (like a float or string); TVFs return virtual row sets."
            ),
            QuizQuestionBlueprint(
                question="Why is marking a function as `IMMUTABLE` in PostgreSQL beneficial for performance?",
                options=[
                    "The query optimizer can pre-evaluate constant calls and use the function in expression indexes",
                    "It prevents the function from ever being deleted",
                    "It speeds up internet connection speeds",
                    "It forces the CPU to run at maximum clock speed"
                ],
                correct_answer="The query optimizer can pre-evaluate constant calls and use the function in expression indexes",
                explanation="IMMUTABLE guarantees that same inputs yield same outputs, enabling indexing and pre-evaluation."
            ),
            QuizQuestionBlueprint(
                question="Can a User-Defined Function be called directly inside an SQL `SELECT` list (e.g. `SELECT calculate_tax(price) FROM products`)?",
                options=[
                    "Yes, scalar functions can be used anywhere an expression is valid",
                    "No, functions can only be executed in Python",
                    "Only if the table has fewer than 5 rows",
                    "Only on MySQL"
                ],
                correct_answer="Yes, scalar functions can be used anywhere an expression is valid",
                explanation="Scalar UDFs act as expressions, evaluating dynamically across projected rows."
            ),
            QuizQuestionBlueprint(
                question="What happens if a complex, slow scalar UDF is placed inside a `WHERE` clause on a 1,000,000-row table without an index?",
                options=[
                    "The function executes 1,000,000 times (row-by-row), causing massive query latency",
                    "The query finishes in 1 microsecond automatically",
                    "The database crashes and restarts",
                    "The rows are converted to JSON"
                ],
                correct_answer="The function executes 1,000,000 times (row-by-row), causing massive query latency",
                explanation="Non-indexed UDFs in WHERE clauses incur costly row-by-row execution penalties."
            ),
            QuizQuestionBlueprint(
                question="What does a `VOLATILE` function classification mean in PostgreSQL?",
                options=[
                    "The function's output can vary even for identical inputs within the same query (e.g. random() or clock_timestamp())",
                    "The function is likely to corrupt the database",
                    "The function was written in C++",
                    "The function cannot accept parameters"
                ],
                correct_answer="The function's output can vary even for identical inputs within the same query (e.g. random() or clock_timestamp())",
                explanation="VOLATILE functions can return different results on consecutive calls, preventing query plan caching."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 23
    # -------------------------------------------------------------
    DayBlueprint(
        order=23,
        title="Day 23: Database Triggers - Event-Based Automation",
        concept="Automating audit logs, enforcing complex business rules, and managing automatic state synchronizations using BEFORE and AFTER triggers",
        analogy="Think of a database trigger like an automated home burglar alarm system. You don't have to remember to hire a security guard to manually inspect your window every second. The moment a burglar tries to open the window (an `INSERT`, `UPDATE`, or `DELETE` event), the tripwire sensor fires automatically (`TRIGGER`), captures a security snapshot, sounds the siren, and logs the intruder's entry timestamp into the police ledger!",
        theory_sections=[
            {
                "heading": "How Database Triggers Operate",
                "body": "A Trigger is a special procedural block that automatically executes in response to specific DML events (`INSERT`, `UPDATE`, or `DELETE`) on a specified table. Triggers can fire **BEFORE** an action (ideal for data validation, scrubbing, or assigning computed values to `NEW.column`) or **AFTER** an action (ideal for writing audit logs and updating denormalized counters)."
            },
            {
                "heading": "The NEW and OLD Special Records",
                "body": "Inside trigger execution scopes, two pseudo-records exist: `NEW` represents the newly inserted or updated state of the row; `OLD` represents the pre-update or pre-deletion state. In an `INSERT` trigger, only `NEW` exists. In a `DELETE` trigger, only `OLD` exists. In an `UPDATE` trigger, both `NEW` and `OLD` are available, making change tracking effortless."
            }
        ],
        code_snippets=[
            {
                "title": "BEFORE Trigger for Data Sanitization and Automatic Timestamping",
                "language": "sql",
                "code": "CREATE OR REPLACE FUNCTION sanitize_user_input()\nRETURNS TRIGGER AS $$\nBEGIN\n    -- Scrub whitespace and force lowercase on email\n    NEW.email := LOWER(TRIM(NEW.email));\n    NEW.updated_at := CURRENT_TIMESTAMP;\n    RETURN NEW; -- Returns modified row to be written to disk\nEND;\n$$ LANGUAGE plpgsql;\n\nCREATE TRIGGER trg_before_user_insert_or_update\nBEFORE INSERT OR UPDATE ON users\nFOR EACH ROW\nEXECUTE FUNCTION sanitize_user_input();",
                "explanation": "BEFORE triggers intercept the row prior to disk persistence, sanitizing attributes directly on NEW."
            },
            {
                "title": "AFTER Trigger for Comprehensive Security Audit Logging",
                "language": "sql",
                "code": "CREATE TABLE audit_logs (\n    log_id SERIAL PRIMARY KEY,\n    table_name VARCHAR(50),\n    operation VARCHAR(10),\n    record_id INT,\n    old_data JSONB,\n    new_data JSONB,\n    performed_by VARCHAR(50),\n    performed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP\n);\n\nCREATE OR REPLACE FUNCTION log_employee_changes()\nRETURNS TRIGGER AS $$\nBEGIN\n    INSERT INTO audit_logs (table_name, operation, record_id, old_data, new_data, performed_by)\n    VALUES (\n        'employees',\n        TG_OP,\n        COALESCE(NEW.id, OLD.id),\n        CASE WHEN TG_OP IN ('UPDATE', 'DELETE') THEN to_jsonb(OLD) ELSE NULL END,\n        CASE WHEN TG_OP IN ('INSERT', 'UPDATE') THEN to_jsonb(NEW) ELSE NULL END,\n        CURRENT_USER\n    );\n    RETURN NULL; -- AFTER triggers ignore return value\nEND;\n$$ LANGUAGE plpgsql;\n\nCREATE TRIGGER trg_audit_employees\nAFTER INSERT OR UPDATE OR DELETE ON employees\nFOR EACH ROW\nEXECUTE FUNCTION log_employee_changes();",
                "explanation": "AFTER triggers reliably capture historical diffs (OLD vs NEW) in an immutable audit ledger."
            },
            {
                "title": "Testing Trigger In Action with DML Operations",
                "language": "sql",
                "code": "-- Insert row with messy email casing\nINSERT INTO users (username, email) VALUES ('zainab', '  ZAINAB@Hunar.App  ');\n\n-- Inspect: BEFORE trigger automatically cleaned email to 'zainab@hunar.app'\nSELECT username, email, updated_at FROM users WHERE username = 'zainab';",
                "explanation": "Verifies that the BEFORE trigger executed transparently during the INSERT statement."
            },
            {
                "title": "Dropping a Trigger Safely",
                "language": "sql",
                "code": "-- Drop the trigger binding while keeping the underlying function\nDROP TRIGGER IF EXISTS trg_audit_employees ON employees;\n\n-- Drop the trigger function if no longer needed\nDROP FUNCTION IF EXISTS log_employee_changes();",
                "explanation": "Removes the trigger attachment from the table schema cleanly."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Trigger Pseudo-Record Availability Checker",
            description="Write a Python function `get_trigger_records(operation: str) -> dict[str, bool]` that returns a dictionary `{'NEW': bool, 'OLD': bool}` indicating whether `NEW` and `OLD` are populated for `'INSERT'`, `'UPDATE'`, and `'DELETE'` operations.",
            starter_code="def get_trigger_records(operation: str) -> dict[str, bool]:\n    # Return {'NEW': bool, 'OLD': bool}\n    pass",
            solution_code="def get_trigger_records(operation: str) -> dict[str, bool]:\n    op = operation.strip().upper()\n    if op == 'INSERT':\n        return {'NEW': True, 'OLD': False}\n    elif op == 'DELETE':\n        return {'NEW': False, 'OLD': True}\n    elif op == 'UPDATE':\n        return {'NEW': True, 'OLD': True}\n    return {'NEW': False, 'OLD': False}",
            expected_output="get_trigger_records('INSERT') == {'NEW': True, 'OLD': False}, get_trigger_records('UPDATE') == {'NEW': True, 'OLD': True}"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the difference between a `BEFORE` trigger and an `AFTER` trigger in SQL?",
                options=[
                    "`BEFORE` triggers run before row data is written to disk (ideal for sanitizing NEW values); `AFTER` triggers run after the write succeeds (ideal for audit logs)",
                    "`BEFORE` triggers delete rows; `AFTER` triggers insert rows",
                    "`BEFORE` triggers can only run on Sundays",
                    "There is no difference in database execution"
                ],
                correct_answer="`BEFORE` triggers run before row data is written to disk (ideal for sanitizing NEW values); `AFTER` triggers run after the write succeeds (ideal for audit logs)",
                explanation="BEFORE triggers inspect/modify data before disk persistence; AFTER triggers handle secondary side-effects."
            ),
            QuizQuestionBlueprint(
                question="Which special pseudo-record holds the state of a row *prior* to an UPDATE or DELETE operation?",
                options=[
                    "OLD",
                    "NEW",
                    "PREV",
                    "BEFORE"
                ],
                correct_answer="OLD",
                explanation="The `OLD` pseudo-record contains pre-modification column values."
            ),
            QuizQuestionBlueprint(
                question="In an `INSERT` trigger, what will accessing `OLD.column_name` evaluate to?",
                options=[
                    "NULL (or undefined, since no prior row existed)",
                    "The number 0",
                    "The primary key of the server",
                    "An automatic database error"
                ],
                correct_answer="NULL (or undefined, since no prior row existed)",
                explanation="Newly inserted rows have no preceding record; hence OLD is NULL."
            ),
            QuizQuestionBlueprint(
                question="What does `FOR EACH ROW` specify in a trigger definition?",
                options=[
                    "The trigger fires once for every individual row modified by the SQL statement",
                    "The trigger only executes on the first row of the table",
                    "The trigger converts the table to CSV",
                    "The trigger loops indefinitely"
                ],
                correct_answer="The trigger fires once for every individual row modified by the SQL statement",
                explanation="Row-level triggers execute once for each row affected; statement-level triggers execute once per query."
            ),
            QuizQuestionBlueprint(
                question="Why can excessive or unmonitored triggers become an architectural antipattern?",
                options=[
                    "They execute hidden 'magic' side effects that complicate debugging and slow down high-throughput batch writes",
                    "They cause the physical computer screen to flicker",
                    "They double the cost of cloud hosting automatically",
                    "They are strictly prohibited in enterprise software"
                ],
                correct_answer="They execute hidden 'magic' side effects that complicate debugging and slow down high-throughput batch writes",
                explanation="Hidden cascading trigger chains make code difficult to trace and introduce write-latency overhead."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 24
    # -------------------------------------------------------------
    DayBlueprint(
        order=24,
        title="Day 24: ACID Properties - Atomicity, Consistency, Isolation, Durability",
        concept="The four sacred pillars of enterprise database reliability: guaranteeing data correctness during crashes, power failures, and concurrent updates",
        analogy="Think of ACID like transferring money at a bank ATM. You want to send $500 from your account to your friend. **Atomicity**: Either $500 leaves your account AND arrives in their account, or nothing happens at all (never lost in limbo). **Consistency**: The total money in the bank remains mathematically balanced. **Isolation**: If 10 people send money simultaneously, each transaction acts as if it's the only one happening. **Durability**: The moment the ATM prints your receipt, an earthquake could cut the power, but your transfer is etched in stone!",
        theory_sections=[
            {
                "heading": "Atomicity and Consistency Defined",
                "body": "**Atomicity (All-or-Nothing)** guarantees that a transaction composed of multiple operations is treated as a single indivisible unit; if any statement fails, the entire transaction is rolled back. **Consistency** ensures that a transaction can only transition the database from one valid state to another, maintaining all schema constraints, foreign keys, and business invariants."
            },
            {
                "heading": "Isolation and Durability Mechanics",
                "body": "**Isolation** prevents concurrent transactions from interfering with each other, dictating how uncommitted changes are visible to other connections. **Durability** guarantees that once a transaction commits, its modifications are permanently recorded in non-volatile storage (via the Write-Ahead Log - WAL) and survive system crashes or power outages."
            }
        ],
        code_snippets=[
            {
                "title": "Demonstrating Atomicity: All or Nothing Rollback",
                "language": "sql",
                "code": "BEGIN;\n-- Step 1: Debit Alice\nUPDATE bank_accounts SET balance = balance - 500 WHERE id = 1;\n\n-- Step 2: Attempt to credit an invalid non-existent account\nUPDATE bank_accounts SET balance = balance + 500 WHERE id = 99999;\n\n-- If Step 2 fails, ROLLBACK cancels Step 1 completely!\n-- Alice loses $0 and balance remains safe\nROLLBACK;",
                "explanation": "Atomicity guarantees that partial operations are completely undone upon failure."
            },
            {
                "title": "Enforcing Consistency Through Database Invariants",
                "language": "sql",
                "code": "-- Table schema enforcing non-negative account balances\nCREATE TABLE bank_accounts (\n    id SERIAL PRIMARY KEY,\n    owner VARCHAR(50) NOT NULL,\n    balance DECIMAL(12, 2) NOT NULL CHECK (balance >= 0.00)\n);\n\n-- If a transaction attempts to withdraw more than available balance,\n-- the CHECK constraint rejects it, preserving database Consistency!\n-- UPDATE bank_accounts SET balance = balance - 1000 WHERE id = 1; -- ERROR!",
                "explanation": "Consistency ensures the database never enters an illegal state violating constraints."
            },
            {
                "title": "Write-Ahead Logging (WAL): The Engine of Durability",
                "language": "sql",
                "code": "-- Inspecting PostgreSQL Write-Ahead Log (WAL) status\nSELECT pg_current_wal_lsn(), pg_walfile_name(pg_current_wal_lsn());\n\n-- Durability ensures WAL buffers are flushed (fsync) to disk before\n-- the client receives a 'COMMIT SUCCESS' acknowledgment.",
                "explanation": "Durability relies on write-ahead logging flushed to non-volatile disk blocks."
            },
            {
                "title": "Transactional Money Transfer Script (Atomic Execution)",
                "language": "sql",
                "code": "BEGIN;\nUPDATE bank_accounts SET balance = balance - 100 WHERE id = 1;\nUPDATE bank_accounts SET balance = balance + 100 WHERE id = 2;\nCOMMIT; -- Both steps permanently sealed together!",
                "explanation": "The standard atomic transaction pattern committing dual updates together."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="ACID Acronym Property Matcher",
            description="Write a Python function `explain_acid_letter(letter: str) -> str` that maps `'A'`, `'C'`, `'I'`, and `'D'` to their full name and brief definition (e.g. `'Atomicity - All or nothing'`). Return `'Unknown'` for invalid letters.",
            starter_code="def explain_acid_letter(letter: str) -> str:\n    # Return description of ACID component\n    pass",
            solution_code="def explain_acid_letter(letter: str) -> str:\n    mapping = {\n        'A': 'Atomicity - All or nothing',\n        'C': 'Consistency - Preserves constraints',\n        'I': 'Isolation - Independent concurrent execution',\n        'D': 'Durability - Survives crashes and power loss'\n    }\n    return mapping.get(letter.strip().upper(), 'Unknown')",
            expected_output="explain_acid_letter('A') == 'Atomicity - All or nothing', explain_acid_letter('D') == 'Durability - Survives crashes and power loss'"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What does 'Atomicity' guarantee in a database transaction?",
                options=[
                    "All operations within the transaction succeed together, or the entire transaction is rolled back with zero changes applied (all-or-nothing)",
                    "Data is stored at the molecular sub-atomic level",
                    "Transactions execute at nuclear speeds",
                    "Tables can only have one row"
                ],
                correct_answer="All operations within the transaction succeed together, or the entire transaction is rolled back with zero changes applied (all-or-nothing)",
                explanation="Atomicity guarantees indivisibility: all operations commit, or all roll back."
            ),
            QuizQuestionBlueprint(
                question="What does 'Durability' ensure after a client receives a successful COMMIT confirmation?",
                options=[
                    "The committed changes are recorded in persistent storage (e.g. WAL on disk) and will survive server crashes or power failures",
                    "The hard drive will physically never break",
                    "The database password can never be changed",
                    "The data is replicated to the cloud for free"
                ],
                correct_answer="The committed changes are recorded in persistent storage (e.g. WAL on disk) and will survive server crashes or power failures",
                explanation="Durability guarantees that committed data is written to non-volatile disk structures."
            ),
            QuizQuestionBlueprint(
                question="Which mechanism do relational databases (like PostgreSQL and SQLite) use to guarantee Durability and Crash Recovery?",
                options=[
                    "WAL (Write-Ahead Logging)",
                    "HTML caching",
                    "JavaScript promises",
                    "Browser cookies"
                ],
                correct_answer="WAL (Write-Ahead Logging)",
                explanation="Write-Ahead Logging records transaction changes sequentially to disk before dirty pages are written."
            ),
            QuizQuestionBlueprint(
                question="What does 'Consistency' mean in the context of ACID?",
                options=[
                    "Transactions only take the database from one valid state to another, strictly satisfying all schema rules and constraints",
                    "All users must use the same font size",
                    "Every table must have the same number of rows",
                    "The database server must never reboot"
                ],
                correct_answer="Transactions only take the database from one valid state to another, strictly satisfying all schema rules and constraints",
                explanation="Consistency ensures database invariants, constraints, and relational rules are never violated."
            ),
            QuizQuestionBlueprint(
                question="What does 'Isolation' in ACID prevent?",
                options=[
                    "Concurrent transactions from interfering with each other or reading uncommitted, intermediate corrupted states",
                    "Users from accessing the database via internet",
                    "Servers from communicating across networks",
                    "Backups from being restored"
                ],
                correct_answer="Concurrent transactions from interfering with each other or reading uncommitted, intermediate corrupted states",
                explanation="Isolation ensures that concurrent transactions execute as if they were running serially."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 25
    # -------------------------------------------------------------
    DayBlueprint(
        order=25,
        title="Day 25: Transaction Controls (BEGIN, COMMIT, ROLLBACK & SAVEPOINT)",
        concept="Controlling transaction lifecycle explicitly: initiating transactions, committing state, rolling back errors, and setting partial rollback checkpoints with SAVEPOINT",
        analogy="Think of transaction controls like playing a difficult video game with save checkpoints. You enter a dangerous dungeon boss fight (`BEGIN TRANSACTION`). If you defeat the boss and collect the treasure, you save your progress permanently (`COMMIT`). If the boss destroys your character, you restart back at the dungeon entrance as if you never stepped inside (`ROLLBACK`). A `SAVEPOINT` is like a mid-battle checkpoint where you can reload if you get poisoned without restarting the entire dungeon!",
        theory_sections=[
            {
                "heading": "Transaction Demarcation Statements",
                "body": "A transaction begins with `BEGIN` (or `START TRANSACTION`). Once opened, all subsequent DML statements execute inside a private transaction buffer visible only to the active connection. Calling `COMMIT` makes the changes permanent and visible to all other database connections. Calling `ROLLBACK` aborts the transaction, reverting all changes made since `BEGIN`."
            },
            {
                "heading": "Savepoints: Granular Partial Rollbacks",
                "body": "In long-running or complex batch transactions, an error in statement #15 would ordinarily abort all 14 preceding successful steps. `SAVEPOINT point_name` establishes a named bookmark within the transaction. Using `ROLLBACK TO SAVEPOINT point_name` undoes only the actions taken after that checkpoint, allowing the preceding steps to proceed to final `COMMIT`."
            }
        ],
        code_snippets=[
            {
                "title": "Standard Transaction with Explicit COMMIT",
                "language": "sql",
                "code": "BEGIN;\n\nINSERT INTO orders (customer_id, total_amount)\nVALUES (42, 199.99);\n\nUPDATE inventory \nSET stock = stock - 1 \nWHERE product_id = 101;\n\n-- Make all updates permanent\nCOMMIT;",
                "explanation": "Groups order creation and inventory reduction into an atomic, committed transaction."
            },
            {
                "title": "Aborting Changes with ROLLBACK",
                "language": "sql",
                "code": "BEGIN;\n\nDELETE FROM audit_records WHERE created_at < '2020-01-01';\n\n-- Oh no, we accidentally targeted the wrong table or range!\n-- Undo everything instantly:\nROLLBACK;\n\n-- Records remain intact and un-deleted!",
                "explanation": "ROLLBACK discards uncommitted modifications, restoring the exact pre-transaction state."
            },
            {
                "title": "Partial Rollbacks Using SAVEPOINT",
                "language": "sql",
                "code": "BEGIN;\n\nINSERT INTO customers (name, email) VALUES ('Sara', 'sara@hunar.app');\n\n-- Create a checkpoint bookmark\nSAVEPOINT before_optional_bonus;\n\n-- Try an optional promotional credit that might fail\nINSERT INTO user_bonuses (user_email, bonus_code) VALUES ('sara@hunar.app', 'EXPIRED_2024');\n\n-- If the bonus code is invalid, rollback to checkpoint without losing the customer!\nROLLBACK TO SAVEPOINT before_optional_bonus;\n\n-- Release the savepoint and commit the customer registration\nCOMMIT;",
                "explanation": "SAVEPOINT allows partial rollbacks, letting earlier successful operations survive and commit."
            },
            {
                "title": "Transaction Handling in Python with Automatic Context Managers",
                "language": "python",
                "code": "import psycopg2\n\nconn = psycopg2.connect('dbname=store user=postgres')\n\n# Context manager automatically executes BEGIN and COMMIT;\n# If an exception occurs, it automatically triggers ROLLBACK!\ntry:\n    with conn:\n        with conn.cursor() as cur:\n            cur.execute('UPDATE accounts SET balance = balance - 50 WHERE id = %s', (1,))\n            cur.execute('UPDATE accounts SET balance = balance + 50 WHERE id = %s', (2,))\n    print('Transaction successfully committed!')\nexcept Exception as e:\n    print(f'Transaction rolled back due to error: {e}')\nfinally:\n    conn.close()",
                "explanation": "Python database context managers automate BEGIN, COMMIT, and ROLLBACK lifecycle management."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Transaction Command Validator",
            description="Write a Python function `is_valid_transaction_control(cmd: str) -> bool` that verifies whether a string (case-insensitive) is one of `'BEGIN'`, `'START TRANSACTION'`, `'COMMIT'`, `'ROLLBACK'`, or starts with `'SAVEPOINT'`.",
            starter_code="def is_valid_transaction_control(cmd: str) -> bool:\n    # Verify valid TCL statement\n    pass",
            solution_code="def is_valid_transaction_control(cmd: str) -> bool:\n    c = cmd.strip().upper()\n    valid_commands = {'BEGIN', 'START TRANSACTION', 'COMMIT', 'ROLLBACK'}\n    return c in valid_commands or c.startswith('SAVEPOINT ')",
            expected_output="is_valid_transaction_control('BEGIN') == True, is_valid_transaction_control('SAVEPOINT sp1') == True"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What SQL command marks the beginning of an explicit transaction block?",
                options=[
                    "BEGIN (or START TRANSACTION)",
                    "OPEN DATABASE",
                    "CREATE TRANSACTION",
                    "INIT SESSION"
                ],
                correct_answer="BEGIN (or START TRANSACTION)",
                explanation="`BEGIN` or `START TRANSACTION` opens an explicit transaction context."
            ),
            QuizQuestionBlueprint(
                question="What happens to uncommitted changes if a database server experiences a sudden power cut during a transaction?",
                options=[
                    "During crash recovery on reboot, the database automatically rolls back all uncommitted transactions",
                    "The database commits half of the changes",
                    "The changes are emailed to the administrator",
                    "The hard drive must be formatted"
                ],
                correct_answer="During crash recovery on reboot, the database automatically rolls back all uncommitted transactions",
                explanation="Crash recovery parses the Write-Ahead Log and rolls back any incomplete uncommitted transactions."
            ),
            QuizQuestionBlueprint(
                question="What is the purpose of a `SAVEPOINT` in SQL?",
                options=[
                    "To create a named checkpoint inside a transaction allowing partial rollback without aborting the entire transaction",
                    "To save the database to an external thumb drive",
                    "To pause the query for 10 seconds",
                    "To print table data to a PDF"
                ],
                correct_answer="To create a named checkpoint inside a transaction allowing partial rollback without aborting the entire transaction",
                explanation="SAVEPOINT allows fine-grained error recovery via `ROLLBACK TO SAVEPOINT`."
            ),
            QuizQuestionBlueprint(
                question="What SQL command permanently saves all changes made during the transaction and releases locks?",
                options=[
                    "COMMIT",
                    "SAVE",
                    "PERSIST",
                    "FLUSH_ALL"
                ],
                correct_answer="COMMIT",
                explanation="`COMMIT` makes modifications permanent and visible to all other database sessions."
            ),
            QuizQuestionBlueprint(
                question="What is 'Autocommit' mode in database client connections?",
                options=[
                    "A default mode where every single SQL statement is treated as its own independent transaction and committed immediately",
                    "A mode that automatically writes code using AI",
                    "A setting that prohibits DELETE statements",
                    "A tool for backing up tables to GitHub"
                ],
                correct_answer="A default mode where every single SQL statement is treated as its own independent transaction and committed immediately",
                explanation="Autocommit automatically executes an implicit COMMIT after every single SQL command."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 26
    # -------------------------------------------------------------
    DayBlueprint(
        order=26,
        title="Day 26: Concurrency Control - Multi-User Edits & Race Conditions",
        concept="Preventing concurrent data corruption: Dirty Reads, Non-Repeatable Reads, Phantom Reads, Lost Updates, and Pessimistic vs Optimistic Locking",
        analogy="Think of database concurrency like two people trying to buy the very last concert ticket seat online at the exact same millisecond. If the ticketing database doesn't manage concurrency, both users' credit cards get charged, but only one seat exists—causing customer outrage (a classic **Lost Update / Race Condition**). Concurrency control locks the seat temporarily so only one buyer completes the purchase cleanly!",
        theory_sections=[
            {
                "heading": "The Four Classic Concurrency Anomalies",
                "body": "When thousands of concurrent transactions access the same rows without proper controls, anomalies arise: (1) **Lost Updates** (two transactions overwrite each other's changes); (2) **Dirty Reads** (Transaction A reads uncommitted changes from Transaction B that are later rolled back); (3) **Non-Repeatable Reads** (Transaction A re-reads a row and finds modified column values); (4) **Phantom Reads** (Transaction A re-runs a range query and discovers newly inserted rows that match the filter)."
            },
            {
                "heading": "Pessimistic vs Optimistic Concurrency Control",
                "body": "**Pessimistic Locking** assumes conflicts will happen and locks rows immediately using `SELECT ... FOR UPDATE` (blocking other writers until commit). **Optimistic Locking** assumes conflicts are rare, attaching a `version` integer column to the row. On write, it executes `UPDATE ... WHERE id = 1 AND version = 5`; if the version changed, the write aborts and retries in the application."
            }
        ],
        code_snippets=[
            {
                "title": "Pessimistic Row Locking with SELECT FOR UPDATE",
                "language": "sql",
                "code": "BEGIN;\n-- Acquire exclusive lock on ticket row #42; other transactions wait\nSELECT seat_number, status, price\nFROM concert_tickets\nWHERE id = 42\nFOR UPDATE;\n\n-- Safely update status knowing no other thread can touch row #42\nUPDATE concert_tickets\nSET status = 'sold', buyer_id = 999\nWHERE id = 42;\n\nCOMMIT; -- Releases lock",
                "explanation": "`FOR UPDATE` prevents race conditions by placing an exclusive row-level lock on the selected tuples."
            },
            {
                "title": "Optimistic Locking with Version Numbers",
                "language": "sql",
                "code": "-- Step 1: Client reads product row (version = 3)\n-- SELECT id, name, price, version FROM products WHERE id = 101;\n\n-- Step 2: Client submits update checking that version is still 3\nUPDATE products\nSET \n    price = 89.99,\n    version = version + 1 -- Increment version\nWHERE id = 101 AND version = 3;\n\n-- If rows_affected == 0, another user modified the row first! (Conflict detected)",
                "explanation": "Optimistic locking avoids database-level locks, verifying version numbers on write."
            },
            {
                "title": "Shared Locks (FOR SHARE) vs Exclusive Locks (FOR UPDATE)",
                "language": "sql",
                "code": "-- Shared lock: allows other connections to READ, but blocks them from UPDATING/DELETING\nSELECT * FROM system_settings WHERE key = 'maintenance_mode' FOR SHARE;\n\n-- Exclusive lock: blocks both concurrent reads and concurrent writes\nSELECT * FROM accounts WHERE id = 10 FOR UPDATE;",
                "explanation": "FOR SHARE permits concurrent readers; FOR UPDATE enforces exclusive single-writer access."
            },
            {
                "title": "Non-Blocking Lock Attempt with SKIP LOCKED (Job Queues)",
                "language": "sql",
                "code": "-- Workers process background queue tasks without stepping on each other\nBEGIN;\nSELECT task_id, payload\nFROM background_tasks\nWHERE status = 'pending'\nORDER BY task_id ASC\nLIMIT 1\nFOR UPDATE SKIP LOCKED;\n\n-- The worker instantly skips rows already locked by other worker threads!\nCOMMIT;",
                "explanation": "`SKIP LOCKED` enables building high-throughput worker job queues without thread contention."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Optimistic Lock Query Builder",
            description="Write a Python function `build_optimistic_update(table: str, row_id: int, current_version: int, new_val: str) -> str` that produces a version-checked UPDATE SQL query incrementing `version`.",
            starter_code="def build_optimistic_update(table: str, row_id: int, current_version: int, new_val: str) -> str:\n    # Generate optimistic locking UPDATE query\n    pass",
            solution_code="def build_optimistic_update(table: str, row_id: int, current_version: int, new_val: str) -> str:\n    return f\"UPDATE {table} SET data = '{new_val}', version = version + 1 WHERE id = {row_id} AND version = {current_version};\"",
            expected_output="build_optimistic_update('items', 1, 2, 'fresh') == \"UPDATE items SET data = 'fresh', version = version + 1 WHERE id = 1 AND version = 2;\""
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is a 'Lost Update' anomaly in concurrent database systems?",
                options=[
                    "When two simultaneous transactions overwrite the same row and the second write overwrites the first without incorporating its changes",
                    "When a user forgets their password",
                    "When an operating system update fails to download",
                    "When an index file is erased"
                ],
                correct_answer="When two simultaneous transactions overwrite the same row and the second write overwrites the first without incorporating its changes",
                explanation="Lost updates occur when concurrent writes blind-overwrite each other's calculations."
            ),
            QuizQuestionBlueprint(
                question="What SQL clause in PostgreSQL and MySQL acquires an exclusive row lock on read to prevent race conditions?",
                options=[
                    "FOR UPDATE",
                    "LOCK ALL ROWS",
                    "FREEZE TABLE",
                    "HALT EXECUTION"
                ],
                correct_answer="FOR UPDATE",
                explanation="`SELECT ... FOR UPDATE` locks matching rows exclusively until transaction commit/rollback."
            ),
            QuizQuestionBlueprint(
                question="How does Optimistic Concurrency Control detect write conflicts?",
                options=[
                    "By verifying that a `version` or `timestamp` column on the row has not changed since it was originally read",
                    "By guessing user intentions with machine learning",
                    "By holding locks on the entire database 24/7",
                    "By asking the user to confirm via email"
                ],
                correct_answer="By verifying that a `version` or `timestamp` column on the row has not changed since it was originally read",
                explanation="Optimistic locking checks whether the row version matches the initial read snapshot."
            ),
            QuizQuestionBlueprint(
                question="What is a 'Dirty Read'?",
                options=[
                    "When a transaction reads uncommitted changes from another transaction that are subsequently rolled back",
                    "When reading data from a damaged hard drive",
                    "When a table has missing column headers",
                    "When a query contains profanity"
                ],
                correct_answer="When a transaction reads uncommitted changes from another transaction that are subsequently rolled back",
                explanation="A dirty read occurs when uncommitted, temporary state is read and later invalidated by a rollback."
            ),
            QuizQuestionBlueprint(
                question="What does `SKIP LOCKED` do when querying job queues with `FOR UPDATE`?",
                options=[
                    "It automatically skips rows currently locked by other concurrent workers rather than blocking and waiting",
                    "It bypasses all database passwords",
                    "It deletes locked rows immediately",
                    "It prints a warning in the terminal"
                ],
                correct_answer="It automatically skips rows currently locked by other concurrent workers rather than blocking and waiting",
                explanation="`SKIP LOCKED` allows multi-threaded workers to grab unassigned tasks without contention."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 27
    # -------------------------------------------------------------
    DayBlueprint(
        order=27,
        title="Day 27: Transaction Isolation Levels (Read Uncommitted to Serializable)",
        concept="Analyzing the ANSI SQL isolation spectrum: Read Uncommitted, Read Committed, Repeatable Read, and Serializable guarantees",
        analogy="Think of isolation levels like noise-canceling headphones with different settings on an airplane. **Read Uncommitted** is taking off the headphones completely (you hear every draft whisper, cough, and fake sneeze from other passengers). **Read Committed** lets you hear passengers only when they speak clearly on the intercom. **Repeatable Read** puts on high-grade noise cancellation. **Serializable** places you in an isolated private soundproof jet cabin where nobody else exists!",
        theory_sections=[
            {
                "heading": "The 4 ANSI SQL Isolation Levels",
                "body": "The SQL standard defines 4 levels trading concurrency speed against anomaly protection: (1) **Read Uncommitted**: lowest isolation, permits dirty reads. (2) **Read Committed** (default in PostgreSQL and Oracle): prevents dirty reads; queries see only committed data. (3) **Repeatable Read** (default in MySQL InnoDB): guarantees that re-reading a row yields identical values; prevents non-repeatable reads. (4) **Serializable**: highest isolation, guarantees execution matches some serial order, eliminating phantom reads."
            },
            {
                "heading": "MVCC: Multi-Version Concurrency Control",
                "body": "Modern engines like PostgreSQL do not lock tables for read queries. Instead, they use **MVCC**: readers never block writers, and writers never block readers. When a row is updated, PostgreSQL writes a new version of the row with transaction timestamps (`xmin`, `xmax`), allowing concurrent transactions to view historical snapshots corresponding to their isolation level."
            }
        ],
        code_snippets=[
            {
                "title": "Setting Transaction Isolation Level in SQL",
                "language": "sql",
                "code": "-- Setting isolation level for a specific transaction block\nBEGIN TRANSACTION ISOLATION LEVEL REPEATABLE READ;\n\nSELECT balance FROM accounts WHERE id = 101;\n-- Even if another transaction commits an update to id=101 right now,\n-- repeating this SELECT in this transaction will return the exact same balance!\nSELECT balance FROM accounts WHERE id = 101;\n\nCOMMIT;",
                "explanation": "REPEATABLE READ locks the snapshot view at transaction start, preventing non-repeatable reads."
            },
            {
                "title": "Configuring Global or Session Default Isolation Level",
                "language": "sql",
                "code": "-- Check current session isolation level\nSHOW default_transaction_isolation;\n\n-- Set session default to SERIALIZABLE for financial compliance\nSET SESSION CHARACTERISTICS AS TRANSACTION ISOLATION LEVEL SERIALIZABLE;",
                "explanation": "Allows configuring default isolation constraints across sessions."
            },
            {
                "title": "Handling Serialization Failures in Application Code",
                "language": "python",
                "code": "# In SERIALIZABLE isolation, the database will throw serialization errors (40001)\n# if it detects conflicting dependency cycles. Applications MUST retry!\nimport psycopg2\nimport time\n\ndef execute_with_retry(conn, max_retries=3):\n    for attempt in range(max_retries):\n        try:\n            with conn:\n                with conn.cursor() as cur:\n                    cur.execute('SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;')\n                    cur.execute('UPDATE inventory SET stock = stock - 1 WHERE id = 1;')\n            return True\n        except psycopg2.errors.SerializationFailure:\n            time.sleep(0.05 * (2 ** attempt)) # Exponential backoff retry\n    raise Exception('Serialization retry limit exceeded')",
                "explanation": "Serializable isolation demands retry logic in application backends to handle serialization failures."
            },
            {
                "title": "Inspecting Row MVCC Metadata in PostgreSQL (xmin, xmax)",
                "language": "sql",
                "code": "-- Hidden system columns tracking row versions under MVCC\nSELECT xmin, xmax, id, name, salary \nFROM employees \nWHERE id = 1;",
                "explanation": "xmin and xmax track transaction IDs that created and expired specific row versions."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Isolation Anomaly Matrix Lookup",
            description="Write a Python function `can_anomaly_occur(isolation_level: str, anomaly: str) -> bool` for anomalies `'dirty_read'`, `'non_repeatable_read'`, and `'phantom_read'` across levels `'read_uncommitted'`, `'read_committed'`, `'repeatable_read'`, and `'serializable'`.",
            starter_code="def can_anomaly_occur(isolation_level: str, anomaly: str) -> bool:\n    # Return True if anomaly is possible in specified isolation level\n    pass",
            solution_code="def can_anomaly_occur(isolation_level: str, anomaly: str) -> bool:\n    matrix = {\n        'read_uncommitted': {'dirty_read': True, 'non_repeatable_read': True, 'phantom_read': True},\n        'read_committed': {'dirty_read': False, 'non_repeatable_read': True, 'phantom_read': True},\n        'repeatable_read': {'dirty_read': False, 'non_repeatable_read': False, 'phantom_read': False},\n        'serializable': {'dirty_read': False, 'non_repeatable_read': False, 'phantom_read': False}\n    }\n    lvl = isolation_level.strip().lower()\n    anom = anomaly.strip().lower()\n    return matrix.get(lvl, {}).get(anom, False)",
            expected_output="can_anomaly_occur('read_committed', 'dirty_read') == False, can_anomaly_occur('read_committed', 'non_repeatable_read') == True"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the default transaction isolation level in PostgreSQL?",
                options=[
                    "Read Committed",
                    "Read Uncommitted",
                    "Repeatable Read",
                    "Serializable"
                ],
                correct_answer="Read Committed",
                explanation="PostgreSQL defaults to Read Committed, ensuring queries view only committed transactions."
            ),
            QuizQuestionBlueprint(
                question="Which isolation level provides the strongest possible consistency, completely eliminating all concurrency anomalies?",
                options=[
                    "Serializable",
                    "Repeatable Read",
                    "Read Committed",
                    "Read Uncommitted"
                ],
                correct_answer="Serializable",
                explanation="Serializable guarantees transaction outcomes match a strictly sequential, serial schedule."
            ),
            QuizQuestionBlueprint(
                question="What is Multi-Version Concurrency Control (MVCC)?",
                options=[
                    "A concurrency mechanism where readers do not block writers and writers do not block readers by maintaining multiple snapshot versions of rows",
                    "A tool for managing Git repositories inside SQL",
                    "A system that limits tables to version 1.0",
                    "A way to run multiple versions of Linux on one server"
                ],
                correct_answer="A concurrency mechanism where readers do not block writers and writers do not block readers by maintaining multiple snapshot versions of rows",
                explanation="MVCC avoids read/write locking contention by serving snapshot versions of tuples."
            ),
            QuizQuestionBlueprint(
                question="What anomaly is eliminated when upgrading from `Read Committed` to `Repeatable Read`?",
                options=[
                    "Non-Repeatable Reads (where re-reading a row inside the same transaction yields modified values from other commits)",
                    "Division by zero errors",
                    "Server memory leaks",
                    "Power outages"
                ],
                correct_answer="Non-Repeatable Reads (where re-reading a row inside the same transaction yields modified values from other commits)",
                explanation="Repeatable Read freezes the snapshot view, guaranteeing identical reads across the transaction."
            ),
            QuizQuestionBlueprint(
                question="What must an application backend be prepared to do when running transactions in `Serializable` isolation?",
                options=[
                    "Catch serialization failure exceptions (SQLSTATE 40001) and retry the transaction",
                    "Restart the entire operating system",
                    "Send an SMS to the user",
                    "Convert all numbers to strings"
                ],
                correct_answer="Catch serialization failure exceptions (SQLSTATE 40001) and retry the transaction",
                explanation="Serializable engines abort transactions that form dependency cycles, requiring application-level retries."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 28
    # -------------------------------------------------------------
    DayBlueprint(
        order=28,
        title="Day 28: Deadlocks - Identification, Resolution & Prevention",
        concept="Diagnosing circular lock dependencies, automated deadlock detection algorithms, and architectural prevention strategies",
        analogy="Think of a database deadlock like two stubborn motorists meeting on an extremely narrow single-lane bridge. Car A moves onto the bridge and blocks Car B. Car B moves onto the bridge and blocks Car A. Neither driver can move forward, and neither driver will back up. They are frozen forever! A deadlock detector is the traffic police officer who immediately spots the circular freeze, orders Car A to back off (aborts and rolls back one transaction), allowing Car B to cross smoothly!",
        theory_sections=[
            {
                "heading": "The Mechanics of a Deadlock",
                "body": "A Deadlock occurs when two or more transactions hold locks on resources that the other transactions need to proceed, forming a circular wait dependency. For example: Transaction 1 locks Account A and requests Account B; Transaction 2 simultaneously locks Account B and requests Account A. Neither can progress, resulting in an indefinite freeze."
            },
            {
                "heading": "Detection and Prevention Strategies",
                "body": "Relational database engines run background deadlock detection daemons that construct **Wait-For Graphs**. If a directed cycle is discovered, the engine automatically breaks the deadlock by choosing a 'victim' transaction and aborting it with a deadlock error (`deadlock detected`). **Prevention**: Always access and lock resources in a strictly consistent, identical global order across all application code (e.g. always sort IDs before locking)."
            }
        ],
        code_snippets=[
            {
                "title": "The Classic Deadlock Scenario (Two Concurrent Transactions)",
                "language": "sql",
                "code": "-- Transaction 1:\nBEGIN;\nUPDATE accounts SET balance = balance - 10 WHERE id = 1; -- Locks Row 1\n-- (Pauses while Transaction 2 runs)\nUPDATE accounts SET balance = balance + 10 WHERE id = 2; -- Waits for Row 2!\n\n-- Transaction 2 (simultaneously):\nBEGIN;\nUPDATE accounts SET balance = balance - 20 WHERE id = 2; -- Locks Row 2\n-- (Tries to update Row 1)\nUPDATE accounts SET balance = balance + 20 WHERE id = 1; -- Waits for Row 1!\n-- DEADLOCK OCCURS! Engine terminates one transaction with error 40P01.",
                "explanation": "Illustrates how cross-locking resources in opposite orders triggers circular lock deadlocks."
            },
            {
                "title": "Architectural Prevention: Consistent Resource Ordering",
                "language": "python",
                "code": "# Golden Rule of Deadlock Prevention: Always lock resources in uniform order!\ndef transfer_money_safely(cursor, sender_id, receiver_id, amount):\n    # Sort account IDs to guarantee every transaction acquires locks in identical order\n    first_id, second_id = sorted([sender_id, receiver_id])\n    \n    # Lock in sorted order -> Deadlock is mathematically IMPOSSIBLE!\n    cursor.execute('SELECT * FROM accounts WHERE id = %s FOR UPDATE;', (first_id,))\n    cursor.execute('SELECT * FROM accounts WHERE id = %s FOR UPDATE;', (second_id,))\n    \n    cursor.execute('UPDATE accounts SET balance = balance - %s WHERE id = %s;', (amount, sender_id))\n    cursor.execute('UPDATE accounts SET balance = balance + %s WHERE id = %s;', (amount, receiver_id))",
                "explanation": "Sorting IDs prior to locking guarantees all threads acquire locks in identical sequence, preventing cycles."
            },
            {
                "title": "Inspecting Active Locks and Blocked Queries in PostgreSQL",
                "language": "sql",
                "code": "-- Query PostgreSQL lock catalog to view blocked processes\nSELECT \n    blocked_locks.pid AS blocked_pid,\n    blocking_locks.pid AS blocking_pid,\n    blocked_activity.query AS blocked_statement,\n    blocking_activity.query AS blocking_statement\nFROM pg_catalog.pg_locks blocked_locks\nJOIN pg_catalog.pg_stat_activity blocked_activity ON blocked_activity.pid = blocked_locks.pid\nJOIN pg_catalog.pg_locks blocking_locks \n    ON blocking_locks.locktype = blocked_locks.locktype\n    AND blocking_locks.database IS NOT DISTINCT FROM blocked_locks.database\n    AND blocking_locks.relation IS NOT DISTINCT FROM blocked_locks.relation\n    AND blocking_locks.page IS NOT DISTINCT FROM blocked_locks.page\n    AND blocking_locks.tuple IS NOT DISTINCT FROM blocked_locks.tuple\n    AND blocking_locks.pid != blocked_locks.pid\nJOIN pg_catalog.pg_stat_activity blocking_activity ON blocking_activity.pid = blocking_locks.pid\nWHERE NOT blocked_locks.granted;",
                "explanation": "Diagnostic query to identify blocking sessions and investigate deadlock root causes."
            },
            {
                "title": "Configuring Deadlock Timeout Settings",
                "language": "sql",
                "code": "-- In postgresql.conf or session: check for deadlocks after 1 second of waiting\nSET deadlock_timeout = '1s';\n\n-- Setting statement lock timeout to avoid indefinite hanging\nSET lock_timeout = '5s';",
                "explanation": "Configures how aggressively the engine runs the Wait-For graph cycle detection algorithm."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Lock Order Sorter for Deadlock Prevention",
            description="Write a Python function `get_safe_lock_sequence(resource_ids: list[int]) -> list[int]` that removes duplicates and returns the unique integer IDs sorted in ascending order.",
            starter_code="def get_safe_lock_sequence(resource_ids: list[int]) -> list[int]:\n    # Return deduplicated, sorted list of resource IDs\n    pass",
            solution_code="def get_safe_lock_sequence(resource_ids: list[int]) -> list[int]:\n    return sorted(list(set(resource_ids)))",
            expected_output="get_safe_lock_sequence([5, 2, 8, 2, 1]) == [1, 2, 5, 8]"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What causes a Deadlock in a database system?",
                options=[
                    "A circular wait condition where two or more transactions hold locks on resources the other transactions need to proceed",
                    "A hard drive running out of free space",
                    "A user forgetting their database password",
                    "An SQL query with missing semicolons"
                ],
                correct_answer="A circular wait condition where two or more transactions hold locks on resources the other transactions need to proceed",
                explanation="Deadlocks occur when transactions form a circular dependency loop, each waiting for locks held by the other."
            ),
            QuizQuestionBlueprint(
                question="How does an RDBMS engine (like PostgreSQL) resolve a deadlock once detected?",
                options=[
                    "It automatically chooses one transaction as a 'victim', aborts it with an error, and rolls it back so the other transaction can complete",
                    "It shuts down the server hardware immediately",
                    "It deletes all rows in the affected tables",
                    "It locks the computer indefinitely"
                ],
                correct_answer="It automatically chooses one transaction as a 'victim', aborts it with an error, and rolls it back so the other transaction can complete",
                explanation="The deadlock detection daemon terminates a victim transaction, breaking the circular dependency."
            ),
            QuizQuestionBlueprint(
                question="What is the most effective software architecture strategy to prevent deadlocks completely?",
                options=[
                    "Always acquire locks on multiple resources in a strictly uniform, consistent global order (e.g. sorted by ID)",
                    "Never use transactions under any circumstances",
                    "Run all database queries sequentially on a single thread",
                    "Reboot the server every 10 minutes"
                ],
                correct_answer="Always acquire locks on multiple resources in a strictly uniform, consistent global order (e.g. sorted by ID)",
                explanation="Locking resources in a consistent global order mathematically eliminates circular dependency wait cycles."
            ),
            QuizQuestionBlueprint(
                question="What data structure does the database engine maintain to detect deadlocks?",
                options=[
                    "A Wait-For Graph (WFG) where vertices represent transactions and directed edges represent lock dependencies",
                    "A linked list of audio files",
                    "A JSON cookie file",
                    "A binary search tree of passwords"
                ],
                correct_answer="A Wait-For Graph (WFG) where vertices represent transactions and directed edges represent lock dependencies",
                explanation="Deadlock detection traverses a Wait-For Graph to identify directed cycles."
            ),
            QuizQuestionBlueprint(
                question="What configuration parameter in PostgreSQL controls how long a blocked transaction waits before the engine triggers cycle detection?",
                options=[
                    "deadlock_timeout",
                    "max_freeze_time",
                    "wait_forever",
                    "cycle_breaker"
                ],
                correct_answer="deadlock_timeout",
                explanation="`deadlock_timeout` specifies the wait time before the background deadlock checker runs."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 29
    # -------------------------------------------------------------
    DayBlueprint(
        order=29,
        title="Day 29: Database Indexing - B-Tree, Hash, Clustered vs Non-Clustered",
        concept="Turbocharging queries from O(N) table scans to O(log N) index seeks: B-Tree architecture, Hash indexes, Clustered vs Non-Clustered storage, and Composite indexes",
        analogy="Think of a database index like the index at the back of a 1,000-page medical textbook. If you want to find 'Hypertension', you don't read all 1,000 pages line by line from page 1 (**Sequential Table Scan: O(N)**). You flip to the alphabetical index at the back, find 'Hypertension -> Page 412', and jump straight to page 412 in 2 seconds (**Index Seek: O(log N)**)!",
        theory_sections=[
            {
                "heading": "B-Tree vs Hash Indexes",
                "body": "The **B-Tree (Balanced Tree)** is the default and most versatile index structure. It maintains sorted keys in hierarchical nodes, delivering O(log N) lookups for equality (`=`), ranges (`BETWEEN`, `<`, `>`), and sorting (`ORDER BY`). A **Hash Index** uses hash tables, providing lightning-fast O(1) lookups strictly for equality checks (`=`), but cannot assist range queries or sorting."
            },
            {
                "heading": "Clustered vs Non-Clustered Indexes",
                "body": "A **Clustered Index** physically dictates the storage order of the actual table rows on disk. Because rows can only be sorted on disk in one physical way, a table can have **only ONE Clustered Index** (often the Primary Key in MySQL InnoDB or SQL Server). A **Non-Clustered Index** is a separate secondary B-Tree structure storing index keys and pointers back to the physical data rows."
            }
        ],
        code_snippets=[
            {
                "title": "Creating B-Tree and Hash Indexes in PostgreSQL",
                "language": "sql",
                "code": "-- Standard B-Tree index (Supports equality, ranges <, >, and ORDER BY)\nCREATE INDEX idx_users_email ON users(email);\n\n-- Dedicated Hash index (Ultra-fast equality lookup ONLY)\nCREATE INDEX idx_sessions_token ON user_sessions USING HASH(session_token);",
                "explanation": "B-Tree handles ranges and sorts; Hash indexes optimize pure equality lookups."
            },
            {
                "title": "Composite (Multi-Column) Index and Left-Prefix Rule",
                "language": "sql",
                "code": "-- Multi-column index on (department, salary)\nCREATE INDEX idx_emp_dept_salary ON employees(department, salary);\n\n-- Uses index efficiently (matches left prefix 'department'):\nSELECT * FROM employees WHERE department = 'Sales' AND salary > 50000;\n\n-- DOES NOT use index efficiently (violates left prefix rule by skipping department):\n-- SELECT * FROM employees WHERE salary > 50000;",
                "explanation": "Composite indexes require queries to filter on the leftmost indexed columns."
            },
            {
                "title": "Partial (Filtered) Index for Storage and Speed Optimization",
                "language": "sql",
                "code": "-- Indexes ONLY active users, keeping index size tiny and lightning fast\nCREATE INDEX idx_active_users ON users(email) \nWHERE is_active = TRUE AND is_deleted = FALSE;",
                "explanation": "Partial indexes index only rows matching a predicate, saving massive RAM and disk I/O."
            },
            {
                "title": "Inspecting Index Utilization and Size via System Statistics",
                "language": "sql",
                "code": "-- Check index physical disk size\nSELECT pg_size_pretty(pg_relation_size('idx_users_email')) AS index_size;\n\n-- Check how many times an index has been scanned\nSELECT relname, indexrelname, idx_scan, idx_tup_read, idx_tup_fetch\nFROM pg_stat_user_indexes\nWHERE indexrelname = 'idx_users_email';",
                "explanation": "System statistics confirm whether indexes are actively used by production queries."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Index Left-Prefix Rule Matcher",
            description="Write a Python function `uses_left_prefix(index_cols: list[str], query_cols: set[str]) -> bool` that verifies whether `query_cols` contains the first column (`index_cols[0]`) of the composite index.",
            starter_code="def uses_left_prefix(index_cols: list[str], query_cols: set[str]) -> bool:\n    # Return True if query adheres to left-prefix rule\n    pass",
            solution_code="def uses_left_prefix(index_cols: list[str], query_cols: set[str]) -> bool:\n    if not index_cols:\n        return False\n    return index_cols[0] in query_cols",
            expected_output="uses_left_prefix(['dept', 'salary'], {'dept'}) == True, uses_left_prefix(['dept', 'salary'], {'salary'}) == False"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the default index data structure used by relational database engines (PostgreSQL, MySQL, SQLite)?",
                options=[
                    "B-Tree (Balanced Tree)",
                    "Linked List",
                    "Red-Black Tree",
                    "Array"
                ],
                correct_answer="B-Tree (Balanced Tree)",
                explanation="B-Trees are the universal standard because they support equality, range queries, and ordering in O(log N) time."
            ),
            QuizQuestionBlueprint(
                question="How many Clustered Indexes can a single table have in an RDBMS?",
                options=[
                    "Exactly one, because physical rows on disk can only be stored in one sorted order",
                    "Unlimited",
                    "Up to 16",
                    "Zero; clustered indexes are not supported in relational databases"
                ],
                correct_answer="Exactly one, because physical rows on disk can only be stored in one sorted order",
                explanation="Clustered indexes dictate the physical layout of rows on disk, so only one can exist per table."
            ),
            QuizQuestionBlueprint(
                question="What is the trade-off of adding too many indexes to a table?",
                options=[
                    "Read queries speed up, but INSERT, UPDATE, and DELETE operations slow down because every index must be updated on each write",
                    "The database server runs out of IP addresses",
                    "Queries stop using WHERE clauses",
                    "Columns become read-only"
                ],
                correct_answer="Read queries speed up, but INSERT, UPDATE, and DELETE operations slow down because every index must be updated on each write",
                explanation="Every index incurs write overhead during DML operations and consumes additional disk storage."
            ),
            QuizQuestionBlueprint(
                question="If a composite index is created on `(country, city, postal_code)`, which query CANNOT use the index efficiently?",
                options=[
                    "`WHERE city = 'Karachi'` (violates the left-prefix rule by skipping `country`)",
                    "`WHERE country = 'Pakistan'`",
                    "`WHERE country = 'Pakistan' AND city = 'Karachi'`",
                    "`WHERE country = 'Pakistan' AND city = 'Karachi' AND postal_code = '75500'`"
                ],
                correct_answer="`WHERE city = 'Karachi'` (violates the left-prefix rule by skipping `country`)",
                explanation="Composite indexes require the query predicate to reference the leading (leftmost) column."
            ),
            QuizQuestionBlueprint(
                question="What is a 'Partial Index' in PostgreSQL?",
                options=[
                    "An index built over a subset of rows defined by a WHERE clause (e.g. `WHERE is_active = TRUE`)",
                    "An index that has been partially corrupted",
                    "An index that only stores half of each string",
                    "An index built only on odd-numbered days"
                ],
                correct_answer="An index built over a subset of rows defined by a WHERE clause (e.g. `WHERE is_active = TRUE`)",
                explanation="Partial indexes cover only rows matching a filter predicate, saving space and improving performance."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 30
    # -------------------------------------------------------------
    DayBlueprint(
        order=30,
        title="Day 30: Query Execution Plan Analysis (EXPLAIN & EXPLAIN ANALYZE)",
        concept="Reading the mind of the SQL Query Optimizer: Cost estimation, Sequential Scans, Index Scans, Bitmap Index Scans, and Execution Timings",
        analogy="Think of `EXPLAIN ANALYZE` like an X-ray machine and GPS telemetry tracker for your SQL query. Before driving a route, a GPS calculates estimated fuel and time (**EXPLAIN - Cost Estimation**). When you actually drive the route, the telemetry records your exact speed, red lights, and traffic jams at every intersection (**EXPLAIN ANALYZE - Actual Execution Runtime**). It reveals the exact bottleneck slowing down your system!",
        theory_sections=[
            {
                "heading": "The Cost-Based Query Optimizer (CBO)",
                "body": "When you issue a SQL query, the database engine parses it, generates dozens of alternative execution trees, and uses catalog statistics (`pg_statistic`) to choose the path with the lowest estimated **Cost**. Cost is an arbitrary unit where 1.0 roughly equals reading one sequential disk page."
            },
            {
                "heading": "EXPLAIN vs EXPLAIN ANALYZE",
                "body": "`EXPLAIN` displays the optimizer's estimated plan (cost, rows, width) without running the query. `EXPLAIN ANALYZE` actually executes the query, outputting real elapsed milliseconds (`actual time=...`), buffer cache hits/misses, and actual row counts. Reading plans reveals whether queries perform slow Sequential Scans (`Seq Scan`) or rapid Index Seeks (`Index Scan`)."
            }
        ],
        code_snippets=[
            {
                "title": "Generating an Execution Plan with EXPLAIN ANALYZE",
                "language": "sql",
                "code": "-- Runs the query and returns actual timing and buffer statistics\nEXPLAIN (ANALYZE, BUFFERS, VERBOSE)\nSELECT id, email, full_name\nFROM users\nWHERE email = 'bilal@hunar.app';",
                "explanation": "Outputs the actual execution tree, execution time in milliseconds, and memory buffer hits."
            },
            {
                "title": "Analyzing Sequential Scan (Seq Scan) Output",
                "language": "text",
                "code": "Seq Scan on users  (cost=0.00..1845.00 rows=1 width=64) (actual time=14.234..18.421 rows=1 loops=1)\n  Filter: ((email)::text = 'bilal@hunar.app'::text)\n  Rows Removed by Filter: 99999\nPlanning Time: 0.124 ms\nExecution Time: 18.462 ms",
                "explanation": "Indicates a full table scan: the database examined 100,000 rows because no index was present on email."
            },
            {
                "title": "Analyzing Index Scan (Index Scan) Output After Optimization",
                "language": "text",
                "code": "Index Scan using idx_users_email on users  (cost=0.29..8.30 rows=1 width=64) (actual time=0.042..0.045 rows=1 loops=1)\n  Index Cond: ((email)::text = 'bilal@hunar.app'::text)\nPlanning Time: 0.150 ms\nExecution Time: 0.068 ms -- Over 250x FASTER!",
                "explanation": "An index seek directly fetches the target row in 0.068 milliseconds."
            },
            {
                "title": "Updating Database Statistics with ANALYZE",
                "language": "sql",
                "code": "-- Informs query optimizer about recent data distribution changes\nANALYZE users;\n\n-- Vacuum and analyze entire database to maintain optimal planner stats\nVACUUM ANALYZE;",
                "explanation": "ANALYZE refreshes distribution histograms in the system catalog so the optimizer makes accurate plan decisions."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Execution Plan Bottleneck Detector",
            description="Write a Python function `detect_plan_bottlenecks(plan_text: str) -> list[str]` that inspects an EXPLAIN output string and flags `'Seq Scan detected'` if `'Seq Scan'` is present and `'High Cost detected'` if any cost exceeds 10000.",
            starter_code="def detect_plan_bottlenecks(plan_text: str) -> list[str]:\n    # Analyze plan string for bottlenecks\n    pass",
            solution_code="import re\n\ndef detect_plan_bottlenecks(plan_text: str) -> list[str]:\n    issues = []\n    if 'Seq Scan' in plan_text:\n        issues.append('Seq Scan detected')\n    costs = re.findall(r'cost=\\d+\\.\\d+\\.\\.(\\d+\\.\\d+)', plan_text)\n    if any(float(c) > 10000 for c in costs):\n        issues.append('High Cost detected')\n    return issues",
            expected_output="detect_plan_bottlenecks('Seq Scan on orders (cost=0.00..15000.00)') == ['Seq Scan detected', 'High Cost detected']"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the critical difference between `EXPLAIN` and `EXPLAIN ANALYZE` in PostgreSQL?",
                options=[
                    "`EXPLAIN` estimates the query plan without executing it; `EXPLAIN ANALYZE` actually executes the query to measure real elapsed time and row counts",
                    "`EXPLAIN` only works on numbers; `EXPLAIN ANALYZE` only works on text",
                    "`EXPLAIN ANALYZE` automatically creates missing indexes",
                    "There is no difference"
                ],
                correct_answer="`EXPLAIN` estimates the query plan without executing it; `EXPLAIN ANALYZE` actually executes the query to measure real elapsed time and row counts",
                explanation="EXPLAIN plans based on catalog statistics; EXPLAIN ANALYZE runs the query to measure real execution telemetry."
            ),
            QuizQuestionBlueprint(
                question="What does seeing a `Seq Scan` (Sequential Scan) on a 5,000,000-row table in an execution plan indicate?",
                options=[
                    "The database is reading every single row from disk sequentially because no suitable index was found or utilized",
                    "The query is running at maximum optimal speed",
                    "The table has been deleted",
                    "The database is running in memory"
                ],
                correct_answer="The database is reading every single row from disk sequentially because no suitable index was found or utilized",
                explanation="Seq Scan indicates an unindexed table scan, reading all pages from disk sequentially."
            ),
            QuizQuestionBlueprint(
                question="What command updates table statistics and histograms so the Query Optimizer makes intelligent execution plans?",
                options=[
                    "ANALYZE table_name;",
                    "OPTIMIZE_NOW;",
                    "REFRESH DATABASE;",
                    "CHECK STATS;"
                ],
                correct_answer="ANALYZE table_name;",
                explanation="`ANALYZE` updates data distribution statistics in system catalogs used by the Cost-Based Optimizer."
            ),
            QuizQuestionBlueprint(
                question="What is an 'Index Only Scan' in an execution plan?",
                options=[
                    "The query retrieved all requested columns directly from the index tree without ever having to touch the table heap on disk",
                    "An index that cannot be modified",
                    "A scan that only runs on primary keys",
                    "An error where indexes are missing"
                ],
                correct_answer="The query retrieved all requested columns directly from the index tree without ever having to touch the table heap on disk",
                explanation="Index Only Scans are the fastest possible queries: all selected attributes exist within the index itself."
            ),
            QuizQuestionBlueprint(
                question="What does the `BUFFERS` option display when combined with `EXPLAIN (ANALYZE, BUFFERS)`?",
                options=[
                    "The exact count of shared memory blocks read from cache (hit) versus read physically from disk (read)",
                    "The computer monitor buffer refresh rate",
                    "The network packet size",
                    "The length of the SQL text"
                ],
                correct_answer="The exact count of shared memory blocks read from cache (hit) versus read physically from disk (read)",
                explanation="BUFFERS reveals memory cache hits versus physical disk I/O reads."
            )
        ]
    )
]
