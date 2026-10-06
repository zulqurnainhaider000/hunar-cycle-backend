"""
debugging_curriculum_days_16_30.py
Days 16 to 30 for Debugging & Problem Solving 60-Day Course.
Covers:
- Module 3 (cont): Custom Exceptions, Defensive Programming, Day 18 Project (Fail-Safe Input Processor)
- Module 4: Using IDE Debugger Tools (Days 19-25) - Breakpoints, Stepping, Watches, Expression Evaluation, Call Stack
- Module 5: Web & Frontend Browser DevTools (Days 26-30) - Elements, Console, DOM/CSS, Network, Application Storage
"""

from seeder.course_blueprint import DayBlueprint

DAYS_16_TO_30 = [
    # ---------------------------------------------------------
    # Day 16: Throwing / Raising Custom Exceptions
    # ---------------------------------------------------------
    DayBlueprint(
        order=16,
        title="Day 16: Throwing / Raising Custom Exceptions",
        concept="Custom exceptions subclass standard error hierarchies to model domain-specific failure states (e.g., InsufficientBalanceError, InvalidTokenError), giving callers clear error taxonomy and actionable remediation.",
        analogy="If you go to a medical clinic, you don't want a generic stamp that says 'SICK'. You want a specific medical diagnosis: 'Sprained Left Ankle' or 'Seasonal Flu'. Custom exceptions give your software distinct, unambiguous diagnoses so other systems know whether to prescribe an ice pack or antibiotics.",
        theory_sections=[
            {
                "heading": "Why Standard Built-in Exceptions Are Not Enough",
                "content": (
                    "While `ValueError` and `KeyError` work for low-level operations, they are too generic for business logic. If a banking payment function raises `ValueError('Insufficient funds')`, a caller catching `ValueError` might catch a string conversion bug instead of an account balance issue.\n\n"
                    "Creating **Custom Domain Exceptions** (`class InsufficientFundsError(Exception): pass`) allows callers to catch the exact domain failure cleanly without collateral damage."
                )
            },
            {
                "heading": "Designing Clean Exception Hierarchies",
                "content": (
                    "Best practice in enterprise systems is to define a base exception for your library or module, then subclass specific variants:\n"
                    "- `class AppError(Exception): pass` (Top-level base)\n"
                    "  - `class AuthenticationError(AppError): pass`\n"
                    "    - `class TokenExpiredError(AuthenticationError): pass`\n"
                    "    - `class InvalidCredentialsError(AuthenticationError): pass`\n"
                    "  - `class PaymentError(AppError): pass`\n"
                    "Callers can catch `TokenExpiredError` to prompt a refresh token, or catch `AppError` to catch any error originating from your package."
                )
            },
            {
                "heading": "Attaching Context to Custom Exceptions",
                "content": (
                    "Custom exceptions should carry structured debugging metadata, such as user IDs, remaining limits, or error codes, directly in instance attributes rather than forcing callers to parse strings."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Defining Structured Custom Exceptions",
                "language": "python",
                "code": (
                    "class PaymentGatewayError(Exception):\n"
                    "    '''Base exception for payment operations.'''\n"
                    "    pass\n\n"
                    "class InsufficientFundsError(PaymentGatewayError):\n"
                    "    def __init__(self, account_id: str, balance: float, required: float):\n"
                    "        self.account_id = account_id\n"
                    "        self.balance = balance\n"
                    "        self.required = required\n"
                    "        super().__init__(\n"
                    "            f'Account {account_id} has ${balance:.2f}, but ${required:.2f} is required.'\n"
                    "        )"
                ),
                "explanation": "Custom exception encapsulates rich domain state directly on instance variables."
            },
            {
                "title": "Raising and Catching Custom Domain Exceptions",
                "language": "python",
                "code": (
                    "def debit_account(account_id: str, current_balance: float, amount: float):\n"
                    "    if amount > current_balance:\n"
                    "        raise InsufficientFundsError(account_id, current_balance, amount)\n"
                    "    return current_balance - amount\n\n"
                    "try:\n"
                    "    debit_account('acc_101', 50.0, 120.0)\n"
                    "except InsufficientFundsError as err:\n"
                    "    print(f'Payment Declined! Short by ${err.required - err.balance:.2f}')"
                ),
                "explanation": "Caller accesses `err.required` and `err.balance` directly without fragile regex string parsing."
            },
            {
                "title": "Exception Chaining with `raise ... from` in Python",
                "language": "python",
                "code": (
                    "import json\n\n"
                    "class ConfigurationLoadError(Exception): pass\n\n"
                    "def load_system_config(filepath):\n"
                    "    try:\n"
                    "        with open(filepath) as f:\n"
                    "            return json.load(f)\n"
                    "    except (FileNotFoundError, json.JSONDecodeError) as cause:\n"
                    "        # Preserve original causal traceback using 'from cause'\n"
                    "        raise ConfigurationLoadError(f'Failed to load config: {filepath}') from cause"
                ),
                "explanation": "`raise ... from cause` chains the original low-level exception, preserving the root diagnostic trail."
            },
            {
                "title": "Custom Exceptions in JavaScript / TypeScript",
                "language": "javascript",
                "code": (
                    "class ValidationError extends Error {\n"
                    "  constructor(message, field) {\n"
                    "    super(message);\n"
                    "    this.name = 'ValidationError';\n"
                    "    this.field = field;\n"
                    "  }\n"
                    "}\n\n"
                    "function validateEmail(email) {\n"
                    "  if (!email.includes('@')) {\n"
                    "    throw new ValidationError('Invalid email syntax', 'email');\n"
                    "  }\n"
                    "}"
                ),
                "explanation": "Extends built-in `Error` class and overrides `this.name` for standard error tracking."
            }
        ],
        coding_challenge={
            "title": "Build a Custom RateLimitExceeded Exception",
            "instructions": "Create a custom exception `RateLimitExceeded(limit, retry_after_seconds)` that inherits from `Exception`. Write a function `check_rate_limit(requests_made, max_limit)` that raises `RateLimitExceeded(max_limit, 60)` if `requests_made >= max_limit`, otherwise returns True.",
            "starter_code": (
                "# Define RateLimitExceeded and check_rate_limit\n"
                "class RateLimitExceeded(Exception):\n"
                "    pass\n\n"
                "def check_rate_limit(requests_made: int, max_limit: int) -> bool:\n"
                "    pass\n"
            ),
            "solution_code": (
                "class RateLimitExceeded(Exception):\n"
                "    def __init__(self, limit: int, retry_after: int):\n"
                "        self.limit = limit\n"
                "        self.retry_after = retry_after\n"
                "        super().__init__(f'Rate limit of {limit} requests exceeded. Retry after {retry_after}s.')\n\n"
                "def check_rate_limit(requests_made: int, max_limit: int) -> bool:\n"
                "    if requests_made >= max_limit:\n"
                "        raise RateLimitExceeded(max_limit, 60)\n"
                "    return True\n\n"
                "try:\n"
                "    check_rate_limit(10, 10)\n"
                "except RateLimitExceeded as e:\n"
                "    print(f'Caught: limit={e.limit}, retry={e.retry_after}')"
            ),
            "expected_output": "Caught: limit=10, retry=60"
        },
        quizzes=[
            {
                "question": "What is the primary advantage of defining custom exception classes over reusing generic `ValueError` or `Exception`?",
                "options": [
                    "They provide unambiguous, domain-specific categorization and can carry structured metadata without fragile string parsing",
                    "They execute twice as fast as built-in exceptions",
                    "They do not consume computer RAM",
                    "They prevent code from needing tests"
                ],
                "correct_answer": "They provide unambiguous, domain-specific categorization and can carry structured metadata without fragile string parsing",
                "explanation": "Custom exceptions allow callers to catch explicit failure modes and access structured context cleanly."
            },
            {
                "question": "What class should all custom user-defined exceptions inherit from in Python?",
                "options": [
                    "`Exception` (or a subclass of `Exception`)",
                    "`BaseException` directly",
                    "`object`",
                    "`dict`"
                ],
                "correct_answer": "`Exception` (or a subclass of `Exception`)",
                "explanation": "User exceptions must subclass `Exception`. Subclassing `BaseException` bypasses standard `except Exception:` catches."
            },
            {
                "question": "In Python, what is the purpose of the syntax `raise NewError() from original_error`?",
                "options": [
                    "Exception Chaining: It explicitly connects the new high-level error to the underlying cause in the traceback",
                    "It ignores the original error completely",
                    "It writes the error into a database table",
                    "It converts the error into an HTTP 200 response"
                ],
                "correct_answer": "Exception Chaining: It explicitly connects the new high-level error to the underlying cause in the traceback",
                "explanation": "Chaining preserves the original causal exception in the `__cause__` attribute for diagnostic clarity."
            },
            {
                "question": "Why is it best practice to create a base exception class for a package (e.g. `class StripeError(Exception): pass`)?",
                "options": [
                    "Callers can write a single `except StripeError:` block to catch any error originating from that package",
                    "It is legally required by software licenses",
                    "It allows Python to run in browser windows",
                    "It automatically fixes broken API calls"
                ],
                "correct_answer": "Callers can write a single `except StripeError:` block to catch any error originating from that package",
                "explanation": "Package-level base exceptions provide a clean abstraction boundary for client error handling."
            },
            {
                "question": "What is an antipattern when instantiating custom exceptions?",
                "options": [
                    "Embedding complex unstructured data in the error message string and forcing callers to parse it with regex",
                    "Providing custom attributes on the exception object",
                    "Calling `super().__init__(message)`",
                    "Subclassing from `Exception`"
                ],
                "correct_answer": "Embedding complex unstructured data in the error message string and forcing callers to parse it with regex",
                "explanation": "Callers should access attributes directly (`err.status_code`) rather than parsing error message strings."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 17: Failsafe & Defensive Programming
    # ---------------------------------------------------------
    DayBlueprint(
        order=17,
        title="Day 17: Failsafe & Defensive Programming",
        concept="Defensive programming designs software under the assumption of Murphy's Law: anything that can go wrong will go wrong. It validates inputs, uses immutable structures, and provides graceful fallbacks.",
        analogy="Defensive driving means you don't just follow traffic rules; you assume other drivers might run red lights, swerve without signaling, or slam their brakes. Defensive programming means you assume external APIs will timeout, users will enter emojis into age fields, and disks will fill to 100%.",
        theory_sections=[
            {
                "heading": "Core Tenets of Defensive Programming",
                "content": (
                    "1. **Never Trust External Input**: Treat all data from users, query params, headers, files, and third-party APIs as untrusted and potentially malicious.\n"
                    "2. **Validate at the Perimeter**: Check types, ranges, lengths, and formats as soon as data enters your system, before passing it to core logic.\n"
                    "3. **Fail Fast and Loud in Development, Gracefully in Production**: In development, throw loud assertions immediately. In production, fail safely without crashing the entire system."
                )
            },
            {
                "heading": "Safe Navigation and Graceful Degradation",
                "content": (
                    "Instead of directly indexing dictionaries or nested structures:\n"
                    "- Use `.get(key, default)` in Python.\n"
                    "- Use Optional Chaining (`?.`) and Nullish Coalescing (`??`) in JavaScript.\n"
                    "- Provide **circuit breaker fallbacks**: If the recommendation engine is down, render a static top-10 list instead of a 500 Internal Server Error page."
                )
            },
            {
                "heading": "Guarding Against State Mutations",
                "content": (
                    "A frequent cause of hard-to-trace bugs is passing mutable objects (lists, dictionaries) into functions that unexpectedly modify them in-place. Defensive code creates shallow or deep copies before mutation, or uses frozen/immutable data structures (`NamedTuple`, `dataclass(frozen=True)`)."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Fragile vs Defensive Dictionary Access",
                "language": "python",
                "code": (
                    "# FRAGILE: Crashes with KeyError if 'address' or 'city' is missing\n"
                    "def get_city_fragile(user):\n"
                    "    return user['address']['city']\n\n"
                    "# DEFENSIVE: Uses get() with default fallbacks\n"
                    "def get_city_defensive(user: dict) -> str:\n"
                    "    if not isinstance(user, dict):\n"
                    "        return 'Unknown'\n"
                    "    address = user.get('address')\n"
                    "    if isinstance(address, dict):\n"
                    "        return address.get('city', 'Unknown')\n"
                    "    return 'Unknown'"
                ),
                "explanation": "Guards against missing keys and unexpected data shapes at each hierarchical level."
            },
            {
                "title": "Defensive Copying of Mutable Default Arguments",
                "language": "python",
                "code": (
                    "# THE CLASSIC PYTHON TRAP: Mutable default list accumulates state across calls!\n"
                    "def add_tag_buggy(tag, tags=[]):\n"
                    "    tags.append(tag)\n"
                    "    return tags\n\n"
                    "# DEFENSIVE FIX: Use None as default and instantiate internally\n"
                    "def add_tag_defensive(tag: str, tags: list[str] = None) -> list[str]:\n"
                    "    if tags is None:\n"
                    "        tags = []\n"
                    "    else:\n"
                    "        tags = tags.copy() # Defensively copy to avoid mutating caller list\n"
                    "    tags.append(tag)\n"
                    "    return tags"
                ),
                "explanation": "Eliminates persistent state contamination caused by Python's mutable default arguments."
            },
            {
                "title": "Defensive Immutability with Frozen Dataclasses",
                "language": "python",
                "code": (
                    "from dataclasses import dataclass\n\n"
                    "@dataclass(frozen=True)\n"
                    "class AppConfig:\n"
                    "    api_key: str\n"
                    "    timeout_seconds: int = 30\n\n"
                    "config = AppConfig(api_key='secret_123')\n"
                    "# config.timeout_seconds = 100 -> FrozenInstanceError: cannot assign to field!"
                ),
                "explanation": "`frozen=True` ensures critical system configurations cannot be mutated at runtime."
            },
            {
                "title": "Graceful Fallback on External API Failure",
                "language": "python",
                "code": (
                    "import requests\n\n"
                    "def get_currency_rate(base: str, target: str) -> float:\n"
                    "    FALLBACK_RATES = {'USD_EUR': 0.92, 'USD_GBP': 0.79}\n"
                    "    try:\n"
                    "        res = requests.get(f'https://rates.internal/{base}/{target}', timeout=1.5)\n"
                    "        if res.status_code == 200:\n"
                    "            return res.json()['rate']\n"
                    "    except (requests.RequestException, KeyError):\n"
                    "        pass # Log warning in production\n\n"
                    "    # Graceful degradation fallback\n"
                    "    return FALLBACK_RATES.get(f'{base}_{target}', 1.0)"
                ),
                "explanation": "Guarantees continuous user service even when an external microservice experiences downtime."
            }
        ],
        coding_challenge={
            "title": "Implement Defensive Deep Key Getter",
            "instructions": "Write a function `safe_nested_get(dictionary, path_list, default=None)` that takes a nested dictionary and a list of key strings, safely navigating through the path. If any key along the path does not exist or intermediate value is not a dict, return `default`.",
            "starter_code": (
                "def safe_nested_get(d: dict, path: list, default=None):\n"
                "    # Return nested value or default safely\n"
                "    pass\n"
            ),
            "solution_code": (
                "def safe_nested_get(d: dict, path: list, default=None):\n"
                "    curr = d\n"
                "    for key in path:\n"
                "        if not isinstance(curr, dict) or key not in curr:\n"
                "            return default\n"
                "        curr = curr[key]\n"
                "    return curr\n\n"
                "data = {'user': {'profile': {'age': 28}}}\n"
                "print(safe_nested_get(data, ['user', 'profile', 'age']))\n"
                "print(safe_nested_get(data, ['user', 'settings', 'theme'], 'dark'))"
            ),
            "expected_output": "28\ndark"
        },
        quizzes=[
            {
                "question": "What is the primary philosophy of Defensive Programming?",
                "options": [
                    "Writing code under the assumption that external inputs will be invalid and dependencies will fail, ensuring graceful recovery",
                    "Refusing to share code with other team members",
                    "Encrypting all Python source files",
                    "Writing unit tests only after production crashes"
                ],
                "correct_answer": "Writing code under the assumption that external inputs will be invalid and dependencies will fail, ensuring graceful recovery",
                "explanation": "Defensive programming protects applications against Murphy's Law and hostile/unexpected data."
            },
            {
                "question": "What bug occurs when you define a Python function with `def append_item(x, target_list=[])`?",
                "options": [
                    "The list is created only once when the function is defined, causing items to accumulate across all subsequent function calls",
                    "A SyntaxError is raised on definition",
                    "The function cannot accept arguments",
                    "The list is automatically sorted"
                ],
                "correct_answer": "The list is created only once when the function is defined, causing items to accumulate across all subsequent function calls",
                "explanation": "Mutable default arguments are evaluated once at function definition, creating shared mutable state."
            },
            {
                "question": "What does 'Graceful Degradation' mean in system resilience?",
                "options": [
                    "When a secondary subsystem fails, the application continues functioning with reduced non-critical capabilities rather than crashing completely",
                    "Slowly deleting database tables when disk space is low",
                    "Turning off the server monitor during peak traffic",
                    "Downgrading all user passwords to plain text"
                ],
                "correct_answer": "When a secondary subsystem fails, the application continues functioning with reduced non-critical capabilities rather than crashing completely",
                "explanation": "Graceful degradation ensures critical user paths remain operational during partial outages."
            },
            {
                "question": "Why is `dict.get('key', default_val)` safer than direct indexing `dict['key']`?",
                "options": [
                    "It returns the default value instead of crashing with a `KeyError` if the key is missing",
                    "It prevents SQL injection",
                    "It runs 10x faster in hardware",
                    "It encrypts the key"
                ],
                "correct_answer": "It returns the default value instead of crashing with a `KeyError` if the key is missing",
                "explanation": "`.get()` handles missing keys safely without requiring an explicit try/except block."
            },
            {
                "question": "What is the purpose of passing `frozen=True` to Python dataclasses?",
                "options": [
                    "It makes instances immutable, preventing any runtime modification of fields after initialization",
                    "It saves the object to a cold storage glacier disk",
                    "It prevents the object from being printed",
                    "It disables garbage collection"
                ],
                "correct_answer": "It makes instances immutable, preventing any runtime modification of fields after initialization",
                "explanation": "Frozen dataclasses throw an error on attribute reassignment, preventing unintended side effects."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 18: Project: Building a Fail-Safe Input Processor System
    # ---------------------------------------------------------
    DayBlueprint(
        order=18,
        title="Day 18: Project: Building a Fail-Safe Input Processor System",
        concept="Synthesizes Modules 1-3 into a production-grade input validation and sanitation engine that parses untrusted batch records, sanitizes data, captures structured errors, and outputs clean analytics.",
        analogy="Think of a modern airport baggage screening system. Bags arrive from all over the world with dirt, stickers, or broken zippers. The automated scanner doesn't shut down the entire airport when it finds an oversized bottle of shampoo; it diverts the single bad bag to an inspection lane while hundreds of valid bags continue smoothly to their flights.",
        theory_sections=[
            {
                "heading": "Architectural Design of a Batch Processor",
                "content": (
                    "In real-world data pipelines (ETL, CSV imports, webhook ingestions), receiving 10,000 records where 3 are corrupt should **never crash the entire batch**.\n\n"
                    "The **Fail-Safe Processing Pattern** consists of:\n"
                    "1. **Isolation Boundary**: Each record is processed inside an isolated transaction/try-block.\n"
                    "2. **Dual-Bucket Output**: Valid items are sent to `success_records`; invalid items are sent to `quarantine_records` with exact error diagnostics.\n"
                    "3. **Telemetry & Metrics**: Reports total processed, success percentage, and aggregated error frequencies."
                )
            },
            {
                "heading": "Sanitization vs Validation",
                "content": (
                    "- **Sanitization**: Cleaning input without failing (e.g. trimming whitespace, lowercasing emails, converting string `'100'` to integer `100`).\n"
                    "- **Validation**: Rejecting records that fail immutable business rules (e.g. negative prices, invalid email syntax, missing primary keys).\n"
                    "Always sanitize first, then validate."
                )
            },
            {
                "heading": "Milestone Project Requirements",
                "content": (
                    "In this milestone project, we implement `BatchInputProcessor` with custom exceptions, defensive typing, field sanitization, and structured audit logs."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Custom Exceptions for the Processor Pipeline",
                "language": "python",
                "code": (
                    "class BatchProcessingError(Exception): pass\n"
                    "class MissingFieldError(BatchProcessingError): pass\n"
                    "class InvalidDataFormatError(BatchProcessingError): pass\n"
                    "class BusinessRuleViolationError(BatchProcessingError): pass"
                ),
                "explanation": "Defines explicit domain taxonomy for classification of batch ingestion failures."
            },
            {
                "title": "Record Sanitizer and Validator Implementation",
                "language": "python",
                "code": (
                    "def sanitize_and_validate_user(raw: dict) -> dict:\n"
                    "    if not isinstance(raw, dict):\n"
                    "        raise InvalidDataFormatError('Record must be a dictionary')\n\n"
                    "    # 1. Check required fields\n"
                    "    for req in ['id', 'email', 'score']:\n"
                    "        if req not in raw:\n"
                    "            raise MissingFieldError(f'Missing required field: {req}')\n\n"
                    "    # 2. Sanitize and validate email\n"
                    "    email = str(raw['email']).strip().lower()\n"
                    "    if '@' not in email or '.' not in email:\n"
                    "        raise BusinessRuleViolationError(f'Invalid email format: {email}')\n\n"
                    "    # 3. Sanitize and validate numeric score\n"
                    "    try:\n"
                    "        score = float(raw['score'])\n"
                    "    except (ValueError, TypeError):\n"
                    "        raise InvalidDataFormatError(f'Score must be numeric, got: {raw[\"score\"]!r}')\n\n"
                    "    if not (0 <= score <= 100):\n"
                    "        raise BusinessRuleViolationError(f'Score {score} out of bounds (0-100)')\n\n"
                    "    return {'id': raw['id'], 'email': email, 'score': score}"
                ),
                "explanation": "Executes multi-step sanitization followed by strict business rule enforcement."
            },
            {
                "title": "Dual-Bucket Batch Processing Engine",
                "language": "python",
                "code": (
                    "def process_batch(records: list) -> dict:\n"
                    "    valid = []\n"
                    "    quarantined = []\n\n"
                    "    for idx, item in enumerate(records):\n"
                    "        try:\n"
                    "            cleaned = sanitize_and_validate_user(item)\n"
                    "            valid.append(cleaned)\n"
                    "        except BatchProcessingError as err:\n"
                    "            quarantined.append({\n"
                    "                'index': idx,\n"
                    "                'raw_record': item,\n"
                    "                'error_type': type(err).__name__,\n"
                    "                'reason': str(err)\n"
                    "            })\n\n"
                    "    return {\n"
                    "        'total_processed': len(records),\n"
                    "        'success_count': len(valid),\n"
                    "        'failed_count': len(quarantined),\n"
                    "        'valid_records': valid,\n"
                    "        'quarantined_records': quarantined\n"
                    "    }"
                ),
                "explanation": "Isolates exceptions so bad records are quarantined while valid records succeed."
            },
            {
                "title": "Executing Batch with Broken Inputs",
                "language": "python",
                "code": (
                    "raw_batch = [\n"
                    "    {'id': 1, 'email': ' Alice@Work.com ', 'score': '95.5'}, # Valid (needs sanitizing)\n"
                    "    {'id': 2, 'score': 80},                                   # Missing email\n"
                    "    {'id': 3, 'email': 'bad_email', 'score': 50},            # Invalid email\n"
                    "    {'id': 4, 'email': 'carol@test.io', 'score': 150}         # Out of bounds score\n"
                    "]\n"
                    "results = process_batch(raw_batch)\n"
                    "print(f'Success: {results[\"success_count\"]}, Failed: {results[\"failed_count\"]}')"
                ),
                "explanation": "Demonstrates resilient processing handling mixed valid and corrupt data."
            }
        ],
        coding_challenge={
            "title": "Build Batch Summary Reporter",
            "instructions": "Write a function `generate_batch_report(processor_results)` that takes the dictionary output from `process_batch` and returns a summary string: `'PROCESSED: X | VALID: Y (Z%) | ERRORS: [ErrorType1: N, ...]'` sorted alphabetically by error type.",
            "starter_code": (
                "def generate_batch_report(results: dict) -> str:\n"
                "    # Return formatted batch summary string\n"
                "    pass\n"
            ),
            "solution_code": (
                "def generate_batch_report(results: dict) -> str:\n"
                "    total = results['total_processed']\n"
                "    valid = results['success_count']\n"
                "    pct = round((valid / total * 100), 1) if total > 0 else 0.0\n"
                "    counts = {}\n"
                "    for q in results['quarantined_records']:\n"
                "        t = q['error_type']\n"
                "        counts[t] = counts.get(t, 0) + 1\n"
                "    err_parts = [f'{k}: {counts[k]}' for k in sorted(counts.keys())]\n"
                "    return f'PROCESSED: {total} | VALID: {valid} ({pct}%) | ERRORS: [{err_parts[0] if err_parts else \"\"}]'\n\n"
                "sample = {\n"
                "    'total_processed': 4,\n"
                "    'success_count': 3,\n"
                "    'quarantined_records': [{'error_type': 'MissingFieldError'}]\n"
                "}\n"
                "print(generate_batch_report(sample))"
            ),
            "expected_output": "PROCESSED: 4 | VALID: 3 (75.0%) | ERRORS: [MissingFieldError: 1]"
        },
        quizzes=[
            {
                "question": "What is the primary architectural goal of a 'Fail-Safe Batch Processor'?",
                "options": [
                    "To process valid records successfully while routing corrupt records to a quarantine bucket without halting the entire pipeline",
                    "To automatically delete any database containing errors",
                    "To convert all invalid data into random numbers",
                    "To double the processing speed by disabling validation"
                ],
                "correct_answer": "To process valid records successfully while routing corrupt records to a quarantine bucket without halting the entire pipeline",
                "explanation": "Dual-bucket quarantine architectures guarantee that isolated record flaws do not derail entire operations."
            },
            {
                "question": "What is the difference between Sanitization and Validation?",
                "options": [
                    "Sanitization cleans and normalizes data (e.g. trimming spaces); Validation verifies business rules and rejects invalid records",
                    "Sanitization is for SQL; Validation is for CSS",
                    "Validation must always happen before Sanitization",
                    "They are identical terms"
                ],
                "correct_answer": "Sanitization cleans and normalizes data (e.g. trimming spaces); Validation verifies business rules and rejects invalid records",
                "explanation": "Sanitizing first allows harmless issues (e.g. extra whitespace) to be cleaned before validation rules run."
            },
            {
                "question": "What information should be recorded for each entry in the `quarantined_records` bucket?",
                "options": [
                    "The raw record, the index/identifier, the specific error type, and the explanatory failure message",
                    "The user's credit card number and password",
                    "A random timestamp only",
                    "The entire operating system memory dump"
                ],
                "correct_answer": "The raw record, the index/identifier, the specific error type, and the explanatory failure message",
                "explanation": "Recording the original input and exact error allows operators to inspect and remediate failures."
            },
            {
                "question": "Why is handling exceptions per-record inside a loop safer than wrapping the entire `for` loop in one `try` block?",
                "options": [
                    "Wrapping inside the loop ensures an error on record 3 does not abort processing for records 4 through 1,000",
                    "Wrapping inside the loop reduces file size",
                    "Wrapping outside the loop is forbidden by Python syntax",
                    "Python cannot run `for` loops without internal `try` blocks"
                ],
                "correct_answer": "Wrapping inside the loop ensures an error on record 3 does not abort processing for records 4 through 1,000",
                "explanation": "A single external try block terminates the loop on the first failure, losing all subsequent records."
            },
            {
                "question": "What HTTP status code should an API return when receiving a batch request where some items succeeded and others were quarantined?",
                "options": [
                    "207 Multi-Status (RFC 4918) or 200 OK with a detailed summary payload",
                    "500 Internal Server Error",
                    "301 Moved Permanently",
                    "404 Not Found"
                ],
                "correct_answer": "207 Multi-Status (RFC 4918) or 200 OK with a detailed summary payload",
                "explanation": "RFC 4918 defines 207 Multi-Status specifically for batch operations containing individual sub-statuses."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 19: Intro to Visual Debuggers (VS Code & PyCharm)
    # ---------------------------------------------------------
    DayBlueprint(
        order=19,
        title="Day 19: Intro to Visual Debuggers (VS Code & PyCharm)",
        concept="Visual debuggers provide an interactive control plane that pauses live program execution, allowing developers to inspect memory variables, examine call stacks, and step through code instruction-by-instruction.",
        analogy="If print debugging is taking blurry polaroid photos of a racecar as it speeds past at 200 MPH, a visual debugger is pressing a freeze-ray button that suspends the racecar mid-air, letting you pop the hood, measure piston temperatures, and rotate the wheels by hand.",
        theory_sections=[
            {
                "heading": "The Power of the Modern Visual Debugger",
                "content": (
                    "While print statements require you to modify code, re-run, inspect stdout, add more prints, and re-run again, a **Visual Debugger** connects directly to the runtime engine (Python's `pdb` / `debugpy`, Node's V8 inspector, or JVM debugging):\n"
                    "- Freeze code execution at any designated line (**Breakpoint**).\n"
                    "- Inspect all variables in local, closure, and global scopes without writing a single `print`.\n"
                    "- Dynamically change variable values in memory while the program is paused."
                )
            },
            {
                "heading": "The 4 Core Panels of an IDE Debugger",
                "content": (
                    "When an IDE hits a breakpoint, the debugging interface opens 4 synchronized views:\n"
                    "1. **Variables / Scope View**: Shows all active variables (Locals, Globals) and their values.\n"
                    "2. **Watch Window**: Allows pinning specific expressions (e.g. `len(cart.items)`) to watch them evaluate in real time.\n"
                    "3. **Call Stack**: Displays the active stack frames from `main` to current paused line.\n"
                    "4. **Debug Console / REPL**: An interactive command line running inside the live memory context of the paused program."
                )
            },
            {
                "heading": "Configuring VS Code `launch.json`",
                "content": (
                    "VS Code stores debugging configurations inside `.vscode/launch.json`. Configurations specify:\n"
                    "- `type`: Runtime type (`debugpy`, `node`, `chrome`).\n"
                    "- `request`: `'launch'` (starts program) or `'attach'` (attaches to already-running process).\n"
                    "- `program`: Entry point script (`${workspaceFolder}/main.py`).\n"
                    "- `args` and `env`: CLI flags and environment variables."
                )
            }
        ],
        code_snippets=[
            {
                "title": "VS Code `launch.json` Configuration for Python",
                "language": "json",
                "code": (
                    "{\n"
                    "  \"version\": \"0.2.0\",\n"
                    "  \"configurations\": [\n"
                    "    {\n"
                    "      \"name\": \"Python: Current File\",\n"
                    "      \"type\": \"debugpy\",\n"
                    "      \"request\": \"launch\",\n"
                    "      \"program\": \"${file}\",\n"
                    "      \"console\": \"integratedTerminal\",\n"
                    "      \"justMyCode\": true\n"
                    "    }\n"
                    "  ]\n"
                    "}"
                ),
                "explanation": "Standard VS Code launch configuration enabling single-file interactive debugging."
            },
            {
                "title": "Setting a Programmatic Breakpoint in Python (`breakpoint()`)",
                "language": "python",
                "code": (
                    "def calculate_tax(subtotal):\n"
                    "    rate = 0.08\n"
                    "    # Python 3.7+ built-in breakpoint() halts execution and opens debugger\n"
                    "    breakpoint()\n"
                    "    total = subtotal * (1 + rate)\n"
                    "    return total\n\n"
                    "calculate_tax(100.0)"
                ),
                "explanation": "Built-in `breakpoint()` halts execution anywhere without needing IDE GUI clicks."
            },
            {
                "title": "Configuring 'Attach to Process' for Docker / Remote",
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
                "explanation": "Enables debugging containers or remote servers by mapping local and remote paths."
            },
            {
                "title": "The `justMyCode` Setting in VS Code",
                "language": "json",
                "code": (
                    "// In launch.json:\n"
                    "\"justMyCode\": true\n"
                    "// true: Debugger only pauses in your own files, skipping library internals\n"
                    "// false: Debugger steps into standard library and pip packages"
                ),
                "explanation": "`justMyCode` prevents getting lost in complex external dependency source code."
            }
        ],
        coding_challenge={
            "title": "Generate VS Code Debug Configuration Programmatically",
            "instructions": "Write a function `generate_launch_config(app_name, script_path, env_vars)` that returns a dictionary matching a valid VS Code `debugpy` launch configuration object with the provided `name`, `program`, and `env` dictionary.",
            "starter_code": (
                "def generate_launch_config(app_name: str, script_path: str, env: dict) -> dict:\n"
                "    # Return VS Code configuration dictionary\n"
                "    pass\n"
            ),
            "solution_code": (
                "def generate_launch_config(app_name: str, script_path: str, env: dict) -> dict:\n"
                "    return {\n"
                "        'name': f'Python: {app_name}',\n"
                "        'type': 'debugpy',\n"
                "        'request': 'launch',\n"
                "        'program': script_path,\n"
                "        'console': 'integratedTerminal',\n"
                "        'justMyCode': True,\n"
                "        'env': env\n"
                "    }\n\n"
                "print(generate_launch_config('API Server', '${workspaceFolder}/app.py', {'PORT': '8000'}))"
            ),
            "expected_output": "{'name': 'Python: API Server', 'type': 'debugpy', 'request': 'launch', 'program': '${workspaceFolder}/app.py', 'console': 'integratedTerminal', 'justMyCode': True, 'env': {'PORT': '8000'}}"
        },
        quizzes=[
            {
                "question": "What is the primary function of a visual debugger?",
                "options": [
                    "To pause program execution and interactively inspect and modify runtime state, variables, and call stacks",
                    "To format code with prettier indentation",
                    "To compress video files",
                    "To run database backups"
                ],
                "correct_answer": "To pause program execution and interactively inspect and modify runtime state, variables, and call stacks",
                "explanation": "A debugger grants live interactive inspection of memory and execution flow."
            },
            {
                "question": "Which built-in Python function introduced in Python 3.7 invokes the configured debugger at that line?",
                "options": [
                    "`breakpoint()`",
                    "`debugger()`",
                    "`pause()`",
                    "`stop()`"
                ],
                "correct_answer": "`breakpoint()`",
                "explanation": "`breakpoint()` drops the interpreter into `pdb` or the connected IDE debugger automatically."
            },
            {
                "question": "In VS Code, where are custom debug configurations stored?",
                "options": [
                    "In `.vscode/launch.json`",
                    "In `package.json`",
                    "In `system.ini`",
                    "In `requirements.txt`"
                ],
                "correct_answer": "In `.vscode/launch.json`",
                "explanation": "VS Code reads debugging launch targets and parameters from `.vscode/launch.json`."
            },
            {
                "question": "What does setting `\"justMyCode\": true` do in a Python debug configuration?",
                "options": [
                    "It ensures stepping through code only visits your own project files, skipping third-party library source code",
                    "It prevents other developers from viewing your code",
                    "It deletes all comments",
                    "It restricts execution to one CPU core"
                ],
                "correct_answer": "It ensures stepping through code only visits your own project files, skipping third-party library source code",
                "explanation": "`justMyCode` bypasses standard library and installed package internals during stepping."
            },
            {
                "question": "What is the difference between a `'launch'` request and an `'attach'` request in debugging configurations?",
                "options": [
                    "`'launch'` starts a new process under the debugger; `'attach'` connects to an existing, already-running process",
                    "`'attach'` is for web browsers only",
                    "`'launch'` is for C++ only",
                    "There is no difference"
                ],
                "correct_answer": "`'launch'` starts a new process under the debugger; `'attach'` connects to an existing, already-running process",
                "explanation": "`attach` connects to running background daemons or Docker containers via open debug ports."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 20: Breakpoints (Line Breakpoints Basics)
    # ---------------------------------------------------------
    DayBlueprint(
        order=20,
        title="Day 20: Breakpoints (Line Breakpoints Basics)",
        concept="A line breakpoint is an intentional pausing marker placed on a specific executable line of code that signals the runtime interpreter to suspend thread execution right before that line runs.",
        analogy="A line breakpoint is like placing a red traffic light at an intersection. When the car reaches the red light, it comes to a complete halt with the engine running. You can open the car door, check the dashboard, inspect the trunk, and only switch the light to green when you are ready.",
        theory_sections=[
            {
                "heading": "How Breakpoints Work Under the Hood",
                "content": (
                    "When you click in the left margin (gutter) of an IDE, a red dot appears. At the machine level:\n"
                    "- In compiled languages (C/C++), the debugger replaces the machine opcode at that memory address with an `INT 3` (software interrupt instruction).\n"
                    "- In interpreted languages (Python, Node.js), the runtime's execution trace function (`sys.settrace`) checks if the current program counter matches an active breakpoint register.\n"
                    "- When triggered, CPU/thread execution halts, and control yields to the debugger."
                )
            },
            {
                "heading": "Setting and Managing Breakpoints in Modern IDEs",
                "content": (
                    "- **Clicking the Gutter**: Left-clicking next to the line number toggles a breakpoint on/off.\n"
                    "- **Enabling / Disabling**: Right-clicking allows temporarily disabling a breakpoint without deleting it.\n"
                    "- **Breakpoints Window**: The IDE panel lists all active breakpoints across all files, allowing you to mute or enable all with a single click."
                )
            },
            {
                "heading": "Where to Place Line Breakpoints Strategically",
                "content": (
                    "Don't place 50 breakpoints randomly. Place them at strategic decision junctions:\n"
                    "1. Right at the entry point of the suspect function (to verify incoming parameters).\n"
                    "2. Immediately before a complex calculation or mutation.\n"
                    "3. Inside an `if / else` branch to verify whether control actually enters that branch.\n"
                    "4. Right before a `return` statement to inspect the final return value."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Placing Strategic Breakpoints",
                "language": "python",
                "code": (
                    "def calculate_discounted_cart(cart, discount_code):\n"
                    "    # BREAKPOINT 1: Line 3 (Inspect incoming cart items and code)\n"
                    "    subtotal = sum(item['price'] for item in cart)\n"
                    "    \n"
                    "    # BREAKPOINT 2: Line 6 (Check which branch executes)\n"
                    "    if discount_code == 'SUMMER20':\n"
                    "        discount = subtotal * 0.20\n"
                    "    else:\n"
                    "        discount = 0.0\n"
                    "        \n"
                    "    # BREAKPOINT 3: Line 13 (Verify final calculated total)\n"
                    "    final_total = max(0.0, subtotal - discount)\n"
                    "    return final_total"
                ),
                "explanation": "Illustrates strategic placement: input verification, branch entry, and return state."
            },
            {
                "title": "Interactive PDB Breakpoint CLI Commands",
                "language": "bash",
                "code": (
                    "# When breakpoint() triggers in terminal:\n"
                    "# (Pdb) p subtotal          # Print variable value\n"
                    "# (Pdb) whatis discount_code # Print type of variable\n"
                    "# (Pdb) l                   # List surrounding source code lines\n"
                    "# (Pdb) c                   # Continue execution until next breakpoint"
                ),
                "explanation": "Essential commands when using terminal Python PDB debuggers."
            },
            {
                "title": "Breakpoint Execution Flow Rules",
                "language": "python",
                "code": (
                    "# IMPORTANT: Breakpoints pause BEFORE the line executes!\n"
                    "x = 10\n"
                    "x = x + 5  # <-- If breakpoint is placed on this line:\n"
                    "# At this moment, x is STILL 10! The addition has NOT occurred yet."
                ),
                "explanation": "Fundamental debugger behavior: state is frozen prior to executing the marked line."
            },
            {
                "title": "Function Breakpoints vs Line Breakpoints",
                "language": "text",
                "code": (
                    "VS Code / PyCharm Feature:\n"
                    "- Line Breakpoint: Pauses on file 'order.py' line 42.\n"
                    "- Function Breakpoint: Pauses whenever 'checkout()' is invoked,\n"
                    "  regardless of which file or line called it."
                ),
                "explanation": "Function breakpoints are powerful when tracking unexpected calls across large codebases."
            }
        ],
        coding_challenge={
            "title": "Simulate a Breakpoint Execution Tracker",
            "instructions": "Write a class `BreakpointTracker` with methods `add_breakpoint(line_no)` and `execute_line(line_no, current_state)`. When `execute_line` is called on a registered breakpoint line, return `{'paused': True, 'line': line_no, 'state': current_state}`. Otherwise return `{'paused': False}`.",
            "starter_code": (
                "class BreakpointTracker:\n"
                "    def __init__(self):\n"
                "        pass\n\n"
                "    def add_breakpoint(self, line: int):\n"
                "        pass\n\n"
                "    def execute_line(self, line: int, state: dict) -> dict:\n"
                "        pass\n"
            ),
            "solution_code": (
                "class BreakpointTracker:\n"
                "    def __init__(self):\n"
                "        self.bps = set()\n\n"
                "    def add_breakpoint(self, line: int):\n"
                "        self.bps.add(line)\n\n"
                "    def execute_line(self, line: int, state: dict) -> dict:\n"
                "        if line in self.bps:\n"
                "            return {'paused': True, 'line': line, 'state': state.copy()}\n"
                "        return {'paused': False}\n\n"
                "tracker = BreakpointTracker()\n"
                "tracker.add_breakpoint(15)\n"
                "print(tracker.execute_line(14, {'x': 1}))\n"
                "print(tracker.execute_line(15, {'x': 2}))"
            ),
            "expected_output": "{'paused': False}\n{'paused': True, 'line': 15, 'state': {'x': 2}}"
        },
        quizzes=[
            {
                "question": "When execution halts on a line containing a breakpoint, has that specific line already executed?",
                "options": [
                    "No, execution is suspended immediately BEFORE that line runs",
                    "Yes, the line has already completed execution",
                    "Only if the line is an assignment",
                    "It executes halfway"
                ],
                "correct_answer": "No, execution is suspended immediately BEFORE that line runs",
                "explanation": "Breakpoints pause the thread prior to executing the statement on that line."
            },
            {
                "question": "How do you typically toggle a line breakpoint in modern IDEs like VS Code or PyCharm?",
                "options": [
                    "Clicking in the margin (gutter) directly to the left of the line number",
                    "Typing `STOP` in all caps in the code",
                    "Deleting the line of code",
                    "Saving the file as a PDF"
                ],
                "correct_answer": "Clicking in the margin (gutter) directly to the left of the line number",
                "explanation": "Clicking the left gutter toggles a red breakpoint dot on that source line."
            },
            {
                "question": "What is a 'Function Breakpoint'?",
                "options": [
                    "A breakpoint that pauses execution whenever a named function is entered, regardless of where it was called",
                    "A breakpoint that only pauses on weekends",
                    "A breakpoint that modifies the function's return type",
                    "A breakpoint that deletes the function"
                ],
                "correct_answer": "A breakpoint that pauses execution whenever a named function is entered, regardless of where it was called",
                "explanation": "Function breakpoints trigger on entry to any function matching the specified name."
            },
            {
                "question": "What happens if you place a breakpoint on a comment line (`# Just a comment`) in Python?",
                "options": [
                    "The debugger skips it or moves it to the next valid executable line, because comments generate no bytecode instructions",
                    "The computer crashes with a SyntaxError",
                    "The comment is deleted",
                    "The debugger converts the comment into a variable"
                ],
                "correct_answer": "The debugger skips it or moves it to the next valid executable line, because comments generate no bytecode instructions",
                "explanation": "Breakpoints can only bind to executable AST bytecode, so comments are automatically skipped."
            },
            {
                "question": "In the standard Python terminal debugger (`pdb`), which command resumes normal execution until the next breakpoint?",
                "options": [
                    "`c` (continue)",
                    "`r` (restart)",
                    "`q` (quit)",
                    "`k` (kill)"
                ],
                "correct_answer": "`c` (continue)",
                "explanation": "`c` or `continue` instructs the debugger to resume continuous execution until the next breakpoint or termination."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 21: Conditional Breakpoints
    # ---------------------------------------------------------
    DayBlueprint(
        order=21,
        title="Day 21: Conditional Breakpoints",
        concept="Conditional breakpoints evaluate an expression at the breakpoint location, pausing execution ONLY when the condition evaluates to True, eliminating tedious manual stepping through loops.",
        analogy="Imagine an automated traffic camera on a highway with 10,000 cars. You don't want the camera to photograph every single car (standard breakpoint). You configure the camera: 'Only flash if speed > 100 MPH' (conditional breakpoint). The 9,999 normal cars pass through unhindered, and the camera freezes only on the violator.",
        theory_sections=[
            {
                "heading": "The Agony of the 1,000-Iteration Loop",
                "content": (
                    "Imagine a loop processing 5,000 transactions:\n"
                    "```python\n"
                    "for i, tx in enumerate(transactions):\n"
                    "    process(tx)\n"
                    "```\n"
                    "A bug occurs only on transaction index `i == 4821`. If you set a normal breakpoint, you would have to click 'Continue' 4,820 times! One accidental double-click, and you overshoot, forced to restart from zero.\n\n"
                    "A **Conditional Breakpoint** solves this instantly: right-click the breakpoint and enter `i == 4821` or `tx['amount'] < 0`. The debugger runs at full speed for 4,820 iterations and pauses on 4,821."
                )
            },
            {
                "heading": "Types of Advanced Breakpoints",
                "content": (
                    "1. **Expression Condition**: Pauses when a boolean statement is True (e.g. `user_id == 'target_user'`, `len(cart) > 50`).\n"
                    "2. **Hit Count Condition**: Pauses when the line has executed a specific number of times (e.g. `hit count == 100`, `hit count >= 500`).\n"
                    "3. **Logpoints (Tracepoints)**: Prints a message to the debug console without pausing execution (e.g. `Log: Current user is {user.name}`). Zero code edits required!"
                )
            },
            {
                "heading": "Writing Safe Conditional Expressions",
                "content": (
                    "Expressions inside conditional breakpoints must be **side-effect free**:\n"
                    "- DO NOT write `list.pop() == 0` (this alters data during evaluation!).\n"
                    "- DO NOT call functions that write to databases or send network packets.\n"
                    "- Use pure read-only boolean checks: `user.is_admin is False and balance > 10000`."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Loop with Rare Corrupt Record",
                "language": "python",
                "code": (
                    "customers = [{'id': i, 'balance': 100} for i in range(1000)]\n"
                    "# The bug: Record 782 has corrupted balance\n"
                    "customers[782]['balance'] = -9999\n\n"
                    "for cust in customers:\n"
                    "    # CONDITIONAL BREAKPOINT HERE:\n"
                    "    # Condition: cust['balance'] < 0\n"
                    "    # Debugger skips the first 781 iterations and pauses on 782!\n"
                    "    process_account(cust)"
                ),
                "explanation": "Conditional breakpoint expression `cust['balance'] < 0` isolates the defect in milliseconds."
            },
            {
                "title": "Setting Conditional Breakpoint in VS Code",
                "language": "text",
                "code": (
                    "How to configure in VS Code:\n"
                    "1. Right-click the red breakpoint in the gutter.\n"
                    "2. Select 'Edit Breakpoint...'\n"
                    "3. Select 'Expression' from the dropdown.\n"
                    "4. Enter: cust.get('id') == 782 or cust.get('balance') < 0\n"
                    "5. Press Enter. The red dot turns into a red dot with an '=' symbol."
                ),
                "explanation": "UI workflow for attaching dynamic condition criteria to line breakpoints."
            },
            {
                "title": "Hit Count Breakpoint Example",
                "language": "python",
                "code": (
                    "# Pause only on the 500th iteration of a loop\n"
                    "# Edit Breakpoint -> Hit Count: 500\n"
                    "while stream.has_next():\n"
                    "    chunk = stream.read_chunk()\n"
                    "    # Pauses automatically after exactly 500 executions"
                ),
                "explanation": "Hit counts are ideal when debugging memory leaks or performance degradation over time."
            },
            {
                "title": "Logpoints: Logging Without Touching Code",
                "language": "text",
                "code": (
                    "VS Code Logpoint (Diamond Icon):\n"
                    "- Right click gutter -> 'Add Logpoint...'\n"
                    "- Enter: User {user.id} logged in from IP {user.ip_address}\n"
                    "- Behavior: Prints message to Debug Console without stopping execution!\n"
                    "- Benefit: No need to import logging or modify source files."
                ),
                "explanation": "Logpoints inject non-intrusive logging without modifying production source code."
            }
        ],
        coding_challenge={
            "title": "Simulate Conditional Breakpoint Evaluator",
            "instructions": "Write a function `evaluate_breakpoint(condition_str, context_dict)` that safely evaluates a condition expression string against variables in `context_dict`. Return True if the condition evaluates to True, and False if False or if an exception occurs during evaluation.",
            "starter_code": (
                "def evaluate_breakpoint(cond: str, ctx: dict) -> bool:\n"
                "    # Safely evaluate condition within ctx\n"
                "    pass\n"
            ),
            "solution_code": (
                "def evaluate_breakpoint(cond: str, ctx: dict) -> bool:\n"
                "    try:\n"
                "        # Evaluate expression using context as locals dictionary\n"
                "        return bool(eval(cond, {}, ctx))\n"
                "    except Exception:\n"
                "        return False\n\n"
                "context = {'user_id': 105, 'balance': -50}\n"
                "print(evaluate_breakpoint('balance < 0 and user_id == 105', context))\n"
                "print(evaluate_breakpoint('balance > 0', context))"
            ),
            "expected_output": "True\nFalse"
        },
        quizzes=[
            {
                "question": "What is the primary benefit of using a Conditional Breakpoint?",
                "options": [
                    "It pauses execution only when a specified boolean condition evaluates to True, avoiding manual stepping through thousands of loop iterations",
                    "It fixes the bug automatically",
                    "It encrypts the source code",
                    "It bypasses all unit tests"
                ],
                "correct_answer": "It pauses execution only when a specified boolean condition evaluates to True, avoiding manual stepping through thousands of loop iterations",
                "explanation": "Conditional breakpoints filter pauses to exact state scenarios (e.g. `item_id == '123'`)."
            },
            {
                "question": "What is a 'Hit Count' breakpoint?",
                "options": [
                    "A breakpoint that only pauses execution after that line has executed a specified number of times (e.g. on the 100th visit)",
                    "A breakpoint that counts how many times the user clicked the mouse",
                    "A breakpoint that measures website views",
                    "A tool for deleting duplicate files"
                ],
                "correct_answer": "A breakpoint that only pauses execution after that line has executed a specified number of times (e.g. on the 100th visit)",
                "explanation": "Hit count breakpoints pause when iteration counters reach the configured threshold."
            },
            {
                "question": "What is a 'Logpoint' (or Tracepoint) in modern IDEs like VS Code?",
                "options": [
                    "A special breakpoint that prints a formatted message to the debug console without pausing the program's execution",
                    "A tool that exports code to PDF",
                    "A permanent file written to the hard drive",
                    "A database table trigger"
                ],
                "correct_answer": "A special breakpoint that prints a formatted message to the debug console without pausing the program's execution",
                "explanation": "Logpoints log variables on the fly without modifying source files or halting threads."
            },
            {
                "question": "Why should expressions written inside conditional breakpoints be strictly side-effect free?",
                "options": [
                    "Because expressions with side effects (like mutating arrays or calling network endpoints) will alter program behavior every time the condition is evaluated",
                    "Because side effects cause computer monitors to flicker",
                    "Because Python forbids function calls in debuggers",
                    "Because it violates the license agreement"
                ],
                "correct_answer": "Because expressions with side effects (like mutating arrays or calling network endpoints) will alter program behavior every time the condition is evaluated",
                "explanation": "Mutating state during condition checks introduces debugger-induced bugs (Heisenbugs)."
            },
            {
                "question": "What icon typically represents a conditional breakpoint in VS Code's editor gutter?",
                "options": [
                    "A red circle containing an equals sign (`=`) or question mark",
                    "A green triangle",
                    "A yellow star",
                    "A black skull"
                ],
                "correct_answer": "A red circle containing an equals sign (`=`) or question mark",
                "explanation": "VS Code uses a modified red dot symbol to distinguish conditional breakpoints from normal ones."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 22: Stepping Through Code (Over, Into, Out)
    # ---------------------------------------------------------
    DayBlueprint(
        order=22,
        title="Day 22: Stepping Through Code (Over, Into, Out)",
        concept="Stepping navigation controls the execution pointer line-by-line using three primary mechanics: Step Over (next line in current scope), Step Into (dive inside called function), and Step Out (finish current function and return to caller).",
        analogy="Think of reading an encyclopedia. Reading the next paragraph on the same page is Step Over. If a paragraph mentions 'Photosynthesis' and you flip to the dedicated Photosynthesis chapter to study every detail, that is Step Into. Once you finish reading Photosynthesis and flip back to your original bookmark, that is Step Out.",
        theory_sections=[
            {
                "heading": "The 3 Navigation Commands Decoded",
                "content": (
                    "Once a breakpoint halts execution, the debugger toolbar appears with navigation controls:\n"
                    "1. **Step Over (F10 / Step)**: Executes the current line completely and moves to the very next line in the current function. If the line calls a function (`send_email()`), that function runs at full speed without diving into its internal code.\n"
                    "2. **Step Into (F11)**: If the current line calls a function, dives straight into the first line of that called function, creating a new stack frame.\n"
                    "3. **Step Out (Shift+F11)**: Runs the rest of the current function to completion at full speed, returns to the caller, and pauses on the line right after the return."
                )
            },
            {
                "heading": "Continue (F5) vs Step: Knowing When to Use Which",
                "content": (
                    "- Use **Step Over / Step Into** when you are actively examining the crime scene: checking local variables line-by-line.\n"
                    "- Use **Continue (Resume)** when you are done inspecting this area and want the program to run at full speed until the next designated breakpoint.\n"
                    "- Use **Restart (Ctrl+Shift+F5)** to reboot the process with the same debug configuration."
                )
            },
            {
                "heading": "Avoiding the 'Library Abyss' Trap",
                "content": (
                    "A classic beginner mistake is pressing **Step Into** on a line like `print(f'Hello {name}')` or `math.sqrt(x)`. Suddenly the debugger opens Python's internal C-source or standard library code! If this happens, do not panic: press **Step Out (Shift+F11)** immediately to return to your code."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Stepping Navigation Example",
                "language": "python",
                "code": (
                    "def helper_calculation(val):\n"
                    "    a = val * 2\n"
                    "    b = a + 10\n"
                    "    return b\n\n"
                    "def main_process():\n"
                    "    # Paused here on Line 8\n"
                    "    x = 5\n"
                    "    # If you press STEP OVER: helper_calculation runs and pauses on Line 11\n"
                    "    # If you press STEP INTO: Execution dives into Line 2 of helper_calculation\n"
                    "    result = helper_calculation(x)\n"
                    "    print(f'Done: {result}')\n\n"
                    "main_process()"
                ),
                "explanation": "Contrasts Step Over (treating function as a single unit) vs Step Into (diving into function internals)."
            },
            {
                "title": "Standard IDE Keyboard Shortcuts for Stepping",
                "language": "text",
                "code": (
                    "VS Code / Visual Studio Shortcuts:\n"
                    "- Continue / Resume: F5\n"
                    "- Step Over:         F10\n"
                    "- Step Into:         F11\n"
                    "- Step Out:          Shift + F11\n"
                    "- Restart:           Ctrl + Shift + F5\n"
                    "- Stop:              Shift + F5"
                ),
                "explanation": "Standard keybindings for rapid single-handed stepping navigation."
            },
            {
                "title": "PDB Equivalent Stepping Commands",
                "language": "bash",
                "code": (
                    "# In Python PDB Terminal:\n"
                    "# (Pdb) n    # 'next' -> Step Over\n"
                    "# (Pdb) s    # 'step' -> Step Into\n"
                    "# (Pdb) r    # 'return' -> Step Out\n"
                    "# (Pdb) c    # 'continue' -> Resume to next breakpoint"
                ),
                "explanation": "Terminal single-character shorthand for terminal PDB stepping."
            },
            {
                "title": "Step Out Recovery Pattern",
                "language": "python",
                "code": (
                    "# Accidental Step Into third-party library:\n"
                    "# (Pdb) s  -> dives into: site-packages/urllib3/util/retry.py\n"
                    "# Press 'r' (PDB) or Shift+F11 (IDE) to Step Out back to your script!"
                ),
                "explanation": "Demonstrates recovering immediately from accidentally stepping into external libraries."
            }
        ],
        coding_challenge={
            "title": "Simulate Debugger Stepping State Machine",
            "instructions": "Write a class `SteppingSimulator` initialized with call depth 0. Implement methods `step_into()`, `step_out()`, and `step_over()`. `step_into` increments depth. `step_out` decrements depth (minimum 0). `step_over` leaves depth unchanged. Return current depth after each call.",
            "starter_code": (
                "class SteppingSimulator:\n"
                "    def __init__(self):\n"
                "        self.depth = 0\n\n"
                "    def step_into(self) -> int:\n"
                "        pass\n\n"
                "    def step_out(self) -> int:\n"
                "        pass\n\n"
                "    def step_over(self) -> int:\n"
                "        pass\n"
            ),
            "solution_code": (
                "class SteppingSimulator:\n"
                "    def __init__(self):\n"
                "        self.depth = 0\n\n"
                "    def step_into(self) -> int:\n"
                "        self.depth += 1\n"
                "        return self.depth\n\n"
                "    def step_out(self) -> int:\n"
                "        self.depth = max(0, self.depth - 1)\n"
                "        return self.depth\n\n"
                "    def step_over(self) -> int:\n"
                "        return self.depth\n\n"
                "sim = SteppingSimulator()\n"
                "print(sim.step_into())\n"
                "print(sim.step_over())\n"
                "print(sim.step_out())"
            ),
            "expected_output": "1\n1\n0"
        },
        quizzes=[
            {
                "question": "What does the 'Step Over' command do in a visual debugger?",
                "options": [
                    "It executes the current line (including any called functions) and pauses on the very next line in the current scope",
                    "It deletes the current line of code",
                    "It skips the line without executing it",
                    "It restarts the program from the beginning"
                ],
                "correct_answer": "It executes the current line (including any called functions) and pauses on the very next line in the current scope",
                "explanation": "Step Over treats functions called on that line as atomic operations, advancing to the next line in the same function."
            },
            {
                "question": "When would you choose 'Step Into' instead of 'Step Over'?",
                "options": [
                    "When the current line calls a function and you want to enter that function to debug its internal line-by-line logic",
                    "When you want to quit the debugger",
                    "When you want to compile the project",
                    "When you want to format code with black"
                ],
                "correct_answer": "When the current line calls a function and you want to enter that function to debug its internal line-by-line logic",
                "explanation": "Step Into dives into the called function's body, creating a new stack frame."
            },
            {
                "question": "What is the purpose of 'Step Out'?",
                "options": [
                    "It runs the remainder of the current function to completion and pauses immediately in the caller function right after the return",
                    "It shuts down the debugger and closes VS Code",
                    "It signs the user out of GitHub",
                    "It uninstalls the current library"
                ],
                "correct_answer": "It runs the remainder of the current function to completion and pauses immediately in the caller function right after the return",
                "explanation": "Step Out completes the active function execution and pops back up to the caller's frame."
            },
            {
                "question": "If you accidentally press 'Step Into' on `math.sqrt(x)` and end up inside standard library internals, how do you escape back to your code?",
                "options": [
                    "Press 'Step Out' (Shift+F11 in VS Code)",
                    "Delete Python from your computer",
                    "Turn off the power strip",
                    "Press Enter 500 times"
                ],
                "correct_answer": "Press 'Step Out' (Shift+F11 in VS Code)",
                "explanation": "Step Out executes the remainder of the library function and returns immediately to your application frame."
            },
            {
                "question": "What is the standard VS Code shortcut for 'Continue' (resume continuous execution until next breakpoint)?",
                "options": [
                    "F5",
                    "F10",
                    "F1",
                    "Ctrl+C"
                ],
                "correct_answer": "F5",
                "explanation": "F5 resumes normal program execution until the next breakpoint or completion."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 23: Watching Variables in Real-Time
    # ---------------------------------------------------------
    DayBlueprint(
        order=23,
        title="Day 23: Watching Variables in Real-Time",
        concept="The Watch Window allows developers to pin live variables, object properties, and dynamic expressions, tracking how values mutate step-by-step as code executes.",
        analogy="Think of an airplane cockpit. The pilot doesn't constantly climb down into the fuel tank with a wooden dipstick to check fuel levels; they have a fuel gauge right on the main dashboard instrument panel (the Watch Window) that updates in real time as the engines burn fuel.",
        theory_sections=[
            {
                "heading": "Locals Panel vs Watch Window",
                "content": (
                    "- **Variables / Locals Panel**: Automatically displays *every* variable in the current scope. In complex functions, this panel can contain 50 variables, making it noisy to find what you care about.\n"
                    "- **Watch Window**: A custom dashboard where you pin only the specific 2 or 3 expressions you are investigating (e.g. `user.cart.total_price`, `len(active_sessions)`).\n"
                    "As you step through code (F10), pinned watch expressions automatically re-evaluate and display values with color-coded change highlights."
                )
            },
            {
                "heading": "Watching Dynamic Expressions",
                "content": (
                    "Watch expressions are not limited to variable names (`x`). You can enter complete dynamic computational expressions:\n"
                    "- `len(queue) == 0` (Boolean check on whether a buffer is empty)\n"
                    "- `user.role == 'admin'`\n"
                    "- `[item.id for item in items if item.price > 100]`\n"
                    "- `type(payload).__name__`"
                )
            },
            {
                "heading": "Detecting Unintended State Mutations",
                "content": (
                    "A primary utility of watching variables is catching side effects. When stepping over an innocent-looking function call like `format_report(report)`: if you watch `report['generated_at']` change color from red to green, you instantly know `format_report` is mutating your data structure in-place!"
                )
            }
        ],
        code_snippets=[
            {
                "title": "Tracing Variable Mutation in Loop",
                "language": "python",
                "code": (
                    "def calculate_accrued_interest(principal, rate, years):\n"
                    "    balance = principal\n"
                    "    history = []\n"
                    "    for year in range(1, years + 1):\n"
                    "        interest = balance * rate\n"
                    "        balance += interest\n"
                    "        # WATCH EXPRESSIONS TO PIN IN IDE:\n"
                    "        # 1. balance\n"
                    "        # 2. round(interest, 2)\n"
                    "        # 3. f'{balance / principal:.2f}x'\n"
                    "        history.append({'year': year, 'balance': round(balance, 2)})\n"
                    "    return history"
                ),
                "explanation": "Watching expressions during loop steps reveals progression of compounding calculations."
            },
            {
                "title": "Adding Expressions to VS Code Watch Window",
                "language": "text",
                "code": (
                    "How to add watch expressions in VS Code:\n"
                    "1. When debugger is paused, look at 'Watch' panel on left sidebar.\n"
                    "2. Click the '+' icon.\n"
                    "3. Type any valid expression: user.is_authenticated\n"
                    "4. Or right-click a highlighted variable in code -> 'Add to Watch'"
                ),
                "explanation": "UI steps to pin active watches in the VS Code sidebar."
            },
            {
                "title": "Watching Complex Nested Dictionary Attributes",
                "language": "python",
                "code": (
                    "response = {\n"
                    "    'data': {\n"
                    "        'users': [{'id': 1, 'active': True}, {'id': 2, 'active': False}],\n"
                    "        'total': 2\n"
                    "    }\n"
                    "}\n"
                    "# Watch Expression: sum(1 for u in response['data']['users'] if u['active'])\n"
                    "# Evaluates to: 1"
                ),
                "explanation": "Demonstrates watching complex aggregate queries directly inside paused debugger memory."
            },
            {
                "title": "PDB Watch Equivalent (`display` command)",
                "language": "bash",
                "code": (
                    "# In Python PDB:\n"
                    "# (Pdb) display balance\n"
                    "# Displays: balance: 100.0\n"
                    "# Now on every step (n), PDB automatically prints balance changes!"
                ),
                "explanation": "The `display` command in PDB monitors variable changes on every single step."
            }
        ],
        coding_challenge={
            "title": "Simulate a Watch Window Evaluator",
            "instructions": "Write a function `evaluate_watch_list(watch_expressions, scope_dict)` that takes a list of string expressions and evaluates each against `scope_dict`. Return a dictionary `{expr: value_or_error_string}`.",
            "starter_code": (
                "def evaluate_watch_list(watches: list, scope: dict) -> dict:\n"
                "    # Return evaluated watch results\n"
                "    pass\n"
            ),
            "solution_code": (
                "def evaluate_watch_list(watches: list, scope: dict) -> dict:\n"
                "    results = {}\n"
                "    for expr in watches:\n"
                "        try:\n"
                "            val = eval(expr, {}, scope)\n"
                "            results[expr] = val\n"
                "        except Exception as e:\n"
                "            results[expr] = f'<Error: {type(e).__name__}>'\n"
                "    return results\n\n"
                "active_scope = {'count': 5, 'items': ['a', 'b']}\n"
                "print(evaluate_watch_list(['count * 2', 'len(items)', 'items[10]'], active_scope))"
            ),
            "expected_output": "{'count * 2': 10, 'len(items)': 2, 'items[10]': '<Error: IndexError>'}"
        },
        quizzes=[
            {
                "question": "What is the primary difference between the 'Locals / Variables' panel and the 'Watch' window in an IDE debugger?",
                "options": [
                    "Locals shows all variables currently in scope automatically; Watch lets you pin specific variables or custom computed expressions",
                    "Watch is only available in paid versions of software",
                    "Locals only works for numbers",
                    "There is no difference"
                ],
                "correct_answer": "Locals shows all variables currently in scope automatically; Watch lets you pin specific variables or custom computed expressions",
                "explanation": "Watch gives developers focused telemetry on specific expressions without local scope noise."
            },
            {
                "question": "Can you enter computed expressions (e.g. `len(cart) > 0`) into the Watch window, or only bare variable names?",
                "options": [
                    "You can enter any valid runtime language expression, including comparisons, method calls, and arithmetic",
                    "Only single variable names are supported",
                    "Only string literals are supported",
                    "Only global constants are supported"
                ],
                "correct_answer": "You can enter any valid runtime language expression, including comparisons, method calls, and arithmetic",
                "explanation": "Watch windows evaluate full expressions within the active paused frame's memory context."
            },
            {
                "question": "How does the Watch window notify you when a variable's value changes between steps?",
                "options": [
                    "Modern IDEs highlight the changed value with a distinct color (often yellow or green)",
                    "It plays a loud siren through the speakers",
                    "It restarts the computer",
                    "It sends an email alert"
                ],
                "correct_answer": "Modern IDEs highlight the changed value with a distinct color (often yellow or green)",
                "explanation": "Visual highlight cues draw immediate focus to fields that mutated during the previous step."
            },
            {
                "question": "What happens if a watch expression references a variable that has not been defined in the current scope yet?",
                "options": [
                    "The watch displays an error (e.g. `NameError` or `<undefined>`) without crashing your paused program",
                    "The program immediately crashes and closes the IDE",
                    "The variable is initialized to 0",
                    "The file is deleted"
                ],
                "correct_answer": "The watch displays an error (e.g. `NameError` or `<undefined>`) without crashing your paused program",
                "explanation": "Watch expressions are safely sandboxed; errors are caught and rendered inline."
            },
            {
                "question": "Which command in Python's built-in PDB debugger provides continuous watch functionality on every step?",
                "options": [
                    "`display <expression>`",
                    "`watch <expression>`",
                    "`inspect <expression>`",
                    "`track <expression>`"
                ],
                "correct_answer": "`display <expression>`",
                "explanation": "The `display` command in PDB monitors and prints the specified expression on every prompt step."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 24: Evaluating Expressions Dynamically (The Debug Console)
    # ---------------------------------------------------------
    DayBlueprint(
        order=24,
        title="Day 24: Evaluating Expressions Dynamically (The Debug Console)",
        concept="The Debug Console / REPL allows developers to interact directly with paused program memory, evaluating ad-hoc expressions, testing hypothetical fixes, and modifying variable values on the fly.",
        analogy="The Debug Console is like having a direct telephone hotline into the operating room while surgery is paused. You can ask: 'What is the patient's exact oxygen level right now? What happens if we give them 5ml of saline?' You can test the intervention mentally before committing to it.",
        theory_sections=[
            {
                "heading": "The Power of the Interactive Debug Console",
                "content": (
                    "When your code pauses at a breakpoint, execution is frozen, but the Python/Node interpreter is alive and responsive. The **Debug Console** (Debug REPL) runs statements inside the **exact local scope** of that paused line:\n"
                    "- Test edge cases: `sanitize_input(malformed_string)`.\n"
                    "- Query database collections: `db.users.filter(active=True).count()`.\n"
                    "- Check object methods and attributes: `dir(user)` or `help(service.charge)`."
                )
            },
            {
                "heading": "Hot-Patching Memory During Live Debugging",
                "content": (
                    "Did a variable have a wrong value that would crash the next line? In the Debug Console, you can **reassign the variable directly in memory**:\n"
                    "```python\n"
                    "user.is_verified = True\n"
                    "```\n"
                    "When you press Continue (F5), the program proceeds with the newly patched value! This allows you to verify your hypothesis immediately without restarting a 20-minute setup process."
                )
            },
            {
                "heading": "PDB vs IDE Debug Console",
                "content": (
                    "- In VS Code / PyCharm: Simply open the 'Debug Console' tab at the bottom and type expressions.\n"
                    "- In terminal PDB: Any command that is not a PDB keyword (`n`, `s`, `c`) is evaluated directly as Python code. If your variable is named `c` or `n`, prefix with `!` (e.g. `!c = 10` or `p c`)."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Interactive Console Testing at a Breakpoint",
                "language": "python",
                "code": (
                    "def generate_auth_token(user):\n"
                    "    secret = 'my_secret_key'\n"
                    "    # Breakpoint paused here:\n"
                    "    # Debug Console interactions:\n"
                    "    # >>> user['role']\n"
                    "    # 'guest'\n"
                    "    # >>> 'admin' in user['permissions']\n"
                    "    # False\n"
                    "    # >>> # Test fix in console before editing file:\n"
                    "    # >>> user.get('role') == 'admin' or 'admin' in user.get('permissions', [])\n"
                    "    is_admin = user['role'] == 'admin'\n"
                    "    return {'token': 'xyz', 'admin': is_admin}"
                ),
                "explanation": "Allows drafting and verifying complex boolean logic directly against live memory."
            },
            {
                "title": "Hot-Patching State in Debug Console",
                "language": "python",
                "code": (
                    "def process_transaction(balance, cost):\n"
                    "    # Paused here with balance = 0, which would cause an error downstream\n"
                    "    # Developer types in Debug Console: balance = 500\n"
                    "    # Resume execution: code proceeds with balance = 500!\n"
                    "    remaining = balance - cost\n"
                    "    return remaining"
                ),
                "explanation": "Modifying state dynamically confirms whether changing variable values resolves issues downstream."
            },
            {
                "title": "PDB `!` Escape Prefix for Shadowed Commands",
                "language": "bash",
                "code": (
                    "# In PDB, typing 'c' means 'continue'!\n"
                    "# What if your variable is named 'c'?\n"
                    "# (Pdb) p c         # 'p' prints variable c\n"
                    "# (Pdb) !c = 100    # '!' forces Python assignment instead of PDB command"
                ),
                "explanation": "The `!` prefix distinguishes Python statements from PDB single-character debugger directives."
            },
            {
                "title": "Inspecting Methods with `dir()` in Debug Console",
                "language": "python",
                "code": (
                    "# When dealing with unfamiliar third-party objects:\n"
                    "# >>> dir(response)\n"
                    "# ['__class__', 'content', 'headers', 'json', 'status_code', 'text']\n"
                    "# >>> response.status_code\n"
                    "# 200"
                ),
                "explanation": "`dir()` exposes all available methods and attributes on any live object in scope."
            }
        ],
        coding_challenge={
            "title": "Build a Safe Expression Evaluator with State Patching",
            "instructions": "Write a function `execute_debug_command(command_str, context_dict)` that evaluates expression statements. If `command_str` is an assignment like `'x = 50'`, update `context_dict['x'] = 50` and return `'UPDATED'`. If it is an expression like `'x + 10'`, return the evaluated result. If it raises an error, return `'ERROR: <type>'`.",
            "starter_code": (
                "def execute_debug_command(cmd: str, ctx: dict):\n"
                "    # Execute or evaluate command in ctx\n"
                "    pass\n"
            ),
            "solution_code": (
                "def execute_debug_command(cmd: str, ctx: dict):\n"
                "    try:\n"
                "        if '=' in cmd and not any(op in cmd for op in ['==', '!=', '<=', '>=']):\n"
                "            var_name, val_expr = cmd.split('=', 1)\n"
                "            ctx[var_name.strip()] = eval(val_expr.strip(), {}, ctx)\n"
                "            return 'UPDATED'\n"
                "        return eval(cmd, {}, ctx)\n"
                "    except Exception as e:\n"
                "        return f'ERROR: {type(e).__name__}'\n\n"
                "scope = {'a': 10}\n"
                "print(execute_debug_command('a * 3', scope))\n"
                "print(execute_debug_command('a = 40', scope))\n"
                "print(scope['a'])"
            ),
            "expected_output": "30\nUPDATED\n40"
        },
        quizzes=[
            {
                "question": "What is the primary function of the Debug Console (Debug REPL) during a paused breakpoint session?",
                "options": [
                    "It allows evaluating ad-hoc expressions and testing code directly inside the live memory scope of the paused program",
                    "It formats the code with Prettier",
                    "It turns the screen brightness down",
                    "It uploads the code to GitHub"
                ],
                "correct_answer": "It allows evaluating ad-hoc expressions and testing code directly inside the live memory scope of the paused program",
                "explanation": "The Debug Console runs interactive code inside the exact call frame and scope of the paused thread."
            },
            {
                "question": "Can you modify the value of a variable in memory via the Debug Console while execution is paused?",
                "options": [
                    "Yes, reassigning variables in the console mutates live memory, and execution continues with the new value upon resume",
                    "No, memory is completely read-only in debuggers",
                    "Only if using C++",
                    "Only on Linux"
                ],
                "correct_answer": "Yes, reassigning variables in the console mutates live memory, and execution continues with the new value upon resume",
                "explanation": "Hot-patching memory in the console allows testing fixes without restarting the process."
            },
            {
                "question": "In Python's terminal PDB, why do you need to write `!n = 10` instead of `n = 10`?",
                "options": [
                    "Because 'n' is the reserved PDB command for 'next' (step over); the '!' prefix forces execution as a Python statement",
                    "Because '!' makes the variable global",
                    "Because '!' is required for all integers in Python",
                    "Because '!' encrypts the assignment"
                ],
                "correct_answer": "Because 'n' is the reserved PDB command for 'next' (step over); the '!' prefix forces execution as a Python statement",
                "explanation": "The `!` prefix tells PDB to interpret the command as raw Python rather than a debugger command."
            },
            {
                "question": "What built-in Python function is useful in the Debug Console to inspect all available methods on an unfamiliar object?",
                "options": [
                    "`dir(object)`",
                    "`list_methods(object)`",
                    "`inspect(object)`",
                    "`methods(object)`"
                ],
                "correct_answer": "`dir(object)`",
                "explanation": "`dir(object)` returns all valid attributes and methods available on that instance."
            },
            {
                "question": "What happens to variables created exclusively inside the Debug Console session after the program finishes execution?",
                "options": [
                    "They exist only in transient memory and are discarded when the process terminates",
                    "They are saved to your source code file automatically",
                    "They are written to a permanent SQL database",
                    "They create merge conflicts in Git"
                ],
                "correct_answer": "They exist only in transient memory and are discarded when the process terminates",
                "explanation": "Debug console variables reside in process RAM and vanish upon process termination."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 25: Call Stack Inspection & Frame Switching
    # ---------------------------------------------------------
    DayBlueprint(
        order=25,
        title="Day 25: Call Stack Inspection & Frame Switching",
        concept="The Call Stack panel visualizes active execution frames, allowing developers to travel backwards in time by switching frames to inspect caller variables and arguments higher up the chain.",
        analogy="Imagine an elevator in a 10-story department store. You got on at Floor 1 (main), transferred at Floor 4 (API handler), and reached Floor 9 (database query) where an item is missing. You don't have to guess how you got here: the elevator indicator shows every floor you passed, and you can press Floor 4 to look at the shopping cart you carried before reaching Floor 9.",
        theory_sections=[
            {
                "heading": "Understanding Call Stack Frames",
                "content": (
                    "When an application crashes or pauses 5 levels deep in a utility function:\n"
                    "- Frame 0 (top): `db.query('SELECT ...')`\n"
                    "- Frame 1: `user_repository.find_by_id(user_id)`\n"
                    "- Frame 2: `auth_service.login(username, password)`\n"
                    "- Frame 3: `api_controller.handle_login(request)`\n"
                    "- Frame 4 (bottom): `server.run()`\n\n"
                    "The defect is rarely in `db.query` (Frame 0). The real bug is usually that `api_controller` (Frame 3) passed `None` into `user_repository`!"
                )
            },
            {
                "heading": "Frame Switching in Visual Debuggers",
                "content": (
                    "In VS Code and PyCharm, the Call Stack window is **interactive**:\n"
                    "1. Click on Frame 3 (`api_controller`).\n"
                    "2. The code editor instantly jumps to that file and line.\n"
                    "3. The Variables and Watch windows **instantly update to show the local variables of Frame 3**!\n"
                    "You are traveling backward through the call chain without restarting the program."
                )
            },
            {
                "heading": "Frame Switching in Terminal PDB (`up` / `down`)",
                "content": (
                    "In terminal PDB, you can navigate frames directly:\n"
                    "- `u` (`up`): Move one level UP the call stack toward the caller.\n"
                    "- `d` (`down`): Move one level DOWN the call stack toward the crash site.\n"
                    "- `where` / `w`: Print the full call stack with an arrow indicating the currently selected frame."
                )
            }
        ],
        code_snippets=[
            {
                "title": "A Multi-Frame Execution Chain",
                "language": "python",
                "code": (
                    "def format_receipt(customer_name, items, tax_rate):\n"
                    "    # Frame 3: Paused here. Why is tax_rate 0?\n"
                    "    subtotal = sum(i['price'] for i in items)\n"
                    "    return {'customer': customer_name, 'tax': subtotal * tax_rate}\n\n"
                    "def checkout_workflow(order_dict):\n"
                    "    # Frame 2: Look at order_dict in caller frame!\n"
                    "    # Real bug: order_dict was missing 'tax_rate', defaulted to 0\n"
                    "    rate = order_dict.get('tax_rate', 0.0)\n"
                    "    return format_receipt(order_dict['name'], order_dict['items'], rate)\n\n"
                    "def handle_web_request(raw_payload):\n"
                    "    # Frame 1: Entry point\n"
                    "    return checkout_workflow(raw_payload)"
                ),
                "explanation": "Switching to Frame 2 reveals that `tax_rate` was defaulted to 0 because the caller omitted the key."
            },
            {
                "title": "Inspecting Frames in PDB via CLI",
                "language": "bash",
                "code": (
                    "# When breakpoint triggers in format_receipt:\n"
                    "# (Pdb) where\n"
                    "#   handle_web_request()\n"
                    "#   checkout_workflow()\n"
                    "# > format_receipt()  <-- Current frame\n"
                    "# (Pdb) u             # Move UP to checkout_workflow frame\n"
                    "# (Pdb) p order_dict  # Inspect caller's local variables!\n"
                    "# (Pdb) d             # Move back DOWN to format_receipt frame"
                ),
                "explanation": "Navigating call frames using `u` and `d` commands in PDB."
            },
            {
                "title": "Programmatically Inspecting the Call Stack",
                "language": "python",
                "code": (
                    "import inspect\n\n"
                    "def audit_caller():\n"
                    "    # Get current stack frames\n"
                    "    stack = inspect.stack()\n"
                    "    # stack[1] is the immediate caller\n"
                    "    caller_frame = stack[1]\n"
                    "    print(f'Called by: {caller_frame.function} at {caller_frame.filename}:{caller_frame.lineno}')\n\n"
                    "def my_service():\n"
                    "    audit_caller()\n\n"
                    "my_service() # Prints caller metadata"
                ),
                "explanation": "`inspect.stack()` inspects caller frame metadata dynamically at runtime."
            },
            {
                "title": "Call Stack Overflow Visualization",
                "language": "python",
                "code": (
                    "# Infinite recursion generating 1000 identical frames:\n"
                    "def infinite_call(count):\n"
                    "    return infinite_call(count + 1)\n\n"
                    "# RecursionError: maximum recursion depth exceeded\n"
                    "# The call stack shows 1000 copies of infinite_call frame"
                ),
                "explanation": "Illustrates how recursive logic flaws exhaust call stack capacity."
            }
        ],
        coding_challenge={
            "title": "Trace the Call Hierarchy Programmatically",
            "instructions": "Write a function `get_call_chain()` that uses Python's `inspect.stack()` to return a list of function name strings representing the call sequence leading to `get_call_chain` (ordered from highest-level caller down to `'get_call_chain'`).",
            "starter_code": (
                "import inspect\n\n"
                "def get_call_chain() -> list:\n"
                "    # Return list of function names in call stack order\n"
                "    pass\n"
            ),
            "solution_code": (
                "import inspect\n\n"
                "def get_call_chain() -> list:\n"
                "    stack = inspect.stack()\n"
                "    names = [frame.function for frame in reversed(stack)]\n"
                "    return names\n\n"
                "def alpha(): return beta()\n"
                "def beta(): return get_call_chain()\n"
                "chain = alpha()\n"
                "print([f for f in chain if f in ['alpha', 'beta', 'get_call_chain']])"
            ),
            "expected_output": "['alpha', 'beta', 'get_call_chain']"
        },
        quizzes=[
            {
                "question": "What is the primary benefit of clicking on an older frame in the IDE's Call Stack window?",
                "options": [
                    "The editor jumps to that caller's line and updates the Variables window to show that caller's local variables",
                    "It rewinds program execution and re-runs the code backwards",
                    "It restarts the computer",
                    "It deletes that frame from memory"
                ],
                "correct_answer": "The editor jumps to that caller's line and updates the Variables window to show that caller's local variables",
                "explanation": "Frame switching shifts the debugger's inspection lens to examine caller state and arguments."
            },
            {
                "question": "In Python's terminal PDB, which command navigates one level UP the call stack toward the caller?",
                "options": [
                    "`u` (or `up`)",
                    "`d` (or `down`)",
                    "`n` (or `next`)",
                    "`c` (or `continue`)"
                ],
                "correct_answer": "`u` (or `up`)",
                "explanation": "`u` ascends toward the caller frame; `d` descends toward the point of the breakpoint/crash."
            },
            {
                "question": "Why is the root cause of a bug frequently found in an upper stack frame rather than the bottom-most frame where the crash occurred?",
                "options": [
                    "Because an upper caller function passed invalid, corrupt, or None arguments into the utility function that crashed",
                    "Because bottom frames are always written in C",
                    "Because upper frames are faster",
                    "Because top frames are ignored by the compiler"
                ],
                "correct_answer": "Because an upper caller function passed invalid, corrupt, or None arguments into the utility function that crashed",
                "explanation": "Utility functions crash when callers provide bad inputs; checking caller frames exposes the source."
            },
            {
                "question": "What Python standard library module allows programmatically inspecting the live call stack and caller metadata?",
                "options": [
                    "`inspect`",
                    "`callstack`",
                    "`frames`",
                    "`memory`"
                ],
                "correct_answer": "`inspect`",
                "explanation": "Python's `inspect` module provides `inspect.stack()` to retrieve active frame objects."
            },
            {
                "question": "What error occurs when a function calls itself indefinitely without reaching a terminating base condition?",
                "options": [
                    "`RecursionError` (Stack Overflow)",
                    "`SyntaxError`",
                    "`KeyError`",
                    "`ModuleNotFoundError`"
                ],
                "correct_answer": "`RecursionError` (Stack Overflow)",
                "explanation": "Unbounded recursive calls exhaust stack frame memory, triggering a RecursionError."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 26: Browser DevTools Basics (Inspect Element & Box Model)
    # ---------------------------------------------------------
    DayBlueprint(
        order=26,
        title="Day 26: Browser DevTools Basics (Inspect Element & Box Model)",
        concept="Browser DevTools provide an interactive client-side diagnostic suite to inspect rendered HTML DOM trees, tweak CSS box models in real time, and audit responsive layouts.",
        analogy="Inspect Element is like wearing architectural X-Ray goggles while walking through a building. You point your goggles at a wall and see the exact pipes, electrical wiring, insulation thickness (padding), wall studs (border), and air gap to the next building (margin).",
        theory_sections=[
            {
                "heading": "Opening and Docking Browser DevTools",
                "content": (
                    "Available across Chrome, Firefox, Safari, and Edge:\n"
                    "- Shortcut: `F12` or `Ctrl+Shift+I` (Windows/Linux) / `Cmd+Option+I` (macOS).\n"
                    "- Direct inspection: Right-click any UI element on any webpage -> **Inspect**.\n"
                    "- Docking options: Dock to right (best for widescreen), dock to bottom (best for console/logs), or undock to a separate monitor."
                )
            },
            {
                "heading": "The Elements / Inspector Panel",
                "content": (
                    "The Elements panel is a live, bi-directional view of the DOM (Document Object Model):\n"
                    "- **DOM Tree (Left)**: Live rendered HTML elements. You can double-click any text or attribute to edit it, or drag-and-drop elements to test layout reflows.\n"
                    "- **Styles Pane (Right)**: Shows all active CSS rules applied to the selected element, ordered by specificity. Crossed-out lines indicate overridden or invalid CSS properties."
                )
            },
            {
                "heading": "Mastering the CSS Box Model",
                "content": (
                    "Every HTML element is a box composed of 4 concentric layers:\n"
                    "1. **Content**: The inner dimensions of text/images (width x height).\n"
                    "2. **Padding**: Spacing *inside* the element between content and border.\n"
                    "3. **Border**: The stroke line surrounding the padding.\n"
                    "4. **Margin**: Spacing *outside* the element separating it from neighbors.\n"
                    "The visual Box Model diagram at the bottom of the Styles tab shows the exact computed pixel values for all 4 layers."
                )
            }
        ],
        code_snippets=[
            {
                "title": "A Classic Box Model Overflow Bug",
                "language": "html",
                "code": (
                    "<!-- BUG: Element overflows container because default box-sizing adds padding to width! -->\n"
                    "<style>\n"
                    "  .container { width: 300px; border: 1px solid black; }\n"
                    "  /* Width = 300px + 20px padding left + 20px padding right = 340px! (Overflows) */\n"
                    "  .box-broken {\n"
                    "    width: 300px;\n"
                    "    padding: 20px;\n"
                    "    background: coral;\n"
                    "  }\n"
                    "</style>\n"
                    "<div class=\"container\">\n"
                    "  <div class=\"box-broken\">Overflows parent container!</div>\n"
                    "</div>"
                ),
                "explanation": "Default `box-sizing: content-box` adds padding outside the declared width, breaking layouts."
            },
            {
                "title": "The Universal Box-Sizing Fix (`border-box`)",
                "language": "css",
                "code": (
                    "/* THE UNIVERSAL CSS RESET: Enforces border-box everywhere */\n"
                    "*,\n"
                    "*::before,\n"
                    "*::after {\n"
                    "  box-sizing: border-box;\n"
                    "}\n\n"
                    "/* Now width: 300px includes content + padding + border inside the 300px! */\n"
                    ".box-fixed {\n"
                    "  width: 300px;\n"
                    "  padding: 20px;\n"
                    "  background: lightgreen;\n"
                    "}"
                ),
                "explanation": "`border-box` absorbs padding and border into the specified width, eliminating overflow."
            },
            {
                "title": "Using the Computed Styles Tab",
                "language": "text",
                "code": (
                    "Debugging CSS Specificity Conflicts:\n"
                    "1. Inspect the element.\n"
                    "2. Click the 'Computed' tab in the right pane.\n"
                    "3. Filter for 'display' or 'font-size'.\n"
                    "4. Click the small arrow next to the property to see EVERY stylesheet rule\n"
                    "   that competed for that property and which selector won specificity!"
                ),
                "explanation": "Computed tab resolves which selector won CSS specificity conflicts."
            },
            {
                "title": "Forcing Element Pseudo-States (:hover, :active)",
                "language": "text",
                "code": (
                    "Testing Hover & Active States in DevTools:\n"
                    "1. In Styles tab, click the ':hov' toggle button.\n"
                    "2. Check ':hover' or ':focus'.\n"
                    "3. The browser permanently simulates hover state without you holding the mouse!"
                ),
                "explanation": "Forcing pseudo-states allows debugging dropdowns and tooltips without mouse gymnastics."
            }
        ],
        coding_challenge={
            "title": "Calculate Total Rendered Box Model Width",
            "instructions": "Write a function `calculate_box_width(width, padding_x, border_x, margin_x, box_sizing)` that calculates the total horizontal space occupied by an element. For `'content-box'`, total width is `width + 2*(padding_x + border_x + margin_x)`. For `'border-box'`, total width is `max(width, 2*(padding_x + border_x)) + 2*margin_x`.",
            "starter_code": (
                "def calculate_box_width(w: int, pad: int, border: int, margin: int, sizing: str) -> int:\n"
                "    # Return total horizontal space\n"
                "    pass\n"
            ),
            "solution_code": (
                "def calculate_box_width(w: int, pad: int, border: int, margin: int, sizing: str) -> int:\n"
                "    if sizing == 'content-box':\n"
                "        return w + (2 * pad) + (2 * border) + (2 * margin)\n"
                "    elif sizing == 'border-box':\n"
                "        inner = max(w, 2 * (pad + border))\n"
                "        return inner + (2 * margin)\n"
                "    return w\n\n"
                "print(calculate_box_width(300, 20, 2, 10, 'content-box'))\n"
                "print(calculate_box_width(300, 20, 2, 10, 'border-box'))"
            ),
            "expected_output": "364\n320"
        },
        quizzes=[
            {
                "question": "What is the keyboard shortcut to open Browser Developer Tools across modern desktop browsers?",
                "options": [
                    "F12 (or Ctrl+Shift+I / Cmd+Option+I)",
                    "F1",
                    "F5",
                    "Alt+Tab"
                ],
                "correct_answer": "F12 (or Ctrl+Shift+I / Cmd+Option+I)",
                "explanation": "F12 is the universal shortcut to toggle DevTools in Chrome, Edge, Firefox, and Safari."
            },
            {
                "question": "In the CSS Box Model, what is the layer between the content and the border?",
                "options": [
                    "Padding",
                    "Margin",
                    "Outline",
                    "Shadow"
                ],
                "correct_answer": "Padding",
                "explanation": "Padding surrounds the content; the border encases the padding; margins surround the border."
            },
            {
                "question": "Why do modern CSS developers apply `box-sizing: border-box` across all elements?",
                "options": [
                    "It ensures padding and borders are included inside the declared width, preventing elements from overflowing containers",
                    "It makes web pages load twice as fast",
                    "It renders 3D shadows automatically",
                    "It converts HTML to canvas"
                ],
                "correct_answer": "It ensures padding and borders are included inside the declared width, preventing elements from overflowing containers",
                "explanation": "`border-box` includes padding and borders within the declared width/height dimensions."
            },
            {
                "question": "In the DevTools Styles pane, what does a strikethrough line through a CSS property mean?",
                "options": [
                    "The rule was overridden by another selector with higher specificity or declared later in the cascade",
                    "The browser deleted the CSS file",
                    "The CSS property is illegal",
                    "The server returned a 404 error"
                ],
                "correct_answer": "The rule was overridden by another selector with higher specificity or declared later in the cascade",
                "explanation": "Strikethrough styling signals that a higher-specificity rule won the cascade battle."
            },
            {
                "question": "How can you debug a `:hover` dropdown menu in DevTools without holding your mouse over the element?",
                "options": [
                    "Use the `:hov` toggle in the Styles panel to force the `:hover` pseudo-class permanently",
                    "Take a screenshot of the screen",
                    "Disconnect the mouse",
                    "Reload the browser tab"
                ],
                "correct_answer": "Use the `:hov` toggle in the Styles panel to force the `:hover` pseudo-class permanently",
                "explanation": "The `:hov` toggle locks pseudo-classes (`:hover`, `:focus`, `:active`) in place for inspection."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 27: Console Debugging (console.log, table, trace, group)
    # ---------------------------------------------------------
    DayBlueprint(
        order=27,
        title="Day 27: Console Debugging (console.log, table, trace, group)",
        concept="The Browser Console API provides specialized diagnostic formatting methods—such as console.table, console.trace, and console.group—turning messy text logs into rich, interactive data tables.",
        analogy="If `console.log` is dumping a sack of groceries all over your kitchen counter in a chaotic pile, `console.table` is putting the groceries into neatly organized, labeled refrigerator drawers with prices and expiry dates clearly visible.",
        theory_sections=[
            {
                "heading": "Beyond Simple `console.log`",
                "content": (
                    "Most web developers only know `console.log()`. But the Browser Console API contains powerful built-in utilities:\n"
                    "- `console.table(data)`: Renders arrays of objects as an interactive, sortable spreadsheet table.\n"
                    "- `console.trace(label)`: Prints the exact JavaScript call stack at that line.\n"
                    "- `console.group('Title')` / `console.groupEnd()`: Collapses related log statements into expandable accordion folders.\n"
                    "- `console.time('Timer')` / `console.timeEnd('Timer')`: High-precision performance benchmarking in milliseconds."
                )
            },
            {
                "heading": "The Danger of Logging Objects by Reference",
                "content": (
                    "A notorious JavaScript debugging bug:\n"
                    "```javascript\n"
                    "const user = { name: 'Alice', age: 20 };\n"
                    "console.log(user);\n"
                    "user.age = 30;\n"
                    "```\n"
                    "When you expand the object in the browser console, Chrome shows `age: 30`! Why? Because the browser console stores an **active reference** to the object, resolving its properties only when you expand it.\n\n"
                    "**Solution**: Log a snapshot: `console.log(JSON.parse(JSON.stringify(user)))` or `console.log({ ...user })`."
                )
            },
            {
                "heading": "Colorizing Console Output with CSS",
                "content": (
                    "You can style browser console messages using the `%c` format specifier:\n"
                    "`console.log('%c SUCCESS ', 'background: green; color: white; border-radius: 4px', user);`\n"
                    "This creates striking visual signposts in dense application logs."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Interactive Spreadsheet Output with `console.table`",
                "language": "javascript",
                "code": (
                    "const users = [\n"
                    "  { id: 101, name: 'Alice', role: 'admin', active: true },\n"
                    "  { id: 102, name: 'Bob', role: 'member', active: false },\n"
                    "  { id: 103, name: 'Charlie', role: 'member', active: true }\n"
                    "];\n\n"
                    "// Renders a beautiful sortable table in DevTools\n"
                    "console.table(users, ['name', 'role']);"
                ),
                "explanation": "Renders an interactive tabular view, optionally filtering for specific columns."
            },
            {
                "title": "Benchmarking with `console.time`",
                "language": "javascript",
                "code": (
                    "console.time('fetchAndParse');\n"
                    "// Simulate computationally heavy task or API call\n"
                    "const data = Array.from({ length: 100000 }, (_, i) => i * 2);\n"
                    "const sum = data.reduce((acc, n) => acc + n, 0);\n"
                    "console.timeEnd('fetchAndParse');\n"
                    "// Output: fetchAndParse: 4.82ms"
                ),
                "explanation": "Measures precise elapsed millisecond duration between paired markers."
            },
            {
                "title": "Collapsible Log Groups with `console.group`",
                "language": "javascript",
                "code": (
                    "console.groupCollapsed('User Registration Pipeline');\n"
                    "console.log('1. Validating input fields...');\n"
                    "console.log('2. Hashing password...');\n"
                    "console.log('3. Storing in database...');\n"
                    "console.groupEnd();\n"
                    "// Renders as a clean, collapsed folder in the browser console"
                ),
                "explanation": "Groups related log statements into collapsible accordions to keep consoles uncluttered."
            },
            {
                "title": "Avoiding the Live Object Reference Trap",
                "language": "javascript",
                "code": (
                    "const cart = { items: ['apple'] };\n"
                    "// BUG: If items is mutated later, expanding this shows future state\n"
                    "console.log('Live ref:', cart);\n\n"
                    "// FIX: Snapshot clone captures current state permanently\n"
                    "console.log('Snapshot:', JSON.parse(JSON.stringify(cart)));\n"
                    "cart.items.push('banana');"
                ),
                "explanation": "Deep cloning captures the exact state snapshot at that specific moment in time."
            }
        ],
        coding_challenge={
            "title": "Format Data for Console Table Simulator",
            "instructions": "Write a function `simulate_console_table(objects_list, columns)` that takes a list of dictionaries and returns a list of dictionaries where each item only contains the keys listed in `columns`. If an object is missing a column key, assign `'<undefined>'`.",
            "starter_code": (
                "def simulate_console_table(items: list, columns: list) -> list:\n"
                "    # Return filtered table representation\n"
                "    pass\n"
            ),
            "solution_code": (
                "def simulate_console_table(items: list, columns: list) -> list:\n"
                "    table = []\n"
                "    for obj in items:\n"
                "        row = {col: obj.get(col, '<undefined>') for col in columns}\n"
                "        table.append(row)\n"
                "    return table\n\n"
                "data = [\n"
                "    {'name': 'Alice', 'role': 'admin', 'age': 30},\n"
                "    {'name': 'Bob', 'age': 25}\n"
                "]\n"
                "print(simulate_console_table(data, ['name', 'role']))"
            ),
            "expected_output": "[{'name': 'Alice', 'role': 'admin'}, {'name': 'Bob', 'role': '<undefined>'}]"
        },
        quizzes=[
            {
                "question": "What does `console.table(users)` do when called in browser JavaScript?",
                "options": [
                    "Renders an array of objects as a clean, sortable tabular grid in the developer console",
                    "Creates an HTML `<table>` element on the webpage",
                    "Exports data to an Excel spreadsheet",
                    "Sends data to a SQL database"
                ],
                "correct_answer": "Renders an array of objects as a clean, sortable tabular grid in the developer console",
                "explanation": "`console.table` formats collections of objects as formatted interactive console tables."
            },
            {
                "question": "Why can expanding an object logged with `console.log(myObj)` sometimes display deceptive or future property values in Chrome DevTools?",
                "options": [
                    "The console evaluates object properties lazily when you expand the arrow, showing the object's mutated state at the moment of expansion",
                    "Chrome reverses data structures automatically",
                    "JavaScript does not support objects",
                    "The browser re-runs the program from line 1"
                ],
                "correct_answer": "The console evaluates object properties lazily when you expand the arrow, showing the object's mutated state at the moment of expansion",
                "explanation": "Browsers store active references; expanding the object reads live current memory rather than historical state."
            },
            {
                "question": "Which paired Console API methods measure the elapsed execution time of an operation in milliseconds?",
                "options": [
                    "`console.time('label')` and `console.timeEnd('label')`",
                    "`console.startTimer()` and `console.stopTimer()`",
                    "`console.clock()` and `console.unclock()`",
                    "`console.measure()` and `console.done()`"
                ],
                "correct_answer": "`console.time('label')` and `console.timeEnd('label')`",
                "explanation": "`console.time`/`timeEnd` provide high-resolution timer benchmarking labeled with the identifier string."
            },
            {
                "question": "What is the purpose of `console.groupCollapsed('Details')`?",
                "options": [
                    "It organizes subsequent log statements into a collapsed, expandable accordion folder in the console",
                    "It deletes previous log statements",
                    "It hides logs from non-admin users",
                    "It compresses console logs into zip files"
                ],
                "correct_answer": "It organizes subsequent log statements into a collapsed, expandable accordion folder in the console",
                "explanation": "Group collapsed folders keep complex multi-step logs organized and readable."
            },
            {
                "question": "What does `console.trace('Checkpoint')` print to the browser console?",
                "options": [
                    "The full JavaScript call stack leading up to the line where `console.trace` was called",
                    "A GPS map of user location",
                    "The browser's cookies",
                    "The entire HTML DOM structure"
                ],
                "correct_answer": "The full JavaScript call stack leading up to the line where `console.trace` was called",
                "explanation": "`console.trace()` logs the active call stack frames without throwing an actual error."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 28: DOM & CSS Debugging (Break on Subtree, Z-Index)
    # ---------------------------------------------------------
    DayBlueprint(
        order=28,
        title="Day 28: DOM & CSS Debugging (Break on Subtree, Z-Index)",
        concept="DOM & CSS debugging isolates visual defects such as z-index stacking context traps, phantom margins, and mysterious JavaScript DOM modifications using DOM Mutation Breakpoints.",
        analogy="Imagine you arrange chairs in your living room, but whenever you turn around, someone secretly moves a chair. DOM Mutation Breakpoints are like putting a laser sensor on the chair. The instant any JavaScript code touches or moves the chair, the laser trips and freezes the culprit red-handed with their hands on the furniture.",
        theory_sections=[
            {
                "heading": "DOM Mutation Breakpoints (Catching Sneaky JS)",
                "content": (
                    "In large frontend applications (React, Vue, legacy jQuery), third-party scripts or rogue event listeners often mutate the DOM unexpectedly (e.g. removing a class or deleting an element).\n\n"
                    "**DOM Breakpoints**: In the Elements panel, right-click an element -> **Break on**:\n"
                    "1. **Subtree Modifications**: Pauses JS execution if any child node is added or removed.\n"
                    "2. **Attribute Modifications**: Pauses JS execution when an attribute changes (e.g. `class=\"hidden\"` or `disabled`).\n"
                    "3. **Node Removal**: Pauses JS execution when the element is removed from the DOM."
                )
            },
            {
                "heading": "The Z-Index Stacking Context Trap",
                "content": (
                    "You set `z-index: 999999;` on a modal popup, but a header element with `z-index: 2;` still renders on top of it! Why?\n\n"
                    "**Stacking Contexts**: `z-index` values are **not global**. An element can only compete within its own Stacking Context. A new stacking context is created by:\n"
                    "- Elements with `position: relative/absolute` and a numeric `z-index`.\n"
                    "- Elements with `opacity < 1`.\n"
                    "- Elements with `transform`, `filter`, or `will-change`.\n"
                    "If a parent has lower stacking priority, a child with `z-index: 999999` is trapped inside the parent's lower plane."
                )
            },
            {
                "heading": "Debugging Flexbox and Grid Layouts in DevTools",
                "content": (
                    "Modern DevTools feature dedicated interactive layout badges:\n"
                    "- Clicking the **`flex`** or **`grid`** badge overlays visual alignment guides directly on the page.\n"
                    "- Clicking the layout icon in the Styles panel opens an interactive GUI editor to toggle `justify-content`, `align-items`, and `gap` dynamically."
                )
            }
        ],
        code_snippets=[
            {
                "title": "The Stacking Context Trap Demonstrated",
                "language": "html",
                "code": (
                    "<!-- Stacking Context Trap: Parent A has opacity < 1, creating isolated context -->\n"
                    "<div class=\"parent-a\" style=\"position: relative; z-index: 1; opacity: 0.99;\">\n"
                    "  <!-- Child modal has huge z-index, but cannot escape Parent A's z-index of 1! -->\n"
                    "  <div class=\"modal\" style=\"position: absolute; z-index: 999999; background: red;\">\n"
                    "    Trapped Modal\n"
                    "  </div>\n"
                    "</div>\n\n"
                    "<!-- Parent B renders on TOP because its z-index (2) beats Parent A (1) -->\n"
                    "<div class=\"parent-b\" style=\"position: relative; z-index: 2; background: blue;\">\n"
                    "  Header renders above the modal!\n"
                    "</div>"
                ),
                "explanation": "Illustrates why high z-index values fail when trapped inside a lower parent stacking context."
            },
            {
                "title": "Fixing the Stacking Trap with React Portals / Body Appending",
                "language": "html",
                "code": (
                    "<!-- Solution: Mount modals directly to <body> to escape nested contexts -->\n"
                    "<body>\n"
                    "  <div class=\"app-root\">...</div>\n"
                    "  <!-- Modal mounted at top level of DOM, competing on root stacking context -->\n"
                    "  <div class=\"modal-portal\" style=\"position: fixed; z-index: 1000; inset: 0;\">\n"
                    "    Free Unconstrained Modal\n"
                    "  </div>\n"
                    "</body>"
                ),
                "explanation": "Mounting modals at document root avoids isolated stacking context boundaries."
            },
            {
                "title": "DOM Mutation Breakpoint Trigger in JavaScript",
                "language": "javascript",
                "code": (
                    "// DevTools 'Break on -> Attribute Modifications' set on <div id='target'>\n"
                    "const target = document.getElementById('target');\n\n"
                    "// The moment this line executes, DevTools pauses execution\n"
                    "// and highlights this exact line in the Sources panel!\n"
                    "target.classList.add('is-active');"
                ),
                "explanation": "Demonstrates how DOM mutation breakpoints automatically reveal the culprit JavaScript line."
            },
            {
                "title": "Inspecting CSS Grid and Flexbox Overlays",
                "language": "css",
                "code": (
                    "/* In DevTools Elements panel, clicking the 'grid' badge */\n"
                    "/* reveals explicit track lines, line numbers, and gap gutters */\n"
                    ".gallery-grid {\n"
                    "  display: grid;\n"
                    "  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));\n"
                    "  gap: 1.5rem;\n"
                    "}"
                ),
                "explanation": "Interactive DevTools badges render visual guides illustrating track dimensions and alignments."
            }
        ],
        coding_challenge={
            "title": "Simulate Stacking Context Z-Index Comparator",
            "instructions": "Write a function `resolve_z_order(element_a, element_b)` where each element is a dict `{'parent_z': int, 'child_z': int}`. If their parent stacking contexts differ (`parent_z`), the element with higher `parent_z` wins. If parents are equal, the element with higher `child_z` wins. Return `'A'` or `'B'`.",
            "starter_code": (
                "def resolve_z_order(elem_a: dict, elem_b: dict) -> str:\n"
                "    # Return 'A' or 'B' depending on which renders on top\n"
                "    pass\n"
            ),
            "solution_code": (
                "def resolve_z_order(elem_a: dict, elem_b: dict) -> str:\n"
                "    if elem_a['parent_z'] != elem_b['parent_z']:\n"
                "        return 'A' if elem_a['parent_z'] > elem_b['parent_z'] else 'B'\n"
                "    return 'A' if elem_a['child_z'] >= elem_b['child_z'] else 'B'\n\n"
                "a = {'parent_z': 1, 'child_z': 999999}\n"
                "b = {'parent_z': 2, 'child_z': 5}\n"
                "print(resolve_z_order(a, b))"
            ),
            "expected_output": "B"
        },
        quizzes=[
            {
                "question": "What is a 'DOM Mutation Breakpoint' in Browser DevTools?",
                "options": [
                    "A breakpoint that pauses JavaScript execution the instant a script modifies an element's attributes, children, or deletes it",
                    "A tool that prevents websites from rendering CSS",
                    "A hardware failure in the browser engine",
                    "A security vulnerability in HTML5"
                ],
                "correct_answer": "A breakpoint that pauses JavaScript execution the instant a script modifies an element's attributes, children, or deletes it",
                "explanation": "DOM mutation breakpoints catch the exact JavaScript line responsible for DOM changes."
            },
            {
                "question": "Why does setting `z-index: 999999;` on a modal sometimes fail to place it above a header with `z-index: 2;`?",
                "options": [
                    "Because the modal is trapped inside a parent element with a lower stacking context (e.g. parent has `z-index: 1`), which limits child priority",
                    "Because browsers only support z-index values up to 100",
                    "Because z-index requires JavaScript to work",
                    "Because z-index is deprecated in modern CSS"
                ],
                "correct_answer": "Because the modal is trapped inside a parent element with a lower stacking context (e.g. parent has `z-index: 1`), which limits child priority",
                "explanation": "Z-index is scoped to its local stacking context; child elements cannot outrank a superior parent context."
            },
            {
                "question": "Which of the following CSS properties can unintentionally create a new Stacking Context on a parent element?",
                "options": [
                    "`opacity < 1`, `transform`, or `filter`",
                    "`color: red`",
                    "`font-size: 16px`",
                    "`text-align: center`"
                ],
                "correct_answer": "`opacity < 1`, `transform`, or `filter`",
                "explanation": "Opacity, transform, filter, and will-change isolate elements into new stacking contexts."
            },
            {
                "question": "How do UI libraries (like React Portals) avoid the Stacking Context trap for modals and tooltips?",
                "options": [
                    "By rendering the modal HTML node directly into `document.body`, escaping nested parent stacking contexts",
                    "By setting the modal's opacity to zero",
                    "By running JavaScript inside web workers",
                    "By converting the modal into an SVG image"
                ],
                "correct_answer": "By rendering the modal HTML node directly into `document.body`, escaping nested parent stacking contexts",
                "explanation": "Portals mount overlays at the top level of the document body where they compete at the root context."
            },
            {
                "question": "What feature in modern browser DevTools helps debug CSS Flexbox and Grid layouts visually?",
                "options": [
                    "Interactive 'flex' and 'grid' badges that draw visual alignment guides and track lines directly on the webpage",
                    "A text-to-speech engine",
                    "An automatic CSS compiler",
                    "A button that reboots the browser"
                ],
                "correct_answer": "Interactive 'flex' and 'grid' badges that draw visual alignment guides and track lines directly on the webpage",
                "explanation": "DevTools badges overlay visual grid lines and flexbox alignments directly onto the page."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 29: Network Panel (API Requests, Responses & Timing)
    # ---------------------------------------------------------
    DayBlueprint(
        order=29,
        title="Day 29: Network Panel (API Requests, Responses & Timing)",
        concept="The DevTools Network Panel logs every HTTP asset and API transaction exchanged between browser and server, providing diagnostic inspection of headers, payloads, status codes, and timing waterfalls.",
        analogy="The Network Panel is like the package tracking and x-ray scanner at a shipping distribution center. For every package sent across the wire, it shows the exact sender address, destination, box dimensions, shipping label (headers), contents (payload), and delivery delay breakdown.",
        theory_sections=[
            {
                "heading": "Anatomy of the Network Panel",
                "content": (
                    "When investigating frontend API failures:\n"
                    "- **Filter Bar**: Filter by request type: **Fetch/XHR** (AJAX/API calls), **JS**, **CSS**, **Img**, **WS** (WebSockets).\n"
                    "- **Status Column**: Highlights HTTP `200` (green), `304` (cached), `401`/`403`/`404` (red), `500` (server error).\n"
                    "- **Preserve Log Checkbox**: Keeps network history across full page reloads and redirects (essential for debugging OAuth or login flows)."
                )
            },
            {
                "heading": "Inspecting Individual Requests",
                "content": (
                    "Clicking on any request row opens detailed sub-tabs:\n"
                    "1. **Headers**: Request URL, HTTP Method, Status Code, and all Request/Response headers (CORS headers, Authorization tokens).\n"
                    "2. **Payload**: The query parameters or JSON request body sent by the browser.\n"
                    "3. **Response**: Raw JSON, HTML, or binary data returned by the server.\n"
                    "4. **Timing**: Waterfall breakdown: DNS Lookup, Initial Connection (TCP/TLS handshake), TTFB (Time to First Byte / server wait time), and Content Download."
                )
            },
            {
                "heading": "Network Throttling & Offline Simulation",
                "content": (
                    "Most developers build apps on high-speed fiber internet. The Network panel dropdown lets you simulate real-world conditions:\n"
                    "- **Fast 3G / Slow 3G**: Tests loading spinners, skeleton screens, and timeout recovery.\n"
                    "- **Offline**: Simulates disconnection to test PWA service workers and error boundaries."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Copying Request as cURL from DevTools",
                "language": "bash",
                "code": (
                    "# DevTools Superpower: Right-click any failed request in Network Panel\n"
                    "# -> Copy -> Copy as cURL\n"
                    "# Paste directly into terminal to reproduce outside the browser!\n"
                    "curl 'https://api.example.com/v1/orders' \\\n"
                    "  -H 'Authorization: Bearer eyJhbGciOi...' \\\n"
                    "  -H 'Content-Type: application/json' \\\n"
                    "  --data-raw '{\"item_id\":42}'"
                ),
                "explanation": "'Copy as cURL' captures identical headers and cookies, enabling instant backend reproduction."
            },
            {
                "title": "Diagnosing High TTFB (Time To First Byte)",
                "language": "text",
                "code": (
                    "Analyzing Network Timing Waterfall:\n"
                    "- Queueing: 1.2ms (Browser waiting for connection pool)\n"
                    "- DNS Lookup: 15ms\n"
                    "- Initial Connection (TLS): 45ms\n"
                    "- Waiting for Server Response (TTFB): 2800ms  <-- SLOW BOTTLENECK!\n"
                    "- Content Download: 4ms\n\n"
                    "Diagnosis: Network is fast; the backend SQL query took 2.8 seconds!"
                ),
                "explanation": "Timing breakdowns isolate whether latency is caused by network transmission or backend processing."
            },
            {
                "title": "Simulating Slow Networks Programmatically",
                "language": "javascript",
                "code": (
                    "// Test timeout behavior in client code\n"
                    "async function fetchWithTimeout(url, timeoutMs = 3000) {\n"
                    "  const controller = new AbortController();\n"
                    "  const timer = setTimeout(() => controller.abort(), timeoutMs);\n"
                    "  try {\n"
                    "    const res = await fetch(url, { signal: controller.signal });\n"
                    "    return await res.json();\n"
                    "  } catch (err) {\n"
                    "    if (err.name === 'AbortError') throw new Error('Request timed out');\n"
                    "    throw err;\n"
                    "  } finally {\n"
                    "    clearTimeout(timer);\n"
                    "  }\n"
                    "}"
                ),
                "explanation": "Client-side timeout handling testable via DevTools network throttling."
            },
            {
                "title": "Checking CORS Preflight in Network Panel",
                "language": "text",
                "code": (
                    "Spotting CORS Failures:\n"
                    "1. Look for an OPTIONS request preceding your POST/PUT request.\n"
                    "2. If the OPTIONS request returns red status (403 or missing headers),\n"
                    "   the browser refuses to dispatch the actual POST request!\n"
                    "3. Check response headers for: Access-Control-Allow-Origin"
                ),
                "explanation": "Preflight failures in the Network tab explain missing API dispatches."
            }
        ],
        coding_challenge={
            "title": "Parse Network Timing Metrics",
            "instructions": "Write a function `analyze_waterfall(timings_dict)` that takes a dictionary with keys `'dns'`, `'tls'`, `'ttfb'`, and `'download'` (in milliseconds). Return a dictionary with `'total_latency'` (sum of all 4) and `'primary_bottleneck'` (the key with the highest value).",
            "starter_code": (
                "def analyze_waterfall(timings: dict) -> dict:\n"
                "    # Return {'total_latency': ..., 'primary_bottleneck': ...}\n"
                "    pass\n"
            ),
            "solution_code": (
                "def analyze_waterfall(timings: dict) -> dict:\n"
                "    total = sum(timings.values())\n"
                "    bottleneck = max(timings.items(), key=lambda x: x[1])[0]\n"
                "    return {'total_latency': total, 'primary_bottleneck': bottleneck}\n\n"
                "metrics = {'dns': 12, 'tls': 40, 'ttfb': 1500, 'download': 8}\n"
                "print(analyze_waterfall(metrics))"
            ),
            "expected_output": "{'total_latency': 1560, 'primary_bottleneck': 'ttfb'}"
        },
        quizzes=[
            {
                "question": "What does 'TTFB' stand for in the Network panel timing waterfall?",
                "options": [
                    "Time to First Byte",
                    "Total Time for Bandwidth",
                    "Target Thread Frequency Buffer",
                    "Transmission Type Flag Byte"
                ],
                "correct_answer": "Time to First Byte",
                "explanation": "TTFB measures the latency from the request dispatch until the first byte of response arrives."
            },
            {
                "question": "Why is the 'Preserve Log' checkbox in the Network panel essential when debugging login or checkout flows?",
                "options": [
                    "It keeps previous network requests visible in the panel across page redirects and page reloads",
                    "It saves logs to your local hard drive automatically",
                    "It prevents the browser from using cache memory",
                    "It encrypts sensitive credit card numbers"
                ],
                "correct_answer": "It keeps previous network requests visible in the panel across page redirects and page reloads",
                "explanation": "Redirects normally clear the network log; Preserve Log maintains diagnostic history across pages."
            },
            {
                "question": "How can you instantly reproduce a failing browser API call in your local terminal?",
                "options": [
                    "Right-click the request in the Network panel and select 'Copy as cURL'",
                    "Type `curl current_tab` in the terminal",
                    "Take a screenshot and paste it into Bash",
                    "Reboot the router"
                ],
                "correct_answer": "Right-click the request in the Network panel and select 'Copy as cURL'",
                "explanation": "Copy as cURL exports the exact headers, cookies, and body into a command-line executable string."
            },
            {
                "question": "Which tab in the request details panel displays the JSON data sent by the browser to the backend?",
                "options": [
                    "Payload (or Request Body)",
                    "Cookies",
                    "Preview",
                    "Initiator"
                ],
                "correct_answer": "Payload (or Request Body)",
                "explanation": "The Payload tab shows outgoing query strings or POST/PUT request bodies."
            },
            {
                "question": "If a Network request has a TTFB of 4,000ms while DNS and download times are under 10ms, where is the performance bottleneck?",
                "options": [
                    "On the backend server (slow database query, locking, or heavy backend processing)",
                    "On the client's Wi-Fi router",
                    "In the client's CSS stylesheet",
                    "In the client's monitor refresh rate"
                ],
                "correct_answer": "On the backend server (slow database query, locking, or heavy backend processing)",
                "explanation": "High TTFB indicates the server received the request quickly but spent 4 seconds processing before responding."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 30: Application / Storage Panel (Cookies & LocalStorage)
    # ---------------------------------------------------------
    DayBlueprint(
        order=30,
        title="Day 30: Application / Storage Panel (Cookies & LocalStorage)",
        concept="The Application panel audits client-side persistence layers—LocalStorage, SessionStorage, IndexedDB, and HTTP Cookies—to diagnose authentication desyncs, expired sessions, and storage quotas.",
        analogy="The Application panel is like inspecting the glove compartment and trunk of a car. You can check what parking permits (cookies) are taped to the windshield, what tools (LocalStorage) are kept in the glove box, and empty out expired junk that is weighing down the vehicle.",
        theory_sections=[
            {
                "heading": "Client-Side Storage Mechanisms Compared",
                "content": (
                    "Modern browsers provide 4 distinct persistence layers:\n"
                    "1. **Cookies**: Small strings ($\le$ 4KB) sent with *every* HTTP request. Configured with flags: `HttpOnly` (inaccessible to JS), `Secure` (HTTPS only), `SameSite` (CSRF defense).\n"
                    "2. **LocalStorage**: Key-value string storage ($\approx$ 5-10MB). Persists forever across tab and browser restarts until cleared.\n"
                    "3. **SessionStorage**: Key-value storage scoped strictly to the lifetime of a **single browser tab**.\n"
                    "4. **IndexedDB**: Full client-side NoSQL transactional database for offline data storage."
                )
            },
            {
                "heading": "Debugging Session and Auth Bugs in DevTools",
                "content": (
                    "When users report *'I logged in, but the dashboard redirects me back to login immediately'*, open **Application -> Storage**:\n"
                    "- Are `auth_token` or `session_id` present in Cookies or LocalStorage?\n"
                    "- Check cookie **Expires / Max-Age**: Is the cookie already expired due to client/server clock skew?\n"
                    "- Check cookie **Domain** and **Path**: Is the cookie scoped to `api.domain.com` while the user is on `app.domain.com`?"
                )
            },
            {
                "heading": "The 'Clear Site Data' Superpower",
                "content": (
                    "When an application gets stuck in a corrupted client state, the **Clear site data** button under the Application tab nukes Cookies, LocalStorage, IndexedDB, Cache Storage, and Service Workers with 1 click, resetting the browser to pristine clean-install state."
                )
            }
        ],
        code_snippets=[
            {
                "title": "LocalStorage Interaction and Serialization",
                "language": "javascript",
                "code": (
                    "// LocalStorage ONLY stores strings! Common beginner trap:\n"
                    "const session = { userId: 101, token: 'abc' };\n"
                    "// BUG: localStorage.setItem('session', session); -> stores '[object Object]'!\n\n"
                    "// FIX: Explicit JSON serialization\n"
                    "localStorage.setItem('session', JSON.stringify(session));\n\n"
                    "// Safe deserialization\n"
                    "const raw = localStorage.getItem('session');\n"
                    "const savedSession = raw ? JSON.parse(raw) : null;"
                ),
                "explanation": "LocalStorage converts non-strings to `[object Object]` unless serialized via `JSON.stringify`."
            },
            {
                "title": "Inspecting Cookies via JavaScript vs `HttpOnly`",
                "language": "javascript",
                "code": (
                    "// document.cookie only shows cookies WITHOUT HttpOnly flag\n"
                    "console.log('Client-accessible cookies:', document.cookie);\n\n"
                    "// Secure auth cookies marked 'HttpOnly' by backend CANNOT be read by JS!\n"
                    "// To inspect HttpOnly cookies, you MUST use the DevTools Application panel."
                ),
                "explanation": "`HttpOnly` cookies are invisible to JavaScript for XSS defense; DevTools reveals them directly."
            },
            {
                "title": "Handling Storage Quota Exceeded Errors",
                "language": "javascript",
                "code": (
                    "function safeSetLocalStorage(key, val) {\n"
                    "  try {\n"
                    "    localStorage.setItem(key, val);\n"
                    "  } catch (err) {\n"
                    "    if (err.name === 'QuotaExceededError') {\n"
                    "      console.warn('LocalStorage full! Evicting old cache keys...');\n"
                    "      localStorage.removeItem('old_cache_key');\n"
                    "      localStorage.setItem(key, val);\n"
                    "    }\n"
                    "  }\n"
                    "}"
                ),
                "explanation": "Guards against `QuotaExceededError` when client storage reaches capacity."
            },
            {
                "title": "Storage Panel DevTools Navigation",
                "language": "text",
                "code": (
                    "DevTools Application Tab Layout:\n"
                    "- Storage -> Clear site data (Master Reset)\n"
                    "- LocalStorage -> https://app.example.com (Inspect key/value pairs)\n"
                    "- SessionStorage -> https://app.example.com (Tab-isolated storage)\n"
                    "- Cookies -> https://app.example.com (Inspect HttpOnly, Secure, SameSite, Expiry)"
                ),
                "explanation": "Navigational map of client storage diagnostic views."
            }
        ],
        coding_challenge={
            "title": "Simulate Cookie Parser and Expiry Checker",
            "instructions": "Write a function `parse_and_filter_cookies(cookie_header, current_timestamp)` that takes a list of cookie dictionaries `[{'name': 'token', 'val': 'xyz', 'expires': 1000}]` and returns a dictionary of `{name: val}` for only those cookies where `expires > current_timestamp`.",
            "starter_code": (
                "def parse_and_filter_cookies(cookies: list, now: float) -> dict:\n"
                "    # Return unexpired cookies dictionary\n"
                "    pass\n"
            ),
            "solution_code": (
                "def parse_and_filter_cookies(cookies: list, now: float) -> dict:\n"
                "    valid = {}\n"
                "    for c in cookies:\n"
                "        if c.get('expires', 0) > now:\n"
                "            valid[c['name']] = c['val']\n"
                "    return valid\n\n"
                "cookie_jar = [\n"
                "    {'name': 'session', 'val': 'abc123', 'expires': 1500},\n"
                "    {'name': 'tracking', 'val': 'trk999', 'expires': 800}\n"
                "]\n"
                "print(parse_and_filter_cookies(cookie_jar, now=1000))"
            ),
            "expected_output": "{'session': 'abc123'}"
        },
        quizzes=[
            {
                "question": "What is the primary difference between LocalStorage and SessionStorage?",
                "options": [
                    "LocalStorage persists across browser restarts; SessionStorage is wiped clean as soon as the browser tab is closed",
                    "SessionStorage is stored on the server",
                    "LocalStorage can only store numbers",
                    "SessionStorage has unlimited capacity"
                ],
                "correct_answer": "LocalStorage persists across browser restarts; SessionStorage is wiped clean as soon as the browser tab is closed",
                "explanation": "SessionStorage is scoped strictly to the tab lifecycle; LocalStorage survives tab and browser restarts."
            },
            {
                "question": "Why can't you inspect an `HttpOnly` authentication cookie by typing `document.cookie` in the Console tab?",
                "options": [
                    "`HttpOnly` cookies are explicitly blocked from JavaScript access to protect against token theft via Cross-Site Scripting (XSS)",
                    "Because `document.cookie` is deprecated",
                    "Because `HttpOnly` cookies are stored on disk as binary images",
                    "Because the browser deletes them after login"
                ],
                "correct_answer": "`HttpOnly` cookies are explicitly blocked from JavaScript access to protect against token theft via Cross-Site Scripting (XSS)",
                "explanation": "HttpOnly prevents malicious JavaScript from reading session cookies during XSS attacks."
            },
            {
                "question": "Where in Browser DevTools can you view, edit, and delete `HttpOnly` cookies?",
                "options": [
                    "In the Application panel under Storage -> Cookies",
                    "In the Console tab",
                    "In the Sources panel",
                    "In the Memory panel"
                ],
                "correct_answer": "In the Application panel under Storage -> Cookies",
                "explanation": "The DevTools Application panel has privileged browser access to inspect all cookies."
            },
            {
                "question": "What happens if you store an object directly in LocalStorage with `localStorage.setItem('user', { id: 1 })`?",
                "options": [
                    "It is implicitly coerced into the string `\"[object Object]\"`, corrupting the data",
                    "It is automatically serialized into JSON",
                    "A TypeError is thrown",
                    "The object is uploaded to Google Drive"
                ],
                "correct_answer": "It is implicitly coerced into the string `\"[object Object]\"`, corrupting the data",
                "explanation": "LocalStorage calls `toString()` on non-strings, yielding `'[object Object]'`; use `JSON.stringify`."
            },
            {
                "question": "What does the 'Clear site data' button in the Application panel accomplish?",
                "options": [
                    "It wipes all Cookies, LocalStorage, SessionStorage, IndexedDB, and Cache Storage for that origin with one click",
                    "It uninstalls the web browser",
                    "It formats the computer's hard drive",
                    "It deletes your GitHub account"
                ],
                "correct_answer": "It wipes all Cookies, LocalStorage, SessionStorage, IndexedDB, and Cache Storage for that origin with one click",
                "explanation": "Clear Site Data resets all client-side persistence for the domain to clean-install state."
            }
        ]
    )
]
