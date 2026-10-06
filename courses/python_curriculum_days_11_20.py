"""
Days 11 to 20 of Python Mastery (35 Days)
Includes:
- Day 12 Project: Terminal Guess-the-Number Game with State & Replay Mechanics
- Day 18 Project: Contact Book & Directory Manager CLI
"""

from seeder.course_blueprint import DayBlueprint, QuizQuestionBlueprint, CodingChallengeBlueprint

DAYS_11_TO_20 = [
    # -------------------------------------------------------------
    # DAY 11
    # -------------------------------------------------------------
    DayBlueprint(
        order=11,
        title="Day 11: Loop Control Statements: break, continue & pass",
        concept="Interrupting, skipping, and reserving loop cycles dynamically",
        analogy="Think of `break` like pulling the emergency brake on a subway train (the whole trip stops immediately). Think of `continue` like a VIP FastPass skipping a single roller coaster line (skip today's turn and jump to tomorrow's). And `pass` is just a yellow 'Under Construction' sticky note!",
        theory_sections=[
            {
                "heading": "The Three Loop Control Directives",
                "body": "Python provides three precise control keywords inside loops:\n- `break`: Terminate the loop immediately and transfer control to the statement after the loop.\n- `continue`: Skip the rest of the current iteration and jump straight to the next cycle.\n- `pass`: A null operation / no-op placeholder when syntax requires a statement but no action is needed."
            },
            {
                "heading": "The Loop else Clause with break",
                "body": "A unique Python feature is that loops can have an `else` block. The `else` block executes only if the loop completes all iterations **without** hitting a `break` statement. This is commonly used in searching algorithms to detect when an item was not found."
            }
        ],
        code_snippets=[
            {
                "title": "Using break to Exit Early",
                "code": "# Stop searching as soon as target is found\ntarget = 'Banana'\nfor fruit in ['Apple', 'Banana', 'Cherry', 'Date']:\n    print('Checking:', fruit)\n    if fruit == target:\n        print('Found', target, '! Breaking out.')\n        break"
            },
            {
                "title": "Using continue to Skip Odd Numbers",
                "code": "# Print only even numbers by skipping odds\nfor n in range(1, 10):\n    if n % 2 != 0:\n        continue\n    print('Even number:', n)"
            },
            {
                "title": "Search Pattern with for-else",
                "code": "users = ['alice', 'bob', 'charlie']\nsearch_for = 'david'\nfor u in users:\n    if u == search_for:\n        print('User located!')\n        break\nelse:\n    print(f'User {search_for} does not exist in records.')"
            },
            {
                "title": "Using pass for Future Stubs",
                "code": "def complex_future_algorithm():\n    pass # Will implement tomorrow\n\nfor i in range(3):\n    if i == 1:\n        pass # Placeholder for special handling\n    print('Processing step', i)"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Filter and Skip Negative Numbers",
            description="Given `nums = [10, -5, 20, -1, 30, 0]`. Use a `for` loop and `continue` to calculate the sum of strictly positive numbers (> 0). Print: 'Positive Sum: 60'.",
            starter_code="nums = [10, -5, 20, -1, 30, 0]\npos_sum = 0\n# TODO: Skip non-positive numbers and calculate sum\n",
            solution_code="nums = [10, -5, 20, -1, 30, 0]\npos_sum = 0\nfor n in nums:\n    if n <= 0:\n        continue\n    pos_sum += n\nprint('Positive Sum:', pos_sum)",
            expected_output="Positive Sum: 60"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What does the `continue` statement do inside a loop?",
                options=[
                    "Skips the rest of the current iteration and jumps to the next iteration.",
                    "Terminates the entire loop immediately.",
                    "Restarts the entire loop from iteration 0.",
                    "Pauses execution for 1 second."
                ],
                correct_answer="Skips the rest of the current iteration and jumps to the next iteration.",
                explanation="`continue` discards remaining statements in the active cycle and proceeds with the next cycle."
            ),
            QuizQuestionBlueprint(
                question="What is the purpose of the `pass` keyword in Python?",
                options=[
                    "It acts as a syntactic placeholder that does nothing.",
                    "It forces a function to return True.",
                    "It bypasses security permission checks.",
                    "It skips memory garbage collection."
                ],
                correct_answer="It acts as a syntactic placeholder that does nothing.",
                explanation="`pass` is a null statement used where syntax requires a body but no code is to be run."
            ),
            QuizQuestionBlueprint(
                question="Under what condition does the `else` block of a `for` loop execute?",
                options=[
                    "Only when the loop finishes all iterations without encountering a `break`.",
                    "Whenever the loop fails with an exception.",
                    "If the iterable passed to the loop was empty.",
                    "On every single iteration."
                ],
                correct_answer="Only when the loop finishes all iterations without encountering a `break`.",
                explanation="The `else` branch of a loop runs when the loop completes naturally without being broken."
            ),
            QuizQuestionBlueprint(
                question="What will this code print: for i in range(3): if i == 1: break; print(i)?",
                options=["0", "0 1", "1 2", "0 1 2"],
                correct_answer="0",
                explanation="When i is 0, it prints 0. When i becomes 1, the condition triggers `break`, terminating before printing."
            ),
            QuizQuestionBlueprint(
                question="Can `continue` and `break` be used inside a `while` loop?",
                options=[
                    "Yes, both statements work identically in both `for` and `while` loops.",
                    "No, only `break` works in `while` loops.",
                    "No, they are exclusive to `for` loops.",
                    "Only when the condition is `while True:`."
                ],
                correct_answer="Yes, both statements work identically in both `for` and `while` loops.",
                explanation="Both `break` and `continue` are valid loop control primitives for any Python loop."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 12 - PROJECT DAY 2
    # -------------------------------------------------------------
    DayBlueprint(
        order=12,
        title="Day 12: [PROJECT 2] Terminal Guess-the-Number Game with State & Replay Mechanics",
        concept="Combining random numbers, loops, state tracking, conditionals, and input validation into an engaging game",
        analogy="You are building an arcade machine game! The machine secretly rolls a 100-sided die behind a curtain. The player inserts coins, guesses, and the machine flashes 'Higher' or 'Lower' neon signs until victory!",
        is_project_day=True,
        project_name="Terminal Guess-the-Number Game",
        theory_sections=[
            {
                "heading": "Game Architecture & State Variables",
                "body": "A game loop relies on state management. In our game, we track:\n- `secret_number`: Generated pseudo-randomly using Python's `random.randint(1, 100)`.\n- `attempts_left`: Decremented after each guess to create suspense.\n- `has_won`: Boolean flag determining victory.\n- `score_history`: Storing how many tries previous rounds took."
            },
            {
                "heading": "Input Validation & Replay Loop",
                "body": "The game must never crash if a player types non-numeric text like 'banana'. We will use `.isdigit()` or exception handling to catch bad inputs, guide the player, and allow replaying new rounds seamlessly."
            }
        ],
        code_snippets=[
            {
                "title": "Random Secret Generation & Comparison Logic",
                "code": "import random\n\ndef evaluate_guess(guess: int, secret: int) -> str:\n    if guess < secret:\n        return '📈 Too low! Aim higher.'\n    elif guess > secret:\n        return '📉 Too high! Aim lower.'\n    else:\n        return '🎉 Bingo! Correct guess!'"
            },
            {
                "title": "Safe Number Parser",
                "code": "def parse_guess(raw_text: str):\n    raw_text = raw_text.strip()\n    if not raw_text.isdigit():\n        return None\n    return int(raw_text)\n\nprint('Parsed 42:', parse_guess(' 42 '))\nprint('Parsed abc:', parse_guess('abc'))"
            },
            {
                "title": "Complete Working Game Engine Simulation",
                "code": "def run_game_round(secret: int, simulated_guesses: list):\n    print(f'=== Starting Guess The Number (Range: 1-100) ===')\n    attempts = 0\n    max_attempts = 7\n    \n    for guess in simulated_guesses:\n        attempts += 1\n        print(f'Player guessed: {guess}')\n        if guess == secret:\n            print(f'🏆 Winner! Cracked the secret {secret} in {attempts} tries!')\n            return attempts\n        elif guess < secret:\n            print('  -> Higher!')\n        else:\n            print('  -> Lower!')\n        \n        if attempts >= max_attempts:\n            print(f'💀 Game Over! The number was {secret}.')\n            return None\n    return attempts\n\n# Run a test round\nrun_game_round(secret=48, simulated_guesses=[25, 75, 50, 40, 48])"
            },
            {
                "title": "Replay Session & Best Score Tracker",
                "code": "class ScoreTracker:\n    def __init__(self):\n        self.scores = []\n    def record(self, attempts):\n        if attempts:\n            self.scores.append(attempts)\n    def best_score(self):\n        return min(self.scores) if self.scores else None\n\ntracker = ScoreTracker()\ntracker.record(5)\ntracker.record(3)\nprint(f'Best round took {tracker.best_score()} attempts.')"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Implement Score Grading for the Game",
            description="Write a function `grade_performance(attempts)`: 1-3 attempts returns 'Diamond', 4-5 returns 'Gold', 6-7 returns 'Silver', and >7 returns 'Bronze'. Test with `attempts = 4` and print: 'Rank: Gold'.",
            starter_code="attempts = 4\n# TODO: Implement grading logic\n",
            solution_code="attempts = 4\nif 1 <= attempts <= 3:\n    rank = 'Diamond'\nelif 4 <= attempts <= 5:\n    rank = 'Gold'\nelif 6 <= attempts <= 7:\n    rank = 'Silver'\nelse:\n    rank = 'Bronze'\nprint(f'Rank: {rank}')",
            expected_output="Rank: Gold"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Which standard library module is used to generate pseudo-random numbers in Python?",
                options=["random", "math", "secrets_only", "sys"],
                correct_answer="random",
                explanation="The `random` module provides functions like `random.randint()` for number generation."
            ),
            QuizQuestionBlueprint(
                question="What range of integers can random.randint(1, 10) return?",
                options=[
                    "Any integer from 1 to 10, inclusive of both endpoints.",
                    "Integers from 1 to 9 (10 is excluded).",
                    "Floats between 1.0 and 10.0.",
                    "Only even numbers between 1 and 10."
                ],
                correct_answer="Any integer from 1 to 10, inclusive of both endpoints.",
                explanation="Unlike `range()`, `random.randint(a, b)` includes BOTH endpoints `a` and `b`."
            ),
            QuizQuestionBlueprint(
                question="What does the string method '42'.isdigit() return?",
                options=["True", "False", "42", "Raises ValueError"],
                correct_answer="True",
                explanation="`.isdigit()` checks if all characters in the string are digits."
            ),
            QuizQuestionBlueprint(
                question="In binary search strategy, what is the maximum guesses needed to find a number between 1 and 100?",
                options=["7 guesses (log2(100) ≈ 6.64)", "10 guesses", "50 guesses", "100 guesses"],
                correct_answer="7 guesses (log2(100) ≈ 6.64)",
                explanation="With binary search (halving each time), 2^7 = 128, which easily covers 100 possibilities."
            ),
            QuizQuestionBlueprint(
                question="Why is it helpful to wrap game rounds in a function like run_round()?",
                options=[
                    "It encapsulates state and allows clean replaying via a while loop.",
                    "Functions make Python code run in C speed.",
                    "Python requires all code to be inside functions.",
                    "To prevent memory garbage collection."
                ],
                correct_answer="It encapsulates state and allows clean replaying via a while loop.",
                explanation="Encapsulating the round logic in a function isolates variables and makes repeating rounds trivial."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 13
    # -------------------------------------------------------------
    DayBlueprint(
        order=13,
        title="Day 13: Python Lists & 0-Indexed Operations",
        concept="Ordered, mutable sequences, positive and negative indexing, and len()",
        analogy="Imagine a train with connected passenger wagons. The engine is at index 0, the first wagon is 1, and so on. If you walk to the very back of the train, the caboose is index -1, and the wagon right in front of the caboose is -2!",
        theory_sections=[
            {
                "heading": "What is a Python List?",
                "body": "A list is an ordered, mutable (changeable) collection of items enclosed in square brackets `[]`. Lists can hold any data types—even mixed types or other nested lists! Because lists are ordered, every element has a fixed position called an **index**."
            },
            {
                "heading": "0-Based Indexing & Negative Indexing",
                "body": "Python uses **0-based indexing**, meaning the first item is at index `0`, the second is at `1`, and the last is at `len(lst) - 1`. Python also supports **negative indexing**: index `-1` directly refers to the last element, `-2` to the second-to-last, etc."
            }
        ],
        code_snippets=[
            {
                "title": "Creating Lists and Index Access",
                "code": "fruits = ['Apple', 'Banana', 'Cherry', 'Dragonfruit']\nprint('First item (0):', fruits[0])\nprint('Second item (1):', fruits[1])\nprint('Last item (-1):', fruits[-1])\nprint('Second-to-last (-2):', fruits[-2])"
            },
            {
                "title": "Mutating Items In-Place",
                "code": "inventory = ['Torch', 'Shield', 'Dagger']\nprint('Before:', inventory)\ninventory[1] = 'Tower Shield'\nprint('After upgrade:', inventory)"
            },
            {
                "title": "List Length and Membership Testing",
                "code": "heroes = ['Batman', 'Superman', 'Wonder Woman']\nprint('Total heroes:', len(heroes))\n# Using 'in' and 'not in' operators\nprint('Is Flash in heroes?', 'Flash' in heroes)\nprint('Is Batman in heroes?', 'Batman' in heroes)"
            },
            {
                "title": "Nested Lists (Matrices)",
                "code": "matrix = [\n    [1, 2, 3],\n    [4, 5, 6],\n    [7, 8, 9]\n]\n# Row 1, Column 2 -> element 6\nprint('Matrix center:', matrix[1][1])\nprint('Matrix row 1 col 2:', matrix[1][2])"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Retrieve and Swap First and Last Elements",
            description="Given `queue = ['Guest1', 'Guest2', 'Guest3', 'VIP']`. Swap the first and last elements in-place and print: 'Updated Queue: ['VIP', 'Guest2', 'Guest3', 'Guest1']'.",
            starter_code="queue = ['Guest1', 'Guest2', 'Guest3', 'VIP']\n# TODO: Swap first and last elements\n",
            solution_code="queue = ['Guest1', 'Guest2', 'Guest3', 'VIP']\nqueue[0], queue[-1] = queue[-1], queue[0]\nprint('Updated Queue:', queue)",
            expected_output="Updated Queue: ['VIP', 'Guest2', 'Guest3', 'Guest1']"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the index of the first element in a Python list?",
                options=["0", "1", "-1", "None"],
                correct_answer="0",
                explanation="Python uses 0-based indexing for all ordered collections."
            ),
            QuizQuestionBlueprint(
                question="Given lst = [10, 20, 30, 40], what does lst[-1] evaluate to?",
                options=["40", "10", "30", "Raises IndexError"],
                correct_answer="40",
                explanation="Negative index `-1` always points to the last element of the sequence."
            ),
            QuizQuestionBlueprint(
                question="What exception is raised if you access an index that does not exist (e.g. lst[99] when len is 3)?",
                options=["IndexError", "KeyError", "ValueError", "OutOfBoundsException"],
                correct_answer="IndexError",
                explanation="Python raises `IndexError: list index out of range` when accessing invalid indices."
            ),
            QuizQuestionBlueprint(
                question="Are Python lists mutable?",
                options=[
                    "Yes, you can modify, add, or delete elements in-place.",
                    "No, lists are strictly immutable.",
                    "Only if they contain only integers.",
                    "Only before they are passed into functions."
                ],
                correct_answer="Yes, you can modify, add, or delete elements in-place.",
                explanation="Lists are mutable; you can change elements via index or methods like append."
            ),
            QuizQuestionBlueprint(
                question="How do you check if an element 'item' is present inside a list 'my_list'?",
                options=["'item' in my_list", "my_list.has('item')", "my_list.contains('item')", "my_list.exists('item')"],
                correct_answer="'item' in my_list",
                explanation="The `in` keyword checks membership in any iterable collection."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 14
    # -------------------------------------------------------------
    DayBlueprint(
        order=14,
        title="Day 14: List Slicing & Core Mutation Methods",
        concept="Extracting sublists using [start:stop:step] and built-in list methods",
        analogy="Think of slicing like using a bread slicer on a loaf of bread. You can cut slices from wedge 2 up to wedge 5, or you can cut every second slice throughout the entire loaf! Reversing is simply flipping the loaf from crust to crust with `[::-1]`.",
        theory_sections=[
            {
                "heading": "List Slicing Syntax [start:stop:step]",
                "body": "Slicing extracts a new sublist without modifying the original:\n- `lst[start:stop]`: from index `start` up to (excluding) `stop`.\n- `lst[:stop]`: from the beginning up to `stop`.\n- `lst[start:]`: from `start` to the very end.\n- `lst[::-1]`: step of -1 neatly reverses the entire list!"
            },
            {
                "heading": "Essential In-Place Mutation Methods",
                "body": "- `.append(item)`: Adds item to the very end.\n- `.insert(index, item)`: Inserts item at specified index.\n- `.pop([index])`: Removes and returns item at index (defaults to last).\n- `.remove(val)`: Searches for and removes first occurrence of `val`.\n- `.sort()`: Sorts list in-place (ascending by default)."
            }
        ],
        code_snippets=[
            {
                "title": "Slicing Operations",
                "code": "nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\nprint('Slice 2 to 6:', nums[2:6])\nprint('First 4 items:', nums[:4])\nprint('From index 6 to end:', nums[6:])\nprint('Every 2nd item:', nums[::2])\nprint('Reversed slice:', nums[::-1])"
            },
            {
                "title": "Adding and Inserting Elements",
                "code": "cart = ['Milk', 'Eggs']\ncart.append('Bread')        # Adds to end\ncart.insert(0, 'Coffee')     # Inserts at front\nprint('Cart after additions:', cart)"
            },
            {
                "title": "Removing and Popping Elements",
                "code": "stack = ['Page 1', 'Page 2', 'Page 3']\nlast_page = stack.pop()      # Removes 'Page 3'\nprint('Popped:', last_page)\nstack.remove('Page 1')       # Removes by value\nprint('Stack left:', stack)"
            },
            {
                "title": "Sorting and Reversing",
                "code": "scores = [88, 42, 95, 73, 61]\nscores.sort()               # Sorts ascending in-place\nprint('Ascending:', scores)\nscores.sort(reverse=True)   # Sorts descending\nprint('Descending:', scores)"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Clean and Sort High Scores",
            description="Given `raw_scores = [45, 99, 12, 88, 34, 100, 77]`. Remove the lowest score, sort the remaining scores in descending order, and extract the top 3 scores using slicing. Print: 'Top 3: [100, 99, 88]'.",
            starter_code="raw_scores = [45, 99, 12, 88, 34, 100, 77]\n# TODO: Clean, sort descending, slice top 3\n",
            solution_code="raw_scores = [45, 99, 12, 88, 34, 100, 77]\nraw_scores.remove(min(raw_scores))\nraw_scores.sort(reverse=True)\ntop_3 = raw_scores[:3]\nprint('Top 3:', top_3)",
            expected_output="Top 3: [100, 99, 88]"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What does list slicing lst[1:4] return?",
                options=[
                    "Elements at index 1, 2, and 3 (excluding index 4)",
                    "Elements at index 1, 2, 3, and 4",
                    "Elements at index 0, 1, 2, and 3",
                    "The first 4 elements"
                ],
                correct_answer="Elements at index 1, 2, and 3 (excluding index 4)",
                explanation="The `stop` index in Python slices is always exclusive."
            ),
            QuizQuestionBlueprint(
                question="How do you reverse a list using slice notation without modifying the original?",
                options=["lst[::-1]", "lst[reverse]", "lst[-1:0]", "lst[-1:]"],
                correct_answer="lst[::-1]",
                explanation="`[::-1]` steps backward through the sequence from end to beginning."
            ),
            QuizQuestionBlueprint(
                question="What is the difference between lst.pop() and lst.remove('x')?",
                options=[
                    "pop() removes and returns an item by index; remove() deletes the first matching value.",
                    "pop() deletes values; remove() deletes indices.",
                    "pop() works on strings; remove() works on lists.",
                    "There is no difference."
                ],
                correct_answer="pop() removes and returns an item by index; remove() deletes the first matching value.",
                explanation="`pop(i)` targets index position, whereas `remove(v)` searches for and removes by value."
            ),
            QuizQuestionBlueprint(
                question="What does lst.append([1, 2]) do to an existing list lst = ['a']?",
                options=[
                    "Appends the entire list as a single nested element: ['a', [1, 2]]",
                    "Flattens and extends: ['a', 1, 2]",
                    "Raises a TypeError",
                    "Replaces the contents with [1, 2]"
                ],
                correct_answer="Appends the entire list as a single nested element: ['a', [1, 2]]",
                explanation="`append` adds its single argument as-is; to flatten multiple elements, use `extend()`."
            ),
            QuizQuestionBlueprint(
                question="What is the return value of the lst.sort() method?",
                options=["None (it sorts in-place)", "The sorted list", "A boolean True", "An iterator"],
                correct_answer="None (it sorts in-place)",
                explanation="`list.sort()` mutates the list in place and returns `None` to prevent confusion with `sorted()`."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 15
    # -------------------------------------------------------------
    DayBlueprint(
        order=15,
        title="Day 15: Tuples, Immutability & Sequence Unpacking",
        concept="Immutable sequences, memory efficiency, and multiple variable assignment",
        analogy="Think of a list like a dry-erase whiteboard (you can write, erase, and change elements anytime). Think of a tuple like a carved stone monument (once etched, its inscriptions can never be altered). That guarantees safety and integrity!",
        theory_sections=[
            {
                "heading": "What is a Tuple and Why Immutability?",
                "body": "A tuple is an ordered sequence enclosed in parentheses `()`. Unlike lists, tuples are **immutable**—once defined, elements cannot be added, removed, or changed. This makes tuples safer for constants, faster in memory, and usable as dictionary keys."
            },
            {
                "heading": "Tuple Unpacking & Starred Expressions",
                "body": "Tuple unpacking allows extracting elements into individual variables in a single clean line. With the starred expression `*rest`, you can even capture variable-length sequences cleanly."
            }
        ],
        code_snippets=[
            {
                "title": "Defining Tuples and Immutability Guard",
                "code": "point = (10, 20)\nrgb_color = (255, 128, 0)\nprint('Point coordinates:', point)\nprint('X:', point[0], 'Y:', point[1])\n# point[0] = 5  # Uncommenting this raises TypeError: 'tuple' object does not support item assignment"
            },
            {
                "title": "Single Element Tuple Trap",
                "code": "# A single element in parentheses is NOT a tuple without a trailing comma!\nnot_a_tuple = (42)\nreal_tuple = (42,)\nprint('Type 1:', type(not_a_tuple)) # <class 'int'>\nprint('Type 2:', type(real_tuple))   # <class 'tuple'>"
            },
            {
                "title": "Tuple Unpacking in Action",
                "code": "user_record = ('Alice', 28, 'Software Engineer')\nname, age, profession = user_record\nprint(f'{name} is {age} years old and works as a {profession}.')"
            },
            {
                "title": "Starred Unpacking (*rest)",
                "code": "grades = [95, 88, 72, 85, 90]\n# First score, last score, and all middle scores\nfirst, *middle, last = grades\nprint('First:', first)\nprint('Middle scores:', middle)\nprint('Last:', last)"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Unpack Server Config Tuple",
            description="Given `server_info = ('api.hunar.com', 8080, 'active', 'TLS_1_3')`. Unpack the host, port, and collect remaining settings in `*meta`. Print: 'Host: api.hunar.com:8080 | Meta: ['active', 'TLS_1_3']'.",
            starter_code="server_info = ('api.hunar.com', 8080, 'active', 'TLS_1_3')\n# TODO: Unpack using host, port, and *meta\n",
            solution_code="server_info = ('api.hunar.com', 8080, 'active', 'TLS_1_3')\nhost, port, *meta = server_info\nprint(f'Host: {host}:{port} | Meta: {meta}')",
            expected_output="Host: api.hunar.com:8080 | Meta: ['active', 'TLS_1_3']"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the primary difference between a list and a tuple?",
                options=[
                    "Lists are mutable; tuples are immutable.",
                    "Lists can hold numbers; tuples can only hold strings.",
                    "Tuples cannot be indexed.",
                    "Lists use parentheses (); tuples use square brackets []."
                ],
                correct_answer="Lists are mutable; tuples are immutable.",
                explanation="Tuples cannot be altered after creation (immutable), while lists can be mutated in-place."
            ),
            QuizQuestionBlueprint(
                question="How do you create a tuple with exactly one element 5?",
                options=["(5,)", "(5)", "tuple(5)", "[5]"],
                correct_answer="(5,)",
                explanation="The trailing comma `(5,)` is required for Python to distinguish a single-element tuple from parenthesized math."
            ),
            QuizQuestionBlueprint(
                question="What happens if you attempt to execute t = (1, 2); t[0] = 99?",
                options=[
                    "Raises a TypeError ('tuple' object does not support item assignment)",
                    "Changes the element to 99",
                    "Appends 99 to the tuple",
                    "Silently ignores the assignment"
                ],
                correct_answer="Raises a TypeError ('tuple' object does not support item assignment)",
                explanation="Immutability prevents changing or assigning to tuple elements."
            ),
            QuizQuestionBlueprint(
                question="Can a tuple contain a mutable list inside it (e.g. t = (1, [2, 3]))?",
                options=[
                    "Yes, and the list inside CAN be mutated, though the tuple's reference cannot.",
                    "No, tuples can never contain lists.",
                    "Yes, but the list becomes automatically frozen.",
                    "Only in Python 2."
                ],
                correct_answer="Yes, and the list inside CAN be mutated, though the tuple's reference cannot.",
                explanation="Tuples hold references. The references cannot change, but mutable objects inside can still be altered."
            ),
            QuizQuestionBlueprint(
                question="What will a, *b, c = [1, 2, 3, 4, 5] assign to b?",
                options=["[2, 3, 4]", "[1, 2, 3]", "[3, 4, 5]", "3"],
                correct_answer="[2, 3, 4]",
                explanation="The starred variable `*b` collects all intermediate elements into a list."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 16
    # -------------------------------------------------------------
    DayBlueprint(
        order=16,
        title="Day 16: Dictionaries: Keys, Values & O(1) Lookups",
        concept="Hash maps, key-value associations, .get() safe access, and dictionary methods",
        analogy="Think of a dictionary like the real Oxford English Dictionary. Instead of flipping through page 1 to 500 one by one to find 'Elephant' (like searching an unsorted list), you look up the word directly under 'E' and instantly read its definition! That instant lookup is called O(1) time complexity.",
        theory_sections=[
            {
                "heading": "The Power of Dictionaries",
                "body": "A dictionary (`dict`) is an unordered (insertion-ordered since Python 3.7) collection of key-value pairs written as `{key: value}`. Keys must be unique and immutable (strings, integers, tuples). Dictionaries use hash tables under the hood, making looking up a key nearly instantaneous regardless of how many million items are stored!"
            },
            {
                "heading": "Safe Access with .get()",
                "body": "Accessing a missing key using bracket notation `d['missing']` raises a fatal `KeyError`. The method `d.get('missing', default)` safely returns `None` or your fallback default value without crashing."
            }
        ],
        code_snippets=[
            {
                "title": "Creating and Accessing Dictionaries",
                "code": "student = {\n    'name': 'Kael',\n    'course': 'Python Mastery',\n    'level': 5,\n    'is_active': True\n}\nprint('Student Name:', student['name'])\nprint('Current Level:', student['level'])"
            },
            {
                "title": "Safe Key Access with .get()",
                "code": "profile = {'username': 'coder99', 'role': 'admin'}\n# Safe lookup with default fallback\nemail = profile.get('email', 'No email registered')\nrole = profile.get('role', 'user')\nprint(f'Role: {role} | Email: {email}')"
            },
            {
                "title": "Adding, Updating & Deleting Keys",
                "code": "config = {'theme': 'light', 'volume': 80}\nconfig['theme'] = 'dark'        # Update\nconfig['language'] = 'English'  # Insert\ndel config['volume']            # Delete\nprint('Updated config:', config)"
            },
            {
                "title": "Iterating Over keys(), values(), and items()",
                "code": "prices = {'Apple': 1.20, 'Banana': 0.50, 'Mango': 2.50}\nfor fruit, price in prices.items():\n    print(f'Fruit: {fruit:<7} -> ${price:.2f}')"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Word Frequency Counter",
            description="Given `words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']`. Use a dictionary to count occurrences of each word. Print the count for 'apple': 'Apple count: 3'.",
            starter_code="words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']\ncounts = {}\n# TODO: Count frequencies\n",
            solution_code="words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']\ncounts = {}\nfor w in words:\n    counts[w] = counts.get(w, 0) + 1\nprint('Apple count:', counts['apple'])",
            expected_output="Apple count: 3"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What data structure does Python use behind dictionaries to achieve fast lookups?",
                options=["Hash Table", "Binary Search Tree", "Linked List", "Stack"],
                correct_answer="Hash Table",
                explanation="Python dictionaries are built using hash tables, allowing average O(1) time complexity."
            ),
            QuizQuestionBlueprint(
                question="What happens if you look up a non-existent key using square bracket notation dict['missing']?",
                options=["Raises a KeyError", "Returns None", "Returns False", "Creates the key with value None"],
                correct_answer="Raises a KeyError",
                explanation="Bracket notation raises `KeyError` if the specified key is absent."
            ),
            QuizQuestionBlueprint(
                question="What is the advantage of using dict.get('key', 'default')?",
                options=[
                    "It returns the default value instead of raising a KeyError if the key is missing.",
                    "It permanently inserts the default into the dictionary.",
                    "It encrypts the key for safety.",
                    "It sorts the dictionary keys."
                ],
                correct_answer="It returns the default value instead of raising a KeyError if the key is missing.",
                explanation="`.get()` prevents crashes by providing a fallback when keys are absent."
            ),
            QuizQuestionBlueprint(
                question="Which of the following CANNOT be used as a dictionary key?",
                options=["A mutable list [1, 2]", "A string 'id'", "An integer 100", "An immutable tuple (1, 2)"],
                correct_answer="A mutable list [1, 2]",
                explanation="Dictionary keys must be hashable and immutable; lists are unhashable."
            ),
            QuizQuestionBlueprint(
                question="Which method returns an iterable view of (key, value) pairs from a dictionary?",
                options=[".items()", ".pairs()", ".entries()", ".all()"],
                correct_answer=".items()",
                explanation="`dict.items()` yields `(key, value)` tuples suitable for unpacking in loops."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 17
    # -------------------------------------------------------------
    DayBlueprint(
        order=17,
        title="Day 17: Sets & Mathematical Set Operations",
        concept="Unordered unique collections, deduplication, union, intersection, and difference",
        analogy="Think of a set like a ring of unique scout merit badges. You cannot have two identical 'Archery' badges on the same ring—if you try to clip a duplicate badge on, it just merges! And comparing two scouts' rings shows which badges they both share (intersection).",
        theory_sections=[
            {
                "heading": "Sets and Unique Membership",
                "body": "A `set` is an unordered collection of unique, immutable elements enclosed in curly braces `{}`. Duplicate elements are automatically and silently removed. Sets are fantastic for fast membership testing (`O(1)`), deduplicating lists, and mathematical set logic."
            },
            {
                "heading": "Mathematical Operations",
                "body": "- **Union (`|` or `.union()`)**: All elements from both sets.\n- **Intersection (`&` or `.intersection()`)**: Only elements present in both sets.\n- **Difference (`-` or `.difference()`)**: Elements in set A that are not in set B.\n- **Symmetric Difference (`^`)**: Elements in either set, but not in both."
            }
        ],
        code_snippets=[
            {
                "title": "Creating Sets and Deduplication",
                "code": "raw_tags = ['python', 'backend', 'python', 'ai', 'backend', 'django']\nunique_tags = set(raw_tags)\nprint('Original length:', len(raw_tags))\nprint('Deduplicated set:', unique_tags)"
            },
            {
                "title": "Union and Intersection",
                "code": "devs_team_a = {'Alice', 'Bob', 'Charlie'}\ndevs_team_b = {'Charlie', 'David', 'Eve'}\n\n# Union: All engineers\nall_devs = devs_team_a | devs_team_b\nprint('All devs (Union):', all_devs)\n\n# Intersection: Shared engineers on both teams\nshared_devs = devs_team_a & devs_team_b\nprint('Shared devs (Intersection):', shared_devs)"
            },
            {
                "title": "Difference and Symmetric Difference",
                "code": "set_x = {1, 2, 3, 4}\nset_y = {3, 4, 5, 6}\nprint('In X but not in Y (Difference):', set_x - set_y)\nprint('In either, but not both (Symmetric):', set_x ^ set_y)"
            },
            {
                "title": "Adding and Modifying Sets",
                "code": "active_users = {'user1', 'user2'}\nactive_users.add('user3')\nactive_users.discard('user1') # Safe discard without KeyError\nprint('Active set:', active_users)"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Find Common Friends Between Two Profiles",
            description="Given `user_a_friends = {'Zaid', 'Sara', 'Hamza', 'Dua'}` and `user_b_friends = {'Ali', 'Sara', 'Bilal', 'Hamza'}`. Find their mutual friends using set intersection and print: 'Mutual Friends: 2'.",
            starter_code="user_a_friends = {'Zaid', 'Sara', 'Hamza', 'Dua'}\nuser_b_friends = {'Ali', 'Sara', 'Bilal', 'Hamza'}\n# TODO: Calculate mutual friends\n",
            solution_code="user_a_friends = {'Zaid', 'Sara', 'Hamza', 'Dua'}\nuser_b_friends = {'Ali', 'Sara', 'Bilal', 'Hamza'}\nmutual = user_a_friends & user_b_friends\nprint('Mutual Friends:', len(mutual))",
            expected_output="Mutual Friends: 2"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="How do you declare an empty set in Python?",
                options=["set()", "{}", "[]", "set([])"],
                correct_answer="set()",
                explanation="`{}` creates an empty dictionary by default; to create an empty set, use `set()`."
            ),
            QuizQuestionBlueprint(
                question="What happens when you add an existing element to a set using set.add(item)?",
                options=[
                    "Nothing, sets enforce unique elements and ignore duplicates.",
                    "Raises a DuplicateValueError.",
                    "Replaces the entire set.",
                    "Increments an internal frequency count."
                ],
                correct_answer="Nothing, sets enforce unique elements and ignore duplicates.",
                explanation="Sets enforce strict uniqueness, so adding an existing item is a no-op."
            ),
            QuizQuestionBlueprint(
                question="Which operator performs mathematical intersection between two sets?",
                options=["&", "|", "-", "^"],
                correct_answer="&",
                explanation="`&` computes the intersection (elements present in both sets)."
            ),
            QuizQuestionBlueprint(
                question="What is the result of set([1, 2, 2, 3, 3, 3])?",
                options=["{1, 2, 3}", "[1, 2, 3]", "{1: 1, 2: 2, 3: 3}", "(1, 2, 3)"],
                correct_answer="{1, 2, 3}",
                explanation="Passing an iterable to `set()` removes all redundant duplicate values."
            ),
            QuizQuestionBlueprint(
                question="What is the time complexity of checking membership (item in my_set) in a Python set?",
                options=["O(1) average time", "O(N) linear time", "O(N^2)", "O(log N)"],
                correct_answer="O(1) average time",
                explanation="Like dictionaries, sets use hash lookup providing O(1) average time complexity."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 18 - PROJECT DAY 3
    # -------------------------------------------------------------
    DayBlueprint(
        order=18,
        title="Day 18: [PROJECT 3] Contact Book & Directory Manager",
        concept="Building a complete CRUD (Create, Read, Update, Delete) directory tool with Dictionaries and Lists",
        analogy="You are constructing a modern digital smartphone address book! Every person has a profile card (dictionary) with their phone, email, and tags, all neatly filed in your contacts database.",
        is_project_day=True,
        project_name="Contact Book & Directory Manager",
        theory_sections=[
            {
                "heading": "Project Overview & CRUD Philosophy",
                "body": "Almost all software engineering revolves around CRUD:\n1. **C**reate: Add new contact entries.\n2. **R**ead: Search contacts by name or list all entries.\n3. **U**pdate: Modify existing phone numbers or emails.\n4. **D**elete: Remove obsolete entries.\nWe will build a modular in-memory Contact Directory supporting all 4 operations with input validation."
            },
            {
                "heading": "Data Model Structure",
                "body": "We store contacts in a top-level dictionary where keys are unique normalized names (e.g. `'bilal khan'`) and values are contact metadata dictionaries containing `'phone'`, `'email'`, and `'category'`."
            }
        ],
        code_snippets=[
            {
                "title": "Directory State & Add Contact (Create)",
                "code": "contacts_db = {}\n\ndef add_contact(name: str, phone: str, email: str, category: str = 'General') -> str:\n    key = name.strip().lower()\n    if key in contacts_db:\n        return f'⚠️ Contact \"{name}\" already exists!'\n    contacts_db[key] = {\n        'display_name': name.strip(),\n        'phone': phone.strip(),\n        'email': email.strip(),\n        'category': category\n    }\n    return f'✅ Contact \"{name}\" successfully added!'"
            },
            {
                "title": "Search Contact (Read)",
                "code": "def get_contact(name: str):\n    key = name.strip().lower()\n    contact = contacts_db.get(key)\n    if not contact:\n        return f'❌ Contact \"{name}\" not found.'\n    return f\"👤 {contact['display_name']} | 📞 {contact['phone']} | ✉️ {contact['email']} [{contact['category']}]\""
            },
            {
                "title": "Update & Delete (Update & Delete)",
                "code": "def update_phone(name: str, new_phone: str) -> str:\n    key = name.strip().lower()\n    if key not in contacts_db:\n        return 'Contact not found.'\n    contacts_db[key]['phone'] = new_phone\n    return f'Phone updated for {contacts_db[key][\"display_name\"]}.'\n\ndef delete_contact(name: str) -> str:\n    key = name.strip().lower()\n    if key in contacts_db:\n        del contacts_db[key]\n        return f'Deleted {name}.'\n    return 'Contact not found.'"
            },
            {
                "title": "Full CRUD Workflow Demonstration",
                "code": "# Populate initial contacts\nadd_contact('Sara Ahmed', '+923001234567', 'sara@hunar.com', 'Colleague')\nadd_contact('Hamza Tariq', '+923219876543', 'hamza@hunar.com', 'Friend')\n\nprint(get_contact('Sara Ahmed'))\nupdate_phone('Sara Ahmed', '+923009999999')\nprint(get_contact('Sara Ahmed'))\ndelete_contact('Hamza Tariq')\nprint('Total contacts remaining:', len(contacts_db))"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Filter Contacts by Category",
            description="Given `directory = {'alice': {'cat': 'Work'}, 'bob': {'cat': 'Friends'}, 'clara': {'cat': 'Work'}}`. Write a loop that counts how many contacts belong to 'Work'. Print: 'Work contacts: 2'.",
            starter_code="directory = {'alice': {'cat': 'Work'}, 'bob': {'cat': 'Friends'}, 'clara': {'cat': 'Work'}}\n# TODO: Count Work contacts\n",
            solution_code="directory = {'alice': {'cat': 'Work'}, 'bob': {'cat': 'Friends'}, 'clara': {'cat': 'Work'}}\nwork_count = sum(1 for c in directory.values() if c['cat'] == 'Work')\nprint('Work contacts:', work_count)",
            expected_output="Work contacts: 2"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What does the acronym CRUD represent in software development?",
                options=[
                    "Create, Read, Update, Delete",
                    "Compile, Run, Undo, Debug",
                    "Control, Route, Unload, Deliver",
                    "Class, Record, Union, Data"
                ],
                correct_answer="Create, Read, Update, Delete",
                explanation="CRUD encompasses the four fundamental persistent data manipulation operations."
            ),
            QuizQuestionBlueprint(
                question="Why is normalizing keys (e.g. using .strip().lower()) a best practice for search directories?",
                options=[
                    "It ensures case-insensitive and whitespace-resilient lookups.",
                    "It automatically encrypts the contact data.",
                    "It converts strings into integers for faster CPU execution.",
                    "It is mandated by PEP 8."
                ],
                correct_answer="It ensures case-insensitive and whitespace-resilient lookups.",
                explanation="Lowercasing and stripping whitespace prevents 'Sara' and '  sara ' from acting as duplicate distinct keys."
            ),
            QuizQuestionBlueprint(
                question="Which Python statement permanently removes a key from a dictionary?",
                options=["del my_dict[key]", "my_dict.erase(key)", "my_dict.drop(key)", "remove key from my_dict"],
                correct_answer="del my_dict[key]",
                explanation="The `del` keyword deletes the target key-value pair from the dictionary."
            ),
            QuizQuestionBlueprint(
                question="What does contacts_db.values() return?",
                options=[
                    "A view object containing all the values stored in the dictionary.",
                    "A list of dictionary keys.",
                    "A single string of merged text.",
                    "A boolean indicating if the dictionary is non-empty."
                ],
                correct_answer="A view object containing all the values stored in the dictionary.",
                explanation="`.values()` provides an iterable view of all values in the dictionary."
            ),
            QuizQuestionBlueprint(
                question="How can you count items meeting a condition across dictionary values?",
                options=[
                    "Using a generator expression with sum() or a simple for-loop accumulator.",
                    "By calling dict.count_if()",
                    "Using binary search.",
                    "Dictionaries do not support iteration."
                ],
                correct_answer="Using a generator expression with sum() or a simple for-loop accumulator.",
                explanation="Iterating over `.values()` with an `if` filter is the idiomatic Python approach."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 19
    # -------------------------------------------------------------
    DayBlueprint(
        order=19,
        title="Day 19: Functions: Definition, Parameters & Return Values",
        concept="Modular reusable code blocks, input parameters, and output return values",
        analogy="Think of a function like a bread toaster! You put raw bread slices into the slot (input parameters), the toaster does its internal heating work, and out pops crispy golden toast (the return value). You can toast 100 slices without rebuilding the toaster every morning!",
        theory_sections=[
            {
                "heading": "Why Functions?",
                "body": "Functions embody the DRY principle (**Don't Repeat Yourself**). Instead of copying and pasting the same 10 lines of code across your project, you encapsulate the logic inside a named function using the `def` keyword, and call it whenever needed."
            },
            {
                "heading": "Parameters vs Arguments & return vs print",
                "body": "- **Parameters**: The variable placeholders declared in the function definition (e.g. `def add(a, b)`).\n- **Arguments**: The actual concrete values passed when calling the function (e.g. `add(5, 10)`).\n- **The return keyword**: Hands a calculated result back to the caller so it can be stored in a variable. If a function reaches its end without a `return`, it implicitly returns `None`."
            }
        ],
        code_snippets=[
            {
                "title": "Defining and Calling a Basic Function",
                "code": "def greet_user(username: str) -> str:\n    \"\"\"Generates a personalized greeting banner.\"\"\"\n    return f'Welcome back to Hunar Cycle, {username}!'\n\nmessage = greet_user('Fatima')\nprint(message)"
            },
            {
                "title": "Function with Multiple Parameters and Math",
                "code": "def calculate_cylinder_volume(radius: float, height: float) -> float:\n    pi = 3.14159\n    return pi * (radius ** 2) * height\n\nvol = calculate_cylinder_volume(3.0, 5.0)\nprint(f'Cylinder Volume: {vol:.2f} cubic units')"
            },
            {
                "title": "Returning Multiple Values (Implicit Tuple Packing)",
                "code": "def get_min_and_max(numbers: list):\n    # Python bundles multiple returned values into a tuple!\n    return min(numbers), max(numbers)\n\nlowest, highest = get_min_and_max([45, 12, 89, 3, 99, 23])\nprint(f'Lowest: {lowest} | Highest: {highest}')"
            },
            {
                "title": "The Pitfall of Missing return (Implicit None)",
                "code": "def silent_calculator(x, y):\n    total = x + y\n    # Notice: No return statement!\n\nresult = silent_calculator(10, 20)\nprint('Function result is:', result) # Prints None"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Create a Celsius to Fahrenheit Converter Function",
            description="Write a function `celsius_to_fahrenheit(c)` that uses the formula `(c * 9/5) + 32` and returns the temperature. Test with `c = 25` and print: '25°C = 77.0°F'.",
            starter_code="# TODO: Define celsius_to_fahrenheit function\n",
            solution_code="def celsius_to_fahrenheit(c: float) -> float:\n    return (c * 9 / 5) + 32\n\nres = celsius_to_fahrenheit(25)\nprint(f'25°C = {res:.1f}°F')",
            expected_output="25°C = 77.0°F"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Which keyword is used to declare a function in Python?",
                options=["def", "function", "fn", "fun"],
                correct_answer="def",
                explanation="The `def` keyword (short for define) is used to declare functions in Python."
            ),
            QuizQuestionBlueprint(
                question="What does a Python function return if it executes to completion without a return statement?",
                options=["None", "0", "False", "Empty string ''"],
                correct_answer="None",
                explanation="Functions without an explicit return statement return the singleton object `None`."
            ),
            QuizQuestionBlueprint(
                question="What is the difference between a parameter and an argument?",
                options=[
                    "Parameters are variable names in the function definition; arguments are the actual values passed in calls.",
                    "Arguments are defined with def; parameters are passed to print.",
                    "Parameters are numbers; arguments are strings.",
                    "They are identical synonyms with no distinction."
                ],
                correct_answer="Parameters are variable names in the function definition; arguments are the actual values passed in calls.",
                explanation="Parameters are the signature variables; arguments are the runtime values supplied by the caller."
            ),
            QuizQuestionBlueprint(
                question="How does Python handle returning multiple values like: return a, b?",
                options=[
                    "It packs the values into a single tuple and returns it.",
                    "It returns only the first value and ignores the rest.",
                    "It raises a CompilationError.",
                    "It converts both values into strings."
                ],
                correct_answer="It packs the values into a single tuple and returns it.",
                explanation="Returning comma-separated values implicitly packs them into a tuple."
            ),
            QuizQuestionBlueprint(
                question="What is a docstring in a Python function?",
                options=[
                    "A string literal placed as the first statement in a function body to document its behavior.",
                    "A comment starting with #doc",
                    "A string used exclusively to print errors.",
                    "A type hint declaration."
                ],
                correct_answer="A string literal placed as the first statement in a function body to document its behavior.",
                explanation="Docstrings (triple-quoted strings) document modules, classes, and functions."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 20
    # -------------------------------------------------------------
    DayBlueprint(
        order=20,
        title="Day 20: Function Arguments: Default, *args & **kwargs",
        concept="Flexible function signatures, optional parameters, and variable-length arguments",
        analogy="Think of ordering a custom burger at a restaurant! The base burger has default ingredients (beef patty, lettuce). You can say 'add 3 extra toppings' (*args: bacon, cheese, pickles) and specify special instructions (**kwargs: sauce='extra spicy', toasted=True)!",
        theory_sections=[
            {
                "heading": "Default Arguments",
                "body": "You can assign default values to parameters (e.g. `def connect(port=8080)`). If the caller does not supply that argument, Python falls back to the default automatically. **Crucial Rule**: Parameters with default values must always follow parameters without defaults."
            },
            {
                "heading": "Variable Positional (*args) & Keyword (**kwargs) Arguments",
                "body": "- `*args`: Collects an arbitrary number of positional arguments into a **tuple**.\n- `**kwargs`: Collects an arbitrary number of keyword/named arguments into a **dictionary**.\nThis pattern makes functions infinitely extensible (widely used in decorators, APIs, and frameworks like Django and Flask)."
            }
        ],
        code_snippets=[
            {
                "title": "Default Parameter Values",
                "code": "def make_coffee(size='Medium', milk=True, syrup=None):\n    milk_desc = 'with milk' if milk else 'black'\n    syrup_desc = f' + {syrup} syrup' if syrup else ''\n    return f'{size} coffee {milk_desc}{syrup_desc}'\n\nprint(make_coffee())\nprint(make_coffee('Large', milk=False))\nprint(make_coffee('Small', syrup='Vanilla'))"
            },
            {
                "title": "Variable Positional Arguments (*args)",
                "code": "def sum_all(*numbers):\n    # 'numbers' is received as a tuple of all passed arguments\n    print('Received arguments tuple:', numbers)\n    return sum(numbers)\n\nprint('Total:', sum_all(10, 20, 30, 40))\nprint('Empty call total:', sum_all())"
            },
            {
                "title": "Variable Keyword Arguments (**kwargs)",
                "code": "def build_user_profile(user_id, **attributes):\n    print(f'User ID: {user_id}')\n    for key, value in attributes.items():\n        print(f'  • {key}: {value}')\n\nbuild_user_profile(101, username='zainab', country='Pakistan', role='Engineer')"
            },
            {
                "title": "Unpacking with * and ** in Function Calls",
                "code": "def send_email(to, subject, urgent=False):\n    return f'Sending email to {to} | Subject: {subject} | Urgent: {urgent}'\n\nemail_params = {'to': 'boss@company.com', 'subject': 'Q3 Reports', 'urgent': True}\n# Unpack dictionary keys into keyword arguments with **\nprint(send_email(**email_params))"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Universal Multiplier with *args",
            description="Write a function `multiply_all(*factors)` that multiplies all provided numbers together. If no arguments are passed, return 1. Test with `multiply_all(2, 3, 4, 5)` and print: 'Product: 120'.",
            starter_code="# TODO: Define multiply_all(*factors)\n",
            solution_code="def multiply_all(*factors):\n    res = 1\n    for f in factors:\n        res *= f\n    return res\n\nprint('Product:', multiply_all(2, 3, 4, 5))",
            expected_output="Product: 120"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What data structure is used inside a function to hold *args?",
                options=["A tuple", "A list", "A dictionary", "A set"],
                correct_answer="A tuple",
                explanation="`*args` bundles variable positional arguments into an immutable tuple."
            ),
            QuizQuestionBlueprint(
                question="What data structure is used inside a function to hold **kwargs?",
                options=["A dictionary", "A tuple", "A list", "A named tuple"],
                correct_answer="A dictionary",
                explanation="`**kwargs` bundles variable keyword arguments into a standard dictionary."
            ),
            QuizQuestionBlueprint(
                question="Why is def bad_func(lst=[]) considered a dangerous anti-pattern in Python?",
                options=[
                    "Because default mutable arguments are evaluated once at definition time and shared across calls.",
                    "Because Python forbids lists as default arguments.",
                    "Because it raises a SyntaxError.",
                    "Because lists cannot be passed to functions."
                ],
                correct_answer="Because default mutable arguments are evaluated once at definition time and shared across calls.",
                explanation="Default argument expressions are evaluated once when the function is defined, causing mutable defaults to persist state across calls."
            ),
            QuizQuestionBlueprint(
                question="What is the correct parameter ordering in a Python function definition?",
                options=[
                    "Standard positional, default parameters, *args, **kwargs",
                    "**kwargs, *args, default parameters, standard positional",
                    "*args, default parameters, standard positional, **kwargs",
                    "Any order is valid"
                ],
                correct_answer="Standard positional, default parameters, *args, **kwargs",
                explanation="Python requires positional arguments first, then defaults, then *args, then **kwargs."
            ),
            QuizQuestionBlueprint(
                question="What does func(**my_dict) do when calling a function?",
                options=[
                    "Unpacks the key-value pairs of the dictionary as named keyword arguments.",
                    "Passes the dictionary as a single argument.",
                    "Creates a pointer to the dictionary.",
                    "Calculates the power of the dictionary."
                ],
                correct_answer="Unpacks the key-value pairs of the dictionary as named keyword arguments.",
                explanation="The double star `**` unpacks dictionaries into keyword arguments."
            )
        ]
    )
]
