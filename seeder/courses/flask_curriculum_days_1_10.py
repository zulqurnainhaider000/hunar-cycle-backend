"""
Flask Mastery 40-Day Curriculum - Module 1 & Module 2 (Days 1 to 10)
Module 1: Basics & Setup (Days 1-5)
Module 2: Templates & UI (Days 6-10)
"""

from seeder.course_blueprint import DayBlueprint, QuizQuestionBlueprint, CodingChallengeBlueprint

DAYS_1_TO_10 = [
    # -------------------------------------------------------------
    # DAY 1
    # -------------------------------------------------------------
    DayBlueprint(
        order=1,
        title="Day 1: Virtual Environments & Flask Installation",
        concept="Isolating Python project dependencies using venv and pip",
        analogy="Imagine you are building a LEGO castle in your living room, and your sibling is building a LEGO spaceship. If you mix all the pieces in one big box, you might accidentally lose or break each other's custom bricks. A virtual environment gives you your own dedicated, private toy box just for your Flask project!",
        theory_sections=[
            {
                "heading": "Why Do We Need Virtual Environments?",
                "body": "When developing Python applications, different projects often require different versions of libraries (such as Flask 2.0 vs Flask 3.0). If you install everything globally on your operating system, version conflicts will occur. A Python virtual environment (`venv`) is a self-contained directory tree that contains a specific Python installation plus extra packages, keeping your project clean and reproducible."
            },
            {
                "heading": "Core CLI Commands for Virtual Environments",
                "body": "Python includes the `venv` module by default. You create an environment with `python -m venv venv`. You activate it using `venv\\Scripts\\activate` on Windows or `source venv/bin/activate` on macOS/Linux. Once activated, any package installed via `pip install flask` stays inside this sandbox."
            }
        ],
        code_snippets=[
            {
                "title": "Creating a Virtual Environment",
                "code": "# In your terminal, navigate to your project directory:\n# python -m venv myenv"
            },
            {
                "title": "Activating the Environment on Windows & Linux",
                "code": "# On Windows (PowerShell/CMD):\n# .\\myenv\\Scripts\\activate\n\n# On macOS / Linux:\n# source myenv/bin/activate"
            },
            {
                "title": "Installing Flask with pip",
                "code": "# With the environment activated:\n# pip install flask\n# pip freeze > requirements.txt"
            },
            {
                "title": "Verifying Flask Installation in Python",
                "code": "import flask\n\nprint('Flask successfully imported!')\nprint(f'Installed Flask Version: {flask.__version__}')"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Environment & Version Inspector",
            description="Write a Python script that imports Flask, checks its version string, and prints a success banner confirming the environment is ready for development.",
            starter_code="import flask\n\n# TODO: Inspect flask version and print confirmation\nversion = flask.__version__\nprint(f'Ready to build with Flask v{version}')\n",
            solution_code="import flask\n\nversion = flask.__version__\nprint('=== ENVIRONMENT CHECK ===')\nprint(f'Status: ACTIVE')\nprint(f'Framework: Flask v{version}')\nprint('=========================')",
            expected_output="=== ENVIRONMENT CHECK ===\nStatus: ACTIVE\nFramework: Flask v3.0.0\n========================="
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Why is it best practice to use a virtual environment for Flask projects?",
                options=[
                    "To isolate dependencies and avoid package version conflicts between projects.",
                    "Because Python refuses to run without a virtual environment.",
                    "To increase internet download speeds for web requests.",
                    "Virtual environments automatically compile Python to machine code."
                ],
                correct_answer="To isolate dependencies and avoid package version conflicts between projects.",
                explanation="Virtual environments sandbox project packages so dependencies don't interfere with system Python."
            ),
            QuizQuestionBlueprint(
                question="Which standard library module creates virtual environments in modern Python?",
                options=["venv", "virtualenv", "pip", "flask_env"],
                correct_answer="venv",
                explanation="The built-in `venv` module has been standard in Python since 3.3."
            ),
            QuizQuestionBlueprint(
                question="On Windows PowerShell, which script activates a virtual environment named 'venv'?",
                options=[
                    ".\\venv\\Scripts\\Activate.ps1",
                    "source venv/bin/activate",
                    "python venv start",
                    "pip activate venv"
                ],
                correct_answer=".\\venv\\Scripts\\Activate.ps1",
                explanation="On Windows, activation scripts reside inside the `Scripts` directory."
            ),
            QuizQuestionBlueprint(
                question="Which file is standardly used to freeze and document project dependencies?",
                options=["requirements.txt", "packages.json", "flask.lock", "setup.cfg"],
                correct_answer="requirements.txt",
                explanation="`pip freeze > requirements.txt` records all installed package versions."
            ),
            QuizQuestionBlueprint(
                question="What terminal command installs the Flask package into an activated environment?",
                options=["pip install flask", "python install flask", "flask get", "npm install flask"],
                correct_answer="pip install flask",
                explanation="`pip install flask` downloads and installs Flask and its dependencies (Werkzeug, Jinja2, etc.)."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 2
    # -------------------------------------------------------------
    DayBlueprint(
        order=2,
        title="Day 2: Hello World App (app = Flask(__name__))",
        concept="Instantiating the Flask application object and running the WSGI development server",
        analogy="Think of `app = Flask(__name__)` like opening the doors to a new restaurant. The restaurant manager (Flask) needs to know what building it is situated in (`__name__`) so it can find the kitchen (templates) and the pantry (static files)!",
        theory_sections=[
            {
                "heading": "Understanding the Application Object",
                "body": "Every Flask web application begins with an instance of the `Flask` class. We pass `__name__` as the first argument, which is a special Python variable that evaluates to the current module's name (`'__main__'`). Flask uses this location to find templates, assets, and root configurations."
            },
            {
                "heading": "The Request-Response Lifecycle",
                "body": "When a web browser sends an HTTP request to `http://127.0.0.1:5000/`, Flask receives the request, matches the URL path to a registered view function using a decorator `@app.route('/')`, executes the Python function, and sends the returned string back as an HTTP 200 response."
            }
        ],
        code_snippets=[
            {
                "title": "The Minimal Flask Application",
                "code": "from flask import Flask\n\napp = Flask(__name__)\n\n@app.route('/')\ndef hello_world():\n    return 'Hello, World! Welcome to Flask!'\n\nif __name__ == '__main__':\n    app.run(debug=True)"
            },
            {
                "title": "Why We Pass __name__ to Flask",
                "code": "# __name__ is a built-in Python string\nprint(f'Current module name: {__name__}')\n# If executed directly, __name__ is '__main__'"
            },
            {
                "title": "Running with the Flask CLI",
                "code": "# In terminal:\n# export FLASK_APP=app.py (Linux/Mac)\n# $env:FLASK_APP = 'app.py' (Windows PowerShell)\n# flask run --port=5000 --debug"
            },
            {
                "title": "Returning HTML directly from a route",
                "code": "from flask import Flask\n\napp = Flask(__name__)\n\n@app.route('/')\ndef home():\n    return '<h1>Welcome to Hunar Cycle!</h1><p>Crafted with Flask microframework.</p>'"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Construct a Minimal Flask App with Custom Port",
            description="Write a complete Python script that instantiates a Flask app object, defines a root route returning 'Server Online: Port 5000', and configures app.run with host='0.0.0.0' and port=5000.",
            starter_code="from flask import Flask\n\n# TODO: Create app instance and define root route\napp = Flask(__name__)\n",
            solution_code="from flask import Flask\n\napp = Flask(__name__)\n\n@app.route('/')\ndef status():\n    return 'Server Online: Port 5000'\n\nif __name__ == '__main__':\n    app.run(host='0.0.0.0', port=5000, debug=True)",
            expected_output="Server Online: Port 5000"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What does `__name__` represent when passed into `Flask(__name__)`?",
                options=[
                    "The name of the current Python module or package.",
                    "The title of the website displayed in the browser tab.",
                    "The database connection string.",
                    "The secret encryption key for sessions."
                ],
                correct_answer="The name of the current Python module or package.",
                explanation="Flask uses `__name__` to determine the root path of the application to locate resources."
            ),
            QuizQuestionBlueprint(
                question="What Python construct is used to bind a URL endpoint to a view function?",
                options=[
                    "Decorator (`@app.route`)",
                    "Class inheritance",
                    "Generator (`yield`)",
                    "Lambda expression"
                ],
                correct_answer="Decorator (`@app.route`)",
                explanation="`@app.route('/path')` is a decorator that registers the function as the handler for that URL."
            ),
            QuizQuestionBlueprint(
                question="What is the default port number that the Flask development server listens on?",
                options=["5000", "8000", "3000", "8080"],
                correct_answer="5000",
                explanation="Flask defaults to port 5000 on localhost (127.0.0.1:5000)."
            ),
            QuizQuestionBlueprint(
                question="What does the parameter `debug=True` do in `app.run()`?",
                options=[
                    "Enables interactive in-browser debugger and auto-reloading on code changes.",
                    "Disables all security checks for production.",
                    "Logs all requests directly to a remote cloud database.",
                    "Runs tests automatically before each request."
                ],
                correct_answer="Enables interactive in-browser debugger and auto-reloading on code changes.",
                explanation="Debug mode provides live reload and an interactive traceback debugger in the browser."
            ),
            QuizQuestionBlueprint(
                question="What is the standard HTTP status code returned by default when a route function returns a string?",
                options=["200 OK", "201 Created", "302 Found", "404 Not Found"],
                correct_answer="200 OK",
                explanation="Flask automatically wraps string return values in a Response object with status 200 OK."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 3
    # -------------------------------------------------------------
    DayBlueprint(
        order=3,
        title="Day 3: Routing & URL Mapping",
        concept="Mapping different endpoint URLs to specific Python view functions",
        analogy="Think of URL routing like a building directory in a shopping mall. When a visitor asks for '/electronics', the front desk directs them to the 3rd floor. When they ask for '/food-court', they are guided to the ground floor. In Flask, `@app.route` is that directory!",
        theory_sections=[
            {
                "heading": "URL Rules and Endpoint Registration",
                "body": "Routing is the mechanism of binding a URL pattern to a Python function. When an incoming HTTP request arrives, Flask searches its internal URL map (`app.url_map`). If a match is found, Flask executes the corresponding function."
            },
            {
                "heading": "Trailing Slashes and Redirection",
                "body": "In Flask, a route defined as `@app.route('/about/')` with a trailing slash acts like a folder in a filesystem. If the user visits `/about`, Flask automatically redirects them to `/about/` with HTTP 308. Conversely, a route defined as `@app.route('/about')` without a slash is treated like a unique file; accessing `/about/` returns a 404 Not Found."
            }
        ],
        code_snippets=[
            {
                "title": "Registering Multiple Static Routes",
                "code": "from flask import Flask\n\napp = Flask(__name__)\n\n@app.route('/')\ndef home():\n    return 'Home Page'\n\n@app.route('/about')\ndef about():\n    return 'About Us Page'\n\n@app.route('/contact')\ndef contact():\n    return 'Contact Us Page'"
            },
            {
                "title": "Mapping Multiple URLs to the Same Function",
                "code": "@app.route('/')\n@app.route('/index')\n@app.route('/home')\ndef index():\n    return 'Welcome to the landing page!'"
            },
            {
                "title": "Generating URLs dynamically with url_for",
                "code": "from flask import Flask, url_for\n\napp = Flask(__name__)\n\n@app.route('/dashboard')\ndef user_dashboard():\n    return 'Dashboard'\n\nwith app.test_request_context():\n    # url_for takes the FUNCTION name, not the path\n    print('Generated URL:', url_for('user_dashboard'))\n    # Output: /dashboard"
            },
            {
                "title": "Inspecting the Flask URL Map",
                "code": "with app.test_request_context():\n    print(app.url_map)"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Multi-Endpoint Navigation System",
            description="Create a Flask application with three distinct routes: '/', '/pricing', and '/faq'. Each route should return a distinct plaintext description.",
            starter_code="from flask import Flask\n\napp = Flask(__name__)\n\n# TODO: Add '/', '/pricing', and '/faq' routes\n",
            solution_code="from flask import Flask\n\napp = Flask(__name__)\n\n@app.route('/')\ndef home():\n    return 'Home View'\n\n@app.route('/pricing')\ndef pricing():\n    return 'Tier 1: Free, Tier 2: Pro'\n\n@app.route('/faq')\ndef faq():\n    return 'Frequently Asked Questions'",
            expected_output="Tier 1: Free, Tier 2: Pro"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What function is used in Flask to reverse-lookup or generate URLs from function names?",
                options=["url_for()", "reverse()", "get_url()", "route_to()"],
                correct_answer="url_for()",
                explanation="`url_for('function_name')` looks up the URL rule associated with the given endpoint."
            ),
            QuizQuestionBlueprint(
                question="Can multiple `@app.route` decorators be stacked on top of a single Python view function?",
                options=[
                    "Yes, mapping multiple different URLs to the same handler function.",
                    "No, Flask will throw a RouteCollisionError.",
                    "Only if using regular expressions.",
                    "Only if the HTTP method is POST."
                ],
                correct_answer="Yes, mapping multiple different URLs to the same handler function.",
                explanation="Stacking decorators is standard practice to alias URLs (e.g. '/' and '/home')."
            ),
            QuizQuestionBlueprint(
                question="If a route is defined as `@app.route('/contact/')`, what happens if the user visits `/contact`?",
                options=[
                    "Flask issues a 308 permanent redirect to `/contact/`.",
                    "Flask immediately returns 404 Not Found.",
                    "Flask throws an Internal Server Error 500.",
                    "The browser crashes."
                ],
                correct_answer="Flask issues a 308 permanent redirect to `/contact/`.",
                explanation="Flask normalizes URLs with trailing slashes by redirecting users to the canonical version."
            ),
            QuizQuestionBlueprint(
                question="Where does Flask store all registered route patterns internally?",
                options=["app.url_map", "app.routes_list", "app.router_cache", "app.endpoints"],
                correct_answer="app.url_map",
                explanation="`app.url_map` is a Werkzeug Map object holding all URL routing rules."
            ),
            QuizQuestionBlueprint(
                question="What argument does `url_for('about')` expect as its first parameter?",
                options=[
                    "The name of the view function as a string.",
                    "The raw URL path string (e.g. '/about').",
                    "The HTTP method (e.g. 'GET').",
                    "The template file name (e.g. 'about.html')."
                ],
                correct_answer="The name of the view function as a string.",
                explanation="`url_for` takes the endpoint name, which defaults to the Python function name."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 4
    # -------------------------------------------------------------
    DayBlueprint(
        order=4,
        title="Day 4: Dynamic Routing & URL Converters",
        concept="Capturing variable segments from URLs and converting them into typed Python arguments",
        analogy="Think of dynamic routing like a personalized name tag slot on an office door. Instead of building 500 different doors for 500 employees, you build one standard door frame with a slot `<employee_name>`. Whoever walks up slides their name in, and the office welcomes them by name!",
        theory_sections=[
            {
                "heading": "Variable URL Parts",
                "body": "Static routes only match fixed text. Modern web applications require dynamic parameters, such as user IDs or product slugs. In Flask, you add variable sections to a URL by marking them with `<variable_name>`. Your view function receives this variable as a keyword argument."
            },
            {
                "heading": "Built-In Type Converters",
                "body": "By default, variables are parsed as strings (`string:`). Flask provides built-in type converters that parse the URL value before passing it to your function: `int:` (accepts positive integers), `float:` (accepts floating-point numbers), `path:` (accepts strings including slashes), and `uuid:` (accepts UUID strings). If the URL does not match the converter type, Flask returns a 404 automatically."
            }
        ],
        code_snippets=[
            {
                "title": "Basic String Variable in Route",
                "code": "from flask import Flask\n\napp = Flask(__name__)\n\n@app.route('/user/<username>')\ndef show_user_profile(username):\n    # username is passed directly as a string\n    return f'Viewing profile for: {username}'"
            },
            {
                "title": "Integer and Float Converters",
                "code": "@app.route('/post/<int:post_id>')\ndef show_post(post_id):\n    # post_id is guaranteed to be a Python int\n    return f'Displaying Blog Post #{post_id} (Type: {type(post_id).__name__})'\n\n@app.route('/price/<float:amount>')\ndef show_discount(amount):\n    return f'Discounted Price: ${amount * 0.9:.2f}'"
            },
            {
                "title": "The Path Converter for Multi-Segment URLs",
                "code": "@app.route('/files/<path:subpath>')\ndef show_subpath(subpath):\n    # Captures everything after /files/, including slashes like 'docs/2026/report.pdf'\n    return f'Accessing subpath: {subpath}'"
            },
            {
                "title": "Dynamic url_for with keyword arguments",
                "code": "from flask import url_for\n\nwith app.test_request_context():\n    url = url_for('show_post', post_id=42)\n    print('Generated dynamic URL:', url)\n    # Output: /post/42"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Product SKU and Quantity Calculator",
            description="Define a route `/order/<int:item_id>/<int:quantity>` that calculates the total cost for an item assuming a fixed unit price of $25 and returns a formatted invoice summary.",
            starter_code="from flask import Flask\n\napp = Flask(__name__)\n\n# TODO: Define /order/<int:item_id>/<int:quantity> route\n",
            solution_code="from flask import Flask\n\napp = Flask(__name__)\n\n@app.route('/order/<int:item_id>/<int:quantity>')\ndef calculate_order(item_id, quantity):\n    unit_price = 25\n    total = unit_price * quantity\n    return f'Item #{item_id}: Quantity {quantity} | Total: ${total}'",
            expected_output="Item #101: Quantity 4 | Total: $100"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What happens if a user visits `/post/abc` when the route is defined as `@app.route('/post/<int:post_id>')`?",
                options=[
                    "Flask immediately returns a 404 Not Found error because 'abc' is not an integer.",
                    "Flask throws an unhandled ValueError exception.",
                    "Flask converts 'abc' into 0.",
                    "Flask converts 'abc' into its ASCII code."
                ],
                correct_answer="Flask immediately returns a 404 Not Found error because 'abc' is not an integer.",
                explanation="Type converters validate the URL before invoking the view function; failed validation triggers a 404."
            ),
            QuizQuestionBlueprint(
                question="Which converter allows a URL parameter to match text containing forward slashes (`/`)?",
                options=["path", "string", "slug", "all"],
                correct_answer="path",
                explanation="The `path:` converter accepts slashes, making it suitable for file systems and folder paths."
            ),
            QuizQuestionBlueprint(
                question="What is the default data type of a variable parameter if no converter prefix is specified (e.g., `<username>`)?",
                options=["string (str)", "integer (int)", "bytes", "object"],
                correct_answer="string (str)",
                explanation="If omitted, `<variable>` defaults to `<string:variable>`, matching any text without slashes."
            ),
            QuizQuestionBlueprint(
                question="How do you pass variable arguments into `url_for()` when reversing a dynamic route?",
                options=[
                    "As keyword arguments: `url_for('show_post', post_id=12)`",
                    "By concatenating strings: `url_for('show_post') + '/12'`",
                    "Through a list: `url_for('show_post', [12])`",
                    "In the headers dictionary"
                ],
                correct_answer="As keyword arguments: `url_for('show_post', post_id=12)`",
                explanation="`url_for` accepts keyword arguments matching the variable parameters defined in the route rule."
            ),
            QuizQuestionBlueprint(
                question="Which built-in converter validates standard 32-character hexadecimal UUID strings?",
                options=["uuid", "guid", "hex", "hash"],
                correct_answer="uuid",
                explanation="Flask provides a built-in `uuid:` converter that yields a `uuid.UUID` Python object."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 5 (Mini-Project)
    # -------------------------------------------------------------
    DayBlueprint(
        order=5,
        title="Day 5: HTTP Methods (GET & POST) - Data Receiver Mini-Project",
        concept="Handling different HTTP request methods (GET vs POST) within Flask route handlers",
        analogy="Think of HTTP GET like looking at a restaurant's display menu through the window (you are only reading information, not changing anything). Think of HTTP POST like placing your food order with the waiter (you are sending new data to the kitchen to be prepared)!",
        theory_sections=[
            {
                "heading": "HTTP Verbs and REST Principles",
                "body": "Web browsers interact with servers using HTTP methods. By default, Flask routes only respond to `GET` requests. To allow forms or clients to submit data, you must explicitly enable `POST` via the `methods` argument: `@app.route('/submit', methods=['GET', 'POST'])`."
            },
            {
                "heading": "Differentiating GET vs POST with request.method",
                "body": "Inside the view function, you inspect `request.method` from the `flask` module. If `request.method == 'POST'`, you process submitted payload data (such as `request.form`). If it is a `GET` request, you display an input form or default message."
            }
        ],
        code_snippets=[
            {
                "title": "Specifying Allowed HTTP Methods",
                "code": "from flask import Flask, request\n\napp = Flask(__name__)\n\n@app.route('/login', methods=['GET', 'POST'])\ndef login():\n    if request.method == 'POST':\n        return 'Processing login submission...'\n    return 'Displaying login page...'"
            },
            {
                "title": "Accessing Form Data with request.form",
                "code": "@app.route('/feedback', methods=['POST'])\ndef receive_feedback():\n    user_name = request.form.get('username', 'Anonymous')\n    message = request.form.get('message', '')\n    return f'Thank you {user_name}! We received: {message}'"
            },
            {
                "title": "Returning Custom HTTP Status Codes",
                "code": "@app.route('/create-user', methods=['POST'])\ndef create_user():\n    # In REST APIs, 201 Created is returned for successful resource creation\n    return {'status': 'success', 'user_id': 101}, 201"
            },
            {
                "title": "Mini-Project: The Multi-Method Data Receiver",
                "code": "from flask import Flask, request, jsonify\n\napp = Flask(__name__)\n\n# In-memory storage for demonstration\nmessages_db = []\n\n@app.route('/api/messages', methods=['GET', 'POST'])\ndef handle_messages():\n    if request.method == 'POST':\n        data = request.form.get('text')\n        if not data:\n            return jsonify({'error': 'Message text is required'}), 400\n        messages_db.append(data)\n        return jsonify({'message': 'Saved successfully', 'total': len(messages_db)}), 201\n    return jsonify({'messages': messages_db})"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Lead Capture Data Receiver",
            description="Implement a route `/subscribe` that accepts both GET and POST requests. On GET, return 'Please submit your email via POST'. On POST, extract 'email' from request.form and return 'Subscription confirmed for: <email>' with status 201.",
            starter_code="from flask import Flask, request\n\napp = Flask(__name__)\n\n# TODO: Implement /subscribe for GET and POST\n",
            solution_code="from flask import Flask, request\n\napp = Flask(__name__)\n\n@app.route('/subscribe', methods=['GET', 'POST'])\ndef subscribe():\n    if request.method == 'POST':\n        email = request.form.get('email', 'unknown')\n        return f'Subscription confirmed for: {email}', 201\n    return 'Please submit your email via POST'",
            expected_output="Subscription confirmed for: user@example.com"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What HTTP method do Flask routes listen to by default if `methods` is not specified?",
                options=["GET only", "GET and POST", "POST only", "ALL HTTP methods"],
                correct_answer="GET only",
                explanation="By default, `@app.route('/path')` only accepts GET requests. Other methods receive a 405 Method Not Allowed."
            ),
            QuizQuestionBlueprint(
                question="Which HTTP status code is sent automatically by Flask when an unpermitted method is used?",
                options=["405 Method Not Allowed", "400 Bad Request", "403 Forbidden", "404 Not Found"],
                correct_answer="405 Method Not Allowed",
                explanation="HTTP 405 indicates that the request method is recognized by the server but not supported by the target resource."
            ),
            QuizQuestionBlueprint(
                question="Where does Flask store submitted form data encoded as `application/x-www-form-urlencoded`?",
                options=["request.form", "request.args", "request.data", "request.body"],
                correct_answer="request.form",
                explanation="`request.form` contains parsed key-value pairs submitted from HTML forms via POST."
            ),
            QuizQuestionBlueprint(
                question="What HTTP status code semantically signifies that a new resource was successfully created?",
                options=["201 Created", "200 OK", "204 No Content", "301 Moved Permanently"],
                correct_answer="201 Created",
                explanation="In standard HTTP semantics, 201 Created indicates successful resource generation."
            ),
            QuizQuestionBlueprint(
                question="Why is `request.form.get('field', default_value)` safer than `request.form['field']`?",
                options=[
                    "It returns the default value without raising a KeyError if the field is missing.",
                    "It automatically encrypts the string.",
                    "It prevents SQL injection automatically.",
                    "It makes the request run asynchronously."
                ],
                correct_answer="It returns the default value without raising a KeyError if the field is missing.",
                explanation="Dictionary `.get()` avoids unhandled `KeyError` (which manifests as HTTP 400 Bad Request in Flask)."
            )
        ],
        is_project_day=True,
        project_name="HTTP Methods & Basic Data Receiver"
    ),

    # -------------------------------------------------------------
    # DAY 6
    # -------------------------------------------------------------
    DayBlueprint(
        order=6,
        title="Day 6: Jinja2 Templating Engine Basics",
        concept="Rendering dynamic HTML pages using Jinja2 variables, filters, and control structures",
        analogy="Think of a Jinja2 template like a 'Fill-in-the-Blanks' certificate. The certificate has pre-printed borders and text, but has blank lines marked `{{ student_name }}` and `{{ completion_date }}`. When a student graduates, Flask prints the exact name into the blank space!",
        theory_sections=[
            {
                "heading": "Separating Business Logic from Presentation",
                "body": "Returning raw HTML strings inside Python functions becomes unmanageable as UI grows. Flask uses the Jinja2 templating engine, which allows you to store `.html` files in a `templates/` folder and render them dynamically using the `render_template()` helper."
            },
            {
                "heading": "Jinja2 Syntax: Delimiters and Filters",
                "body": "Jinja2 provides three primary delimiters: `{{ variable }}` for printing output expressions, `{% statement %}` for control logic like `if` conditions and `for` loops, and `{# comment #}` for template comments. Jinja2 also includes filters like `{{ name|upper }}` or `{{ title|title }}` to format data directly in HTML."
            }
        ],
        code_snippets=[
            {
                "title": "Rendering a Template from Python",
                "code": "from flask import Flask, render_template\n\napp = Flask(__name__)\n\n@app.route('/')\ndef home():\n    user_name = 'Zubair'\n    skills = ['Python', 'Flask', 'PostgreSQL', 'Docker']\n    # Passes variables into templates/index.html\n    return render_template('index.html', name=user_name, skills=skills)"
            },
            {
                "title": "Basic Jinja2 Variable and Filter Syntax (index.html)",
                "code": "<!-- templates/index.html -->\n<h1>Welcome, {{ name|upper }}!</h1>\n<p>Account Status: {{ status|default('Standard Member') }}</p>"
            },
            {
                "title": "Control Structures: If Conditions & For Loops",
                "code": "<!-- templates/skills.html -->\n<h2>Technical Skills</h2>\n<ul>\n{% for skill in skills %}\n    <li>{{ loop.index }}. {{ skill }}</li>\n{% else %}\n    <li>No skills listed yet.</li>\n{% endfor %}\n</ul>"
            },
            {
                "title": "Conditional Statements in Jinja2",
                "code": "{% if is_logged_in %}\n    <p>Welcome back! <a href=\"/logout\">Sign Out</a></p>\n{% else %}\n    <p>Please <a href=\"/login\">Log In</a> to continue.</p>\n{% endif %}"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Dynamic Grade Report Generator",
            description="Write a Python script that renders a Jinja2 template string simulating a student report card. Calculate average score and display 'Honor Roll' if score >= 85.",
            starter_code="from jinja2 import Template\n\ntemplate_str = '''Student: {{ name }}\nScore: {{ score }}\nStatus: {% if score >= 85 %}Honor Roll{% else %}Passing{% endif %}'''\n# TODO: Render template with name='Amina' and score=92\n",
            solution_code="from jinja2 import Template\n\ntemplate_str = '''Student: {{ name }}\nScore: {{ score }}\nStatus: {% if score >= 85 %}Honor Roll{% else %}Passing{% endif %}'''\ntemplate = Template(template_str)\nresult = template.render(name='Amina', score=92)\nprint(result)",
            expected_output="Student: Amina\nScore: 92\nStatus: Honor Roll"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What folder does Flask look in by default when `render_template('index.html')` is called?",
                options=["templates", "views", "html", "static"],
                correct_answer="templates",
                explanation="By default, Flask expects template files to reside inside a subfolder named `templates`."
            ),
            QuizQuestionBlueprint(
                question="Which Jinja2 delimiter is used to evaluate statements like loops and conditionals?",
                options=["{% ... %}", "{{ ... }}", "{# ... #}", "<% ... %>"],
                correct_answer="{% ... %}",
                explanation="`{% ... %}` is used for control structures, while `{{ ... }}` is for printing expressions."
            ),
            QuizQuestionBlueprint(
                question="How do you apply a filter to transform a variable to uppercase in Jinja2?",
                options=["{{ name|upper }}", "{{ name.toUpperCase() }}", "{% upper name %}", "{{ upper(name) }}"],
                correct_answer="{{ name|upper }}",
                explanation="Jinja2 uses the pipe operator (`|`) followed by the filter name to transform values."
            ),
            QuizQuestionBlueprint(
                question="Inside a Jinja2 `{% for %}` loop, what special variable gives the 1-based index of the current iteration?",
                options=["loop.index", "loop.counter", "index", "loop.i"],
                correct_answer="loop.index",
                explanation="`loop.index` provides the 1-based counter; `loop.index0` provides the 0-based counter."
            ),
            QuizQuestionBlueprint(
                question="Which Jinja2 delimiter is used for template comments that do not render in the final HTML?",
                options=["{# comment #}", "<!-- comment -->", "// comment", "/* comment */"],
                correct_answer="{# comment #}",
                explanation="`{# ... #}` comments are completely stripped by Jinja2 during rendering."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 7
    # -------------------------------------------------------------
    DayBlueprint(
        order=7,
        title="Day 7: Template Inheritance & Layout Architecture",
        concept="Creating reusable base layouts with blocks using {% extends %} and {% block %}",
        analogy="Think of template inheritance like a newspaper template. The header banner, navigation menu, and footer copyright are printed on every single page. The blank square in the middle is reserved for whatever article is written that day. Child pages only write the article, not the whole newspaper!",
        theory_sections=[
            {
                "heading": "The DRY Principle in Web Design",
                "body": "Don't Repeat Yourself (DRY) is a cornerstone of software engineering. Copy-pasting the HTML `<head>`, `<nav>`, and `<footer>` across 20 different pages creates a maintenance nightmare. Template inheritance allows you to define a single skeleton (`base.html`) containing common UI elements."
            },
            {
                "heading": "Extends and Block Tags",
                "body": "In Jinja2, child templates declare their parent using `{% extends 'base.html' %}` as the very first line. The parent defines replaceable placeholders using `{% block content %}{% endblock %}`. Child templates override these specific blocks with their own unique content."
            }
        ],
        code_snippets=[
            {
                "title": "The Master Layout (templates/base.html)",
                "code": "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n    <meta charset=\"UTF-8\">\n    <title>{% block title %}My Application{% endblock %}</title>\n    <link rel=\"stylesheet\" href=\"/static/css/style.css\">\n</head>\n<body>\n    <nav>\n        <a href=\"/\">Home</a> | <a href=\"/about\">About</a> | <a href=\"/contact\">Contact</a>\n    </nav>\n    <main class=\"container\">\n        {% block content %}{% endblock %}\n    </main>\n    <footer>\n        <p>&copy; 2026 Hunar Cycle. All Rights Reserved.</p>\n    </footer>\n</body>\n</html>"
            },
            {
                "title": "Child Template Overriding Blocks (templates/home.html)",
                "code": "{% extends 'base.html' %}\n\n{% block title %}Home - Hunar Cycle{% endblock %}\n\n{% block content %}\n    <h1>Welcome to the Platform</h1>\n    <p>Empowering vocational skills with modern software engineering.</p>\n{% endblock %}"
            },
            {
                "title": "Preserving Parent Block Content with super()",
                "code": "{% extends 'base.html' %}\n\n{% block scripts %}\n    {# Retain scripts defined in base.html and append custom page script #}\n    {{ super() }}\n    <script src=\"/static/js/chart.js\"></script>\n{% endblock %}"
            },
            {
                "title": "Rendering the Child Template in Flask",
                "code": "from flask import Flask, render_template\n\napp = Flask(__name__)\n\n@app.route('/')\ndef home():\n    return render_template('home.html')"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Build a Two-Tier Template Structure",
            description="Construct a minimal base template string with a title block and content block, and a child template string extending it that sets the title to 'Dashboard' and content to 'System Analytics Active'.",
            starter_code="# Build base and child template strings\nbase_tpl = '''<title>{% block title %}{% endblock %}</title><body>{% block content %}{% endblock %}</body>'''\n",
            solution_code="from jinja2 import Environment, DictLoader\n\nloader = DictLoader({\n    'base.html': '<title>{% block title %}{% endblock %}</title><body>{% block content %}{% endblock %}</body>',\n    'dashboard.html': '{% extends \"base.html\" %}{% block title %}Dashboard{% endblock %}{% block content %}System Analytics Active{% endblock %}'\n})\nenv = Environment(loader=loader)\ntpl = env.get_template('dashboard.html')\nprint(tpl.render())",
            expected_output="<title>Dashboard</title><body>System Analytics Active</body>"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Which Jinja2 tag informs the templating engine that a template inherits from a parent layout?",
                options=["{% extends 'base.html' %}", "{% include 'base.html' %}", "{% import 'base.html' %}", "{% inherits 'base.html' %}"],
                correct_answer="{% extends 'base.html' %}",
                explanation="`{% extends %}` must be the first tag in the child template to declare inheritance."
            ),
            QuizQuestionBlueprint(
                question="What tag is used inside base layouts to define replaceable regions for child templates?",
                options=["{% block name %}{% endblock %}", "{% slot name %}", "{% placeholder name %}", "{{ block.name }}"],
                correct_answer="{% block name %}{% endblock %}",
                explanation="Blocks define named anchor points that child templates can populate or override."
            ),
            QuizQuestionBlueprint(
                question="How can a child template retain content from the parent's block while adding its own content?",
                options=["By calling `{{ super() }}`", "By using `{% parent %}`", "By using `{% inherit_all %}`", "It is not possible in Jinja2"],
                correct_answer="By calling `{{ super() }}`",
                explanation="`{{ super() }}` renders the parent block's contents inside the overriding child block."
            ),
            QuizQuestionBlueprint(
                question="What is the key difference between `{% extends %}` and `{% include %}` in Jinja2?",
                options=[
                    "`extends` establishes a master hierarchy; `include` simply copies a snippet directly into the template.",
                    "`include` can only be used for CSS files.",
                    "`extends` is deprecated in Flask 3.0.",
                    "`include` cannot access variables passed to the view."
                ],
                correct_answer="`extends` establishes a master hierarchy; `include` simply copies a snippet directly into the template.",
                explanation="`include` is for partials (like a navbar or modal snippet); `extends` is for architectural page layouts."
            ),
            QuizQuestionBlueprint(
                question="Where must the `{% extends %}` tag be located in a child template file?",
                options=[
                    "As the very first line/tag in the template.",
                    "Anywhere inside the `<head>` tag.",
                    "At the bottom of the template.",
                    "Inside the `{% block content %}` tag."
                ],
                correct_answer="As the very first line/tag in the template.",
                explanation="Jinja2 requires `{% extends %}` to appear before any other template content or blocks."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 8
    # -------------------------------------------------------------
    DayBlueprint(
        order=8,
        title="Day 8: Serving Static Files (CSS, JavaScript, Images)",
        concept="Managing static client assets using Flask's static folder and url_for",
        analogy="Think of static files like the stationery cabinet in a school. While the teacher (Python code) writes customized lessons every day, the paper, pens, and posters (CSS, JS, images) stay in the stationary cabinet, ready to be handed out to any student who asks for them!",
        theory_sections=[
            {
                "heading": "The Static Files Folder Convention",
                "body": "Web applications require static assets such as CSS stylesheets, JavaScript client scripts, web fonts, and images. Flask automatically configures a route `/static/<filename>` mapped to a directory named `static/` located in your project root."
            },
            {
                "heading": "Best Practice: Generating Static URLs with url_for",
                "body": "Never hardcode `/static/css/style.css` in your HTML. Always use `url_for('static', filename='css/style.css')`. This ensures URLs remain correct if the application is moved to a subpath, served behind a reverse proxy (like Nginx), or hosted on a CDN."
            }
        ],
        code_snippets=[
            {
                "title": "Recommended Project Directory Structure",
                "code": "# my_project/\n# ├── app.py\n# ├── templates/\n# │   ├── base.html\n# │   └── index.html\n# └── static/\n#     ├── css/\n#     │   └── main.css\n#     ├── js/\n#     │   └── app.js\n#     └── images/\n#         └── logo.png"
            },
            {
                "title": "Linking Static CSS and JS in base.html",
                "code": "<head>\n    <!-- Dynamically link CSS stylesheet -->\n    <link rel=\"stylesheet\" href=\"{{ url_for('static', filename='css/main.css') }}\">\n</head>\n<body>\n    <!-- Display image asset -->\n    <img src=\"{{ url_for('static', filename='images/logo.png') }}\" alt=\"Hunar Cycle Logo\">\n    \n    <!-- Include client JavaScript -->\n    <script src=\"{{ url_for('static', filename='js/app.js') }}\"></script>\n</body>"
            },
            {
                "title": "Customizing the Static Folder Location",
                "code": "from flask import Flask\n\n# Configure custom static folder and custom URL path if needed\napp = Flask(\n    __name__,\n    static_folder='public_assets',\n    static_url_path='/assets'\n)"
            },
            {
                "title": "Adding Cache-Busting Query Parameters",
                "code": "<!-- Avoid browser caching stale CSS during rapid development -->\n<link rel=\"stylesheet\" href=\"{{ url_for('static', filename='css/main.css', v='1.0.4') }}\">"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Static Asset Path Resolver",
            description="Write a Python script using Flask's test_request_context to generate valid static URLs for three files: 'css/bootstrap.min.css', 'js/bundle.js', and 'img/favicon.ico'.",
            starter_code="from flask import Flask, url_for\n\napp = Flask(__name__)\n\n# TODO: Generate static URLs within test_request_context\n",
            solution_code="from flask import Flask, url_for\n\napp = Flask(__name__)\n\nwith app.test_request_context():\n    css_url = url_for('static', filename='css/bootstrap.min.css')\n    js_url = url_for('static', filename='js/bundle.js')\n    fav_url = url_for('static', filename='img/favicon.ico')\n    print(f'CSS: {css_url}\\nJS: {js_url}\\nFAV: {fav_url}')",
            expected_output="CSS: /static/css/bootstrap.min.css\nJS: /static/js/bundle.js\nFAV: /static/img/favicon.ico"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the default directory name where Flask looks for CSS, JS, and image assets?",
                options=["static", "public", "assets", "resources"],
                correct_answer="static",
                explanation="Flask looks inside a folder named `static` located in the root of the application package."
            ),
            QuizQuestionBlueprint(
                question="What is the proper way to link a static stylesheet in a Jinja2 template?",
                options=[
                    "`<link rel=\"stylesheet\" href=\"{{ url_for('static', filename='css/style.css') }}\">`",
                    "`<link rel=\"stylesheet\" href=\"/static/css/style.css\">`",
                    "`<link rel=\"stylesheet\" href=\"{% static 'css/style.css' %}\">`",
                    "`<link rel=\"stylesheet\" href=\"{{ get_asset('css/style.css') }}\">`"
                ],
                correct_answer="`<link rel=\"stylesheet\" href=\"{{ url_for('static', filename='css/style.css') }}\">`",
                explanation="Using `url_for('static', filename=...)` ensures dynamic URL generation across different deployment roots."
            ),
            QuizQuestionBlueprint(
                question="Which parameter in the `Flask()` constructor allows customizing the folder where static files live?",
                options=["static_folder", "assets_dir", "public_path", "static_root"],
                correct_answer="static_folder",
                explanation="`app = Flask(__name__, static_folder='custom_folder')` overrides the default 'static' directory."
            ),
            QuizQuestionBlueprint(
                question="Why is adding a query parameter like `?v=1.2` (cache busting) helpful for static assets?",
                options=[
                    "It forces browsers to download the fresh asset instead of using stale browser cache.",
                    "It encrypts the stylesheet during transit.",
                    "It automatically minifies the CSS file.",
                    "It prevents ad-blockers from blocking the CSS."
                ],
                correct_answer="It forces browsers to download the fresh asset instead of using stale browser cache.",
                explanation="Changing the query string tells the browser the asset has changed, bypassing stale cache."
            ),
            QuizQuestionBlueprint(
                question="What endpoint name does Flask use internally to route static files?",
                options=["'static'", "'assets'", "'file'", "'public'"],
                correct_answer="'static'",
                explanation="The built-in endpoint name for static file handling is `'static'`."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 9
    # -------------------------------------------------------------
    DayBlueprint(
        order=9,
        title="Day 9: Custom Error Pages & Error Handlers",
        concept="Intercepting HTTP error codes like 404 and 500 with custom @app.errorhandler functions",
        analogy="Think of a custom error page like a polite concierge in a hotel. If a guest wanders into an unauthorized hallway or looks for room 999 that doesn't exist, instead of showing a scary red alarm, a friendly concierge steps in and says: 'Excuse me, that room does not exist! Let me guide you back to the lobby.'",
        theory_sections=[
            {
                "heading": "Why Custom Error Pages Matter",
                "body": "Default browser error messages (such as white screens with 'Not Found') feel broken and unprofessional. Providing brand-consistent 404 (Not Found) and 500 (Internal Server Error) pages reassures users and gives them clear links to navigate back to safety."
            },
            {
                "heading": "Using the @app.errorhandler Decorator",
                "body": "Flask allows you to register error handlers using the `@app.errorhandler(code_or_exception)` decorator. The handler function receives the exception or error object as an argument and must return both the rendered template AND the matching HTTP status code (e.g., `404`)."
            }
        ],
        code_snippets=[
            {
                "title": "Registering a Custom 404 Not Found Handler",
                "code": "from flask import Flask, render_template\n\napp = Flask(__name__)\n\n@app.errorhandler(404)\ndef page_not_found(error):\n    # IMPORTANT: Always return the 404 status code as the second argument\n    return render_template('errors/404.html'), 404"
            },
            {
                "title": "Handling Internal Server Errors (500)",
                "code": "@app.errorhandler(500)\ndef internal_server_error(error):\n    # You can log the error details to a file or monitoring service here\n    app.logger.error(f'Server Error: {error}')\n    return render_template('errors/500.html'), 500"
            },
            {
                "title": "Sample 404 Error Template (templates/errors/404.html)",
                "code": "{% extends 'base.html' %}\n\n{% block title %}404 - Page Not Found{% endblock %}\n\n{% block content %}\n<div class=\"error-box\">\n    <h1>404</h1>\n    <h2>Oops! Page Missing</h2>\n    <p>The page you requested could not be located on our servers.</p>\n    <a href=\"/\" class=\"btn btn-primary\">Return to Home</a>\n</div>\n{% endblock %}"
            },
            {
                "title": "Manually Triggering an HTTP Error with abort()",
                "code": "from flask import abort\n\n@app.route('/project/<int:project_id>')\ndef get_project(project_id):\n    if project_id > 100:\n        # Immediately halts execution and triggers the 404 error handler\n        abort(404)\n    return f'Displaying project {project_id}'"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Implement Complete Custom Error Suite",
            description="Write a Flask script defining both a 404 handler returning ('404 Page Not Found', 404) and a 403 handler returning ('403 Access Forbidden', 403).",
            starter_code="from flask import Flask, abort\n\napp = Flask(__name__)\n\n# TODO: Add 404 and 403 error handlers\n",
            solution_code="from flask import Flask, abort\n\napp = Flask(__name__)\n\n@app.errorhandler(404)\ndef handle_404(e):\n    return '404 Page Not Found', 404\n\n@app.errorhandler(403)\ndef handle_403(e):\n    return '403 Access Forbidden', 403",
            expected_output="404 Page Not Found"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What must an error handler function return along with the rendered template?",
                options=[
                    "The corresponding HTTP status code integer (e.g. 404).",
                    "A redirect to the homepage.",
                    "The user's IP address.",
                    "A cryptographic signature."
                ],
                correct_answer="The corresponding HTTP status code integer (e.g. 404).",
                explanation="If you forget to return the status code (e.g., `return render_template(...), 404`), Flask defaults to returning 200 OK."
            ),
            QuizQuestionBlueprint(
                question="Which Flask function allows you to immediately halt a request and trigger an HTTP error status code?",
                options=["abort()", "exit()", "raise_http()", "stop()"],
                correct_answer="abort()",
                explanation="`abort(404)` or `abort(403)` immediately stops route execution and invokes the corresponding error handler."
            ),
            QuizQuestionBlueprint(
                question="What does an HTTP 403 error code mean?",
                options=["Forbidden / Access Denied", "Not Found", "Internal Server Error", "Bad Gateway"],
                correct_answer="Forbidden / Access Denied",
                explanation="403 Forbidden indicates the server understands the request but refuses to authorize it."
            ),
            QuizQuestionBlueprint(
                question="What argument does a function decorated with `@app.errorhandler` always receive?",
                options=["The error or exception object.", "The database session.", "The incoming request cookies.", "The client IP address."],
                correct_answer="The error or exception object.",
                explanation="Flask passes the exception or HTTP error instance as the first parameter to the handler."
            ),
            QuizQuestionBlueprint(
                question="Why is it dangerous to display raw error tracebacks to end users on production 500 pages?",
                options=[
                    "It leaks sensitive code, database credentials, and internal directory paths to potential attackers.",
                    "It slows down the database connection.",
                    "It violates HTML5 validation rules.",
                    "It causes the web server to run out of RAM."
                ],
                correct_answer="It leaks sensitive code, database credentials, and internal directory paths to potential attackers.",
                explanation="Detailed stack traces expose implementation details and vulnerabilities to bad actors."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 10 (Project)
    # -------------------------------------------------------------
    DayBlueprint(
        order=10,
        title="Day 10: Complete Portfolio Website UI Project",
        concept="Synthesizing routing, templates, inheritance, static assets, and custom error pages into a portfolio",
        analogy="Think of building this portfolio like assembling a finished house. In Days 1-5 you laid the concrete foundation and plumbing (routing & setup). In Days 6-9 you built the walls, roof, windows, and paint (Jinja2, static CSS, error handling). Today, you furnish the entire home and open the front doors for guests!",
        theory_sections=[
            {
                "heading": "Capstone Architecture for Portfolio UI",
                "body": "This milestone project combines everything learned across Modules 1 & 2. You will structure a multi-page web application featuring a homepage, an interactive projects gallery, an about page, a contact view, and custom error handlers, all unified under a responsive `base.html` layout."
            },
            {
                "heading": "Data-Driven Template Rendering",
                "body": "Instead of hardcoding projects into HTML, the Flask view function supplies a list of project dictionaries (with title, description, tags, and URLs). Jinja2 dynamically loops over this list to render cards, demonstrating the power of server-side data presentation."
            }
        ],
        code_snippets=[
            {
                "title": "Complete Portfolio Application (app.py)",
                "code": "from flask import Flask, render_template, abort\n\napp = Flask(__name__)\n\nPROJECTS = [\n    {\n        'id': 1,\n        'title': 'AI Skill Matcher',\n        'desc': 'Smart vocational recommendation engine using TF-IDF.',\n        'tech': ['Python', 'Flask', 'PostgreSQL'],\n        'stars': 48\n    },\n    {\n        'id': 2,\n        'title': 'Solar Farm IoT Tracker',\n        'desc': 'Real-time telemetry dashboard for microgrid solar panels.',\n        'tech': ['Python', 'MQTT', 'ChartJS'],\n        'stars': 92\n    },\n    {\n        'id': 3,\n        'title': 'Hunar Cycle Mobile App',\n        'desc': 'React Native and Flask educational platform.',\n        'tech': ['React Native', 'Flask', 'Redis'],\n        'stars': 135\n    }\n]\n\n@app.route('/')\ndef index():\n    return render_template('portfolio/index.html', projects=PROJECTS)\n\n@app.route('/project/<int:project_id>')\ndef project_detail(project_id):\n    project = next((p for p in PROJECTS if p['id'] == project_id), None)\n    if not project:\n        abort(404)\n    return render_template('portfolio/detail.html', project=project)\n\n@app.errorhandler(404)\ndef not_found(e):\n    return render_template('errors/404.html'), 404"
            },
            {
                "title": "Master Layout (templates/portfolio/base.html)",
                "code": "<!DOCTYPE html>\n<html>\n<head>\n    <title>{% block title %}Developer Portfolio{% endblock %}</title>\n    <link rel=\"stylesheet\" href=\"{{ url_for('static', filename='css/portfolio.css') }}\">\n</head>\n<body>\n    <header class=\"navbar\">\n        <div class=\"brand\">Hunar<b>Dev</b></div>\n        <nav>\n            <a href=\"{{ url_for('index') }}\">Home</a>\n            <a href=\"#projects\">Projects</a>\n            <a href=\"#contact\">Contact</a>\n        </nav>\n    </header>\n    <main>\n        {% block content %}{% endblock %}\n    </main>\n    <footer>\n        <p>&copy; 2026 Crafted with Flask & Jinja2</p>\n    </footer>\n</body>\n</html>"
            },
            {
                "title": "Dynamic Projects Grid (templates/portfolio/index.html)",
                "code": "{% extends 'portfolio/base.html' %}\n\n{% block content %}\n<section class=\"hero\">\n    <h1>Full-Stack Flask Software Engineer</h1>\n    <p>Building high-performance web backends and intelligent microservices.</p>\n</section>\n\n<section id=\"projects\" class=\"grid\">\n    {% for item in projects %}\n    <div class=\"card\">\n        <h3>{{ item.title }}</h3>\n        <p>{{ item.desc }}</p>\n        <div class=\"tags\">\n            {% for t in item.tech %}<span class=\"badge\">{{ t }}</span>{% endfor %}\n        </div>\n        <a href=\"{{ url_for('project_detail', project_id=item.id) }}\" class=\"btn\">View Details &rarr;</a>\n    </div>\n    {% endfor %}\n</section>\n{% endblock %}"
            },
            {
                "title": "Minimal Portfolio Styling (static/css/portfolio.css)",
                "code": "body { margin: 0; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: #0F172A; color: #F8FAFC; }\n.navbar { display: flex; justify-content: space-between; padding: 20px 40px; background: #1E293B; border-bottom: 1px solid #334155; }\n.grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 24px; padding: 40px; }\n.card { background: #1E293B; border-radius: 16px; padding: 24px; border: 1px solid #334155; transition: transform 0.2s; }\n.card:hover { transform: translateY(-4px); border-color: #10B981; }\n.badge { background: rgba(16, 185, 129, 0.2); color: #10B981; padding: 4px 8px; border-radius: 8px; font-size: 12px; margin-right: 6px; }"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Portfolio Project Lookup by Identifier",
            description="Write a function that searches an in-memory list of projects by numeric ID and returns a formatted string 'Project: <title> (<tech_count> technologies)'. If not found, raise a ValueError('Project not found').",
            starter_code="projects = [\n    {'id': 1, 'title': 'AI Matcher', 'tech': ['Flask', 'PyTorch']},\n    {'id': 2, 'title': 'Solar IoT', 'tech': ['Python', 'MQTT', 'InfluxDB']}\n]\n\ndef lookup(pid):\n    # TODO: Implement lookup\n    pass\n",
            solution_code="projects = [\n    {'id': 1, 'title': 'AI Matcher', 'tech': ['Flask', 'PyTorch']},\n    {'id': 2, 'title': 'Solar IoT', 'tech': ['Python', 'MQTT', 'InfluxDB']}\n]\n\ndef lookup(pid):\n    match = next((p for p in projects if p['id'] == pid), None)\n    if not match:\n        raise ValueError('Project not found')\n    return f\"Project: {match['title']} ({len(match['tech'])} technologies)\"\n\nprint(lookup(1))",
            expected_output="Project: AI Matcher (2 technologies)"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Why is separating mock project data from the HTML templates considered a superior design pattern?",
                options=[
                    "It decouples data structure from presentation, allowing future migration to a database without rewriting UI.",
                    "It reduces CSS file sizes.",
                    "Because Jinja2 cannot parse strings directly.",
                    "To prevent browsers from executing JavaScript."
                ],
                correct_answer="It decouples data structure from presentation, allowing future migration to a database without rewriting UI.",
                explanation="Decoupling data from presentation adheres to the Model-View-Controller pattern."
            ),
            QuizQuestionBlueprint(
                question="In `url_for('project_detail', project_id=item.id)`, what does `'project_detail'` refer to?",
                options=[
                    "The name of the Python view function handling that route.",
                    "The HTML template file name.",
                    "The database table name.",
                    "The CSS class applied to the anchor tag."
                ],
                correct_answer="The name of the Python view function handling that route.",
                explanation="`url_for` takes the name of the target Python view function."
            ),
            QuizQuestionBlueprint(
                question="If a requested project ID does not exist in our dataset, what standard HTTP error should we raise?",
                options=["404 Not Found", "500 Internal Server Error", "401 Unauthorized", "301 Moved Permanently"],
                correct_answer="404 Not Found",
                explanation="HTTP 404 communicates that the requested resource could not be found on the server."
            ),
            QuizQuestionBlueprint(
                question="What Jinja2 loop helper provides the total count of items in the iterable?",
                options=["loop.length", "loop.total", "loop.count", "loop.size"],
                correct_answer="loop.length",
                explanation="`loop.length` gives the total number of items in the loop sequence."
            ),
            QuizQuestionBlueprint(
                question="Which CSS property creates an automatic responsive grid layout without media queries?",
                options=[
                    "grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));",
                    "display: inline-block;",
                    "flex-direction: wrap;",
                    "float: left;"
                ],
                correct_answer="grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));",
                explanation="`repeat(auto-fit, minmax(...))` creates fluid, responsive column wrapping automatically."
            )
        ],
        is_project_day=True,
        project_name="Complete Portfolio Website UI"
    ),
]
