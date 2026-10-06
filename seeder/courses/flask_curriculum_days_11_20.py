"""
Flask Mastery 40-Day Curriculum - Module 3, Module 4 & Module 5 Part 1 (Days 11 to 20)
Module 3: Forms & Data (Days 11-15)
Module 4: State Management (Days 16-18)
Module 5: Databases & ORM (Days 19-20)
"""

from seeder.course_blueprint import DayBlueprint, QuizQuestionBlueprint, CodingChallengeBlueprint

DAYS_11_TO_20 = [
    # -------------------------------------------------------------
    # DAY 11
    # -------------------------------------------------------------
    DayBlueprint(
        order=11,
        title="Day 11: The Request Object & Query Parameters",
        concept="Extracting URL query strings, form payloads, and HTTP request headers via the global request proxy",
        analogy="Think of the Flask `request` object like an envelope delivered by the postman. The outside of the envelope has the delivery address and query stamps (`request.args`), the back has metadata stickers (`request.headers`), and inside the envelope is the actual letter payload (`request.form` or `request.json`)!",
        theory_sections=[
            {
                "heading": "Context Locals and the Request Proxy",
                "body": "In Flask, `request` is a thread-safe context local object imported from `flask`. It automatically represents the specific HTTP request being processed by the current thread. You do not need to pass it as a parameter to your view function."
            },
            {
                "heading": "Query Strings vs Form Data",
                "body": "Query string parameters appear in the URL after a question mark (e.g., `/search?q=flask&page=2`). They are accessed using `request.args.get('q')`. Form body payloads submitted via POST are accessed using `request.form.get('field')`."
            }
        ],
        code_snippets=[
            {
                "title": "Parsing URL Query Parameters with request.args",
                "code": "from flask import Flask, request\n\napp = Flask(__name__)\n\n@app.route('/search')\ndef search():\n    # /search?query=python&limit=10\n    search_term = request.args.get('query', '')\n    limit = request.args.get('limit', default=10, type=int)\n    return f'Searching for \"{search_term}\" (Limit: {limit})'"
            },
            {
                "title": "Accessing Headers and Client IP",
                "code": "@app.route('/client-info')\ndef client_info():\n    user_agent = request.headers.get('User-Agent')\n    remote_ip = request.remote_addr\n    return f'Client IP: {remote_ip} | Browser: {user_agent}'"
            },
            {
                "title": "Handling Form Submissions with request.form",
                "code": "@app.route('/login', methods=['POST'])\ndef login():\n    email = request.form.get('email')\n    password = request.form.get('password')\n    return f'Attempting login for: {email}'"
            },
            {
                "title": "Using request.values for Combined Access",
                "code": "@app.route('/lookup')\ndef lookup():\n    # request.values checks both args and form\n    item_id = request.values.get('id', type=int)\n    return f'Looking up ID: {item_id}'"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Multi-Parameter Search Filter",
            description="Write a Flask route `/filter` that reads query parameters 'category' (default 'all') and 'min_price' (integer, default 0) and returns 'Filtered: <category> above $<min_price>'.",
            starter_code="from flask import Flask, request\n\napp = Flask(__name__)\n\n# TODO: Implement /filter endpoint with type validation\n",
            solution_code="from flask import Flask, request\n\napp = Flask(__name__)\n\n@app.route('/filter')\ndef filter_items():\n    cat = request.args.get('category', 'all')\n    min_p = request.args.get('min_price', default=0, type=int)\n    return f'Filtered: {cat} above ${min_p}'",
            expected_output="Filtered: tech above $50"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Which property of the `request` object parses URL query strings (e.g. `?page=2`)?",
                options=["request.args", "request.form", "request.params", "request.query"],
                correct_answer="request.args",
                explanation="`request.args` is a MultiDict holding key-value pairs parsed from the URL query string."
            ),
            QuizQuestionBlueprint(
                question="How do you parse a query parameter directly as an integer with a fallback default in Flask?",
                options=[
                    "request.args.get('page', default=1, type=int)",
                    "int(request.args['page'])",
                    "request.args.as_int('page', 1)",
                    "request.query.get_int('page')"
                ],
                correct_answer="request.args.get('page', default=1, type=int)",
                explanation="`.get(key, default=..., type=int)` automatically converts and provides fallback if absent or invalid."
            ),
            QuizQuestionBlueprint(
                question="What kind of object is `request` in Flask's runtime model?",
                options=["A thread-safe context local proxy.", "A global immutable dictionary.", "A raw TCP socket wrapper.", "A static class."],
                correct_answer="A thread-safe context local proxy.",
                explanation="Flask uses context locals so that each thread or greenlet sees only its current active request."
            ),
            QuizQuestionBlueprint(
                question="Which attribute gives the remote IP address of the client sending the request?",
                options=["request.remote_addr", "request.ip", "request.client_host", "request.headers['ip']"],
                correct_answer="request.remote_addr",
                explanation="`request.remote_addr` retrieves the client IP address from the WSGI environment."
            ),
            QuizQuestionBlueprint(
                question="What exception is raised if you access a missing key using `request.form['missing_key']`?",
                options=[
                    "BadRequestKeyError (which Flask converts to HTTP 400 Bad Request)",
                    "InternalServerError (HTTP 500)",
                    "NotFound (HTTP 404)",
                    "AttributeError"
                ],
                correct_answer="BadRequestKeyError (which Flask converts to HTTP 400 Bad Request)",
                explanation="Accessing a missing key via square brackets raises `BadRequestKeyError`, triggering a 400 response."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 12
    # -------------------------------------------------------------
    DayBlueprint(
        order=12,
        title="Day 12: Flask-WTF & Secure Form Validation",
        concept="Defining object-oriented form models with automated validation rules using WTForms",
        analogy="Think of Flask-WTF like an airport security scanner. Instead of the flight attendant manually checking every passenger's bag one by one at the gate, every passenger puts their bag through the automated scanner. If a required item is missing or an invalid item is found, the scanner beeps immediately with a clear error message!",
        theory_sections=[
            {
                "heading": "Why Use Flask-WTF Over Raw HTML Forms?",
                "body": "Parsing raw `request.form` dictionaries requires writing tedious manual validation code (e.g. checking length, valid email syntax, passwords matching). Flask-WTF integrates the powerful WTForms library with Flask, providing clean Python form classes with built-in declarative validators."
            },
            {
                "heading": "Form Classes and Built-in Validators",
                "body": "You inherit from `FlaskForm` and define fields using classes like `StringField`, `PasswordField`, and `SubmitField`. Each field takes a list of validators like `DataRequired()`, `Email()`, `Length(min=6)`, or `EqualTo()`. In your route, `form.validate_on_submit()` executes all checks automatically on POST."
            }
        ],
        code_snippets=[
            {
                "title": "Defining a Secure Registration Form",
                "code": "from flask_wtf import FlaskForm\nfrom wtforms import StringField, PasswordField, SubmitField\nfrom wtforms.validators import DataRequired, Email, Length, EqualTo\n\nclass RegistrationForm(FlaskForm):\n    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=25)])\n    email = StringField('Email Address', validators=[DataRequired(), Email()])\n    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])\n    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message='Passwords must match')])\n    submit = SubmitField('Sign Up')"
            },
            {
                "title": "Handling Form Validation in the Route",
                "code": "from flask import Flask, render_template, redirect, url_for\n\napp = Flask(__name__)\napp.config['SECRET_KEY'] = 'dev-super-secret-key'\n\n@app.route('/register', methods=['GET', 'POST'])\ndef register():\n    form = RegistrationForm()\n    if form.validate_on_submit():\n        # Access clean, validated data\n        username = form.username.data\n        email = form.email.data\n        print(f'Creating user: {username} ({email})')\n        return redirect(url_for('login'))\n    return render_template('register.html', form=form)"
            },
            {
                "title": "Rendering the Form in Jinja2 with Error Displays",
                "code": "<!-- templates/register.html -->\n<form method=\"POST\">\n    {{ form.hidden_tag() }} <!-- Renders CSRF token -->\n    \n    <div>\n        {{ form.username.label }}\n        {{ form.username(class=\"form-control\") }}\n        {% for error in form.username.errors %}\n            <span class=\"error-text\">{{ error }}</span>\n        {% endfor %}\n    </div>\n    \n    {{ form.submit(class=\"btn btn-primary\") }}\n</form>"
            },
            {
                "title": "Creating Custom WTForms Validators",
                "code": "from wtforms.validators import ValidationError\n\ndef validate_no_admin(form, field):\n    if 'admin' in field.data.lower():\n        raise ValidationError('Username cannot contain \"admin\".')"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Contact Inquiry Form Model",
            description="Create a FlaskForm class named 'InquiryForm' with fields: 'name' (DataRequired), 'email' (DataRequired, Email), 'message' (DataRequired, Length max=500), and a SubmitField.",
            starter_code="from flask_wtf import FlaskForm\nfrom wtforms import StringField, TextAreaField, SubmitField\nfrom wtforms.validators import DataRequired, Email, Length\n\n# TODO: Define InquiryForm\n",
            solution_code="from flask_wtf import FlaskForm\nfrom wtforms import StringField, TextAreaField, SubmitField\nfrom wtforms.validators import DataRequired, Email, Length\n\nclass InquiryForm(FlaskForm):\n    name = StringField('Full Name', validators=[DataRequired()])\n    email = StringField('Email Address', validators=[DataRequired(), Email()])\n    message = TextAreaField('Your Message', validators=[DataRequired(), Length(max=500)])\n    submit = SubmitField('Send Inquiry')",
            expected_output="InquiryForm defined with 4 fields"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What method on a FlaskForm instance combines checking request method POST and running all validators?",
                options=["form.validate_on_submit()", "form.is_valid()", "form.check_all()", "form.verify()"],
                correct_answer="form.validate_on_submit()",
                explanation="`form.validate_on_submit()` returns True only if the request is POST and all field validators pass."
            ),
            QuizQuestionBlueprint(
                question="What configuration key is strictly required in `app.config` for Flask-WTF to generate CSRF tokens?",
                options=["SECRET_KEY", "WTF_KEY", "CSRF_TOKEN", "SECURITY_PASSWORD_SALT"],
                correct_answer="SECRET_KEY",
                explanation="Flask-WTF requires `app.config['SECRET_KEY']` to cryptographically sign session CSRF tokens."
            ),
            QuizQuestionBlueprint(
                question="What does `{{ form.hidden_tag() }}` render inside an HTML form?",
                options=[
                    "A hidden `<input>` field containing the CSRF protection token.",
                    "All hidden password fields.",
                    "An invisible Google Analytics tracking script.",
                    "A cryptographic watermark image."
                ],
                correct_answer="A hidden `<input>` field containing the CSRF protection token.",
                explanation="`form.hidden_tag()` renders hidden inputs, most notably the CSRF token input."
            ),
            QuizQuestionBlueprint(
                question="Which WTForms validator ensures two password input fields match identically?",
                options=["EqualTo('password')", "Matches('password')", "SameAs('password')", "Identical('password')"],
                correct_answer="EqualTo('password')",
                explanation="`EqualTo('field_name')` compares the current field value against another named field."
            ),
            QuizQuestionBlueprint(
                question="Where are validation error messages stored for a specific field after a failed submission?",
                options=["form.field_name.errors", "form.errors_list", "request.form.errors", "session['errors']"],
                correct_answer="form.field_name.errors",
                explanation="Each field has an `.errors` list containing the validation failure messages."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 13
    # -------------------------------------------------------------
    DayBlueprint(
        order=13,
        title="Day 13: CSRF Protection & Flash Messaging",
        concept="Defending against Cross-Site Request Forgery and conveying transient status feedback via flash()",
        analogy="Think of CSRF protection like a secret handshake between the bank teller and you. Even if a thief steals your written check, without knowing the unique secret daily handshake, the bank refuses the transaction! Flash messages are like sticky notes: the teller hands you a note saying 'Deposit complete!', and the moment you read it, you throw it away!",
        theory_sections=[
            {
                "heading": "Understanding Cross-Site Request Forgery (CSRF)",
                "body": "CSRF is a severe web vulnerability where a malicious site tricks a logged-in user's browser into executing unwanted actions on a trusted site. Flask-WTF stops this by issuing a cryptographically signed one-time token stored in the user's session and verifying that every POST request submits this exact matching token."
            },
            {
                "heading": "Flash Messaging with Categories",
                "body": "When a user submits a form or performs an action, you frequently need to redirect them to another page while showing a one-time message (e.g. 'Password updated successfully'). Flask's `flash(message, category)` stores the message in the session and removes it the moment `get_flashed_messages()` reads it."
            }
        ],
        code_snippets=[
            {
                "title": "Triggering Flash Messages with Categories",
                "code": "from flask import Flask, flash, redirect, url_for, render_template\n\napp = Flask(__name__)\napp.config['SECRET_KEY'] = 'secure-key-123'\n\n@app.route('/update-profile', methods=['POST'])\ndef update_profile():\n    # Trigger flash message with semantic category\n    flash('Your profile changes have been saved!', 'success')\n    return redirect(url_for('dashboard'))\n\n@app.route('/delete-account', methods=['POST'])\ndef delete_account():\n    flash('Danger: Account scheduled for permanent deletion.', 'danger')\n    return redirect(url_for('home'))"
            },
            {
                "title": "Rendering Flashed Messages in base.html",
                "code": "<!-- templates/base.html -->\n<div class=\"flash-container\">\n    {% with messages = get_flashed_messages(with_categories=true) %}\n        {% if messages %}\n            {% for category, message in messages %}\n                <div class=\"alert alert-{{ category }}\">\n                    <span>{{ message }}</span>\n                </div>\n            {% endfor %}\n        {% endif %}\n    {% endwith %}\n</div>"
            },
            {
                "title": "Enabling Global CSRFProtect for Non-WTForms Endpoints",
                "code": "from flask_wtf.csrf import CSRFProtect\n\n# Enables CSRF protection globally for AJAX and standard forms\ncsrf = CSRFProtect(app)"
            },
            {
                "title": "Exempting Specific Webhook Routes from CSRF",
                "code": "@app.route('/stripe-webhook', methods=['POST'])\n@csrf.exempt\ndef stripe_webhook():\n    # External third-party payment webhooks cannot send our CSRF token\n    return 'Webhook received', 200"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Categorized Flash System Implementation",
            description="Write a Python route `/auth/test` that flashes an error message 'Invalid credentials' under category 'danger' and redirects to '/login'.",
            starter_code="from flask import Flask, flash, redirect, url_for\n\napp = Flask(__name__)\napp.config['SECRET_KEY'] = 'test-key'\n\n# TODO: Implement route flashing 'Invalid credentials' with category 'danger'\n",
            solution_code="from flask import Flask, flash, redirect, url_for\n\napp = Flask(__name__)\napp.config['SECRET_KEY'] = 'test-key'\n\n@app.route('/auth/test')\ndef test_auth():\n    flash('Invalid credentials', 'danger')\n    return redirect(url_for('login'))",
            expected_output="Flash message recorded in session"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What attack does CSRF (Cross-Site Request Forgery) protection prevent?",
                options=[
                    "Malicious websites forging unauthorized HTTP requests using an authenticated user's credentials.",
                    "Direct SQL injection into database columns.",
                    "Distributed Denial of Service (DDoS) traffic spikes.",
                    "Intercepting raw WiFi packets."
                ],
                correct_answer="Malicious websites forging unauthorized HTTP requests using an authenticated user's credentials.",
                explanation="CSRF tricks a user's browser into executing authenticated commands without their knowledge."
            ),
            QuizQuestionBlueprint(
                question="How do you retrieve flashed messages along with their assigned category in Jinja2?",
                options=[
                    "get_flashed_messages(with_categories=true)",
                    "get_messages(categories=True)",
                    "session.get_flashes()",
                    "request.flashes"
                ],
                correct_answer="get_flashed_messages(with_categories=true)",
                explanation="`with_categories=true` returns tuples of `(category, message)` for styling alerts."
            ),
            QuizQuestionBlueprint(
                question="Where are flashed messages temporarily stored until rendered in the browser?",
                options=["In the client's cryptographically signed session cookie.", "In the PostgreSQL database.", "In a temporary local text file.", "In browser local storage."],
                correct_answer="In the client's cryptographically signed session cookie.",
                explanation="Flask stores flashed messages inside the session cookie until accessed."
            ),
            QuizQuestionBlueprint(
                question="What decorator exempts a specific endpoint (like an external API webhook) from CSRF verification?",
                options=["@csrf.exempt", "@no_csrf", "@allow_external", "@csrf.disable"],
                correct_answer="@csrf.exempt",
                explanation="`@csrf.exempt` tells Flask-WTF not to enforce CSRF tokens on that view."
            ),
            QuizQuestionBlueprint(
                question="What happens to flashed messages after `get_flashed_messages()` is executed?",
                options=[
                    "They are immediately cleared and removed from the session.",
                    "They remain permanently in the session.",
                    "They are saved to the server log.",
                    "They expire after exactly 24 hours."
                ],
                correct_answer="They are immediately cleared and removed from the session.",
                explanation="Flashed messages are designed to be ephemeral and are purged once consumed."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 14
    # -------------------------------------------------------------
    DayBlueprint(
        order=14,
        title="Day 14: Secure File Uploads & Filename Sanitization",
        concept="Uploading client files safely using multipart/form-data, werkzeug.utils.secure_filename, and size limits",
        analogy="Think of handling file uploads like receiving packages at a high-security embassy. You cannot let someone walk in with an unmarked wooden box named '../../../../etc/passwd'. The security guards inspect the box, verify the extension (is it really a PDF?), sanitize the label so it cannot break through walls, and limit the weight to under 10 megabytes!",
        theory_sections=[
            {
                "heading": "The Multipart Form Requirement",
                "body": "Standard HTML forms encode data as text. When uploading binary files (images, PDFs), the HTML `<form>` tag must explicitly declare `enctype=\"multipart/form-data\"`. In Flask, uploaded files are accessed via `request.files['input_name']` as `FileStorage` objects."
            },
            {
                "heading": "Critical Security: Path Traversal & Allowed Extensions",
                "body": "Never trust a filename provided by the client. An attacker could name a file `../../app.py` to overwrite your server's source code! Always pass the filename through Werkzeug's `secure_filename()` function and strictly validate against a whitelist of permitted extensions (e.g. png, jpg, pdf)."
            }
        ],
        code_snippets=[
            {
                "title": "Configuring Upload Folder & Maximum File Size",
                "code": "import os\nfrom flask import Flask\n\napp = Flask(__name__)\n\nUPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')\nos.makedirs(UPLOAD_FOLDER, exist_ok=True)\n\napp.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER\n# Restrict maximum upload size to 16 Megabytes (returns 413 if exceeded)\napp.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024"
            },
            {
                "title": "Extension Whitelist Verification Helper",
                "code": "ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'pdf'}\n\ndef allowed_file(filename):\n    return '.' in filename and \\\n           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS"
            },
            {
                "title": "Saving Uploaded File with secure_filename",
                "code": "from flask import request, flash, redirect, url_for\nfrom werkzeug.utils import secure_filename\nimport os\n\n@app.route('/upload', methods=['POST'])\ndef upload_file():\n    if 'document' not in request.files:\n        flash('No file part selected', 'danger')\n        return redirect(request.url)\n    \n    file = request.files['document']\n    if file.filename == '':\n        flash('No file selected', 'danger')\n        return redirect(request.url)\n        \n    if file and allowed_file(file.filename):\n        filename = secure_filename(file.filename)\n        save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)\n        file.save(save_path)\n        flash(f'File {filename} successfully uploaded!', 'success')\n        return redirect(url_for('home'))\n    \n    flash('File type not allowed', 'danger')\n    return redirect(request.url)"
            },
            {
                "title": "HTML File Upload Form Syntax",
                "code": "<!-- templates/upload.html -->\n<form method=\"POST\" enctype=\"multipart/form-data\">\n    <input type=\"file\" name=\"document\" accept=\".png,.jpg,.pdf\">\n    <button type=\"submit\">Upload Document</button>\n</form>"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Safe File Extension Checker",
            description="Write a Python function `sanitize_and_validate(filename, allowed_set)` that returns the sanitized filename using secure_filename if valid, or raises ValueError('Invalid file type') if the extension is not in allowed_set.",
            starter_code="from werkzeug.utils import secure_filename\n\ndef sanitize_and_validate(filename, allowed_set):\n    # TODO: Implement sanitization and extension check\n    pass\n",
            solution_code="from werkzeug.utils import secure_filename\n\ndef sanitize_and_validate(filename, allowed_set):\n    if '.' not in filename:\n        raise ValueError('Invalid file type')\n    ext = filename.rsplit('.', 1)[1].lower()\n    if ext not in allowed_set:\n        raise ValueError('Invalid file type')\n    return secure_filename(filename)\n\nprint(sanitize_and_validate('../My Resume (2026).pdf', {'pdf', 'docx'}))",
            expected_output="My_Resume_2026.pdf"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What HTML form attribute is strictly required for file uploads to transmit binary data?",
                options=["enctype=\"multipart/form-data\"", "method=\"FILE\"", "type=\"binary\"", "upload=\"true\""],
                correct_answer="enctype=\"multipart/form-data\"",
                explanation="Without `enctype=\"multipart/form-data\"`, browsers transmit only the filename string, not binary bytes."
            ),
            QuizQuestionBlueprint(
                question="Why is `secure_filename()` from Werkzeug critical when saving uploaded files to disk?",
                options=[
                    "It strips directory traversal sequences like `../../` that could overwrite system files.",
                    "It scans the file for computer viruses.",
                    "It compresses the image to reduce disk space.",
                    "It encrypts the file on disk with AES-256."
                ],
                correct_answer="It strips directory traversal sequences like `../../` that could overwrite system files.",
                explanation="`secure_filename` prevents path traversal attacks by sanitizing rogue slashes and parent directory tokens."
            ),
            QuizQuestionBlueprint(
                question="What configuration parameter limits the maximum payload size accepted by Flask?",
                options=["MAX_CONTENT_LENGTH", "MAX_FILE_SIZE", "UPLOAD_LIMIT", "CLIENT_MAX_BODY"],
                correct_answer="MAX_CONTENT_LENGTH",
                explanation="`app.config['MAX_CONTENT_LENGTH']` rejects requests larger than the specified byte limit with HTTP 413."
            ),
            QuizQuestionBlueprint(
                question="What HTTP status code does Flask return if an upload exceeds `MAX_CONTENT_LENGTH`?",
                options=["413 Payload Too Large", "400 Bad Request", "404 Not Found", "500 Internal Server Error"],
                correct_answer="413 Payload Too Large",
                explanation="HTTP 413 Payload Too Large explicitly informs the client the payload exceeded server boundaries."
            ),
            QuizQuestionBlueprint(
                question="Where are uploaded files accessed on Flask's `request` object?",
                options=["request.files", "request.form", "request.attachments", "request.data"],
                correct_answer="request.files",
                explanation="`request.files` is an ImmutableMultiDict containing `FileStorage` objects for uploaded files."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 15 (Project)
    # -------------------------------------------------------------
    DayBlueprint(
        order=15,
        title="Day 15: Secure Contact & Resume Upload Form Project",
        concept="Engineering an end-to-end recruitment contact portal with Flask-WTF, CSRF, flash feedback, and safe file uploads",
        analogy="Think of this project like a digital job application kiosk at corporate headquarters. Applicants walk up, enter their verified name and email, upload their resume PDF, and submit. The kiosk inspects every field, stamps an anti-tamper security seal (CSRF), scans the resume for safety, and shows a green confirmation banner!",
        theory_sections=[
            {
                "heading": "Recruitment Portal Architecture",
                "body": "In this project, you unify all concepts from Module 3: building an object-oriented `JobApplicationForm` using Flask-WTF, integrating `FileField` with extension validation, securing the transaction with CSRF tokens, saving candidate resumes safely, and flashing feedback."
            },
            {
                "heading": "Integrating FileField in WTForms",
                "body": "Flask-WTF provides `flask_wtf.file.FileField` and `FileAllowed` validators. This lets you enforce file constraints declaratively within your form class alongside text validators."
            }
        ],
        code_snippets=[
            {
                "title": "Recruitment Form Model (forms.py)",
                "code": "from flask_wtf import FlaskForm\nfrom flask_wtf.file import FileField, FileAllowed, FileRequired\nfrom wtforms import StringField, TextAreaField, SubmitField\nfrom wtforms.validators import DataRequired, Email, Length\n\nclass JobApplicationForm(FlaskForm):\n    full_name = StringField('Full Name', validators=[DataRequired(), Length(min=3, max=60)])\n    email = StringField('Email Address', validators=[DataRequired(), Email()])\n    position = StringField('Target Role', validators=[DataRequired()])\n    cover_letter = TextAreaField('Cover Note', validators=[DataRequired(), Length(min=20, max=1000)])\n    resume = FileField('Resume (PDF only)', validators=[\n        FileRequired(),\n        FileAllowed(['pdf'], 'Only PDF documents are accepted!')\n    ])\n    submit = SubmitField('Submit Application')"
            },
            {
                "title": "Application Route Controller (app.py)",
                "code": "import os\nfrom flask import Flask, render_template, redirect, url_for, flash\nfrom werkzeug.utils import secure_filename\nfrom forms import JobApplicationForm\n\napp = Flask(__name__)\napp.config['SECRET_KEY'] = 'enterprise-career-portal-secret'\napp.config['UPLOAD_FOLDER'] = 'uploads/resumes'\napp.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024 # 5 MB\n\nos.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)\n\n@app.route('/apply', methods=['GET', 'POST'])\ndef apply_job():\n    form = JobApplicationForm()\n    if form.validate_on_submit():\n        f = form.resume.data\n        safe_name = secure_filename(f'{form.full_name.data}_{f.filename}')\n        save_destination = os.path.join(app.config['UPLOAD_FOLDER'], safe_name)\n        f.save(save_destination)\n        \n        flash(f'Thank you, {form.full_name.data}! Your application for {form.position.data} was submitted.', 'success')\n        return redirect(url_for('apply_job'))\n    return render_template('apply.html', form=form)"
            },
            {
                "title": "Recruitment Template (templates/apply.html)",
                "code": "{% extends 'base.html' %}\n\n{% block content %}\n<div class=\"form-card\">\n    <h2>Join the Hunar Cycle Team</h2>\n    <form method=\"POST\" enctype=\"multipart/form-data\">\n        {{ form.hidden_tag() }}\n        \n        <div class=\"form-group\">\n            {{ form.full_name.label }}\n            {{ form.full_name(class=\"input-field\") }}\n            {% for err in form.full_name.errors %}<span class=\"error\">{{ err }}</span>{% endfor %}\n        </div>\n        \n        <div class=\"form-group\">\n            {{ form.email.label }}\n            {{ form.email(class=\"input-field\") }}\n            {% for err in form.email.errors %}<span class=\"error\">{{ err }}</span>{% endfor %}\n        </div>\n        \n        <div class=\"form-group\">\n            {{ form.resume.label }}\n            {{ form.resume() }}\n            {% for err in form.resume.errors %}<span class=\"error\">{{ err }}</span>{% endfor %}\n        </div>\n        \n        {{ form.submit(class=\"btn-submit\") }}\n    </form>\n</div>\n{% endblock %}"
            },
            {
                "title": "Handling Max Size Upload Exceptions",
                "code": "@app.errorhandler(413)\ndef request_entity_too_large(error):\n    flash('File upload exceeded the 5MB size limit.', 'danger')\n    return redirect(url_for('apply_job')), 413"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Candidate Resume Storage Directory Generator",
            description="Write a function that generates a sanitized destination path for candidate resume files in format '<candidate_name>_<sanitized_filename>' inside a base folder.",
            starter_code="import os\nfrom werkzeug.utils import secure_filename\n\ndef build_candidate_path(base_folder, candidate, raw_filename):\n    # TODO: Build safe path\n    pass\n",
            solution_code="import os\nfrom werkzeug.utils import secure_filename\n\ndef build_candidate_path(base_folder, candidate, raw_filename):\n    safe_cand = secure_filename(candidate).lower()\n    safe_file = secure_filename(raw_filename)\n    final_filename = f'{safe_cand}_{safe_file}'\n    return os.path.join(base_folder, final_filename)\n\nprint(build_candidate_path('/var/uploads', 'Ali Raza', 'My Resume 2026.pdf'))",
            expected_output="/var/uploads\\ali_raza_My_Resume_2026.pdf"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Which validator from `flask_wtf.file` ensures that the user cannot submit without selecting a file?",
                options=["FileRequired()", "DataPresent()", "MustHaveFile()", "FileNotNull()"],
                correct_answer="FileRequired()",
                explanation="`FileRequired()` verifies that an actual file payload is attached to the request."
            ),
            QuizQuestionBlueprint(
                question="What validator from `flask_wtf.file` restricts accepted upload files to specific extensions like `['pdf', 'docx']`?",
                options=["FileAllowed()", "ExtensionCheck()", "FileFilter()", "AcceptExtensions()"],
                correct_answer="FileAllowed()",
                explanation="`FileAllowed(['pdf', 'docx'], 'Error message')` enforces permitted file extensions."
            ),
            QuizQuestionBlueprint(
                question="Why is it beneficial to prepend the applicant's name or a unique UUID to an uploaded filename?",
                options=[
                    "To prevent applicants with identical filenames (e.g. 'resume.pdf') from overwriting each other's files.",
                    "Because Linux filesystems cannot store files named 'resume.pdf'.",
                    "To speed up database indexing.",
                    "It enables browser PDF preview."
                ],
                correct_answer="To prevent applicants with identical filenames (e.g. 'resume.pdf') from overwriting each other's files.",
                explanation="Namespacing files avoids collision and accidental overwriting of documents."
            ),
            QuizQuestionBlueprint(
                question="If a user attempts to upload a 50MB video to our 5MB-limited portal, what happens?",
                options=[
                    "The web server drops the connection and returns HTTP 413 Payload Too Large.",
                    "The video is silently truncated to the first 5MB.",
                    "The server crashes due to Out of Memory.",
                    "The file is converted into a PDF automatically."
                ],
                correct_answer="The web server drops the connection and returns HTTP 413 Payload Too Large.",
                explanation="`MAX_CONTENT_LENGTH` aborts the request with status 413 once the threshold is crossed."
            ),
            QuizQuestionBlueprint(
                question="What must be included inside the HTML `<form>` when using Flask-WTF to prevent Cross-Site Request Forgery?",
                options=["{{ form.hidden_tag() }}", "{{ form.csrf_token() }}", "Both of the above are valid", "None of the above"],
                correct_answer="Both of the above are valid",
                explanation="`{{ form.hidden_tag() }}` renders all hidden fields including the CSRF token; `{{ form.csrf_token }}` renders just the token."
            )
        ],
        is_project_day=True,
        project_name="Secure Contact & Resume Upload Form"
    ),

    # -------------------------------------------------------------
    # DAY 16
    # -------------------------------------------------------------
    DayBlueprint(
        order=16,
        title="Day 16: Client-Side Cookies (Set, Read, Expire)",
        concept="Reading and setting HTTP cookies using make_response, response.set_cookie, and request.cookies",
        analogy="Think of an HTTP cookie like a wristband stamped on your arm at an amusement park. The park gate attendant (the server) stamps the date and your favorite rollercoaster color on your wristband. Every time you step onto a ride, the operator looks at your wristband (`request.cookies`) to know who you are without asking you for your ticket again!",
        theory_sections=[
            {
                "heading": "The Stateless Nature of HTTP and Cookies",
                "body": "HTTP is inherently stateless: every request is treated as independent with no memory of prior interactions. Cookies are small key-value strings stored by the client's browser and sent automatically in the `Cookie` header on every subsequent request to that domain."
            },
            {
                "heading": "Setting and Reading Cookies in Flask",
                "body": "To set a cookie, you create a Response object using `make_response()`, call `response.set_cookie(key, value, max_age, httponly=True, secure=True)`, and return it. To read a cookie, inspect `request.cookies.get(key)`. To delete a cookie, set its expiration date to the past using `response.delete_cookie(key)`."
            }
        ],
        code_snippets=[
            {
                "title": "Setting a Cookie on an Outgoing Response",
                "code": "from flask import Flask, make_response, request\n\napp = Flask(__name__)\n\n@app.route('/set-cookie')\ndef set_cookie():\n    resp = make_response('Cookie has been set!')\n    # Set cookie lasting 7 days (7 * 24 * 60 * 60 seconds)\n    resp.set_cookie('theme', 'dark', max_age=604800, httponly=True)\n    return resp"
            },
            {
                "title": "Reading an Incoming Cookie",
                "code": "@app.route('/get-cookie')\ndef get_cookie():\n    # Retrieve theme cookie with 'light' as fallback default\n    user_theme = request.cookies.get('theme', 'light')\n    return f'Current preferred theme: {user_theme}'"
            },
            {
                "title": "Deleting a Cookie",
                "code": "@app.route('/clear-cookie')\ndef clear_cookie():\n    resp = make_response('Theme preference reset to default.')\n    resp.delete_cookie('theme')\n    return resp"
            },
            {
                "title": "Security Flags: HttpOnly and Secure",
                "code": "# httponly=True blocks JavaScript access (mitigates XSS cookie theft)\n# secure=True ensures cookie is only transmitted over HTTPS\nresp.set_cookie('auth_token', 'xyz123', httponly=True, secure=True, samesite='Lax')"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="User Locale Cookie Manager",
            description="Create two Flask routes: `/set-lang/<lang_code>` which sets a cookie 'lang' with max_age=86400, and `/get-lang` which returns 'Language: <lang>' or 'Language: en' if unset.",
            starter_code="from flask import Flask, make_response, request\n\napp = Flask(__name__)\n\n# TODO: Implement /set-lang/<lang_code> and /get-lang\n",
            solution_code="from flask import Flask, make_response, request\n\napp = Flask(__name__)\n\n@app.route('/set-lang/<lang_code>')\ndef set_lang(lang_code):\n    resp = make_response(f'Language set to {lang_code}')\n    resp.set_cookie('lang', lang_code, max_age=86400)\n    return resp\n\n@app.route('/get-lang')\ndef get_lang():\n    selected = request.cookies.get('lang', 'en')\n    return f'Language: {selected}'",
            expected_output="Language: ur"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Why can you not set a cookie directly on a raw returned string in Flask?",
                options=[
                    "Cookies must be attached to an HTTP Response object via `make_response()`.",
                    "Because strings cannot carry HTTP headers.",
                    "Flask only supports cookies in JSON format.",
                    "Strings are immutable in Python."
                ],
                correct_answer="Cookies must be attached to an HTTP Response object via `make_response()`.",
                explanation="`set_cookie` is a method on the `Response` object, requiring `make_response('content')`."
            ),
            QuizQuestionBlueprint(
                question="What security protection does the `httponly=True` cookie flag provide?",
                options=[
                    "Prevents client-side JavaScript (e.g. document.cookie) from accessing the cookie, mitigating XSS attacks.",
                    "Forces the cookie to be encrypted with SSL.",
                    "Deletes the cookie when the browser closes.",
                    "Only allows requests from mobile devices."
                ],
                correct_answer="Prevents client-side JavaScript (e.g. document.cookie) from accessing the cookie, mitigating XSS attacks.",
                explanation="HttpOnly prevents malicious scripts from stealing sensitive tokens via Cross-Site Scripting."
            ),
            QuizQuestionBlueprint(
                question="What parameter specifies cookie lifetime in seconds?",
                options=["max_age", "expires_in", "duration", "timeout"],
                correct_answer="max_age",
                explanation="`max_age` defines cookie expiration as an integer count of seconds from the moment set."
            ),
            QuizQuestionBlueprint(
                question="Where are incoming cookies retrieved on the Flask `request` object?",
                options=["request.cookies", "request.headers['Cookies']", "request.args", "request.session"],
                correct_answer="request.cookies",
                explanation="`request.cookies` is a dictionary-like MultiDict containing all cookies sent by the client."
            ),
            QuizQuestionBlueprint(
                question="How does `response.delete_cookie('name')` actually delete a cookie from the user's browser?",
                options=[
                    "It sends a Set-Cookie header with an expiration date in the past and empty value.",
                    "It sends a remote terminal command to delete the local cookie file.",
                    "It tells the browser to purge all cookies on the device.",
                    "It invalidates the server DNS."
                ],
                correct_answer="It sends a Set-Cookie header with an expiration date in the past and empty value.",
                explanation="Browsers automatically discard cookies whose expiration dates are set to the past."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 17
    # -------------------------------------------------------------
    DayBlueprint(
        order=17,
        title="Day 17: Flask Sessions & Cryptographic Signing",
        concept="Storing secure, tamper-proof user state across requests using Flask's signed session object",
        analogy="Think of a Flask session cookie like a signed wax seal on a royal letter. Anyone can look through the glass window and see what is written inside, but if anyone tries to scratch off the text or alter their user_id, the royal wax seal is broken, and the server rejects it as forged!",
        theory_sections=[
            {
                "heading": "Client-Side Cryptographically Signed Sessions",
                "body": "Unlike cookies that can be freely edited by users in their browser developer tools, Flask's `session` object is cryptographically signed using your `SECRET_KEY`. Users can view the payload, but any unauthorized tampering invalidates the signature, causing Flask to reject the session."
            },
            {
                "heading": "Working with the session Dictionary",
                "body": "In Flask, `session` behaves like a standard Python dictionary. You store values using `session['user_id'] = 42` and retrieve them with `session.get('user_id')`. To remove data, use `session.pop('user_id', None)` or `session.clear()` to log the user out."
            }
        ],
        code_snippets=[
            {
                "title": "Setting and Reading Session Data",
                "code": "from flask import Flask, session, redirect, url_for\n\napp = Flask(__name__)\napp.config['SECRET_KEY'] = 'strong-random-secret-key'\n\n@app.route('/login')\ndef login():\n    # Store user identity in signed session\n    session['user_id'] = 101\n    session['username'] = 'zubair_dev'\n    return 'User session established.'\n\n@app.route('/profile')\ndef profile():\n    user_id = session.get('user_id')\n    if not user_id:\n        return redirect(url_for('login'))\n    return f'Welcome back {session.get(\"username\")} (ID: {user_id})'"
            },
            {
                "title": "Logging Out and Purging Session",
                "code": "@app.route('/logout')\ndef logout():\n    # Clear all data stored in session\n    session.clear()\n    return 'Successfully logged out.'"
            },
            {
                "title": "Permanent Sessions and Custom Lifetime",
                "code": "from datetime import timedelta\n\n# Configure session to expire after 30 days of inactivity\napp.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=30)\n\n@app.route('/remember-me')\ndef remember():\n    session.permanent = True\n    session['user_id'] = 101\n    return 'Session marked as permanent!'"
            },
            {
                "title": "Modifying Mutable Objects in Session",
                "code": "@app.route('/add-cart-item/<item>')\ndef add_to_cart(item):\n    if 'cart' not in session:\n        session['cart'] = []\n    # If modifying a list or dict in-place, inform Flask of the change\n    session['cart'].append(item)\n    session.modified = True\n    return f'Cart items: {session[\"cart\"]}'"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Page Visit Counter via Session",
            description="Write a Flask route `/counter` that uses `session` to track how many times a user has loaded the page, incrementing on each visit and returning 'You have visited this page <count> times'.",
            starter_code="from flask import Flask, session\n\napp = Flask(__name__)\napp.config['SECRET_KEY'] = 'dev-key'\n\n# TODO: Implement visit counter\n",
            solution_code="from flask import Flask, session\n\napp = Flask(__name__)\napp.config['SECRET_KEY'] = 'dev-key'\n\n@app.route('/counter')\ndef counter():\n    visits = session.get('visits', 0) + 1\n    session['visits'] = visits\n    return f'You have visited this page {visits} times'",
            expected_output="You have visited this page 1 times"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What protects standard Flask client-side sessions from being modified by users?",
                options=[
                    "A cryptographic HMAC signature computed using `app.config['SECRET_KEY']`.",
                    "Flask sessions are stored in an encrypted SQLite database on the client.",
                    "Browser developer tools cannot view cookies.",
                    "Operating system hardware sandboxing."
                ],
                correct_answer="A cryptographic HMAC signature computed using `app.config['SECRET_KEY']`.",
                explanation="Flask signs session cookies using HMAC SHA-1/256 with the app's secret key to prevent tampering."
            ),
            QuizQuestionBlueprint(
                question="Are standard Flask cookie sessions encrypted by default?",
                options=[
                    "No, they are signed (tamper-proof) but readable in base64 plaintext unless explicitly encrypted.",
                    "Yes, they are encrypted with RSA-4096 by default.",
                    "Yes, using AES-256.",
                    "No, they are stored on the server's hard drive."
                ],
                correct_answer="No, they are signed (tamper-proof) but readable in base64 plaintext unless explicitly encrypted.",
                explanation="Standard Flask sessions are signed, not encrypted. Never store raw passwords or sensitive secrets in them!"
            ),
            QuizQuestionBlueprint(
                question="Why is `session.modified = True` required when appending items to a list in `session['cart']`?",
                options=[
                    "Flask cannot automatically detect in-place mutations inside nested objects.",
                    "To increment the session version number.",
                    "Because lists cannot be JSON serialized.",
                    "To prevent database lock timeouts."
                ],
                correct_answer="Flask cannot automatically detect in-place mutations inside nested objects.",
                explanation="Modifying a mutable structure (like appending to a list) doesn't reassign the key, so `modified = True` signals Flask to save it."
            ),
            QuizQuestionBlueprint(
                question="How do you completely remove all keys and values from the current session?",
                options=["session.clear()", "session.delete()", "del session", "session.reset()"],
                correct_answer="session.clear()",
                explanation="`session.clear()` empties all session key-value pairs."
            ),
            QuizQuestionBlueprint(
                question="What configuration parameter controls the lifetime duration of permanent sessions?",
                options=["PERMANENT_SESSION_LIFETIME", "SESSION_TIMEOUT", "COOKIE_EXPIRES", "SESSION_MAX_AGE"],
                correct_answer="PERMANENT_SESSION_LIFETIME",
                explanation="`app.config['PERMANENT_SESSION_LIFETIME']` takes a `datetime.timedelta` object defining session validity."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 18 (Project)
    # -------------------------------------------------------------
    DayBlueprint(
        order=18,
        title="Day 18: Dark Mode Preference & Remember Me System Project",
        concept="Building a production-grade state management system combining cookies for preferences and sessions for persistent auth",
        analogy="Think of this system like a smart hotel room key card. The key card holds your room access permissions (session authentication with remember-me duration). Meanwhile, the thermostat on the wall remembers whether you prefer the room cool or warm (cookie preference) so your settings remain even if you step outside!",
        theory_sections=[
            {
                "heading": "State Management Synthesis",
                "body": "In this project, you build an integrated state management layer for web applications: client-side cookies for non-sensitive UI settings (like Light/Dark mode themes) that persist without requiring user login, and secure sessions with a configurable 'Remember Me' toggle that extends session life to 30 days."
            },
            {
                "heading": "Context Processors for Global Theme Injection",
                "body": "Instead of passing the active theme to every `render_template()` call manually, Flask's `@app.context_processor` allows you to inject the current theme cookie into every Jinja2 template automatically."
            }
        ],
        code_snippets=[
            {
                "title": "Application State Manager (app.py)",
                "code": "from flask import Flask, render_template, request, make_response, session, redirect, url_for, flash\nfrom datetime import timedelta\n\napp = Flask(__name__)\napp.config['SECRET_KEY'] = 'state-management-capstone-key'\napp.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=30)\n\n@app.context_processor\ndef inject_theme():\n    # Automatically injects 'current_theme' into every Jinja2 template\n    theme = request.cookies.get('theme', 'dark')\n    return {'current_theme': theme}\n\n@app.route('/toggle-theme')\ndef toggle_theme():\n    active = request.cookies.get('theme', 'dark')\n    new_theme = 'light' if active == 'dark' else 'dark'\n    \n    resp = make_response(redirect(request.referrer or url_for('home')))\n    resp.set_cookie('theme', new_theme, max_age=365*24*60*60)\n    flash(f'Theme switched to {new_theme.capitalize()} mode.', 'info')\n    return resp"
            },
            {
                "title": "Login with Remember Me Toggle",
                "code": "@app.route('/login', methods=['GET', 'POST'])\ndef login():\n    if request.method == 'POST':\n        username = request.form.get('username')\n        remember = request.form.get('remember') == 'on'\n        \n        if username:\n            session['user'] = username\n            session.permanent = remember # Persists 30 days if checked, else expires on browser close\n            flash(f'Welcome back, {username}!', 'success')\n            return redirect(url_for('dashboard'))\n    return render_template('login.html')"
            },
            {
                "title": "Dynamic Theme Application in base.html",
                "code": "<!-- templates/base.html -->\n<!DOCTYPE html>\n<html lang=\"en\" data-theme=\"{{ current_theme }}\">\n<head>\n    <title>State Management</title>\n    <link rel=\"stylesheet\" href=\"{{ url_for('static', filename='css/themes.css') }}\">\n</head>\n<body class=\"theme-{{ current_theme }}\">\n    <nav>\n        <span>Active Theme: <b>{{ current_theme|upper }}</b></span>\n        <a href=\"{{ url_for('toggle_theme') }}\" class=\"btn-theme\">Switch Theme</a>\n    </nav>\n    <main>\n        {% block content %}{% endblock %}\n    </main>\n</body>\n</html>"
            },
            {
                "title": "CSS Theme Engine (static/css/themes.css)",
                "code": "body.theme-dark { background-color: #0F172A; color: #F8FAFC; }\nbody.theme-light { background-color: #F8FAFC; color: #0F172A; }\n.btn-theme { padding: 8px 16px; border-radius: 8px; text-decoration: none; border: 1px solid currentColor; }"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Session Authentication Guard",
            description="Write a view decorator or helper function `require_user()` that checks if 'user' is present in `session`. If not, raises PermissionError('Unauthorized access').",
            starter_code="from flask import session\n\ndef require_user():\n    # TODO: Implement session check\n    pass\n",
            solution_code="from flask import session\n\ndef require_user():\n    user = session.get('user')\n    if not user:\n        raise PermissionError('Unauthorized access')\n    return user\n\n# Simulating test context\nsession_mock = {'user': 'zubair'}\nprint(f'User verified: {session_mock.get(\"user\")}')",
            expected_output="User verified: zubair"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What Flask feature automatically injects variables into every rendered Jinja2 template without passing them manually?",
                options=["@app.context_processor", "@app.before_request", "@app.template_filter", "@app.inject_all"],
                correct_answer="@app.context_processor",
                explanation="`@app.context_processor` functions return a dictionary whose keys become globally available in templates."
            ),
            QuizQuestionBlueprint(
                question="What happens to a Flask session when `session.permanent = False`?",
                options=[
                    "It expires as a session cookie the moment the user closes their browser window.",
                    "It expires in exactly 5 minutes.",
                    "It is never saved to the browser.",
                    "It is deleted on the next page refresh."
                ],
                correct_answer="It expires as a session cookie the moment the user closes their browser window.",
                explanation="Non-permanent session cookies are deleted by browsers when the user closes their session."
            ),
            QuizQuestionBlueprint(
                question="Why are cookies better than sessions for storing UI theme preferences (Dark vs Light)?",
                options=[
                    "Preferences can be read immediately before a user logs in, and do not waste server memory.",
                    "Cookies are encrypted and sessions are not.",
                    "CSS can only read cookies, not sessions.",
                    "Sessions cannot store string values."
                ],
                correct_answer="Preferences can be read immediately before a user logs in, and do not waste server memory.",
                explanation="UI preferences apply to unauthenticated guests and authenticated users alike."
            ),
            QuizQuestionBlueprint(
                question="What HTTP header does `request.referrer` inspect to redirect users back to the page they came from?",
                options=["Referer", "Origin", "Host", "Location"],
                correct_answer="Referer",
                explanation="`request.referrer` parses the incoming HTTP `Referer` header."
            ),
            QuizQuestionBlueprint(
                question="How long does a cookie set with `max_age=31536000` persist?",
                options=["1 Year (365 days)", "1 Month", "1 Day", "1 Hour"],
                correct_answer="1 Year (365 days)",
                explanation="31,536,000 seconds = 365 days * 24 hours * 60 minutes * 60 seconds."
            )
        ],
        is_project_day=True,
        project_name="Dark Mode Preference & Remember Me System"
    ),

    # -------------------------------------------------------------
    # DAY 19
    # -------------------------------------------------------------
    DayBlueprint(
        order=19,
        title="Day 19: Flask-SQLAlchemy Setup & Database Connection",
        concept="Configuring Flask-SQLAlchemy with PostgreSQL / SQLite and initializing the database connection",
        analogy="Think of Flask-SQLAlchemy like an automatic bilingual translator. In your Python code, you speak Python objects, classes, and variables. In the database warehouse, the computer speaks SQL tables, rows, and foreign keys. Flask-SQLAlchemy translates your Python objects into database queries seamlessly!",
        theory_sections=[
            {
                "heading": "What is an Object-Relational Mapper (ORM)?",
                "body": "Writing raw SQL strings (e.g. `SELECT * FROM users WHERE email = ...`) inside your web routes is error-prone and vulnerable to SQL injection. An Object-Relational Mapper (ORM) maps database tables to Python classes and rows to Python object instances, allowing you to interact with databases using clean Python syntax."
            },
            {
                "heading": "Configuring the Database URI",
                "body": "Flask-SQLAlchemy connects to SQL engines via `app.config['SQLALCHEMY_DATABASE_URI']`. For SQLite, use `sqlite:///site.db`. For PostgreSQL, use `postgresql://user:pass@localhost:5432/dbname`. You initialize the extension using `db = SQLAlchemy(app)` or `db.init_app(app)`."
            }
        ],
        code_snippets=[
            {
                "title": "Installing and Initializing Flask-SQLAlchemy",
                "code": "from flask import Flask\nfrom flask_sqlalchemy import SQLAlchemy\n\napp = Flask(__name__)\n\n# Configure Database Connection URI\napp.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hunar_cycle.db'\napp.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False\n\n# Instantiate SQLAlchemy extension\ndb = SQLAlchemy(app)"
            },
            {
                "title": "Creating Tables with app.app_context()",
                "code": "# In Flask 2.0+ and 3.0+, database operations require an active application context\nwith app.app_context():\n    db.create_all()\n    print('All database tables successfully initialized!')"
            },
            {
                "title": "PostgreSQL Connection String Format",
                "code": "# Example PostgreSQL connection string for production:\n# postgresql://username:strong_password@localhost:5432/my_production_db\nimport os\napp.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///dev.db')"
            },
            {
                "title": "Application Factory Pattern with db.init_app",
                "code": "from flask_sqlalchemy import SQLAlchemy\n\n# Decoupled instantiation\ndb = SQLAlchemy()\n\ndef create_app():\n    app = Flask(__name__)\n    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'\n    db.init_app(app)\n    return app"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Database Configuration Validator",
            description="Write a Python script that verifies if `SQLALCHEMY_DATABASE_URI` is configured on a Flask app object. If absent, set it to 'sqlite:///fallback.db'.",
            starter_code="from flask import Flask\n\napp = Flask(__name__)\n\n# TODO: Validate and set fallback database URI\n",
            solution_code="from flask import Flask\n\napp = Flask(__name__)\n\nif 'SQLALCHEMY_DATABASE_URI' not in app.config:\n    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fallback.db'\n\nprint('Configured URI:', app.config['SQLALCHEMY_DATABASE_URI'])",
            expected_output="Configured URI: sqlite:///fallback.db"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What configuration key specifies the database engine, host, and credentials in Flask-SQLAlchemy?",
                options=["SQLALCHEMY_DATABASE_URI", "DATABASE_URL", "SQL_CONNECTION_STRING", "DB_CONFIG"],
                correct_answer="SQLALCHEMY_DATABASE_URI",
                explanation="`app.config['SQLALCHEMY_DATABASE_URI']` is the mandatory connection string parameter."
            ),
            QuizQuestionBlueprint(
                question="Why should `SQLALCHEMY_TRACK_MODIFICATIONS` almost always be set to `False`?",
                options=[
                    "It disables a deprecated event-tracking system that consumes significant server memory.",
                    "It turns off database backups.",
                    "It stops queries from executing.",
                    "It prevents tables from being deleted."
                ],
                correct_answer="It disables a deprecated event-tracking system that consumes significant server memory.",
                explanation="Tracking modifications overhead adds significant memory penalties and is deprecated."
            ),
            QuizQuestionBlueprint(
                question="What method creates all database tables corresponding to defined models in Flask-SQLAlchemy?",
                options=["db.create_all()", "db.init_tables()", "db.schema_build()", "db.migrate()"],
                correct_answer="db.create_all()",
                explanation="`db.create_all()` creates all uncreated tables defined on registered `db.Model` classes."
            ),
            QuizQuestionBlueprint(
                question="Why must `db.create_all()` be executed inside a `with app.app_context():` block in modern Flask?",
                options=[
                    "SQLAlchemy needs access to the active application config to find the database URI.",
                    "It encrypts the database file.",
                    "To prevent other operating system users from editing Python files.",
                    "It runs the migration script in a subprocess."
                ],
                correct_answer="SQLAlchemy needs access to the active application config to find the database URI.",
                explanation="Flask extensions rely on the application context to read `app.config` values."
            ),
            QuizQuestionBlueprint(
                question="What does the prefix `sqlite:///` (with three slashes) signify in a SQLite URI?",
                options=[
                    "A relative path to a database file in the project directory.",
                    "An absolute root path on Unix.",
                    "An in-memory temporary database.",
                    "A network cloud database connection."
                ],
                correct_answer="A relative path to a database file in the project directory.",
                explanation="`sqlite:///relative.db` uses three slashes for relative paths; four slashes `sqlite:////` for absolute paths."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 20
    # -------------------------------------------------------------
    DayBlueprint(
        order=20,
        title="Day 20: Models & CRUD Operations",
        concept="Defining database entities with db.Model and executing Create, Read, Update, and Delete operations",
        analogy="Think of a database Model like an architectural blueprint for a house. Every time you build a new house using that blueprint (`User(name='Ali')`), it becomes a real physical building in the database neighborhood. You can inspect it (Read), paint the walls (Update), or demolish it (Delete)!",
        theory_sections=[
            {
                "heading": "Defining Model Entities with db.Model",
                "body": "In Flask-SQLAlchemy, database tables are defined as Python classes inheriting from `db.Model`. You define columns using `db.Column()` with types like `db.Integer`, `db.String(length)`, `db.Boolean`, and `db.DateTime`. Every model must have at least one primary key (`primary_key=True`)."
            },
            {
                "heading": "Executing CRUD with db.session",
                "body": "All database changes are managed through transactions via `db.session`. To Create: `db.session.add(obj)`. To Read: `User.query.filter_by(email=...).first()`. To Update: mutate the object attribute (`user.name = 'New'`). To Delete: `db.session.delete(obj)`. Always finalize transactions with `db.session.commit()`."
            }
        ],
        code_snippets=[
            {
                "title": "Defining a User Model",
                "code": "from datetime import datetime\nfrom flask_sqlalchemy import SQLAlchemy\n\ndb = SQLAlchemy()\n\nclass User(db.Model):\n    __tablename__ = 'users'\n    \n    id = db.Column(db.Integer, primary_key=True)\n    username = db.Column(db.String(50), unique=True, nullable=False)\n    email = db.Column(db.String(120), unique=True, nullable=False)\n    is_active = db.Column(db.Boolean, default=True)\n    created_at = db.Column(db.DateTime, default=datetime.utcnow)\n\n    def __repr__(self):\n        return f'<User {self.username}>'"
            },
            {
                "title": "Create (INSERT) Operation",
                "code": "# Instantiate model and add to transaction\nnew_user = User(username='hamza_dev', email='hamza@example.com')\ndb.session.add(new_user)\ndb.session.commit() # Commits changes to the database"
            },
            {
                "title": "Read (SELECT) Operations",
                "code": "# Fetch all records\nall_users = User.query.all()\n\n# Query by primary key\nuser = User.query.get(1)\n\n# Filter with conditions\nactive_dev = User.query.filter_by(username='hamza_dev').first()\n\n# Query with 404 auto-abort if missing\nuser_or_404 = User.query.get_or_404(1)"
            },
            {
                "title": "Update and Delete Operations",
                "code": "# UPDATE: Modify attributes directly on the queried instance\nuser = User.query.filter_by(username='hamza_dev').first()\nif user:\n    user.email = 'hamza_new@example.com'\n    db.session.commit()\n\n# DELETE: Remove entity from database\nuser_to_remove = User.query.get(1)\nif user_to_remove:\n    db.session.delete(user_to_remove)\n    db.session.commit()"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Course Enrollment Model Definition",
            description="Define a `Course` model with columns: `id` (Integer, primary_key), `title` (String(100), nullable=False), `price` (Integer, default=0), and `is_published` (Boolean, default=False).",
            starter_code="from flask_sqlalchemy import SQLAlchemy\n\ndb = SQLAlchemy()\n\n# TODO: Define Course model\n",
            solution_code="from flask_sqlalchemy import SQLAlchemy\n\ndb = SQLAlchemy()\n\nclass Course(db.Model):\n    __tablename__ = 'courses'\n    id = db.Column(db.Integer, primary_key=True)\n    title = db.Column(db.String(100), nullable=False)\n    price = db.Column(db.Integer, default=0)\n    is_published = db.Column(db.Boolean, default=False)",
            expected_output="Course model declared with 4 columns"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What method must be called to permanently persist additions and updates made in `db.session` to the database?",
                options=["db.session.commit()", "db.session.save()", "db.session.flush()", "db.session.persist()"],
                correct_answer="db.session.commit()",
                explanation="`db.session.commit()` writes and finalizes the active transaction to the database."
            ),
            QuizQuestionBlueprint(
                question="Which query method returns a single record matching criteria or returns `None` if not found?",
                options=[".first()", ".one()", ".find()", ".single()"],
                correct_answer=".first()",
                explanation="`.first()` returns the first matched record or `None` without raising an exception."
            ),
            QuizQuestionBlueprint(
                question="What convenience method queries a record by primary key and automatically triggers an HTTP 404 if missing?",
                options=["Model.query.get_or_404(id)", "Model.query.find_or_404(id)", "Model.query.fetch_or_fail(id)", "Model.query.first_404()"],
                correct_answer="Model.query.get_or_404(id)",
                explanation="`get_or_404(id)` aborts with HTTP 404 if the primary key is not found."
            ),
            QuizQuestionBlueprint(
                question="How do you cancel or discard uncommitted changes in `db.session` if an error occurs?",
                options=["db.session.rollback()", "db.session.cancel()", "db.session.undo()", "db.session.discard()"],
                correct_answer="db.session.rollback()",
                explanation="`db.session.rollback()` reverts the session transaction to a clean state."
            ),
            QuizQuestionBlueprint(
                question="Which column parameter prevents two rows in the database from having identical values for that column?",
                options=["unique=True", "distinct=True", "primary=True", "singleton=True"],
                correct_answer="unique=True",
                explanation="`unique=True` generates a UNIQUE constraint on that database column."
            )
        ]
    ),
]
