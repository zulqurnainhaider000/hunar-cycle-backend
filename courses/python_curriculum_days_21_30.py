"""
Days 21 to 30 of Python Mastery (35 Days)
Includes:
- Day 24 Project: Text-Based RPG Battle Simulator
- Day 30 Project: Complete OOP Banking & ATM Simulation System
"""

from seeder.course_blueprint import DayBlueprint, QuizQuestionBlueprint, CodingChallengeBlueprint

DAYS_21_TO_30 = [
    # -------------------------------------------------------------
    # DAY 21
    # -------------------------------------------------------------
    DayBlueprint(
        order=21,
        title="Day 21: Variable Scope & The LEGB Resolution Rule",
        concept="Namespace visibility, the global and nonlocal keywords, and the LEGB lookup hierarchy",
        analogy="Think of variable scope like Russian nesting dolls! When you are standing inside the smallest inner doll (Local), you can look out through the transparent layers and see variables in the parent doll (Enclosing), the big doll (Global), and the room itself (Built-in). But someone outside the doll cannot look inside to see your local secrets!",
        theory_sections=[
            {
                "heading": "The LEGB Lookup Hierarchy",
                "body": "When you reference a variable name in Python, the interpreter searches four namespaces in strict order:\n1. **L (Local)**: Defined inside the current active function.\n2. **E (Enclosing)**: Defined in enclosing/outer nested functions.\n3. **G (Global)**: Defined at the top-level module script.\n4. **B (Built-in)**: Pre-assigned built-in names (e.g. `len`, `range`, `print`)."
            },
            {
                "heading": "The global and nonlocal Keywords",
                "body": "Reading global variables from inside a function is permitted by default. However, assigning to a variable inside a function creates a new **local** variable by default. To modify an existing global variable, you must explicitly declare `global var_name`. Similarly, to modify an enclosing variable inside a closure, use `nonlocal var_name`."
            }
        ],
        code_snippets=[
            {
                "title": "Local vs Global Scope Demonstration",
                "code": "app_name = 'Hunar System'  # Global\n\ndef show_scope():\n    version = '2.4.0'       # Local to show_scope\n    print(f'Inside function: {app_name} v{version}')\n\nshow_scope()\n# print(version)  # Uncommenting raises NameError: name 'version' is not defined"
            },
            {
                "title": "The global Keyword",
                "code": "counter = 0\n\ndef increment():\n    global counter\n    counter += 1\n\nincrement()\nincrement()\nprint('Global counter after 2 calls:', counter)"
            },
            {
                "title": "Enclosing Scope & nonlocal in Nested Functions",
                "code": "def make_multiplier(factor):\n    # Enclosing scope\n    def multiply(number):\n        # Accesses 'factor' from enclosing scope\n        return number * factor\n    return multiply\n\ndouble = make_multiplier(2)\ntriple = make_multiplier(3)\nprint('Double 10:', double(10))\nprint('Triple 10:', triple(10))"
            },
            {
                "title": "Inspecting Scope Dictionaries with locals() and globals()",
                "code": "def inspect_me(a, b):\n    c = a + b\n    print('Local variables dict:', locals())\n\ninspect_me(5, 10)"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Create a Closure Counter with nonlocal",
            description="Write a function `create_counter()` that returns an inner function that increments and returns a count each time it is called using `nonlocal`. Test by calling it 3 times and print: 'Count after 3 ticks: 3'.",
            starter_code="# TODO: Implement create_counter closure\n",
            solution_code="def create_counter():\n    count = 0\n    def tick():\n        nonlocal count\n        count += 1\n        return count\n    return tick\n\nc = create_counter()\nc(); c()\nfinal_count = c()\nprint('Count after 3 ticks:', final_count)",
            expected_output="Count after 3 ticks: 3"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What does the LEGB acronym stand for in Python variable resolution?",
                options=[
                    "Local, Enclosing, Global, Built-in",
                    "Lexical, External, Generic, Binary",
                    "List, Element, Group, Block",
                    "Loop, Expression, Generator, Branch"
                ],
                correct_answer="Local, Enclosing, Global, Built-in",
                explanation="LEGB defines the exact order Python traverses to find variable bindings."
            ),
            QuizQuestionBlueprint(
                question="What happens if you assign a variable inside a function without the global keyword?",
                options=[
                    "Python creates a new local variable in that function's namespace.",
                    "Python automatically updates the global variable.",
                    "A NameError is thrown.",
                    "The variable is placed in the Built-in namespace."
                ],
                correct_answer="Python creates a new local variable in that function's namespace.",
                explanation="Assignment inside a function defaults to creating or modifying local scope."
            ),
            QuizQuestionBlueprint(
                question="When should the nonlocal keyword be used?",
                options=[
                    "To modify a variable in the nearest enclosing (outer) function that is not global.",
                    "To define a variable that can be accessed across different servers.",
                    "To declare a constant in C extensions.",
                    "To make a variable accessible in HTML templates."
                ],
                correct_answer="To modify a variable in the nearest enclosing (outer) function that is not global.",
                explanation="`nonlocal` binds names in outer enclosing functions for closures."
            ),
            QuizQuestionBlueprint(
                question="Why is excessive use of the global keyword considered poor engineering practice?",
                options=[
                    "It introduces hidden side effects and makes code hard to test and debug.",
                    "It slows down Python execution by 500%.",
                    "It causes memory leaks that crash the computer.",
                    "It is deprecated in Python 3."
                ],
                correct_answer="It introduces hidden side effects and makes code hard to test and debug.",
                explanation="Global state increases coupling and makes isolating bugs and unit testing difficult."
            ),
            QuizQuestionBlueprint(
                question="Which namespace is searched last in the LEGB hierarchy?",
                options=["Built-in", "Global", "Enclosing", "Local"],
                correct_answer="Built-in",
                explanation="If a name is not found in Local, Enclosing, or Global, Python checks Built-in as the final resort."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 22
    # -------------------------------------------------------------
    DayBlueprint(
        order=22,
        title="Day 22: Lambda Functions, map(), and filter()",
        concept="Anonymous single-expression functions and functional sequence transformations",
        analogy="Think of a lambda like a disposable paper coffee cup compared to a ceramic mug (standard `def` function). When you just need a quick sip of coffee on the go for 10 seconds, you don't build a dishwasher-safe ceramic mug; you grab a quick disposable cup!",
        theory_sections=[
            {
                "heading": "Anonymous Lambda Functions",
                "body": "A `lambda` function is a small, anonymous function defined inline without a name using the syntax `lambda arguments: expression`. Lambdas can take any number of arguments, but can only contain a single expression whose result is automatically returned."
            },
            {
                "heading": "Functional Primitives: map() and filter()",
                "body": "- `map(func, iterable)`: Applies `func` to every item in the iterable, producing a transformed stream.\n- `filter(func, iterable)`: Tests each item with `func` (which returns True/False) and retains only items where the result is True.\n- Lambdas are also heavily used in `sorted()` via the `key=` parameter!"
            }
        ],
        code_snippets=[
            {
                "title": "Lambda Syntax Comparison",
                "code": "# Standard function\ndef square_def(x): return x ** 2\n\n# Equivalent Lambda function\nsquare_lambda = lambda x: x ** 2\n\nprint('Def:', square_def(5))\nprint('Lambda:', square_lambda(5))"
            },
            {
                "title": "Transforming Sequences with map()",
                "code": "prices_usd = [10.0, 25.5, 99.0]\n# Convert USD to PKR using conversion rate (e.g. 280)\nprices_pkr = list(map(lambda p: p * 280, prices_usd))\nprint('Prices in PKR:', prices_pkr)"
            },
            {
                "title": "Filtering Data with filter()",
                "code": "temperatures = [18, 24, 31, 15, 29, 35, 22]\n# Keep only hot days (> 28 degrees)\nhot_days = list(filter(lambda t: t > 28, temperatures))\nprint('Hot days list:', hot_days)"
            },
            {
                "title": "Custom Sorting with Lambda key",
                "code": "students = [\n    {'name': 'Zayd', 'score': 88},\n    {'name': 'Amna', 'score': 95},\n    {'name': 'Bilal', 'score': 74}\n]\n# Sort students by score descending\nstudents.sort(key=lambda s: s['score'], reverse=True)\nprint('Ranked leaderboard:', students)"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Filter and Double Even Numbers",
            description="Given `nums = [1, 2, 3, 4, 5, 6]`. Use `filter()` with a lambda to keep only evens, and `map()` with a lambda to double them. Print: 'Doubled Evens: [4, 8, 12]'.",
            starter_code="nums = [1, 2, 3, 4, 5, 6]\n# TODO: Filter evens, map double\n",
            solution_code="nums = [1, 2, 3, 4, 5, 6]\nevens = filter(lambda x: x % 2 == 0, nums)\ndoubled = list(map(lambda x: x * 2, evens))\nprint('Doubled Evens:', doubled)",
            expected_output="Doubled Evens: [4, 8, 12]"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the key limitation of a Python lambda function?",
                options=[
                    "It can only contain a single expression and cannot contain complex statements or assignments.",
                    "It cannot take more than one argument.",
                    "It can only work with integer data types.",
                    "It cannot return values."
                ],
                correct_answer="It can only contain a single expression and cannot contain complex statements or assignments.",
                explanation="Lambdas are restricted to a single evaluated expression that forms the return value."
            ),
            QuizQuestionBlueprint(
                question="What type of object is returned by map() and filter() in Python 3?",
                options=[
                    "An iterator (generator-like map/filter object) evaluated lazily",
                    "A standard Python list",
                    "A dictionary",
                    "A tuple"
                ],
                correct_answer="An iterator (generator-like map/filter object) evaluated lazily",
                explanation="In Python 3, `map` and `filter` return lazy iterators; wrap in `list()` to evaluate eagerly."
            ),
            QuizQuestionBlueprint(
                question="What does the key parameter in sorted(iterable, key=...) do?",
                options=[
                    "Specifies a one-argument function to extract a comparison key from each element.",
                    "Specifies a database primary key.",
                    "Sets the cryptographic encryption key.",
                    "Limits sorting to only dictionary keys."
                ],
                correct_answer="Specifies a one-argument function to extract a comparison key from each element.",
                explanation="The `key` function extracts a value from each element to use as the sorting criterion."
            ),
            QuizQuestionBlueprint(
                question="What is the output of: (lambda a, b: a if a > b else b)(12, 20)?",
                options=["20", "12", "True", "Raises SyntaxError"],
                correct_answer="20",
                explanation="The lambda evaluates the ternary: 12 > 20 is False, so it returns b (20)."
            ),
            QuizQuestionBlueprint(
                question="Which keyword starts the definition of an anonymous function?",
                options=["lambda", "anonymous", "inline", "proc"],
                correct_answer="lambda",
                explanation="`lambda` is the reserved keyword in Python for anonymous functions."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 23
    # -------------------------------------------------------------
    DayBlueprint(
        order=23,
        title="Day 23: List, Dictionary & Set Comprehensions",
        concept="Concise, idiomatic sequence transformations using comprehension syntax",
        analogy="Imagine an industrial pasta extruder machine. Instead of rolling out dough by hand, cutting each noodle, and placing it on a tray with 4 separate manual steps, the machine extrudes 500 perfect star-shaped noodles in a single continuous stream directly into the boiling pot!",
        theory_sections=[
            {
                "heading": "The Anatomy of a Comprehension",
                "body": "Comprehensions provide a concise way to create collections from existing iterables. The general syntax is:\n`[expression for item in iterable if condition]`\nThis replaces 4-line `for` loops with an append call, and runs significantly faster in CPython because bytecode loops are optimized internally."
            },
            {
                "heading": "Dictionary & Set Comprehensions",
                "body": "- **Set comprehension**: `{expr for item in iterable}` produces a deduplicated set.\n- **Dictionary comprehension**: `{key_expr: val_expr for item in iterable}` creates a dict mapping dynamically."
            }
        ],
        code_snippets=[
            {
                "title": "Traditional Loop vs List Comprehension",
                "code": "# Old way with append\nnums = [1, 2, 3, 4, 5]\nsquares_old = []\nfor n in nums:\n    squares_old.append(n ** 2)\n\n# Modern List Comprehension\nsquares_comp = [n ** 2 for n in nums]\nprint('Squares:', squares_comp)"
            },
            {
                "title": "Filtering with if Clauses in Comprehensions",
                "code": "words = ['code', 'python', 'ai', 'developer', 'ml', 'django']\n# Keep words with 4 or more letters and uppercase them\nlong_words = [w.upper() for w in words if len(w) >= 4]\nprint('Long words uppercase:', long_words)"
            },
            {
                "title": "Dictionary Comprehension",
                "code": "cities = ['Karachi', 'Lahore', 'Islamabad']\n# Map each city to its string character length\ncity_lengths = {city: len(city) for city in cities}\nprint('City length map:', city_lengths)"
            },
            {
                "title": "Nested List Comprehension (Matrix Flattening)",
                "code": "grid = [[1, 2], [3, 4], [5, 6]]\nflattened = [val for row in grid for val in row]\nprint('Flattened 1D list:', flattened)"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Create Price Discount Map Using Dict Comprehension",
            description="Given `catalog = {'Shirt': 50, 'Shoes': 100, 'Cap': 20}`. Create a new dictionary `discounted` where all items over $30 get a 20% discount (`price * 0.8`). Print: 'Discounted: {'Shirt': 40.0, 'Shoes': 80.0}'.",
            starter_code="catalog = {'Shirt': 50, 'Shoes': 100, 'Cap': 20}\n# TODO: Dict comprehension for items > 30\n",
            solution_code="catalog = {'Shirt': 50, 'Shoes': 100, 'Cap': 20}\ndiscounted = {k: v * 0.8 for k, v in catalog.items() if v > 30}\nprint('Discounted:', discounted)",
            expected_output="Discounted: {'Shirt': 40.0, 'Shoes': 80.0}"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the primary advantage of list comprehensions over traditional for-loops with .append()?",
                options=[
                    "More concise, readable syntax and faster execution in CPython.",
                    "They allow multi-threading automatically.",
                    "They can run without installing Python.",
                    "They consume zero memory."
                ],
                correct_answer="More concise, readable syntax and faster execution in CPython.",
                explanation="Comprehensions are optimized in C bytecode and express mapping/filtering cleanly."
            ),
            QuizQuestionBlueprint(
                question="What will [x for x in range(5) if x % 2 == 0] produce?",
                options=["[0, 2, 4]", "[2, 4]", "[1, 3]", "[0, 1, 2, 3, 4]"],
                correct_answer="[0, 2, 4]",
                explanation="Range(5) generates 0, 1, 2, 3, 4. Even numbers are 0, 2, 4."
            ),
            QuizQuestionBlueprint(
                question="How do you write a Set Comprehension in Python?",
                options=[
                    "{x ** 2 for x in nums}",
                    "[x ** 2 for x in nums]",
                    "(x ** 2 for x in nums)",
                    "set(x for x in nums)"
                ],
                correct_answer="{x ** 2 for x in nums}",
                explanation="Enclosing the comprehension in `{}` without colons creates a set."
            ),
            QuizQuestionBlueprint(
                question="What does (x for x in range(1000)) with parentheses produce instead of a list?",
                options=["A generator expression (lazy iterator)", "A tuple", "A SyntaxError", "An immutable list"],
                correct_answer="A generator expression (lazy iterator)",
                explanation="Parentheses create a generator expression which produces items on demand."
            ),
            QuizQuestionBlueprint(
                question="Can you use if-else conditional expressions in the expression part of a list comprehension?",
                options=[
                    "Yes: ['Even' if x % 2 == 0 else 'Odd' for x in numbers]",
                    "No, if-else is forbidden in comprehensions.",
                    "Only with integers.",
                    "Only in Python 3.12+."
                ],
                correct_answer="Yes: ['Even' if x % 2 == 0 else 'Odd' for x in numbers]",
                explanation="Ternary if-else expressions are valid in the left-hand transformation position."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 24 - PROJECT DAY 4
    # -------------------------------------------------------------
    DayBlueprint(
        order=24,
        title="Day 24: [PROJECT 4] Text-Based RPG Battle Simulator",
        concept="Developing a complete turn-based role-playing combat engine with stats, random actions, and victory states",
        analogy="You are programming the battle engine of Pokémon or Final Fantasy! Two fighters face off in the arena, exchanging attacks, drinking health potions, and defending until one hero emerges victorious.",
        is_project_day=True,
        project_name="Text-Based RPG Battle Simulator",
        theory_sections=[
            {
                "heading": "Game Mechanics & Entities",
                "body": "In this RPG simulator, we define two entities: **The Hero** and **The Monster**. Each entity possesses attributes: `name`, `hp`, `max_hp`, `attack_power`, and `heal_potions`."
            },
            {
                "heading": "Turn-Based Combat Loop",
                "body": "The combat proceeds in sequential rounds. On the player's turn, choices include:\n1. **Strike**: Deal damage with random variance (`base_power ± 5`).\n2. **Heal**: Drink potion to recover health.\n3. **Defend**: Reduce damage on the monster's next turn by 50%.\nThen the monster counterattacks automatically!"
            }
        ],
        code_snippets=[
            {
                "title": "Character Entity Representation",
                "code": "import random\n\ndef create_fighter(name: str, hp: int, attack: int, potions: int):\n    return {\n        'name': name,\n        'hp': hp,\n        'max_hp': hp,\n        'attack': attack,\n        'potions': potions,\n        'is_defending': False\n    }"
            },
            {
                "title": "Action Handlers: Attack and Heal",
                "code": "def deal_damage(attacker, defender):\n    variance = random.randint(-3, 3)\n    dmg = max(1, attacker['attack'] + variance)\n    if defender['is_defending']:\n        dmg = max(1, dmg // 2)\n        defender['is_defending'] = False # Shield used\n    defender['hp'] = max(0, defender['hp'] - dmg)\n    return dmg\n\ndef drink_potion(fighter):\n    if fighter['potions'] > 0:\n        fighter['potions'] -= 1\n        heal_amt = 25\n        fighter['hp'] = min(fighter['max_hp'], fighter['hp'] + heal_amt)\n        return heal_amt\n    return 0"
            },
            {
                "title": "Full Automated Battle Simulation Execution",
                "code": "def simulate_battle():\n    hero = create_fighter('Aragorn', hp=60, attack=15, potions=2)\n    monster = create_fighter('Goblin Chieftain', hp=50, attack=12, potions=0)\n    \n    print(f'⚔️ BATTLE START: {hero[\"name\"]} vs {monster[\"name\"]}')\n    round_num = 1\n    \n    while hero['hp'] > 0 and monster['hp'] > 0:\n        print(f'--- Round {round_num} ---')\n        # Hero Turn\n        if hero['hp'] < 25 and hero['potions'] > 0:\n            healed = drink_potion(hero)\n            print(f'💚 {hero[\"name\"]} drank a potion and restored {healed} HP! [HP: {hero[\"hp\"]}]')\n        else:\n            dmg = deal_damage(hero, monster)\n            print(f'🗡️ {hero[\"name\"]} struck {monster[\"name\"]} for {dmg} damage! [Boss HP: {monster[\"hp\"]}]')\n            \n        if monster['hp'] == 0:\n            print(f'🎉 {hero[\"name\"]} defeated the {monster[\"name\"]} in round {round_num}!')\n            return 'Hero Wins'\n            \n        # Monster Turn\n        m_dmg = deal_damage(monster, hero)\n        print(f'👹 {monster[\"name\"]} hits back for {m_dmg} damage! [Hero HP: {hero[\"hp\"]}]')\n        \n        if hero['hp'] == 0:\n            print('💀 Hero was slain in battle!')\n            return 'Monster Wins'\n        round_num += 1\n\nsimulate_battle()"
            },
            {
                "title": "ASCII Health Bar Visualizer",
                "code": "def render_health_bar(name: str, current: int, maximum: int):\n    filled_slots = int((current / maximum) * 10)\n    empty_slots = 10 - filled_slots\n    bar = '█' * filled_slots + '░' * empty_slots\n    return f'{name:<10} [{bar}] {current}/{maximum} HP'\n\nprint(render_health_bar('Hero', 45, 60))\nprint(render_health_bar('Monster', 15, 50))"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Implement Critical Hit Mechanic",
            description="Write a function `calculate_critical_strike(base_damage, is_critical)` that multiplies damage by 2 if `is_critical` is True, otherwise returns `base_damage`. Test with `base = 18` and `critical = True`. Print: 'Critical Damage: 36'.",
            starter_code="base = 18\ncritical = True\n# TODO: Calculate damage\n",
            solution_code="base = 18\ncritical = True\ndef calculate_critical_strike(dmg: int, crit: bool) -> int:\n    return dmg * 2 if crit else dmg\n\nprint('Critical Damage:', calculate_critical_strike(base, critical))",
            expected_output="Critical Damage: 36"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What condition keeps the RPG battle loop executing?",
                options=[
                    "while hero['hp'] > 0 and monster['hp'] > 0",
                    "while round_num < 100",
                    "while True: pass",
                    "for i in range(10)"
                ],
                correct_answer="while hero['hp'] > 0 and monster['hp'] > 0",
                explanation="The battle continues as long as both combatants have remaining health."
            ),
            QuizQuestionBlueprint(
                question="Why is max(0, current_hp - damage) used when subtracting damage in game programming?",
                options=[
                    "To prevent health from displaying as a negative number below 0.",
                    "Because Python cannot store negative integers.",
                    "To speed up float calculations.",
                    "It automatically revives the character."
                ],
                correct_answer="To prevent health from displaying as a negative number below 0.",
                explanation="Using `max(0, ...)` clamps health at zero so characters don't have -12 HP."
            ),
            QuizQuestionBlueprint(
                question="What does min(max_hp, current_hp + heal) ensure when drinking potions?",
                options=[
                    "It prevents overhealing beyond the character's maximum health pool.",
                    "It empties the potion bottle.",
                    "It calculates critical heals.",
                    "It turns potions into coins."
                ],
                correct_answer="It prevents overhealing beyond the character's maximum health pool.",
                explanation="Clamping with `min()` ensures healing cannot exceed maximum capacity."
            ),
            QuizQuestionBlueprint(
                question="Which function from the random module generates an integer between -3 and +3 inclusive?",
                options=["random.randint(-3, 3)", "random.random(-3, 3)", "random.choice(-3, 3)", "random.range(-3, 3)"],
                correct_answer="random.randint(-3, 3)",
                explanation="`random.randint(a, b)` generates uniform random integers between `a` and `b` inclusive."
            ),
            QuizQuestionBlueprint(
                question="How does defending work in our game logic?",
                options=[
                    "It halves incoming damage on the monster's turn, then resets the defending flag.",
                    "It prevents the hero from ever taking damage again.",
                    "It reflects 100% of damage back to the attacker.",
                    "It skips the monster's turn completely."
                ],
                correct_answer="It halves incoming damage on the monster's turn, then resets the defending flag.",
                explanation="A boolean flag `is_defending` temporarily reduces next damage, then resets."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 25
    # -------------------------------------------------------------
    DayBlueprint(
        order=25,
        title="Day 25: Exception Handling: try, except, else & finally",
        concept="Graceful runtime error recovery, catching specific exception types, and cleanup",
        analogy="Think of exception handling like a circus trapeze safety net! When an acrobat slips in mid-air (an unexpected error occurs), instead of crashing onto the hard concrete floor (program crashes), the soft safety net catches them safely (`except`), so the circus show can continue smoothly!",
        theory_sections=[
            {
                "heading": "The Purpose of Exception Handling",
                "body": "Bugs and unexpected user input are inevitable. Rather than allowing Python to terminate with a traceback, you wrap risky operations inside a `try` block. If an error occurs, Python jumps immediately into matching `except` blocks."
            },
            {
                "heading": "The 4-Part Structure: try, except, else, finally",
                "body": "- `try`: Code that might raise an exception.\n- `except SpecificError as e`: Handles only that error type gracefully.\n- `else`: Runs ONLY if the try block succeeded without any errors.\n- `finally`: ALWAYS runs no matter what (used for closing database connections and files)."
            }
        ],
        code_snippets=[
            {
                "title": "Catching ZeroDivisionError and ValueError",
                "code": "def divide_strings(a_str: str, b_str: str):\n    try:\n        a = float(a_str)\n        b = float(b_str)\n        result = a / b\n    except ValueError:\n        return '❌ Error: Please provide valid numerical inputs!'\n    except ZeroDivisionError:\n        return '🚨 Error: Division by zero is mathematically undefined!'\n    else:\n        return f'✅ Success: Result is {result:.2f}'\n\nprint(divide_strings('10', '2'))\nprint(divide_strings('10', '0'))\nprint(divide_strings('abc', '5'))"
            },
            {
                "title": "The Guaranteed Execution of finally",
                "code": "def simulate_database_query():\n    print('1. Connecting to database...')\n    try:\n        print('2. Executing SQL query...')\n        # Simulate an error\n        x = 1 / 0\n    except ZeroDivisionError:\n        print('3. Caught database query error!')\n    finally:\n        print('4. Disconnecting database socket (always executed).')\n\nsimulate_database_query()"
            },
            {
                "title": "Accessing the Exception Object (as e)",
                "code": "try:\n    data = {'title': 'Python'}\n    print(data['author'])\nexcept KeyError as err:\n    print(f'Missing required key: {err}')"
            },
            {
                "title": "Catching Multiple Exceptions in One Line",
                "code": "try:\n    raw = int('hello')\nexcept (ValueError, TypeError) as e:\n    print('Caught type or value conversion issue:', type(e).__name__)"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Safe Integer Input Parser",
            description="Write a function `safe_int_parse(val, fallback)` that returns `int(val)` if possible, but catches `(ValueError, TypeError)` and returns `fallback`. Test with `val = 'invalid'` and `fallback = -1`. Print: 'Parsed: -1'.",
            starter_code="# TODO: Implement safe_int_parse\n",
            solution_code="def safe_int_parse(val, fallback):\n    try:\n        return int(val)\n    except (ValueError, TypeError):\n        return fallback\n\nprint('Parsed:', safe_int_parse('invalid', -1))",
            expected_output="Parsed: -1"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Why is a bare except: (catching all exceptions indiscriminately) considered bad practice?",
                options=[
                    "It accidentally intercepts system exit signals (SystemExit, KeyboardInterrupt) and obscures bugs.",
                    "It causes a compilation error in Python 3.",
                    "It disables garbage collection.",
                    "It makes code run 10x slower."
                ],
                correct_answer="It accidentally intercepts system exit signals (SystemExit, KeyboardInterrupt) and obscures bugs.",
                explanation="Catching all exceptions prevents users from terminating scripts with Ctrl+C and hides typos."
            ),
            QuizQuestionBlueprint(
                question="When does the else block of a try-except statement execute?",
                options=[
                    "Only when NO exceptions occurred in the try block.",
                    "Whenever an exception was caught and handled.",
                    "Always, right before finally.",
                    "Only when the try block raised an AssertionError."
                ],
                correct_answer="Only when NO exceptions occurred in the try block.",
                explanation="The `else` branch runs only if the `try` suite executed without raising an exception."
            ),
            QuizQuestionBlueprint(
                question="What guarantee does the finally block provide?",
                options=[
                    "It will execute regardless of whether an exception was raised, caught, or unhandled.",
                    "It guarantees all variables are saved to disk.",
                    "It suppresses all errors.",
                    "It automatically rolls back database transactions."
                ],
                correct_answer="It will execute regardless of whether an exception was raised, caught, or unhandled.",
                explanation="The `finally` clause always executes upon leaving the try construct."
            ),
            QuizQuestionBlueprint(
                question="Which built-in exception is raised when looking up a missing key in a dictionary?",
                options=["KeyError", "IndexError", "LookupError", "ValueError"],
                correct_answer="KeyError",
                explanation="A dictionary lookup with a missing key raises a `KeyError`."
            ),
            QuizQuestionBlueprint(
                question="What exception is raised when trying to add a string to an integer ('5' + 5)?",
                options=["TypeError", "ValueError", "ArithmeticError", "SyntaxError"],
                correct_answer="TypeError",
                explanation="Mixing unsupported operand types raises `TypeError`."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 26
    # -------------------------------------------------------------
    DayBlueprint(
        order=26,
        title="Day 26: Raising Exceptions & Custom Exception Classes",
        concept="Enforcing business rules using raise and inheriting from Exception",
        analogy="Think of a smoke detector in a kitchen! When burnt toast causes smoke, the detector doesn't stay quiet; it blasts a loud siren (`raise SmokeDetectedError()`). Creating custom exceptions lets you build specialized alarms for your exact business requirements!",
        theory_sections=[
            {
                "heading": "The raise Keyword",
                "body": "You don't have to wait for Python to encounter an arithmetic or syntax error to stop execution. When an input violates your domain rules (e.g. negative bank balance or invalid email format), you trigger an error proactively using `raise ValueError('message')`."
            },
            {
                "heading": "Custom Exception Classes",
                "body": "In production backends, standard Python exceptions are often too generic. By creating custom exception classes that inherit from `Exception`, your API can distinguish domain-specific errors (e.g. `InsufficientFundsError`, `InvalidAuthTokenError`)."
            }
        ],
        code_snippets=[
            {
                "title": "Raising Built-in Exceptions for Rule Enforcement",
                "code": "def set_account_age(age: int):\n    if not isinstance(age, int):\n        raise TypeError('Age must be an integer!')\n    if age < 13:\n        raise ValueError('User must be at least 13 years old to register!')\n    return f'Account registered for age {age}.'\n\nprint(set_account_age(20))"
            },
            {
                "title": "Defining Custom Exception Classes",
                "code": "class InsufficientFundsError(Exception):\n    \"\"\"Raised when a withdrawal exceeds account balance.\"\"\"\n    def __init__(self, current_balance, attempted_amount):\n        self.deficit = attempted_amount - current_balance\n        super().__init__(f'Short by ${self.deficit:.2f}! Balance is ${current_balance:.2f}.')\n\ndef withdraw(balance, amount):\n    if amount > balance:\n        raise InsufficientFundsError(balance, amount)\n    return balance - amount"
            },
            {
                "title": "Catching Custom Exceptions Cleanly",
                "code": "try:\n    new_bal = withdraw(balance=100.0, amount=250.0)\nexcept InsufficientFundsError as err:\n    print(f'🚨 Transaction Denied: {err}')\n    print(f'Need to deposit ${err.deficit:.2f} more.')"
            },
            {
                "title": "Re-raising Exceptions for Logging (bare raise)",
                "code": "try:\n    num = int('invalid')\nexcept ValueError as err:\n    print('Logging error to monitoring service...')\n    # Re-raises the same exception to outer callers\n    # raise"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Create an InvalidPasswordError Class",
            description="Define a custom exception `InvalidPasswordError(Exception)`. Write a function `check_password(pwd)` that raises `InvalidPasswordError` if `len(pwd) < 8`. Catch the error and print: 'Auth Alert: Password must be at least 8 characters!'.",
            starter_code="# TODO: Define custom exception and validation function\n",
            solution_code="class InvalidPasswordError(Exception):\n    pass\n\ndef check_password(pwd: str):\n    if len(pwd) < 8:\n        raise InvalidPasswordError('Password must be at least 8 characters!')\n\ntry:\n    check_password('short')\nexcept InvalidPasswordError as e:\n    print(f'Auth Alert: {e}')",
            expected_output="Auth Alert: Password must be at least 8 characters!"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Which keyword is used to trigger an exception manually in Python?",
                options=["raise", "throw", "error", "catch"],
                correct_answer="raise",
                explanation="In Python, `raise` is used to trigger an exception (unlike Java/JS which use `throw`)."
            ),
            QuizQuestionBlueprint(
                question="What class should all custom user-defined exceptions inherit from in Python?",
                options=["Exception", "BaseException", "ErrorClass", "object"],
                correct_answer="Exception",
                explanation="User-defined exceptions should inherit from `Exception`. `BaseException` is reserved for system exits."
            ),
            QuizQuestionBlueprint(
                question="What does a bare raise statement inside an except block do?",
                options=[
                    "Re-raises the active exception currently being handled.",
                    "Raises a generic RuntimeError.",
                    "Terminates the operating system.",
                    "Clears the call stack."
                ],
                correct_answer="Re-raises the active exception currently being handled.",
                explanation="A bare `raise` re-throws the current exception with its original traceback intact."
            ),
            QuizQuestionBlueprint(
                question="Can custom exceptions store additional attributes and metadata?",
                options=[
                    "Yes, by defining custom attributes in the __init__() method.",
                    "No, exceptions can only store string messages.",
                    "Only if they inherit from SystemError.",
                    "Only in Python 3.11+."
                ],
                correct_answer="Yes, by defining custom attributes in the __init__() method.",
                explanation="Custom exception classes are regular Python classes and can store any metadata."
            ),
            QuizQuestionBlueprint(
                question="What is the result of executing raise ValueError('Invalid input')?",
                options=[
                    "Immediately stops normal execution and propagates ValueError up the call stack.",
                    "Prints a warning to console and continues execution.",
                    "Writes the message to a log file silently.",
                    "Converts the value to None."
                ],
                correct_answer="Immediately stops normal execution and propagates ValueError up the call stack.",
                explanation="`raise` initiates exception propagation up the call stack until caught or crashing."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 27
    # -------------------------------------------------------------
    DayBlueprint(
        order=27,
        title="Day 27: File I/O: Reading and Writing Files",
        concept="Persistent disk storage, open() modes (r, w, a), and reading file buffers",
        analogy="Think of File I/O like handling a physical leather binder on your desk! You reach into the bookshelf and open the binder (`open()`). You read the pages or write fresh notes with your pen (`read()`, `write()`). And most importantly, you snap the binder shut when finished (`close()`) so nobody spills coffee on it!",
        theory_sections=[
            {
                "heading": "File Access Modes in Python",
                "body": "Python interacts with operating system files using the `open(filename, mode)` function:\n- `'r'`: Read mode (default; errors if file does not exist).\n- `'w'`: Write mode (creates new file or **overwrites** existing file completely!).\n- `'a'`: Append mode (writes data to the very end without deleting existing content).\n- `'r+'`: Read and write simultaneously."
            },
            {
                "heading": "Reading Strategies: read(), readline(), and readlines()",
                "body": "- `.read()`: Reads the entire file into a single string (watch out for gigabyte-sized files!).\n- `.readline()`: Reads a single line.\n- Iterating directly `for line in file:`: Reads line-by-line efficiently in O(1) memory."
            }
        ],
        code_snippets=[
            {
                "title": "Writing Data to a File",
                "code": "# Writing text to a sample file\nf = open('sample_output.txt', 'w', encoding='utf-8')\nf.write('Line 1: Hunar Cycle Python Course\\n')\nf.write('Line 2: Mastering File Operations\\n')\nf.close() # Always close manually if not using context manager"
            },
            {
                "title": "Reading File Content Efficiently",
                "code": "f = open('sample_output.txt', 'r', encoding='utf-8')\ncontent = f.read()\nf.close()\nprint('File Content:\\n' + content)"
            },
            {
                "title": "Appending Content Without Overwriting",
                "code": "f = open('sample_output.txt', 'a', encoding='utf-8')\nf.write('Line 3: Appended audit log entry\\n')\nf.close()"
            },
            {
                "title": "Streaming Line-by-Line Iteration",
                "code": "f = open('sample_output.txt', 'r', encoding='utf-8')\nfor idx, line in enumerate(f, start=1):\n    print(f'{idx}: {line.strip()}')\nf.close()"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Count Total Lines in Text String Buffer",
            description="Given `buffer = 'Apple\\nBanana\\nCherry\\nDate'`. Split the lines or count newlines, and print: 'Total lines: 4'.",
            starter_code="buffer = 'Apple\\nBanana\\nCherry\\nDate'\n# TODO: Count lines\n",
            solution_code="buffer = 'Apple\\nBanana\\nCherry\\nDate'\nlines = buffer.strip().split('\\n')\nprint('Total lines:', len(lines))",
            expected_output="Total lines: 4"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What happens if you open an existing file with mode 'w' in Python?",
                options=[
                    "The existing file is immediately truncated (wiped empty) for new writing.",
                    "The new content is appended to the end.",
                    "Python raises a FileExistsError.",
                    "The file opens in read-only mode."
                ],
                correct_answer="The existing file is immediately truncated (wiped empty) for new writing.",
                explanation="Mode `'w'` overwrites existing files; use `'a'` to append."
            ),
            QuizQuestionBlueprint(
                question="Why is it important to specify encoding='utf-8' when opening text files?",
                options=[
                    "It ensures cross-platform character compatibility across Windows, Mac, and Linux.",
                    "It encrypts the file on disk.",
                    "It compresses file size.",
                    "It is required by the operating system kernel."
                ],
                correct_answer="It ensures cross-platform character compatibility across Windows, Mac, and Linux.",
                explanation="Default encodings vary by OS (e.g. cp1252 on Windows); UTF-8 prevents decoding corruption."
            ),
            QuizQuestionBlueprint(
                question="What exception is raised when trying to open a non-existent file in 'r' mode?",
                options=["FileNotFoundError", "MissingFileException", "IOClosedError", "DirectoryError"],
                correct_answer="FileNotFoundError",
                explanation="Opening a missing file in read mode raises `FileNotFoundError`."
            ),
            QuizQuestionBlueprint(
                question="Which method reads an entire file into memory as a list of strings line by line?",
                options=[".readlines()", ".readall()", ".getlines()", ".scan()"],
                correct_answer=".readlines()",
                explanation="`.readlines()` reads all lines and returns them as a list of string elements."
            ),
            QuizQuestionBlueprint(
                question="What is the most memory-efficient way to process a 10 GB log file in Python?",
                options=[
                    "Iterate over the file object directly: for line in file_handle:",
                    "Call file_handle.read() into a single variable.",
                    "Call file_handle.readlines()",
                    "Convert the file into a JSON string."
                ],
                correct_answer="Iterate over the file object directly: for line in file_handle:",
                explanation="Iterating over the file handle streams lines one at a time, consuming minimal RAM."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 28
    # -------------------------------------------------------------
    DayBlueprint(
        order=28,
        title="Day 28: Context Managers & The with Statement",
        concept="Deterministic resource management, automatic cleanup, and the context protocol",
        analogy="Think of a context manager like an automatic bank vault door with an emergency air-lock. The moment you step in, the air-lock opens. When you leave—even if there is a fire, a blackout, or an earthquake—the door is guaranteed to slam shut and lock automatically! That is what the `with` statement does for files and sockets.",
        theory_sections=[
            {
                "heading": "The with Statement Guarantee",
                "body": "Opening files with `f = open()` is risky: if an unhandled exception occurs before `f.close()`, the file descriptor remains locked by the operating system, causing resource leaks. The `with` statement guarantees that the file is closed automatically the instant the block ends, even if errors crash the code inside!"
            },
            {
                "heading": "The Context Protocol: __enter__ and __exit__",
                "body": "Any object can become a context manager by implementing two magic methods:\n- `__enter__()`: Prepares resources and returns the target object.\n- `__exit__(exc_type, exc_val, exc_tb)`: Tears down and releases resources, handling any exceptions gracefully."
            }
        ],
        code_snippets=[
            {
                "title": "Idiomatic File Handling with with",
                "code": "# File automatically and safely closed at end of block\nwith open('auto_closed.txt', 'w', encoding='utf-8') as f:\n    f.write('Safe and clean resource management!\\n')\n\nprint('Is file closed?', f.closed) # Returns True!"
            },
            {
                "title": "Creating a Custom Context Manager Class",
                "code": "class Timer:\n    import time\n    def __enter__(self):\n        import time\n        self.start = time.time()\n        print('⏱️ Timer started...')\n        return self\n    def __exit__(self, exc_type, exc_val, exc_tb):\n        import time\n        elapsed = time.time() - self.start\n        print(f'⏱️ Completed in {elapsed:.4f} seconds.')\n\nwith Timer():\n    total = sum(i ** 2 for i in range(100000))"
            },
            {
                "title": "Opening Multiple Files Simultaneously",
                "code": "# Python allows comma-separated context managers in one with statement\nwith open('source.txt', 'w') as src, open('dest.txt', 'w') as dst:\n    src.write('Original data')\n    dst.write('Copied data')\nprint('Both files closed safely!')"
            },
            {
                "title": "Using contextlib.contextmanager Decorator",
                "code": "from contextlib import contextmanager\n\n@contextmanager\ntagged_block(tag_name):\n    print(f'<{tag_name}>')\n    yield\n    print(f'</{tag_name}>')\n\nwith tagged_block('div'):\n    print('Hello inside HTML div!')"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Implement a Banner Context Manager",
            description="Create a context manager class `Banner(msg)` that prints `=== START: {msg} ===` on enter, and `=== END: {msg} ===` on exit. Test it with message 'TEST'.",
            starter_code="# TODO: Implement Banner class with __enter__ and __exit__\n",
            solution_code="class Banner:\n    def __init__(self, msg):\n        self.msg = msg\n    def __enter__(self):\n        print(f'=== START: {self.msg} ===')\n    def __exit__(self, exc_type, exc_val, exc_tb):\n        print(f'=== END: {self.msg} ===')\n\nwith Banner('TEST'):\n    print('Running payload')",
            expected_output="=== START: TEST ===\nRunning payload\n=== END: TEST ==="
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the main benefit of using with open(...) as f: over manual open/close?",
                options=[
                    "It guarantees the file will be closed automatically, even if an exception occurs.",
                    "It makes reading 10x faster.",
                    "It automatically converts files to JSON.",
                    "It avoids needing write permissions."
                ],
                correct_answer="It guarantees the file will be closed automatically, even if an exception occurs.",
                explanation="The `with` construct ensures deterministic cleanup via `__exit__` under all circumstances."
            ),
            QuizQuestionBlueprint(
                question="What two methods must a Python class implement to support the context manager protocol?",
                options=["__enter__ and __exit__", "__start__ and __stop__", "__open__ and __close__", "__init__ and __del__"],
                correct_answer="__enter__ and __exit__",
                explanation="The context protocol is defined strictly by `__enter__()` and `__exit__()`."
            ),
            QuizQuestionBlueprint(
                question="What does the boolean f.closed indicate on a file object?",
                options=[
                    "Whether the underlying file stream has been successfully closed.",
                    "Whether the file is locked by another process.",
                    "Whether the file has zero bytes.",
                    "Whether the file exists on disk."
                ],
                correct_answer="Whether the underlying file stream has been successfully closed.",
                explanation="`f.closed` is True once the file descriptor is released."
            ),
            QuizQuestionBlueprint(
                question="Can you open multiple context managers in a single with statement?",
                options=[
                    "Yes, by separating them with commas: with open(a) as f1, open(b) as f2:",
                    "No, you must always nest separate with blocks.",
                    "Only in Python 2.7.",
                    "Only if both files are read-only."
                ],
                correct_answer="Yes, by separating them with commas: with open(a) as f1, open(b) as f2:",
                explanation="Python supports multiple context expressions separated by commas in a single `with` statement."
            ),
            QuizQuestionBlueprint(
                question="Which standard library module provides the @contextmanager generator decorator?",
                options=["contextlib", "os", "sys", "functools"],
                correct_answer="contextlib",
                explanation="`contextlib` provides utilities for working with context managers, including `@contextmanager`."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 29
    # -------------------------------------------------------------
    DayBlueprint(
        order=29,
        title="Day 29: Object-Oriented Programming: Classes & Objects",
        concept="Blueprints vs instances, the __init__ constructor, instance attributes, and self",
        analogy="Think of a Class like a metal cookie cutter or architectural blueprint. The blueprint itself is just paper—you cannot live inside a blueprint! But from that ONE blueprint, you can build 50 real brick houses (objects/instances). Each house has its own address, wall color, and owner!",
        theory_sections=[
            {
                "heading": "Classes as Blueprints, Objects as Instances",
                "body": "Object-Oriented Programming (OOP) models software around real-world entities that bundle state (attributes) and behavior (methods) together. The `class` keyword defines the blueprint. Calling the class constructor creates an instance (object) in memory."
            },
            {
                "heading": "The __init__ Constructor and self",
                "body": "- `__init__`: The initializer method called automatically when creating a new instance.\n- `self`: Represents the specific instance of the class being operated on. It allows each object to access and modify its own unique attributes."
            }
        ],
        code_snippets=[
            {
                "title": "Defining a Class and Creating Instances",
                "code": "class Car:\n    def __init__(self, brand: str, model: str, year: int):\n        # Instance attributes\n        self.brand = brand\n        self.model = model\n        self.year = year\n        self.odometer = 0\n    \n    def drive(self, miles: int):\n        self.odometer += miles\n        print(f'{self.brand} {self.model} drove {miles} miles. Odometer: {self.odometer}')\n\ncar1 = Car('Tesla', 'Model 3', 2024)\ncar2 = Car('Toyota', 'Corolla', 2022)\ncar1.drive(50)\ncar2.drive(12)"
            },
            {
                "title": "Class Attributes vs Instance Attributes",
                "code": "class Employee:\n    # Class attribute (shared by all instances)\n    company_name = 'Hunar Technologies'\n    \n    def __init__(self, name: str, salary: float):\n        # Instance attributes (unique to each employee)\n        self.name = name\n        self.salary = salary\n\ne1 = Employee('Bilal', 85000)\ne2 = Employee('Sara', 92000)\nprint(e1.name, 'works at', Employee.company_name)"
            },
            {
                "title": "Instance Methods Modifying State",
                "code": "class BankAccount:\n    def __init__(self, owner: str, balance: float = 0.0):\n        self.owner = owner\n        self.balance = balance\n    \n    def deposit(self, amount: float):\n        self.balance += amount\n        return self.balance\n\nacc = BankAccount('Dua', 100)\nprint('New balance after deposit:', acc.deposit(50))"
            },
            {
                "title": "Inspecting Objects with isinstance() and type()",
                "code": "print('Is car1 a Car?', isinstance(car1, Car))\nprint('Type of car1:', type(car1).__name__)"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Create a Smartphone Class",
            description="Create a class `Smartphone` with `brand`, `model`, and `battery_level` (default 100). Add a method `use_app(cost)` that subtracts `cost` from `battery_level`. Test by using an app costing 15% battery and print: 'Remaining Battery: 85%'.",
            starter_code="# TODO: Implement Smartphone class\n",
            solution_code="class Smartphone:\n    def __init__(self, brand, model, battery_level=100):\n        self.brand = brand\n        self.model = model\n        self.battery_level = battery_level\n    def use_app(self, cost):\n        self.battery_level = max(0, self.battery_level - cost)\n\nphone = Smartphone('Apple', 'iPhone 15')\nphone.use_app(15)\nprint(f'Remaining Battery: {phone.battery_level}%')",
            expected_output="Remaining Battery: 85%"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the role of the self parameter in Python class methods?",
                options=[
                    "It refers to the current instance of the class upon which the method is called.",
                    "It is a pointer to the Python interpreter.",
                    "It declares a static method.",
                    "It is optional and can be omitted in method definitions."
                ],
                correct_answer="It refers to the current instance of the class upon which the method is called.",
                explanation="`self` binds instance methods to the concrete object instance calling them."
            ),
            QuizQuestionBlueprint(
                question="What is the purpose of the __init__ method in a Python class?",
                options=[
                    "To initialize newly created instance attributes when an object is instantiated.",
                    "To allocate memory from the C heap.",
                    "To destroy an object when deleted.",
                    "To convert the class into a string."
                ],
                correct_answer="To initialize newly created instance attributes when an object is instantiated.",
                explanation="`__init__` is the instance initializer constructor called immediately after object creation."
            ),
            QuizQuestionBlueprint(
                question="What is the difference between a class attribute and an instance attribute?",
                options=[
                    "Class attributes are shared across all instances; instance attributes are unique to each object.",
                    "Class attributes can only be integers; instance attributes can be any type.",
                    "Instance attributes are defined outside methods; class attributes are in __init__.",
                    "There is no difference."
                ],
                correct_answer="Class attributes are shared across all instances; instance attributes are unique to each object.",
                explanation="Class attributes live on the class object; instance attributes live on individual object instances."
            ),
            QuizQuestionBlueprint(
                question="How do you instantiate an object of a class named Hero?",
                options=["my_hero = Hero()", "my_hero = new Hero()", "my_hero = create Hero", "my_hero = Hero.new()"],
                correct_answer="my_hero = Hero()",
                explanation="In Python, objects are instantiated by calling the class name as a function: `Hero()`."
            ),
            QuizQuestionBlueprint(
                question="Can a Python class have multiple instances active at the same time in memory?",
                options=[
                    "Yes, you can create as many unique instances as system memory permits.",
                    "No, only one instance per class (singleton) is allowed.",
                    "Only up to 10 instances.",
                    "Only if using threads."
                ],
                correct_answer="Yes, you can create as many unique instances as system memory permits.",
                explanation="Classes are templates; you can spawn unlimited distinct object instances from them."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 30 - PROJECT DAY 5
    # -------------------------------------------------------------
    DayBlueprint(
        order=30,
        title="Day 30: [PROJECT 5] Complete OOP Banking & ATM Simulation System",
        concept="Architecting a modular, enterprise-grade banking system with classes, transactions, and security checks",
        analogy="You are building the software core of a national bank! Vault doors, tellers, customer bank accounts, transaction ledger books, and ATM terminals all communicate via clean, structured OOP methods.",
        is_project_day=True,
        project_name="Complete OOP Banking & ATM Simulation System",
        theory_sections=[
            {
                "heading": "System Architecture & Domain Classes",
                "body": "In this major milestone project, we implement an Object-Oriented Banking Engine featuring:\n1. `BankAccount`: Represents an individual account with `account_number`, `holder_name`, `pin`, `balance`, and `transaction_history`.\n2. `Bank`: Manages account registries, account creation, lookup, and cross-account funds transfers.\n3. `ATM`: Provides a secure user interface layer requiring PIN authentication before executing operations."
            },
            {
                "heading": "Security & Transaction Integrity",
                "body": "Every transaction records a timestamped receipt entry in `transaction_history`. Unauthorized access is blocked by verifying PIN hashes before disclosing balances or approving withdrawals."
            }
        ],
        code_snippets=[
            {
                "title": "The BankAccount Class with PIN Protection",
                "code": "class BankAccount:\n    def __init__(self, acc_num: str, holder: str, pin: str, initial_balance: float = 0.0):\n        self.acc_num = acc_num\n        self.holder = holder\n        self._pin = pin # Protected attribute convention\n        self._balance = initial_balance\n        self.history = [f'Account opened with initial deposit: ${initial_balance:.2f}']\n    \n    def verify_pin(self, pin: str) -> bool:\n        return self._pin == pin\n        \n    def get_balance(self, pin: str):\n        if not self.verify_pin(pin):\n            return '🚨 Access Denied: Incorrect PIN.'\n        return self._balance\n        \n    def deposit(self, amount: float):\n        if amount <= 0:\n            return 'Invalid deposit amount.'\n        self._balance += amount\n        self.history.append(f'Deposited: +${amount:.2f}')\n        return f'Deposited ${amount:.2f}. New Balance: ${self._balance:.2f}'\n        \n    def withdraw(self, amount: float, pin: str):\n        if not self.verify_pin(pin):\n            return '🚨 Access Denied: Incorrect PIN.'\n        if amount > self._balance:\n            return '❌ Transaction Denied: Insufficient Funds.'\n        self._balance -= amount\n        self.history.append(f'Withdrew: -${amount:.2f}')\n        return f'Withdrew ${amount:.2f}. Remaining Balance: ${self._balance:.2f}'"
            },
            {
                "title": "The Bank Management & Transfer Class",
                "code": "class Bank:\n    def __init__(self, name: str):\n        self.name = name\n        self.accounts = {}\n        \n    def open_account(self, acc_num: str, holder: str, pin: str, deposit: float):\n        if acc_num in self.accounts:\n            return 'Account number already exists.'\n        acc = BankAccount(acc_num, holder, pin, deposit)\n        self.accounts[acc_num] = acc\n        return f'Account {acc_num} opened for {holder}.'\n        \n    def transfer(self, from_acc: str, to_acc: str, amount: float, pin: str):\n        if from_acc not in self.accounts or to_acc not in self.accounts:\n            return 'One or both account numbers not found.'\n        sender = self.accounts[from_acc]\n        receiver = self.accounts[to_acc]\n        \n        # Execute debit\n        withdraw_res = sender.withdraw(amount, pin)\n        if 'Withdrew' not in withdraw_res:\n            return f'Transfer failed: {withdraw_res}'\n        # Execute credit\n        receiver.deposit(amount)\n        return f'✅ Successfully transferred ${amount:.2f} from {from_acc} to {to_acc}.'"
            },
            {
                "title": "Complete ATM Simulation Workflow",
                "code": "# Setup Bank and Accounts\nhunar_bank = Bank('Hunar Global Bank')\nhunar_bank.open_account('PK001', 'Hamza Khan', pin='1234', deposit=500.0)\nhunar_bank.open_account('PK002', 'Ayesha Malik', pin='5678', deposit=200.0)\n\n# Test operations\nprint(hunar_bank.transfer('PK001', 'PK002', amount=150.0, pin='1234'))\n\n# Verify sender balance\nsender = hunar_bank.accounts['PK001']\nprint('Hamza Balance:', sender.get_balance('1234'))\nprint('Transaction History:', sender.history)"
            },
            {
                "title": "Security Guard Check",
                "code": "# Wrong PIN demonstration\nprint('Tampering attempt:', sender.get_balance('9999'))"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Implement Account Interest Calculation Method",
            description="Add an `apply_interest(rate)` method to a bank account that adds `balance * rate` to `_balance`. If balance is 1000 and rate is 0.05 (5%), print: 'Balance after interest: $1050.00'.",
            starter_code="balance = 1000.0\nrate = 0.05\n# TODO: Calculate interest and print\n",
            solution_code="balance = 1000.0\nrate = 0.05\nbalance += balance * rate\nprint(f'Balance after interest: ${balance:.2f}')",
            expected_output="Balance after interest: $1050.00"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Why is it standard in Python OOP to prefix private-like attributes with an underscore (e.g. _pin, _balance)?",
                options=[
                    "It signals to developers that this attribute is internal and should not be accessed or modified directly outside the class.",
                    "It physically encrypts the memory slot.",
                    "It is required by the compiler for floating numbers.",
                    "It turns the attribute into a class attribute."
                ],
                correct_answer="It signals to developers that this attribute is internal and should not be accessed or modified directly outside the class.",
                explanation="The leading underscore is PEP 8's convention for non-public API attributes."
            ),
            QuizQuestionBlueprint(
                question="How does our Bank class link accounts for fund transfers?",
                options=[
                    "By storing BankAccount objects mapped to their unique account number in a dictionary.",
                    "By using external CSV files.",
                    "By running a raw SQL query on every method.",
                    "By global variables."
                ],
                correct_answer="By storing BankAccount objects mapped to their unique account number in a dictionary.",
                explanation="The `accounts` dictionary provides fast, clean O(1) lookup of accounts by ID."
            ),
            QuizQuestionBlueprint(
                question="What ensures atomicity in the fund transfer method?",
                options=[
                    "Checking that the withdrawal from sender succeeded before depositing into the receiver.",
                    "Running both transactions asynchronously in parallel.",
                    "Ignoring errors during withdrawal.",
                    "Restarting the computer if an error occurs."
                ],
                correct_answer="Checking that the withdrawal from sender succeeded before depositing into the receiver.",
                explanation="Validating the withdrawal result before depositing ensures money is not created out of thin air if debit fails."
            ),
            QuizQuestionBlueprint(
                question="What design principle does hiding internal data behind methods like verify_pin() illustrate?",
                options=["Encapsulation", "Polymorphism", "Recursion", "Dynamic Typing"],
                correct_answer="Encapsulation",
                explanation="Encapsulation bundles data with the methods that operate on that data and restricts direct external access."
            ),
            QuizQuestionBlueprint(
                question="Can a BankAccount object be placed inside a list of accounts?",
                options=[
                    "Yes, Python objects are first-class citizens and can be stored in any collection.",
                    "No, custom classes cannot be stored in lists.",
                    "Only if the class inherits from list.",
                    "Only after serializing to XML."
                ],
                correct_answer="Yes, Python objects are first-class citizens and can be stored in any collection.",
                explanation="Python objects can be stored in lists, dicts, sets, or passed as arguments freely."
            )
        ]
    )
]
