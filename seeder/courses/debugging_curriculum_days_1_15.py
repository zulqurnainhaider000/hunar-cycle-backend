"""
debugging_curriculum_days_1_15.py
Days 1 to 15 for Debugging & Problem Solving 60-Day Course.
Covers:
- Module 1: Problem Solving Fundamentals & Mindset (Days 1-6)
- Module 2: Basic Debugging Strategies (Days 7-12)
- Module 3: Reading Errors & Exception Handling (Days 13-15)
"""

from seeder.course_blueprint import DayBlueprint

DAYS_1_TO_15 = [
    # ---------------------------------------------------------
    # Day 1: Introduction to Debugging (What is a Bug and Why It Happens)
    # ---------------------------------------------------------
    DayBlueprint(
        order=1,
        title="Day 1: Introduction to Debugging (What is a Bug and Why It Happens)",
        concept="Debugging is the systematic, scientific process of identifying, isolating, and rectifying defects (bugs) that cause computer software to behave unexpectedly or crash.",
        analogy="Think of code like baking a cake from a recipe. If the recipe says 'add 1 cup of sugar' but you accidentally poured 1 cup of salt, the cake looks fine on the outside, but one bite makes everyone gag. Debugging is tasting the batter, reading the recipe step-by-step, finding the salt jar with the sugar label, and replacing it with real sugar.",
        theory_sections=[
            {
                "heading": "The Origin of the 'Bug' and Software Defects",
                "content": (
                    "In 1947, computer pioneer Admiral Grace Hopper found an actual moth trapped between relays of the Harvard Mark II computer, disrupting calculations. She taped the moth into the logbook with the notation: 'First actual case of bug being found.'\n\n"
                    "Today, a **software bug** is not an insect. It is a flaw, failure, or fault in a computer program that produces an incorrect or unexpected result, or causes it to behave in unintended ways. Debugging is not random guessing; it is the **scientific method applied to software**: observation, hypothesis, experiment, analysis, and fix."
                )
            },
            {
                "heading": "Why Bugs Happen in Modern Systems",
                "content": (
                    "Bugs are inevitable whenever humans translate ambiguous human requirements into rigid binary instructions. Primary causes include:\n"
                    "1. **Mismatched Assumptions**: Expecting a user to enter an integer age, but they submit `'twenty-one'`.\n"
                    "2. **Off-by-One Errors**: Looping `< length` instead of `<= length` or 0-indexed vs 1-indexed mismatches.\n"
                    "3. **State Corruption**: Global variables being modified unexpectedly across concurrent routines.\n"
                    "4. **Implicit Type Coercion**: In languages like JavaScript, `5 + '5'` becomes `'55'` instead of `10`."
                )
            },
            {
                "heading": "The Scientific Debugging Cycle",
                "content": (
                    "Effective engineers follow a rigorous 5-step loop:\n"
                    "1. **Observe**: Accurately note what happened vs what was expected.\n"
                    "2. **Reproduce**: Create a minimal deterministic scenario that reliably triggers the defect.\n"
                    "3. **Formulate Hypothesis**: Dedicate mental effort to asking *'Why could this state exist?'*\n"
                    "4. **Test Hypothesis**: Use logs, debuggers, or assertions to confirm or disprove the theory.\n"
                    "5. **Implement Fix & Regression Test**: Resolve the root cause and write an automated test ensuring it never returns."
                )
            }
        ],
        code_snippets=[
            {
                "title": "A Classic Type Coercion Bug in Python",
                "language": "python",
                "code": (
                    "# Bug: input() returns a string, leading to string concatenation instead of math\n"
                    "price = input('Enter item price: ')  # user enters: 100\n"
                    "tax = price * 0.15                  # TypeError: can't multiply sequence by non-int of type 'float'\n"
                    "print(f'Total: {price + tax}')"
                ),
                "explanation": "Variables from user inputs or web forms are strings; without explicit casting, runtime errors or semantic bugs occur."
            },
            {
                "title": "The Fixed & Defensively Parsed Code",
                "language": "python",
                "code": (
                    "raw_price = input('Enter item price: ')\n"
                    "try:\n"
                    "    price = float(raw_price)\n"
                    "    tax = price * 0.15\n"
                    "    print(f'Total: ${price + tax:.2f}')\n"
                    "except ValueError:\n"
                    "    print(f'Error: \"{raw_price}\" is not a valid numeric price!')"
                ),
                "explanation": "Defensive conversion with exception handling catches invalid input gracefully before mathematical operations."
            },
            {
                "title": "A Subtle JavaScript Truthy / Falsy Bug",
                "language": "javascript",
                "code": (
                    "function calculateDiscount(user) {\n"
                    "  // BUG: If discountPercentage is 0, JavaScript treats 0 as falsy!\n"
                    "  // It falls back to default 10%, giving customers unintended discounts!\n"
                    "  const discount = user.discountPercentage || 10;\n"
                    "  return discount;\n"
                    "}\n\n"
                    "console.log(calculateDiscount({ discountPercentage: 0 })); // Prints 10, expected 0!"
                ),
                "explanation": "Using logical OR `||` for default fallback fails when `0` or `false` is a legitimate value; use nullish coalescing `??` instead."
            },
            {
                "title": "Fixing the Falsy Bug with Nullish Coalescing (`??`)",
                "language": "javascript",
                "code": (
                    "function calculateDiscount(user) {\n"
                    "  // FIX: ?? only triggers on null or undefined, preserving 0\n"
                    "  const discount = user.discountPercentage ?? 10;\n"
                    "  return discount;\n"
                    "}\n\n"
                    "console.log(calculateDiscount({ discountPercentage: 0 })); // Prints 0"
                ),
                "explanation": "Modern JavaScript nullish coalescing checks specifically for null or undefined, avoiding zero-coercion bugs."
            }
        ],
        coding_challenge={
            "title": "Fix the Shopping Cart Total Bug",
            "instructions": "The `calculate_cart_total` function has a bug where item prices stored as strings cause string multiplication or runtime crashes. Fix the function so it safely converts prices to floats and sums them accurately.",
            "starter_code": (
                "def calculate_cart_total(items: list) -> float:\n"
                "    # BUGGY CODE: items is a list of dicts [{'name': 'Book', 'price': '15.50'}]\n"
                "    total = 0\n"
                "    for item in items:\n"
                "        total += item['price']  # Crashes if price is string or adds strings\n"
                "    return total\n"
            ),
            "solution_code": (
                "def calculate_cart_total(items: list) -> float:\n"
                "    total = 0.0\n"
                "    for item in items:\n"
                "        total += float(item['price'])\n"
                "    return round(total, 2)\n\n"
                "cart = [{'name': 'Book', 'price': '15.50'}, {'name': 'Pen', 'price': '2.50'}]\n"
                "print(calculate_cart_total(cart))"
            ),
            "expected_output": "18.0"
        },
        quizzes=[
            {
                "question": "What is the primary definition of a software bug?",
                "options": [
                    "A flaw or defect in code that causes it to produce incorrect output, crash, or behave unexpectedly",
                    "A physical insect that eats computer silicon chips",
                    "A feature requested by marketing that engineers refuse to build",
                    "A compiler that runs too slowly"
                ],
                "correct_answer": "A flaw or defect in code that causes it to produce incorrect output, crash, or behave unexpectedly",
                "explanation": "A bug is any defect or flaw in a computer system that produces unintended behavior or failure."
            },
            {
                "question": "Which historic pioneer coined the term 'debugging' after finding a real moth in the Harvard Mark II relay?",
                "options": [
                    "Grace Hopper",
                    "Alan Turing",
                    "Ada Lovelace",
                    "Linus Torvalds"
                ],
                "correct_answer": "Grace Hopper",
                "explanation": "Admiral Grace Hopper and her team taped a moth into their relay logbook in 1947, popularizing the term."
            },
            {
                "question": "What is the very first step in the scientific debugging process?",
                "options": [
                    "Observe and reproduce the defect consistently",
                    "Immediately start editing random lines of code",
                    "Delete the git repository and re-clone",
                    "Blame the hardware vendor"
                ],
                "correct_answer": "Observe and reproduce the defect consistently",
                "explanation": "You cannot reliably fix what you cannot reproduce and observe."
            },
            {
                "question": "In Python, what happens when you evaluate `'50' + 10`?",
                "options": [
                    "A TypeError is raised because Python does not implicitly coerce strings to integers",
                    "It automatically returns 60",
                    "It returns '5010'",
                    "It returns None"
                ],
                "correct_answer": "A TypeError is raised because Python does not implicitly coerce strings to integers",
                "explanation": "Python is strongly typed and refuses to implicitly add integers to strings."
            },
            {
                "question": "Why is random 'trial-and-error' guessing dangerous when debugging complex software?",
                "options": [
                    "It often introduces secondary side-effect bugs while masking the true root cause",
                    "It consumes zero CPU cycles",
                    "Compilers detect guessing and refuse to build",
                    "It is illegal under software copyright laws"
                ],
                "correct_answer": "It often introduces secondary side-effect bugs while masking the true root cause",
                "explanation": "Guessing treats symptoms rather than root causes and frequently creates hidden regression bugs."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 2: The Developer Mindset (Logic Over Panic)
    # ---------------------------------------------------------
    DayBlueprint(
        order=2,
        title="Day 2: The Developer Mindset (Logic Over Panic)",
        concept="Effective debugging requires emotional composure, cognitive resilience, and objective evidence-based investigation rather than frustration, panic, or guesswork.",
        analogy="When a medical doctor hears a patient wheezing in the ER, they do not scream, hyperventilate, or guess randomly. They check vitals, order an X-ray, isolate symptoms, and systematically diagnose the illness. A senior developer debugging a production outage operates like an ER surgeon.",
        theory_sections=[
            {
                "heading": "The Psychology of Debugging",
                "content": (
                    "When production breaks or code fails after 4 hours of effort, the human brain triggers the amygdala: fight-or-flight, elevated heart rate, and tunnel vision. This leads to common cognitive traps:\n"
                    "- **Confirmation Bias**: Assuming *'My code is definitely right, so the library or framework must be broken.'*\n"
                    "- **Shotgun Debugging**: Rapidly changing 15 different lines across 4 files hoping something works, leaving a mess of uncommitted broken state.\n"
                    "- **Tunnel Vision**: Staring at a single function for 3 hours when the bug was actually in the database connection string."
                )
            },
            {
                "heading": "The 3 Golden Rules of Debugging Composure",
                "content": (
                    "1. **Assume Nothing, Verify Everything**: If you believe a variable is `5`, prove it with an assertion, print statement, or debugger inspection.\n"
                    "2. **Change One Variable at a Time**: When testing hypotheses, alter exactly one factor. If you change 3 things at once, you will never know which one solved or caused the problem.\n"
                    "3. **Take a Bio-Break**: When stuck for over 45 minutes, cognitive fatigue sets in. Stepping away for 10 minutes allows your subconscious 'diffuse mode' thinking to spot obvious oversights."
                )
            },
            {
                "heading": "Separating Facts from Assumptions",
                "content": (
                    "Write down two columns on a notepad:\n"
                    "- **Facts (What I know with certainty)**: *'The HTTP response is 404. The URL requested is `/api/v1/users`. The server is running on port 8000.'*\n"
                    "- **Assumptions (What I believe but haven't proven)**: *'The route was registered in FastAPI. The router was imported in `app.py`.'*\n"
                    "90% of bugs live in the gap between what you assume and what you have verified."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Verifying Assumptions with Defensive Assertions",
                "language": "python",
                "code": (
                    "def transfer_funds(account_from, account_to, amount):\n"
                    "    # Verify assumptions immediately at function boundary\n"
                    "    assert amount > 0, f'Transfer amount must be positive, got {amount}'\n"
                    "    assert account_from['balance'] >= amount, 'Insufficient funds'\n"
                    "    \n"
                    "    account_from['balance'] -= amount\n"
                    "    account_to['balance'] += amount"
                ),
                "explanation": "Assertions enforce expected invariants early before state corruption propagates downstream."
            },
            {
                "title": "Shotgun Debugging Antipattern (What NOT to do)",
                "language": "python",
                "code": (
                    "# ANTIPATTERN: Changing random lines frantically\n"
                    "# Maybe if I cast this to str?\n"
                    "# Maybe if I add + 1?\n"
                    "# Maybe if I wrap everything in try/except pass?\n"
                    "try:\n"
                    "    val = str(int(data.get('count', 0)) + 1)\n"
                    "except Exception:\n"
                    "    val = 0  # Swallows the real bug silently!\n"
                    "# Result: Nobody knows why the app produces wrong numbers"
                ),
                "explanation": "Swallowing exceptions with empty `except` blocks masks bugs, making root cause analysis impossible."
            },
            {
                "title": "Isolating the Single Variable Under Test",
                "language": "python",
                "code": (
                    "# Scientific test harness isolating single transformation\n"
                    "def sanitize_username(raw: str) -> str:\n"
                    "    return raw.strip().lower().replace(' ', '_')\n\n"
                    "# Test single hypothesis directly in REPL or test harness\n"
                    "print(f'Test empty: {repr(sanitize_username(\"\"))}')\n"
                    "print(f'Test spaces: {repr(sanitize_username(\"  Alice Bob  \"))}')"
                ),
                "explanation": "Testing isolated helper inputs one at a time exposes boundary failures systematically."
            },
            {
                "title": "Logging State vs Staring at Code",
                "language": "python",
                "code": (
                    "import logging\n"
                    "logging.basicConfig(level=logging.DEBUG)\n\n"
                    "def parse_payload(payload):\n"
                    "    logging.debug('Input payload type: %s, keys: %s', type(payload), getattr(payload, 'keys', None))\n"
                    "    # Now you know the real runtime shape instead of guessing"
                ),
                "explanation": "Inspecting runtime shape provides hard facts, neutralizing false assumptions."
            }
        ],
        coding_challenge={
            "title": "Verify Invariants with an Assumption Checker",
            "instructions": "Write a function `validate_user_state(user)` that checks: `user` is a dict, has `'id'` (integer > 0), has non-empty `'username'`, and `'role'` is in `['admin', 'member']`. Raise `ValueError` with a clear explanation if any assumption fails, otherwise return True.",
            "starter_code": (
                "def validate_user_state(user: dict) -> bool:\n"
                "    # BUG: Does no validation, assumes perfect user state\n"
                "    return True\n"
            ),
            "solution_code": (
                "def validate_user_state(user: dict) -> bool:\n"
                "    if not isinstance(user, dict):\n"
                "        raise ValueError('User must be a dictionary')\n"
                "    if not isinstance(user.get('id'), int) or user['id'] <= 0:\n"
                "        raise ValueError('User id must be a positive integer')\n"
                "    if not user.get('username') or not str(user['username']).strip():\n"
                "        raise ValueError('Username must not be empty')\n"
                "    if user.get('role') not in ('admin', 'member'):\n"
                "        raise ValueError('Role must be admin or member')\n"
                "    return True\n\n"
                "print(validate_user_state({'id': 1, 'username': 'sam', 'role': 'member'}))"
            ),
            "expected_output": "True"
        },
        quizzes=[
            {
                "question": "What is 'Shotgun Debugging' and why is it considered an antipattern?",
                "options": [
                    "Randomly modifying multiple lines across files hoping something works, which creates hidden bugs and masks root causes",
                    "Using a terminal debugger like GDB",
                    "Debugging code using multiple monitors",
                    "Writing automated tests before coding"
                ],
                "correct_answer": "Randomly modifying multiple lines across files hoping something works, which creates hidden bugs and masks root causes",
                "explanation": "Shotgun debugging makes untracked, haphazard modifications without formulating a hypothesis."
            },
            {
                "question": "When debugging, what is the best rule regarding changing code variables?",
                "options": [
                    "Change only one variable or factor at a time so you know exactly which change affected the outcome",
                    "Change at least 10 lines at once to save time",
                    "Never change anything and wait for the computer to fix itself",
                    "Delete all functions and retype them from memory"
                ],
                "correct_answer": "Change only one variable or factor at a time so you know exactly which change affected the outcome",
                "explanation": "Isolating single variables is fundamental to the scientific debugging method."
            },
            {
                "question": "What is 'Confirmation Bias' in software debugging?",
                "options": [
                    "Assuming your code is flawless and blaming external factors (compiler, database, OS) without evidence",
                    "Requiring users to confirm their email address",
                    "Validating SSL certificates",
                    "Writing unit tests that pass"
                ],
                "correct_answer": "Assuming your code is flawless and blaming external factors (compiler, database, OS) without evidence",
                "explanation": "Confirmation bias leads developers to ignore their own logic errors while searching for external culprits."
            },
            {
                "question": "Why does taking a 10-15 minute walk or break help when you have been stuck on a bug for over an hour?",
                "options": [
                    "It breaks cognitive tunnel vision and allows subconscious 'diffuse mode' thinking to recognize simple oversights",
                    "It causes the operating system to clear memory leaks automatically",
                    "It gives other developers time to steal your code",
                    "It restarts the internet connection"
                ],
                "correct_answer": "It breaks cognitive tunnel vision and allows subconscious 'diffuse mode' thinking to recognize simple oversights",
                "explanation": "Mental fatigue creates fixation; stepping away resets working memory and perspective."
            },
            {
                "question": "What is the primary danger of wrapping suspect code in `try: ... except Exception: pass`?",
                "options": [
                    "It swallows errors silently, hiding bugs and leaving the application in a corrupted, unpredictable state",
                    "It doubles CPU clock frequency",
                    "It deletes source code files",
                    "It converts numbers to strings"
                ],
                "correct_answer": "It swallows errors silently, hiding bugs and leaving the application in a corrupted, unpredictable state",
                "explanation": "Silent exception swallowing destroys error visibility and corrupts application invariants."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 3: Algorithm Design: Step-by-Step Problem Solving
    # ---------------------------------------------------------
    DayBlueprint(
        order=3,
        title="Day 3: Algorithm Design: Step-by-Step Problem Solving",
        concept="Algorithm design breaks complex, ambiguous real-world requirements into finite, deterministic, and verifiable computational steps before any syntax is written.",
        analogy="Building software without an algorithm is like trying to assemble a 2,000-piece IKEA wardrobe without the assembly booklet. If you start randomly driving screws into wooden boards, you will end up with a wobbly heap and 12 leftover screws.",
        theory_sections=[
            {
                "heading": "What is an Algorithm?",
                "content": (
                    "An algorithm is a well-defined computational procedure that takes some value or set of values as **input** and produces some value or set of values as **output**. An algorithm must possess five essential properties:\n"
                    "1. **Finiteness**: It must terminate after a finite number of steps.\n"
                    "2. **Definiteness**: Each step must be clearly and unambiguously defined.\n"
                    "3. **Input**: Quantities specified from an external source.\n"
                    "4. **Output**: Quantities produced having a specific relation to inputs.\n"
                    "5. **Effectiveness**: Operations must be basic enough that they could theoretically be performed on paper."
                )
            },
            {
                "heading": "George Pólya’s 4-Step Problem-Solving Framework",
                "content": (
                    "Mathematician George Pólya defined a timeless framework used by top software engineers:\n"
                    "1. **Understand the Problem**: What are the inputs? What is the expected output? What are the constraints and edge cases (e.g. empty lists, negative numbers, null values)?\n"
                    "2. **Devise a Plan**: How do the data connect? Have you solved a similar problem before? Can you solve a simplified version first?\n"
                    "3. **Carry Out the Plan**: Write the code step-by-step. Verify each step as you execute it.\n"
                    "4. **Look Back (Reflect & Optimize)**: Can you check the result? Is there an edge case that could break it? Can you improve efficiency?"
                )
            },
            {
                "heading": "Why Poor Algorithm Design Causes Subtle Logic Bugs",
                "content": (
                    "Most production bugs are not syntax errors (compilers catch those instantly). They are **logic bugs** where the developer translated a flawed algorithm into code:\n"
                    "- Forgetting the terminating condition in recursion.\n"
                    "- Sorting strings alphabetically when numeric sorting was required (`['10', '2']` sorts to `['10', '2']` instead of `['2', '10']`).\n"
                    "- Assuming data is always sorted when receiving it from an API."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Problem: Finding the Maximum Value (Algorithmic Plan)",
                "language": "text",
                "code": (
                    "ALGORITHM FindMax(numbers):\n"
                    "  1. If numbers is empty -> Raise error (edge case)\n"
                    "  2. Set current_max to first element: numbers[0]\n"
                    "  3. For each num in numbers from index 1 to end:\n"
                    "       If num > current_max:\n"
                    "         Set current_max = num\n"
                    "  4. Return current_max"
                ),
                "explanation": "Clear pseudo-algorithmic specification defining edge cases, initialization, and loop invariants."
            },
            {
                "title": "Buggy Implementation (Fails on Negative Numbers)",
                "language": "python",
                "code": (
                    "def find_max_buggy(numbers):\n"
                    "    # BUG: Initializing max to 0 fails if all numbers are negative!\n"
                    "    max_val = 0\n"
                    "    for n in numbers:\n"
                    "        if n > max_val:\n"
                    "            max_val = n\n"
                    "    return max_val\n\n"
                    "print(find_max_buggy([-5, -12, -3]))  # Returns 0! Expected -3"
                ),
                "explanation": "Initializing with arbitrary constant 0 violates algorithmic correctness for negative sets."
            },
            {
                "title": "Correct Implementation Handling Edge Cases",
                "language": "python",
                "code": (
                    "def find_max(numbers: list[int]) -> int:\n"
                    "    if not numbers:\n"
                    "        raise ValueError('Cannot find max of empty list')\n"
                    "    max_val = numbers[0]\n"
                    "    for n in numbers[1:]:\n"
                    "        if n > max_val:\n"
                    "            max_val = n\n"
                    "    return max_val\n\n"
                    "print(find_max([-5, -12, -3]))  # Returns -3 correctly"
                ),
                "explanation": "Initializes to the first element and guards against empty input sets."
            },
            {
                "title": "The String Sorting Logic Trap",
                "language": "python",
                "code": (
                    "# BUG: Sorting numbers stored as strings causes lexical sorting\n"
                    "raw_ids = ['100', '25', '3', '1000']\n"
                    "print(sorted(raw_ids))  # ['100', '1000', '25', '3'] -> Lexical bug!\n\n"
                    "# FIX: Sort using integer key function\n"
                    "print(sorted(raw_ids, key=int))  # ['3', '25', '100', '1000']"
                ),
                "explanation": "Demonstrates why understanding data types in algorithmic sorting avoids sorting bugs."
            }
        ],
        coding_challenge={
            "title": "Implement Linear Search with Sentinel Check",
            "instructions": "Write a function `linear_search(items, target)` that returns the 0-based index of the first occurrence of `target` in `items`. If `target` is not found, return -1. Handle empty lists properly.",
            "starter_code": (
                "def linear_search(items: list, target) -> int:\n"
                "    # BUG: Returns None or crashes on empty items\n"
                "    pass\n"
            ),
            "solution_code": (
                "def linear_search(items: list, target) -> int:\n"
                "    for idx, item in enumerate(items):\n"
                "        if item == target:\n"
                "            return idx\n"
                "    return -1\n\n"
                "print(linear_search(['apple', 'banana', 'cherry'], 'banana'))\n"
                "print(linear_search([1, 2, 3], 99))"
            ),
            "expected_output": "1\n-1"
        },
        quizzes=[
            {
                "question": "What is an algorithm in computer science?",
                "options": [
                    "A finite, unambiguous sequence of computational instructions that transforms inputs into outputs",
                    "A specific computer programming language like Python",
                    "A brand of computer hardware processor",
                    "A database table containing user passwords"
                ],
                "correct_answer": "A finite, unambiguous sequence of computational instructions that transforms inputs into outputs",
                "explanation": "An algorithm is a step-by-step recipe for solving a problem within finite time and resources."
            },
            {
                "question": "Why did `find_max([-5, -12, -3])` return `0` when `max_val` was initialized to `0`?",
                "options": [
                    "Because 0 is greater than all negative numbers in the list, masking the true negative maximum",
                    "Because computers cannot calculate negative numbers",
                    "Because Python converts negative numbers to zero automatically",
                    "Because the loop ran in reverse order"
                ],
                "correct_answer": "Because 0 is greater than all negative numbers in the list, masking the true negative maximum",
                "explanation": "Initializing with 0 assumes all numbers are positive, a classic algorithmic assumption bug."
            },
            {
                "question": "What are George Pólya's four steps for problem solving?",
                "options": [
                    "Understand the problem, Devise a plan, Carry out the plan, Look back & reflect",
                    "Write code, Compile, Deploy, Panic",
                    "Buy servers, Install OS, Code, Pray",
                    "Read errors, Ignore warnings, Reboot, Test"
                ],
                "correct_answer": "Understand the problem, Devise a plan, Carry out the plan, Look back & reflect",
                "explanation": "Pólya's methodology emphasizes understanding requirements and designing plans before coding."
            },
            {
                "question": "Why does sorting the list `['10', '2', '300']` without a key function produce `['10', '2', '300']` instead of numeric ascending order?",
                "options": [
                    "Strings are compared lexicographically (character-by-character based on ASCII values) rather than numerically",
                    "Python sort algorithm is broken",
                    "The number 10 is mathematically smaller than 2",
                    "Lists cannot be sorted"
                ],
                "correct_answer": "Strings are compared lexicographically (character-by-character based on ASCII values) rather than numerically",
                "explanation": "In string comparison, `'1'` comes before `'2'`, so `'10'` is evaluated as smaller than `'2'`."
            },
            {
                "question": "What is an 'invariant' in algorithm design?",
                "options": [
                    "A condition or property that remains true throughout the execution of a loop or subroutine",
                    "A variable whose value changes randomly",
                    "A syntax error in C++",
                    "An unused imported library"
                ],
                "correct_answer": "A condition or property that remains true throughout the execution of a loop or subroutine",
                "explanation": "Loop invariants guarantee correctness by maintaining true conditions at initialization, maintenance, and termination."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 4: Flowcharts & Pseudocode (Pre-Code Validation)
    # ---------------------------------------------------------
    DayBlueprint(
        order=4,
        title="Day 4: Flowcharts & Pseudocode (Pre-Code Validation)",
        concept="Flowcharts and pseudocode provide visual and syntactic abstractions of program logic, enabling developers to discover architectural flaws before investing time in syntax.",
        analogy="Writing pseudocode before coding is like drawing a rough floorplan sketch on a napkin before pouring a concrete building foundation. It costs 5 cents to erase a pencil line on a napkin; it costs $50,000 to jackhammer a cured concrete wall.",
        theory_sections=[
            {
                "heading": "Standard Flowchart Symbols and Logic Flow",
                "content": (
                    "Flowcharts standardize graphical modeling of control flow:\n"
                    "- **Oval / Rounded Rectangle (Terminal)**: Program Start or End.\n"
                    "- **Rectangle (Process)**: Action, assignment, or computation (e.g. `sum = a + b`).\n"
                    "- **Diamond (Decision)**: Branching condition producing True/False or Yes/No paths.\n"
                    "- **Parallelogram (Input/Output)**: Reading data or printing/rendering.\n"
                    "- **Arrows**: Directed flow of program control."
                )
            },
            {
                "heading": "Writing Effective Pseudocode",
                "content": (
                    "Pseudocode is an informal high-level description of an algorithm intended for human reading rather than machine execution. Key rules:\n"
                    "1. Use clear keywords: `IF`, `THEN`, `ELSE`, `WHILE`, `FOR`, `RETURN`.\n"
                    "2. Avoid language-specific quirks (don't write `malloc` or `useEffect`).\n"
                    "3. Indent nested blocks clearly to represent scope.\n"
                    "4. Focus on the *intent* of the operation rather than low-level mechanics."
                )
            },
            {
                "heading": "Catching Dead Ends & Infinite Loops on Paper",
                "content": (
                    "A primary benefit of diagramming flowcharts is tracing edge conditions:\n"
                    "- **Unreachable Code (Dead Ends)**: A decision path that can never be reached under any mathematical inputs.\n"
                    "- **Missing Else Branches**: What happens when the user clicks 'Cancel' or when an API returns an empty payload?\n"
                    "- **Unterminated Loops**: Tracing arrow loops on paper confirms there is a guaranteed exit condition."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Pseudocode: ATM Withdrawal Logic",
                "language": "text",
                "code": (
                    "FUNCTION WithdrawCash(account, requested_amount):\n"
                    "  IF requested_amount <= 0 THEN\n"
                    "    RETURN Error('Amount must be positive')\n"
                    "  END IF\n"
                    "  \n"
                    "  IF requested_amount > account.balance THEN\n"
                    "    RETURN Error('Insufficient funds')\n"
                    "  END IF\n"
                    "  \n"
                    "  IF requested_amount > ATM.cash_available THEN\n"
                    "    RETURN Error('ATM out of cash')\n"
                    "  END IF\n"
                    "  \n"
                    "  account.balance = account.balance - requested_amount\n"
                    "  ATM.cash_available = ATM.cash_available - requested_amount\n"
                    "  DispenseCash(requested_amount)\n"
                    "  RETURN Success(account.balance)"
                ),
                "explanation": "Clear pseudocode capturing multiple edge cases (negative input, insufficient account funds, ATM reservoir limits)."
            },
            {
                "title": "Python Translation of the ATM Logic",
                "language": "python",
                "code": (
                    "class ATM:\n"
                    "    def __init__(self, cash_available: float):\n"
                    "        self.cash = cash_available\n\n"
                    "    def withdraw(self, account: dict, amount: float) -> dict:\n"
                    "        if amount <= 0:\n"
                    "            return {'success': False, 'error': 'Amount must be positive'}\n"
                    "        if amount > account['balance']:\n"
                    "            return {'success': False, 'error': 'Insufficient funds'}\n"
                    "        if amount > self.cash:\n"
                    "            return {'success': False, 'error': 'ATM cash limit reached'}\n\n"
                    "        account['balance'] -= amount\n"
                    "        self.cash -= amount\n"
                    "        return {'success': True, 'new_balance': account['balance']}"
                ),
                "explanation": "Direct, 1-to-1 implementation of the pre-validated pseudocode without missing edge cases."
            },
            {
                "title": "Flawed Logic Traced on Paper (Missing Else)",
                "language": "python",
                "code": (
                    "# BUG: What if score is exactly 70? Or negative?\n"
                    "def get_grade_flawed(score):\n"
                    "    if score > 90:\n"
                    "        return 'A'\n"
                    "    elif score > 80:\n"
                    "        return 'B'\n"
                    "    elif score > 70:\n"
                    "        return 'C'\n"
                    "    # Missing return! If score is 70, returns None implicitly!\n\n"
                    "print(get_grade_flawed(70))  # None! Expected 'D' or 'C'"
                ),
                "explanation": "Traced on a flowchart, score 70 falls off the diagram without an exit node."
            },
            {
                "title": "Fixed Logic with Comprehensive Catch-All",
                "language": "python",
                "code": (
                    "def get_grade(score: int) -> str:\n"
                    "    if not (0 <= score <= 100):\n"
                    "        raise ValueError(f'Invalid score: {score}')\n"
                    "    if score >= 90: return 'A'\n"
                    "    if score >= 80: return 'B'\n"
                    "    if score >= 70: return 'C'\n"
                    "    if score >= 60: return 'D'\n"
                    "    return 'F'"
                ),
                "explanation": "Guards boundaries and guarantees a valid deterministic string return for every integer 0-100."
            }
        ],
        coding_challenge={
            "title": "Translate Pseudocode to Python: FizzBuzz Variant",
            "instructions": "Translate the following pseudocode into a working Python function `custom_fizz_buzz(n)`:\nFOR i from 1 to n:\n  IF i divisible by 15: add 'FizzBuzz'\n  ELSE IF i divisible by 3: add 'Fizz'\n  ELSE IF i divisible by 5: add 'Buzz'\n  ELSE: add string(i)\nRETURN list of results.",
            "starter_code": (
                "def custom_fizz_buzz(n: int) -> list:\n"
                "    # Implement translated pseudocode\n"
                "    pass\n"
            ),
            "solution_code": (
                "def custom_fizz_buzz(n: int) -> list:\n"
                "    res = []\n"
                "    for i in range(1, n + 1):\n"
                "        if i % 15 == 0:\n"
                "            res.append('FizzBuzz')\n"
                "        elif i % 3 == 0:\n"
                "            res.append('Fizz')\n"
                "        elif i % 5 == 0:\n"
                "            res.append('Buzz')\n"
                "        else:\n"
                "            res.append(str(i))\n"
                "    return res\n\n"
                "print(custom_fizz_buzz(5))"
            ),
            "expected_output": "['1', '2', 'Fizz', '4', 'Buzz']"
        },
        quizzes=[
            {
                "question": "Which standard flowchart shape represents a conditional decision point (such as an IF/ELSE condition)?",
                "options": [
                    "Diamond",
                    "Rectangle",
                    "Circle",
                    "Parallelogram"
                ],
                "correct_answer": "Diamond",
                "explanation": "A diamond represents a conditional evaluation with diverging branch paths (e.g. Yes/No)."
            },
            {
                "question": "What is the primary objective of writing pseudocode before typing code in an IDE?",
                "options": [
                    "To clarify logic, order of operations, and edge conditions without getting distracted by language-specific syntax errors",
                    "To compile faster machine code",
                    "To compress files on disk",
                    "To replace database indexes"
                ],
                "correct_answer": "To clarify logic, order of operations, and edge conditions without getting distracted by language-specific syntax errors",
                "explanation": "Pseudocode allows engineers to validate concepts rapidly before investing in syntax."
            },
            {
                "question": "In a flowchart, what does a parallelogram symbol represent?",
                "options": [
                    "Input / Output operations (such as reading user input or printing results)",
                    "Program start and stop",
                    "A database table join",
                    "An infinite loop"
                ],
                "correct_answer": "Input / Output operations (such as reading user input or printing results)",
                "explanation": "Parallelograms represent external data input or output operations in ANSI flowchart standards."
            },
            {
                "question": "What common programming bug occurs when all branches of an `if / elif` chain fail and there is no `else` fallback?",
                "options": [
                    "The function returns an unexpected `None` or produces undefined behavior",
                    "The CPU reboots",
                    "The compiler automatically writes an else statement",
                    "The file is deleted"
                ],
                "correct_answer": "The function returns an unexpected `None` or produces undefined behavior",
                "explanation": "In Python, falling through an unhandled branching path results in an implicit `return None`."
            },
            {
                "question": "Why should pseudocode avoid language-specific keywords like `std::vector` or `malloc`?",
                "options": [
                    "Pseudocode is intended to be universally readable by any programmer regardless of their target language",
                    "Compilers crash when pseudocode is saved on disk",
                    "It is forbidden by the Linux Foundation",
                    "Variable names must be shorter than 4 characters"
                ],
                "correct_answer": "Pseudocode is intended to be universally readable by any programmer regardless of their target language",
                "explanation": "Pseudocode focuses on algorithmic architecture rather than implementation specifics."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 5: Divide and Conquer Approach (Decomposition)
    # ---------------------------------------------------------
    DayBlueprint(
        order=5,
        title="Day 5: Divide and Conquer Approach (Decomposition)",
        concept="Divide and Conquer decomposes a large, intimidating problem into smaller, independent sub-problems, solves each sub-problem in isolation, and combines their solutions.",
        analogy="If you are tasked with cleaning a messy 4-story mansion, you will feel overwhelmed and freeze if you look at the whole building at once. But if you divide it room-by-room—first wash dishes in Kitchen, then vacuum Living Room, then wipe Bathroom mirrors—each small task is manageable.",
        theory_sections=[
            {
                "heading": "The 3 Steps of Divide and Conquer",
                "content": (
                    "Divide and Conquer is both an algorithmic paradigm (Merge Sort, Binary Search) and a master debugging principle:\n"
                    "1. **Divide**: Break the problem or codebase into disjoint, smaller parts.\n"
                    "2. **Conquer**: Solve or test each sub-component in total isolation.\n"
                    "3. **Combine**: Integrate the validated components together to solve the macro-problem."
                )
            },
            {
                "heading": "Functional Decomposition in Software Architecture",
                "content": (
                    "A 500-line monolithic function that reads a CSV, cleans text, connects to a database, calculates sales tax, and sends an email is a debugging nightmare. When an error occurs on line 342, tracking state variables is nearly impossible.\n\n"
                    "**Decomposition** splits this monster into 5 single-responsibility functions:\n"
                    "- `parse_csv(file_path)`\n"
                    "- `sanitize_data(records)`\n"
                    "- `calculate_tax(subtotal)`\n"
                    "- `save_to_db(records)`\n"
                    "- `send_notification(email)`\n"
                    "Now, each function can be unit tested, debugged, and reasoned about independently."
                )
            },
            {
                "heading": "Debugging by Bisection (Divide and Conquer on Bugs)",
                "content": (
                    "When a bug occurs in an unfamiliar 10,000-line codebase:\n"
                    "- Don't read all 10,000 lines sequentially.\n"
                    "- Check the state at line 5,000 (the midpoint). Is the state corrupted here?\n"
                    "- If YES: The bug is in the first half (lines 1 to 5,000).\n"
                    "- If NO: The bug is in the second half (lines 5,001 to 10,000).\n"
                    "In just 13 inspections ($log_2(10000)$), you isolate the exact faulty line."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Monolithic Spaghetti Code (Difficult to Debug)",
                "language": "python",
                "code": (
                    "# MONOLITH: If this crashes, which of the 5 operations failed?\n"
                    "def process_order(raw_text):\n"
                    "    lines = raw_text.split('\\n')\n"
                    "    user = lines[0].split(':')[1]\n"
                    "    total = sum([float(x.split(',')[1]) for x in lines[1:] if x])\n"
                    "    tax = total * 0.08\n"
                    "    db = {'user': user, 'total': total + tax}\n"
                    "    return f'Charged {db[\"user\"]} ${db[\"total\"]:.2f}'"
                ),
                "explanation": "Combining string parsing, summation, tax calculation, and formatting into one block complicates bug isolation."
            },
            {
                "title": "Refactored via Functional Decomposition",
                "language": "python",
                "code": (
                    "def parse_user(header_line: str) -> str:\n"
                    "    return header_line.split(':')[1].strip()\n\n"
                    "def calculate_subtotal(item_lines: list[str]) -> float:\n"
                    "    return sum(float(line.split(',')[1]) for line in item_lines if line.strip())\n\n"
                    "def compute_total_with_tax(subtotal: float, tax_rate: float = 0.08) -> float:\n"
                    "    return round(subtotal * (1 + tax_rate), 2)\n\n"
                    "def process_order_decomposed(raw_text: str) -> str:\n"
                    "    lines = raw_text.strip().split('\\n')\n"
                    "    user = parse_user(lines[0])\n"
                    "    subtotal = calculate_subtotal(lines[1:])\n"
                    "    total = compute_total_with_tax(subtotal)\n"
                    "    return f'Charged {user} ${total:.2f}'"
                ),
                "explanation": "Each distinct step is testable in isolation; bugs in tax calculation or parsing are immediately identifiable."
            },
            {
                "title": "Divide and Conquer Algorithm: Binary Search",
                "language": "python",
                "code": (
                    "def binary_search(sorted_arr, target):\n"
                    "    low, high = 0, len(sorted_arr) - 1\n"
                    "    while low <= high:\n"
                    "        mid = (low + high) // 2\n"
                    "        if sorted_arr[mid] == target:\n"
                    "            return mid\n"
                    "        elif sorted_arr[mid] < target:\n"
                    "            low = mid + 1\n"
                    "        else:\n"
                    "            high = mid - 1\n"
                    "    return -1"
                ),
                "explanation": "Halves the search space on each step, demonstrating log(N) reduction."
            },
            {
                "title": "Testing Decomposed Units in Isolation",
                "language": "python",
                "code": (
                    "# Testing subtotal in complete isolation from string parsing\n"
                    "assert calculate_subtotal(['ItemA,10.00', 'ItemB,5.50']) == 15.50\n"
                    "assert compute_total_with_tax(100.0, 0.10) == 110.00\n"
                    "print('All decomposed unit tests passed!')"
                ),
                "explanation": "Isolated units are verified without needing the full system or mock databases."
            }
        ],
        coding_challenge={
            "title": "Decompose Word Frequency Counter",
            "instructions": "Break down a text word counter into two functions: `clean_words(text)` which lowercases text and removes punctuation, returning a list of words; and `count_frequencies(words)` which takes a list of words and returns a dictionary of counts `{word: count}`.",
            "starter_code": (
                "def clean_words(text: str) -> list:\n"
                "    pass\n\n"
                "def count_frequencies(words: list) -> dict:\n"
                "    pass\n"
            ),
            "solution_code": (
                "import re\n\n"
                "def clean_words(text: str) -> list:\n"
                "    cleaned = re.sub(r'[^a-zA-Z0-9\\s]', '', text).lower()\n"
                "    return cleaned.split()\n\n"
                "def count_frequencies(words: list) -> dict:\n"
                "    freqs = {}\n"
                "    for w in words:\n"
                "        freqs[w] = freqs.get(w, 0) + 1\n"
                "    return freqs\n\n"
                "words = clean_words('Hello world! Hello Python.')\n"
                "print(count_frequencies(words))"
            ),
            "expected_output": "{'hello': 2, 'world': 1, 'python': 1}"
        },
        quizzes=[
            {
                "question": "What are the three core steps in the Divide and Conquer strategy?",
                "options": [
                    "Divide, Conquer, and Combine",
                    "Delete, Reinstall, and Reboot",
                    "Compile, Execute, and Deploy",
                    "Lock, Unlock, and Release"
                ],
                "correct_answer": "Divide, Conquer, and Combine",
                "explanation": "Divide into subproblems, conquer by solving each independently, and combine results."
            },
            {
                "question": "Why is a 500-line monolithic function harder to debug than five 100-line functions?",
                "options": [
                    "In a monolith, variable state can be mutated anywhere, making it difficult to isolate which line caused the corruption",
                    "Monolithic functions are rejected by the Python interpreter",
                    "Monolithic functions always run at half speed",
                    "Variables in monolithic functions are deleted every 10 lines"
                ],
                "correct_answer": "In a monolith, variable state can be mutated anywhere, making it difficult to isolate which line caused the corruption",
                "explanation": "Large functions create excessive variable coupling, making localized reasoning difficult."
            },
            {
                "question": "How does bisection (binary search) apply to debugging a sequence of instructions?",
                "options": [
                    "By inspecting program state at the halfway point, eliminating half of the codebase from suspicion in one check",
                    "By writing the program twice",
                    "By running the program on two computers at once",
                    "By splitting variables into two halves"
                ],
                "correct_answer": "By inspecting program state at the halfway point, eliminating half of the codebase from suspicion in one check",
                "explanation": "Checking the midpoint tells you whether the defect occurred before or after that checkpoint."
            },
            {
                "question": "What is the primary benefit of Functional Decomposition?",
                "options": [
                    "Each sub-function has a single responsibility and can be tested and debugged in complete isolation",
                    "It converts interpreted code into assembly",
                    "It bypasses operating system memory limits",
                    "It prevents syntax errors automatically"
                ],
                "correct_answer": "Each sub-function has a single responsibility and can be tested and debugged in complete isolation",
                "explanation": "Decomposition adheres to Single Responsibility Principle, facilitating modular unit testing."
            },
            {
                "question": "Approximately how many checks are needed to find a single faulty line in 1,000 lines of code using binary search bisection?",
                "options": [
                    "Approximately 10 checks (since 2^10 = 1024)",
                    "1,000 checks",
                    "500 checks",
                    "100 checks"
                ],
                "correct_answer": "Approximately 10 checks (since 2^10 = 1024)",
                "explanation": "Binary search has logarithmic time complexity $O(\\log_2 N)$; $\\log_2(1000) \\approx 10$."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 6: Types of Errors (Syntax, Runtime, Logical/Semantic)
    # ---------------------------------------------------------
    DayBlueprint(
        order=6,
        title="Day 6: Types of Errors (Syntax, Runtime, Logical/Semantic)",
        concept="Software defects fall into three primary categories: Syntax Errors (grammar violations caught before execution), Runtime Errors (crashes during execution), and Logical/Semantic Errors (silent wrong answers).",
        analogy="Syntax error is writing a sentence with broken spelling: 'The dogg are green'—the English teacher spots it instantly. Runtime error is asking someone to 'divide 10 by zero apples'—their brain freezes mid-calculation. Logical error is asking for directions to New York and the GPS politely guides you straight into the Pacific Ocean—no crash, just totally wrong.",
        theory_sections=[
            {
                "heading": "1. Syntax Errors (Parse-Time Failures)",
                "content": (
                    "Syntax errors occur when code violates the formal grammatical rules of the programming language. Examples include missing colons (`:`), unmatched parentheses, misspelled keywords (`whille`), or invalid indentation.\n\n"
                    "Because compilers and interpreters build an Abstract Syntax Tree (AST) before running code, syntax errors **prevent the program from executing a single line**."
                )
            },
            {
                "heading": "2. Runtime Errors (Exceptions during Execution)",
                "content": (
                    "The program compiles and parses cleanly, starts running, and suddenly encounters an impossible operation, crashing the process unless caught:\n"
                    "- `ZeroDivisionError`: Dividing by 0.\n"
                    "- `IndexError` / `KeyError`: Accessing an index or key that does not exist.\n"
                    "- `TypeError`: Trying to add an integer to a dictionary.\n"
                    "- `FileNotFoundError` or network connection dropouts."
                )
            },
            {
                "heading": "3. Logical & Semantic Errors (The Most Dangerous)",
                "content": (
                    "The code compiles cleanly. It runs without throwing any exception. It produces output. But the output is **completely wrong**.\n\n"
                    "Because the computer did exactly what you *told* it to do rather than what you *intended* it to do, logical bugs generate no error messages, no stack traces, and no immediate crashes. They can persist undetected in production databases for months, quietly miscalculating bank balances or skewing reports."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Syntax Error Example",
                "language": "python",
                "code": (
                    "# SyntaxError: invalid syntax (missing colon at end of if statement)\n"
                    "age = 20\n"
                    "if age >= 18\n"
                    "    print('Eligible to vote')\n"
                    "# Python fails immediately before executing line 1!"
                ),
                "explanation": "The parser halts immediately during AST generation; no bytecode is emitted."
            },
            {
                "title": "Runtime Error Example",
                "language": "python",
                "code": (
                    "# Code parses fine and starts executing, but crashes on step 3\n"
                    "accounts = {'Alice': 100, 'Bob': 50}\n"
                    "print('Starting transaction...') # Prints successfully\n"
                    "user = 'Charlie'\n"
                    "print(accounts[user]) # KeyError: 'Charlie' crashes the script!"
                ),
                "explanation": "Runtime errors abort execution mid-stream when invalid operations occur."
            },
            {
                "title": "Logical / Semantic Error Example",
                "language": "python",
                "code": (
                    "# Calculates average of 3 numbers\n"
                    "a, b, c = 10, 20, 30\n"
                    "# BUG: Operator precedence causes a + b + (c / 3) instead of (a + b + c) / 3\n"
                    "average = a + b + c / 3\n"
                    "print(f'Average: {average}') # Prints 40.0! (Correct average is 20.0)\n"
                    "# Zero errors, zero crashes, completely incorrect result."
                ),
                "explanation": "Operator precedence logic bug calculates 10 + 20 + 10 = 40 instead of 60 / 3 = 20."
            },
            {
                "title": "Fixing the Logical Error with Parentheses",
                "language": "python",
                "code": (
                    "a, b, c = 10, 20, 30\n"
                    "average = (a + b + c) / 3\n"
                    "print(f'Correct Average: {average:.1f}') # Prints 20.0"
                ),
                "explanation": "Explicit grouping ensures additions occur prior to division, resolving semantic defect."
            }
        ],
        coding_challenge={
            "title": "Identify and Fix All 3 Error Types",
            "instructions": "The function below has a syntax error, a runtime error risk, and a logical error in calculating discount. Fix all three so `apply_discount(100, 20)` correctly returns `80.0`.",
            "starter_code": (
                "# 1. Syntax error on def line\n"
                "# 2. Runtime error if price is non-numeric\n"
                "# 3. Logic error calculating discount\n"
                "def apply_discount(price, percent)\n"
                "    discount = price * percent # Logic bug: multiplies by 20 instead of 0.20\n"
                "    return price + discount    # Logic bug: adds instead of subtracts\n"
            ),
            "solution_code": (
                "def apply_discount(price: float, percent: float) -> float:\n"
                "    if not isinstance(price, (int, float)) or not isinstance(percent, (int, float)):\n"
                "        raise TypeError('Price and percent must be numeric')\n"
                "    discount_amount = price * (percent / 100.0)\n"
                "    return round(price - discount_amount, 2)\n\n"
                "print(apply_discount(100, 20))"
            ),
            "expected_output": "80.0"
        },
        quizzes=[
            {
                "question": "Which type of error prevents a program from even starting execution?",
                "options": [
                    "Syntax Error",
                    "Logical Error",
                    "Runtime Error",
                    "Semantic Error"
                ],
                "correct_answer": "Syntax Error",
                "explanation": "Syntax errors violate language grammar and prevent the parser from building valid bytecode."
            },
            {
                "question": "What is a Logical (Semantic) Error?",
                "options": [
                    "An error where the program runs without crashing but produces incorrect business results",
                    "An error caused by a missing semicolon or parenthesis",
                    "A crash caused by dividing by zero",
                    "A hardware failure in the computer monitor"
                ],
                "correct_answer": "An error where the program runs without crashing but produces incorrect business results",
                "explanation": "Logical errors represent flaws in algorithm design where code executes smoothly to a wrong answer."
            },
            {
                "question": "Why are Logical Errors generally considered the most dangerous in production?",
                "options": [
                    "Because they produce no crash or error logs, allowing corrupted data to accumulate silently",
                    "Because they permanently damage the motherboard",
                    "Because they make source code unreadable",
                    "Because they delete git history"
                ],
                "correct_answer": "Because they produce no crash or error logs, allowing corrupted data to accumulate silently",
                "explanation": "Without crashes or alerts, logical errors can corrupt financial or user data unnoticed for long periods."
            },
            {
                "question": "Accessing `my_list[10]` when `len(my_list) == 3` produces what category of error?",
                "options": [
                    "Runtime Error (`IndexError`)",
                    "Syntax Error",
                    "Compile-time Error",
                    "Encoding Error"
                ],
                "correct_answer": "Runtime Error (`IndexError`)",
                "explanation": "The syntax is valid, but the CPU encounters an out-of-bounds index dynamically at runtime."
            },
            {
                "question": "What will `print(10 + 20 / 2)` output in Python, and why is it a frequent beginner logic bug?",
                "options": [
                    "20.0, because division `/` has higher operator precedence than addition `+`",
                    "15.0, because calculations always run strictly left to right",
                    "ZeroDivisionError",
                    "TypeError"
                ],
                "correct_answer": "20.0, because division `/` has higher operator precedence than addition `+`",
                "explanation": "Division happens first: $20 / 2 = 10$, then $10 + 10 = 20.0$. Parentheses are required for $(10 + 20) / 2$."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 7: Reproducing the Bug (Trigger Mechanisms)
    # ---------------------------------------------------------
    DayBlueprint(
        order=7,
        title="Day 7: Reproducing the Bug (Trigger Mechanisms)",
        concept="Bug reproduction is the discipline of creating a minimal, deterministic, and isolated scenario that reliably causes the bug to appear on demand.",
        analogy="Imagine taking your car to a mechanic and saying 'It makes a squeaking sound sometimes.' If you can't show the mechanic when it happens, they can't fix it. But if you can say 'Shift into 3rd gear, turn right, and tap the brake,' the mechanic reproduces the sound in 10 seconds.",
        theory_sections=[
            {
                "heading": "The Golden Rule: 'If You Can't Reproduce It, You Can't Fix It'",
                "content": (
                    "Attempting to patch a bug without reproducing it first is playing Russian roulette with your codebase. You might write a fix that addresses a non-existent issue while the real defect remains.\n\n"
                    "A **reproducible bug** converts an elusive mystery into an engineering problem. Once you can trigger it with a single command or script, verifying the fix takes 2 seconds: run the script; if it passes, the bug is dead."
                )
            },
            {
                "heading": "Finding the Trigger Mechanism",
                "content": (
                    "To reproduce a bug reported by users, gather the critical telemetry:\n"
                    "1. **Exact Input Data**: Special characters (emojis, quotes), extreme values, or empty strings.\n"
                    "2. **Environmental Context**: OS, browser version, screen resolution, timezone, locale.\n"
                    "3. **State Preconditions**: Was the user logged in? Did they have an expired session cookie? Did they click 'Submit' twice in rapid succession?\n"
                    "4. **Exact Sequence of Actions**: Step-by-step navigation pathway."
                )
            },
            {
                "heading": "Creating a Minimal Reproducible Example (MRE / SSCCE)",
                "content": (
                    "When debugging an enterprise app, do not test inside a 50,000-line codebase. Extract the suspect logic into a standalone 15-line script.\n"
                    "- **Short**: Strip away 95% of unrelated application code.\n"
                    "- **Self-Contained**: No external database or network dependencies (use mock data).\n"
                    "- **Correct**: It must run and demonstrate the exact failure."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Bug Report: 'App crashes when searching for names'",
                "language": "python",
                "code": (
                    "# User says: 'It crashes sometimes!'\n"
                    "# Step 1: Discover the trigger mechanism (e.g. searching with apostrophe 'O'Connor')\n"
                    "def search_user(query: str, users: list[str]) -> list[str]:\n"
                    "    # BUG: Assumes query is always alphanumeric\n"
                    "    return [u for u in users if query.lower() in u.lower()]"
                ),
                "explanation": "Broad bug reports require identifying exact edge-case trigger inputs (such as None or special punctuation)."
            },
            {
                "title": "Minimal Reproducible Example (MRE Script)",
                "language": "python",
                "code": (
                    "# Standalone MRE reproducing the crash on demand\n"
                    "def test_trigger():\n"
                    "    trigger_inputs = [None, '', \"O'Connor\", '🎉', 123]\n"
                    "    for test_val in trigger_inputs:\n"
                    "        try:\n"
                    "            # Call suspect function\n"
                    "            test_val.lower() # Crashes on None and 123 with AttributeError\n"
                    "            print(f'Input {repr(test_val)}: PASSED')\n"
                    "        except Exception as e:\n"
                    "            print(f'TRIGGER FOUND! Input {repr(test_val)} failed with {type(e).__name__}: {e}')\n\n"
                    "test_trigger()"
                ),
                "explanation": "Script tests edge inputs and pinpoints non-string types as the deterministic trigger."
            },
            {
                "title": "Writing the Defensively Hardened Function",
                "language": "python",
                "code": (
                    "def safe_search_user(query, users: list[str]) -> list[str]:\n"
                    "    if not query or not isinstance(query, str):\n"
                    "        return []\n"
                    "    clean_q = query.strip().lower()\n"
                    "    return [u for u in users if isinstance(u, str) and clean_q in u.lower()]"
                ),
                "explanation": "Guards against non-string and empty triggers, handling inputs deterministically."
            },
            {
                "title": "Automated Regression Test from the Reproduction Script",
                "language": "python",
                "code": (
                    "def test_search_regression():\n"
                    "    sample_users = ['Alice', \"O'Connor\", 'Bob']\n"
                    "    # Verify previously failing triggers now pass gracefully\n"
                    "    assert safe_search_user(None, sample_users) == []\n"
                    "    assert safe_search_user(123, sample_users) == []\n"
                    "    assert safe_search_user(\"o'connor\", sample_users) == [\"O'Connor\"]\n"
                    "    print('Regression tests passed!')\n\n"
                    "test_search_regression()"
                ),
                "explanation": "Converts the reproduction script directly into a permanent regression test."
            }
        ],
        coding_challenge={
            "title": "Create a Deterministic Test Case for a Hidden Date Bug",
            "instructions": "The function `parse_iso_year(date_str)` crashes when given dates with missing components or invalid formats. Write a reproduction function `find_failing_inputs(date_list)` that tests each string in `date_list` and returns a list of only the strings that triggered an exception.",
            "starter_code": (
                "def parse_iso_year(date_str: str) -> int:\n"
                "    return int(date_str.split('-')[0])\n\n"
                "def find_failing_inputs(dates: list) -> list:\n"
                "    # Return list of items from dates that cause parse_iso_year to crash\n"
                "    pass\n"
            ),
            "solution_code": (
                "def parse_iso_year(date_str: str) -> int:\n"
                "    return int(date_str.split('-')[0])\n\n"
                "def find_failing_inputs(dates: list) -> list:\n"
                "    failing = []\n"
                "    for d in dates:\n"
                "        try:\n"
                "            parse_iso_year(d)\n"
                "        except Exception:\n"
                "            failing.append(d)\n"
                "    return failing\n\n"
                "test_dates = ['2026-05-12', 'invalid', '2025/01/01', '']\n"
                "print(find_failing_inputs(test_dates))"
            ),
            "expected_output": "['invalid', '']"
        },
        quizzes=[
            {
                "question": "Why is reproducing a bug considered the essential prerequisite to fixing it?",
                "options": [
                    "Because if you cannot reliably trigger the bug, you cannot verify whether your code changes actually fixed the root cause",
                    "Because compilers refuse to commit code without reproduction files",
                    "Because reproducing bugs makes the computer run faster",
                    "Because it is required by database protocols"
                ],
                "correct_answer": "Because if you cannot reliably trigger the bug, you cannot verify whether your code changes actually fixed the root cause",
                "explanation": "Without reproduction, any code modification is guesswork without proof of resolution."
            },
            {
                "question": "What does 'MRE' stand for in software debugging terminology?",
                "options": [
                    "Minimal Reproducible Example",
                    "Memory Register Execution",
                    "Main Routing Engine",
                    "Module Runtime Environment"
                ],
                "correct_answer": "Minimal Reproducible Example",
                "explanation": "An MRE isolates the defect in the smallest possible runnable code snippet."
            },
            {
                "question": "What type of bugs are notoriously difficult to reproduce because they depend on unpredictable timing or concurrency?",
                "options": [
                    "Heisenbugs (Race Conditions)",
                    "Syntax errors",
                    "404 Not Found errors",
                    "Missing semicolon errors"
                ],
                "correct_answer": "Heisenbugs (Race Conditions)",
                "explanation": "Heisenbugs change behavior or disappear when inspected due to multi-threaded timing dependencies."
            },
            {
                "question": "What should you do with a minimal reproduction script once you have fixed the bug?",
                "options": [
                    "Convert it into an automated unit/regression test to ensure the bug never recurs",
                    "Delete it immediately",
                    "Print it on paper and archive it in a closet",
                    "Send it in an email to all users"
                ],
                "correct_answer": "Convert it into an automated unit/regression test to ensure the bug never recurs",
                "explanation": "Adding reproduction scripts to your test suite creates a regression shield for the lifetime of the software."
            },
            {
                "question": "Which of the following is NOT a helpful piece of information when trying to reproduce a user-reported bug?",
                "options": [
                    "The user's favorite color and music playlist",
                    "Exact error messages or screenshots",
                    "The operating system and browser version",
                    "The step-by-step sequence of user actions before the failure"
                ],
                "correct_answer": "The user's favorite color and music playlist",
                "explanation": "Telemetry must focus on environment, inputs, state, and actions."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 8: Rubber Duck Debugging (Line-by-Line Explanation)
    # ---------------------------------------------------------
    DayBlueprint(
        order=8,
        title="Day 8: Rubber Duck Debugging (Line-by-Line Explanation)",
        concept="Rubber Duck Debugging is the practice of explaining code line-by-line in plain human language to an inanimate object, forcing the brain to articulate assumptions and discover logical oversights.",
        analogy="Have you ever searched your entire house for your car keys for 30 minutes, called a family member to complain, and while saying 'I looked on the counter, next to the toaster...' you glance over and see the keys sitting right beside the toaster? Explaining aloud forces your brain to observe reality rather than memory.",
        theory_sections=[
            {
                "heading": "The Science Behind Rubber Ducking",
                "content": (
                    "When reading code silently in your head, the brain operates in an **optimistic simulation mode**: it skims past assumptions, filling in blanks with what you *meant* to write rather than what is actually on the screen.\n\n"
                    "When you speak aloud to an inanimate object (like a yellow rubber duck on your desk):\n"
                    "1. You switch from internal visual scanning to external verbal articulation.\n"
                    "2. You are forced to slow down to conversational speed.\n"
                    "3. In explaining *'Here I take the user ID from the URL... wait, I passed the user ID into the item ID parameter!'*, the bug reveals itself instantly."
                )
            },
            {
                "heading": "The 4-Step Rubber Duck Protocol",
                "content": (
                    "1. **State the Goal**: Tell the duck what the function is supposed to achieve.\n"
                    "2. **Describe Inputs & Invariants**: Tell the duck what data is arriving and what types you expect.\n"
                    "3. **Walk Line-by-Line**: Explain every single line: *'Line 12 opens the file. Line 13 reads line by line. Line 14 splits by comma...'*.\n"
                    "4. **Acknowledge Discrepancies**: The moment you say a sentence that sounds hesitant or contradictory, stop! You just found the bug."
                )
            },
            {
                "heading": "Modern AI as the Ultimate Rubber Duck",
                "content": (
                    "While a plastic duck is silent, modern developers use conversational AI as an active rubber duck:\n"
                    "- Paste your function and prompt: *'Explain to me what line 24 does in this function, step by step, without writing any code.'*\n"
                    "- The interactive dialogue exposes edge cases you overlooked."
                )
            }
        ],
        code_snippets=[
            {
                "title": "A Function with a Subtle Argument Swap Bug",
                "language": "python",
                "code": (
                    "def create_user_profile(user_id: int, organization_id: int, is_admin: bool):\n"
                    "    return {'uid': user_id, 'org': organization_id, 'admin': is_admin}\n\n"
                    "# Calling site: Silent logic bug that silent reading misses!\n"
                    "current_org = 50\n"
                    "current_user = 1001\n"
                    "# BUG: Arguments swapped! current_org passed into user_id position\n"
                    "profile = create_user_profile(current_org, current_user, False)\n"
                    "print(profile) # {'uid': 50, 'org': 1001, 'admin': False}"
                ),
                "explanation": "Because both arguments are integers, Python does not crash, but identity state is permanently inverted."
            },
            {
                "title": "The Rubber Duck Realization",
                "language": "text",
                "code": (
                    "Developer explaining to Duck:\n"
                    "- 'Duck, look at line 8.'\n"
                    "- 'I am calling create_user_profile.'\n"
                    "- 'The first parameter is user_id.'\n"
                    "- 'Wait... why am I passing current_org first?!'\n"
                    "- 'current_org is 50, not the user ID! Ah!'"
                ),
                "explanation": "Verbalizing argument order immediately exposes position transposition."
            },
            {
                "title": "Fixing with Keyword Arguments (Self-Documenting)",
                "language": "python",
                "code": (
                    "# FIX: Use explicit keyword arguments to eliminate positional swap bugs\n"
                    "profile = create_user_profile(\n"
                    "    user_id=current_user,\n"
                    "    organization_id=current_org,\n"
                    "    is_admin=False\n"
                    ")\n"
                    "print(profile) # {'uid': 1001, 'org': 50, 'admin': False}"
                ),
                "explanation": "Keyword arguments prevent positional argument mix-ups."
            },
            {
                "title": "Enforcing Keyword-Only Arguments in Python",
                "language": "python",
                "code": (
                    "# Using '*' forces callers to name arguments explicitly\n"
                    "def create_user_profile_safe(*, user_id: int, organization_id: int, is_admin: bool):\n"
                    "    return {'uid': user_id, 'org': organization_id, 'admin': is_admin}\n\n"
                    "# create_user_profile_safe(50, 1001, False) -> TypeError: takes 0 positional arguments!"
                ),
                "explanation": "Keyword-only syntax (`*`) transforms runtime argument swaps into immediate compiler/interpreter errors."
            }
        ],
        coding_challenge={
            "title": "Find the Loop Invariant Flaw via Explanation",
            "instructions": "The function below attempts to remove all even numbers from a list in-place, but produces wrong results because modifying a list while iterating over it skips elements. Fix the function so it safely returns a list containing only odd numbers.",
            "starter_code": (
                "def remove_evens(numbers: list) -> list:\n"
                "    # BUG: Modifying list during iteration shifts indices!\n"
                "    for n in numbers:\n"
                "        if n % 2 == 0:\n"
                "            numbers.remove(n)\n"
                "    return numbers\n"
            ),
            "solution_code": (
                "def remove_evens(numbers: list) -> list:\n"
                "    # Solution: Use list comprehension or copy to avoid mutating during iteration\n"
                "    return [n for n in numbers if n % 2 != 0]\n\n"
                "nums = [2, 4, 6, 7, 8, 10]\n"
                "print(remove_evens(nums))"
            ),
            "expected_output": "[7]"
        },
        quizzes=[
            {
                "question": "What is 'Rubber Duck Debugging'?",
                "options": [
                    "Explaining your code line-by-line aloud to an inanimate object to trigger cognitive self-realization of logical bugs",
                    "A stress-relief bath toy for programmers",
                    "An automated AI tool inside VS Code",
                    "A technique for cleaning mechanical keyboards"
                ],
                "correct_answer": "Explaining your code line-by-line aloud to an inanimate object to trigger cognitive self-realization of logical bugs",
                "explanation": "Verbalizing each line forces the brain to examine code objectively rather than skimming assumptions."
            },
            {
                "question": "Why does silent reading often fail to catch subtle bugs that verbal explanation catches instantly?",
                "options": [
                    "Silent reading relies on optimistic visual skimming, whereas verbalization forces slower, sequential processing of every token",
                    "Human eyes cannot read programming code silently",
                    "Silent reading disables monitor pixels",
                    "Rubber ducks emit ultrasonic debugging frequencies"
                ],
                "correct_answer": "Silent reading relies on optimistic visual skimming, whereas verbalization forces slower, sequential processing of every token",
                "explanation": "Vocalizing code engages different neural pathways, breaking cognitive skimming habits."
            },
            {
                "question": "In Python, what bug occurs when you call `numbers.remove(n)` inside `for n in numbers:`?",
                "options": [
                    "Elements are skipped because deleting an item shifts subsequent elements to lower indices while the iterator increments",
                    "A SyntaxError is raised",
                    "The list is cleared entirely",
                    "The Python process crashes with a segmentation fault"
                ],
                "correct_answer": "Elements are skipped because deleting an item shifts subsequent elements to lower indices while the iterator increments",
                "explanation": "Mutating a collection during iteration corrupts the iterator's index counter."
            },
            {
                "question": "How does using keyword arguments (`func(user_id=1, role='admin')`) prevent bugs spotted during rubber ducking?",
                "options": [
                    "It prevents accidental argument transposition when multiple parameters share identical data types",
                    "It makes code compile to C binaries",
                    "It encrypts variables in RAM",
                    "It bypasses function timeouts"
                ],
                "correct_answer": "It prevents accidental argument transposition when multiple parameters share identical data types",
                "explanation": "Keyword arguments link values to explicit parameter names regardless of order."
            },
            {
                "question": "What is the recommended first step in a Rubber Duck Debugging session?",
                "options": [
                    "State the high-level goal and expected behavior of the code before diving into lines",
                    "Immediately start typing new code",
                    "Delete all comments",
                    "Turn off the computer screen"
                ],
                "correct_answer": "State the high-level goal and expected behavior of the code before diving into lines",
                "explanation": "Defining the expected output establishes the baseline against which every line is evaluated."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 9: The "Wolf Fence" / Binary Search Debugging
    # ---------------------------------------------------------
    DayBlueprint(
        order=9,
        title="Day 9: The 'Wolf Fence' / Binary Search Debugging",
        concept="The Wolf Fence algorithm isolates defects in large systems by placing diagnostic checkpoints midway, halving the suspect area at each step until the exact defect line is trapped.",
        analogy="There is a wolf howling inside Alaska, but you don't know where it is. You build a fence across the center of Alaska from north to south and listen. The wolf howls on the west side. You build another fence down the center of West Alaska. In 10 fence builds, the wolf is trapped in a tiny 10-meter cage.",
        theory_sections=[
            {
                "heading": "The Wolf Fence Metaphor in Computer Science",
                "content": (
                    "Attributed to Gauss and popularized by computer scientist Edward Gauss (1982), the Wolf Fence algorithm is **Binary Search applied to software diagnostics**.\n\n"
                    "When an application crashes or corrupts data after executing 2,000 lines of code across 10 modules, do not read lines 1 through 2,000 sequentially ($O(N)$ linear search). Build a 'fence' at line 1,000 with a logging statement or assertion."
                )
            },
            {
                "heading": "Applying the Wolf Fence in Code",
                "content": (
                    "1. **Identify Boundary**: Bug occurs somewhere between point A (input validated, state known to be good) and point B (crash or corrupted output).\n"
                    "2. **Place Fence at Midpoint M**: Inspect state at $M = (A + B) / 2$.\n"
                    "3. **Evaluate**: Is state still clean at $M$?\n"
                    "   - If YES: The defect lies downstream between $M$ and $B$.\n"
                    "   - If NO: The defect already occurred upstream between $A$ and $M$.\n"
                    "4. **Iterate**: Repeat until the fence narrows down to a single function or single line of code."
                )
            },
            {
                "heading": "Git Bisect: The Ultimate Wolf Fence for Version Control",
                "content": (
                    "When an application worked last month in commit `v1.2.0`, but is broken today in `v1.5.0` (with 500 commits in between):\n"
                    "`git bisect` automatically checks out the midpoint commit. You test it (or let a script test it). `git bisect` marks it good or bad, and in $\\approx 9$ steps ($2^9 = 512$), it pinpoints the exact commit and developer who introduced the bug!"
                )
            }
        ],
        code_snippets=[
            {
                "title": "Wolf Fence with Print Statements",
                "language": "python",
                "code": (
                    "def long_pipeline(data):\n"
                    "    step1 = transform_a(data)\n"
                    "    step2 = transform_b(step1)\n"
                    "    \n"
                    "    # FENCE 1: Checkpoint at midpoint\n"
                    "    print(f'=== FENCE 1 (Midpoint) ===: len={len(step2)}, sample={step2[:1]}')\n"
                    "    # If step2 is already corrupted, bug is in transform_a or transform_b\n"
                    "    # If step2 is valid, bug is in transform_c or transform_d\n"
                    "    \n"
                    "    step3 = transform_c(step2)\n"
                    "    step4 = transform_d(step3)\n"
                    "    return step4"
                ),
                "explanation": "A single print checkpoint eliminates 50% of the pipeline from suspicion immediately."
            },
            {
                "title": "Automating Git Bisect in CLI",
                "language": "bash",
                "code": (
                    "# Start binary search on git commit history\n"
                    "git bisect start\n"
                    "git bisect bad                 # Current commit is broken\n"
                    "git bisect good v1.2.0         # v1.2.0 was known to be working\n\n"
                    "# Git checks out commit #250 automatically!\n"
                    "# Run tests: pytest tests/test_orders.py\n"
                    "# If tests pass:  git bisect good\n"
                    "# If tests fail:  git bisect bad\n"
                    "# Within 8 checks, Git prints:\n"
                    "# 'a8f3b21 is the first bad commit - Author: Dev <dev@work.com>'"
                ),
                "explanation": "Standard git bisect workflow halving historical commits automatically."
            },
            {
                "title": "Fully Automated Git Bisect with Script",
                "language": "bash",
                "code": (
                    "# Automate bisect with an executable test script\n"
                    "git bisect run pytest tests/test_auth.py\n\n"
                    "# Git runs the test on each bisect commit unattended\n"
                    "# and finishes with the culprit commit in under 30 seconds"
                ),
                "explanation": "Automated regression isolation executing zero-touch binary testing."
            },
            {
                "title": "Wolf Fence Implementation in Algorithmic Code",
                "language": "python",
                "code": (
                    "# Finding the first bad API build version (LeetCode 278)\n"
                    "def first_bad_version(n: int, is_bad_version_api) -> int:\n"
                    "    left, right = 1, n\n"
                    "    while left < right:\n"
                    "        mid = left + (right - left) // 2\n"
                    "        if is_bad_version_api(mid):\n"
                    "            right = mid  # Wolf is in the left half (including mid)\n"
                    "        else:\n"
                    "            left = mid + 1 # Wolf is strictly in the right half\n"
                    "    return left"
                ),
                "explanation": "Classic binary search algorithm finding the boundary where state turns bad."
            }
        ],
        coding_challenge={
            "title": "Simulate Git Bisect on Commit History",
            "instructions": "Write a function `find_bad_commit(commits, test_fn)` where `commits` is a list of commit hash strings in chronological order. `test_fn(commit)` returns True if good, and False if bad. Once a commit is bad, all subsequent commits are bad. Return the hash of the *first* bad commit using binary search.",
            "starter_code": (
                "def find_bad_commit(commits: list, test_fn) -> str:\n"
                "    # Return first bad commit using binary search\n"
                "    pass\n"
            ),
            "solution_code": (
                "def find_bad_commit(commits: list, test_fn) -> str:\n"
                "    low, high = 0, len(commits) - 1\n"
                "    culprit = None\n"
                "    while low <= high:\n"
                "        mid = (low + high) // 2\n"
                "        if not test_fn(commits[mid]):\n"
                "            culprit = commits[mid]\n"
                "            high = mid - 1\n"
                "        else:\n"
                "            low = mid + 1\n"
                "    return culprit\n\n"
                "history = ['c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7']\n"
                "is_good = lambda c: int(c[1]) < 4  # c4 is first bad commit\n"
                "print(find_bad_commit(history, is_good))"
            ),
            "expected_output": "c4"
        },
        quizzes=[
            {
                "question": "What is the core principle of the 'Wolf Fence' debugging algorithm?",
                "options": [
                    "Placing diagnostic checkpoints at the midpoint to halve the suspect code area at each step",
                    "Encrypting network packets behind a firewall",
                    "Writing code inside Docker containers",
                    "Surrounding sensitive variables with mutex locks"
                ],
                "correct_answer": "Placing diagnostic checkpoints at the midpoint to halve the suspect code area at each step",
                "explanation": "The Wolf Fence uses binary search to divide and conquer suspect execution regions."
            },
            {
                "question": "What does the `git bisect` command do?",
                "options": [
                    "It performs a binary search through commit history to identify the exact commit that introduced a bug",
                    "It splits a Git branch into two parallel branches",
                    "It deletes merge conflicts automatically",
                    "It compresses git packfiles"
                ],
                "correct_answer": "It performs a binary search through commit history to identify the exact commit that introduced a bug",
                "explanation": "`git bisect` automates binary search through commits between known good and bad versions."
            },
            {
                "question": "If an application has 1,000 commits between the last good release and the current broken release, approximately how many steps does `git bisect` take to find the culprit?",
                "options": [
                    "About 10 steps ($2^{10} = 1024$)",
                    "1,000 steps",
                    "500 steps",
                    "50 steps"
                ],
                "correct_answer": "About 10 steps ($2^{10} = 1024$)",
                "explanation": "Binary search solves $N$ elements in $\\log_2 N$ steps; $\\log_2(1000) \\approx 10$."
            },
            {
                "question": "How can you fully automate `git bisect` so it runs without human intervention?",
                "options": [
                    "Using `git bisect run <test_script>`",
                    "Running `git commit --auto`",
                    "Setting up a cron job for `git pull`",
                    "Typing `git push --force`"
                ],
                "correct_answer": "Using `git bisect run <test_script>`",
                "explanation": "`git bisect run` accepts a test command/script and evaluates exit code 0 vs non-zero automatically."
            },
            {
                "question": "When debugging a long data processing pipeline, where should you place your first diagnostic checkpoint?",
                "options": [
                    "Approximately halfway through the pipeline, checking if intermediate data is corrupted",
                    "At the very end of the program only",
                    "On line 1 only",
                    "Inside external vendor packages"
                ],
                "correct_answer": "Approximately halfway through the pipeline, checking if intermediate data is corrupted",
                "explanation": "Checking the midpoint immediately clears or implicates 50% of the entire pipeline."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 10: Print Statement Debugging (Variable Checking Mastery)
    # ---------------------------------------------------------
    DayBlueprint(
        order=10,
        title="Day 10: Print Statement Debugging (Variable Checking Mastery)",
        concept="Print statement debugging is the universal, zero-dependency practice of inserting diagnostic output statements to inspect runtime variable state, types, and execution flow.",
        analogy="Print statements are like leaving neon sticky notes along a hiking trail in a dark forest. As you hike through the trail, the sticky notes show you: 'You made it to the river bridge at 10:05 AM, water level was 3 feet, and you took the left fork.' If you disappear, searchers follow the notes to the exact spot where things went wrong.",
        theory_sections=[
            {
                "heading": "Why Print Debugging Remains Essential",
                "content": (
                    "Despite advanced graphical IDE debuggers, print statements remain the fastest, most universal debugging tool across all programming environments (embedded hardware, remote SSH servers, serverless Lambdas, CI/CD runners, and quick scripts).\n\n"
                    "However, amateur print debugging (`print('here')`, `print('asdasd')`, `print(x)`) creates confusing terminal noise. Professional print debugging is **structured, informative, and unambiguous**."
                )
            },
            {
                "heading": "The 4 Hallmarks of Professional Print Statements",
                "content": (
                    "1. **Clear Context Label**: Never print bare values. Always print the variable name: `print(f'user_id={user_id}')`.\n"
                    "2. **Type and Length Telemetry**: When debugging collections or objects: `print(f'items: len={len(items)}, type={type(items)}')`.\n"
                    "3. **Exact Representation (`repr()` / `!r`)**: Distinguishes strings from numbers, and exposes hidden whitespace: `print(f'input={input_str!r}')` shows `' hello '` vs `'hello'`.\n"
                    "4. **Location Anchors**: Include function name or line tag: `print(f'[auth_middleware:42] token={token[:6]}...')`."
                )
            },
            {
                "heading": "Modern Print Shorthands (Python 3.8+ `=`)",
                "content": (
                    "In modern Python 3.8+, f-strings support the `=` specifier:\n"
                    "```python\n"
                    "user_id = 42\n"
                    "status = 'active'\n"
                    "print(f'{user_id=}, {status=}')\n"
                    "# Prints: user_id=42, status='active'\n"
                    "```\n"
                    "This outputs both the variable expression and its evaluated representation automatically."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Bad vs Professional Print Debugging",
                "language": "python",
                "code": (
                    "data = ' 450 '\n\n"
                    "# AMATEUR PRINT: Confusing and unhelpful\n"
                    "print(data)        # Output:  450  (hard to see leading/trailing spaces)\n"
                    "print('here 1')    # Clutters console\n\n"
                    "# PROFESSIONAL PRINT: Explicit, formatted, exposing types and whitespace\n"
                    "print(f'[DEBUG:calc_total] data={data!r}, type={type(data).__name__}')\n"
                    "# Output: [DEBUG:calc_total] data=' 450 ', type=str"
                ),
                "explanation": "`!r` uses `repr()`, immediately highlighting invisible spaces that cause parsing bugs."
            },
            {
                "title": "Python 3.8+ F-String Self-Documenting Expression (`=`)",
                "language": "python",
                "code": (
                    "import math\n\n"
                    "radius = 5.0\n"
                    "area = math.pi * (radius ** 2)\n\n"
                    "# The '=' specifier prints the expression name AND its value\n"
                    "print(f'{radius=}, {area=:.2f}')\n"
                    "# Output: radius=5.0, area=78.54"
                ),
                "explanation": "Drastically reduces boilerplate when logging multiple variable states."
            },
            {
                "title": "Tracing Control Flow Branches with Prints",
                "language": "python",
                "code": (
                    "def process_payment(amount, balance):\n"
                    "    print(f'[ENTER process_payment] {amount=}, {balance=}')\n"
                    "    if amount <= 0:\n"
                    "        print(' -> Branch: amount <= 0 (REJECTED)')\n"
                    "        return False\n"
                    "    if amount > balance:\n"
                    "        print(' -> Branch: amount > balance (INSUFFICIENT)')\n"
                    "        return False\n"
                    "    print(' -> Branch: SUCCESS')\n"
                    "    return True"
                ),
                "explanation": "Clearly marks which conditional branches executed during runtime."
            },
            {
                "title": "Using `icecream` for Next-Level Print Debugging",
                "language": "python",
                "code": (
                    "# Python 'icecream' library (pip install icecream)\n"
                    "from icecream import ic\n\n"
                    "def add(a, b):\n"
                    "    return a + b\n\n"
                    "x = 10\n"
                    "ic(x)\n"
                    "ic(add(x, 20))\n"
                    "# Outputs: ic| x: 10\n"
                    "# Outputs: ic| add(x, 20): 30"
                ),
                "explanation": "`ic()` automatically prints file, line number, expression, and value."
            }
        ],
        coding_challenge={
            "title": "Build a Diagnostic State Printer",
            "instructions": "Write a function `debug_dump(**kwargs)` that takes arbitrary keyword arguments and returns a formatted diagnostic string: `\"[DEBUG] key1='val1' (type), key2=10 (type)\"` sorted alphabetically by key.",
            "starter_code": (
                "def debug_dump(**kwargs) -> str:\n"
                "    # Format kwargs into clear debug output string\n"
                "    pass\n"
            ),
            "solution_code": (
                "def debug_dump(**kwargs) -> str:\n"
                "    parts = []\n"
                "    for k in sorted(kwargs.keys()):\n"
                "        val = kwargs[k]\n"
                "        parts.append(f\"{k}={val!r} ({type(val).__name__})\")\n"
                "    return f\"[DEBUG] {', '.join(parts)}\"\n\n"
                "print(debug_dump(user='Alice', age=25, active=True))"
            ),
            "expected_output": "[DEBUG] age=25 (int), active=True (bool), user='Alice' (str)"
        },
        quizzes=[
            {
                "question": "What is the primary danger of leaving `print('here')` or `print(x)` scattered in production code?",
                "options": [
                    "It pollutes production logs, degrades performance under high throughput, and lacks context for identifying sources",
                    "It crashes the Python virtual machine",
                    "It causes database tables to lock",
                    "It prevents unit tests from compiling"
                ],
                "correct_answer": "It pollutes production logs, degrades performance under high throughput, and lacks context for identifying sources",
                "explanation": "Ad-hoc prints clutter server logs, leak memory in stdout buffers, and expose internal state."
            },
            {
                "question": "What does the `!r` conversion flag do in a Python f-string (e.g. `f'{name!r}'`)?",
                "options": [
                    "It calls `repr()`, displaying explicit quotes and escaping hidden whitespace or control characters",
                    "It reverses the string",
                    "It converts text to uppercase",
                    "It replaces vowels with numbers"
                ],
                "correct_answer": "It calls `repr()`, displaying explicit quotes and escaping hidden whitespace or control characters",
                "explanation": "`repr()` reveals hidden characters (like trailing spaces or newlines `\\n`) that `str()` hides."
            },
            {
                "question": "In Python 3.8+, what does `print(f'{count=}')` output if `count = 15`?",
                "options": [
                    "count=15",
                    "15",
                    "=15",
                    "count"
                ],
                "correct_answer": "count=15",
                "explanation": "The `=` modifier in f-strings expands to the expression text followed by its evaluated value."
            },
            {
                "question": "Why is print statement debugging often preferred in serverless AWS Lambda or embedded microcontroller environments?",
                "options": [
                    "Because connecting interactive visual GUI debuggers to short-lived cloud lambdas or microcontrollers is complex or impossible",
                    "Because print statements run faster than C++",
                    "Because visual debuggers are banned on Linux",
                    "Because prints delete cache memory"
                ],
                "correct_answer": "Because connecting interactive visual GUI debuggers to short-lived cloud lambdas or microcontrollers is complex or impossible",
                "explanation": "Ephemeral serverless environments and hardware microcontrollers require zero-dependency stdout logging."
            },
            {
                "question": "What tool or practice is recommended before merging code to ensure temporary debug prints are cleaned up?",
                "options": [
                    "Git pre-commit hooks, linters (Flake8/ESLint), or code review diff inspections",
                    "Rebooting the laptop",
                    "Clearing the browser cookies",
                    "Disabling all unit tests"
                ],
                "correct_answer": "Git pre-commit hooks, linters (Flake8/ESLint), or code review diff inspections",
                "explanation": "Linters can flag or block `print` or `console.log` statements before pull requests merge."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 11: Reading the Manual (RTFM) & Official Documentation
    # ---------------------------------------------------------
    DayBlueprint(
        order=11,
        title="Day 11: Reading the Manual (RTFM) & Official Documentation",
        concept="Official documentation, RFC standards, and API specifications are the primary source of truth for software contracts, deprecations, and parameter specifications.",
        analogy="Trying to assemble an intricate mechanical watch by guessing or watching random 15-second TikTok videos will leave you with broken gears. The Swiss watchmaker's official engineering schematic (the manual) tells you the exact torque for every microscopic screw.",
        theory_sections=[
            {
                "heading": "The Engineering Cost of Skipping Documentation",
                "content": (
                    "Software engineers waste thousands of hours debugging 'mysterious issues' that were explicitly documented in the first paragraph of the library's official manual:\n"
                    "- *'Note: This method returns a new copy; it does not mutate in place.'*\n"
                    "- *'Warning: `timeout` is measured in milliseconds, not seconds.'*\n"
                    "- *'Deprecated in v3.0: Use `fetch_by_id` instead.'*\n\n"
                    "Reading the official documentation (RTFM: 'Read The Fine Manual') for 5 minutes prevents 5 hours of frustrating guesswork."
                )
            },
            {
                "heading": "How to Read Official Documentation Efficiently",
                "content": (
                    "Do not read 800 pages of documentation cover-to-cover like a novel. Follow an active reading strategy:\n"
                    "1. **Check Version Compatibility**: Ensure the docs you are reading match your installed version (`v2.4` docs vs `v4.1` installed).\n"
                    "2. **Function Signature & Types**: What parameters are required vs optional? What are their default values? What type does it return?\n"
                    "3. **Exceptions Thrown**: What errors does the documentation state this function can raise under failure?\n"
                    "4. **Notes & Gotchas Callouts**: Look for colored warning/caution blocks."
                )
            },
            {
                "heading": "In-Editor Documentation (Docstrings & Type Stubs)",
                "content": (
                    "You don't always need to open a web browser. Modern IDEs provide instant documentation:\n"
                    "- Hovering over a symbol in VS Code / PyCharm.\n"
                    "- In Python interactive REPL: `help(requests.get)` or `dir(object)`.\n"
                    "- In terminal: `man git-rebase`."
                )
            }
        ],
        code_snippets=[
            {
                "title": "A Classic 'Did Not Read Documentation' Bug (sort vs sorted)",
                "language": "python",
                "code": (
                    "# Developer expects list.sort() to return the sorted list\n"
                    "items = [5, 2, 8, 1]\n"
                    "# BUG: The documentation explicitly states list.sort() mutates IN PLACE and returns None!\n"
                    "result = items.sort()\n"
                    "print(f'{result=}') # result=None! (Items was mutated, but result is None)\n\n"
                    "# Correct usage per documentation:\n"
                    "items.sort() # items is now [1, 2, 5, 8]\n"
                    "# Or using the sorted() built-in function:\n"
                    "sorted_items = sorted([5, 2, 8, 1]) # returns new sorted list"
                ),
                "explanation": "Official docs clearly specify `list.sort()` returns `None` to remind callers of in-place mutation."
            },
            {
                "title": "Inspecting Documentation Directly in Python REPL",
                "language": "python",
                "code": (
                    "import math\n\n"
                    "# Use help() to view official docstring, parameters, and exceptions\n"
                    "# help(math.sqrt)\n"
                    "# sqrt(x, /)\n"
                    "#    Return the square root of x.\n"
                    "#    Raises ValueError if x is negative."
                ),
                "explanation": "Built-in `help()` provides instantaneous documentation without leaving the terminal."
            },
            {
                "title": "Another Common Gotcha: String replace() Immutability",
                "language": "python",
                "code": (
                    "# Developer thinks strings mutate in place\n"
                    "url = 'http://example.com/api'\n"
                    "url.replace('http:', 'https:') # Strings are immutable! Returns new string\n"
                    "print(url) # Still 'http://example.com/api'!\n\n"
                    "# Correct usage:\n"
                    "url = url.replace('http:', 'https:')\n"
                    "print(url) # 'https://example.com/api'"
                ),
                "explanation": "Reading docs confirms Python strings are immutable; string methods always return new objects."
            },
            {
                "title": "Reading Function Signatures & Default Parameters",
                "language": "python",
                "code": (
                    "import inspect\n\n"
                    "# Programmatically inspecting function signature and defaults\n"
                    "sig = inspect.signature(round)\n"
                    "print(f'Signature: {sig}') # Signature: (number, ndigits=None)"
                ),
                "explanation": "Inspect module reveals parameter names, types, and defaults programmatically."
            }
        ],
        coding_challenge={
            "title": "Inspect Function Docstring and Default Arguments",
            "instructions": "Write a function `get_arg_defaults(fn)` using Python's `inspect` module that returns a dictionary mapping parameter names to their default values for any function that has defaults. If a parameter has no default, do not include it in the dictionary.",
            "starter_code": (
                "import inspect\n\n"
                "def get_arg_defaults(fn) -> dict:\n"
                "    # Return dict of parameter_name: default_value\n"
                "    pass\n"
            ),
            "solution_code": (
                "import inspect\n\n"
                "def get_arg_defaults(fn) -> dict:\n"
                "    sig = inspect.signature(fn)\n"
                "    defaults = {}\n"
                "    for param in sig.parameters.values():\n"
                "        if param.default is not inspect.Parameter.empty:\n"
                "            defaults[param.name] = param.default\n"
                "    return defaults\n\n"
                "def example(a, b=10, c='test'): pass\n"
                "print(get_arg_defaults(example))"
            ),
            "expected_output": "{'b': 10, 'c': 'test'}"
        },
        quizzes=[
            {
                "question": "Why does `my_list.sort()` in Python return `None` instead of the sorted list?",
                "options": [
                    "By deliberate API design, to signal that the operation mutates the list in-place rather than allocating a new copy",
                    "Because sorting failed",
                    "Because Python cannot return lists from methods",
                    "Because it is a bug in the Python compiler"
                ],
                "correct_answer": "By deliberate API design, to signal that the operation mutates the list in-place rather than allocating a new copy",
                "explanation": "Python's design philosophy dictates that in-place mutators return `None` to prevent accidental assignment bugs."
            },
            {
                "question": "What is the very first thing you should verify when reading online library documentation?",
                "options": [
                    "Whether the documentation version matches the exact version of the library installed in your project",
                    "The color scheme of the website",
                    "The biography of the author",
                    "The company stock price"
                ],
                "correct_answer": "Whether the documentation version matches the exact version of the library installed in your project",
                "explanation": "Reading v4 documentation while using a v2 library leads to invalid method calls and breaking incompatibilities."
            },
            {
                "question": "Which Python built-in function displays the interactive manual and docstring for any module or function in the terminal?",
                "options": [
                    "`help()`",
                    "`docs()`",
                    "`man()`",
                    "`info()`"
                ],
                "correct_answer": "`help()`",
                "explanation": "`help(object)` opens Python's interactive paged documentation."
            },
            {
                "question": "Why does `text.replace('a', 'b')` not modify the variable `text` in Python?",
                "options": [
                    "Strings in Python are immutable; methods cannot change existing strings and must return new string instances",
                    "Because `replace` is only supported in JavaScript",
                    "Because variables cannot be modified after declaration",
                    "Because `text` must be encrypted first"
                ],
                "correct_answer": "Strings in Python are immutable; methods cannot change existing strings and must return new string instances",
                "explanation": "Immutability guarantees string contents cannot be altered in-place; the return value must be captured."
            },
            {
                "question": "What does RFC stand for in internet and API standards documentation (e.g. RFC 7807)?",
                "options": [
                    "Request for Comments",
                    "Remote File Configuration",
                    "Real Functional Code",
                    "Root Factory Component"
                ],
                "correct_answer": "Request for Comments",
                "explanation": "RFC documents are the official publication standard for the Internet Engineering Task Force (IETF)."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 12: Smart Googling & Researching Technical Issues
    # ---------------------------------------------------------
    DayBlueprint(
        order=12,
        title="Day 12: Smart Googling & Researching Technical Issues",
        concept="Smart technical querying strips localized noise from error messages, leverages search operators, and navigates StackOverflow, GitHub Issues, and release notes to find verified solutions.",
        analogy="Googling a bug poorly is like calling the police and saying 'A person in a shirt took something from my place.' Googling a bug skillfully is giving the police the exact license plate, vehicle make, model, time of theft, and street intersection.",
        theory_sections=[
            {
                "heading": "The Anatomy of an Error Search Query",
                "content": (
                    "When an error occurs, amateur developers copy the entire 20-line stack trace into Google:\n"
                    "`Traceback ... File C:/Users/Bob/Desktop/secret_app/main.py line 42 in my_func KeyError: 'token'`\n\n"
                    "Google will fail because nobody else on Earth has a file path `C:/Users/Bob/Desktop/secret_app/main.py`!\n"
                    "**Strip localized noise**:\n"
                    "- Strip file paths, line numbers, variable names, and project names.\n"
                    "- Keep: Framework name + Exact Exception Type + Core Error Phrase:\n"
                    "`FastAPI KeyError Authorization header missing`."
                )
            },
            {
                "heading": "Power Search Operators for Engineers",
                "content": (
                    "- **Exact Match Quotes (`\"...\"`)**: `\"TypeError: 'NoneType' object is not callable\"`.\n"
                    "- **Site Restriction (`site:...`)**: Search where real engineering discussions happen:\n"
                    "  - `site:github.com/encode/fastapi/issues` (Find open/closed GitHub issues).\n"
                    "  - `site:stackoverflow.com`.\n"
                    "- **Exclude Terms (`-...`)**: `python asyncio timeout -tornado` (exclude unwanted frameworks).\n"
                    "- **Date Filtering**: Bugs in modern React or Next.js change rapidly; filter search results to 'Past 1 Year' to avoid obsolete v14 advice."
                )
            },
            {
                "heading": "GitHub Issues: The Developer's Secret Weapon",
                "content": (
                    "When third-party libraries break (especially following an update), the bug is rarely on StackOverflow yet. It is in the **library's GitHub Issues tracker**:\n"
                    "1. Search both **Open** and **Closed** issues.\n"
                    "2. Look for workarounds posted by maintainers or community members.\n"
                    "3. Check the repository's `CHANGELOG.md` or Release Notes for breaking changes."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Raw Stack Trace with Localized Noise",
                "language": "text",
                "code": (
                    "# RAW TRACE (DO NOT SEARCH THIS DIRECTLY!):\n"
                    "Traceback (most recent call last):\n"
                    "  File \"/home/ahmed/dev/fintech_super_app/services/billing.py\", line 124, in process_invoice\n"
                    "    response = requests.post(url, json=payload, timeout=3)\n"
                    "  File \"/home/ahmed/.venv/lib/python3.11/site-packages/requests/api.py\", line 115, in post\n"
                    "requests.exceptions.SSLError: HTTPSConnectionPool(host='api.stripe.com', port=443): \\\n"
                    "Max retries exceeded with url: /v1/invoices (Caused by SSLError(SSLCertVerificationError(1, \\\n"
                    "'[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain (_ssl.c:1006)')))"
                ),
                "explanation": "Contains user file paths, personal line numbers, and specific endpoint paths that pollute search queries."
            },
            {
                "title": "Extracted Smart Search Query",
                "language": "text",
                "code": (
                    "# SMART SEARCH QUERIES:\n"
                    "# Query 1 (Broad):\n"
                    "python requests \"certificate verify failed: self-signed certificate in certificate chain\"\n\n"
                    "# Query 2 (Targeted GitHub Issues):\n"
                    "site:github.com/psf/requests/issues \"self-signed certificate in certificate chain\"\n\n"
                    "# Query 3 (Corporate Proxy Context):\n"
                    "python requests SSLError corporate proxy REQUESTS_CA_BUNDLE"
                ),
                "explanation": "Stripping paths leaves the universal core error signature, yielding exact matches."
            },
            {
                "title": "Regex Error Sanitizer in Python",
                "language": "python",
                "code": (
                    "import re\n\n"
                    "def sanitize_error_for_search(raw_error: str) -> str:\n"
                    "    # Remove local file paths (e.g. /home/... or C:\\...)\n"
                    "    no_paths = re.sub(r'(\\/[\\w.-]+)+|([A-Za-z]:\\\\[\\w\\\\.-]+)', '', raw_error)\n"
                    "    # Remove line number references\n"
                    "    no_lines = re.sub(r'line \\d+', '', no_paths)\n"
                    "    # Collapse whitespace\n"
                    "    return ' '.join(no_lines.split())\n\n"
                    "raw = 'File \"C:/Users/Zara/app.py\", line 42, in run: ValueError: Invalid token'\n"
                    "print(sanitize_error_for_search(raw))"
                ),
                "explanation": "Demonstrates programmatic removal of localized path strings."
            },
            {
                "title": "Verifying Solutions from GitHub Issues",
                "language": "python",
                "code": (
                    "# Discovered solution from GitHub issue #4521:\n"
                    "# Set REQUESTS_CA_BUNDLE environment variable or specify cert bundle path\n"
                    "import os, requests\n\n"
                    "# Set path to corporate root cert discovered via documentation\n"
                    "# os.environ['REQUESTS_CA_BUNDLE'] = '/etc/ssl/certs/corporate-ca.crt'\n"
                    "# response = requests.post('https://api.stripe.com/v1/invoices', ...)"
                ),
                "explanation": "Applies documented fix resolved in official repository issue tracker."
            }
        ],
        coding_challenge={
            "title": "Automate Search Query Generation from Exception",
            "instructions": "Write a function `build_search_query(framework_name, exception_obj)` that takes a framework string (e.g. `'Flask'`) and an Exception instance, returning a clean search string in the format: `\"<framework> <ExceptionType>: <first_sentence_of_message>\"`.",
            "starter_code": (
                "def build_search_query(framework: str, exc: Exception) -> str:\n"
                "    # Return clean query without localized data\n"
                "    pass\n"
            ),
            "solution_code": (
                "def build_search_query(framework: str, exc: Exception) -> str:\n"
                "    exc_type = type(exc).__name__\n"
                "    msg = str(exc).split('\\n')[0].strip()\n"
                "    return f\"{framework} {exc_type}: {msg}\"\n\n"
                "sample_err = KeyError('token is required')\n"
                "print(build_search_query('FastAPI', sample_err))"
            ),
            "expected_output": "FastAPI KeyError: 'token is required'"
        },
        quizzes=[
            {
                "question": "What is the primary mistake developers make when searching for an error message on Google?",
                "options": [
                    "Copy-pasting local file paths and line numbers that are unique to their laptop, preventing Google from finding matches",
                    "Searching in English instead of Latin",
                    "Using Google Chrome instead of Safari",
                    "Searching during evening hours"
                ],
                "correct_answer": "Copy-pasting local file paths and line numbers that are unique to their laptop, preventing Google from finding matches",
                "explanation": "Localized file paths (e.g. `/Users/john/...`) make search queries unique to your machine, returning zero results."
            },
            {
                "question": "Which search operator restricts your Google search to discussions inside a specific repository's issue tracker?",
                "options": [
                    "`site:github.com/<owner>/<repo>/issues`",
                    "`repo:all`",
                    "`find:issues`",
                    "`filter:github`"
                ],
                "correct_answer": "`site:github.com/<owner>/<repo>/issues`",
                "explanation": "The `site:` operator restricts search queries strictly to the designated URL path."
            },
            {
                "question": "What do double quotes around a search term (e.g. `\"ZeroDivisionError: float division by zero\"`) enforce in search engines?",
                "options": [
                    "Exact verbatim phrase matching, ensuring results contain the exact error string in order",
                    "Searching only on dark web forums",
                    "Translating the query into C++",
                    "Ignoring punctuation"
                ],
                "correct_answer": "Exact verbatim phrase matching, ensuring results contain the exact error string in order",
                "explanation": "Enclosing text in quotes forces search engines to match the exact string sequence without word substitution."
            },
            {
                "question": "Why is checking the GitHub Issues tracker often superior to StackOverflow when dealing with modern, fast-evolving open-source libraries?",
                "options": [
                    "Bugs, breaking changes, and workarounds are discussed by library maintainers directly on GitHub before they ever appear on StackOverflow",
                    "StackOverflow was shut down in 2020",
                    "GitHub issues are written in binary",
                    "GitHub does not allow search queries"
                ],
                "correct_answer": "Bugs, breaking changes, and workarounds are discussed by library maintainers directly on GitHub before they ever appear on StackOverflow",
                "explanation": "Maintainers and early adopters track regressions and edge cases in real-time in GitHub Issues."
            },
            {
                "question": "Why is it important to filter search results by date (e.g. 'Past 1 Year') when researching frontend web framework errors (like Next.js or React)?",
                "options": [
                    "Frontend frameworks evolve rapidly, so answers from 5 years ago often use obsolete APIs that break modern builds",
                    "Old answers are deleted by Google automatically",
                    "Browsers refuse to render old JavaScript",
                    "To save hard drive disk space"
                ],
                "correct_answer": "Frontend frameworks evolve rapidly, so answers from 5 years ago often use obsolete APIs that break modern builds",
                "explanation": "Rapid release cycles make legacy solutions obsolete; recent threads reflect current framework architectures."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 13: Reading Error Messages & Diagnostics
    # ---------------------------------------------------------
    DayBlueprint(
        order=13,
        title="Day 13: Reading Error Messages & Diagnostics",
        concept="Error messages are not roadblocks; they are precise diagnostic reports generated by compilers and runtimes detailing the error category, location, and violation reason.",
        analogy="When the check engine light in a modern car turns on, the dashboard diagnostic scanner doesn't say 'Car Broken.' It outputs code `P0301: Cylinder 1 Misfire Detected`. An error message in software is that exact diagnostic code, telling you precisely which cylinder misfired.",
        theory_sections=[
            {
                "heading": "The Anatomy of an Error Message",
                "content": (
                    "Every standardized error message consists of three distinct parts:\n"
                    "1. **The Error Type / Class**: `TypeError`, `ValueError`, `IndexError`, `SyntaxError`. This categorizes the conceptual rule that was broken.\n"
                    "2. **The Error Description**: Detailed context: `unsupported operand type(s) for +: 'int' and 'str'`. This tells you what operation was attempted and why it was illegal.\n"
                    "3. **The Target Location**: File name, function name, and line number where the runtime detected the illegality."
                )
            },
            {
                "heading": "Reading from the Bottom Up",
                "content": (
                    "Beginner developers panic when they see a 50-line red wall of text, so they look at line 1 and give up.\n\n"
                    "**Crucial Rule**: In languages like Python, Node.js, and Java, **always read the error message from the very bottom first**!\n"
                    "- The very last line is the actual exception and description.\n"
                    "- As you scan upward, you see the stack trace leading back to your application code."
                )
            },
            {
                "heading": "Common Standard Exceptions Decoded",
                "content": (
                    "- `TypeError`: Operation applied to an inappropriate type (e.g. `len(5)`).\n"
                    "- `ValueError`: Operation received correct type, but inappropriate value (e.g. `int('abc')`).\n"
                    "- `AttributeError`: Attempting to access a property or method that does not exist on that object (`user.profile_url` when `user` has no `profile_url`).\n"
                    "- `KeyError`: Dictionary key does not exist.\n"
                    "- `IndexError`: Array or list sequence index out of bounds."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Reading a Python Error Message",
                "language": "python",
                "code": (
                    "# Code that generates a TypeError\n"
                    "def format_greeting(name, count):\n"
                    "    return 'Hello ' + name + '! You have ' + count + ' messages.'\n\n"
                    "# format_greeting('Sara', 5)\n"
                    "# Output:\n"
                    "# Traceback (most recent call last):\n"
                    "#   File \"app.py\", line 2, in format_greeting\n"
                    "#     return 'Hello ' + name + '! You have ' + count + ' messages.'\n"
                    "# TypeError: can only concatenate str (not \"int\") to str"
                ),
                "explanation": "The last line gives the exact failure reason: `count` is an `int` being concatenated to `str`."
            },
            {
                "title": "Fixing the TypeError via F-String",
                "language": "python",
                "code": (
                    "def format_greeting_fixed(name: str, count: int) -> str:\n"
                    "    # F-strings automatically convert variables to their string representation\n"
                    "    return f'Hello {name}! You have {count} messages.'\n\n"
                    "print(format_greeting_fixed('Sara', 5))"
                ),
                "explanation": "F-strings perform interpolation safely without explicit type casting."
            },
            {
                "title": "Decoding an AttributeError",
                "language": "python",
                "code": (
                    "class User:\n"
                    "    def __init__(self, username):\n"
                    "        self.username = username\n\n"
                    "u = User('tariq')\n"
                    "try:\n"
                    "    print(u.email) # AttributeError: 'User' object has no attribute 'email'\n"
                    "except AttributeError as e:\n"
                    "    print(f'Caught expected error: {e}')\n"
                    "    # Safe fallback using getattr\n"
                    "    print(f'Fallback email: {getattr(u, \"email\", \"no-email@example.com\")}')"
                ),
                "explanation": "AttributeError indicates an uninitialized or misspelled attribute name on an object instance."
            },
            {
                "title": "Decoding JavaScript TypeError: Cannot read property of undefined",
                "language": "javascript",
                "code": (
                    "const order = { id: 101 };\n"
                    "// In JS: TypeError: Cannot read properties of undefined (reading 'street')\n"
                    "// console.log(order.shippingAddress.street);\n\n"
                    "// FIX: Optional chaining (?.) prevents crashes when intermediate properties are missing\n"
                    "console.log(order.shippingAddress?.street ?? 'No street provided');"
                ),
                "explanation": "Demonstrates the universal nature of type exceptions across programming languages."
            }
        ],
        coding_challenge={
            "title": "Parse and Categorize Error Message Strings",
            "instructions": "Write a function `categorize_error(error_line)` that takes a string like `\"TypeError: unsupported operand\"` or `\"KeyError: 'id'\"` and returns a tuple `(error_type, error_message)`. If no colon is present, return `('Unknown', error_line)`.",
            "starter_code": (
                "def categorize_error(line: str) -> tuple:\n"
                "    # Split line into (type, message)\n"
                "    pass\n"
            ),
            "solution_code": (
                "def categorize_error(line: str) -> tuple:\n"
                "    if ':' in line:\n"
                "        parts = line.split(':', 1)\n"
                "        return (parts[0].strip(), parts[1].strip())\n"
                "    return ('Unknown', line.strip())\n\n"
                "print(categorize_error(\"TypeError: can only concatenate str to str\"))\n"
                "print(categorize_error(\"Generic failure occurred\"))"
            ),
            "expected_output": "('TypeError', 'can only concatenate str to str')\n('Unknown', 'Generic failure occurred')"
        },
        quizzes=[
            {
                "question": "When reading a long Python or Node.js error stack trace, where should your eyes look first?",
                "options": [
                    "At the very bottom line, which contains the exact exception class and root failure description",
                    "At line 1 only",
                    "In the exact middle of the text block",
                    "At the operating system kernel log"
                ],
                "correct_answer": "At the very bottom line, which contains the exact exception class and root failure description",
                "explanation": "Standard tracebacks conclude with the specific exception type and explanatory message."
            },
            {
                "question": "What does a `TypeError` communicate to the developer?",
                "options": [
                    "An operation or function was applied to an object of inappropriate or incompatible data type",
                    "The keyboard was typed too fast",
                    "A variable name was spelled incorrectly in HTML",
                    "The hard drive is out of storage"
                ],
                "correct_answer": "An operation or function was applied to an object of inappropriate or incompatible data type",
                "explanation": "TypeErrors occur when operations (e.g. mathematical addition or indexing) are applied to unsupported types."
            },
            {
                "question": "What is the difference between a `TypeError` and a `ValueError` in Python?",
                "options": [
                    "`TypeError` means wrong data type (e.g. string instead of int); `ValueError` means correct type but invalid content (e.g. `int('hello')`)",
                    "There is no difference",
                    "`ValueError` only occurs in databases",
                    "`TypeError` only occurs in web browsers"
                ],
                "correct_answer": "`TypeError` means wrong data type (e.g. string instead of int); `ValueError` means correct type but invalid content (e.g. `int('hello')`)",
                "explanation": "`int('hello')` receives a string (valid type for `int()`), but the contents cannot be parsed as a base-10 integer."
            },
            {
                "question": "What does the JavaScript error `TypeError: Cannot read properties of undefined` signify?",
                "options": [
                    "You attempted to access a property on a variable that evaluates to `undefined` or `null`",
                    "The variable is defined twice",
                    "The browser has disabled JavaScript",
                    "The CSS stylesheet failed to load"
                ],
                "correct_answer": "You attempted to access a property on a variable that evaluates to `undefined` or `null`",
                "explanation": "Trying to navigate nested properties (e.g. `user.address.street`) when `user.address` is undefined throws this error."
            },
            {
                "question": "What does an `IndexError: list index out of range` indicate?",
                "options": [
                    "You attempted to access a list element at an offset index that does not exist in the collection",
                    "The list contains too many items",
                    "The list items are not sorted",
                    "The list contains negative values"
                ],
                "correct_answer": "You attempted to access a list element at an offset index that does not exist in the collection",
                "explanation": "Accessing `arr[5]` when the list only contains 3 items violates memory bounds, triggering an IndexError."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 14: Understanding Stack Traces & Tracebacks
    # ---------------------------------------------------------
    DayBlueprint(
        order=14,
        title="Day 14: Understanding Stack Traces & Tracebacks",
        concept="A stack trace (traceback) is a historical snapshot of the call stack at the moment of an exception, detailing the exact chain of function calls leading from entry point to point of failure.",
        analogy="A stack trace is like the black box flight recorder of an airplane. When an incident occurs, the flight recorder doesn't just record the moment of impact; it plays back every command: 'Pilot called copilot at 20,000 feet, copilot engaged flap control, flap control triggered hydraulic valve 4, hydraulic valve 4 jammed.'",
        theory_sections=[
            {
                "heading": "The Call Stack: How Function Execution Works",
                "content": (
                    "Whenever your program calls a function, the computer creates a **Stack Frame** in memory containing that function's local variables and return address, pushing it onto the **Call Stack** (LIFO: Last In, First Out):\n"
                    "- `main()` calls `handle_request()`\n"
                    "- `handle_request()` calls `validate_auth()`\n"
                    "- `validate_auth()` calls `decode_jwt()`\n\n"
                    "If `decode_jwt()` crashes, the runtime unwinds the call stack and prints the complete journey in order. This printout is the **Stack Trace**."
                )
            },
            {
                "heading": "Differentiating Library Code from Your Application Code",
                "content": (
                    "In modern web applications (Django, FastAPI, Express), a stack trace might contain 40 frames. 36 of those frames are internal library code (`site-packages/uvicorn/...`, `site-packages/starlette/...`).\n\n"
                    "**Crucial Skill: Identifying the Pivot Frame**:\n"
                    "- Ignore internal framework boilerplates.\n"
                    "- Scan from the bottom upward until you see the **last line of code that YOU wrote** in your own project directory.\n"
                    "- That pivot frame is where your code made the invalid call that triggered the downstream explosion."
                )
            },
            {
                "heading": "Programmatic Traceback Inspection (`traceback` module)",
                "content": (
                    "In production systems, you don't just let tracebacks print to stdout. You capture them programmatically using Python's `traceback` module to format, log, and send them to error monitors like Sentry or Datadog without terminating the server."
                )
            }
        ],
        code_snippets=[
            {
                "title": "A Multi-Level Call Stack Crash",
                "language": "python",
                "code": (
                    "def step_three(data):\n"
                    "    # Crash point: division by zero\n"
                    "    return 100 / data['divisor']\n\n"
                    "def step_two(data):\n"
                    "    return step_three(data) + 5\n\n"
                    "def step_one(data):\n"
                    "    return step_two(data) * 2\n\n"
                    "# step_one({'divisor': 0})\n"
                    "# Traceback shows the chain: step_one -> step_two -> step_three"
                ),
                "explanation": "Illustrates how each nested call is recorded in the unwinding stack trace."
            },
            {
                "title": "Capturing Tracebacks Programmatically in Python",
                "language": "python",
                "code": (
                    "import traceback\n\n"
                    "try:\n"
                    "    step_one({'divisor': 0})\n"
                    "except ZeroDivisionError:\n"
                    "    # Capture formatted traceback string for logging\n"
                    "    tb_str = traceback.format_exc()\n"
                    "    print('LOGGED ERROR TO MONITORING:')\n"
                    "    # Print the last 2 lines of the formatted trace\n"
                    "    print('\\n'.join(tb_str.strip().split('\\n')[-2:]))"
                ),
                "explanation": "`traceback.format_exc()` retrieves the complete stack trace string inside an except block."
            },
            {
                "title": "Inspecting Stack Frames with `traceback.extract_tb()`",
                "language": "python",
                "code": (
                    "import sys, traceback\n\n"
                    "try:\n"
                    "    val = [1, 2][99]\n"
                    "except IndexError:\n"
                    "    _, _, tb = sys.exc_info()\n"
                    "    frames = traceback.extract_tb(tb)\n"
                    "    last_frame = frames[-1]\n"
                    "    print(f'File: {last_frame.filename}')\n"
                    "    print(f'Line: {last_frame.lineno}')\n"
                    "    print(f'Function: {last_frame.name}')\n"
                    "    print(f'Code: {last_frame.line}')"
                ),
                "explanation": "Extracts granular file, line number, and function attributes from traceback objects."
            },
            {
                "title": "Node.js Error Stack Trace Inspection",
                "language": "javascript",
                "code": (
                    "function processOrder() {\n"
                    "  throw new Error('Payment gateway timeout');\n"
                    "}\n\n"
                    "try {\n"
                    "  processOrder();\n"
                    "} catch (err) {\n"
                    "  console.log('Error Name:', err.name);\n"
                    "  console.log('Error Message:', err.message);\n"
                    "  // err.stack contains the complete multi-frame call stack string\n"
                    "  console.log('First Stack Frame:', err.stack.split('\\n')[1].trim());\n"
                    "}"
                ),
                "explanation": "Demonstrates identical stack trace capture principles in JavaScript/Node.js."
            }
        ],
        coding_challenge={
            "title": "Extract the Originating File and Line from Traceback",
            "instructions": "Write a function `parse_crash_location(tb_string)` that parses a standard Python traceback string and extracts a dictionary with `'filename'`, `'line_number'` (as int), and `'function_name'` corresponding to the *final* frame (where the error actually occurred).",
            "starter_code": (
                "def parse_crash_location(tb_text: str) -> dict:\n"
                "    # Return {'filename': ..., 'line_number': ..., 'function_name': ...}\n"
                "    pass\n"
            ),
            "solution_code": (
                "import re\n\n"
                "def parse_crash_location(tb_text: str) -> dict:\n"
                "    # Pattern: File \"...\", line ..., in ...\n"
                "    matches = re.findall(r'File \"([^\"]+)\", line (\\d+), in (\\w+)', tb_text)\n"
                "    if not matches:\n"
                "        return {}\n"
                "    last_match = matches[-1]\n"
                "    return {\n"
                "        'filename': last_match[0],\n"
                "        'line_number': int(last_match[1]),\n"
                "        'function_name': last_match[2]\n"
                "    }\n\n"
                "sample_tb = '''\n"
                "Traceback (most recent call last):\n"
                "  File \"main.py\", line 10, in run\n"
                "    calc()\n"
                "  File \"math_ops.py\", line 42, in calc\n"
                "    1 / 0\n"
                "ZeroDivisionError: division by zero\n"
                "'''\n"
                "print(parse_crash_location(sample_tb))"
            ),
            "expected_output": "{'filename': 'math_ops.py', 'line_number': 42, 'function_name': 'calc'}"
        },
        quizzes=[
            {
                "question": "What is a 'Stack Trace' (Traceback)?",
                "options": [
                    "A sequential snapshot of active function call frames showing the path execution took leading up to an exception",
                    "A list of installed Python libraries",
                    "A list of database indexes",
                    "A record of git commit hashes"
                ],
                "correct_answer": "A sequential snapshot of active function call frames showing the path execution took leading up to an exception",
                "explanation": "A stack trace reveals the exact nested call sequence active at the moment of failure."
            },
            {
                "question": "In a 30-frame traceback involving third-party framework libraries, what is the 'pivot frame' you should look for?",
                "options": [
                    "The last frame containing code you or your team wrote in your application codebase",
                    "The very first line of the framework kernel",
                    "A random line in the middle",
                    "The Python C-source engine"
                ],
                "correct_answer": "The last frame containing code you or your team wrote in your application codebase",
                "explanation": "The pivot frame reveals the argument or call in your own code that triggered downstream library exceptions."
            },
            {
                "question": "Which Python standard module allows capturing and formatting exception tracebacks as strings for logging?",
                "options": [
                    "`traceback`",
                    "`syslog`",
                    "`inspect_errors`",
                    "`debugger`"
                ],
                "correct_answer": "`traceback`",
                "explanation": "Python's `traceback` module provides utilities like `format_exc()` to inspect tracebacks programmatically."
            },
            {
                "question": "What data structure does the CPU/runtime use to manage active function calls and their local variables?",
                "options": [
                    "A Call Stack (LIFO: Last-In, First-Out)",
                    "A Queue (FIFO: First-In, First-Out)",
                    "A Hash Table",
                    "A Circular Ring Buffer"
                ],
                "correct_answer": "A Call Stack (LIFO: Last-In, First-Out)",
                "explanation": "Function frames are pushed on call and popped on return using a LIFO stack."
            },
            {
                "question": "What happens to the Call Stack if a recursive function calls itself infinitely without a base case?",
                "options": [
                    "A `RecursionError` / Stack Overflow occurs when available call stack memory is exhausted",
                    "The computer automatically reboots",
                    "The function starts running in reverse",
                    "The list is cleared"
                ],
                "correct_answer": "A `RecursionError` / Stack Overflow occurs when available call stack memory is exhausted",
                "explanation": "Unbounded recursion pushes infinite frames until reaching maximum call stack limits."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 15: Exception Handling Basics (Try, Except, Else, Finally)
    # ---------------------------------------------------------
    DayBlueprint(
        order=15,
        title="Day 15: Exception Handling Basics (Try, Except, Else, Finally)",
        concept="Structured exception handling intercepts runtime errors gracefully using try, except/catch, else, and finally blocks, preventing unexpected crashes and guaranteeing resource cleanup.",
        analogy="Exception handling is like wearing a trapeze safety net. The acrobat performs their dangerous routine in the air (`try`). If they slip and fall (`except`), they land safely in the net without breaking their neck. And no matter whether they landed the trick or fell into the net, the stage lights are always turned off at closing time (`finally`).",
        theory_sections=[
            {
                "heading": "The 4 Pillars of Structured Exception Handling",
                "content": (
                    "In Python, structured exception handling consists of 4 complementary blocks:\n"
                    "1. `try`: Code that carries risk of failure (network calls, file I/O, parsing).\n"
                    "2. `except <SpecificException>`: Runs ONLY if that specific exception occurs. Intercepts the error and handles remediation.\n"
                    "3. `else`: Runs ONLY if the `try` block succeeded with **zero exceptions**. Excellent for actions that should only proceed on guaranteed success.\n"
                    "4. `finally`: Runs **unconditionally** no matter what happened (success, caught error, or unhandled crash). Essential for closing files, database connections, and releasing locks."
                )
            },
            {
                "heading": "The Cardinal Sin: Bare `except:` or `except Exception:`",
                "content": (
                    "Never write:\n"
                    "```python\n"
                    "try:\n"
                    "    do_work()\n"
                    "except:\n"
                    "    pass # EVIL ANTIPATTERN!\n"
                    "```\n"
                    "A bare `except:` intercepts **everything**, including `KeyboardInterrupt` (Ctrl+C to stop the script) and `SystemExit`! Always catch specific exceptions (`except (ValueError, KeyError):`)."
                )
            },
            {
                "heading": "Context Managers (`with` statement) as Syntactic Sugar",
                "content": (
                    "The `finally` block is so critical for closing files and network sockets that Python introduced the **Context Manager** (`with open(...) as f:`). The context manager guarantees `f.close()` is called automatically on exit, even if an exception explodes inside the block."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Comprehensive Try / Except / Else / Finally Block",
                "language": "python",
                "code": (
                    "def read_numeric_config(filepath):\n"
                    "    f = None\n"
                    "    try:\n"
                    "        print('1. Opening file...')\n"
                    "        f = open(filepath, 'r')\n"
                    "        content = f.read().strip()\n"
                    "        val = int(content)\n"
                    "    except FileNotFoundError:\n"
                    "        print('2. Caught FileNotFoundError! Using default 100.')\n"
                    "        val = 100\n"
                    "    except ValueError:\n"
                    "        print('2. Caught ValueError (not a number)! Using default 100.')\n"
                    "        val = 100\n"
                    "    else:\n"
                    "        print('3. Success! No exceptions were raised.')\n"
                    "    finally:\n"
                    "        print('4. Finally block executing cleanup.')\n"
                    "        if f:\n"
                    "            f.close()\n"
                    "    return val"
                ),
                "explanation": "Shows the exact order of execution across all 4 exception handling constructs."
            },
            {
                "title": "Catching Multiple Specific Exceptions",
                "language": "python",
                "code": (
                    "def parse_payload_data(data: dict, key: str) -> float:\n"
                    "    try:\n"
                    "        return float(data[key])\n"
                    "    except (KeyError, TypeError, ValueError) as err:\n"
                    "        # Logs the specific error and returns safe fallback\n"
                    "        print(f'Failed to parse key \"{key}\": {type(err).__name__} - {err}')\n"
                    "        return 0.0"
                ),
                "explanation": "Catches multiple related exceptions in a single tuple while maintaining specificity."
            },
            {
                "title": "Context Manager Equivalent (`with` statement)",
                "language": "python",
                "code": (
                    "# Python 'with' statement handles try/finally file closing under the hood\n"
                    "def safe_read(path):\n"
                    "    try:\n"
                    "        with open(path, 'r') as file:\n"
                    "            return file.read()\n"
                    "    except FileNotFoundError:\n"
                    "        return ''\n"
                    "# File descriptor is guaranteed to be closed upon exiting 'with'"
                ),
                "explanation": "Context managers eliminate manual finally cleanup boilerplate."
            },
            {
                "title": "JavaScript Equivalent (try / catch / finally)",
                "language": "javascript",
                "code": (
                    "function parseJsonConfig(rawJson) {\n"
                    "  try {\n"
                    "    const parsed = JSON.parse(rawJson);\n"
                    "    return parsed;\n"
                    "  } catch (err) {\n"
                    "    console.error('JSON parsing failed:', err.message);\n"
                    "    return {};\n"
                    "  } finally {\n"
                    "    console.log('JSON parse attempt complete');\n"
                    "  }\n"
                    "}"
                ),
                "explanation": "Demonstrates identical exception handling architecture in JavaScript."
            }
        ],
        coding_challenge={
            "title": "Build a Resilient Integer Divider",
            "instructions": "Write a function `safe_divide(a, b)` that attempts to return `float(a) / float(b)`. If `b == 0` (ZeroDivisionError), return `'DIV_BY_ZERO'`. If either cannot be converted to float (TypeError or ValueError), return `'INVALID_INPUT'`. Use structured try/except blocks.",
            "starter_code": (
                "def safe_divide(a, b):\n"
                "    # Return a / b with structured exception handling\n"
                "    pass\n"
            ),
            "solution_code": (
                "def safe_divide(a, b):\n"
                "    try:\n"
                "        num = float(a)\n"
                "        denom = float(b)\n"
                "        return num / denom\n"
                "    except ZeroDivisionError:\n"
                "        return 'DIV_BY_ZERO'\n"
                "    except (TypeError, ValueError):\n"
                "        return 'INVALID_INPUT'\n\n"
                "print(safe_divide(10, 2))\n"
                "print(safe_divide(10, 0))\n"
                "print(safe_divide('ten', 2))"
            ),
            "expected_output": "5.0\nDIV_BY_ZERO\nINVALID_INPUT"
        },
        quizzes=[
            {
                "question": "What is the primary role of the `finally` block in a try/except/finally structure?",
                "options": [
                    "To execute cleanup logic (closing files, releasing locks) unconditionally, regardless of whether exceptions were raised or caught",
                    "To catch only final exceptions",
                    "To restart the operating system",
                    "To run only when code has an error"
                ],
                "correct_answer": "To execute cleanup logic (closing files, releasing locks) unconditionally, regardless of whether exceptions were raised or caught",
                "explanation": "The `finally` block is guaranteed to execute before the block finishes, ensuring resource cleanup."
            },
            {
                "question": "Under what condition does the `else` block execute in Python's `try / except / else / finally`?",
                "options": [
                    "Only when the `try` block completes successfully with ZERO exceptions raised",
                    "Whenever an exception is caught",
                    "Whenever the computer has extra RAM",
                    "Only when an exception is thrown"
                ],
                "correct_answer": "Only when the `try` block completes successfully with ZERO exceptions raised",
                "explanation": "In Python, `else` runs exclusively when no exception was raised in `try`."
            },
            {
                "question": "Why is writing a bare `except:` block considered dangerous in Python?",
                "options": [
                    "It catches system-level signals like `KeyboardInterrupt` (Ctrl+C) and `SystemExit`, preventing programs from being terminated cleanly",
                    "It causes a syntax error",
                    "It deletes the code file",
                    "It slows down network Wi-Fi"
                ],
                "correct_answer": "It catches system-level signals like `KeyboardInterrupt` (Ctrl+C) and `SystemExit`, preventing programs from being terminated cleanly",
                "explanation": "A bare `except:` catches `BaseException`, preventing the user from interrupting frozen scripts."
            },
            {
                "question": "How do Python Context Managers (`with open(...) as f:`) guarantee safe file handling?",
                "options": [
                    "They automatically execute `f.close()` in an internal finally block upon exiting the scope",
                    "They encrypt the file on disk",
                    "They make the file read-only forever",
                    "They convert text files to binary databases"
                ],
                "correct_answer": "They automatically execute `f.close()` in an internal finally block upon exiting the scope",
                "explanation": "Context managers invoke `__enter__` on setup and `__exit__` on teardown, automating cleanup."
            },
            {
                "question": "What happens if an exception is raised in a `try` block and there is NO matching `except` clause for that exception type?",
                "options": [
                    "The `finally` block executes (if present), and the unhandled exception propagates up the call stack to crashing the process",
                    "The exception is converted to a string and printed silently",
                    "The program reboots",
                    "The computer enters sleep mode"
                ],
                "correct_answer": "The `finally` block executes (if present), and the unhandled exception propagates up the call stack to crashing the process",
                "explanation": "Unmatched exceptions execute `finally` blocks during stack unwinding before terminating the program."
            }
        ]
    )
]
