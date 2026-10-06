"""
Flask Mastery 40-Day Curriculum - Module 5 (Part 2), Module 6, Module 7 & Module 8 (Part 1) (Days 21 to 30)
Module 5: Databases & ORM (Days 21-23)
Module 6: Security & Auth (Days 24-27)
Module 7: Architecture (Days 28-29)
Module 8: RESTful APIs Part 1 (Day 30)
"""

from seeder.course_blueprint import DayBlueprint, QuizQuestionBlueprint, CodingChallengeBlueprint

DAYS_21_TO_30 = [
    # -------------------------------------------------------------
    # DAY 21
    # -------------------------------------------------------------
    DayBlueprint(
        order=21,
        title="Day 21: Database Relationships (One-to-Many & Foreign Keys)",
        concept="Modeling relational connections between tables using db.ForeignKey and db.relationship",
        analogy="Think of a one-to-many relationship like an author and their books. One author can write dozens of books, but each physical book has exactly one primary author's signature inside the cover. In SQLAlchemy, the book carries a small library tag (`ForeignKey`) pointing directly back to the author!",
        theory_sections=[
            {
                "heading": "The Anatomy of a Relational Connection",
                "body": "Relational databases derive their power from linking tables together. In a One-to-Many relationship (e.g. One User has Many Posts), the child table (`Post`) stores the parent's primary key inside a `db.ForeignKey('users.id')` column. The parent table (`User`) defines a virtual `db.relationship('Post', backref='author', lazy=True)`."
            },
            {
                "heading": "Backrefs and Lazy Loading Strategies",
                "body": "The `backref='author'` attribute automatically injects an `author` property onto every `Post` instance, allowing bidirectional navigation (`post.author.username` and `user.posts`). The `lazy=True` parameter tells SQLAlchemy to load related posts only when accessed, optimizing query performance."
            }
        ],
        code_snippets=[
            {
                "title": "Defining One-to-Many User and Post Models",
                "code": "from datetime import datetime\nfrom flask_sqlalchemy import SQLAlchemy\n\ndb = SQLAlchemy()\n\nclass User(db.Model):\n    __tablename__ = 'users'\n    id = db.Column(db.Integer, primary_key=True)\n    username = db.Column(db.String(50), unique=True, nullable=False)\n    \n    # Virtual relationship: links User to multiple Post objects\n    posts = db.relationship('Post', backref='author', lazy=True, cascade='all, delete-orphan')\n\nclass Post(db.Model):\n    __tablename__ = 'posts'\n    id = db.Column(db.Integer, primary_key=True)\n    title = db.Column(db.String(120), nullable=False)\n    content = db.Column(db.Text, nullable=False)\n    date_posted = db.Column(db.DateTime, default=datetime.utcnow)\n    \n    # Foreign Key pointing to the 'id' column of the 'users' table\n    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)"
            },
            {
                "title": "Creating Related Records in Python",
                "code": "# 1. Create the Author\nauthor = User(username='sarah_writer')\ndb.session.add(author)\ndb.session.commit()\n\n# 2. Create a Post associated with Sarah\n# You can assign the object instance directly via the backref!\npost1 = Post(title='Intro to Flask', content='Flask is amazing...', author=author)\ndb.session.add(post1)\ndb.session.commit()"
            },
            {
                "title": "Bidirectional Navigation Between Entities",
                "code": "# Accessing child objects from parent\nuser = User.query.filter_by(username='sarah_writer').first()\nfor p in user.posts:\n    print(f'Post: {p.title}')\n\n# Accessing parent object from child\npost = Post.query.first()\nprint(f'Written by: {post.author.username}')"
            },
            {
                "title": "Cascading Deletes",
                "code": "# cascade='all, delete-orphan' ensures deleting a user automatically deletes all their posts\nuser_to_delete = User.query.get(1)\ndb.session.delete(user_to_delete)\ndb.session.commit()"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Department and Employee Relationship Model",
            description="Declare models `Department` (id, name, employees relationship) and `Employee` (id, name, department_id ForeignKey pointing to 'departments.id' with backref 'department').",
            starter_code="from flask_sqlalchemy import SQLAlchemy\n\ndb = SQLAlchemy()\n\n# TODO: Define Department and Employee models\n",
            solution_code="from flask_sqlalchemy import SQLAlchemy\n\ndb = SQLAlchemy()\n\nclass Department(db.Model):\n    __tablename__ = 'departments'\n    id = db.Column(db.Integer, primary_key=True)\n    name = db.Column(db.String(50), nullable=False)\n    employees = db.relationship('Employee', backref='department', lazy=True)\n\nclass Employee(db.Model):\n    __tablename__ = 'employees'\n    id = db.Column(db.Integer, primary_key=True)\n    name = db.Column(db.String(50), nullable=False)\n    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'), nullable=False)",
            expected_output="Department and Employee relational models declared"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="In `db.ForeignKey('users.id')`, what does `'users'` refer to?",
                options=[
                    "The actual SQL database table name (`__tablename__`).",
                    "The Python model class name.",
                    "The database schema name.",
                    "The name of the relationship variable."
                ],
                correct_answer="The actual SQL database table name (`__tablename__`).",
                explanation="Foreign keys reference underlying database table columns directly (`tablename.column`)."
            ),
            QuizQuestionBlueprint(
                question="What parameter on `db.relationship` automatically adds a reverse pointer onto child objects?",
                options=["backref", "reverse_name", "target", "parent_ref"],
                correct_answer="backref",
                explanation="`backref='author'` establishes the reverse attribute on the child model automatically."
            ),
            QuizQuestionBlueprint(
                question="What does `cascade='all, delete-orphan'` do when a parent record is deleted?",
                options=[
                    "Automatically deletes all associated child records so they are not left orphaned.",
                    "Prevents the parent from being deleted if child records exist.",
                    "Sets the child foreign keys to NULL.",
                    "Exports deleted records to a backup CSV."
                ],
                correct_answer="Automatically deletes all associated child records so they are not left orphaned.",
                explanation="Cascading deletes maintain database integrity by automatically removing orphaned child records."
            ),
            QuizQuestionBlueprint(
                question="What does `lazy=True` signify in `db.relationship`?",
                options=[
                    "SQLAlchemy loads child records from the database on-demand only when accessed in Python.",
                    "SQLAlchemy performs an immediate SQL JOIN on every query.",
                    "Queries run on a background thread.",
                    "Queries are cached in Redis forever."
                ],
                correct_answer="SQLAlchemy loads child records from the database on-demand only when accessed in Python.",
                explanation="Lazy loading defers executing SQL for related records until the attribute is explicitly referenced."
            ),
            QuizQuestionBlueprint(
                question="Can a child object be assigned its parent using the backref object directly instead of raw foreign key integer IDs?",
                options=[
                    "Yes, e.g. `Post(title='...', author=user_instance)`.",
                    "No, only numeric foreign key IDs can be assigned.",
                    "Only in SQLite, not PostgreSQL.",
                    "Only if using raw SQL queries."
                ],
                correct_answer="Yes, e.g. `Post(title='...', author=user_instance)`.",
                explanation="SQLAlchemy automatically resolves the primary key when you assign the model instance to the backref."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 22
    # -------------------------------------------------------------
    DayBlueprint(
        order=22,
        title="Day 22: Schema Migrations with Flask-Migrate & Alembic",
        concept="Tracking, evolving, and applying database schema modifications over time using Alembic migrations",
        analogy="Think of Flask-Migrate like Git version control for your database tables. Just like Git tracks changes to your code line-by-line (`git commit`), Alembic tracks changes to your database schema column-by-column (`flask db migrate`). If you make a mistake, you can roll back your database to a previous revision without losing existing user data!",
        theory_sections=[
            {
                "heading": "Why `db.create_all()` Fails in Production",
                "body": "`db.create_all()` only creates tables that do not exist yet; it never alters existing columns, adds new fields, or changes data types on already created tables. If you add a column to your Python model, `db.create_all()` does nothing, leaving your code out of sync with the database."
            },
            {
                "heading": "The Flask-Migrate Workflow",
                "body": "Flask-Migrate wraps the Alembic migration library. The standard workflow is: (1) `flask db init` to generate the migration repository folder, (2) `flask db migrate -m 'add bio column'` to detect Python model changes and generate an upgrade script, and (3) `flask db upgrade` to execute the schema migration on PostgreSQL."
            }
        ],
        code_snippets=[
            {
                "title": "Integrating Flask-Migrate in app.py",
                "code": "from flask import Flask\nfrom flask_sqlalchemy import SQLAlchemy\nfrom flask_migrate import Migrate\n\napp = Flask(__name__)\napp.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'\n\ndb = SQLAlchemy(app)\n# Initialize Migrate extension linking app and db\nmigrate = Migrate(app, db)"
            },
            {
                "title": "Core CLI Migration Commands",
                "code": "# 1. Initialize migration folder (run once at project creation):\n# flask db init\n\n# 2. Detect model changes and generate a migration script:\n# flask db migrate -m \"Add bio and phone to user\"\n\n# 3. Apply the migration to the live database:\n# flask db upgrade\n\n# 4. Rollback to the previous migration version:\n# flask db downgrade"
            },
            {
                "title": "Understanding an Alembic Migration Script",
                "code": "# migrations/versions/a1b2c3d4_add_bio.py\n\"\"\"Add bio to user\"\"\"\ndef upgrade():\n    # Adds 'bio' column to the 'users' table\n    op.add_column('users', sa.Column('bio', sa.String(length=200), nullable=True))\n\ndef downgrade():\n    # Reverts by dropping 'bio' column if rolled back\n    op.drop_column('users', 'bio')"
            },
            {
                "title": "Checking Current Database Migration Revision",
                "code": "# Check active revision hash in the database:\n# flask db current\n\n# View migration history:\n# flask db history"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Migration Command Sequence",
            description="Write a Python script that prints the standard three-step terminal command sequence for modifying a model and safely upgrading the database schema.",
            starter_code="# TODO: Print standard Flask-Migrate command sequence\n",
            solution_code="commands = [\n    'flask db migrate -m \"update schema\"',\n    'flask db upgrade'\n]\nprint('STEP 1:', commands[0])\nprint('STEP 2:', commands[1])",
            expected_output="STEP 1: flask db migrate -m \"update schema\"\nSTEP 2: flask db upgrade"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Why can `db.create_all()` not be used to update existing database columns?",
                options=[
                    "It only creates tables if they do not exist; it cannot alter existing tables.",
                    "It deletes all tables before recreating them.",
                    "It only works on MySQL.",
                    "It requires root operating system access."
                ],
                correct_answer="It only creates tables if they do not exist; it cannot alter existing tables.",
                explanation="`db.create_all()` does not inspect schema differences on pre-existing tables."
            ),
            QuizQuestionBlueprint(
                question="What underlying database migration engine powers Flask-Migrate?",
                options=["Alembic", "Flyway", "Liquibase", "Prisma"],
                correct_answer="Alembic",
                explanation="Alembic is the official database migration tool for SQLAlchemy."
            ),
            QuizQuestionBlueprint(
                question="Which terminal command applies pending migration scripts to your active database?",
                options=["flask db upgrade", "flask db apply", "flask db push", "flask db run"],
                correct_answer="flask db upgrade",
                explanation="`flask db upgrade` executes the `upgrade()` function of all unapplied migration files."
            ),
            QuizQuestionBlueprint(
                question="What command generates a new version migration file by detecting changes in your `db.Model` classes?",
                options=["flask db migrate -m \"message\"", "flask db create", "flask db make", "flask db diff"],
                correct_answer="flask db migrate -m \"message\"",
                explanation="`flask db migrate` inspects your models and autogenerates an Alembic revision file."
            ),
            QuizQuestionBlueprint(
                question="How do you revert the most recently applied database migration?",
                options=["flask db downgrade", "flask db revert", "flask db undo", "flask db rollback"],
                correct_answer="flask db downgrade",
                explanation="`flask db downgrade` rolls back the schema to the previous revision hash."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 23 (Project)
    # -------------------------------------------------------------
    DayBlueprint(
        order=23,
        title="Day 23: Database-Driven Blog Engine Project",
        concept="Developing a complete multi-model blog engine with posts, authors, comments, and full CRUD interfaces",
        analogy="Think of building this blog engine like launching a digital magazine publishing house. Journalists (Users) write articles (Posts). Readers interact by publishing thoughts underneath each article (Comments). The central database archives every article and comment in perfect order, linking writers and readers together!",
        theory_sections=[
            {
                "heading": "Multi-Entity Architecture",
                "body": "In this project, you build a production-grade relational application containing three models: `User`, `Post`, and `Comment`. A User has many Posts and many Comments. A Post has many Comments. You will implement complete CRUD views: creating posts, listing paginated feeds, viewing post details with comments, and deleting content."
            },
            {
                "heading": "Pagination for Scalable Querying",
                "body": "Displaying 10,000 blog posts on a single page would crash the server and browser. Flask-SQLAlchemy provides `.paginate(page=1, per_page=5)`, which executes efficient SQL `LIMIT` and `OFFSET` queries and returns a `Pagination` helper object for rendering Next/Prev buttons in templates."
            }
        ],
        code_snippets=[
            {
                "title": "Blog Models with Multi-Table Relationships (models.py)",
                "code": "from datetime import datetime\nfrom flask_sqlalchemy import SQLAlchemy\n\ndb = SQLAlchemy()\n\nclass User(db.Model):\n    __tablename__ = 'users'\n    id = db.Column(db.Integer, primary_key=True)\n    username = db.Column(db.String(50), unique=True, nullable=False)\n    posts = db.relationship('Post', backref='author', lazy=True)\n    comments = db.relationship('Comment', backref='author', lazy=True)\n\nclass Post(db.Model):\n    __tablename__ = 'posts'\n    id = db.Column(db.Integer, primary_key=True)\n    title = db.Column(db.String(150), nullable=False)\n    body = db.Column(db.Text, nullable=False)\n    created_at = db.Column(db.DateTime, default=datetime.utcnow)\n    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)\n    comments = db.relationship('Comment', backref='post', lazy=True, cascade='all, delete-orphan')\n\nclass Comment(db.Model):\n    __tablename__ = 'comments'\n    id = db.Column(db.Integer, primary_key=True)\n    content = db.Column(db.Text, nullable=False)\n    created_at = db.Column(db.DateTime, default=datetime.utcnow)\n    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)\n    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)"
            },
            {
                "title": "Paginated Feed Controller (app.py)",
                "code": "@app.route('/blog')\ndef blog_feed():\n    page = request.args.get('page', 1, type=int)\n    # Efficient SQL LIMIT/OFFSET pagination\n    posts = Post.query.order_by(Post.created_at.desc()).paginate(page=page, per_page=5)\n    return render_template('blog/feed.html', pagination=posts)"
            },
            {
                "title": "Post Detail & Comment Submission View",
                "code": "@app.route('/blog/<int:post_id>', methods=['GET', 'POST'])\ndef post_detail(post_id):\n    post = Post.query.get_or_404(post_id)\n    if request.method == 'POST':\n        comment_text = request.form.get('comment')\n        if comment_text:\n            new_comment = Comment(content=comment_text, user_id=1, post=post)\n            db.session.add(new_comment)\n            db.session.commit()\n            flash('Comment published!', 'success')\n            return redirect(url_for('post_detail', post_id=post.id))\n    return render_template('blog/detail.html', post=post)"
            },
            {
                "title": "Jinja2 Pagination Controls (feed.html)",
                "code": "<!-- Render pagination controls -->\n<div class=\"pagination\">\n    {% if pagination.has_prev %}\n        <a href=\"{{ url_for('blog_feed', page=pagination.prev_num) }}\">&larr; Newer Posts</a>\n    {% endif %}\n    <span>Page {{ pagination.page }} of {{ pagination.pages }}</span>\n    {% if pagination.has_next %}\n        <a href=\"{{ url_for('blog_feed', page=pagination.next_num) }}\">Older Posts &rarr;</a>\n    {% endif %}\n</div>"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Pagination State Inspector",
            description="Write a function that calculates total pages given total records count and items per page, returning a tuple (total_pages, has_next) for a requested page number.",
            starter_code="import math\n\ndef calc_pagination(total_items, per_page, current_page):\n    # TODO: Calculate total_pages and has_next boolean\n    pass\n",
            solution_code="import math\n\ndef calc_pagination(total_items, per_page, current_page):\n    total_pages = math.ceil(total_items / per_page)\n    has_next = current_page < total_pages\n    return (total_pages, has_next)\n\nprint(calc_pagination(23, 5, 2))",
            expected_output="(5, True)"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What method on a SQLAlchemy query generates a `Pagination` object with page limits?",
                options=[".paginate(page=..., per_page=...)", ".limit_page()", ".slice_records()", ".split()"],
                correct_answer=".paginate(page=..., per_page=...)",
                explanation="`.paginate(page=..., per_page=...)` executes `LIMIT` and `OFFSET` queries and creates pagination metadata."
            ),
            QuizQuestionBlueprint(
                question="On a `Pagination` object in Jinja2, which property indicates if a subsequent page exists?",
                options=["pagination.has_next", "pagination.next_exists", "pagination.can_forward", "pagination.more"],
                correct_answer="pagination.has_next",
                explanation="`pagination.has_next` returns True if there is at least one more page after the current one."
            ),
            QuizQuestionBlueprint(
                question="If a Post has a cascading delete relationship with Comments, what happens when the Post is deleted?",
                options=[
                    "All comments associated with that post are deleted automatically.",
                    "The comments remain with NULL post_id.",
                    "SQLAlchemy throws a foreign key constraint violation.",
                    "The user who wrote the comments is deleted."
                ],
                correct_answer="All comments associated with that post are deleted automatically.",
                explanation="Cascading deletes prune child comments when their parent post is removed."
            ),
            QuizQuestionBlueprint(
                question="How do you sort blog posts from newest to oldest in a SQLAlchemy query?",
                options=[
                    "Post.query.order_by(Post.created_at.desc())",
                    "Post.query.sort('created_at', reverse=True)",
                    "Post.query.reverse()",
                    "Post.query.filter(created_at='desc')"
                ],
                correct_answer="Post.query.order_by(Post.created_at.desc())",
                explanation="`order_by(Model.column.desc())` translates to `ORDER BY created_at DESC` in SQL."
            ),
            QuizQuestionBlueprint(
                question="Why is `Post.query.get_or_404(post_id)` preferred over `Post.query.get(post_id)` in blog route handlers?",
                options=[
                    "It automatically returns an HTTP 404 response if the blog post ID does not exist, eliminating manual error handling.",
                    "It encrypts the post in memory.",
                    "It automatically loads comments eagerly.",
                    "It caches the blog post in browser local storage."
                ],
                correct_answer="It automatically returns an HTTP 404 response if the blog post ID does not exist, eliminating manual error handling.",
                explanation="`get_or_404` simplifies code by raising an abort(404) whenever a requested ID is missing."
            )
        ],
        is_project_day=True,
        project_name="Database-Driven Blog Engine"
    ),

    # -------------------------------------------------------------
    # DAY 24
    # -------------------------------------------------------------
    DayBlueprint(
        order=24,
        title="Day 24: Password Hashing & Security Fundamentals",
        concept="Securing user passwords cryptographically using salted hashes with Werkzeug security functions",
        analogy="Think of password hashing like a meat grinder. You can put an apple into a meat grinder and turn it into applesauce, but no matter how hard you try, you can never reconstruct the original apple from the applesauce! When a user logs in, you put their entered password through the same grinder and compare the sauce!",
        theory_sections=[
            {
                "heading": "The Golden Rule: Never Store Plaintext Passwords",
                "body": "Storing passwords in plaintext is an unforgivable security flaw. If your database is ever compromised, every user's credentials are leaked. Passwords must be hashed using a one-way mathematical function designed with computational difficulty to defeat brute-force and rainbow table attacks."
            },
            {
                "heading": "Werkzeug Security: Salted Hashes",
                "body": "Flask's core dependency, Werkzeug, provides `generate_password_hash(password, method='pbkdf2:sha256')` and `check_password_hash(hash, candidate_password)`. Werkzeug automatically generates a random cryptographic salt for every hash, guaranteeing that two identical passwords produce completely different hash strings."
            }
        ],
        code_snippets=[
            {
                "title": "Generating a Salted Password Hash",
                "code": "from werkzeug.security import generate_password_hash, check_password_hash\n\nraw_password = 'MySecretPassword2026!'\n# Generates a salted PBKDF2/scrypt hash\nhashed_pw = generate_password_hash(raw_password)\nprint(f'Hashed Output: {hashed_pw}')\n# Output format: pbkdf2:sha256:600000$salt$hash_digest"
            },
            {
                "title": "Verifying Candidate Passwords",
                "code": "# Verification returns a clean Boolean\nis_correct = check_password_hash(hashed_pw, 'MySecretPassword2026!')\nprint(f'Valid Password: {is_correct}') # True\n\nis_wrong = check_password_hash(hashed_pw, 'WrongPassword')\nprint(f'Invalid Password: {is_wrong}') # False"
            },
            {
                "title": "Integrating Password Hashing into User Model",
                "code": "class User(db.Model):\n    id = db.Column(db.Integer, primary_key=True)\n    username = db.Column(db.String(50), unique=True)\n    password_hash = db.Column(db.String(256), nullable=False)\n\n    def set_password(self, password):\n        self.password_hash = generate_password_hash(password)\n\n    def check_password(self, password):\n        return check_password_hash(self.password_hash, password)"
            },
            {
                "title": "Demonstrating Salt Randomness",
                "code": "# Two identical passwords produce completely different hashes due to salt:\nh1 = generate_password_hash('password123')\nh2 = generate_password_hash('password123')\nprint(f'H1 == H2? {h1 == h2}') # False"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Credential Verification Engine",
            description="Write a Python class `AuthService` with methods `register(password)` returning the hash, and `verify(stored_hash, candidate_password)` returning a boolean.",
            starter_code="from werkzeug.security import generate_password_hash, check_password_hash\n\n# TODO: Implement AuthService\n",
            solution_code="from werkzeug.security import generate_password_hash, check_password_hash\n\nclass AuthService:\n    @staticmethod\n    def register(password):\n        return generate_password_hash(password)\n\n    @staticmethod\n    def verify(stored_hash, candidate_password):\n        return check_password_hash(stored_hash, candidate_password)\n\nh = AuthService.register('secret')\nprint('Verification:', AuthService.verify(h, 'secret'))",
            expected_output="Verification: True"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Why is MD5 or SHA-1 considered unsafe for hashing user passwords today?",
                options=[
                    "They are fast algorithms easily cracked by modern GPUs using rainbow tables.",
                    "They can only hash strings shorter than 8 characters.",
                    "They require Windows operating systems.",
                    "They do not work in Python 3."
                ],
                correct_answer="They are fast algorithms easily cracked by modern GPUs using rainbow tables.",
                explanation="Password hashing algorithms must be computationally slow (like PBKDF2, bcrypt, or scrypt) to hinder brute force."
            ),
            QuizQuestionBlueprint(
                question="What is a cryptographic 'salt' in password hashing?",
                options=[
                    "A random unique string prepended to the password before hashing to prevent rainbow table lookups.",
                    "An encryption cipher key.",
                    "A browser cookie.",
                    "A password expiration date."
                ],
                correct_answer="A random unique string prepended to the password before hashing to prevent rainbow table lookups.",
                explanation="Salts ensure that identical passwords yield distinct hashes, defeating precomputed lookup tables."
            ),
            QuizQuestionBlueprint(
                question="Which Werkzeug function verifies an entered plaintext password against a stored hash string?",
                options=["check_password_hash()", "verify_password()", "compare_hash()", "is_password_valid()"],
                correct_answer="check_password_hash()",
                explanation="`check_password_hash(hash, password)` extracts the salt and verifies the hash."
            ),
            QuizQuestionBlueprint(
                question="What should be the minimum recommended length of the `password_hash` database column?",
                options=[
                    "String(256) or String(512)",
                    "String(32)",
                    "String(16)",
                    "String(8)"
                ],
                correct_answer="String(256) or String(512)",
                explanation="Modern hashing methods (like PBKDF2 or scrypt) produce long hash strings with parameters and salts."
            ),
            QuizQuestionBlueprint(
                question="Can you decrypt a hashed password back into its original plaintext?",
                options=[
                    "No, hashing is a strictly one-way mathematical function.",
                    "Yes, using the application secret key.",
                    "Yes, by using Python's unhash() library.",
                    "Only within the first 24 hours."
                ],
                correct_answer="No, hashing is a strictly one-way mathematical function.",
                explanation="Unlike encryption (which is two-way and reversible with a key), hashing is strictly irreversible."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 25
    # -------------------------------------------------------------
    DayBlueprint(
        order=25,
        title="Day 25: Flask-Login & Session-Based Authentication",
        concept="Managing user authentication sessions, current_user proxy, and route protection using @login_required",
        analogy="Think of Flask-Login like the VIP bouncer and wristband manager at a concert venue. When you show your ID at the door, the bouncer hands you a VIP pass (`login_user`). Every time you want to enter the backstage VIP lounge (`@login_required`), the bouncer checks your pass (`current_user.is_authenticated`) instantly!",
        theory_sections=[
            {
                "heading": "The Role of Flask-Login",
                "body": "Managing authentication manually by writing session cookies for every route is repetitive and prone to security bugs. Flask-Login manages the user session lifecycle transparently: logging in, logging out, remembering users across sessions, and loading user objects from the database."
            },
            {
                "heading": "The UserMixin and user_loader Callback",
                "body": "Your `User` model inherits from `UserMixin`, which provides standard properties: `is_authenticated`, `is_active`, `is_anonymous`, and `get_id()`. You define a `@login_manager.user_loader` function that Flask-Login calls on every request to reload the current user from their session ID."
            }
        ],
        code_snippets=[
            {
                "title": "Configuring Flask-Login and UserMixin",
                "code": "from flask import Flask\nfrom flask_sqlalchemy import SQLAlchemy\nfrom flask_login import LoginManager, UserMixin\n\napp = Flask(__name__)\napp.config['SECRET_KEY'] = 'auth-super-secret'\n\ndb = SQLAlchemy(app)\nlogin_manager = LoginManager(app)\n# Route to redirect unauthenticated users when accessing protected views\nlogin_manager.login_view = 'login'\nlogin_manager.login_message_category = 'warning'\n\nclass User(db.Model, UserMixin):\n    id = db.Column(db.Integer, primary_key=True)\n    username = db.Column(db.String(50), unique=True)\n    password_hash = db.Column(db.String(256))"
            },
            {
                "title": "Defining the user_loader Callback",
                "code": "@login_manager.user_loader\ndef load_user(user_id):\n    # Must return User object from primary key integer\n    return User.query.get(int(user_id))"
            },
            {
                "title": "Logging Users In and Out",
                "code": "from flask import request, redirect, url_for, flash\nfrom flask_login import login_user, logout_user, login_required\n\n@app.route('/login', methods=['POST'])\ndef login():\n    username = request.form.get('username')\n    password = request.form.get('password')\n    user = User.query.filter_by(username=username).first()\n    \n    if user and user.check_password(password):\n        login_user(user, remember=True) # Logs user in and serializes ID to session\n        flash('Logged in successfully!', 'success')\n        return redirect(url_for('dashboard'))\n    flash('Invalid credentials', 'danger')\n    return redirect(url_for('login'))\n\n@app.route('/logout')\n@login_required\ndef logout():\n    logout_user() # Clears session\n    flash('You have been logged out.', 'info')\n    return redirect(url_for('login'))"
            },
            {
                "title": "Protecting Routes with @login_required",
                "code": "from flask_login import current_user\n\n@app.route('/dashboard')\n@login_required\ndef dashboard():\n    # current_user represents the active authenticated User instance\n    return f'Welcome to your private dashboard, {current_user.username}!'"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="User Model with UserMixin",
            description="Declare a Flask-SQLAlchemy `User` model that inherits from both `db.Model` and `UserMixin` with fields: `id` (Integer, primary_key) and `email` (String(100), unique=True).",
            starter_code="from flask_sqlalchemy import SQLAlchemy\nfrom flask_login import UserMixin\n\ndb = SQLAlchemy()\n\n# TODO: Declare User inheriting from db.Model and UserMixin\n",
            solution_code="from flask_sqlalchemy import SQLAlchemy\nfrom flask_login import UserMixin\n\ndb = SQLAlchemy()\n\nclass User(db.Model, UserMixin):\n    __tablename__ = 'users'\n    id = db.Column(db.Integer, primary_key=True)\n    email = db.Column(db.String(100), unique=True, nullable=False)",
            expected_output="User model created with UserMixin inheritance"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What decorator protects routes so that only authenticated users can access them?",
                options=["@login_required", "@auth_only", "@require_user", "@protected"],
                correct_answer="@login_required",
                explanation="`@login_required` blocks anonymous access and redirects to `login_manager.login_view`."
            ),
            QuizQuestionBlueprint(
                question="What callback function must be registered so Flask-Login knows how to load a user from session storage?",
                options=["@login_manager.user_loader", "@login_manager.load", "@app.load_user", "@session.user_handler"],
                correct_answer="@login_manager.user_loader",
                explanation="The `@login_manager.user_loader` callback fetches the User object by ID from the database."
            ),
            QuizQuestionBlueprint(
                question="What object represents the currently logged-in user in views and Jinja2 templates?",
                options=["current_user", "active_user", "session.user", "g.user"],
                correct_answer="current_user",
                explanation="`current_user` is a proxy representing the active authenticated User object."
            ),
            QuizQuestionBlueprint(
                question="What mixin class should your User model inherit from to provide default authentication properties?",
                options=["UserMixin", "AuthModel", "LoginModel", "SessionMixin"],
                correct_answer="UserMixin",
                explanation="`UserMixin` provides implementations of `is_authenticated`, `is_active`, `is_anonymous`, and `get_id()`."
            ),
            QuizQuestionBlueprint(
                question="What function is called to log an authenticated User instance into the active session?",
                options=["login_user(user)", "user.login()", "auth.start_session(user)", "session.set_user(user)"],
                correct_answer="login_user(user)",
                explanation="`login_user(user)` records the user ID into the signed session cookie."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 26
    # -------------------------------------------------------------
    DayBlueprint(
        order=26,
        title="Day 26: Role-Based Access Control (RBAC) & Custom Decorators",
        concept="Restricting administrative endpoints using roles, permissions, and Python decorator wrappers",
        analogy="Think of Role-Based Access Control like color-coded security badges in a hospital. A Green badge (Patient) can enter the waiting room and clinic. A Blue badge (Doctor) can enter the operating room. A Red badge (Hospital Administrator) can enter the billing records and server room. The security system checks your badge color before sliding open any door!",
        theory_sections=[
            {
                "heading": "Principles of Role-Based Access Control (RBAC)",
                "body": "Not all authenticated users have equal privileges. In enterprise web applications, users are assigned roles (e.g. `'student'`, `'instructor'`, `'admin'`). While regular users can manage their own profile, only administrators should access user management, billing, and system metrics."
            },
            {
                "heading": "Building Custom Decorators with functools.wraps",
                "body": "Instead of copy-pasting `if current_user.role != 'admin': abort(403)` across 30 different administrative routes, you write a reusable Python decorator `@admin_required`. Using `functools.wraps(f)` preserves the original function's name and docstring, ensuring Flask's routing table works seamlessly."
            }
        ],
        code_snippets=[
            {
                "title": "Adding Role Column to User Model",
                "code": "class User(db.Model, UserMixin):\n    id = db.Column(db.Integer, primary_key=True)\n    username = db.Column(db.String(50), unique=True)\n    # Roles: 'user', 'moderator', 'admin'\n    role = db.Column(db.String(20), default='user', nullable=False)\n\n    @property\n    def is_admin(self):\n        return self.role == 'admin'"
            },
            {
                "title": "Constructing the @admin_required Decorator",
                "code": "from functools import wraps\nfrom flask import abort\nfrom flask_login import current_user\n\ndef admin_required(f):\n    @wraps(f)\n    def decorated_function(*args, **kwargs):\n        # Must be logged in AND have admin role\n        if not current_user.is_authenticated or current_user.role != 'admin':\n            abort(403) # Return HTTP 403 Forbidden\n        return f(*args, **kwargs)\n    return decorated_function"
            },
            {
                "title": "Securing Admin Routes with Multiple Decorators",
                "code": "@app.route('/admin/users')\n@login_required\n@admin_required\ndef manage_users():\n    users = User.query.all()\n    return render_template('admin/users.html', users=users)"
            },
            {
                "title": "Conditionally Rendering Admin UI Elements in Jinja2",
                "code": "<!-- templates/base.html -->\n<nav>\n    <a href=\"/dashboard\">Dashboard</a>\n    {% if current_user.is_authenticated and current_user.role == 'admin' %}\n        <a href=\"/admin/users\" class=\"badge-admin\">Admin Console</a>\n    {% endif %}\n</nav>"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Generalized Role Guard Decorator",
            description="Write a Python decorator factory `role_required(allowed_role)` that checks if `current_user.role == allowed_role`, aborting with 403 if mismatched.",
            starter_code="from functools import wraps\nfrom flask import abort\n\n# TODO: Implement role_required factory\ndef role_required(role_name):\n    pass\n",
            solution_code="from functools import wraps\nfrom flask import abort\n\ndef role_required(role_name):\n    def decorator(f):\n        @wraps(f)\n        def wrapper(*args, **kwargs):\n            user_role = getattr(current_user, 'role', None)\n            if user_role != role_name:\n                abort(403)\n            return f(*args, **kwargs)\n        return wrapper\n    return decorator",
            expected_output="role_required decorator constructed"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Why is `functools.wraps(f)` essential when creating custom route decorators in Flask?",
                options=[
                    "It preserves the original function's name and module docstring so Flask's endpoint mapper doesn't crash from name collisions.",
                    "It automatically creates a database transaction.",
                    "It validates the user's password.",
                    "It speeds up execution by 50%."
                ],
                correct_answer="It preserves the original function's name and module docstring so Flask's endpoint mapper doesn't crash from name collisions.",
                explanation="Without `wraps`, decorated functions inherit the inner wrapper's name, causing route endpoint collisions in Flask."
            ),
            QuizQuestionBlueprint(
                question="What HTTP status code is standard when an authenticated user attempts to access an endpoint their role is not authorized for?",
                options=["403 Forbidden", "401 Unauthorized", "404 Not Found", "405 Method Not Allowed"],
                correct_answer="403 Forbidden",
                explanation="401 means not authenticated; 403 means authenticated but lacking permissions (Forbidden)."
            ),
            QuizQuestionBlueprint(
                question="When stacking decorators, in what order should `@login_required` and `@admin_required` be placed?",
                options=[
                    "`@app.route`, followed by `@login_required`, followed by `@admin_required`.",
                    "`@admin_required` first, then `@app.route`.",
                    "The order does not matter in Python.",
                    "Only one decorator can be used per route."
                ],
                correct_answer="`@app.route`, followed by `@login_required`, followed by `@admin_required`.",
                explanation="Route decorators execute top-to-bottom: verify route, then verify user is logged in, then verify admin role."
            ),
            QuizQuestionBlueprint(
                question="How can you verify admin status inside a Jinja2 template conditionally?",
                options=[
                    "`{% if current_user.is_authenticated and current_user.role == 'admin' %}`",
                    "`{% if is_admin() %}`",
                    "`{% admin %}`",
                    "`{{ user.admin_only }}`"
                ],
                correct_answer="`{% if current_user.is_authenticated and current_user.role == 'admin' %}`",
                explanation="Jinja2 checks both that a user is logged in and that their role matches 'admin'."
            ),
            QuizQuestionBlueprint(
                question="What is the advantage of using an enum or fixed strings for user roles?",
                options=[
                    "Prevents typos like 'admim' and establishes predictable authorization checks.",
                    "Encrypts database columns.",
                    "Reduces RAM usage by 90%.",
                    "Allows users to change their own role."
                ],
                correct_answer="Prevents typos like 'admim' and establishes predictable authorization checks.",
                explanation="Enforcing role constants prevents typo-induced security bypasses."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 27 (Project)
    # -------------------------------------------------------------
    DayBlueprint(
        order=27,
        title="Day 27: Production Authentication & Authorization System Project",
        concept="Building a complete authentication ecosystem: Registration, Hashed Login, Remember-Me, and Admin Dashboard",
        analogy="Think of this project like building the digital security vault for an entire office building. You have an enrollment desk (Registration), a biometric badge scanner at the turnstile (Login with password hashing), a visitor desk, and an executive keycard elevator to the top floor (Admin RBAC)!",
        theory_sections=[
            {
                "heading": "Enterprise Authentication Architecture",
                "body": "In this project, you unify all concepts from Module 6 into a cohesive enterprise security layer: user registration with password confirmation and duplicate email prevention, salted password hashing using Werkzeug, session state management via Flask-Login, and a role-guarded administrative portal."
            },
            {
                "heading": "Preventing User Enumeration Attacks",
                "body": "When a login fails, never display specific messages like 'Username not found' or 'Incorrect password'. Attackers use these differences to enumerate valid user accounts. Always display a generic message: 'Invalid username or password'."
            }
        ],
        code_snippets=[
            {
                "title": "Complete Authentication Application (auth_app.py)",
                "code": "from flask import Flask, render_template, redirect, url_for, flash, request, abort\nfrom flask_sqlalchemy import SQLAlchemy\nfrom flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user\nfrom werkzeug.security import generate_password_hash, check_password_hash\nfrom functools import wraps\n\napp = Flask(__name__)\napp.config['SECRET_KEY'] = 'enterprise-auth-master-key'\napp.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///production_auth.db'\n\ndb = SQLAlchemy(app)\nlogin_manager = LoginManager(app)\nlogin_manager.login_view = 'login'\nlogin_manager.login_message_category = 'info'\n\nclass User(db.Model, UserMixin):\n    id = db.Column(db.Integer, primary_key=True)\n    email = db.Column(db.String(120), unique=True, nullable=False)\n    password_hash = db.Column(db.String(256), nullable=False)\n    role = db.Column(db.String(20), default='user')\n\n    def set_password(self, password):\n        self.password_hash = generate_password_hash(password)\n\n    def check_password(self, password):\n        return check_password_hash(self.password_hash, password)\n\n@login_manager.user_loader\ndef load_user(user_id):\n    return User.query.get(int(user_id))\n\ndef admin_required(f):\n    @wraps(f)\n    def decorated_function(*args, **kwargs):\n        if not current_user.is_authenticated or current_user.role != 'admin':\n            abort(403)\n        return f(*args, **kwargs)\n    return decorated_function"
            },
            {
                "title": "Registration Controller with Duplicate Checks",
                "code": "@app.route('/register', methods=['GET', 'POST'])\ndef register():\n    if request.method == 'POST':\n        email = request.form.get('email', '').strip().lower()\n        password = request.form.get('password', '')\n        \n        if User.query.filter_by(email=email).first():\n            flash('An account with this email already exists.', 'warning')\n            return redirect(url_for('register'))\n            \n        user = User(email=email, role='user')\n        user.set_password(password)\n        db.session.add(user)\n        db.session.commit()\n        \n        flash('Registration successful! Please log in.', 'success')\n        return redirect(url_for('login'))\n    return render_template('auth/register.html')"
            },
            {
                "title": "Secure Login with Remember-Me",
                "code": "@app.route('/login', methods=['GET', 'POST'])\ndef login():\n    if current_user.is_authenticated:\n        return redirect(url_for('dashboard'))\n        \n    if request.method == 'POST':\n        email = request.form.get('email', '').strip().lower()\n        password = request.form.get('password', '')\n        remember = request.form.get('remember') == 'on'\n        \n        user = User.query.filter_by(email=email).first()\n        if user and user.check_password(password):\n            login_user(user, remember=remember)\n            next_page = request.args.get('next')\n            return redirect(next_page or url_for('dashboard'))\n            \n        flash('Invalid email or password.', 'danger')\n    return render_template('auth/login.html')"
            },
            {
                "title": "Admin Dashboard & Role Escalation",
                "code": "@app.route('/admin')\n@login_required\n@admin_required\ndef admin_dashboard():\n    all_users = User.query.all()\n    return render_template('admin/dashboard.html', users=all_users)"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Safe Next URL Redirection Validator",
            description="Write a function `is_safe_url(target)` that ensures a redirect target is a relative local URL (starts with '/' and does not start with '//'), mitigating Open Redirect phishing vulnerabilities.",
            starter_code="def is_safe_url(target):\n    # TODO: Validate relative URL\n    pass\n",
            solution_code="def is_safe_url(target):\n    if not target:\n        return False\n    return target.startswith('/') and not target.startswith('//')\n\nprint('Safe local:', is_safe_url('/dashboard'))\nprint('Phishing attempt:', is_safe_url('https://evil.com'))",
            expected_output="Safe local: True\nPhishing attempt: False"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Why is generic feedback like 'Invalid email or password' considered superior to 'Email not found'?",
                options=[
                    "It prevents attackers from compiling a verified list of registered user emails via account enumeration.",
                    "It requires less database processing.",
                    "Because Flask-Login crashes on specific error messages.",
                    "To prevent SQL injection."
                ],
                correct_answer="It prevents attackers from compiling a verified list of registered user emails via account enumeration.",
                explanation="Specific feedback allows attackers to test whether an email has an account on the platform."
            ),
            QuizQuestionBlueprint(
                question="What attack is prevented by validating the `next` query parameter during post-login redirects?",
                options=[
                    "Open Redirect phishing attacks.",
                    "Cross-Site Scripting (XSS).",
                    "SQL Injection.",
                    "Buffer Overflow."
                ],
                correct_answer="Open Redirect phishing attacks.",
                explanation="Unvalidated `next` redirects can send users to malicious external phishing clones."
            ),
            QuizQuestionBlueprint(
                question="Where does Flask-Login store the user ID between requests?",
                options=["In a cryptographically signed session cookie.", "In an unencrypted text file.", "In the browser URL bar.", "In local memory."],
                correct_answer="In a cryptographically signed session cookie.",
                explanation="Flask-Login serializes the user ID into the signed Flask session."
            ),
            QuizQuestionBlueprint(
                question="What method removes the active user's credentials from the session upon logout?",
                options=["logout_user()", "current_user.exit()", "session.kill()", "db.session.logout()"],
                correct_answer="logout_user()",
                explanation="`logout_user()` cleans up the session and removes remember-me cookies."
            ),
            QuizQuestionBlueprint(
                question="What should happen if an unauthenticated user attempts to visit an `@admin_required` route?",
                options=[
                    "They are first redirected to the login page via `@login_required`.",
                    "The server throws a 500 Internal Error.",
                    "Their IP address is immediately banned.",
                    "The route renders empty HTML."
                ],
                correct_answer="They are first redirected to the login page via `@login_required`.",
                explanation="Because `@login_required` runs first, unauthenticated visitors are sent to the login view."
            )
        ],
        is_project_day=True,
        project_name="Production Authentication & Authorization System"
    ),

    # -------------------------------------------------------------
    # DAY 28
    # -------------------------------------------------------------
    DayBlueprint(
        order=28,
        title="Day 28: Modular Architecture with Flask Blueprints",
        concept="Organizing large applications into decoupled, maintainable component modules using Blueprints",
        analogy="Think of a Flask Blueprint like a specialized department in a university. Instead of one single dean handling student admissions, engineering classes, cafeteria menus, and sports teams, each department (`admissions_bp`, `courses_bp`, `athletics_bp`) operates in its own wing with its own routes, templates, and managers!",
        theory_sections=[
            {
                "heading": "Why Single-File Apps Don't Scale",
                "body": "Putting 50 routes, 10 models, and 15 forms into a single `app.py` file creates spaghetti code. Flask Blueprints allow you to organize an application into reusable, self-contained sub-modules, each with its own route handlers, URL prefix, and dedicated templates."
            },
            {
                "heading": "Registering Blueprints with URL Prefixes",
                "body": "A Blueprint is instantiated using `bp = Blueprint('name', __name__, url_prefix='/prefix')`. In your main application setup, you register each component using `app.register_blueprint(auth_bp, url_prefix='/auth')`. When generating URLs for a blueprint route, prefix the function name with the blueprint name: `url_for('auth.login')`."
            }
        ],
        code_snippets=[
            {
                "title": "Creating an Authentication Blueprint (routes/auth.py)",
                "code": "from flask import Blueprint, render_template, redirect, url_for\n\n# Create Blueprint instance\nauth_bp = Blueprint('auth', __name__, template_folder='templates/auth')\n\n@auth_bp.route('/login')\ndef login():\n    return 'Render Login View'\n\n@auth_bp.route('/register')\ndef register():\n    return 'Render Register View'"
            },
            {
                "title": "Creating an API Blueprint (routes/api.py)",
                "code": "from flask import Blueprint, jsonify\n\napi_bp = Blueprint('api', __name__)\n\n@api_bp.route('/status')\ndef status():\n    return jsonify({'api_version': '1.0', 'status': 'operational'})"
            },
            {
                "title": "Registering Blueprints in app.py",
                "code": "from flask import Flask\nfrom routes.auth import auth_bp\nfrom routes.api import api_bp\n\napp = Flask(__name__)\n\n# Register blueprints with modular URL prefixes\napp.register_blueprint(auth_bp, url_prefix='/auth')\napp.register_blueprint(api_bp, url_prefix='/api/v1')"
            },
            {
                "title": "Referencing Blueprint Endpoints with url_for",
                "code": "from flask import url_for\n\nwith app.test_request_context():\n    # Syntax: url_for('blueprint_name.view_function')\n    login_url = url_for('auth.login')\n    api_url = url_for('api.status')\n    print('Auth URL:', login_url) # /auth/login\n    print('API URL:', api_url)   # /api/v1/status"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Blueprint Module Registration",
            description="Create a Blueprint named 'catalog' with url_prefix='/shop' containing a route '/items' returning 'Catalog Feed'. Register it onto a Flask app.",
            starter_code="from flask import Flask, Blueprint\n\n# TODO: Create catalog blueprint and register on app\n",
            solution_code="from flask import Flask, Blueprint\n\ncatalog_bp = Blueprint('catalog', __name__)\n\n@catalog_bp.route('/items')\ndef items():\n    return 'Catalog Feed'\n\napp = Flask(__name__)\napp.register_blueprint(catalog_bp, url_prefix='/shop')",
            expected_output="Blueprint catalog registered at /shop"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the primary architectural purpose of a Flask Blueprint?",
                options=[
                    "To structure large applications into modular, decoupled sets of views and assets.",
                    "To generate CSS styling automatically.",
                    "To run background asynchronous worker queues.",
                    "To compile Python into C extensions."
                ],
                correct_answer="To structure large applications into modular, decoupled sets of views and assets.",
                explanation="Blueprints allow teams to organize routes, models, and templates into clean functional modules."
            ),
            QuizQuestionBlueprint(
                question="How do you reverse-lookup a URL for a route named `profile` inside a blueprint named `user`?",
                options=["url_for('user.profile')", "url_for('profile')", "url_for('user/profile')", "url_for('blueprint.user.profile')"],
                correct_answer="url_for('user.profile')",
                explanation="Blueprint endpoints are namespaced using the dot syntax: `'blueprint_name.function_name'`."
            ),
            QuizQuestionBlueprint(
                question="What does the `url_prefix='/admin'` parameter do when registering a blueprint?",
                options=[
                    "Prepends `/admin` to every route defined within that blueprint.",
                    "Restricts access to administrators only.",
                    "Creates an admin database table.",
                    "Changes the port number to 8080."
                ],
                correct_answer="Prepends `/admin` to every route defined within that blueprint.",
                explanation="`url_prefix` namespaces all routes under that base path (e.g. `/admin/users`, `/admin/settings`)."
            ),
            QuizQuestionBlueprint(
                question="Can a Blueprint define its own dedicated template and static folders?",
                options=[
                    "Yes, via `template_folder` and `static_folder` constructor arguments.",
                    "No, all templates must live in the global root folder.",
                    "Only if using Docker.",
                    "Only in Flask 1.0."
                ],
                correct_answer="Yes, via `template_folder` and `static_folder` constructor arguments.",
                explanation="Blueprints can encapsulate their own templates and static assets for complete modularity."
            ),
            QuizQuestionBlueprint(
                question="How many times can a single Blueprint be registered onto a Flask application?",
                options=[
                    "Multiple times, each with a different URL prefix.",
                    "Only once per application instance.",
                    "Exactly twice.",
                    "Blueprints cannot be registered."
                ],
                correct_answer="Multiple times, each with a different URL prefix.",
                explanation="A blueprint can be mounted at different prefixes (e.g. `/api/v1` and `/api/v2`) if needed."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 29
    # -------------------------------------------------------------
    DayBlueprint(
        order=29,
        title="Day 29: The Application Factory Pattern (create_app)",
        concept="Decoupling extension instantiation from application creation using create_app() and environment configs",
        analogy="Think of the Application Factory Pattern like an automobile assembly line. Instead of building one single rigid car by hand that can never be modified, you build an automated factory machine (`create_app()`). You can tell the factory: 'Build me a lightweight test car for crash tests' or 'Build me a heavy-duty production car for the highway'!",
        theory_sections=[
            {
                "heading": "The Flaw of Global App Instances",
                "body": "Instantiating `app = Flask(__name__)` at the top level of your file creates circular import problems when models, views, and extensions all try to import `app` from each other. Furthermore, you cannot easily create separate application instances with different configurations for unit testing."
            },
            {
                "heading": "The create_app() Pattern",
                "body": "In the Application Factory pattern, extensions (like `db = SQLAlchemy()`) are instantiated globally without passing an `app`. An application factory function `create_app(config_name)` creates the Flask instance, applies configuration classes, calls `db.init_app(app)`, registers blueprints, and returns the finished app object."
            }
        ],
        code_snippets=[
            {
                "title": "Configuration Classes (config.py)",
                "code": "import os\n\nclass Config:\n    SECRET_KEY = os.getenv('SECRET_KEY', 'default-dev-secret')\n    SQLALCHEMY_TRACK_MODIFICATIONS = False\n\nclass DevelopmentConfig(Config):\n    DEBUG = True\n    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db'\n\nclass TestingConfig(Config):\n    TESTING = True\n    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'\n    WTF_CSRF_ENABLED = False\n\nclass ProductionConfig(Config):\n    DEBUG = False\n    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')"
            },
            {
                "title": "Decoupled Extensions (extensions.py)",
                "code": "from flask_sqlalchemy import SQLAlchemy\nfrom flask_login import LoginManager\nfrom flask_migrate import Migrate\n\n# Instantiated without an active app instance\ndb = SQLAlchemy()\nlogin_manager = LoginManager()\nmigrate = Migrate()"
            },
            {
                "title": "The Application Factory Function (app/__init__.py)",
                "code": "from flask import Flask\nfrom config import DevelopmentConfig, ProductionConfig\nfrom extensions import db, login_manager, migrate\nfrom routes.auth import auth_bp\n\ndef create_app(config_class=DevelopmentConfig):\n    app = Flask(__name__)\n    app.config.from_object(config_class)\n    \n    # Bind extensions to this specific app instance\n    db.init_app(app)\n    login_manager.init_app(app)\n    migrate.init_app(app, db)\n    \n    # Register blueprints\n    app.register_blueprint(auth_bp, url_prefix='/auth')\n    \n    return app"
            },
            {
                "title": "Entrypoint Runner (run.py)",
                "code": "from app import create_app\n\napp = create_app()\n\nif __name__ == '__main__':\n    app.run(port=5000)"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Application Factory Implementation",
            description="Write a minimal `create_app()` factory function that initializes a Flask app, loads a dictionary config, initializes an extension via `ext.init_app(app)`, and returns the app.",
            starter_code="from flask import Flask\n\n# TODO: Implement create_app factory\n",
            solution_code="from flask import Flask\n\nclass MockExt:\n    def init_app(self, app):\n        app.extension_loaded = True\n\next = MockExt()\n\ndef create_app(test_config=None):\n    app = Flask(__name__)\n    if test_config:\n        app.config.update(test_config)\n    ext.init_app(app)\n    return app\n\napp_instance = create_app({'TESTING': True})\nprint('App created with TESTING =', app_instance.config['TESTING'])",
            expected_output="App created with TESTING = True"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What major issue does the Application Factory pattern resolve in medium to large Flask codebases?",
                options=[
                    "Circular import dependencies between models, routes, and extensions.",
                    "Slow database query speeds.",
                    "CSS stylesheet rendering errors.",
                    "Incompatibility with modern browsers."
                ],
                correct_answer="Circular import dependencies between models, routes, and extensions.",
                explanation="Decoupling extension creation from app creation breaks circular import loops."
            ),
            QuizQuestionBlueprint(
                question="How do extensions like SQLAlchemy connect to a Flask app created inside a factory function?",
                options=["Using `extension.init_app(app)`", "Using `extension.bind(app)`", "Using `app.attach(extension)`", "Using `extension.connect()`"],
                correct_answer="Using `extension.init_app(app)`",
                explanation="The `init_app(app)` method binds an unattached extension instance to a specific Flask app."
            ),
            QuizQuestionBlueprint(
                question="Why is the factory pattern crucial for automated unit testing?",
                options=[
                    "It allows spinning up fresh, isolated app instances configured with in-memory test databases.",
                    "It automatically writes unit test assertions.",
                    "It bypasses Python's GIL.",
                    "It compiles tests into bytecode."
                ],
                correct_answer="It allows spinning up fresh, isolated app instances configured with in-memory test databases.",
                explanation="Each test suite can invoke `create_app(TestingConfig)` with isolated state."
            ),
            QuizQuestionBlueprint(
                question="Which method loads configuration parameters directly from a Python class object?",
                options=["app.config.from_object(ConfigClass)", "app.config.load(ConfigClass)", "app.config.read(ConfigClass)", "app.config.parse()"],
                correct_answer="app.config.from_object(ConfigClass)",
                explanation="`app.config.from_object()` reads all uppercase attributes from a class or module."
            ),
            QuizQuestionBlueprint(
                question="What does `sqlite:///:memory:` represent in a test configuration?",
                options=[
                    "A fast in-memory SQLite database that exists only in RAM and resets when the process ends.",
                    "A persistent disk file named ':memory:'.",
                    "A Redis cache server.",
                    "A mock PostgreSQL cloud instance."
                ],
                correct_answer="A fast in-memory SQLite database that exists only in RAM and resets when the process ends.",
                explanation="In-memory SQLite runs entirely in RAM, making unit tests fast and clean."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 30
    # -------------------------------------------------------------
    DayBlueprint(
        order=30,
        title="Day 30: RESTful APIs & JSON Responses (jsonify)",
        concept="Building machine-readable web APIs using HTTP status codes, structured JSON payloads, and jsonify()",
        analogy="Think of a RESTful API like a wholesale warehouse counter. Instead of serving customers with elaborate colorful dining plates and napkins (HTML templates and CSS), you deliver raw packaged crates stamped with exact barcode labels (`JSON` data) that any mobile app, frontend React app, or partner server can read!",
        theory_sections=[
            {
                "heading": "Principles of RESTful Web APIs",
                "body": "Representational State Transfer (REST) is an architectural style where resources are identified by URLs (e.g. `/api/v1/courses`), and actions are determined by standard HTTP methods: `GET` to read, `POST` to create, `PUT`/`PATCH` to update, and `DELETE` to remove. Responses are formatted as structured JSON."
            },
            {
                "heading": "Using Flask's jsonify() Helper",
                "body": "Flask's `jsonify()` function serializes Python dictionaries or lists into JSON strings, sets the `Content-Type: application/json` HTTP response header, and wraps the payload in a proper `Response` object. In modern Flask, returning a raw dictionary (e.g. `return {'key': 'val'}, 200`) also calls `jsonify` implicitly."
            }
        ],
        code_snippets=[
            {
                "title": "Returning Structured JSON Responses with jsonify",
                "code": "from flask import Flask, jsonify, request\n\napp = Flask(__name__)\n\n@app.route('/api/v1/health')\ndef health_check():\n    return jsonify({\n        'status': 'healthy',\n        'database': 'connected',\n        'uptime_seconds': 3600\n    }), 200"
            },
            {
                "title": "Parsing Incoming JSON Payloads with request.get_json()",
                "code": "@app.route('/api/v1/echo', methods=['POST'])\ndef echo_data():\n    # Extracts parsed dictionary from application/json body\n    data = request.get_json()\n    if not data:\n        return jsonify({'error': 'Missing or invalid JSON body'}), 400\n        \n    return jsonify({\n        'received': data,\n        'item_count': len(data)\n    }), 201"
            },
            {
                "title": "Standardized REST API Error Envelope",
                "code": "@app.errorhandler(404)\ndef api_not_found(error):\n    return jsonify({\n        'success': False,\n        'error': {\n            'code': 404,\n            'message': 'Requested API resource does not exist'\n        }\n    }), 404"
            },
            {
                "title": "Complete In-Memory REST Resource CRUD",
                "code": "COURSES = [{'id': 1, 'title': 'Flask Mastery'}, {'id': 2, 'title': 'Python Pro'}]\n\n@app.route('/api/courses', methods=['GET'])\ndef get_courses():\n    return jsonify({'courses': COURSES, 'total': len(COURSES)})\n\n@app.route('/api/courses/<int:course_id>', methods=['GET'])\ndef get_single_course(course_id):\n    course = next((c for c in COURSES if c['id'] == course_id), None)\n    if not course:\n        return jsonify({'error': 'Course not found'}), 404\n    return jsonify(course)"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="REST API Status Envelope",
            description="Write a Flask route `/api/ping` that returns a JSON response `{'ping': 'pong', 'timestamp': 1700000000}` with HTTP status code 200.",
            starter_code="from flask import Flask, jsonify\n\napp = Flask(__name__)\n\n# TODO: Implement /api/ping\n",
            solution_code="from flask import Flask, jsonify\n\napp = Flask(__name__)\n\n@app.route('/api/ping')\ndef ping():\n    return jsonify({'ping': 'pong', 'timestamp': 1700000000}), 200",
            expected_output="{\"ping\":\"pong\",\"timestamp\":1700000000}"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What HTTP `Content-Type` header is automatically set by Flask's `jsonify()`?",
                options=["application/json", "text/html", "application/javascript", "text/plain"],
                correct_answer="application/json",
                explanation="`jsonify` sets `Content-Type: application/json` so clients know to parse JSON."
            ),
            QuizQuestionBlueprint(
                question="How do you parse an incoming JSON payload sent in the body of a POST request?",
                options=["request.get_json()", "request.form.get('json')", "request.args.json()", "json.load(request)"],
                correct_answer="request.get_json()",
                explanation="`request.get_json()` parses the request body as JSON into a Python dictionary."
            ),
            QuizQuestionBlueprint(
                question="What HTTP status code should be returned when a client submits invalid or malformed JSON data?",
                options=["400 Bad Request", "404 Not Found", "500 Internal Error", "302 Redirect"],
                correct_answer="400 Bad Request",
                explanation="HTTP 400 indicates the client sent invalid input that the server cannot process."
            ),
            QuizQuestionBlueprint(
                question="What HTTP status code is standard when a resource is successfully deleted in REST?",
                options=["204 No Content (or 200 OK with confirmation)", "201 Created", "301 Moved", "403 Forbidden"],
                correct_answer="204 No Content (or 200 OK with confirmation)",
                explanation="204 No Content indicates successful execution with an empty response body."
            ),
            QuizQuestionBlueprint(
                question="Can modern Flask automatically serialize a returned Python dictionary to JSON without typing `jsonify()`?",
                options=[
                    "Yes, returning `{'status': 'ok'}` is automatically wrapped in jsonify by Flask 2.0+.",
                    "No, it always raises a TypeError.",
                    "Only if using Django extensions.",
                    "Only on GET requests."
                ],
                correct_answer="Yes, returning `{'status': 'ok'}` is automatically wrapped in jsonify by Flask 2.0+.",
                explanation="Modern Flask automatically converts dictionary returns into JSON responses."
            )
        ]
    ),
]
