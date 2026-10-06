"""
debugging_curriculum_days_46_60.py
Days 46 to 60 for Debugging & Problem Solving 60-Day Course.
Covers:
- Module 8 (cont): Race Conditions & Deadlocks (Day 46), Infinite Loops (Day 47)
- Module 9: Production Level Debugging (Days 48-52) - Local Production Repro, Remote Debugging, Core Dumps, RCA & 5 Whys, Post-Mortems
- Module 10: Bug Prevention & Testing (Days 53-60) - Static Analysis & Linters, Code Reviews, Unit Testing, TDD, Integration Testing, E2E Testing, CI/CD Checks, Day 60 Capstone (The Great Bug Hunt)
"""

from seeder.course_blueprint import DayBlueprint

DAYS_46_TO_60 = [
    # ---------------------------------------------------------
    # Day 46: Race Conditions & Deadlocks (Concurrency Debugging)
    # ---------------------------------------------------------
    DayBlueprint(
        order=46,
        title="Day 46: Race Conditions & Deadlocks (Concurrency Debugging)",
        concept="Concurrency bugs occur when multiple asynchronous threads or processes read and write shared mutable memory in unpredictable sequences, creating non-deterministic state corruption (Race Conditions) or permanent freezing (Deadlocks).",
        analogy="Think of a single bank ATM shared by a husband and wife. The account has $100. At the exact same microsecond, the husband withdraws $100 from an ATM in New York while the wife withdraws $100 from an ATM in London. If the bank doesn't lock the account while processing, both machines dispense $100 and the account ends up with negative money (Race Condition).",
        theory_sections=[
            {
                "heading": "The Anatomy of a Race Condition (Check-Then-Act)",
                "content": (
                    "The most pervasive concurrency bug is the **Check-Then-Act flaw**:\n"
                    "1. Thread A checks: `if balance >= amount:` (True: $100 >= $100)\n"
                    "2. *Thread Context Switch occurs*\n"
                    "3. Thread B checks: `if balance >= amount:` (Still True: $100 >= $100)\n"
                    "4. Thread B acts: `balance -= 100` (Balance is now $0)\n"
                    "5. Thread A resumes and acts: `balance -= 100` (Balance is now -$100!)\n\n"
                    "**Solution: Mutual Exclusion (Mutex Locks)**: Wrap the critical section inside `with lock:` so only one thread can access the resource at a time."
                )
            },
            {
                "heading": "The 4 Coffman Conditions of a Deadlock",
                "content": (
                    "A deadlock can only occur if all 4 conditions hold simultaneously:\n"
                    "1. **Mutual Exclusion**: Resources cannot be shared.\n"
                    "2. **Hold and Wait**: A process holds resource A while waiting for resource B.\n"
                    "3. **No Preemption**: Resources cannot be forcibly taken away.\n"
                    "4. **Circular Wait**: Thread 1 waits for Thread 2, and Thread 2 waits for Thread 1.\n"
                    "**The Fix**: Always acquire locks in a strict, globally ordered sequence (Lock A before Lock B)."
                )
            },
            {
                "heading": "Why Concurrency Bugs Are 'Heisenbugs'",
                "content": (
                    "Named after Werner Heisenberg's uncertainty principle, a **Heisenbug** is a defect that disappears or changes behavior whenever you try to inspect it with a debugger or add a print statement, because printing alters thread timing."
                )
            }
        ],
        code_snippets=[
            {
                "title": "A Classic Race Condition in Python Threading",
                "language": "python",
                "code": (
                    "import threading, time\n\n"
                    "shared_balance = 100\n\n"
                    "def withdraw(amount):\n"
                    "    global shared_balance\n"
                    "    # Check\n"
                    "    if shared_balance >= amount:\n"
                    "        time.sleep(0.001) # Simulate tiny network or context switch delay\n"
                    "        # Act\n"
                    "        shared_balance -= amount\n\n"
                    "# 2 threads attempt to withdraw $100 concurrently from $100 balance\n"
                    "t1 = threading.Thread(target=withdraw, args=(100,))\n"
                    "t2 = threading.Thread(target=withdraw, args=(100,))\n"
                    "t1.start(); t2.start()\n"
                    "t1.join(); t2.join()\n"
                    "print(f'Final Balance: {shared_balance}') # Prints 0 or -100! (Race condition)"
                ),
                "explanation": "Illustrates Check-Then-Act race condition causing illegal overdraft."
            },
            {
                "title": "Fixing the Race Condition with a Threading Lock (Mutex)",
                "language": "python",
                "code": (
                    "import threading\n\n"
                    "shared_balance = 100\n"
                    "balance_lock = threading.Lock()\n\n"
                    "def safe_withdraw(amount):\n"
                    "    global shared_balance\n"
                    "    with balance_lock: # Atomically acquires and releases lock\n"
                    "        if shared_balance >= amount:\n"
                    "            shared_balance -= amount\n"
                    "            return True\n"
                    "        return False"
                ),
                "explanation": "`with balance_lock:` guarantees atomic check-and-act execution."
            },
            {
                "title": "Simulating and Avoiding a Deadlock",
                "language": "python",
                "code": (
                    "lock_a = threading.Lock()\n"
                    "lock_b = threading.Lock()\n\n"
                    "# DEADLOCK RISK: Thread 1 locks A then B; Thread 2 locks B then A\n"
                    "# THE FIX: Enforce identical lock acquisition ordering everywhere!\n"
                    "def safe_transfer(from_lock, to_lock):\n"
                    "    # Always acquire locks ordered by memory address or ID\n"
                    "    first, second = sorted([from_lock, to_lock], key=id)\n"
                    "    with first:\n"
                    "        with second:\n"
                    "            pass # Critical transfer section executed safely"
                ),
                "explanation": "Consistent global lock acquisition ordering eliminates the Circular Wait condition."
            },
            {
                "title": "Atomic Database Updates to Prevent DB-Level Race Conditions",
                "language": "sql",
                "code": (
                    "-- FRAGILE: Reading balance into Python, then writing back\n"
                    "-- UPDATE accounts SET balance = 50 WHERE id = 1;\n\n"
                    "-- ATOMIC: Database performs check and deduction in 1 atomic operation\n"
                    "UPDATE accounts \n"
                    "SET balance = balance - 100 \n"
                    "WHERE id = 1 AND balance >= 100;"
                ),
                "explanation": "Pushing concurrency checks directly into SQL atomic operations eliminates web-tier races."
            }
        ],
        coding_challenge={
            "title": "Build a Thread-Safe Counter Class",
            "instructions": "Write a class `ThreadSafeCounter` with methods `increment(val=1)` and `get_value()`. Use a `threading.Lock` internally so concurrent threads can safely call `increment()` without losing counts.",
            "starter_code": (
                "import threading\n\n"
                "class ThreadSafeCounter:\n"
                "    def __init__(self):\n"
                "        self.count = 0\n\n"
                "    def increment(self, val=1):\n"
                "        pass\n\n"
                "    def get_value(self) -> int:\n"
                "        pass\n"
            ),
            "solution_code": (
                "import threading\n\n"
                "class ThreadSafeCounter:\n"
                "    def __init__(self):\n"
                "        self.count = 0\n"
                "        self.lock = threading.Lock()\n\n"
                "    def increment(self, val=1):\n"
                "        with self.lock:\n"
                "            self.count += val\n\n"
                "    def get_value(self) -> int:\n"
                "        with self.lock:\n"
                "            return self.count\n\n"
                "counter = ThreadSafeCounter()\n"
                "threads = [threading.Thread(target=counter.increment) for _ in range(100)]\n"
                "for t in threads: t.start()\n"
                "for t in threads: t.join()\n"
                "print(counter.get_value())"
            ),
            "expected_output": "100"
        },
        quizzes=[
            {
                "question": "What is a 'Race Condition' in software concurrency?",
                "options": [
                    "A defect where program correctness depends on the non-deterministic timing or execution order of multiple threads or processes",
                    "A speed test between two computers",
                    "A race between two microservices to reply to a user",
                    "A feature in the operating system"
                ],
                "correct_answer": "A defect where program correctness depends on the non-deterministic timing or execution order of multiple threads or processes",
                "explanation": "Race conditions occur when shared mutable memory is accessed without synchronization, leading to corrupted state."
            },
            {
                "question": "What is a 'Heisenbug'?",
                "options": [
                    "A bug that seems to disappear or change behavior whenever you attempt to observe or debug it (often because logging or debuggers alter thread timing)",
                    "A computer virus invented in Germany",
                    "A bug in Python's math library",
                    "A hardware failure in quantum computers"
                ],
                "correct_answer": "A bug that seems to disappear or change behavior whenever you attempt to observe or debug it (often because logging or debuggers alter thread timing)",
                "explanation": "Named after Heisenberg's uncertainty principle, Heisenbugs vanish when diagnostic instrumentation alters timing."
            },
            {
                "question": "What primary strategy prevents Deadlocks when an operation must acquire two separate locks (Lock A and Lock B)?",
                "options": [
                    "Always acquire multiple locks in a strict, consistent global order across all threads (e.g. sorted by lock ID)",
                    "Never use locks anywhere",
                    "Acquire locks in random order",
                    "Run all code on a single thread"
                ],
                "correct_answer": "Always acquire multiple locks in a strict, consistent global order across all threads (e.g. sorted by lock ID)",
                "explanation": "Enforcing identical lock acquisition ordering breaks the Coffman Circular Wait condition."
            },
            {
                "question": "What does a Mutex (Mutual Exclusion) Lock do?",
                "options": [
                    "It ensures that only one thread can execute a critical section of code or access a shared variable at any given time",
                    "It doubles the CPU clock frequency",
                    "It compresses data in memory",
                    "It deletes duplicate records"
                ],
                "correct_answer": "It ensures that only one thread can execute a critical section of code or access a shared variable at any given time",
                "explanation": "Mutex locks serialize access to shared resources, enforcing atomic access boundaries."
            },
            {
                "question": "Why is `UPDATE accounts SET balance = balance - 50 WHERE id = 1 AND balance >= 50;` safer than checking in application code first?",
                "options": [
                    "The database engine executes the balance check and arithmetic update as a single atomic operation inside a row lock",
                    "It encrypts the bank account number",
                    "SQL does not allow bugs",
                    "It runs faster than Python memory"
                ],
                "correct_answer": "The database engine executes the balance check and arithmetic update as a single atomic operation inside a row lock",
                "explanation": "Database-level atomic updates eliminate the race condition gap between checking and acting."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 47: Handling & Fixing Infinite Loops & Runaway Logic
    # ---------------------------------------------------------
    DayBlueprint(
        order=47,
        title="Day 47: Handling & Fixing Infinite Loops & Runaway Logic",
        concept="Infinite loops and unbounded recursion starve CPU cores and freeze application processes when terminating invariants fail to progress toward exit conditions.",
        analogy="An infinite loop is like walking on an exercise treadmill with a sleep mask on. You keep marching with maximum effort, your heart is pounding, sweat is pouring (100% CPU usage), but you are not moving an inch closer to the grocery store because you never reach the destination.",
        theory_sections=[
            {
                "heading": "Anatomy of an Infinite Loop",
                "content": (
                    "Every loop requires 3 components to be algorithmically sound:\n"
                    "1. **Initialization**: Loop index or condition variable is established.\n"
                    "2. **Progress**: The loop body **must mutate the condition variable toward the termination state** on every single iteration.\n"
                    "3. **Termination Condition**: A boolean check that evaluates to False when work is complete.\n\n"
                    "If the loop body forgets to advance the pointer (`i += 1`), skips over the exact equality condition, or encounters floating-point rounding errors, the loop runs forever, pegging CPU at 100%."
                )
            },
            {
                "heading": "The Floating-Point Rounding Trap",
                "content": (
                    "```python\n"
                    "val = 0.0\n"
                    "while val != 1.0:\n"
                    "    val += 0.1\n"
                    "```\n"
                    "Due to IEEE 754 binary floating-point representation, `0.1 + 0.1 + ...` evaluates to `0.9999999999999999` and then `1.0999999999999999`! It **never equals exactly 1.0**, looping forever!\n"
                    "**Rule**: Never use exact equality (`==` or `!=`) with floating-point numbers in loop conditions; use `<` or `>=`."
                )
            },
            {
                "heading": "Defensive Loop Circuit Breakers (Watchdog Bounds)",
                "content": (
                    "In enterprise software, never trust a `while True:` loop without a **safety watchdog counter**:\n"
                    "```python\n"
                    "max_cycles = 10000\n"
                    "for _ in range(max_cycles):\n"
                    "    if condition: break\n"
                    "else:\n"
                    "    raise InfiniteLoopDetectedError('Watchdog tripped')\n"
                    "```"
                )
            }
        ],
        code_snippets=[
            {
                "title": "The Floating-Point Infinite Loop Trap",
                "language": "python",
                "code": (
                    "# INFINITE LOOP BUG: Exact float equality fails due to precision limits\n"
                    "# val = 0.0\n"
                    "# while val != 1.0:\n"
                    "#     val += 0.1  # Skips past 1.0 to 1.0999999999999999!\n\n"
                    "# THE FIX: Use inequality or math.isclose\n"
                    "val = 0.0\n"
                    "step = 0.1\n"
                    "while val < 1.0 - 1e-9:\n"
                    "    val += step\n"
                    "print(f'Finished safely at val={val:.1f}')"
                ),
                "explanation": "Inequality comparison `<` avoids floating-point precision traps."
            },
            {
                "title": "Watchdog Circuit Breaker Pattern",
                "language": "python",
                "code": (
                    "def fetch_all_paginated_pages(client):\n"
                    "    pages = []\n"
                    "    cursor = 'init'\n"
                    "    # Defensive watchdog: cap maximum iterations to prevent infinite while loop\n"
                    "    MAX_PAGES = 500\n"
                    "    for iteration in range(MAX_PAGES):\n"
                    "        res = client.get_page(cursor)\n"
                    "        pages.append(res['data'])\n"
                    "        cursor = res.get('next_cursor')\n"
                    "        if not cursor:\n"
                    "            return pages\n"
                    "    raise RuntimeError('Pagination exceeded safety limit of 500 pages (possible cycle)')"
                ),
                "explanation": "Bounded iterations guarantee loops terminate even if third-party pagination has cyclic bugs."
            },
            {
                "title": "Detecting Infinite Recursion with Base Cases",
                "language": "python",
                "code": (
                    "# BUG: Missing base case for negative integers\n"
                    "def countdown_broken(n):\n"
                    "    if n == 0: return 'Done'\n"
                    "    return countdown_broken(n - 1) # If n = -1, runs infinitely until RecursionError!\n\n"
                    "# FIX: Guard against negative values\n"
                    "def countdown_safe(n):\n"
                    "    if n <= 0: return 'Done'\n"
                    "    return countdown_safe(n - 1)"
                ),
                "explanation": "`n <= 0` defends against negative input edge cases that bypass `n == 0`."
            },
            {
                "title": "Using Python `signal` for Execution Timeouts (Linux/macOS)",
                "language": "python",
                "code": (
                    "import signal\n\n"
                    "class TimeoutException(Exception): pass\n\n"
                    "def handler(signum, frame):\n"
                    "    raise TimeoutException('Operation took too long!')\n\n"
                    "# Arm 3-second watchdog timer\n"
                    "# signal.signal(signal.SIGALRM, handler)\n"
                    "# signal.alarm(3)\n"
                    "# try: potentially_infinite_job()\n"
                    "# finally: signal.alarm(0) # Disarm"
                ),
                "explanation": "OS alarm signals enforce hard deadlines on runaway operations."
            }
        ],
        coding_challenge={
            "title": "Implement a Watchdog Bounded Loop Runner",
            "instructions": "Write a function `safe_loop_runner(step_fn, max_iterations=100)` that repeatedly calls `step_fn()`. `step_fn()` returns True to continue, or False to stop. If `step_fn()` does not return False within `max_iterations`, raise `TimeoutError('LOOP_RUNAWAY')`. Return total iterations completed on clean termination.",
            "starter_code": (
                "def safe_loop_runner(step_fn, max_iterations: int = 100) -> int:\n"
                "    # Execute step_fn with watchdog\n"
                "    pass\n"
            ),
            "solution_code": (
                "def safe_loop_runner(step_fn, max_iterations: int = 100) -> int:\n"
                "    count = 0\n"
                "    while count < max_iterations:\n"
                "        count += 1\n"
                "        should_continue = step_fn()\n"
                "        if not should_continue:\n"
                "            return count\n"
                "    raise TimeoutError('LOOP_RUNAWAY')\n\n"
                "state = {'ticks': 0}\n"
                "def tick():\n"
                "    state['ticks'] += 1\n"
                "    return state['ticks'] < 5\n\n"
                "print(safe_loop_runner(tick, max_iterations=10))"
            ),
            "expected_output": "5"
        },
        quizzes=[
            {
                "question": "What is the primary cause of an infinite loop in software?",
                "options": [
                    "The loop body fails to mutate the loop condition variable toward the termination state, so the condition remains True forever",
                    "The computer monitor refresh rate is too slow",
                    "The compiler ran out of memory",
                    "Variable names are too short"
                ],
                "correct_answer": "The loop body fails to mutate the loop condition variable toward the termination state, so the condition remains True forever",
                "explanation": "Without algorithmic progression toward the exit condition, loops execute indefinitely."
            },
            {
                "question": "Why is `while val != 1.0:` with `val += 0.1` dangerous in Python and JavaScript?",
                "options": [
                    "Binary floating-point rounding imprecision causes `val` to skip past 1.0 (e.g. 0.999999999 to 1.099999999), never matching exactly 1.0",
                    "Floats cannot be used in loops",
                    "Addition is not allowed in while loops",
                    "Python crashes on decimals"
                ],
                "correct_answer": "Binary floating-point rounding imprecision causes `val` to skip past 1.0 (e.g. 0.999999999 to 1.099999999), never matching exactly 1.0",
                "explanation": "IEEE 754 precision issues prevent exact representation of decimal fractions like 0.1."
            },
            {
                "question": "What is a 'Watchdog Circuit Breaker' in loop design?",
                "options": [
                    "A hard maximum iteration cap (e.g. `max_loops = 5000`) that raises an exception if a while loop fails to terminate naturally",
                    "An antivirus software tool",
                    "A hardware dog collar for servers",
                    "A method for speeding up downloads"
                ],
                "correct_answer": "A hard maximum iteration cap (e.g. `max_loops = 5000`) that raises an exception if a while loop fails to terminate naturally",
                "explanation": "Watchdogs bound maximum loop cycles, preventing runaway CPU consumption."
            },
            {
                "question": "What symptom on server monitoring dashboards typically signals an infinite loop in a thread?",
                "options": [
                    "A single CPU core pegs at 100% utilization and stays locked there while request throughput drops",
                    "Disk space increases to 100%",
                    "Network bandwidth spikes to 10 Gbps",
                    "The computer plays a song"
                ],
                "correct_answer": "A single CPU core pegs at 100% utilization and stays locked there while request throughput drops",
                "explanation": "Infinite loops continuously burn CPU cycles without pausing or yielding."
            },
            {
                "question": "How does `countdown(n - 1)` with `if n == 0: return` break if called with a negative integer like `-5`?",
                "options": [
                    "`n` decreases to -6, -7, -8, bypassing `n == 0` completely and recursing infinitely until a `RecursionError` occurs",
                    "It returns 'Done' immediately",
                    "It converts -5 to positive 5",
                    "It prints an error on line 1"
                ],
                "correct_answer": "`n` decreases to -6, -7, -8, bypassing `n == 0` completely and recursing infinitely until a `RecursionError` occurs",
                "explanation": "Using exact equality `== 0` fails for inputs that start below the boundary; use `<= 0`."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 48: Reproducing Production Bugs in Local Environments
    # ---------------------------------------------------------
    DayBlueprint(
        order=48,
        title="Day 48: Reproducing Production Bugs in Local Environments",
        concept="Local reproduction bridges the gap between production outages and developer laptops by mirroring container environments, sanitizing production database snapshots, and replaying production HTTP payloads.",
        analogy="If a bridge collapses in a category 5 hurricane, civil engineers don't try to summon another real hurricane. They build a scale model in a wind tunnel and blow 150 MPH wind at it. Local reproduction is building the wind tunnel on your laptop to simulate the hurricane conditions safely.",
        theory_sections=[
            {
                "heading": "Why 'It Works on My Machine' Is Not an Excuse",
                "content": (
                    "Discrepancies between local laptops and production servers stem from 4 environmental vectors:\n"
                    "1. **OS & Kernel Differences**: macOS (case-insensitive filesystem) vs Linux production (case-sensitive: `import User` vs `import user`).\n"
                    "2. **Database Scale & Engine**: SQLite locally vs PostgreSQL 15 with 10M rows in production.\n"
                    "3. **Dependency Drift**: Minor patch differences between local `pip` packages and production container images.\n"
                    "4. **State & Race Conditions**: Single user locally vs 500 concurrent requests in production."
                )
            },
            {
                "heading": "The 3 Pillars of Environment Parity (Docker & Devcontainers)",
                "content": (
                    "- **Containerization (Docker)**: Guarantees identical Linux distribution, system libraries, and runtime versions.\n"
                    "- **Sanitized Database Dumps**: Scrubbing sensitive PII (credit cards, passwords) while preserving real data volume, distribution, and indexes.\n"
                    "- **Traffic Shadowing / Replay**: Tools like GoReplay capture raw production HTTP traffic and replay it against a local staging environment."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Sanitizing Production Database Dumps for Local Use",
                "language": "sql",
                "code": (
                    "-- Script run on production read-replica before exporting dump for local debugging\n"
                    "BEGIN TRANSACTION;\n"
                    "  -- 1. Scrub PII and sensitive passwords\n"
                    "  UPDATE users SET \n"
                    "    password_hash = '$2b$12$e8Y...dummy_hash',\n"
                    "    email = 'user_' || id || '@test.internal',\n"
                    "    phone = '+15550000000';\n"
                    "  -- 2. Truncate audit log noise\n"
                    "  TRUNCATE TABLE audit_event_logs;\n"
                    "COMMIT;\n"
                    "-- Export sanitized dump: pg_dump -d sanitized_db > local_debug.sql"
                ),
                "explanation": "Masks Personally Identifiable Information (PII) to comply with GDPR/HIPAA during local reproduction."
            },
            {
                "title": "Docker Compose for Identical Local Infrastructure",
                "language": "yaml",
                "code": (
                    "version: '3.8'\n"
                    "services:\n"
                    "  app:\n"
                    "    build: . # Identical Dockerfile used in production deployment\n"
                    "    environment:\n"
                    "      - DATABASE_URL=postgresql://postgres:secret@db:5432/test_db\n"
                    "      - REDIS_URL=redis://cache:6379/0\n"
                    "    ports: ['8000:8000']\n"
                    "  db:\n"
                    "    image: postgres:15-alpine\n"
                    "  cache:\n"
                    "    image: redis:7-alpine"
                ),
                "explanation": "Reproduces exact container images and network topologies locally."
            },
            {
                "title": "Case-Sensitivity Bug (macOS vs Linux)",
                "language": "python",
                "code": (
                    "# File on disk: models/userProfile.py\n"
                    "# In macOS: import models.userprofile  # WORKS (case-insensitive)\n"
                    "# In Linux Production: ModuleNotFoundError: No module named 'models.userprofile'!\n"
                    "# THE FIX: Always match exact case of filenames\n"
                    "from models.userProfile import UserProfile"
                ),
                "explanation": "Case-sensitivity discrepancies between macOS and Linux are a frequent source of deployment crashes."
            },
            {
                "title": "Replaying Production Payloads Locally with cURL",
                "language": "bash",
                "code": (
                    "# Extract failed request payload from Sentry/Datadog and dispatch locally:\n"
                    "curl -X POST http://localhost:8000/api/v1/checkout \\\n"
                    "  -H 'Content-Type: application/json' \\\n"
                    "  -d @production_payload_crash_123.json"
                ),
                "explanation": "Replaying exact production JSON payloads triggers the failure in local debuggers."
            }
        ],
        coding_challenge={
            "title": "Sanitize User PII from Dictionary Payload",
            "instructions": "Write a function `sanitize_pii(record)` that replaces `'email'` with `'user_<id>@sanitized.com'`, replaces `'ssn'` or `'credit_card'` with `'[REDACTED]'`, and keeps other fields untouched. If `'id'` is missing, use `'0'`.",
            "starter_code": (
                "def sanitize_pii(record: dict) -> dict:\n"
                "    # Return sanitized copy of record\n"
                "    pass\n"
            ),
            "solution_code": (
                "def sanitize_pii(record: dict) -> dict:\n"
                "    clean = record.copy()\n"
                "    uid = clean.get('id', 0)\n"
                "    if 'email' in clean:\n"
                "        clean['email'] = f'user_{uid}@sanitized.com'\n"
                "    for sensitive in ['ssn', 'credit_card', 'password']:\n"
                "        if sensitive in clean:\n"
                "            clean[sensitive] = '[REDACTED]'\n"
                "    return clean\n\n"
                "raw = {'id': 42, 'email': 'real_person@gmail.com', 'ssn': '123-45-6789', 'role': 'admin'}\n"
                "print(sanitize_pii(raw))"
            ),
            "expected_output": "{'id': 42, 'email': 'user_42@sanitized.com', 'ssn': '[REDACTED]', 'role': 'admin'}"
        },
        quizzes=[
            {
                "question": "Why does code that imports `from models.user import User` sometimes work on a developer's Mac laptop but crash with `ModuleNotFoundError` on production Linux servers?",
                "options": [
                    "macOS uses a case-insensitive filesystem by default, whereas Linux production filesystems are strictly case-sensitive",
                    "Linux cannot run Python imports",
                    "Mac computers compile Python differently",
                    "The word 'User' is reserved in Linux"
                ],
                "correct_answer": "macOS uses a case-insensitive filesystem by default, whereas Linux production filesystems are strictly case-sensitive",
                "explanation": "Case differences in filenames cause missing module exceptions on Linux production servers."
            },
            {
                "question": "What is the primary legal and security rule when importing production database data to a local developer laptop for debugging?",
                "options": [
                    "Personally Identifiable Information (PII) such as passwords, emails, and credit cards must be scrubbed/anonymized to comply with privacy laws (GDPR/HIPAA)",
                    "You must print the database on paper",
                    "The database must be converted to Microsoft Excel",
                    "All users must be notified by phone"
                ],
                "correct_answer": "Personally Identifiable Information (PII) such as passwords, emails, and credit cards must be scrubbed/anonymized to comply with privacy laws (GDPR/HIPAA)",
                "explanation": "Exporting raw PII to laptops violates GDPR, HIPAA, and SOC2 compliance."
            },
            {
                "question": "How does Docker solve the classic 'It works on my machine' environmental discrepancy?",
                "options": [
                    "By packaging application code, system libraries, OS dependencies, and runtime versions into an identical immutable container image",
                    "By making all computers use the same hardware",
                    "By deleting all dependencies",
                    "By running code exclusively in the cloud"
                ],
                "correct_answer": "By packaging application code, system libraries, OS dependencies, and runtime versions into an identical immutable container image",
                "explanation": "Containers guarantee consistent OS, library, and runtime environments across dev and prod."
            },
            {
                "question": "What is 'Traffic Shadowing' (or Dark Traffic) in production debugging?",
                "options": [
                    "Mirroring a copy of live production HTTP traffic to a staging environment to observe how new code handles real-world requests without affecting users",
                    "Turning off the server monitor during the night",
                    "Routing traffic through the dark web",
                    "Hiding server IP addresses from DNS"
                ],
                "correct_answer": "Mirroring a copy of live production HTTP traffic to a staging environment to observe how new code handles real-world requests without affecting users",
                "explanation": "Traffic shadowing exposes pre-production systems to genuine production scale and payload variety."
            },
            {
                "question": "Why is reproducing a production bug using an in-memory SQLite database locally often misleading when the production database is PostgreSQL?",
                "options": [
                    "SQLite has different locking models, lacks advanced PostgreSQL types (like JSONB/UUIDs), and behaves differently on concurrency and case-sensitivity",
                    "SQLite is faster than PostgreSQL",
                    "SQLite does not allow SQL queries",
                    "PostgreSQL cannot run in Docker"
                ],
                "correct_answer": "SQLite has different locking models, lacks advanced PostgreSQL types (like JSONB/UUIDs), and behaves differently on concurrency and case-sensitivity",
                "explanation": "Dialect and concurrency differences make SQLite an unreliable surrogate for production PostgreSQL."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 49: Remote Debugging Concepts & Tunneling
    # ---------------------------------------------------------
    DayBlueprint(
        order=49,
        title="Day 49: Remote Debugging Concepts & Tunneling",
        concept="Remote debugging attaches a local IDE interface to an application process running on a remote cloud server or Kubernetes pod via secure debug tunnels (debugpy, SSH port forwarding).",
        analogy="Remote debugging is like a surgeon in London operating on a patient in Tokyo using a high-precision robotic surgical arm over a secure fiber-optic video feed. The surgeon sits comfortably in their London office, but their scalpel moves with millimeter precision inside the Tokyo operating room.",
        theory_sections=[
            {
                "heading": "How Remote Debugging Works",
                "content": (
                    "When an issue only occurs in a specific staging cloud environment (e.g. AWS ECS container):\n"
                    "1. The remote application runs with a debug agent attached (`python -m debugpy --listen 0.0.0.0:5678 main.py`).\n"
                    "2. A secure **SSH Tunnel** forwards local port 5678 to the remote server's port 5678.\n"
                    "3. Your local VS Code or PyCharm connects via `'request': 'attach'`.\n"
                    "4. When a remote HTTP request hits the cloud container, **execution halts, and your local VS Code opens the breakpoint**!"
                )
            },
            {
                "heading": "Path Mapping: Translating File Systems",
                "content": (
                    "Your laptop has source files at `C:\\Users\\Sara\\Projects\\app\\main.py`. The Linux container has files at `/app/main.py`. The debugger must map these paths:\n"
                    "```json\n"
                    "\"pathMappings\": [{\n"
                    "  \"localRoot\": \"${workspaceFolder}\",\n"
                    "  \"remoteRoot\": \"/app\"\n"
                    "}]\n"
                    "```\n"
                    "Without path mappings, breakpoints fail to bind because the remote agent doesn't recognize your Windows/Mac paths."
                )
            },
            {
                "heading": "Security Warning: Never Expose Debug Ports Publicly",
                "content": (
                    "Debug ports (like 5678) allow arbitrary code execution! **Never bind debug ports to public internet IPs (`0.0.0.0`) without a firewall**. Always bind to `localhost` and access via SSH tunneling or VPN."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Starting Python with `debugpy` Remote Listener",
                "language": "bash",
                "code": (
                    "# On remote staging server or inside Dockerfile:\n"
                    "python -m debugpy \\\n"
                    "  --listen 0.0.0.0:5678 \\\n"
                    "  --wait-for-client \\\n"
                    "  app.py\n\n"
                    "# --wait-for-client: Pauses on line 1 until local IDE connects"
                ),
                "explanation": "Starts Python process waiting for remote debugger connection on port 5678."
            },
            {
                "title": "Secure SSH Port Forwarding Tunnel",
                "language": "bash",
                "code": (
                    "# On developer laptop: Forward local port 5678 to remote container port 5678\n"
                    "ssh -N -L 5678:localhost:5678 user@staging-server.company.com\n\n"
                    "# Now local VS Code connecting to localhost:5678 is securely encrypted\n"
                    "# and tunneled directly into the remote staging process!"
                ),
                "explanation": "Creates an encrypted tunnel bypassing public firewall exposure."
            },
            {
                "title": "VS Code Remote Attach `launch.json`",
                "language": "json",
                "code": (
                    "{\n"
                    "  \"name\": \"Python: Remote Attach\",\n"
                    "  \"type\": \"debugpy\",\n"
                    "  \"request\": \"attach\",\n"
                    "  \"connect\": {\n"
                    "    \"host\": \"localhost\",\n"
                    "    \"port\": 5678\n"
                    "  },\n"
                    "  \"pathMappings\": [\n"
                    "    {\n"
                    "      \"localRoot\": \"${workspaceFolder}\",\n"
                    "      \"remoteRoot\": \"/app\"\n"
                    "    }\n"
                    "  ]\n"
                    "}"
                ),
                "explanation": "VS Code configuration mapping local workspace directories to remote container roots."
            },
            {
                "title": "Kubernetes Port-Forwarding to a Pod",
                "language": "bash",
                "code": (
                    "# Forward debug port directly from a Kubernetes pod:\n"
                    "kubectl port-forward pod/billing-service-78f99-x2b4 5678:5678\n\n"
                    "# Instant connection to live cloud pod from local IDE!"
                ),
                "explanation": "Standard Kubernetes CLI command forwarding pod ports to local workstations."
            }
        ],
        coding_challenge={
            "title": "Translate Path Mapping Coordinates",
            "instructions": "Write a function `map_remote_to_local_path(remote_path, local_root, remote_root)` that translates a remote file path (e.g. `'/app/services/auth.py'`) into its corresponding local path given `local_root = 'C:/dev/project'` and `remote_root = '/app'`. Use forward slashes.",
            "starter_code": (
                "def map_remote_to_local_path(remote_path: str, local_root: str, remote_root: str) -> str:\n"
                "    # Return translated local path\n"
                "    pass\n"
            ),
            "solution_code": (
                "def map_remote_to_local_path(remote_path: str, local_root: str, remote_root: str) -> str:\n"
                "    clean_remote = remote_path.replace('\\\\', '/')\n"
                "    clean_remote_root = remote_root.replace('\\\\', '/').rstrip('/')\n"
                "    clean_local_root = local_root.replace('\\\\', '/').rstrip('/')\n"
                "    if clean_remote.startswith(clean_remote_root):\n"
                "        rel = clean_remote[len(clean_remote_root):].lstrip('/')\n"
                "        return f\"{clean_local_root}/{rel}\"\n"
                "    return remote_path\n\n"
                "print(map_remote_to_local_path('/app/models/user.py', 'C:/dev/app', '/app'))"
            ),
            "expected_output": "C:/dev/app/models/user.py"
        },
        quizzes=[
            {
                "question": "What is 'Remote Debugging'?",
                "options": [
                    "Connecting your local IDE debugger to an application process running on a remote cloud server or container to set breakpoints and inspect live state",
                    "Debugging without an internet connection",
                    "Debugging an application using a TV remote control",
                    "Fixing bugs by deleting remote git branches"
                ],
                "correct_answer": "Connecting your local IDE debugger to an application process running on a remote cloud server or container to set breakpoints and inspect live state",
                "explanation": "Remote debugging projects live process state from a cloud host into local IDE inspection panels."
            },
            {
                "question": "Why is configuring `pathMappings` mandatory in a remote debugging setup?",
                "options": [
                    "To map file paths on the remote server (e.g. `/app/main.py`) to corresponding file paths on your local laptop (e.g. `C:/dev/main.py`) so breakpoints bind correctly",
                    "To draw a map of the network cables",
                    "To download files from Google Maps",
                    "To speed up hard drive access"
                ],
                "correct_answer": "To map file paths on the remote server (e.g. `/app/main.py`) to corresponding file paths on your local laptop (e.g. `C:/dev/main.py`) so breakpoints bind correctly",
                "explanation": "Path mappings resolve disparate filesystem roots between local OS and remote containers."
            },
            {
                "question": "Why is exposing a debugger port (like port 5678) directly to the public internet a severe security vulnerability?",
                "options": [
                    "Debuggers allow evaluating arbitrary expressions and executing arbitrary shell commands, giving attackers complete remote code execution (RCE)",
                    "It uses too much internet bandwidth",
                    "It makes the server clock run backwards",
                    "It invalidates SSL certificates"
                ],
                "correct_answer": "Debuggers allow evaluating arbitrary expressions and executing arbitrary shell commands, giving attackers complete remote code execution (RCE)",
                "explanation": "Open debug ports grant unrestricted arbitrary code execution into process memory."
            },
            {
                "question": "What tool or protocol is recommended to securely connect your local debugger to a remote debug port?",
                "options": [
                    "An encrypted SSH tunnel (`ssh -L 5678:localhost:5678`) or VPN",
                    "An unencrypted HTTP GET request",
                    "An open Telnet connection",
                    "Sending passwords in plain text emails"
                ],
                "correct_answer": "An encrypted SSH tunnel (`ssh -L 5678:localhost:5678`) or VPN",
                "explanation": "SSH port forwarding encrypts traffic and restricts access strictly to authorized key holders."
            },
            {
                "question": "Which `kubectl` command connects a local laptop port directly to a running Kubernetes pod's debug port?",
                "options": [
                    "`kubectl port-forward pod/<pod-name> 5678:5678`",
                    "`kubectl attach-debugger`",
                    "`kubectl run-debug`",
                    "`kubectl copy-code`"
                ],
                "correct_answer": "`kubectl port-forward pod/<pod-name> 5678:5678`",
                "explanation": "`kubectl port-forward` bridges pod network ports to local localhost sockets securely."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 50: Core Dumps & Crash Reports Analysis
    # ---------------------------------------------------------
    DayBlueprint(
        order=50,
        title="Day 50: Core Dumps & Crash Reports Analysis",
        concept="A core dump is an operating system memory image recorded at the exact moment a process crashes (e.g., Segmentation Fault, fatal crash), enabling post-mortem offline inspection using tools like GDB and LLDB.",
        analogy="A core dump is like a plaster cast of a fossilized dinosaur footprint. The dinosaur (the crashed program) has been dead for millions of years and the bone is gone, but the stone imprint preserves the exact shape, weight, and stride of the creature at the moment it stepped into the mud.",
        theory_sections=[
            {
                "heading": "What is a Core Dump?",
                "content": (
                    "When an application terminates violently (e.g. `SIGSEGV` segmentation fault, `SIGABRT` abort, fatal out-of-memory crash), the operating system kernel dumps the entire virtual address space of the process into a file (called a **Core Dump**).\n\n"
                    "The core dump contains:\n"
                    "- All CPU register values (`RIP`, `RSP`, `EAX`).\n"
                    "- The exact program counter pointing to the machine instruction that caused the crash.\n"
                    "- The call stack and memory contents of all threads."
                )
            },
            {
                "heading": "Post-Mortem Debugging with GDB / LLDB",
                "content": (
                    "Because the process is dead, you cannot 'step' forward in time. But **Post-Mortem Debugging** allows you to inspect the frozen moment of death:\n"
                    "`gdb /usr/bin/python3 /tmp/core.python.1234`\n"
                    "- `bt` (backtrace): Shows the C call stack across Python interpreter internals.\n"
                    "- `py-bt`: Python GDB extension showing the Python-level stack trace!\n"
                    "- `info registers`: Inspect CPU registers."
                )
            },
            {
                "heading": "Enabling Core Dumps in Linux (`ulimit`)",
                "content": (
                    "By default, most Linux distributions set core dump file size to 0 to save disk space (`ulimit -c 0`). To enable crash dumps for debugging:\n"
                    "`ulimit -c unlimited`."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Enabling Core Dumps in Linux Shell",
                "language": "bash",
                "code": (
                    "# 1. Check current core dump size limit (often 0 by default)\n"
                    "ulimit -c\n\n"
                    "# 2. Enable unlimited core dump size\n"
                    "ulimit -c unlimited\n\n"
                    "# 3. Configure kernel core dump pattern to /tmp/cores\n"
                    "# echo '/tmp/core.%e.%p.%t' | sudo tee /proc/sys/kernel/core_pattern"
                ),
                "explanation": "Configures the Linux kernel to persist memory dumps when fatal signals occur."
            },
            {
                "title": "Analyzing a Python Core Dump with GDB",
                "language": "bash",
                "code": (
                    "# Launch GDB on python executable and core dump file\n"
                    "gdb python3 /tmp/core.python3.4812\n\n"
                    "# GDB outputs:\n"
                    "# Program terminated with signal SIGSEGV, Segmentation fault.\n"
                    "# #0  0x00007f... in PyObject_GetAttr ()\n"
                    "# (gdb) bt          # Print native C call stack\n"
                    "# (gdb) py-bt       # Print Python script lines and arguments!"
                ),
                "explanation": "Using GDB post-mortem inspection to analyze native C-extensions and Python crashes."
            },
            {
                "title": "Python Post-Mortem Debugger (`pdb.pm()`)",
                "language": "python",
                "code": (
                    "# If an unhandled exception crashes a script in interactive REPL:\n"
                    "import pdb\n\n"
                    "# pdb.pm() immediately loads the last uncaught exception's traceback\n"
                    "# and lets you inspect variables at the moment of failure!\n"
                    "# >>> pdb.pm()\n"
                    "# > /app/main.py(42)process()\n"
                    "# (Pdb) p failed_variable"
                ),
                "explanation": "`pdb.pm()` starts post-mortem inspection on the active crash traceback."
            },
            {
                "title": "Capturing Crash Reports on Exit with `faulthandler`",
                "language": "python",
                "code": (
                    "import faulthandler\n\n"
                    "# Dumps Python tracebacks on fatal crashes (SIGSEGV, SIGFPE, SIGBUS)\n"
                    "faulthandler.enable()\n\n"
                    "# Now if a native C-extension (like NumPy or OpenCV) crashes with segfault,\n"
                    "# Python prints the Python stack trace to stderr before dying!"
                ),
                "explanation": "`faulthandler` bridges native C-level segfaults to Python source lines."
            }
        ],
        coding_challenge={
            "title": "Parse Crash Signal Code to Human Diagnostic",
            "instructions": "Write a function `interpret_crash_signal(exit_code)` that translates Unix termination codes into diagnostics. For 137 (`128 + 9`), return `'OOM_KILLER (SIGKILL)'`. For 139 (`128 + 11`), return `'SEGMENTATION_FAULT (SIGSEGV)'`. For 134 (`128 + 6`), return `'ABORTED (SIGABRT)'`. For 0, return `'CLEAN_EXIT'`. For other codes, return `'UNRECOGNIZED_SIGNAL'`.",
            "starter_code": (
                "def interpret_crash_signal(code: int) -> str:\n"
                "    # Return human diagnostic string\n"
                "    pass\n"
            ),
            "solution_code": (
                "def interpret_crash_signal(code: int) -> str:\n"
                "    signals = {\n"
                "        0: 'CLEAN_EXIT',\n"
                "        134: 'ABORTED (SIGABRT)',\n"
                "        137: 'OOM_KILLER (SIGKILL)',\n"
                "        139: 'SEGMENTATION_FAULT (SIGSEGV)'\n"
                "    }\n"
                "    return signals.get(code, 'UNRECOGNIZED_SIGNAL')\n\n"
                "print(interpret_crash_signal(137))\n"
                "print(interpret_crash_signal(139))\n"
                "print(interpret_crash_signal(0))"
            ),
            "expected_output": "OOM_KILLER (SIGKILL)\nSEGMENTATION_FAULT (SIGSEGV)\nCLEAN_EXIT"
        },
        quizzes=[
            {
                "question": "What is a 'Core Dump' in Unix/Linux operating systems?",
                "options": [
                    "A snapshot file containing the recorded memory space and CPU register state of a process at the exact moment of a fatal crash",
                    "A backup of the MySQL database",
                    "A tool for deleting old kernel files",
                    "A hardware failure in the CPU cache"
                ],
                "correct_answer": "A snapshot file containing the recorded memory space and CPU register state of a process at the exact moment of a fatal crash",
                "explanation": "Core dumps record the entire memory state at the moment of fatal termination for post-mortem analysis."
            },
            {
                "question": "What tool is commonly used by engineers to open and analyze a core dump file offline?",
                "options": [
                    "GDB (GNU Debugger) or LLDB",
                    "Postman",
                    "Vim",
                    "Microsoft Word"
                ],
                "correct_answer": "GDB (GNU Debugger) or LLDB",
                "explanation": "GDB and LLDB load core dump files to reconstruct thread stacks and registers."
            },
            {
                "question": "What command in Python's standard `pdb` module enters post-mortem debugging on the most recent unhandled exception?",
                "options": [
                    "`pdb.pm()`",
                    "`pdb.start()`",
                    "`pdb.crash()`",
                    "`pdb.recover()`"
                ],
                "correct_answer": "`pdb.pm()`",
                "explanation": "`pdb.pm()` (Post-Mortem) drops directly into the frame where the last uncaught exception failed."
            },
            {
                "question": "What Python module introduced in Python 3.3 automatically dumps Python stack traces when a fatal segmentation fault (SIGSEGV) occurs in C extensions?",
                "options": [
                    "`faulthandler`",
                    "`segfault_dump`",
                    "`crash_tracker`",
                    "`sys_error`"
                ],
                "correct_answer": "`faulthandler`",
                "explanation": "`faulthandler.enable()` captures native faults and prints Python stack frames before termination."
            },
            {
                "question": "If an application process exits with status code 139 in Linux, what signal caused the termination?",
                "options": [
                    "`SIGSEGV` (Segmentation Fault, $128 + 11 = 139$)",
                    "`SIGKILL` ($128 + 9 = 137$)",
                    "`SIGINT` (Ctrl+C)",
                    "Clean exit"
                ],
                "correct_answer": "`SIGSEGV` (Segmentation Fault, $128 + 11 = 139$)",
                "explanation": "Unix exit code 139 indicates termination by signal 11 (`SIGSEGV`), representing an illegal memory access."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 51: Root Cause Analysis (RCA) & The 5 Whys
    # ---------------------------------------------------------
    DayBlueprint(
        order=51,
        title="Day 51: Root Cause Analysis (RCA) & The 5 Whys",
        concept="Root Cause Analysis (RCA) is a disciplined diagnostic methodology that looks beyond immediate surface symptoms to identify the fundamental systemic, architectural, or procedural defect using techniques like 'The 5 Whys'.",
        analogy="If water is leaking through your ceiling, placing a plastic bucket on the rug treats the symptom. Wiping the water off the floor treats the symptom. Finding the cracked copper pipe behind the upstairs bathroom wall, replacing the pipe with braided steel, and inspecting all other pipes for corrosion is Root Cause Analysis.",
        theory_sections=[
            {
                "heading": "Symptoms vs Root Causes",
                "content": (
                    "When an application crashes in production, junior developers restart the server or catch the exception with `pass` and call it 'fixed'. That is placing a bucket under the leak.\n\n"
                    "- **Symptom**: *'The database threw a connection timeout error.'*\n"
                    "- **Intermediate Cause**: *'All 50 connections in the pool were in use.'*\n"
                    "- **Root Cause**: *'An unindexed search query held row locks for 12 seconds, creating a cascading queue that exhausted the pool.'*\n"
                    "Fixing the root cause means adding an index and a query timeout, ensuring the problem can mathematically never recur."
                )
            },
            {
                "heading": "Sakichi Toyoda’s '5 Whys' Method",
                "content": (
                    "Originating in the Toyota Production System, the 5 Whys method drills past human blame to systemic design flaws:\n"
                    "1. **Why did the server crash?** -> Out of disk space.\n"
                    "2. **Why was disk space full?** -> The log file grew to 500GB.\n"
                    "3. **Why did the log file grow to 500GB?** -> It was logging every HTTP request body in DEBUG mode.\n"
                    "4. **Why was DEBUG mode enabled in prod?** -> A developer turned it on during a previous incident and forgot to turn it off.\n"
                    "5. **Why was it possible to leave it on?** -> Because log levels were hardcoded in code rather than controlled via ephemeral environment variables with automated rotation."
                )
            },
            {
                "heading": "Blameless Culture",
                "content": (
                    "RCA must be **blameless**. Human error is a symptom of a flawed system design, not the cause. If a human pushed bad code, the root cause is why the CI/CD pipeline and automated tests allowed bad code to reach production."
                )
            }
        ],
        code_snippets=[
            {
                "title": "The 5 Whys Real-World Outage Analysis",
                "language": "text",
                "code": (
                    "INCIDENT: User checkout failed for 45 minutes on Black Friday\n"
                    "1. Why? The payment service returned HTTP 500.\n"
                    "2. Why? The Stripe API client threw an SSLCertVerificationError.\n"
                    "3. Why? The server's SSL certificate bundle was expired.\n"
                    "4. Why? The automated certbot renewal cron job failed to execute.\n"
                    "5. Why? A permissions change on /etc/letsencrypt locked the cron daemon.\n\n"
                    "SYSTEMIC ACTION ITEMS:\n"
                    "- Fix permissions on /etc/letsencrypt (Remediation)\n"
                    "- Add automated Datadog monitor alerting 30 days before SSL expiry (Root Fix)"
                ),
                "explanation": "Illustrates how drilling through 5 levels of causality exposes the real systemic vulnerability."
            },
            {
                "title": "Symptom Patch (Bad) vs Root Cause Fix (Good)",
                "language": "python",
                "code": (
                    "# BAD (Symptom Patch): Catching and hiding the error\n"
                    "def get_user_data(uid):\n"
                    "    try:\n"
                    "        return db.query(f'SELECT * FROM users WHERE id = {uid}')\n"
                    "    except Exception:\n"
                    "        return {} # Hides database lock failure, returns empty user!\n\n"
                    "# GOOD (Root Cause Fix): Parameterized query + explicit pool timeout\n"
                    "def get_user_data_fixed(uid: int):\n"
                    "    with db.get_connection(timeout_seconds=2.0) as conn:\n"
                    "        return conn.execute('SELECT * FROM users WHERE id = :id', {'id': uid})"
                ),
                "explanation": "Contrasts masking symptoms with addressing root architectural constraints."
            },
            {
                "title": "Ishikawa (Fishbone) Diagram Categories for Software",
                "language": "text",
                "code": (
                    "Root Cause Fishbone Diagram Dimensions:\n"
                    "├── Code (Logic bugs, uncaught exceptions, off-by-one errors)\n"
                    "├── Infrastructure (CPU, RAM, network latency, disk I/O)\n"
                    "├── Dependencies (Third-party API downtime, breaking npm package update)\n"
                    "├── Process / CI-CD (Missing unit tests, skipped staging validation)\n"
                    "└── Environment (Configuration drift, timezone/locale mismatches)"
                ),
                "explanation": "Standard 5-axis framework for categorizing defect origins."
            },
            {
                "title": "Automated Defensive Assertion Guaranteeing Invariants",
                "language": "python",
                "code": (
                    "def calculate_refund(original_charge, refund_amount):\n"
                    "    # Defensive root cause prevention assertion\n"
                    "    assert 0 < refund_amount <= original_charge, \\\n"
                    "        f'Illegal refund amount: {refund_amount} on charge of {original_charge}'\n"
                    "    return original_charge - refund_amount"
                ),
                "explanation": "Hard assertions prevent invalid mathematical states from silently propagating."
            }
        ],
        coding_challenge={
            "title": "Build a 5 Whys Chain Parser",
            "instructions": "Write a function `format_five_whys(questions_and_answers)` that takes a list of 5 string tuples `[(why_question, answer), ...]` and returns a formatted markdown root cause chain string: `'1. Why: <q> -> Because: <a>\\n...'`.",
            "starter_code": (
                "def format_five_whys(chain: list) -> str:\n"
                "    # Return formatted markdown string\n"
                "    pass\n"
            ),
            "solution_code": (
                "def format_five_whys(chain: list) -> str:\n"
                "    lines = []\n"
                "    for idx, (q, a) in enumerate(chain, start=1):\n"
                "        lines.append(f'{idx}. Why: {q} -> Because: {a}')\n"
                "    return '\\n'.join(lines)\n\n"
                "sample_chain = [\n"
                "    ('Server crashed', 'Out of memory'),\n"
                "    ('Out of memory', 'Cache grew without bounds')\n"
                "]\n"
                "print(format_five_whys(sample_chain))"
            ),
            "expected_output": "1. Why: Server crashed -> Because: Out of memory\n2. Why: Out of memory -> Because: Cache grew without bounds"
        },
        quizzes=[
            {
                "question": "What is the primary goal of Root Cause Analysis (RCA)?",
                "options": [
                    "To identify the underlying fundamental defect or systemic design flaw so it can be prevented from ever recurring, rather than just patching surface symptoms",
                    "To assign personal blame to the junior developer",
                    "To restart the server faster",
                    "To delete customer bug tickets"
                ],
                "correct_answer": "To identify the underlying fundamental defect or systemic design flaw so it can be prevented from ever recurring, rather than just patching surface symptoms",
                "explanation": "RCA identifies the fundamental systemic failure mode to prevent recurrence permanently."
            },
            {
                "question": "What is the '5 Whys' technique originally pioneered at Toyota?",
                "options": [
                    "Repeatedly asking 'Why?' (typically 5 times) to drill through superficial symptoms down to the root systemic cause",
                    "Asking 5 different people for their opinion",
                    "Waiting 5 days before fixing a bug",
                    "Writing 5 unit tests for every function"
                ],
                "correct_answer": "Repeatedly asking 'Why?' (typically 5 times) to drill through superficial symptoms down to the root systemic cause",
                "explanation": "Iterative 'Why?' inquiry peels away symptom layers until the root failure point is reached."
            },
            {
                "question": "Why is an engineering culture of 'Blameless Post-Mortems' considered best practice by Google and Netflix?",
                "options": [
                    "When people fear punishment, they hide mistakes; a blameless culture encourages transparent reporting so systemic safety barriers can be built",
                    "Because nobody is ever responsible for code",
                    "Because engineers are not allowed to be fired",
                    "To save money on legal fees"
                ],
                "correct_answer": "When people fear punishment, they hide mistakes; a blameless culture encourages transparent reporting so systemic safety barriers can be built",
                "explanation": "Blameless analysis treats human error as a symptom of flawed process design, encouraging open safety reporting."
            },
            {
                "question": "What is the difference between a Symptom Patch and a Root Cause Fix?",
                "options": [
                    "A symptom patch hides or restarts after the crash (like wrapping with `except: pass`); a root cause fix resolves the underlying architectural invariant",
                    "A symptom patch takes 3 years to write",
                    "Root cause fixes only apply to HTML",
                    "There is no difference"
                ],
                "correct_answer": "A symptom patch hides or restarts after the crash (like wrapping with `except: pass`); a root cause fix resolves the underlying architectural invariant",
                "explanation": "Treating symptoms leaves root vulnerabilities open; root fixes resolve the structural failure mechanism."
            },
            {
                "question": "What visual diagram is frequently used in Root Cause Analysis to categorize causes across Code, Infrastructure, Process, and Environment?",
                "options": [
                    "Ishikawa (Fishbone) Diagram",
                    "Venn Diagram",
                    "Pie Chart",
                    "Scatter Plot"
                ],
                "correct_answer": "Ishikawa (Fishbone) Diagram",
                "explanation": "Ishikawa fishbone diagrams categorize causal contributors across major systemic categories."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 52: Writing Incident Reports / Post-Mortems
    # ---------------------------------------------------------
    DayBlueprint(
        order=52,
        title="Day 52: Writing Incident Reports / Post-Mortems",
        concept="A formal post-mortem document archives production incidents into institutional learning: detailing timelines, root causes, business impact, and measurable preventative action items.",
        analogy="When an airplane makes an emergency landing, the National Transportation Safety Board (NTSB) produces an exhaustive public report. They don't just say 'Plane landed safely, all good.' They publish a 50-page breakdown of every radio transmission, bolt torque, and sensor reading so every airline on Earth learns how to prevent that incident.",
        theory_sections=[
            {
                "heading": "The Anatomy of a Production Incident Post-Mortem",
                "content": (
                    "Every standardized post-mortem document contains 6 core sections:\n"
                    "1. **Executive Summary**: 2-3 sentences explaining what happened, customer impact, and duration.\n"
                    "2. **Impact Assessment**: Downtime in minutes, number of affected users, financial revenue loss, and SLA degradation.\n"
                    "3. **Chronological Timeline**: UTC timestamps from First Event -> Alarm Fired -> Engineer Paged -> Mitigation Applied -> Full Recovery.\n"
                    "4. **Root Cause Analysis**: Detailed technical breakdown of why the system failed.\n"
                    "5. **What Went Well / What Went Poorly**: Critical reflection on response tooling and alerts.\n"
                    "6. **Action Items (SMART)**: Concrete preventative engineering tasks with assignees and due dates."
                )
            },
            {
                "heading": "SMART Action Items (Preventing Future Recurrence)",
                "content": (
                    "Never write vague action items like: *'Be more careful next time'* or *'Write more tests'*.\n"
                    "Action items must be **SMART** (Specific, Measurable, Achievable, Relevant, Time-bound):\n"
                    "- *'Add automated integration test for voucher expiration logic (Assignee: John, Due: Friday)'*.\n"
                    "- *'Configure Datadog alarm alerting when Redis memory exceeds 80% (Assignee: DevOps, Due: Tuesday)'*."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Standard Markdown Post-Mortem Template",
                "language": "markdown",
                "code": (
                    "# Incident Post-Mortem: [INC-4021] Payment Gateway Outage\n\n"
                    "## Executive Summary\n"
                    "On 2026-04-12 from 14:10 to 14:45 UTC (35 mins), our checkout service failed,\n"
                    "preventing 1,420 users from completing purchases. Estimated revenue loss: $12,500.\n\n"
                    "## Timeline (UTC)\n"
                    "- **14:05**: PR #842 deployed to production containing unindexed database migration.\n"
                    "- **14:10**: First customer error recorded in Sentry.\n"
                    "- **14:12**: Datadog p99 latency alert triggered (> 5,000ms).\n"
                    "- **14:15**: On-call engineer paged and opened incident bridge.\n"
                    "- **14:35**: Root cause identified (lock contention on orders table).\n"
                    "- **14:40**: Rolled back release to previous stable image v1.4.1.\n"
                    "- **14:45**: Database locks cleared; latency normalized. Incident closed.\n\n"
                    "## Root Cause\n"
                    "Migration added a `NOT NULL` constraint without `CONCURRENTLY`, acquiring an\n"
                    "`ACCESS EXCLUSIVE` table lock that queued all incoming checkout transactions."
                ),
                "explanation": "Standard enterprise template capturing summary, timeline, and technical root cause."
            },
            {
                "title": "Action Items Table Template",
                "language": "markdown",
                "code": (
                    "## Action Items (Preventative Roadmap)\n\n"
                    "| Action Item | Type | Owner | Due Date | Status |\n"
                    "| :--- | :--- | :--- | :--- | :--- |\n"
                    "| Add linter check blocking non-concurrent migrations | Prevent | Alex | 2026-04-18 | Open |\n"
                    "| Reduce database transaction timeout from 60s to 5s | Mitigate | Sara | 2026-04-15 | In Progress |\n"
                    "| Create staging load test with 2,000 concurrent RPS | Detect | DevOps | 2026-04-22 | Open |"
                ),
                "explanation": "Tabular tracking of assigned preventative tasks with deadlines and types."
            },
            {
                "title": "Calculating Mean Time To Detect (MTTD) & Recover (MTTR)",
                "language": "python",
                "code": (
                    "from datetime import datetime\n\n"
                    "t_start = datetime.fromisoformat('2026-04-12T14:05:00')\n"
                    "t_detect = datetime.fromisoformat('2026-04-12T14:12:00')\n"
                    "t_recover = datetime.fromisoformat('2026-04-12T14:45:00')\n\n"
                    "mttd_minutes = (t_detect - t_start).total_seconds() / 60\n"
                    "mttr_minutes = (t_recover - t_detect).total_seconds() / 60\n"
                    "print(f'MTTD (Detection): {mttd_minutes} mins | MTTR (Recovery): {mttr_minutes} mins')"
                ),
                "explanation": "Calculates primary SRE incident metrics: Time to Detect and Time to Recover."
            },
            {
                "title": "Post-Mortem Review Meeting Guidelines",
                "language": "text",
                "code": (
                    "Rules for the Post-Mortem Meeting:\n"
                    "1. Focus on the timeline and systems, never on individuals.\n"
                    "2. Ask: 'What safety net was missing that allowed this to happen?'\n"
                    "3. Ensure all Action Items have a single assigned DRI (Directly Responsible Individual).\n"
                    "4. Publish the report internally to engineering and product teams."
                ),
                "explanation": "Operational guidelines for conducting constructive review retrospectives."
            }
        ],
        coding_challenge={
            "title": "Calculate Total Outage Duration and MTTD",
            "instructions": "Write a function `calculate_incident_metrics(incident_dict)` that takes `{'start': 'HH:MM', 'detect': 'HH:MM', 'resolved': 'HH:MM'}` (all within the same day) and returns `{'mttd_minutes': int, 'total_outage_minutes': int}`.",
            "starter_code": (
                "def calculate_incident_metrics(times: dict) -> dict:\n"
                "    # Return {'mttd_minutes': ..., 'total_outage_minutes': ...}\n"
                "    pass\n"
            ),
            "solution_code": (
                "def calculate_incident_metrics(times: dict) -> dict:\n"
                "    def to_minutes(t_str):\n"
                "        h, m = map(int, t_str.split(':'))\n"
                "        return h * 60 + m\n"
                "    start = to_minutes(times['start'])\n"
                "    detect = to_minutes(times['detect'])\n"
                "    resolved = to_minutes(times['resolved'])\n"
                "    return {\n"
                "        'mttd_minutes': detect - start,\n"
                "        'total_outage_minutes': resolved - start\n"
                "    }\n\n"
                "sample = {'start': '14:00', 'detect': '14:08', 'resolved': '14:40'}\n"
                "print(calculate_incident_metrics(sample))"
            ),
            "expected_output": "{'mttd_minutes': 8, 'total_outage_minutes': 40}"
        },
        quizzes=[
            {
                "question": "What is the primary objective of writing an Incident Post-Mortem?",
                "options": [
                    "To convert an operational failure into institutional learning and actionable preventative engineering tasks so the incident never recurs",
                    "To reprimand and discipline employees publicly",
                    "To delete customer accounts",
                    "To justify higher pricing"
                ],
                "correct_answer": "To convert an operational failure into institutional learning and actionable preventative engineering tasks so the incident never recurs",
                "explanation": "Post-mortems ensure organizations learn from outages and construct preventative defenses."
            },
            {
                "question": "What does 'MTTD' stand for in site reliability engineering (SRE)?",
                "options": [
                    "Mean Time to Detect",
                    "Maximum Thread Transfer Delay",
                    "Main Terminal Track Daemon",
                    "Memory Total Threshold Dump"
                ],
                "correct_answer": "Mean Time to Detect",
                "explanation": "MTTD measures the average time elapsed between incident occurrence and engineer awareness."
            },
            {
                "question": "What does 'MTTR' stand for in incident metrics?",
                "options": [
                    "Mean Time to Recover (or Repair)",
                    "Master Table Transaction Record",
                    "Minimum Time to Reboot",
                    "Multi-Threaded Test Runner"
                ],
                "correct_answer": "Mean Time to Recover (or Repair)",
                "explanation": "MTTR measures the average time taken from detection to complete system recovery."
            },
            {
                "question": "Why is 'Be more careful when deploying on Fridays' considered an unacceptable Post-Mortem Action Item?",
                "options": [
                    "It is vague, relies on fallible human willpower rather than automated systemic safety nets, and lacks owner and due date",
                    "Friday deployments are forbidden by the United Nations",
                    "It uses too many words",
                    "It must be written in Python"
                ],
                "correct_answer": "It is vague, relies on fallible human willpower rather than automated systemic safety nets, and lacks owner and due date",
                "explanation": "Effective action items implement concrete automation (e.g. CI/CD deployment blocks), not willpower."
            },
            {
                "question": "What section of a post-mortem document provides a chronological minute-by-minute breakdown from trigger to resolution?",
                "options": [
                    "Timeline",
                    "Executive Summary",
                    "Action Items",
                    "Glossary"
                ],
                "correct_answer": "Timeline",
                "explanation": "The Timeline records timestamped events showing communication, discovery, and remediation milestones."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 53: Static Code Analysis & Linting (ESLint, Pylint, Flake8)
    # ---------------------------------------------------------
    DayBlueprint(
        order=53,
        title="Day 53: Static Code Analysis & Linting (ESLint, Pylint, Flake8)",
        concept="Static code analysis inspects source code without executing it, parsing Abstract Syntax Trees (AST) to identify syntax violations, undefined variables, dead code, and security vulnerabilities before runtime.",
        analogy="Static analysis is like the spellcheck and grammar check in Microsoft Word. Before you print 50,000 copies of a book, Word flags: 'Missing comma on line 4, misspelled word on line 12, and you defined a character on page 3 who never appears again in the story.'",
        theory_sections=[
            {
                "heading": "Static vs Dynamic Analysis",
                "content": (
                    "- **Static Analysis**: Evaluates source code at rest without executing a single instruction. Catches uninitialized variables, unused imports, type mismatches, and known security vulnerabilities.\n"
                    "- **Dynamic Analysis**: Evaluates code while running (unit tests, profilers, memory leak detectors).\n"
                    "Static analysis catches 40% of all programming bugs in 200 milliseconds directly in your editor before you even run the code!"
                )
            },
            {
                "heading": "The Python Static Analysis Ecosystem",
                "content": (
                    "- **Flake8**: Blazing fast linter checking PEP 8 styling and basic syntax errors (`F401` unused import, `F821` undefined variable).\n"
                    "- **Pylint**: In-depth code analyzer checking complexity, design smells, and duplicate code.\n"
                    "- **Ruff**: The modern standard written in Rust; 100x faster than Flake8 and Pylint combined.\n"
                    "- **Mypy**: Static type checker verifying Python type annotations (`def add(a: int, b: int) -> int:`)."
                )
            },
            {
                "heading": "Security Scanners (Bandit & Semgrep)",
                "content": (
                    "Static analyzers also prevent security catastrophes:\n"
                    "- **Bandit**: Scans Python code for hardcoded passwords, use of `eval()`, SQL string concatenations, and insecure random number generators (`random` vs `secrets`)."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Bugs Caught Instantly by Static Analysis",
                "language": "python",
                "code": (
                    "# Static analyzer flags 3 errors BEFORE running:\n"
                    "import math # Error F401: 'math' imported but unused\n\n"
                    "def calculate_area(radius):\n"
                    "    # Error F821: undefined name 'radiuss' (typo!)\n"
                    "    return 3.14 * (radiuss ** 2)\n\n"
                    "def unreachable_code():\n"
                    "    return 42\n"
                    "    print('Never executes!') # Error: unreachable code"
                ),
                "explanation": "Linters catch typos, dead code, and unused imports directly in the editor."
            },
            {
                "title": "Running Flake8 and Ruff in Terminal",
                "language": "bash",
                "code": (
                    "# Run modern Ruff linter across entire codebase:\n"
                    "ruff check .\n\n"
                    "# Output:\n"
                    "# app/services/billing.py:12:8: F821 Undefined name 'user_id'\n"
                    "# app/models/user.py:3:1: F401 'os' imported but unused\n"
                    "# Found 2 errors."
                ),
                "explanation": "Ruff analyzes thousands of files in milliseconds, outputting actionable line diagnostics."
            },
            {
                "title": "Security Scanning with Bandit",
                "language": "bash",
                "code": (
                    "# Scan Python code for security vulnerabilities\n"
                    "bandit -r app/\n\n"
                    "# Flags:\n"
                    "# [B105:hardcoded_password_string] Possible hardcoded password: 'secret123'\n"
                    "# [B307:eval] Use of possibly insecure function - eval detected."
                ),
                "explanation": "Bandit scans AST structures for security antipatterns and hardcoded secrets."
            },
            {
                "title": "Static Type Checking with Mypy",
                "language": "python",
                "code": (
                    "# mypy catches type mismatches before runtime\n"
                    "def format_price(amount: float) -> str:\n"
                    "    return f'${amount:.2f}'\n\n"
                    "# Mypy CLI: error: Argument 1 to 'format_price' has incompatible type 'str'; expected 'float'\n"
                    "# format_price('one_hundred')"
                ),
                "explanation": "Mypy verifies type annotation contracts, preventing runtime TypeErrors."
            }
        ],
        coding_challenge={
            "title": "Simulate Linter Rule: Unused Imports Detector",
            "instructions": "Write a function `detect_unused_imports(source_code)` that parses Python source code using `import ast` and returns a sorted list of imported module names that are never referenced anywhere in the rest of the code.",
            "starter_code": (
                "import ast\n\n"
                "def detect_unused_imports(code_str: str) -> list:\n"
                "    # Return list of unused module names\n"
                "    pass\n"
            ),
            "solution_code": (
                "import ast\n\n"
                "def detect_unused_imports(code_str: str) -> list:\n"
                "    tree = ast.parse(code_str)\n"
                "    imports = set()\n"
                "    used_names = set()\n"
                "    for node in ast.walk(tree):\n"
                "        if isinstance(node, ast.Import):\n"
                "            for alias in node.names:\n"
                "                imports.add(alias.name)\n"
                "        elif isinstance(node, ast.Name):\n"
                "            used_names.add(node.id)\n"
                "    unused = sorted(list(imports - used_names))\n"
                "    return unused\n\n"
                "sample = 'import math\\nimport os\\nprint(os.getcwd())'\n"
                "print(detect_unused_imports(sample))"
            ),
            "expected_output": "['math']"
        },
        quizzes=[
            {
                "question": "What is the primary difference between Static Code Analysis and Dynamic Analysis?",
                "options": [
                    "Static analysis inspects source code without executing it; dynamic analysis evaluates program behavior during live execution",
                    "Static analysis is only for HTML; dynamic is for SQL",
                    "Dynamic analysis does not need a computer",
                    "There is no difference"
                ],
                "correct_answer": "Static analysis inspects source code without executing it; dynamic analysis evaluates program behavior during live execution",
                "explanation": "Static analysis checks code at rest (AST inspection); dynamic analysis checks code in motion."
            },
            {
                "question": "What Python static analysis tool, written in Rust, has become the industry standard due to being 100x faster than legacy linters?",
                "options": [
                    "Ruff",
                    "Pylint",
                    "Flake8",
                    "Black"
                ],
                "correct_answer": "Ruff",
                "explanation": "Ruff is an extremely fast Python linter and code formatter written in Rust."
            },
            {
                "question": "What does a static type checker like `Mypy` verify in Python?",
                "options": [
                    "It checks that function arguments, return values, and variable assignments adhere to specified type hints (`amount: float`)",
                    "It checks keyboard typing speed",
                    "It changes variable types automatically",
                    "It deletes untyped functions"
                ],
                "correct_answer": "It checks that function arguments, return values, and variable assignments adhere to specified type hints (`amount: float`)",
                "explanation": "Mypy performs compile-time style type verification over Python's optional type annotations."
            },
            {
                "question": "What security-focused static analyzer scans Python source code for vulnerabilities like `eval()`, hardcoded passwords, and SQL injection?",
                "options": [
                    "Bandit",
                    "NPM",
                    "Pip",
                    "Docker"
                ],
                "correct_answer": "Bandit",
                "explanation": "Bandit is a dedicated security linter for finding security flaws in Python codebases."
            },
            {
                "question": "What internal data structure do linters and compilers generate to represent source code structure for analysis?",
                "options": [
                    "Abstract Syntax Tree (AST)",
                    "Binary Heap",
                    "B-Tree Index",
                    "Hash Table"
                ],
                "correct_answer": "Abstract Syntax Tree (AST)",
                "explanation": "Compilers and linters parse source text into an Abstract Syntax Tree (AST) for rule analysis."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 54: Code Reviews & Pair Programming
    # ---------------------------------------------------------
    DayBlueprint(
        order=54,
        title="Day 54: Code Reviews & Pair Programming",
        concept="Peer code reviews and pair programming serve as continuous human verification filters, catching architectural blindspots, edge cases, and maintainability flaws before code merges.",
        analogy="Code review is like having a co-pilot in an airplane cockpit. The pilot flies the aircraft, but before flipping the fuel valve, the co-pilot verifies the checklist: 'Confirmed, fuel valve 2 selected.' Two pairs of eyes ensure simple mental slips never become catastrophic disasters.",
        theory_sections=[
            {
                "heading": "Why Human Code Review is Irreplaceable",
                "content": (
                    "Linters catch syntax and unused variables; automated tests catch known regressions. But only a **human code reviewer** can evaluate:\n"
                    "- **Design & Architecture**: Does this approach solve the business problem cleanly, or does it add technical debt?\n"
                    "- **Edge Cases**: *'What happens if the customer has an expired credit card and clicks submit twice?'*\n"
                    "- **Maintainability**: Can someone else understand this code 6 months from now at 3 AM during an outage?"
                )
            },
            {
                "heading": "Best Practices for Code Reviewers",
                "content": (
                    "1. **Review Small PRs**: A PR with 20 lines of code receives 10 thoughtful comments; a PR with 2,000 lines receives 'Looks good to me' (LGTM). Keep PRs under 400 lines.\n"
                    "2. **Prefix Comments Clearly**: Distinguish blockers from nitpicks:\n"
                    "   - `[BLOCKER]`: Critical bug or security vulnerability that must be fixed before merge.\n"
                    "   - `[NIT]`: Minor styling or optional naming preference.\n"
                    "   - `[QUESTION]`: Seeking architectural clarification."
                )
            },
            {
                "heading": "Pair Programming Dynamics (Driver vs Navigator)",
                "content": (
                    "In pair programming:\n"
                    "- **Driver**: Has their hands on the keyboard, writing code and focusing on immediate syntax.\n"
                    "- **Navigator**: Observes, thinks ahead, looks for edge cases, and consults documentation.\n"
                    "Pairs catch 80% of typos and logic bugs in real time before code is ever saved to disk."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Constructive Code Review Feedback Examples",
                "language": "text",
                "code": (
                    "# BAD REVIEW COMMENT (Vague, abrasive, unhelpful):\n"
                    "# 'This code is terrible. Why did you write it like this?'\n\n"
                    "# CONSTRUCTIVE REVIEW COMMENTS (Clear, educational, actionable):\n"
                    "# [BLOCKER]: On line 42, `user.cart` could be None for guest users,\n"
                    "# which will cause an AttributeError crash. Consider using `user.cart?.items` or a default.\n\n"
                    "# [QUESTION]: Is there a reason we query the DB inside this loop instead\n"
                    "# of performing a single bulk `WHERE id IN (...)` query outside the loop?"
                ),
                "explanation": "Constructive code reviews provide clear rationale, context, and actionable remedies."
            },
            {
                "title": "Pre-Review Checklist for Authors",
                "language": "markdown",
                "code": (
                    "### Author PR Checklist Before Requesting Review:\n"
                    "- [ ] Did I run tests locally (`pytest`)?\n"
                    "- [ ] Did I run the linter (`ruff check .`)?\n"
                    "- [ ] Did I review my own Git diff to remove temporary debug prints?\n"
                    "- [ ] Is the PR title and description clear with screenshots if UI-related?\n"
                    "- [ ] Is this PR under 400 lines of code?"
                ),
                "explanation": "Author self-review catches obvious oversights before consuming reviewer time."
            },
            {
                "title": "Spotting an N+1 Query in Code Review",
                "language": "python",
                "code": (
                    "# Reviewer catches N+1 query problem before it reaches production:\n"
                    "# REVIEW COMMENT: 'This issues 100 SQL queries for 100 users!'\n"
                    "users = db.query('SELECT * FROM users LIMIT 100')\n"
                    "for u in users:\n"
                    "    orders = db.query(f'SELECT * FROM orders WHERE user_id = {u.id}')\n\n"
                    "# FIX: Use SQL JOIN or eager loading\n"
                    "users = db.query('SELECT * FROM users JOIN orders ON ...')"
                ),
                "explanation": "Human reviewers spot architectural antipatterns that compilers and linters miss."
            },
            {
                "title": "Git Pre-Commit Hook Enforcing Clean Diffs",
                "language": "bash",
                "code": (
                    "# .git/hooks/pre-commit:\n"
                    "#!/bin/sh\n"
                    "# Block commits containing raw print statements or debugger pauses\n"
                    "if git diff --cached | grep -E 'breakpoint\\(\\)|console\\.log'; then\n"
                    "    echo '❌ ERROR: Temporary debug statements detected in commit diff!'\n"
                    "    exit 1\n"
                    "fi"
                ),
                "explanation": "Pre-commit hooks automate filtering of accidental debug statements."
            }
        ],
        coding_challenge={
            "title": "Parse and Tally Code Review Comment Severities",
            "instructions": "Write a function `tally_review_comments(comments_list)` that parses a list of comment strings prefixed with `'[BLOCKER]'`, `'[NIT]'`, or `'[QUESTION]'`. Return a dictionary with counts for each category. If no recognized tag is found, count it under `'OTHER'`.",
            "starter_code": (
                "def tally_review_comments(comments: list) -> dict:\n"
                "    # Return {'BLOCKER': int, 'NIT': int, 'QUESTION': int, 'OTHER': int}\n"
                "    pass\n"
            ),
            "solution_code": (
                "def tally_review_comments(comments: list) -> dict:\n"
                "    tally = {'BLOCKER': 0, 'NIT': 0, 'QUESTION': 0, 'OTHER': 0}\n"
                "    for c in comments:\n"
                "        c_strip = c.strip()\n"
                "        matched = False\n"
                "        for tag in ['BLOCKER', 'NIT', 'QUESTION']:\n"
                "            if c_strip.startswith(f'[{tag}]'):\n"
                "                tally[tag] += 1\n"
                "                matched = True\n"
                "                break\n"
                "        if not matched:\n"
                "            tally['OTHER'] += 1\n"
                "    return tally\n\n"
                "sample = ['[BLOCKER] Fix SQL injection', '[NIT] Rename variable', 'Looks good']\n"
                "print(tally_review_comments(sample))"
            ),
            "expected_output": "{'BLOCKER': 1, 'NIT': 1, 'QUESTION': 0, 'OTHER': 1}"
        },
        quizzes=[
            {
                "question": "What is the primary role of a human peer code review that automated linters and tests cannot replace?",
                "options": [
                    "Evaluating business logic architecture, maintainability, readability, and unanticipated real-world edge cases",
                    "Checking syntax errors",
                    "Formatting indentation",
                    "Checking spellings of keywords"
                ],
                "correct_answer": "Evaluating business logic architecture, maintainability, readability, and unanticipated real-world edge cases",
                "explanation": "Human reviewers evaluate design coherence, maintainability, and domain edge cases."
            },
            {
                "question": "Why is keeping a Pull Request (PR) under 400 lines of code considered an engineering best practice?",
                "options": [
                    "Large PRs cause cognitive fatigue, resulting in reviewers skimming and missing critical bugs; small PRs receive detailed attention",
                    "GitHub blocks PRs over 400 lines",
                    "Git cannot merge files over 400 lines",
                    "To save cloud storage costs"
                ],
                "correct_answer": "Large PRs cause cognitive fatigue, resulting in reviewers skimming and missing critical bugs; small PRs receive detailed attention",
                "explanation": "Review quality drops dramatically on large PRs due to cognitive overload."
            },
            {
                "question": "In Pair Programming, what is the role of the 'Navigator'?",
                "options": [
                    "To observe the big picture, look out for edge cases, consult documentation, and guide direction while the driver types",
                    "To tell the driver where to drive their car",
                    "To take notes and deliver coffee",
                    "To compile the code manually"
                ],
                "correct_answer": "To observe the big picture, look out for edge cases, consult documentation, and guide direction while the driver types",
                "explanation": "The navigator thinks strategically about architecture and edge cases while the driver types."
            },
            {
                "question": "What does a `[NIT]` tag indicate when used in a code review comment?",
                "options": [
                    "A non-blocking minor comment, suggestion, or stylistic preference that does not require resolution before merge",
                    "A critical security emergency",
                    "A syntax error that prevents compilation",
                    "A request to delete the repository"
                ],
                "correct_answer": "A non-blocking minor comment, suggestion, or stylistic preference that does not require resolution before merge",
                "explanation": "`[NIT]` communicates that the feedback is optional polish rather than a merge blocker."
            },
            {
                "question": "What is the very first step an author should take before requesting review on a Pull Request?",
                "options": [
                    "Review their own Git diff to remove temporary debug prints and verify automated tests pass",
                    "Ping all managers on Slack",
                    "Merge the PR into master immediately",
                    "Turn off notifications"
                ],
                "correct_answer": "Review their own Git diff to remove temporary debug prints and verify automated tests pass",
                "explanation": "Self-reviewing your diff catches trivial oversights before wasting team review bandwidth."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 55: Unit Testing Foundations (PyTest & Jest)
    # ---------------------------------------------------------
    DayBlueprint(
        order=55,
        title="Day 55: Unit Testing Foundations (PyTest & Jest)",
        concept="Unit testing validates the smallest isolated units of software (individual functions, classes) against deterministic inputs and assertions, creating an automated regression safety shield.",
        analogy="Think of building an airplane. Before bolting a jet engine onto the wing, aeronautical engineers mount the engine on an isolated test stand in a hangar, measure fuel flow, test spark plugs, and rev the throttle to 10,000 RPM. Unit testing tests the engine alone before connecting it to the plane.",
        theory_sections=[
            {
                "heading": "The AAA Pattern (Arrange, Act, Assert)",
                "content": (
                    "Every robust unit test follows 3 distinct phases:\n"
                    "1. **Arrange**: Set up the initial state, test data, and preconditions (`cart = Cart()`, `user = User(age=25)`).\n"
                    "2. **Act**: Invoke the single method or function under test (`cart.add_item(item)`).\n"
                    "3. **Assert**: Verify that the actual output strictly matches the expected outcome (`assert cart.total == 50.00`)."
                )
            },
            {
                "heading": "The 4 Hallmarks of Great Unit Tests (FIRST Principle)",
                "content": (
                    "- **Fast**: Must run in milliseconds so engineers run them after every edit.\n"
                    "- **Independent / Isolated**: Tests must not depend on other tests or execution order.\n"
                    "- **Repeatable**: Produces the identical result every time (no dependence on system clock or internet).\n"
                    "- **Self-Validating**: Passes with green exit code 0 or fails with red descriptive assertion error."
                )
            },
            {
                "heading": "Parametrization: Testing 20 Edge Cases in 5 Lines",
                "content": (
                    "Instead of writing 20 separate test functions, `pytest.mark.parametrize` allows running one test logic across multiple input/output tuples (empty strings, zero, negative numbers, max integers)."
                )
            }
        ],
        code_snippets=[
            {
                "title": "A PyTest Unit Test Following the AAA Pattern",
                "language": "python",
                "code": (
                    "import pytest\n\n"
                    "def calculate_discount(price: float, discount_pct: float) -> float:\n"
                    "    if price < 0 or not (0 <= discount_pct <= 100):\n"
                    "        raise ValueError('Invalid input parameters')\n"
                    "    return round(price * (1 - discount_pct / 100), 2)\n\n"
                    "def test_calculate_discount_standard():\n"
                    "    # 1. Arrange\n"
                    "    price = 100.0\n"
                    "    pct = 20.0\n"
                    "    # 2. Act\n"
                    "    result = calculate_discount(price, pct)\n"
                    "    # 3. Assert\n"
                    "    assert result == 80.0"
                ),
                "explanation": "Clear demonstration of Arrange, Act, and Assert in PyTest."
            },
            {
                "title": "Testing Exceptions with `pytest.raises`",
                "language": "python",
                "code": (
                    "def test_calculate_discount_negative_price_raises_error():\n"
                    "    # Verify that invalid input triggers the expected ValueError\n"
                    "    with pytest.raises(ValueError) as exc_info:\n"
                    "        calculate_discount(-50.0, 10.0)\n"
                    "    assert 'Invalid input parameters' in str(exc_info.value)"
                ),
                "explanation": "`pytest.raises` validates that functions raise expected exceptions on invalid inputs."
            },
            {
                "title": "Parametrized Testing Across Multiple Edge Cases",
                "language": "python",
                "code": (
                    "@pytest.mark.parametrize('price, pct, expected', [\n"
                    "    (100.0, 0.0, 100.0),    # 0% discount\n"
                    "    (100.0, 100.0, 0.0),    # 100% discount (free)\n"
                    "    (50.0, 50.0, 25.0),     # 50% discount\n"
                    "    (99.99, 10.0, 89.99),   # Precision rounding check\n"
                    "])\n"
                    "def test_calculate_discount_scenarios(price, pct, expected):\n"
                    "    assert calculate_discount(price, pct) == expected"
                ),
                "explanation": "Runs single test logic across multiple test cases cleanly."
            },
            {
                "title": "Jest Equivalent in JavaScript / TypeScript",
                "language": "javascript",
                "code": (
                    "// In Jest (test.js)\n"
                    "describe('calculateDiscount', () => {\n"
                    "  it('should apply 20% discount correctly', () => {\n"
                    "    const result = calculateDiscount(100, 20);\n"
                    "    expect(result).toBe(80);\n"
                    "  });\n"
                    "  it('should throw an error for negative prices', () => {\n"
                    "    expect(() => calculateDiscount(-10, 20)).toThrow('Invalid');\n"
                    "  });\n"
                    "});"
                ),
                "explanation": "Demonstrates identical unit testing concepts in JavaScript's Jest framework."
            }
        ],
        coding_challenge={
            "title": "Write Complete Unit Test Suite for Palindrome Checker",
            "instructions": "Write a function `run_palindrome_tests(fn_under_test)` that calls `fn_under_test(string)` across 4 test cases: `'racecar'` (True), `'hello'` (False), `''` (True), and `'A man a plan a canal Panama'` (True, case/space insensitive). Return True if all 4 tests pass, or False if any assertion fails.",
            "starter_code": (
                "def run_palindrome_tests(fn) -> bool:\n"
                "    # Return True if fn passes all 4 palindrome test cases\n"
                "    pass\n"
            ),
            "solution_code": (
                "def run_palindrome_tests(fn) -> bool:\n"
                "    try:\n"
                "        assert fn('racecar') is True\n"
                "        assert fn('hello') is False\n"
                "        assert fn('') is True\n"
                "        assert fn('A man a plan a canal Panama') is True\n"
                "        return True\n"
                "    except AssertionError:\n"
                "        return False\n\n"
                "def good_palindrome(s: str) -> bool:\n"
                "    clean = [c.lower() for c in s if c.isalnum()]\n"
                "    return clean == clean[::-1]\n\n"
                "print(run_palindrome_tests(good_palindrome))"
            ),
            "expected_output": "True"
        },
        quizzes=[
            {
                "question": "What are the three sequential phases of the standard AAA unit testing pattern?",
                "options": [
                    "Arrange, Act, and Assert",
                    "Assemble, Apply, and Archive",
                    "Authenticate, Authorize, and Audit",
                    "Allocate, Access, and Abort"
                ],
                "correct_answer": "Arrange, Act, and Assert",
                "explanation": "Arrange (setup preconditions), Act (invoke function), and Assert (verify outputs)."
            },
            {
                "question": "Why should unit tests execute in milliseconds rather than minutes?",
                "options": [
                    "Fast test suites can be executed continuously after every single code edit, providing immediate regression feedback",
                    "Computers get tired if tests take too long",
                    "Fast tests use less internet bandwidth",
                    "Python limits test execution time to 1 second"
                ],
                "correct_answer": "Fast test suites can be executed continuously after every single code edit, providing immediate regression feedback",
                "explanation": "Rapid tests encourage developers to run test suites frequently during active development."
            },
            {
                "question": "How do you test that a function raises an expected exception in PyTest?",
                "options": [
                    "Using the `with pytest.raises(ExceptionType):` context manager",
                    "By catching the error with `except: pass`",
                    "By printing the error to stdout",
                    "PyTest cannot test exceptions"
                ],
                "correct_answer": "Using the `with pytest.raises(ExceptionType):` context manager",
                "explanation": "`pytest.raises` asserts that the enclosed block raises the specified exception."
            },
            {
                "question": "What PyTest decorator allows running a single test function across 10 different input and expected output combinations?",
                "options": [
                    "`@pytest.mark.parametrize`",
                    "`@pytest.mark.loop`",
                    "`@pytest.mark.batch`",
                    "`@pytest.mark.repeat`"
                ],
                "correct_answer": "`@pytest.mark.parametrize`",
                "explanation": "`parametrize` feeds parameter tuples into a single test function, generating distinct sub-tests."
            },
            {
                "question": "What does a Unit Test test, by strict definition?",
                "options": [
                    "The smallest isolated piece of code (a single function, class, or method) independent from external databases or networks",
                    "The entire web application and cloud infrastructure together",
                    "The physical monitor and keyboard hardware",
                    "The company's Wi-Fi speed"
                ],
                "correct_answer": "The smallest isolated piece of code (a single function, class, or method) independent from external databases or networks",
                "explanation": "Unit testing isolates individual modular units from external dependencies."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 56: Test-Driven Development (TDD: Red-Green-Refactor)
    # ---------------------------------------------------------
    DayBlueprint(
        order=56,
        title="Day 56: Test-Driven Development (TDD: Red-Green-Refactor)",
        concept="Test-Driven Development (TDD) flips traditional programming by writing an automated failing test before writing any implementation code, driving minimalist design and eliminating unverified code.",
        analogy="Think of baking cookies using a cookie cutter. You don't bake a giant, random blob of dough and then hope it accidentally shapes into a star. You place the star-shaped cutter on the table first (the test), press the dough into the exact mold (the code), and trim off the excess crumbs (refactor).",
        theory_sections=[
            {
                "heading": "The 3 Stages of the TDD Cycle",
                "content": (
                    "1. 🔴 **RED**: Write an automated test for a feature or edge case that does not exist yet. Run the test and watch it fail (confirming the test is actually testing something).\n"
                    "2. 🟢 **GREEN**: Write the **simplest, bare minimum code** necessary to make the test pass. Do not write extra features or premature optimizations.\n"
                    "3. 🔵 **REFACTOR**: Clean up the code—remove duplication, rename variables, extract helper methods. The green tests guarantee your refactoring breaks nothing."
                )
            },
            {
                "heading": "Why TDD Prevents Bugs",
                "content": (
                    "- **Zero Untested Code**: It is impossible to have untested logic because code is only written to satisfy a failing test.\n"
                    "- **Prevents Over-Engineering**: You write only what is required to pass the test, preventing bloated unused abstractions.\n"
                    "- **Design Clarity**: Writing the test first forces you to think as a client of the API, resulting in cleaner function signatures."
                )
            }
        ],
        code_snippets=[
            {
                "title": "TDD Step 1: 🔴 RED (Write Failing Test First)",
                "language": "python",
                "code": (
                    "# Requirement: A function to parse hashtags from tweet text\n"
                    "# Step 1: Write test BEFORE writing extract_hashtags() function!\n"
                    "import pytest\n\n"
                    "def test_extract_hashtags():\n"
                    "    text = 'Learning #python and #debugging is fun!'\n"
                    "    # Running this now fails with NameError: name 'extract_hashtags' is not defined!\n"
                    "    assert extract_hashtags(text) == ['python', 'debugging']"
                ),
                "explanation": "The test fails predictably because the target function has not been created yet."
            },
            {
                "title": "TDD Step 2: 🟢 GREEN (Minimal Code to Pass)",
                "language": "python",
                "code": (
                    "# Step 2: Write minimal implementation to pass the test\n"
                    "def extract_hashtags(text: str) -> list[str]:\n"
                    "    words = text.split()\n"
                    "    return [w[1:] for w in words if w.startswith('#')]\n\n"
                    "# Run pytest: PASSED (GREEN)!"
                ),
                "explanation": "Writing the simplest possible logic to achieve green passing status."
            },
            {
                "title": "TDD Next Iteration: 🔴 Handling Punctuation Edge Case",
                "language": "python",
                "code": (
                    "# Step 3: Write new failing test for punctuation: '#python!' -> 'python'\n"
                    "def test_extract_hashtags_with_punctuation():\n"
                    "    text = 'Love #coding, especially #ai.'\n"
                    "    # Current implementation returns ['coding,', 'ai.'] -> FAILS (RED)!\n"
                    "    assert extract_hashtags(text) == ['coding', 'ai']"
                ),
                "explanation": "Exposes punctuation limitation by writing an explicit failing test."
            },
            {
                "title": "TDD Step 3: 🔵 REFACTOR (Clean Implementation with Regex)",
                "language": "python",
                "code": (
                    "import re\n\n"
                    "# Refactor implementation cleanly using regular expressions\n"
                    "def extract_hashtags(text: str) -> list[str]:\n"
                    "    return re.findall(r'#(\\w+)', text)\n\n"
                    "# Run all tests: ALL PASSED (GREEN)!"
                ),
                "explanation": "Refactoring logic cleanly while automated tests guarantee zero regressions."
            }
        ],
        coding_challenge={
            "title": "TDD Implementation of Roman Numeral Converter",
            "instructions": "Implement `roman_to_int(roman_str)` to satisfy the following test cases: `'I'` -> 1, `'IV'` -> 4, `'IX'` -> 9, `'LVIII'` -> 58, `'MCMXCIV'` -> 1994. Handle subtractive combinations properly.",
            "starter_code": (
                "def roman_to_int(s: str) -> int:\n"
                "    # Return integer value of roman numeral\n"
                "    pass\n"
            ),
            "solution_code": (
                "def roman_to_int(s: str) -> int:\n"
                "    vals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}\n"
                "    total = 0\n"
                "    for i in range(len(s)):\n"
                "        if i + 1 < len(s) and vals[s[i]] < vals[s[i + 1]]:\n"
                "            total -= vals[s[i]]\n"
                "        else:\n"
                "            total += vals[s[i]]\n"
                "    return total\n\n"
                "print(roman_to_int('MCMXCIV'))\n"
                "print(roman_to_int('LVIII'))"
            ),
            "expected_output": "1994\n58"
        },
        quizzes=[
            {
                "question": "What is the core sequence of the Test-Driven Development (TDD) cycle?",
                "options": [
                    "Red (Write failing test) -> Green (Write minimal passing code) -> Refactor (Clean up)",
                    "Write code -> Deploy -> Test in production",
                    "Compile -> Link -> Execute",
                    "Plan -> Code -> Delete"
                ],
                "correct_answer": "Red (Write failing test) -> Green (Write minimal passing code) -> Refactor (Clean up)",
                "explanation": "Red-Green-Refactor is the foundational cadence of test-driven development."
            },
            {
                "question": "Why is it critical to watch the test fail (RED) before writing the implementation code in TDD?",
                "options": [
                    "To verify that the test is actually evaluating real logic and won't pass spuriously due to a flawed assertion",
                    "Because compilers require errors on line 1",
                    "To clear the test runner cache",
                    "It is legally required by software standards"
                ],
                "correct_answer": "To verify that the test is actually evaluating real logic and won't pass spuriously due to a flawed assertion",
                "explanation": "Watching a test fail confirms it is truly testing functionality and not trivially tautological."
            },
            {
                "question": "In the GREEN phase of TDD, how much code should you write?",
                "options": [
                    "Only the absolute bare minimum code required to make the failing test pass",
                    "The entire feature and all future features",
                    "At least 500 lines",
                    "Only comments"
                ],
                "correct_answer": "Only the absolute bare minimum code required to make the failing test pass",
                "explanation": "Writing only minimal code keeps implementations lean and prevents over-engineering."
            },
            {
                "question": "What allows developers to aggressively refactor code in the REFACTOR phase of TDD without fear of breaking functionality?",
                "options": [
                    "The comprehensive suite of passing automated unit tests acts as a continuous safety regression shield",
                    "The code is stored in the cloud",
                    "The compiler prevents bugs during refactoring",
                    "Refactoring never introduces bugs"
                ],
                "correct_answer": "The comprehensive suite of passing automated unit tests acts as a continuous safety regression shield",
                "explanation": "Automated tests immediately alert developers if any refactoring breaks existing behavior."
            },
            {
                "question": "How does TDD improve API design and function signatures?",
                "options": [
                    "Writing tests first forces developers to think as the consumer of the API, resulting in more intuitive interfaces",
                    "It forces all functions to be asynchronous",
                    "It encrypts function names",
                    "It eliminates the need for arguments"
                ],
                "correct_answer": "Writing tests first forces developers to think as the consumer of the API, resulting in more intuitive interfaces",
                "explanation": "Test-first thinking emphasizes consumer developer experience (DX) and ergonomic signatures."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 57: Integration Testing & Mocking External Systems
    # ---------------------------------------------------------
    DayBlueprint(
        order=57,
        title="Day 57: Integration Testing & Mocking External Systems",
        concept="Integration testing validates the collaboration between multiple connected components (Controllers, Services, Databases), using test doubles (Mocks, Stubs) to isolate external third-party dependencies.",
        analogy="If unit testing is testing whether a spark plug sparks on a workbench, integration testing is connecting the spark plug, fuel injector, and piston together inside an engine block to verify they fire in synchronized harmony.",
        theory_sections=[
            {
                "heading": "Unit Testing vs Integration Testing",
                "content": (
                    "- **Unit Test**: Tests a single pure function in complete isolation.\n"
                    "- **Integration Test**: Tests how multiple modules communicate (e.g. an API route writing to a real test database, then triggering an email service).\n"
                    "Most production bugs occur at the **seams** between components (e.g. SQL data type mismatches, serialization errors)."
                )
            },
            {
                "heading": "Mocks, Stubs, and Spies (Test Doubles)",
                "content": (
                    "When testing code that sends real credit card charges or SMS messages, you must NOT hit real external APIs:\n"
                    "- **Stub**: An object providing pre-canned answers to calls (e.g. `mock_fetch.return_value = {'status': 'ok'}`).\n"
                    "- **Mock**: An object that records calls and verifies interactions (e.g. `mock_mailer.send.assert_called_once_with('user@test.com')`).\n"
                    "- **Spy**: Wraps a real object to observe how it was invoked."
                )
            },
            {
                "heading": "Testing with Ephemeral Databases (Testcontainers / SQLite)",
                "content": (
                    "Best practice for database integration testing is spinning up a lightweight Docker container (via Testcontainers) or dedicated test database that is migrated, tested, and wiped clean on every run."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Mocking External HTTP Requests with `unittest.mock`",
                "language": "python",
                "code": (
                    "from unittest.mock import patch, MagicMock\n"
                    "import requests\n\n"
                    "def get_weather_forecast(city: str) -> str:\n"
                    "    res = requests.get(f'https://weather.api/v1/{city}')\n"
                    "    return res.json()['forecast']\n\n"
                    "@patch('requests.get')\n"
                    "def test_weather_with_mock(mock_get):\n"
                    "    # Configure mock response without making real network call\n"
                    "    mock_res = MagicMock()\n"
                    "    mock_res.json.return_value = {'forecast': 'Sunny'}\n"
                    "    mock_get.return_value = mock_res\n\n"
                    "    # Act & Assert\n"
                    "    assert get_weather_forecast('Tokyo') == 'Sunny'\n"
                    "    mock_get.assert_called_once_with('https://weather.api/v1/Tokyo')"
                ),
                "explanation": "`@patch` intercepts external calls, returning deterministic mocked responses."
            },
            {
                "title": "FastAPI Integration Testing with `TestClient`",
                "language": "python",
                "code": (
                    "from fastapi.testclient import TestClient\n"
                    "from app import app\n\n"
                    "client = TestClient(app)\n\n"
                    "def test_create_and_fetch_order():\n"
                    "    # 1. POST create order\n"
                    "    res = client.post('/api/orders', json={'product_id': 10, 'qty': 2})\n"
                    "    assert res.status_code == 201\n"
                    "    order_id = res.json()['id']\n\n"
                    "    # 2. GET verify order was persisted\n"
                    "    get_res = client.get(f'/api/orders/{order_id}')\n"
                    "    assert get_res.status_code == 200\n"
                    "    assert get_res.json()['product_id'] == 10"
                ),
                "explanation": "Tests full multi-layer API integration from route to database."
            },
            {
                "title": "PyTest Fixtures for Test Database Lifecycle",
                "language": "python",
                "code": (
                    "import pytest\n\n"
                    "@pytest.fixture(scope='function')\n"
                    "def test_db():\n"
                    "    # Setup: create clean tables\n"
                    "    db = create_test_database()\n"
                    "    yield db # Hands control to test function\n"
                    "    # Teardown: truncate tables after test finishes\n"
                    "    db.drop_all()"
                ),
                "explanation": "Fixtures guarantee clean database state before and after every test execution."
            },
            {
                "title": "Mocking Built-in System Time",
                "language": "python",
                "code": (
                    "# Using pip install freezegun to test time-sensitive logic\n"
                    "from freezegun import freeze_time\n\n"
                    "@freeze_time('2026-01-01 12:00:00')\n"
                    "def test_subscription_expiration():\n"
                    "    sub = create_monthly_subscription()\n"
                    "    assert str(sub.expires_at) == '2026-02-01 12:00:00'"
                ),
                "explanation": "`freezegun` freezes system time for deterministic testing of expiration logic."
            }
        ],
        coding_challenge={
            "title": "Build a Mock Billing Service Stub",
            "instructions": "Write a mock class `MockBillingService` with method `charge(user_id, amount)`. It should record every charge in a list `self.charges` as `{'uid': user_id, 'amount': amount}` and return `{'status': 'SUCCESS', 'charge_id': f'ch_{len(self.charges)}'}`. If amount is negative, raise `ValueError('NEGATIVE_CHARGE')`.",
            "starter_code": (
                "class MockBillingService:\n"
                "    def __init__(self):\n"
                "        pass\n\n"
                "    def charge(self, user_id: int, amount: float) -> dict:\n"
                "        pass\n"
            ),
            "solution_code": (
                "class MockBillingService:\n"
                "    def __init__(self):\n"
                "        self.charges = []\n\n"
                "    def charge(self, user_id: int, amount: float) -> dict:\n"
                "        if amount < 0:\n"
                "            raise ValueError('NEGATIVE_CHARGE')\n"
                "        record = {'uid': user_id, 'amount': amount}\n"
                "        self.charges.append(record)\n"
                "        return {'status': 'SUCCESS', 'charge_id': f'ch_{len(self.charges)}'}\n\n"
                "mock = MockBillingService()\n"
                "res = mock.charge(101, 49.99)\n"
                "print(res['charge_id'], len(mock.charges))"
            ),
            "expected_output": "ch_1 1"
        },
        quizzes=[
            {
                "question": "What is the primary objective of Integration Testing compared to Unit Testing?",
                "options": [
                    "To verify that multiple connected software modules (e.g. API controllers, services, database queries) work together properly",
                    "To test only individual math functions",
                    "To format CSS code",
                    "To buy cloud server hosting"
                ],
                "correct_answer": "To verify that multiple connected software modules (e.g. API controllers, services, database queries) work together properly",
                "explanation": "Integration testing targets the interaction seams between cooperating components."
            },
            {
                "question": "Why should external third-party services (like Stripe payments or Twilio SMS) be mocked during automated testing?",
                "options": [
                    "To avoid charging real credit cards, incurring API fees, depending on external network uptime, and slowing down test suites",
                    "Because third-party APIs forbid tests",
                    "Because Python cannot send network calls",
                    "To avoid using RAM"
                ],
                "correct_answer": "To avoid charging real credit cards, incurring API fees, depending on external network uptime, and slowing down test suites",
                "explanation": "Mocks eliminate external network dependencies, costs, and side effects during test runs."
            },
            {
                "question": "In Python testing, what does the `@patch` decorator from `unittest.mock` do?",
                "options": [
                    "It temporarily replaces a target object, function, or module attribute with a Mock during the execution of the test",
                    "It downloads software updates from GitHub",
                    "It repairs syntax errors automatically",
                    "It reboots the operating system"
                ],
                "correct_answer": "It temporarily replaces a target object, function, or module attribute with a Mock during the execution of the test",
                "explanation": "`@patch` swaps real functions with mock stand-ins during the scoped test execution."
            },
            {
                "question": "What is a PyTest 'Fixture'?",
                "options": [
                    "A reusable setup and teardown function that prepares state (e.g. clean test databases, auth tokens) and cleans it up after tests finish",
                    "A broken test that cannot be fixed",
                    "A permanent hardware installation in a server room",
                    "A tool for formatting code"
                ],
                "correct_answer": "A reusable setup and teardown function that prepares state (e.g. clean test databases, auth tokens) and cleans it up after tests finish",
                "explanation": "Fixtures manage test dependencies, lifecycle preconditions, and cleanup teardown."
            },
            {
                "question": "What library is commonly used in Python to freeze system time for deterministic testing of subscriptions or token expirations?",
                "options": [
                    "`freezegun`",
                    "`time_pause`",
                    "`stopwatch`",
                    "`clock_lock`"
                ],
                "correct_answer": "`freezegun`",
                "explanation": "`freezegun` freezes Python `datetime.now()` to fixed timestamps for deterministic testing."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 58: End-to-End (E2E) Testing (Cypress & Playwright)
    # ---------------------------------------------------------
    DayBlueprint(
        order=58,
        title="Day 58: End-to-End (E2E) Testing (Cypress & Playwright)",
        concept="End-to-End (E2E) testing controls headless browser instances to simulate real user journeys across the entire application stack—clicking buttons, filling forms, and validating visual states.",
        analogy="If unit testing is testing a tire, and integration testing is assembling the engine and transmission, E2E testing is a crash-test dummy sitting in the driver's seat, turning the key, driving 60 MPH down a real highway in the rain, and verifying that the wipers turn on and the brakes stop the car.",
        theory_sections=[
            {
                "heading": "The Testing Pyramid (Unit vs Integration vs E2E)",
                "content": (
                    "- **Base (70%): Unit Tests**: Ultra-fast (ms), isolated, cheap to maintain.\n"
                    "- **Middle (20%): Integration Tests**: Moderate speed, test API-to-database communication.\n"
                    "- **Top (10%): E2E Tests**: Slower (seconds), drive real headless Chromium/Firefox/WebKit browsers.\n"
                    "E2E tests verify the complete customer experience from frontend DOM to backend database."
                )
            },
            {
                "heading": "Playwright vs Cypress: The Modern Standards",
                "content": (
                    "- **Playwright (Microsoft)**: Ultra-fast, multi-tab, multi-browser (Chrome, Firefox, Safari WebKit), native mobile emulation, automatic waiting.\n"
                    "- **Cypress**: Developer-friendly interactive UI runner with time-travel debugging.\n"
                    "Both tools eliminate the flakiness of legacy Selenium by **automatically waiting for elements to become visible and actionable** before clicking."
                )
            },
            {
                "heading": "Eliminating Flaky E2E Tests",
                "content": (
                    "A 'Flaky Test' passes 9 times and randomly fails once due to network race conditions. Best practices:\n"
                    "- Never use hardcoded sleeps (`sleep(5000)`).\n"
                    "- Use resilient selectors (`data-testid=\"submit-btn\"`) instead of brittle CSS classes (`div > button.btn-blue`)."
                )
            }
        ],
        code_snippets=[
            {
                "title": "A Playwright E2E User Journey Test (TypeScript / JS)",
                "language": "javascript",
                "code": (
                    "import { test, expect } from '@playwright/test';\n\n"
                    "test('User can search, add item to cart, and checkout', async ({ page }) => {\n"
                    "  // 1. Navigate to live app\n"
                    "  await page.goto('https://shop.example.com');\n\n"
                    "  // 2. Type into search using resilient data-testid\n"
                    "  await page.fill('[data-testid=\"search-input\"]', 'Wireless Headphones');\n"
                    "  await page.press('[data-testid=\"search-input\"]', 'Enter');\n\n"
                    "  // 3. Click add to cart (Playwright automatically waits for button to be clickable!)\n"
                    "  await page.click('[data-testid=\"add-to-cart-btn\"]');\n\n"
                    "  // 4. Assert cart badge updates\n"
                    "  const cartBadge = page.locator('[data-testid=\"cart-count\"]');\n"
                    "  await expect(cartBadge).toHaveText('1');\n"
                    "});"
                ),
                "explanation": "Simulates complete end-to-end user navigation with automatic waiting."
            },
            {
                "title": "Cypress Test Scenario with Intercepted Network Call",
                "language": "javascript",
                "code": (
                    "describe('Login Flow', () => {\n"
                    "  it('authenticates and redirects to dashboard', () => {\n"
                    "    cy.visit('/login');\n"
                    "    cy.get('input[name=\"email\"]').type('user@test.com');\n"
                    "    cy.get('input[name=\"password\"]').type('Secret123!');\n"
                    "    cy.get('button[type=\"submit\"]').click();\n\n"
                    "    // Verify URL and dashboard header\n"
                    "    cy.url().should('include', '/dashboard');\n"
                    "    cy.contains('h1', 'Welcome back, User').should('be.visible');\n"
                    "  });\n"
                    "});"
                ),
                "explanation": "Cypress test scenario verifying complete authentication flow."
            },
            {
                "title": "Using `data-testid` Attributes for Resilient Selectors",
                "language": "html",
                "code": (
                    "<!-- FRAGILE: Brittle selector breaks when Tailwind class is edited -->\n"
                    "<button class=\"bg-blue-500 hover:bg-blue-600 rounded px-4\">Checkout</button>\n\n"
                    "<!-- RESILIENT: Dedicated test ID immune to CSS refactoring -->\n"
                    "<button data-testid=\"checkout-submit-btn\" class=\"bg-blue-500 rounded\">Checkout</button>"
                ),
                "explanation": "`data-testid` decouples automated tests from styling refactors."
            },
            {
                "title": "Running Playwright in Headless CI Mode",
                "language": "bash",
                "code": (
                    "# Run tests across Chromium, Firefox, and WebKit in headless mode\n"
                    "npx playwright test --workers=4\n\n"
                    "# View visual trace viewer on failure\n"
                    "npx playwright show-trace trace.zip"
                ),
                "explanation": "CLI execution suitable for automated headless CI/CD pipeline runners."
            }
        ],
        coding_challenge={
            "title": "Simulate E2E Step Executor",
            "instructions": "Write a function `execute_e2e_steps(steps_list, page_state)` where `steps_list` is a list of tuples: `('fill', key, val)` which sets `page_state[key] = val`, or `('assert', key, val)` which verifies `page_state[key] == val`. If all asserts match, return `'TEST_PASSED'`. If an assert fails, return `'TEST_FAILED: <key>'`.",
            "starter_code": (
                "def execute_e2e_steps(steps: list, state: dict) -> str:\n"
                "    # Execute fill and assert steps\n"
                "    pass\n"
            ),
            "solution_code": (
                "def execute_e2e_steps(steps: list, state: dict) -> str:\n"
                "    for action, key, val in steps:\n"
                "        if action == 'fill':\n"
                "            state[key] = val\n"
                "        elif action == 'assert':\n"
                "            if state.get(key) != val:\n"
                "                return f'TEST_FAILED: {key}'\n"
                "    return 'TEST_PASSED'\n\n"
                "test_steps = [\n"
                "    ('fill', 'username', 'admin'),\n"
                "    ('fill', 'is_logged_in', True),\n"
                "    ('assert', 'is_logged_in', True)\n"
                "]\n"
                "print(execute_e2e_steps(test_steps, {}))"
            ),
            "expected_output": "TEST_PASSED"
        },
        quizzes=[
            {
                "question": "What is the primary role of End-to-End (E2E) testing?",
                "options": [
                    "To simulate real user journeys by driving headless browsers through the entire application stack from UI to backend database",
                    "To test individual Python math formulas",
                    "To compress video files",
                    "To replace database indexes"
                ],
                "correct_answer": "To simulate real user journeys by driving headless browsers through the entire application stack from UI to backend database",
                "explanation": "E2E testing validates complete customer workflows through automated browser manipulation."
            },
            {
                "question": "Which modern E2E testing framework, developed by Microsoft, supports cross-browser automation across Chromium, Firefox, and Safari WebKit with automatic waiting?",
                "options": [
                    "Playwright",
                    "Postman",
                    "GDB",
                    "Valgrind"
                ],
                "correct_answer": "Playwright",
                "explanation": "Playwright is Microsoft's modern multi-browser automation framework."
            },
            {
                "question": "What is a 'Flaky Test' in automated testing?",
                "options": [
                    "A test that passes or fails intermittently on the same code without any changes, usually due to timing or network race conditions",
                    "A test that compiles into assembly",
                    "A test written in JavaScript",
                    "A test that takes less than 1 second to run"
                ],
                "correct_answer": "A test that passes or fails intermittently on the same code without any changes, usually due to timing or network race conditions",
                "explanation": "Flaky tests exhibit non-deterministic pass/fail outcomes, eroding trust in CI suites."
            },
            {
                "question": "Why is using `data-testid=\"submit-btn\"` superior to selecting elements by CSS class (e.g. `cy.get('.btn-primary')`)?",
                "options": [
                    "`data-testid` is dedicated strictly to testing and does not break when designers or developers refactor CSS styles",
                    "`data-testid` runs 10x faster in hardware",
                    "`data-testid` encrypts the button",
                    "CSS classes are banned in HTML5"
                ],
                "correct_answer": "`data-testid` is dedicated strictly to testing and does not break when designers or developers refactor CSS styles",
                "explanation": "Dedicated test attributes decouple test selectors from visual style modifications."
            },
            {
                "question": "According to the Testing Pyramid, why should E2E tests comprise a smaller percentage of your test suite than unit tests?",
                "options": [
                    "E2E tests are slower to execute, consume more infrastructure resources, and are more expensive to maintain than unit tests",
                    "E2E tests cannot find real bugs",
                    "E2E tests are illegal in commercial apps",
                    "E2E tests can only run once per week"
                ],
                "correct_answer": "E2E tests are slower to execute, consume more infrastructure resources, and are more expensive to maintain than unit tests",
                "explanation": "The Testing Pyramid balances fast unit test foundations with focused E2E apex verification."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 59: CI/CD Pipeline Checks (Automated Quality Gates)
    # ---------------------------------------------------------
    DayBlueprint(
        order=59,
        title="Day 59: CI/CD Pipeline Checks (Automated Quality Gates)",
        concept="Continuous Integration & Deployment (CI/CD) pipelines enforce automated quality gates on every Pull Request, blocking code from merging if linters, unit tests, security scans, or build stages fail.",
        analogy="A CI/CD pipeline is like the automated quality control conveyor belt in an automobile factory. Before a car is allowed to drive out to the dealership, it passes through 5 automated scanner gates: paint inspection (linter), engine compression check (unit tests), crash simulation (integration tests), and emissions test (security scan). If any sensor beeps red, the conveyor belt halts instantly.",
        theory_sections=[
            {
                "heading": "The Core Philosophy of Continuous Integration (CI)",
                "content": (
                    "Without CI, developers integrate code once a month, resulting in 'Merge Hell'—hundreds of conflicting changes that take weeks to stabilize.\n\n"
                    "**Continuous Integration** enforces frequent merges into the main trunk, verified by an automated build runner on every commit:\n"
                    "1. Spin up clean ephemeral container runner (GitHub Actions, GitLab CI, CircleCI).\n"
                    "2. Install exact locked dependencies (`poetry install` or `npm ci`).\n"
                    "3. Run static analysis & linters (`ruff check .`, `eslint .`).\n"
                    "4. Run automated test suites with coverage thresholds (`pytest --cov=app`).\n"
                    "5. Run security vulnerability scans (`bandit`, `npm audit`).\n"
                    "If **any single stage fails with non-zero exit code**, the Pull Request merge button is **hard-locked**."
                )
            },
            {
                "heading": "Matrix Builds across Operating Systems and Versions",
                "content": (
                    "CI pipelines can test code across a matrix of environments simultaneously:\n"
                    "- Python 3.10, 3.11, 3.12.\n"
                    "- Ubuntu, macOS, Windows.\n"
                    "This catches platform-specific bugs (such as path separator slashes `\\` vs `/`) before software ships."
                )
            }
        ],
        code_snippets=[
            {
                "title": "GitHub Actions Automated CI Workflow (`.github/workflows/ci.yml`)",
                "language": "yaml",
                "code": (
                    "name: Automated Quality Gates\n\n"
                    "on:\n"
                    "  pull_request:\n"
                    "    branches: [main]\n"
                    "  push:\n"
                    "    branches: [main]\n\n"
                    "jobs:\n"
                    "  test:\n"
                    "    runs-on: ubuntu-latest\n"
                    "    steps:\n"
                    "      - name: Checkout code\n"
                    "        uses: actions/checkout@v4\n\n"
                    "      - name: Set up Python 3.11\n"
                    "        uses: actions/setup-python@v5\n"
                    "        with:\n"
                    "          python-version: '3.11'\n"
                    "          cache: 'pip'\n\n"
                    "      - name: Install dependencies\n"
                    "        run: pip install -r requirements.txt\n\n"
                    "      - name: Lint and Static Analysis\n"
                    "        run: ruff check .\n\n"
                    "      - name: Security Vulnerability Scan\n"
                    "        run: bandit -r app/\n\n"
                    "      - name: Run Test Suite with Coverage\n"
                    "        run: pytest --cov=app --cov-fail-under=80"
                ),
                "explanation": "Standard GitHub Actions pipeline enforcing linting, security scans, and 80% test coverage."
            },
            {
                "title": "Matrix Strategy Testing Across Python Versions",
                "language": "yaml",
                "code": (
                    "# Test across multiple Python versions concurrently\n"
                    "strategy:\n"
                    "  matrix:\n"
                    "    python-version: ['3.10', '3.11', '3.12']\n"
                    "    os: [ubuntu-latest, macos-latest]"
                ),
                "explanation": "Matrix configurations execute tests across multiple OS and runtime combinations in parallel."
            },
            {
                "title": "Enforcing Branch Protection in GitHub",
                "language": "text",
                "code": (
                    "GitHub Repository Settings -> Branches -> 'Protect main branch':\n"
                    "- Check: 'Require status checks to pass before merging'\n"
                    "- Select required checks: 'Automated Quality Gates / test'\n"
                    "- Check: 'Require branches to be up to date before merging'\n"
                    "- Result: Nobody (even admins) can push broken code to main!"
                ),
                "explanation": "Branch protection rules enforce automated CI gates at the repository level."
            },
            {
                "title": "Caching CI Dependencies to Speed Up Pipelines",
                "language": "yaml",
                "code": (
                    "# Caching pip wheels saves 3 minutes on every CI run:\n"
                    "- uses: actions/cache@v3\n"
                    "  with:\n"
                    "    path: ~/.cache/pip\n"
                    "    key: ${{ runner.os }}-pip-${{ hashFiles('**/requirements.txt') }}"
                ),
                "explanation": "Dependency caching accelerates CI pipeline cycle times."
            }
        ],
        coding_challenge={
            "title": "Simulate CI Quality Gate Evaluator",
            "instructions": "Write a function `evaluate_pipeline_gates(stage_results_dict)` that takes a dict of `{stage_name: exit_code}` (e.g. `{'lint': 0, 'tests': 1, 'security': 0}`). Return `{'status': 'PASSED', 'failed_stages': []}` if all exit codes are 0. If any stage has a non-zero exit code, return `{'status': 'BLOCKED', 'failed_stages': [list_of_names]}`.",
            "starter_code": (
                "def evaluate_pipeline_gates(stages: dict) -> dict:\n"
                "    # Return {'status': ..., 'failed_stages': ...}\n"
                "    pass\n"
            ),
            "solution_code": (
                "def evaluate_pipeline_gates(stages: dict) -> dict:\n"
                "    failed = [k for k, v in stages.items() if v != 0]\n"
                "    if failed:\n"
                "        return {'status': 'BLOCKED', 'failed_stages': failed}\n"
                "    return {'status': 'PASSED', 'failed_stages': []}\n\n"
                "print(evaluate_pipeline_gates({'lint': 0, 'tests': 0, 'security': 0}))\n"
                "print(evaluate_pipeline_gates({'lint': 0, 'tests': 1, 'security': 0}))"
            ),
            "expected_output": "{'status': 'PASSED', 'failed_stages': []}\n{'status': 'BLOCKED', 'failed_stages': ['tests']}"
        },
        quizzes=[
            {
                "question": "What is the primary role of Automated Quality Gates in a CI/CD pipeline?",
                "options": [
                    "To automatically run linters, security scanners, and test suites on every pull request, blocking merging if any check fails",
                    "To charge users a subscription fee",
                    "To encrypt GitHub repositories",
                    "To delete old branches every weekend"
                ],
                "correct_answer": "To automatically run linters, security scanners, and test suites on every pull request, blocking merging if any check fails",
                "explanation": "Quality gates enforce automated test and code health standards prior to merging."
            },
            {
                "question": "What exit code in command-line environments signals to a CI runner that a stage (e.g. pytest) succeeded?",
                "options": [
                    "Exit Code 0",
                    "Exit Code 1",
                    "Exit Code -1",
                    "Exit Code 200"
                ],
                "correct_answer": "Exit Code 0",
                "explanation": "Standard Unix exit code 0 represents success; any non-zero code represents an error."
            },
            {
                "question": "What does a 'Matrix Build' in GitHub Actions accomplish?",
                "options": [
                    "Runs the identical test suite concurrently across combinations of multiple operating systems (Ubuntu, Windows, Mac) and runtime versions",
                    "Generates 3D graphics",
                    "Watches the movie The Matrix",
                    "Compresses files into zip archives"
                ],
                "correct_answer": "Runs the identical test suite concurrently across combinations of multiple operating systems (Ubuntu, Windows, Mac) and runtime versions",
                "explanation": "Matrix strategies parallelize verification across diverse platforms and language versions."
            },
            {
                "question": "How can teams ensure that broken code can never be merged into the `main` branch by accident?",
                "options": [
                    "By enabling GitHub 'Branch Protection Rules' that require status checks to pass before merging",
                    "By asking developers to be careful",
                    "By making the repository private",
                    "By deleting git history"
                ],
                "correct_answer": "By enabling GitHub 'Branch Protection Rules' that require status checks to pass before merging",
                "explanation": "Branch protection locks the merge button until required CI checks report green."
            },
            {
                "question": "What does `--cov-fail-under=80` enforce when running PyTest in a CI pipeline?",
                "options": [
                    "It causes the CI build to fail if test line coverage falls below 80%",
                    "It limits CPU usage to 80%",
                    "It requires 80 unit tests",
                    "It limits runtime to 80 seconds"
                ],
                "correct_answer": "It causes the CI build to fail if test line coverage falls below 80%",
                "explanation": "Coverage enforcement flags fail builds when new code lacks sufficient automated tests."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 60: Capstone Project: The Great Bug Hunt
    # ---------------------------------------------------------
    DayBlueprint(
        order=60,
        title="Day 60: Capstone Project: The Great Bug Hunt (End-to-End Patch & Release)",
        concept="The culminating 60-day capstone project: triaging, diagnosing, fixing, testing, and documenting a multi-tiered full-stack production application riddled with 10 complex real-world bugs.",
        analogy="You are the lead engineering detective brought in to solve a major industrial mystery. The factory is offline, alarms are sounding, and customers are waiting. You calmly put on your detective coat, analyze the evidence, isolate the culprits, replace the damaged machinery, test every circuit, and restore full production power.",
        theory_sections=[
            {
                "heading": "The Capstone Application Scenario",
                "content": (
                    "In this comprehensive capstone project, you receive a full-stack e-commerce banking platform suffering from 10 distinct, interlocking defects across the entire stack:\n"
                    "1. **Syntax / Import Error**: Typo in module import crashing container boot.\n"
                    "2. **Type Coercion Bug**: String addition in currency calculations.\n"
                    "3. **Box Model Layout Overflow**: CSS fixed width breaking mobile viewports.\n"
                    "4. **Missing Index**: 5-second database freeze on checkout queries.\n"
                    "5. **Check-Then-Act Race Condition**: Concurrent double-spending on user balances.\n"
                    "6. **Connection Pool Leak**: Database connections not released in exception handling.\n"
                    "7. **Unbounded Memory Leak**: Global audit dictionary growing to gigabytes without eviction.\n"
                    "8. **Missing Error Standard**: 500 crashes instead of clean RFC 7807 4xx responses.\n"
                    "9. **Unused / Flaky Selectors in E2E**: Brittle CSS selectors failing automated tests.\n"
                    "10. **Missing CI Pipeline Quality Gate**: Broken code merging straight to main."
                )
            },
            {
                "heading": "The 5-Phase Master Resolution Playbook",
                "content": (
                    "1. **Triage & Reproduce**: Write automated reproduction scripts that trigger each of the 10 bugs.\n"
                    "2. **Trace & Isolate**: Use IDE debuggers, call stack inspections, EXPLAIN queries, and memory profilers.\n"
                    "3. **Refactor & Defend**: Apply defensive programming, mutex locks, context managers, and bounded caches.\n"
                    "4. **Automate Testing**: Write unit tests (AAA), integration tests, and E2E journeys.\n"
                    "5. **Document & Deliver**: Author a comprehensive blameless Post-Mortem and RCA report."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Capstone Bug 1 & 2: Safe Currency Engine Fix",
                "language": "python",
                "code": (
                    "from decimal import Decimal, InvalidOperation\n\n"
                    "# Fixed: Strict decimal parsing eliminating float/string coercion bugs\n"
                    "def parse_money(raw_value) -> Decimal:\n"
                    "    try:\n"
                    "        clean_str = str(raw_value).strip().replace('$', '')\n"
                    "        val = Decimal(clean_str)\n"
                    "        if val < 0:\n"
                    "            raise ValueError('Negative currency illegal')\n"
                    "        return val.quantize(Decimal('0.01'))\n"
                    "    except (InvalidOperation, ValueError) as err:\n"
                    "        raise ValueError(f'Invalid currency format: {raw_value!r}') from err"
                ),
                "explanation": "Decimal arithmetic eliminates floating point rounding errors and string concatenation bugs."
            },
            {
                "title": "Capstone Bug 3 & 4: Thread-Safe Account with Mutex",
                "language": "python",
                "code": (
                    "import threading\n\n"
                    "class Account:\n"
                    "    def __init__(self, account_id: str, initial_balance: Decimal):\n"
                    "        self.id = account_id\n"
                    "        self.balance = initial_balance\n"
                    "        self.lock = threading.Lock()\n\n"
                    "    def debit(self, amount: Decimal) -> bool:\n"
                    "        with self.lock:\n"
                    "            if self.balance >= amount:\n"
                    "                self.balance -= amount\n"
                    "                return True\n"
                    "            return False"
                ),
                "explanation": "Synchronizes account mutation with a mutex lock to defeat double-spend race conditions."
            },
            {
                "title": "Capstone Bug 5 & 6: Bounded LRU Cache Preventing Memory Leaks",
                "language": "python",
                "code": (
                    "from collections import OrderedDict\n\n"
                    "class BoundedAuditLog:\n"
                    "    def __init__(self, max_records=5000):\n"
                    "        self.max = max_records\n"
                    "        self.store = OrderedDict()\n\n"
                    "    def log(self, event_id: str, data: dict):\n"
                    "        if len(self.store) >= self.max:\n"
                    "            self.store.popitem(last=False) # Evict oldest record\n"
                    "        self.store[event_id] = data"
                ),
                "explanation": "Caps memory capacity, permanently neutralizing memory leak crashes."
            },
            {
                "title": "Capstone Test Suite & Verification Harness",
                "language": "python",
                "code": (
                    "def test_capstone_resolution():\n"
                    "    # 1. Verify currency engine\n"
                    "    assert parse_money('$100.50') == Decimal('100.50')\n"
                    "    \n"
                    "    # 2. Verify race condition prevention\n"
                    "    acc = Account('A1', Decimal('100.00'))\n"
                    "    threads = [threading.Thread(target=acc.debit, args=(Decimal('100.00'),)) for _ in range(2)]\n"
                    "    for t in threads: t.start()\n"
                    "    for t in threads: t.join()\n"
                    "    assert acc.balance == Decimal('0.00') # Exactly 1 debit succeeded!\n"
                    "    \n"
                    "    print('🏆 CAPSTONE PROJECT VALIDATION COMPLETE: ALL 10 DEFECTS RESOLVED!')\n\n"
                    "test_capstone_resolution()"
                ),
                "explanation": "Final integration test verifying the complete system operates reliably under stress."
            }
        ],
        coding_challenge={
            "title": "Capstone Verification: The Master Diagnostic Audit",
            "instructions": "Write a master audit function `capstone_audit(system_checks_dict)` that takes a dict of 10 boolean check flags `{'syntax_ok': True, 'race_condition_fixed': True, ...}`. Return `'CERTIFIED_PRODUCTION_READY'` if all 10 checks evaluate to True. If any check is False, return `'FAILED_AUDIT: <first_failed_key>'`.",
            "starter_code": (
                "def capstone_audit(checks: dict) -> str:\n"
                "    # Return certification status\n"
                "    pass\n"
            ),
            "solution_code": (
                "def capstone_audit(checks: dict) -> str:\n"
                "    for k, v in checks.items():\n"
                "        if not v:\n"
                "            return f'FAILED_AUDIT: {k}'\n"
                "    return 'CERTIFIED_PRODUCTION_READY'\n\n"
                "healthy_system = {f'check_{i}': True for i in range(1, 11)}\n"
                "print(capstone_audit(healthy_system))"
            ),
            "expected_output": "CERTIFIED_PRODUCTION_READY"
        },
        quizzes=[
            {
                "question": "What is the primary philosophical lesson of the complete 60-Day Debugging & Problem Solving course?",
                "options": [
                    "Debugging is not random guessing; it is the scientific method applied to software through observation, hypothesis, isolated testing, root cause resolution, and regression prevention",
                    "Debugging means restarting the computer until it works",
                    "Programming languages without bugs will be released soon",
                    "Only senior staff should debug code"
                ],
                "correct_answer": "Debugging is not random guessing; it is the scientific method applied to software through observation, hypothesis, isolated testing, root cause resolution, and regression prevention",
                "explanation": "Effective debugging is a systematic, evidence-based scientific methodology."
            },
            {
                "question": "Which of the following describes the complete end-to-end bug resolution workflow?",
                "options": [
                    "Reproduce -> Isolate with Debugger -> Identify Root Cause -> Fix & Refactor -> Write Automated Tests -> Document Post-Mortem",
                    "Guess -> Edit random lines -> Push to production",
                    "Delete the repository -> Re-clone",
                    "Ignore the error log -> Close the ticket"
                ],
                "correct_answer": "Reproduce -> Isolate with Debugger -> Identify Root Cause -> Fix & Refactor -> Write Automated Tests -> Document Post-Mortem",
                "explanation": "Professional engineers follow systematic reproduction, root cause fixes, test automation, and documentation."
            },
            {
                "question": "How do Mutex locks and atomic SQL updates eliminate double-spending race conditions in financial software?",
                "options": [
                    "They guarantee that checking balance and debiting funds occur as an atomic, serialized unit without interruption by competing threads",
                    "They convert real money into cryptocurrency",
                    "They encrypt the customer's phone number",
                    "They disable all withdrawals"
                ],
                "correct_answer": "They guarantee that checking balance and debiting funds occur as an atomic, serialized unit without interruption by competing threads",
                "explanation": "Atomicity and mutual exclusion ensure state changes occur sequentially without concurrency interleaving."
            },
            {
                "question": "Why is an automated CI/CD pipeline considered the ultimate automated bug prevention tool?",
                "options": [
                    "It acts as an impartial quality gate, refusing to merge code if linters, security scanners, or unit tests fail",
                    "It automatically writes all features",
                    "It eliminates the need for human developers",
                    "It makes code run on mobile phones"
                ],
                "correct_answer": "It acts as an impartial quality gate, refusing to merge code if linters, security scanners, or unit tests fail",
                "explanation": "Automated pipelines objectively enforce verification criteria on every proposed change."
            },
            {
                "question": "What is the true measure of a senior software engineer when resolving production outages?",
                "options": [
                    "Emotional composure, rigorous logical deduction, treating root causes rather than symptoms, and fostering a blameless culture of continuous learning",
                    "Typing 120 words per minute",
                    "Blaming other engineers loudly on Slack",
                    "Never asking for help"
                ],
                "correct_answer": "Emotional composure, rigorous logical deduction, treating root causes rather than symptoms, and fostering a blameless culture of continuous learning",
                "explanation": "Senior engineering maturity combines technical discipline, root-cause focus, and supportive team collaboration."
            }
        ]
    )
]
