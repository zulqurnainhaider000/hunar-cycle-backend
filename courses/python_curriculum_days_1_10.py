"""
Days 1 to 10 of Python Mastery (35 Days)
Includes Day 6 Project: Interactive Terminal Calculator
"""

from seeder.course_blueprint import DayBlueprint, QuizQuestionBlueprint, CodingChallengeBlueprint

DAYS_1_TO_10 = [
    # -------------------------------------------------------------
    # DAY 1
    # -------------------------------------------------------------
    DayBlueprint(
        order=1,
        title="Day 1: Introduction to Python & Interpreter Mechanics",
        concept="How Python interprets human-readable instructions line-by-line",
        analogy="Think of Python as a multilingual chef. Instead of translating the entire 500-page recipe book into French before starting (like compiled languages C++ or Go do), Python reads each recipe line by line and prepares the dish immediately.",
        theory_sections=[
            {
                "heading": "What is Python and How Does it Run?",
                "body": "Python was created by Guido van Rossum and released in 1991. It is known as a **high-level interpreted language**. High-level means the syntax looks very close to standard English sentences, making it natural to read and write. Interpreted means you do not run a separate compiler step before running your code. The Python interpreter reads your program from top to bottom, statement by statement."
            },
            {
                "heading": "The print() Function & Standard Output",
                "body": "Your primary window into what Python is doing inside the computer is the standard output console. The built-in `print()` function takes any data you give it inside parentheses and displays it on your screen. You can pass text enclosed in quotes (strings), numbers, or calculations."
            }
        ],
        code_snippets=[
            {
                "title": "Your Very First Program",
                "code": "print('Hello, World!')\nprint('Welcome to the 35-Day Python Mastery Course!')"
            },
            {
                "title": "Printing Multiple Arguments with Separators",
                "code": "# Python can print multiple items separated by commas\nprint('Python', 'is', 'awesome', sep='-')\nprint('Line 1', end=' | ')\nprint('Line 2')"
            },
            {
                "title": "Immediate Arithmetic Evaluation in print",
                "code": "# Python computes the expression inside parentheses first\nprint('5 + 7 =', 5 + 7)\nprint('10 * 3 =', 10 * 3)"
            },
            {
                "title": "Multi-Line Text and Comments",
                "code": "# This is a single line comment\nprint('''\n==============================\n      HUNAR CYCLE CODING      \n==============================\n''')"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Create Your Developer Business Card",
            description="Write a Python script that prints your name, role, favorite language, and prints the result of multiplying 365 by 24 (the hours in a year).",
            starter_code="# Print your developer card below\nname = 'Alex'\nrole = 'Junior Engineer'\n# TODO: Print card with separators\n",
            solution_code="print('=== DEV CARD ===')\nprint('Name: Alex')\nprint('Role: Junior Engineer')\nprint('Language: Python')\nprint('Hours in a Year:', 365 * 24)\nprint('================')",
            expected_output="=== DEV CARD ===\nName: Alex\nRole: Junior Engineer\nLanguage: Python\nHours in a Year: 8760\n================"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What does it mean that Python is an 'interpreted' programming language?",
                options=[
                    "It translates and executes instructions line-by-line at runtime.",
                    "It translates all code directly into raw assembly before launching.",
                    "It can only run inside a web browser.",
                    "It requires manual memory allocation for every variable."
                ],
                correct_answer="It translates and executes instructions line-by-line at runtime.",
                explanation="Interpreters execute code line-by-line without an upfront compilation step."
            ),
            QuizQuestionBlueprint(
                question="Which built-in Python function writes output directly to the terminal screen?",
                options=["print()", "write()", "console.log()", "display()"],
                correct_answer="print()",
                explanation="`print()` is Python's standard function to send text or values to stdout."
            ),
            QuizQuestionBlueprint(
                question="What character is used to create a single-line comment in Python?",
                options=["#", "//", "/*", "--"],
                correct_answer="#",
                explanation="In Python, lines starting with # are treated as comments and ignored by the interpreter."
            ),
            QuizQuestionBlueprint(
                question="What is the output of print('A', 'B', sep=':')?",
                options=["A:B", "A B", "AB", "':A:B:'"],
                correct_answer="A:B",
                explanation="The `sep` parameter specifies the delimiter between printed arguments."
            ),
            QuizQuestionBlueprint(
                question="Who was the original designer and creator of Python?",
                options=["Guido van Rossum", "Dennis Ritchie", "Bjarne Stroustrup", "James Gosling"],
                correct_answer="Guido van Rossum",
                explanation="Guido van Rossum released Python in 1991 as a successor to the ABC language."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 2
    # -------------------------------------------------------------
    DayBlueprint(
        order=2,
        title="Day 2: Variables, Naming Rules & Memory Pointers",
        concept="How Python stores data in memory and points labels to values",
        analogy="Think of a variable like a sticky label or name tag. In Python, the value (like the number 42) lives in a box in memory, and your variable name is just a sticky tag attached to that box. You can peel off the tag and stick it onto another box anytime!",
        theory_sections=[
            {
                "heading": "Variables as Name Tags (Pointers)",
                "body": "In low-level languages like C, a variable is a reserved memory slot with a fixed type. In Python, variables are **dynamic pointers**. When you write `age = 20`, Python creates an integer object `20` in memory, and the variable `age` points to it. If you later reassign `age = 'twenty'`, `age` simply points to a new string object."
            },
            {
                "heading": "Variable Naming Rules & PEP 8",
                "body": "Python has strict naming rules:\n1. Variable names must start with a letter (a-z, A-Z) or an underscore (`_`).\n2. They cannot start with a number.\n3. They can only contain alphanumeric characters and underscores (`a-z`, `0-9`, `_`).\n4. Names are case-sensitive (`Score` and `score` are two different variables).\n5. The official style guide (PEP 8) recommends `snake_case` for variable names (e.g. `user_balance`)."
            }
        ],
        code_snippets=[
            {
                "title": "Declaring and Reassigning Variables",
                "code": "player_name = 'Geralt'\nplayer_health = 100\nprint('Player:', player_name)\nprint('Health:', player_health)"
            },
            {
                "title": "Dynamic Reassignment",
                "code": "status = 'Active'\nprint('Initial status:', status)\nstatus = 404  # Reassigned to an integer without error!\nprint('Updated status:', status)"
            },
            {
                "title": "Multiple Assignment in a Single Line",
                "code": "x, y, z = 10, 20, 30\nprint('x:', x, 'y:', y, 'z:', z)\na = b = c = 100\nprint('All same:', a, b, c)"
            },
            {
                "title": "Variable Swapping Without a Temp Variable",
                "code": "# Python allows elegant tuple unpacking to swap values\nfirst = 'Alice'\nsecond = 'Bob'\nfirst, second = second, first\nprint('First:', first, '| Second:', second)"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Swap and Update Player Inventories",
            description="Create two variables `hero_weapon` and `boss_weapon`. Swap their weapons using Python's tuple assignment, and print the results.",
            starter_code="hero_weapon = 'Wooden Sword'\nboss_weapon = 'Dragon Slayer Blade'\n# TODO: Swap weapons in one line and print both\n",
            solution_code="hero_weapon = 'Wooden Sword'\nboss_weapon = 'Dragon Slayer Blade'\nhero_weapon, boss_weapon = boss_weapon, hero_weapon\nprint('Hero has:', hero_weapon)\nprint('Boss has:', boss_weapon)",
            expected_output="Hero has: Dragon Slayer Blade\nBoss has: Wooden Sword"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Which of the following is an INVALID variable name in Python?",
                options=["2nd_place", "_secret_key", "total_price", "userScore"],
                correct_answer="2nd_place",
                explanation="Variable names cannot start with a digit (0-9)."
            ),
            QuizQuestionBlueprint(
                question="What style of naming is recommended by PEP 8 for Python variables?",
                options=["snake_case", "camelCase", "PascalCase", "kebab-case"],
                correct_answer="snake_case",
                explanation="PEP 8 specifies lowercase words separated by underscores (snake_case) for variable names."
            ),
            QuizQuestionBlueprint(
                question="What happens when you reassign an existing variable to a value of a different type?",
                options=[
                    "Python dynamically points the variable name to the new object.",
                    "Python throws a static TypeError.",
                    "The program terminates with a MemoryLeak exception.",
                    "Python automatically converts the new value to the old type."
                ],
                correct_answer="Python dynamically points the variable name to the new object.",
                explanation="Python is dynamically typed; variables are names bound to objects in memory."
            ),
            QuizQuestionBlueprint(
                question="What is the result of executing: a, b = 5, 10; a, b = b, a?",
                options=["a is 10, b is 5", "a is 5, b is 10", "a is 10, b is 10", "Throws a SyntaxError"],
                correct_answer="a is 10, b is 5",
                explanation="Python evaluates the right-hand tuple (b, a) first, then unpacks into a and b, effectively swapping them."
            ),
            QuizQuestionBlueprint(
                question="Are variable names in Python case-sensitive?",
                options=["Yes, age and Age are completely distinct variables", "No, Python treats all variables as lowercase", "Only when using UTF-8 characters", "Only inside class definitions"],
                correct_answer="Yes, age and Age are completely distinct variables",
                explanation="Python identifiers are strictly case-sensitive."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 3
    # -------------------------------------------------------------
    DayBlueprint(
        order=3,
        title="Day 3: Primitive Data Types & Type Casting",
        concept="The fundamental primitive types (int, float, str, bool) and explicit conversion",
        analogy="Imagine four different containers: an egg carton (integers: whole items only), a measuring jug (floats: exact amounts with decimals), a letter envelope (strings: text characters), and a light switch (booleans: on or off). Casting is pouring contents from one container format to another!",
        theory_sections=[
            {
                "heading": "The 4 Core Primitive Types",
                "body": "Python categorizes every raw value into a type:\n- **int**: Whole numbers of arbitrary precision (e.g. `10`, `-45`, `1000000`).\n- **float**: Real numbers with decimal points (e.g. `3.14159`, `-0.01`).\n- **str**: Text enclosed in single, double, or triple quotes (e.g. `'Python'`, `\"Code\"`).\n- **bool**: Logical flags which can only be `True` or `False`."
            },
            {
                "heading": "Type Inspection and Explicit Casting",
                "body": "You can inspect the type of any variable using `type(var)`. Because input from users or files always arrives as strings, you must explicitly convert (cast) types using the constructor functions: `int()`, `float()`, `str()`, and `bool()`."
            }
        ],
        code_snippets=[
            {
                "title": "Inspecting Data Types",
                "code": "age = 25\npi = 3.14159\nname = 'Hunar'\nis_student = True\nprint(type(age), type(pi), type(name), type(is_student))"
            },
            {
                "title": "String to Number Casting",
                "code": "price_str = '49.99'\nqty_str = '3'\n# Convert to float and int to perform arithmetic\ntotal = float(price_str) * int(qty_str)\nprint('Total cost: $', total)"
            },
            {
                "title": "Number to String Casting for Concatenation",
                "code": "score = 98\n# str(score) converts 98 to '98'\nmessage = 'Your final score is: ' + str(score) + '/100'\nprint(message)"
            },
            {
                "title": "Boolean Truthiness & Casting",
                "code": "# In Python, 0, empty strings, and None are Falsy; everything else is Truthy\nprint('bool(0):', bool(0))\nprint('bool(1):', bool(1))\nprint('bool(\"\"):', bool(''))\nprint('bool(\"Hello\"):', bool('Hello'))"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Convert and Calculate Cart Totals",
            description="Given two string variables `item_price = '19.50'` and `item_tax = '1.75'`, cast them into floats, calculate the total price, and print: 'Final Total: 21.25'.",
            starter_code="item_price = '19.50'\nitem_tax = '1.75'\n# TODO: Cast and calculate total\n",
            solution_code="item_price = '19.50'\nitem_tax = '1.75'\ntotal = float(item_price) + float(item_tax)\nprint('Final Total:', total)",
            expected_output="Final Total: 21.25"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Which function is used to determine the data type of an object in Python?",
                options=["type()", "typeof()", "datatype()", "isinstance_type()"],
                correct_answer="type()",
                explanation="`type()` returns the class/type of the passed object."
            ),
            QuizQuestionBlueprint(
                question="What happens if you execute: 'Score: ' + 100 without casting?",
                options=[
                    "Python raises a TypeError (cannot concatenate str and int).",
                    "Python automatically converts 100 to string 'Score: 100'.",
                    "Python evaluates the string as ASCII numbers.",
                    "It returns None."
                ],
                correct_answer="Python raises a TypeError (cannot concatenate str and int).",
                explanation="Python does not perform implicit string-integer coercion with the + operator."
            ),
            QuizQuestionBlueprint(
                question="What will bool('') evaluate to?",
                options=["False", "True", "None", "Raises ValueError"],
                correct_answer="False",
                explanation="An empty string has zero length and is considered falsy in Python."
            ),
            QuizQuestionBlueprint(
                question="What is the result of int(7.89)?",
                options=["7", "8", "7.0", "Raises a TypeError"],
                correct_answer="7",
                explanation="Casting a float to an int truncates the decimal part towards zero."
            ),
            QuizQuestionBlueprint(
                question="Which of the following values is an instance of float?",
                options=["5.0", "'5.0'", "5", "True"],
                correct_answer="5.0",
                explanation="5.0 contains a decimal point, classifying it as a float object."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 4
    # -------------------------------------------------------------
    DayBlueprint(
        order=4,
        title="Day 4: Arithmetic, Floor Division & Modulo Operators",
        concept="Mathematical computations, integer division vs float division, and remainders",
        analogy="Imagine dividing 14 candies among 4 children. Float division (`14 / 4`) gives 3.5 candies each. Floor division (`14 // 4`) gives each child 3 whole candies. Modulo (`14 % 4`) gives the 2 leftover candies sitting in the bowl!",
        theory_sections=[
            {
                "heading": "Standard vs Floor Division",
                "body": "Python features two division operators:\n- True division (`/`): Always produces a `float`, even if the numbers divide evenly (e.g. `10 / 2` yields `5.0`).\n- Floor division (`//`): Divides and rounds down to the nearest integer towards negative infinity (e.g. `10 // 3` yields `3`)."
            },
            {
                "heading": "The Power of the Modulo Operator (%)",
                "body": "The modulo operator (`%`) calculates the remainder after division. It is ubiquitous in computer science for: checking even vs odd numbers (`n % 2 == 0`), cyclic rotations (clock arithmetic `hour % 12`), and pagination algorithms."
            }
        ],
        code_snippets=[
            {
                "title": "All 7 Arithmetic Operators in Action",
                "code": "a, b = 17, 5\nprint('Addition (+):', a + b)\nprint('Subtraction (-):', a - b)\nprint('Multiplication (*):', a * b)\nprint('True Division (/):', a / b)\nprint('Floor Division (//):', a // b)\nprint('Modulo (%):', a % b)\nprint('Exponentiation (**):', a ** b)"
            },
            {
                "title": "Even / Odd Number Checking with Modulo",
                "code": "num = 42\nis_even = (num % 2 == 0)\nprint('Is', num, 'even?', is_even)\n\nodd_num = 17\nprint('Is', odd_num, 'even?', (odd_num % 2 == 0))"
            },
            {
                "title": "Time Calculation: Seconds to Minutes and Remaining Seconds",
                "code": "total_seconds = 325\nminutes = total_seconds // 60\nseconds = total_seconds % 60\nprint('Time formatted:', minutes, 'minutes and', seconds, 'seconds')"
            },
            {
                "title": "Augmented Assignment Operators",
                "code": "balance = 100\nbalance += 50   # balance = balance + 50\nbalance -= 20   # balance = balance - 20\nbalance *= 2    # balance = balance * 2\nprint('Final Balance:', balance)"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Convert Total Pennies to Coins",
            description="Write a script that takes `total_cents = 87`. Calculate how many quarters (25 cents) you get, and how many cents remain using floor division and modulo. Print: 'Quarters: 3, Leftover: 12 cents'.",
            starter_code="total_cents = 87\n# TODO: Calculate quarters and leftovers\n",
            solution_code="total_cents = 87\nquarters = total_cents // 25\nleftover = total_cents % 25\nprint('Quarters:', quarters, ', Leftover:', leftover, 'cents')",
            expected_output="Quarters: 3 , Leftover: 12 cents"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the result and type of 10 / 2 in Python 3?",
                options=["5.0 (float)", "5 (int)", "5.5 (float)", "Throws ZeroDivisionError"],
                correct_answer="5.0 (float)",
                explanation="In Python 3, the single slash division operator `/` always produces a float."
            ),
            QuizQuestionBlueprint(
                question="What is the value of 19 // 4?",
                options=["4", "4.75", "5", "3"],
                correct_answer="4",
                explanation="Floor division `//` rounds down to the nearest whole integer (19 // 4 = 4)."
            ),
            QuizQuestionBlueprint(
                question="What is the output of 20 % 6?",
                options=["2", "3", "3.33", "0"],
                correct_answer="2",
                explanation="20 divided by 6 is 3 with a remainder of 2 (6 * 3 + 2 = 20)."
            ),
            QuizQuestionBlueprint(
                question="Which operator is used to raise a number to a power in Python?",
                options=["**", "^", "^^", "exp()"],
                correct_answer="**",
                explanation="`**` is Python's exponentiation operator (e.g. 2 ** 3 = 8). Note that `^` is bitwise XOR."
            ),
            QuizQuestionBlueprint(
                question="If count = 10, what does count += 5 do?",
                options=[
                    "Increments count by 5 to become 15",
                    "Checks if count equals 15",
                    "Raises a SyntaxError",
                    "Creates a tuple with 10 and 5"
                ],
                correct_answer="Increments count by 5 to become 15",
                explanation="`count += 5` is shorthand for `count = count + 5`."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 5
    # -------------------------------------------------------------
    DayBlueprint(
        order=5,
        title="Day 5: Strings, Escape Sequences & Modern F-Strings",
        concept="Text representation, special escape characters, and formatted string literals",
        analogy="Imagine an F-string like a birthday card with blank cutouts. Instead of writing separate notes and gluing them together with scissors (+), you just slide the photos of your friends directly into the precut slots (`{friend_name}`) inside the card!",
        theory_sections=[
            {
                "heading": "Strings and Escape Characters",
                "body": "Strings are sequences of characters. If you need special characters like newlines or tabs inside text, use backslash escape sequences:\n- `\\n`: Newline (moves to next line)\n- `\\t`: Tab indent\n- `\\\"` or `\\'`: Literal quotes inside quotation marks\n- `\\\\`: Literal backslash"
            },
            {
                "heading": "Formatted String Literals (F-Strings)",
                "body": "Introduced in Python 3.6, **f-strings** are the cleanest, most performant way to format strings. By prefixing a string with `f` (e.g. `f\"Hello {name}\"`), Python evaluates any Python expression inside `{}` placeholders at runtime. You can even format float precision: `{price:.2f}`."
            }
        ],
        code_snippets=[
            {
                "title": "Escape Sequences in Output",
                "code": "text = 'Title:\\tPython Mastery\\nAuthor:\\tGuido\\nQuote:\\t\"Simple is better than complex.\"'\nprint(text)"
            },
            {
                "title": "Modern F-Strings with Variables",
                "code": "username = 'Sora'\nlevel = 42\nxp = 95.847\nprint(f'User: {username} | Level: {level} | XP: {xp:.1f}%')"
            },
            {
                "title": "Inline Expressions Inside F-Strings",
                "code": "item = 'Laptop'\nprice = 1200\ndiscount = 0.15\nprint(f'{item} on sale: ${price * (1 - discount):.2f}')"
            },
            {
                "title": "F-String Self-Documenting Debugging (Python 3.8+)",
                "code": "width = 1920\nheight = 1080\n# Adding = prints variable name and its value automatically\nprint(f'{width=}, {height=}')"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Generate a Clean Receipt Invoice Line",
            description="Given `product = 'Espresso'`, `qty = 2`, and `unit_price = 3.5`. Use an f-string to print: 'Item: Espresso | Qty: 2 | Total: $7.00'.",
            starter_code="product = 'Espresso'\nqty = 2\nunit_price = 3.5\n# TODO: Print receipt using an f-string\n",
            solution_code="product = 'Espresso'\nqty = 2\nunit_price = 3.5\ntotal = qty * unit_price\nprint(f'Item: {product} | Qty: {qty} | Total: ${total:.2f}')",
            expected_output="Item: Espresso | Qty: 2 | Total: $7.00"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="How do you declare an f-string in Python?",
                options=[
                    "Prefix the string quote with the letter 'f' or 'F' (e.g. f\"Hello {name}\")",
                    "Wrap the string in curly braces {string}",
                    "End the string with .format()",
                    "Add @ before the string quote"
                ],
                correct_answer="Prefix the string quote with the letter 'f' or 'F' (e.g. f\"Hello {name}\")",
                explanation="Prefixing with 'f' denotes a formatted string literal."
            ),
            QuizQuestionBlueprint(
                question="What escape character represents a newline in Python?",
                options=["\\n", "\\t", "\\r", "\\b"],
                correct_answer="\\n",
                explanation="`\\n` inserts an ASCII linefeed (newline) character."
            ),
            QuizQuestionBlueprint(
                question="What does the format specifier {val:.2f} do inside an f-string?",
                options=[
                    "Rounds and formats the number as a float with exactly 2 decimal places",
                    "Multiplies the number by 2",
                    "Converts the float to base-2 binary",
                    "Pads the string with 2 spaces"
                ],
                correct_answer="Rounds and formats the number as a float with exactly 2 decimal places",
                explanation="`:.2f` specifies a fixed-point floating point format with 2 digits after the decimal."
            ),
            QuizQuestionBlueprint(
                question="What will print(f'{2 + 3 * 4}') output?",
                options=["14", "20", "2 + 3 * 4", "'{14}'"],
                correct_answer="14",
                explanation="Python evaluates the mathematical expression inside `{}` following PEMDAS (3*4=12 + 2=14)."
            ),
            QuizQuestionBlueprint(
                question="How do you print a literal curly brace '{' inside an f-string?",
                options=["Double it: '{{'", "Escape with backslash: '\\{'", "Use unicode: '&lbrace;'", "It is not possible"],
                correct_answer="Double it: '{{'",
                explanation="In f-strings, double curly braces `{{` and `}}` are escaped into literal braces."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 6 - PROJECT DAY 1
    # -------------------------------------------------------------
    DayBlueprint(
        order=6,
        title="Day 6: [PROJECT 1] Interactive Terminal Calculator",
        concept="Synthesizing arithmetic, input parsing, type casting, and formatted results into a complete tool",
        analogy="You are now a watchmaker assembling your first real mechanical pocket watch! Every gear we studied—variables, data types, arithmetic, and formatted string outputs—now fits together into a functioning device.",
        is_project_day=True,
        project_name="Interactive Terminal Calculator",
        theory_sections=[
            {
                "heading": "Project Specifications & Architecture",
                "body": "In this first milestone project, we will construct a production-ready Terminal Calculator. The project requires:\n1. Prompting the user for two numerical inputs.\n2. Casting the string inputs into floating point numbers safely.\n3. Prompting for an arithmetic operation (`+`, `-`, `*`, `/`, `//`, `%`, `**`).\n4. Computing the calculation and displaying a clean receipt using f-strings with 2-decimal precision.\n5. Handling the classic zero-division edge case gracefully."
            },
            {
                "heading": "Step-by-Step Logic Breakdown",
                "body": "Step 1: Welcome Banner & Menu.\nStep 2: Collect operands `num1` and `num2`.\nStep 3: Validate operation and evaluate result.\nStep 4: Format and present the final output badge."
            }
        ],
        code_snippets=[
            {
                "title": "Calculator Engine Logic Function",
                "code": "def calculate(num1: float, num2: float, op: str):\n    if op == '+':\n        return num1 + num2\n    elif op == '-':\n        return num1 - num2\n    elif op == '*':\n        return num1 * num2\n    elif op == '/':\n        return 'Error: Division by zero!' if num2 == 0 else num1 / num2\n    elif op == '//':\n        return 'Error: Division by zero!' if num2 == 0 else num1 // num2\n    elif op == '%':\n        return 'Error: Division by zero!' if num2 == 0 else num1 % num2\n    elif op == '**':\n        return num1 ** num2\n    else:\n        return 'Error: Invalid operator!'"
            },
            {
                "title": "Simulated Execution & Result Formatting",
                "code": "# Demonstration with pre-configured parameters\nn1, n2, operation = 45.5, 5.0, '/'\nres = calculate(n1, n2, operation)\nif isinstance(res, (int, float)):\n    print(f'Result: {n1} {operation} {n2} = {res:.2f}')\nelse:\n    print(res)"
            },
            {
                "title": "Complete Interactive CLI Program",
                "code": "def run_calculator():\n    print('========================================')\n    print('       PYTHON TERMINAL CALCULATOR       ')\n    print('========================================')\n    # In interactive IDE: num1 = float(input('Enter first number: '))\n    # We demonstrate complete execution:\n    a = 28.0\n    b = 4.0\n    for op in ['+', '-', '*', '/', '%']:\n        outcome = calculate(a, b, op)\n        print(f'{a:>6.1f}  {op}  {b:<6.1f}  =  {outcome}')\n\nrun_calculator()"
            },
            {
                "title": "Edge Case Handling: Zero Division Guard",
                "code": "def safe_divide(numerator: float, denominator: float) -> str:\n    if denominator == 0:\n        return '🚨 Math Error: Cannot divide by zero!'\n    return f'Result: {numerator / denominator:.4f}'\n\nprint(safe_divide(100, 0))\nprint(safe_divide(100, 4))"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Implement the Exponent & Modulo Calculator Tool",
            description="Write a calculator function that computes both the power (`a ** b`) and remainder (`a % b`) of two numbers `a = 15` and `b = 4`. Print the formatted results: '15 ** 4 = 50625' and '15 % 4 = 3'.",
            starter_code="a = 15\nb = 4\n# TODO: Print power and modulo results\n",
            solution_code="a = 15\nb = 4\npow_res = a ** b\nmod_res = a % b\nprint(f'{a} ** {b} = {pow_res}')\nprint(f'{a} % {b} = {mod_res}')",
            expected_output="15 ** 4 = 50625\n15 % 4 = 3"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Why is it crucial to check if the denominator equals zero before division in Python?",
                options=[
                    "Because dividing by zero raises an unhandled ZeroDivisionError exception and crashes the script.",
                    "Because Python returns infinity (inf) automatically without errors.",
                    "Because Python converts 0 to 1 automatically.",
                    "Because modern CPUs cannot perform float math."
                ],
                correct_answer="Because dividing by zero raises an unhandled ZeroDivisionError exception and crashes the script.",
                explanation="In Python, dividing any number by 0 immediately raises ZeroDivisionError."
            ),
            QuizQuestionBlueprint(
                question="What built-in function receives raw string input typed by the user from the terminal?",
                options=["input()", "read()", "scan()", "get_line()"],
                correct_answer="input()",
                explanation="`input([prompt])` reads a line from the user console as a string."
            ),
            QuizQuestionBlueprint(
                question="If user enters '25' via input(), what is its Python data type before conversion?",
                options=["str", "int", "float", "object"],
                correct_answer="str",
                explanation="All data returned from `input()` is always of type `str`."
            ),
            QuizQuestionBlueprint(
                question="What does isinstance(res, (int, float)) verify?",
                options=[
                    "Whether res is either an integer or a floating-point number",
                    "Whether res is a tuple containing int and float",
                    "Converts res into an int or float",
                    "Checks if res is equal to zero"
                ],
                correct_answer="Whether res is either an integer or a floating-point number",
                explanation="`isinstance(val, types_tuple)` checks if `val` belongs to any of the specified classes."
            ),
            QuizQuestionBlueprint(
                question="What is the result of 2 ** 3 ** 2 evaluated using Python operator precedence?",
                options=["512", "64", "36", "18"],
                correct_answer="512",
                explanation="The exponentiation operator `**` has right-to-left associativity: 3 ** 2 = 9, then 2 ** 9 = 512."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 7
    # -------------------------------------------------------------
    DayBlueprint(
        order=7,
        title="Day 7: Conditional Logic: if, elif, else Branching",
        concept="Directing program execution flow using boolean evaluation gates",
        analogy="Think of conditional logic like railroad switch tracks. When the train arrives at a junction, the track switch checks the signal (condition). If green (`True`), the train travels down Route A. If red (`False`), it switches down Route B!",
        theory_sections=[
            {
                "heading": "The Anatomy of an if-elif-else Block",
                "body": "Programs need to make decisions. The `if` statement tests an expression that evaluates to `True` or `False`. If `True`, the indented block underneath executes. If `False`, Python skips it and checks subsequent `elif` (else if) blocks. If none match, the optional `else` block catches all remaining cases."
            },
            {
                "heading": "Python's Indentation Rule",
                "body": "Unlike languages that use curly braces `{}` to define code blocks, Python uses whitespace indentation (standard is 4 spaces). Incorrect indentation will raise an `IndentationError`."
            }
        ],
        code_snippets=[
            {
                "title": "Basic If-Else Statement",
                "code": "temperature = 32\nif temperature > 30:\n    print('It is a hot summer day! Drink water.')\nelse:\n    print('The weather is pleasant.')"
            },
            {
                "title": "Multi-Branching with elif",
                "code": "score = 85\nif score >= 90:\n    grade = 'A'\nelif score >= 80:\n    grade = 'B'\nelif score >= 70:\n    grade = 'C'\nelse:\n    grade = 'F'\nprint(f'Student Score: {score} -> Grade: {grade}')"
            },
            {
                "title": "Nested Conditionals",
                "code": "has_ticket = True\nage = 16\nif has_ticket:\n    if age >= 18:\n        print('Welcome to the adult section!')\n    else:\n        print('Welcome to the teen pavilion!')\nelse:\n    print('Please purchase a ticket at the booth.')"
            },
            {
                "title": "Conditional Ternary Expression (Inline If)",
                "code": "status_code = 200\n# [on_true] if [condition] else [on_false]\nmessage = 'Success' if status_code == 200 else 'Failure'\nprint('Response Status:', message)"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Determine Movie Ticket Pricing",
            description="Write a script with `age = 65`. If age < 12, ticket is 8. Elif age >= 65, ticket is 10. Else, ticket is 15. Print: 'Ticket Price: $10'.",
            starter_code="age = 65\n# TODO: Calculate ticket price using if/elif/else\n",
            solution_code="age = 65\nif age < 12:\n    price = 8\nelif age >= 65:\n    price = 10\nelse:\n    price = 15\nprint(f'Ticket Price: ${price}')",
            expected_output="Ticket Price: $10"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="How does Python determine which statements belong inside an if-statement block?",
                options=[
                    "By whitespace indentation level (typically 4 spaces)",
                    "By enclosing the block in curly braces { }",
                    "By ending each line with a semicolon ;",
                    "By typing the 'then' keyword"
                ],
                correct_answer="By whitespace indentation level (typically 4 spaces)",
                explanation="Python uses indentation to delimit code blocks rather than braces."
            ),
            QuizQuestionBlueprint(
                question="What keyword is used in Python for 'else if'?",
                options=["elif", "else if", "elseif", "elsif"],
                correct_answer="elif",
                explanation="Python uses the concise keyword `elif` for chained conditions."
            ),
            QuizQuestionBlueprint(
                question="What will be the output of: x = 10; print('High' if x > 15 else 'Low')?",
                options=["Low", "High", "None", "Raises SyntaxError"],
                correct_answer="Low",
                explanation="Since x > 15 is False, the ternary expression returns 'Low'."
            ),
            QuizQuestionBlueprint(
                question="Can an if-block exist without an else-block?",
                options=[
                    "Yes, the else block is completely optional.",
                    "No, every if must be paired with an else.",
                    "Only if an elif is provided.",
                    "Only inside functions."
                ],
                correct_answer="Yes, the else block is completely optional.",
                explanation="An `else` clause is optional; if omitted and condition is False, execution simply continues."
            ),
            QuizQuestionBlueprint(
                question="Which comparison operator checks for value equality in Python?",
                options=["==", "=", "===", "equals()"],
                correct_answer="==",
                explanation="`==` checks for equality of values, whereas `=` is the assignment operator."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 8
    # -------------------------------------------------------------
    DayBlueprint(
        order=8,
        title="Day 8: Logical Operators & Compound Expressions",
        concept="Combining conditions using and, or, not and short-circuit evaluation",
        analogy="Think of a bank vault door. To open it, you need key A AND key B (both must be `True`). For an office lobby door, you can use an RFID card OR a passcode (either being `True` unlocks it). The `not` operator is simply a photo negative: turning black into white and white into black!",
        theory_sections=[
            {
                "heading": "The Three Logical Operators",
                "body": "Python provides three natural English words for boolean logic:\n- `and`: Evaluates to `True` only if **both** operands are `True`.\n- `or`: Evaluates to `True` if **at least one** operand is `True`.\n- `not`: Inverts the boolean value (`not True` becomes `False`)."
            },
            {
                "heading": "Short-Circuit Evaluation",
                "body": "Python uses **short-circuit evaluation** for performance and safety:\n- In `A and B`, if `A` is `False`, Python immediately returns without evaluating `B`.\n- In `A or B`, if `A` is `True`, Python immediately returns without evaluating `B`.\nThis allows safe checks like: `if user is not None and user.is_active:` without crashing."
            }
        ],
        code_snippets=[
            {
                "title": "Combining Conditions with and / or",
                "code": "age = 22\nhas_license = True\ncan_rent_car = (age >= 21) and has_license\nprint('Eligible to rent car:', can_rent_car)"
            },
            {
                "title": "Chaining with Not and Parentheses",
                "code": "is_weekend = False\nis_holiday = True\nhave_to_work = not (is_weekend or is_holiday)\nprint('Do I have to work today?', have_to_work)"
            },
            {
                "title": "Short-Circuit Protection Demonstration",
                "code": "# If count is 0, (count != 0) is False, so Python never divides by zero!\ncount = 0\ntotal = 100\nif count != 0 and (total / count) > 10:\n    print('High average')\nelse:\n    print('Safe: Short-circuit avoided division by zero!')"
            },
            {
                "title": "Python's Chained Comparison Feature",
                "code": "score = 75\n# In Python you can chain comparisons naturally like in algebra!\nif 70 <= score <= 80:\n    print('Score is comfortably in the 70s range.')"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="VIP Club Entry Bouncer Logic",
            description="Given `age = 20`, `has_invitation = True`, and `is_banned = False`. Allow entry if `not is_banned` AND (`age >= 21` OR `has_invitation`). Print 'Access Granted' or 'Access Denied'.",
            starter_code="age = 20\nhas_invitation = True\nis_banned = False\n# TODO: Implement entry logic\n",
            solution_code="age = 20\nhas_invitation = True\nis_banned = False\nif not is_banned and (age >= 21 or has_invitation):\n    print('Access Granted')\nelse:\n    print('Access Denied')",
            expected_output="Access Granted"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the result of: True and False or True?",
                options=["True", "False", "None", "Raises SyntaxError"],
                correct_answer="True",
                explanation="`and` has higher precedence than `or`: (True and False) is False; (False or True) is True."
            ),
            QuizQuestionBlueprint(
                question="What does 'short-circuit evaluation' mean in Python?",
                options=[
                    "Evaluation stops as soon as the outcome is determined.",
                    "An electrical safety feature in the Python virtual machine.",
                    "Skipping code when an unexpected exception is raised.",
                    "Compiling conditions into bitwise registers."
                ],
                correct_answer="Evaluation stops as soon as the outcome is determined.",
                explanation="In `False and func()`, `func()` is never called because the result is guaranteed to be False."
            ),
            QuizQuestionBlueprint(
                question="What is the result of not (10 == 10)?",
                options=["False", "True", "None", "0"],
                correct_answer="False",
                explanation="10 == 10 is True. Applying `not True` evaluates to False."
            ),
            QuizQuestionBlueprint(
                question="How do you write 'x is between 1 and 10 inclusive' idiomatically in Python?",
                options=["1 <= x <= 10", "x >= 1 and <= 10", "x in range(1, 10)", "between(x, 1, 10)"],
                correct_answer="1 <= x <= 10",
                explanation="Python uniquely supports chained comparisons like `1 <= x <= 10`."
            ),
            QuizQuestionBlueprint(
                question="What will bool(None or 'Python') evaluate to?",
                options=["True", "False", "'Python'", "None"],
                correct_answer="True",
                explanation="`None` is falsy, so `None or 'Python'` evaluates to `'Python'`, and `bool('Python')` is True."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 9
    # -------------------------------------------------------------
    DayBlueprint(
        order=9,
        title="Day 9: While Loops & Sentinel-Controlled Flow",
        concept="Repeating code blocks dynamically while a condition remains True",
        analogy="Think of a while loop like running on an electric treadmill. As long as the emergency stop button has NOT been pressed (`while not stop_button:`), you keep running another stride. The moment the button is pressed, you step off the treadmill!",
        theory_sections=[
            {
                "heading": "The while Loop Mechanics",
                "body": "A `while` loop repeatedly executes its block as long as its test condition evaluates to `True`. It is ideal when you don't know in advance how many times you need to loop—such as waiting for user input, polling an API endpoint, or game loops."
            },
            {
                "heading": "Avoiding Infinite Loops",
                "body": "If the condition never becomes `False`, your program will be trapped in an **infinite loop**, freezing the CPU. You must ensure that something inside the loop modifies the loop condition variables towards termination."
            }
        ],
        code_snippets=[
            {
                "title": "Basic Countdown Counter",
                "code": "countdown = 5\nwhile countdown > 0:\n    print(f'T-minus {countdown}...')\n    countdown -= 1\nprint('🚀 Blast off!')"
            },
            {
                "title": "Sentinel-Controlled Loop Simulation",
                "code": "# Simulating user typing 'quit' to exit\ninputs = ['start', 'status', 'help', 'quit']\nidx = 0\nwhile idx < len(inputs):\n    command = inputs[idx]\n    idx += 1\n    if command == 'quit':\n        print('Exiting application. Goodbye!')\n        break\n    print(f'Processing command: {command}')"
            },
            {
                "title": "Accumulator Pattern with while",
                "code": "# Sum all numbers from 1 to 10\ntotal = 0\ncurr = 1\nwhile curr <= 10:\n    total += curr\n    curr += 1\nprint('Sum of 1 through 10 is:', total)"
            },
            {
                "title": "The while-else Clause",
                "code": "# In Python, while can have an else block that runs when loop finishes normally (without break)\nn = 3\nwhile n > 0:\n    print('Tick', n)\n    n -= 1\nelse:\n    print('Loop completed naturally without break interrupt!')"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Double the Investment Target",
            description="Given `money = 100` and `target = 800`. Use a `while` loop that doubles `money` each year (`money *= 2`) and counts the years. Print: 'Target reached in 3 years with $800'.",
            starter_code="money = 100\ntarget = 800\nyears = 0\n# TODO: Loop until money >= target\n",
            solution_code="money = 100\ntarget = 800\nyears = 0\nwhile money < target:\n    money *= 2\n    years += 1\nprint(f'Target reached in {years} years with ${money}')",
            expected_output="Target reached in 3 years with $800"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="When is a while loop preferred over a for loop?",
                options=[
                    "When the number of iterations is unknown in advance and depends on a condition.",
                    "When iterating over a fixed list of items.",
                    "Only when processing JSON strings.",
                    "When maximum compilation speed is needed."
                ],
                correct_answer="When the number of iterations is unknown in advance and depends on a condition.",
                explanation="`while` loops are condition-driven, while `for` loops are collection/sequence-driven."
            ),
            QuizQuestionBlueprint(
                question="What happens if a while loop condition never becomes False and contains no break?",
                options=[
                    "The program enters an infinite loop and will run indefinitely.",
                    "Python automatically terminates it after 1000 iterations.",
                    "A LoopOverflowError is thrown.",
                    "The operating system restarts the script."
                ],
                correct_answer="The program enters an infinite loop and will run indefinitely.",
                explanation="Without a stopping condition or break statement, an infinite loop will consume CPU until killed."
            ),
            QuizQuestionBlueprint(
                question="What keyword causes immediate termination of the innermost loop?",
                options=["break", "continue", "stop", "exit()"],
                correct_answer="break",
                explanation="`break` immediately halts the loop and jumps to the statement following the loop."
            ),
            QuizQuestionBlueprint(
                question="How many times will this loop execute: i = 5; while i < 5: i += 1?",
                options=["0 times", "1 time", "5 times", "Infinite times"],
                correct_answer="0 times",
                explanation="Because i is initialized to 5, the condition `i < 5` is False immediately, so the loop body never executes."
            ),
            QuizQuestionBlueprint(
                question="When does the `else` block of a while loop execute in Python?",
                options=[
                    "When the loop condition becomes False naturally without encountering a break statement.",
                    "Only when the while condition was never True in the first place.",
                    "Whenever an unhandled exception is caught.",
                    "Simultaneously with each iteration."
                ],
                correct_answer="When the loop condition becomes False naturally without encountering a break statement.",
                explanation="The `else` block executes when the loop condition evaluates to False, but NOT if exited via `break`."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 10
    # -------------------------------------------------------------
    DayBlueprint(
        order=10,
        title="Day 10: For Loops & The range() Generator Function",
        concept="Definite iteration over sequences, step counts, and ranges",
        analogy="Imagine an automated factory assembly line. A line of 10 toy cars moves along the conveyor belt. The robotic arm performs its paint job on Car 1, then Car 2, all the way to Car 10. That's a `for` loop: visiting every item in an orderly sequence!",
        theory_sections=[
            {
                "heading": "For Loops as Sequence Iterators",
                "body": "In Python, `for` loops are strictly designed to iterate over iterables (sequences like lists, strings, ranges, or tuples). On each iteration, the loop variable takes on the value of the next item in the sequence automatically."
            },
            {
                "heading": "The range() Built-in Function",
                "body": "`range()` generates an immutable sequence of numbers on demand without storing them all in memory. It accepts up to three arguments:\n- `range(stop)`: from 0 up to (but not including) `stop`.\n- `range(start, stop)`: from `start` up to (not including) `stop`.\n- `range(start, stop, step)`: increments by `step` (can be negative for reverse counting!)."
            }
        ],
        code_snippets=[
            {
                "title": "Basic range(start, stop)",
                "code": "# Prints numbers 1 through 5\nfor i in range(1, 6):\n    print('Step:', i)"
            },
            {
                "title": "Using the Step Parameter (Even Numbers)",
                "code": "# From 2 to 10 skipping by 2\nfor even in range(2, 11, 2):\n    print(f'{even} is an even number.')"
            },
            {
                "title": "Iterating in Reverse (Countdown)",
                "code": "# Negative step counts backwards\nfor n in range(5, 0, -1):\n    print(f'Countdown: {n}')\nprint('Lift off!')"
            },
            {
                "title": "Iterating Over String Characters with enumerate()",
                "code": "word = 'PYTHON'\nfor idx, char in enumerate(word):\n    print(f'Index {idx}: {char}')"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Calculate Factorial Using a For Loop",
            description="Given `n = 5`. Calculate `5 * 4 * 3 * 2 * 1` using a `for` loop and `range()`. Print: '5! = 120'.",
            starter_code="n = 5\nfactorial = 1\n# TODO: Calculate factorial using a for loop\n",
            solution_code="n = 5\nfactorial = 1\nfor i in range(1, n + 1):\n    factorial *= i\nprint(f'{n}! = {factorial}')",
            expected_output="5! = 120"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What numbers are generated by range(1, 5)?",
                options=["1, 2, 3, 4", "1, 2, 3, 4, 5", "0, 1, 2, 3, 4", "2, 3, 4, 5"],
                correct_answer="1, 2, 3, 4",
                explanation="In `range(start, stop)`, the stop value is exclusive."
            ),
            QuizQuestionBlueprint(
                question="How do you generate numbers from 10 down to 1 using range?",
                options=["range(10, 0, -1)", "range(10, 1, -1)", "range(1, 10, -1)", "reverse(range(10))"],
                correct_answer="range(10, 0, -1)",
                explanation="Start is 10, stop is 0 (exclusive, so stops at 1), step is -1."
            ),
            QuizQuestionBlueprint(
                question="What does the built-in enumerate() function return on each loop iteration?",
                options=[
                    "A tuple containing the current (index, item)",
                    "Only the index as an integer",
                    "A reversed view of the list",
                    "The total length of the sequence"
                ],
                correct_answer="A tuple containing the current (index, item)",
                explanation="`enumerate(iterable)` yields pairs of `(count, value)` starting from 0 by default."
            ),
            QuizQuestionBlueprint(
                question="Does range(1000000) allocate a million integers in memory all at once?",
                options=[
                    "No, range generates numbers on demand (lazy evaluation).",
                    "Yes, it creates a list of 1,000,000 integers immediately.",
                    "Only in Python 2.x.",
                    "Yes, consuming ~8MB of RAM."
                ],
                correct_answer="No, range generates numbers on demand (lazy evaluation).",
                explanation="In Python 3, `range` is an immutable sequence object that computes values lazily in O(1) memory."
            ),
            QuizQuestionBlueprint(
                question="What will be the output of: for c in 'Cat': print(c, end='-')?",
                options=["C-a-t-", "Cat-", "C-a-t", "C a t -"],
                correct_answer="C-a-t-",
                explanation="Strings are iterable character by character; `end='-'` prints hyphen after each letter."
            )
        ]
    )
]
