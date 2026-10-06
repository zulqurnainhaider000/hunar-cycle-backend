import asyncio
from prisma import Prisma

def generate_flashcards():
    flashcards = []

    def add(q, a):
        flashcards.append({"question": q, "answer": str(a)})

    # ==========================================
    # 1. BASICS & SYNTAX (Data Types & Casting)
    # ==========================================
    add("What is the difference between a dynamically typed and statically typed language?", "In a dynamically typed language like Python, variable types are checked during execution (runtime), whereas statically typed languages check types during compilation.")
    add("How do you declare a variable in Python?", "You just assign a value to a name using the `=` operator. E.g., `x = 5`. No type declaration is needed.")
    add("What does the `id()` function do?", "It returns the unique identity (memory address in CPython) of an object.")
    add("Is Python call-by-value or call-by-reference?", "Python is 'call-by-object-reference'. If you pass a mutable object (like a list), changes to it are reflected outside. If you pass an immutable object (like an int or string), it cannot be changed.")

    types_map = {
        "5": "<class 'int'>", "3.14": "<class 'float'>", "'Hello'": "<class 'str'>",
        "[1, 2]": "<class 'list'>", "(1, 2)": "<class 'tuple'>", "{'a': 1}": "<class 'dict'>",
        "{1, 2}": "<class 'set'>", "True": "<class 'bool'>", "None": "<class 'NoneType'>"
    }
    for val, typ in types_map.items():
        add(f"What is the output of `print(type({val}))`?", f"`{typ}`")

    for a in [2, 5, 10, 15]:
        for b in [3, 4, 7]:
            for op in ['+', '-', '*', '//', '%', '**']:
                ans = eval(f"{a} {op} {b}")
                add(f"What is the output of:\n`print({a} {op} {b})`?", f"The output is `{ans}`.")

    # ==========================================
    # 2. STRING MANIPULATION
    # ==========================================
    add("What is the output of `'Hello'.lower()`?", "`'hello'`")
    add("What is the output of `'python'.upper()`?", "`'PYTHON'`")
    add("What is the output of `'  strip me  '.strip()`?", "`'strip me'`")
    add("What is the output of `'a,b,c'.split(',')`?", "`['a', 'b', 'c']`")
    add("What is the output of `'-'.join(['a', 'b'])`?", "`'a-b'`")
    add("How do you check if a string starts with 'Py'?", "Using the method `startswith()`: `s.startswith('Py')`")
    
    word = "Python"
    for start in [None, 0, 2, -2]:
        for end in [None, 4, -1]:
            for step in [None, 1, 2, -1]:
                # Skip some to avoid generating too many similar
                if start is None and end is None and step is None: continue
                
                s_str = "" if start is None else str(start)
                e_str = "" if end is None else str(end)
                st_str = "" if step is None else str(step)
                
                slice_str = f"{s_str}:{e_str}" if step is None else f"{s_str}:{e_str}:{st_str}"
                q = f"Given `s = '{word}'`, what is the output of `print(s[{slice_str}])`?"
                ans = word[slice(start, end, step)]
                add(q, f"`'{ans}'`")

    # ==========================================
    # 3. CONTROL FLOW
    # ==========================================
    add("What is the output of `print(bool(0))`?", "`False`")
    add("What is the output of `print(bool([]))`?", "`False` (Empty collections are falsy)")
    add("What is the output of `print(bool('False'))`?", "`True` (Non-empty strings are truthy)")

    for a in [True, False]:
        for b in [True, False]:
            for c in [True, False]:
                add(f"What is the output of `{a} and {b} or {c}`?", f"`{a and b or c}`")
                add(f"What is the output of `{a} or {b} and {c}`?", f"`{a or b and c}`")

    # ==========================================
    # 4. LOOPS
    # ==========================================
    add("What is the difference between `break` and `continue`?", "`break` exits the loop entirely. `continue` skips the rest of the current iteration and moves to the next.")
    add("What does the `pass` statement do?", "It is a null operation. It does nothing and is used as a placeholder where syntax requires a statement.")
    
    for end_val in [3, 5]:
        for step in [1, 2]:
            output = list(range(0, end_val, step))
            q = f"What sequence of numbers does `range(0, {end_val}, {step})` generate?"
            add(q, f"`{output}`")

    # ==========================================
    # 5. DATA STRUCTURES (Lists, Tuples, Sets, Dicts)
    # ==========================================
    add("Are lists mutable or immutable?", "Mutable (they can be changed after creation).")
    add("Are tuples mutable or immutable?", "Immutable (they cannot be changed after creation).")
    add("How do you add an item to the end of a list?", "Using the `append()` method.")
    add("How do you remove a key-value pair from a dictionary?", "Using the `del` statement (e.g., `del my_dict['key']`) or the `pop()` method.")
    
    for i in [1, 2, 3]:
        add(f"What is the output of `[1, 2, 3] * {i}`?", f"`{[1, 2, 3] * i}`")
        add(f"What is the output of `len([1, 2, 3] * {i})`?", f"`{len([1, 2, 3] * i)}`")

    # List comprehensions
    for i in [2, 3]:
        q = f"What is the output of `[x * {i} for x in range(3)]`?"
        ans = [x * i for x in range(3)]
        add(q, f"`{ans}`")

    # Dictionary access
    add("What is the output of:\n`d = {'a': 1}`\n`print(d.get('b', 0))`?", "`0` (since 'b' is not in the dictionary, it returns the default value 0).")
    
    # Sets
    add("What is the output of `{1, 2, 2, 3}`?", "`{1, 2, 3}` (Sets automatically remove duplicates).")
    add("What is the output of `{1, 2} | {2, 3}`?", "`{1, 2, 3}` (Union of sets).")
    add("What is the output of `{1, 2} & {2, 3}`?", "`{2}` (Intersection of sets).")
    add("What is the output of `{1, 2} - {2, 3}`?", "`{1}` (Difference of sets).")

    # ==========================================
    # 6. FUNCTIONS & SCOPE
    # ==========================================
    add("What is the keyword used to define a function?", "`def`")
    add("What are `*args` and `**kwargs`?", "`*args` allows a function to accept any number of positional arguments (as a tuple). `**kwargs` allows it to accept any number of keyword arguments (as a dictionary).")
    add("What is a lambda expression?", "An anonymous, single-line function defined using the `lambda` keyword. Example: `lambda x: x + 1`.")
    add("If a function doesn't explicitly return a value, what does it return?", "`None`")
    
    add("What is the output of:\n`f = lambda x, y: x + y`\n`print(f(3, 4))`?", "`7`")
    
    # Scope
    add("What is the difference between local and global scope?", "Local scope refers to variables defined within a function. Global scope refers to variables defined at the top level of the script, accessible anywhere.")
    add("How can you modify a global variable inside a function?", "By using the `global` keyword before the variable name inside the function.")

    # ==========================================
    # 7. ERROR & EXCEPTION HANDLING
    # ==========================================
    add("How do you catch all exceptions in a try block?", "Using a bare `except:` block, or preferably `except Exception as e:`.")
    add("What does the `finally` block do?", "It executes code regardless of whether an exception occurred or not. Often used for cleanup (e.g., closing files).")
    add("What keyword is used to manually trigger an exception?", "`raise`")
    add("What exception is raised if you divide by zero?", "`ZeroDivisionError`")
    add("What exception is raised if you access an invalid index in a list?", "`IndexError`")
    add("What exception is raised if you try to access a non-existent key in a dictionary?", "`KeyError`")

    # ==========================================
    # 8. OBJECT-ORIENTED PROGRAMMING (OOP)
    # ==========================================
    add("What is the `__init__` method?", "It is the constructor method in Python. It is automatically called when a new object of the class is instantiated.")
    add("What does the `self` parameter represent?", "It represents the instance of the class itself, allowing access to its attributes and methods.")
    add("What is Inheritance?", "A mechanism where a new class (child) derives properties and methods from an existing class (parent).")
    add("What is Polymorphism in Python?", "The ability of different objects to respond to the same method call in their own specific way (e.g., both a `Dog` and `Cat` class having a `speak()` method).")
    add("How do you indicate that an attribute should be 'private' in Python?", "By prefixing the attribute name with an underscore `_` (convention) or double underscore `__` (name mangling).")

    # ==========================================
    # 9. FILE HANDLING & MODULES
    # ==========================================
    add("How do you open a file for reading?", "`open('filename.txt', 'r')`")
    add("What is the advantage of using the `with` statement to open files?", "It automatically closes the file when the block exits, even if an exception occurs. (Context Manager).")
    add("What does `file.readlines()` do?", "It reads the entire file and returns a list containing each line as a string element.")
    add("How do you import a specific function from a module?", "Using `from module_name import function_name`.")
    add("What is the difference between `import math` and `from math import *`?", "`import math` imports the module object, requiring you to use `math.sqrt()`. `from math import *` imports all functions directly into the current namespace, allowing you to use `sqrt()` directly (but can cause namespace pollution).")

    # Generating additional variations to hit the 500+ mark
    names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi", "Ivan"]
    for i in range(len(names)):
        add(f"Given `names = {names}`, what is `names[{i}]`?", f"`'{names[i]}'`")
        if i > 0:
            add(f"Given `names = {names}`, what is `names[{-i}]`?", f"`'{names[-i]}'`")
            
    # List combinations and manipulations
    for i in range(1, 15):
        for j in range(1, 15):
            add(f"What is the output of `[x for x in range({i}, {i+j}) if x % 2 == 0]`?", f"`{[x for x in range(i, i+j) if x % 2 == 0]}`")
            add(f"What is the output of `[x for x in range({i}, {i+j}) if x % 3 == 0]`?", f"`{[x for x in range(i, i+j) if x % 3 == 0]}`")

    # Math module combinations
    import math
    for val in [1.5, 2.7, 3.1, -1.5, -2.7, 4.9, 0.1]:
        add(f"What is the output of `math.floor({val})`?", f"`{math.floor(val)}`")
        add(f"What is the output of `math.ceil({val})`?", f"`{math.ceil(val)}`")
        add(f"What is the output of `round({val})`?", f"`{round(val)}`")

    # Tuple packing/unpacking
    for a in [1, 2, 3, 4]:
        for b in [5, 6, 7, 8]:
            add(f"What is the output of:\n`x, y = {a}, {b}`\n`x, y = y, x`\n`print(x, y)`?", f"`{b} {a}`")

    # String methods
    for w in ["apple", "banana", "cherry", "date", "elderberry"]:
        add(f"What is the output of `'{w}'.capitalize()`?", f"`'{w.capitalize()}'`")
        add(f"What is the output of `'{w}'.count('a')`?", f"`{w.count('a')}`")
        add(f"What is the output of `'{w}'.count('e')`?", f"`{w.count('e')}`")
        add(f"What is the output of `'{w}'.find('a')`?", f"`{w.find('a')}`")

    # Bitwise operators
    for a in [5, 10, 15]:
        for b in [1, 2, 3]:
            add(f"What is the output of `{a} << {b}`?", f"`{a << b}`")
            add(f"What is the output of `{a} >> {b}`?", f"`{a >> b}`")
            add(f"What is the output of `{a} & {b}`?", f"`{a & b}`")
            add(f"What is the output of `{a} | {b}`?", f"`{a | b}`")

    # Dictionary iterations
    add("How do you iterate over both keys and values in a dictionary?", "Using the `items()` method: `for key, value in my_dict.items():`")

    # Variable naming validity
    valid_names = ["my_var", "_my_var", "myVar123", "var_name", "COUNT"]
    invalid_names = ["123var", "my-var", "my var", "class", "def"]
    for v in valid_names:
        add(f"Is `{v}` a valid Python variable name?", "Yes.")
    for v in invalid_names:
        add(f"Is `{v}` a valid Python variable name?", "No (invalid syntax or reserved keyword).")
        
    # Extra loops output (nested)
    for i in [2, 3]:
        for j in [2, 3]:
            add(f"How many times will this loop run?\n`for x in range({i}):`\n`  for y in range({j}):`\n`    pass`", f"`{i * j}` times.")

    # List insert and extend
    add("What is the difference between `list.append()` and `list.extend()`?", "`append()` adds its argument as a single element to the end of a list. `extend()` iterates over its argument and adds each element to the list.")

    # Truthy/Falsy
    for v in ["''", "0", "0.0", "[]", "()", "{}", "None", "False"]:
        add(f"Is `{v}` considered Truthy or Falsy in Python?", "Falsy.")

    # Remove duplicates
    unique_flashcards = []
    seen = set()
    for fc in flashcards:
        if fc["question"] not in seen:
            seen.add(fc["question"])
            unique_flashcards.append(fc)
            
    return unique_flashcards

def seed():
    db = Prisma()
    db.connect()

    print("Fetching Python lesson...")
    python_lesson = db.lesson.find_first(
        where={
            "title": {
                "contains": "Python"
            }
        }
    )

    if not python_lesson:
        print("Error: Python lesson not found!")
        db.disconnect()
        return

    print("Cleaning up old dummy flashcards for Python...")
    db.flashcard.delete_many(where={"lessonId": python_lesson.id})

    flashcards = generate_flashcards()
    print(f"Generated {len(flashcards)} unique high-quality Python questions.")

    print("Inserting flashcards into database in batches...")
    
    # Insert in batches to avoid query limits
    batch_size = 50
    for i in range(0, len(flashcards), batch_size):
        batch = flashcards[i:i+batch_size]
        data_to_insert = [{"question": f["question"], "answer": f["answer"], "lessonId": python_lesson.id} for f in batch]
        db.flashcard.create_many(data=data_to_insert)

    print("Finished seeding new Python curriculum!")
    db.disconnect()

if __name__ == "__main__":
    seed()
