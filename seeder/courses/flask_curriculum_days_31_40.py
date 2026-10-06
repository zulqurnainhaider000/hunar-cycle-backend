"""
Flask Mastery 40-Day Curriculum - Module 8 (Part 2), Module 9 & Module 10 (Days 31 to 40)
Module 8: RESTful APIs (Days 31-34)
Module 9: Real-Time & Background (Days 35-37)
Module 10: Production & Deployment (Days 38-40)
"""

from seeder.course_blueprint import DayBlueprint, QuizQuestionBlueprint, CodingChallengeBlueprint

DAYS_31_TO_40 = [
    # -------------------------------------------------------------
    # DAY 31
    # -------------------------------------------------------------
    DayBlueprint(
        order=31,
        title="Day 31: Class-Based API Views with Flask-RESTful & Smorest",
        concept="Structuring REST endpoints into clean Object-Oriented Resource classes",
        analogy="Think of class-based REST views like a multi-tool pocket knife. Instead of carrying separate loose tools for cutting, opening cans, and turning screws scattered across your toolbox (separate function routes for GET, POST, DELETE), you have one organized Swiss Army knife (`ProductResource`) with dedicated fold-out blades for each action!",
        theory_sections=[
            {
                "heading": "Limitations of Function-Based API Views",
                "body": "When building large RESTful APIs, writing function views that check `if request.method == 'GET': ... elif request.method == 'POST': ...` becomes repetitive and cluttered. Class-based views map HTTP verbs directly to class methods (`get()`, `post()`, `put()`, `delete()`), enforcing clean separation of concerns."
            },
            {
                "heading": "Flask-RESTful Resource Classes",
                "body": "Using libraries like Flask-RESTful, you create a class inheriting from `Resource`. Inside the class, you implement methods matching HTTP verbs. You then bind the resource to a URL rule using `api.add_resource(ProductResource, '/api/products/<int:id>')`."
            }
        ],
        code_snippets=[
            {
                "title": "Defining a Class-Based Resource",
                "code": "from flask import Flask, request\nfrom flask_restful import Resource, Api\n\napp = Flask(__name__)\napi = Api(app)\n\nPRODUCTS = {\n    1: {'name': 'Mechanical Keyboard', 'price': 120},\n    2: {'name': 'Ergonomic Mouse', 'price': 80}\n}\n\nclass ProductResource(Resource):\n    def get(self, product_id):\n        if product_id not in PRODUCTS:\n            return {'error': 'Product not found'}, 404\n        return PRODUCTS[product_id], 200\n\n    def delete(self, product_id):\n        if product_id in PRODUCTS:\n            del PRODUCTS[product_id]\n            return {'message': 'Product deleted'}, 200\n        return {'error': 'Product not found'}, 404\n\n# Register resource to URL endpoint\napi.add_resource(ProductResource, '/api/products/<int:product_id>')"
            },
            {
                "title": "Collection Resource for Listing and Creating",
                "code": "class ProductListResource(Resource):\n    def get(self):\n        return list(PRODUCTS.values()), 200\n\n    def post(self):\n        data = request.get_json()\n        new_id = max(PRODUCTS.keys(), default=0) + 1\n        PRODUCTS[new_id] = {'name': data['name'], 'price': data['price']}\n        return PRODUCTS[new_id], 201\n\napi.add_resource(ProductListResource, '/api/products')"
            },
            {
                "title": "Modern Flask MethodView (Native Alternative)",
                "code": "from flask.views import MethodView\n\nclass UserAPI(MethodView):\n    def get(self, user_id):\n        return {'user_id': user_id, 'status': 'active'}\n\n    def post(self):\n        return {'created': True}, 201\n\n# Register MethodView without third-party extensions\napp.add_url_rule('/users/<int:user_id>', view_func=UserAPI.as_view('user_api'))"
            },
            {
                "title": "Custom Error Handling in Flask-RESTful",
                "code": "errors = {\n    'UserAlreadyExistsError': {\n        'message': 'A user with that email already exists.',\n        'status': 409,\n    },\n}\napi = Api(app, errors=errors)"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Class-Based Task Resource",
            description="Declare a class `TaskResource` inheriting from `Resource` with a `get(self, task_id)` method returning `{'task_id': task_id, 'completed': False}`, 200.",
            starter_code="from flask_restful import Resource\n\n# TODO: Implement TaskResource\n",
            solution_code="from flask_restful import Resource\n\nclass TaskResource(Resource):\n    def get(self, task_id):\n        return {'task_id': task_id, 'completed': False}, 200\n\nr = TaskResource()\nprint(r.get(10))",
            expected_output="({'task_id': 10, 'completed': False}, 200)"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="In a Flask-RESTful `Resource` class, how do you handle an incoming HTTP GET request?",
                options=[
                    "By defining a method named `def get(self, ...):`.",
                    "By using the `@app.route` decorator inside the class.",
                    "By defining a method named `def handle_request(self):`.",
                    "By implementing `__call__`."
                ],
                correct_answer="By defining a method named `def get(self, ...):`.",
                explanation="Flask-RESTful maps HTTP verbs directly to lowercase method names (`get`, `post`, `put`, `delete`)."
            ),
            QuizQuestionBlueprint(
                question="What method on `Api` connects a Resource class to an endpoint route pattern?",
                options=["api.add_resource(ResourceClass, '/path')", "api.register(ResourceClass)", "api.mount(ResourceClass)", "app.add_resource()"],
                correct_answer="api.add_resource(ResourceClass, '/path')",
                explanation="`api.add_resource()` binds a Resource class to one or more URL rules."
            ),
            QuizQuestionBlueprint(
                question="What is the built-in Flask alternative to Flask-RESTful for class-based views without extra packages?",
                options=["MethodView from `flask.views`", "ClassRoute from `flask`", "ViewFactory", "EndpointClass"],
                correct_answer="MethodView from `flask.views`",
                explanation="`flask.views.MethodView` provides native class-based HTTP method dispatching in vanilla Flask."
            ),
            QuizQuestionBlueprint(
                question="What HTTP status code is returned by convention when creating a new resource via `post()` in a Resource?",
                options=["201 Created", "200 OK", "204 No Content", "202 Accepted"],
                correct_answer="201 Created",
                explanation="HTTP 201 Created indicates successful creation of a resource."
            ),
            QuizQuestionBlueprint(
                question="Can a single Resource class be bound to multiple URL patterns in `add_resource`?",
                options=[
                    "Yes, e.g. `api.add_resource(ItemResource, '/item', '/item/<int:id>')`.",
                    "No, only one URL pattern is allowed per Resource.",
                    "Only if using HTTPS.",
                    "Only on Windows."
                ],
                correct_answer="Yes, e.g. `api.add_resource(ItemResource, '/item', '/item/<int:id>')`.",
                explanation="`api.add_resource()` accepts multiple URL string arguments for flexible routing."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 32
    # -------------------------------------------------------------
    DayBlueprint(
        order=32,
        title="Day 32: Data Serialization & Validation with Marshmallow",
        concept="Validating incoming JSON payloads and serializing complex ORM models using Marshmallow Schemas",
        analogy="Think of Marshmallow like a high-speed customs checkpoint. When incoming cargo (JSON) arrives from abroad, customs officers (`schema.load()`) verify that the papers are signed, no prohibited items exist, and numbers match specifications. When exporting goods (`schema.dump()`), they package complex factory items into neat, standard export cartons!",
        theory_sections=[
            {
                "heading": "The Two Pillars of Marshmallow: Dump and Load",
                "body": "Marshmallow is an ORM-agnostic serialization and data validation library. It performs two core tasks: (1) **Serialization (Dumping)**: Converting complex Python/SQLAlchemy objects into native Python datatypes that easily render to JSON. (2) **Deserialization & Validation (Loading)**: Validating incoming JSON dictionaries against strict rules and transforming them into clean Python objects."
            },
            {
                "heading": "Defining Schemas and Field Validators",
                "body": "You define a class inheriting from `marshmallow.Schema`. Fields are defined using types like `fields.String()`, `fields.Email()`, `fields.Integer()`, and `fields.Nested()`. You attach validators such as `validate.Length(min=3)` or custom `@validates` methods."
            }
        ],
        code_snippets=[
            {
                "title": "Defining a User Schema with Validation",
                "code": "from marshmallow import Schema, fields, validate, ValidationError\n\nclass UserSchema(Schema):\n    id = fields.Integer(dump_only=True) # Included when serializing, ignored on input\n    username = fields.String(required=True, validate=validate.Length(min=3, max=30))\n    email = fields.Email(required=True)\n    age = fields.Integer(validate=validate.Range(min=13, max=120))\n    created_at = fields.DateTime(dump_only=True)"
            },
            {
                "title": "Validating Input Payload with schema.load()",
                "code": "user_schema = UserSchema()\n\nincoming_json = {'username': 'alidev', 'email': 'ali@example.com', 'age': 24}\n\ntry:\n    # Validates and cleans incoming dictionary\n    clean_data = user_schema.load(incoming_json)\n    print('Validation passed:', clean_data)\nexcept ValidationError as err:\n    print('Validation errors:', err.messages)"
            },
            {
                "title": "Serializing SQLAlchemy Model with schema.dump()",
                "code": "# Serialize single object\nuser_json = user_schema.dump(user_db_instance)\n\n# Serialize list of objects (many=True)\nusers_schema = UserSchema(many=True)\nall_users_json = users_schema.dump(User.query.all())"
            },
            {
                "title": "Flask-Marshmallow SQLAlchemyAutoSchema",
                "code": "from flask_marshmallow import Marshmallow\n\nma = Marshmallow(app)\n\nclass AutoUserSchema(ma.SQLAlchemyAutoSchema):\n    class Meta:\n        model = User\n        load_instance = True # Deserializes directly into SQLAlchemy model instance"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Product Payload Schema Validator",
            description="Create a Marshmallow `ProductSchema` with `name` (String, required=True, min length 2) and `price` (Float, required=True, min value 0.01).",
            starter_code="from marshmallow import Schema, fields, validate\n\n# TODO: Declare ProductSchema\n",
            solution_code="from marshmallow import Schema, fields, validate\n\nclass ProductSchema(Schema):\n    name = fields.String(required=True, validate=validate.Length(min=2))\n    price = fields.Float(required=True, validate=validate.Range(min=0.01))\n\nschema = ProductSchema()\nprint('Valid:', schema.load({'name': 'Pen', 'price': 1.99}))",
            expected_output="Valid: {'name': 'Pen', 'price': 1.99}"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What method on a Marshmallow Schema validates an incoming dictionary and returns clean data?",
                options=["schema.load(data)", "schema.validate(data)", "schema.parse(data)", "schema.clean(data)"],
                correct_answer="schema.load(data)",
                explanation="`schema.load()` deserializes and validates incoming dictionaries, raising `ValidationError` on failure."
            ),
            QuizQuestionBlueprint(
                question="What method on a Marshmallow Schema serializes a Python/SQLAlchemy model into a JSON-compatible dictionary?",
                options=["schema.dump(obj)", "schema.serialize(obj)", "schema.to_json(obj)", "schema.export(obj)"],
                correct_answer="schema.dump(obj)",
                explanation="`schema.dump()` serializes complex objects into primitive Python dictionaries."
            ),
            QuizQuestionBlueprint(
                question="What attribute setting marks a field to be included during serialization but ignored during deserialization input?",
                options=["dump_only=True", "readonly=True", "output_only=True", "serialize_only=True"],
                correct_answer="dump_only=True",
                explanation="`dump_only=True` fields (like auto-incremented primary keys) are output-only."
            ),
            QuizQuestionBlueprint(
                question="How do you configure a schema to serialize a list of multiple database objects?",
                options=["Schema(many=True)", "Schema(list=True)", "Schema(batch=True)", "Schema.all()"],
                correct_answer="Schema(many=True)",
                explanation="Passing `many=True` tells the schema to iterate over an iterable collection of items."
            ),
            QuizQuestionBlueprint(
                question="What exception is raised by Marshmallow when loaded data fails validation constraints?",
                options=["marshmallow.exceptions.ValidationError", "ValueError", "DataError", "InvalidSchemaException"],
                correct_answer="marshmallow.exceptions.ValidationError",
                explanation="`ValidationError` contains an `.messages` dictionary detailing the field-specific errors."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 33
    # -------------------------------------------------------------
    DayBlueprint(
        order=33,
        title="Day 33: JWT (JSON Web Tokens) Authentication",
        concept="Implementing stateless API authentication using Flask-JWT-Extended and Bearer access tokens",
        analogy="Think of a JSON Web Token like an encrypted digital ski pass with an embedded clock. When you buy the pass at the lodge (login), the machine signs it cryptographically with an expiration timestamp of 6 PM. Every ski lift on the mountain (`@jwt_required()`) can verify the signature and time without calling central headquarters!",
        theory_sections=[
            {
                "heading": "Why Sessions Don't Work for Mobile & SPAs",
                "body": "Cookie-based sessions rely on browser cookie storage and are vulnerable to CSRF when consumed by cross-origin Single Page Applications (React, Next.js) or native mobile apps (React Native). JSON Web Tokens (JWT) provide a stateless, digitally signed token that clients attach in the `Authorization: Bearer <token>` header."
            },
            {
                "heading": "The Anatomy of a JWT",
                "body": "A JWT consists of three base64url-encoded parts separated by dots: **Header** (algorithm), **Payload** (claims like `sub` user_id and expiration `exp`), and **Signature** (HMAC-SHA256 signature generated with your secret key). With `Flask-JWT-Extended`, you protect routes using `@jwt_required()` and retrieve identity via `get_jwt_identity()`."
            }
        ],
        code_snippets=[
            {
                "title": "Configuring Flask-JWT-Extended",
                "code": "from flask import Flask, jsonify, request\nfrom flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity\nfrom datetime import timedelta\n\napp = Flask(__name__)\napp.config['JWT_SECRET_KEY'] = 'jwt-super-secret-key'\napp.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)\n\njwt = JWTManager(app)"
            },
            {
                "title": "Generating Access Tokens upon Login",
                "code": "@app.route('/api/login', methods=['POST'])\ndef api_login():\n    data = request.get_json() or {}\n    email = data.get('email')\n    password = data.get('password')\n    \n    # Simulate user credential validation\n    if email == 'admin@example.com' and password == 'secret123':\n        # Create cryptographically signed token with user identity\n        access_token = create_access_token(identity=email)\n        return jsonify({'token': access_token, 'token_type': 'Bearer'}), 200\n        \n    return jsonify({'error': 'Invalid credentials'}), 401"
            },
            {
                "title": "Protecting Endpoints with @jwt_required()",
                "code": "@app.route('/api/profile', methods=['GET'])\n@jwt_required()\ndef get_profile():\n    # Retrieves user identity stored inside the verified JWT\n    current_user_email = get_jwt_identity()\n    return jsonify({\n        'email': current_user_email,\n        'authenticated': True,\n        'tier': 'Pro Developer'\n    }), 200"
            },
            {
                "title": "Customizing JWT Error Responses",
                "code": "@jwt.unauthorized_loader\ndef missing_token_callback(error_string):\n    return jsonify({\n        'error': 'Authorization token is missing',\n        'message': 'Include header Authorization: Bearer <token>'\n    }), 401"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Token Generation Endpoint",
            description="Write a Python route `/api/token` that takes a username query parameter and returns `{'access_token': create_access_token(identity=username)}`.",
            starter_code="from flask import Flask, jsonify, request\nfrom flask_jwt_extended import JWTManager, create_access_token\n\napp = Flask(__name__)\napp.config['JWT_SECRET_KEY'] = 'test-key'\njwt = JWTManager(app)\n\n# TODO: Implement /api/token\n",
            solution_code="from flask import Flask, jsonify, request\nfrom flask_jwt_extended import JWTManager, create_access_token\n\napp = Flask(__name__)\napp.config['JWT_SECRET_KEY'] = 'test-key'\njwt = JWTManager(app)\n\n@app.route('/api/token')\ndef generate_token():\n    user = request.args.get('user', 'guest')\n    token = create_access_token(identity=user)\n    return jsonify({'access_token': token}), 200",
            expected_output="JWT access token generated"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What standard HTTP header does a client use to submit a JWT access token?",
                options=["Authorization: Bearer <token>", "Token: <token>", "JWT: <token>", "Authentication: Key <token>"],
                correct_answer="Authorization: Bearer <token>",
                explanation="The standard HTTP authorization scheme uses the `Authorization: Bearer <jwt_token>` format."
            ),
            QuizQuestionBlueprint(
                question="What function retrieves the subject identity (e.g. user ID or email) from an authenticated JWT?",
                options=["get_jwt_identity()", "current_jwt_user()", "jwt.get_user()", "request.jwt_id"],
                correct_answer="get_jwt_identity()",
                explanation="`get_jwt_identity()` parses and returns the identity payload stored inside the token."
            ),
            QuizQuestionBlueprint(
                question="What decorator in Flask-JWT-Extended enforces that requests must include a valid, unexpired token?",
                options=["@jwt_required()", "@require_jwt", "@token_auth", "@jwt_protected"],
                correct_answer="@jwt_required()",
                explanation="`@jwt_required()` validates the token signature and expiration, rejecting invalid requests with 401."
            ),
            QuizQuestionBlueprint(
                question="What are the three structural segments of a standard JSON Web Token?",
                options=[
                    "Header, Payload, and Signature.",
                    "User, Password, and Salt.",
                    "Host, Port, and Path.",
                    "Key, IV, and Ciphertext."
                ],
                correct_answer="Header, Payload, and Signature.",
                explanation="JWTs consist of Header, Payload (claims), and cryptographic Signature separated by dots."
            ),
            QuizQuestionBlueprint(
                question="Why is stateless JWT authentication advantageous for microservices and mobile backends?",
                options=[
                    "The server does not need to query a shared session store in memory to verify user identity on every request.",
                    "JWT tokens cannot be intercepted.",
                    "JWT tokens never expire.",
                    "It eliminates the need for database passwords."
                ],
                correct_answer="The server does not need to query a shared session store in memory to verify user identity on every request.",
                explanation="Stateless verification allows any server with the secret key to authenticate requests without centralized session memory."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 34 (Major Project)
    # -------------------------------------------------------------
    DayBlueprint(
        order=34,
        title="Day 34: E-Commerce RESTful API Major Project",
        concept="Architecting a complete production-grade E-Commerce REST API with JWT Auth, Product Catalog, and Orders",
        analogy="Think of building this E-Commerce API like engineering the backend nerve center of Amazon. You have warehouse inventory (Products), shoppers checking out shopping carts (Orders), and secure digital ID cards (JWT Auth). Mobile apps and web stores worldwide connect through standard JSON doorways!",
        theory_sections=[
            {
                "heading": "Enterprise REST API Architecture",
                "body": "In this major milestone project, you engineer a full-featured E-Commerce RESTful API. The system exposes modular resource endpoints: Authentication (`/api/auth/register`, `/api/auth/login`), Product Catalog (`/api/products`), and Order Checkout (`/api/orders`). All protected mutations enforce JWT security."
            },
            {
                "heading": "Handling Transactions and Inventory Deductions",
                "body": "When placing an order, decrementing product inventory and creating the order record must happen within an atomic database transaction. If inventory is insufficient, the transaction rolls back cleanly, returning HTTP 400 Bad Request."
            }
        ],
        code_snippets=[
            {
                "title": "E-Commerce Database Models (models.py)",
                "code": "from datetime import datetime\nfrom flask_sqlalchemy import SQLAlchemy\n\ndb = SQLAlchemy()\n\nclass Product(db.Model):\n    __tablename__ = 'products'\n    id = db.Column(db.Integer, primary_key=True)\n    name = db.Column(db.String(100), nullable=False)\n    price = db.Column(db.Float, nullable=False)\n    stock = db.Column(db.Integer, default=0)\n\nclass Order(db.Model):\n    __tablename__ = 'orders'\n    id = db.Column(db.Integer, primary_key=True)\n    user_email = db.Column(db.String(120), nullable=False)\n    total_amount = db.Column(db.Float, nullable=False)\n    created_at = db.Column(db.DateTime, default=datetime.utcnow)\n    items = db.relationship('OrderItem', backref='order', lazy=True)\n\nclass OrderItem(db.Model):\n    __tablename__ = 'order_items'\n    id = db.Column(db.Integer, primary_key=True)\n    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))\n    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))\n    quantity = db.Column(db.Integer, nullable=False)\n    price = db.Column(db.Float, nullable=False)"
            },
            {
                "title": "Atomic Checkout Controller with Inventory Locking",
                "code": "@app.route('/api/orders', methods=['POST'])\n@jwt_required()\ndef create_order():\n    buyer_email = get_jwt_identity()\n    data = request.get_json()\n    items = data.get('items', [])\n    \n    if not items:\n        return jsonify({'error': 'Order must contain items'}), 400\n        \n    total_cost = 0.0\n    order_items = []\n    \n    try:\n        for item in items:\n            product = Product.query.get(item['product_id'])\n            if not product or product.stock < item['quantity']:\n                return jsonify({'error': f'Insufficient stock for product {item[\"product_id\"]}'}), 400\n                \n            product.stock -= item['quantity']\n            item_cost = product.price * item['quantity']\n            total_cost += item_cost\n            order_items.append(OrderItem(product_id=product.id, quantity=item['quantity'], price=product.price))\n            \n        new_order = Order(user_email=buyer_email, total_amount=total_cost, items=order_items)\n        db.session.add(new_order)\n        db.session.commit() # Atomic commit for both order and stock deduction\n        \n        return jsonify({'order_id': new_order.id, 'total': total_cost, 'status': 'confirmed'}), 201\n    except Exception as e:\n        db.session.rollback()\n        return jsonify({'error': 'Checkout failed'}), 500"
            },
            {
                "title": "Product Catalog Filter Endpoint",
                "code": "@app.route('/api/products', methods=['GET'])\ndef list_products():\n    min_p = request.args.get('min_price', type=float)\n    max_p = request.args.get('max_price', type=float)\n    \n    query = Product.query\n    if min_p is not None:\n        query = query.filter(Product.price >= min_p)\n    if max_p is not None:\n        query = query.filter(Product.price <= max_p)\n        \n    products = query.all()\n    return jsonify([{'id': p.id, 'name': p.name, 'price': p.price, 'stock': p.stock} for p in products])"
            },
            {
                "title": "Order History for Authenticated User",
                "code": "@app.route('/api/my-orders', methods=['GET'])\n@jwt_required()\ndef get_user_orders():\n    user_email = get_jwt_identity()\n    orders = Order.query.filter_by(user_email=user_email).order_by(Order.created_at.desc()).all()\n    return jsonify([{\n        'order_id': o.id,\n        'total': o.total_amount,\n        'date': o.created_at.isoformat()\n    } for o in orders])"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Cart Price Calculator Engine",
            description="Write a function `calculate_cart_total(items, product_catalog)` that returns the total price given a list of item dictionaries `{'product_id': int, 'qty': int}` and catalog `{id: price}`.",
            starter_code="def calculate_cart_total(items, catalog):\n    # TODO: Calculate sum\n    pass\n",
            solution_code="def calculate_cart_total(items, catalog):\n    total = 0.0\n    for item in items:\n        price = catalog.get(item['product_id'], 0.0)\n        total += price * item['qty']\n    return round(total, 2)\n\ncat = {1: 15.50, 2: 40.00}\ncart = [{'product_id': 1, 'qty': 2}, {'product_id': 2, 'qty': 1}]\nprint('Total:', calculate_cart_total(cart, cat))",
            expected_output="Total: 71.0"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Why is `db.session.rollback()` called inside the `except` block during multi-step order checkout?",
                options=[
                    "To revert all stock deductions and database mutations so the database is never left in an inconsistent state.",
                    "To delete the user's account.",
                    "To cancel the user's internet connection.",
                    "It increases database speed."
                ],
                correct_answer="To revert all stock deductions and database mutations so the database is never left in an inconsistent state.",
                explanation="Rollbacks guarantee atomicity: either all changes commit successfully, or all changes are reverted."
            ),
            QuizQuestionBlueprint(
                question="What HTTP status code is standard when creating a new Order resource successfully?",
                options=["201 Created", "200 OK", "202 Accepted", "204 No Content"],
                correct_answer="201 Created",
                explanation="201 Created indicates successful creation of the new Order entity."
            ),
            QuizQuestionBlueprint(
                question="How does the checkout endpoint know which customer placed the order?",
                options=[
                    "It extracts the authenticated user's email from the verified JWT via `get_jwt_identity()`.",
                    "The client submits an unverified customer_id in the body.",
                    "By inspecting the client's screen resolution.",
                    "By reading the user's hard drive."
                ],
                correct_answer="It extracts the authenticated user's email from the verified JWT via `get_jwt_identity()`.",
                explanation="Deriving identity from the cryptographically verified JWT prevents impersonation."
            ),
            QuizQuestionBlueprint(
                question="What happens if a shopper requests 5 units of a product that only has 2 units in stock?",
                options=[
                    "The API rejects the transaction with HTTP 400 Bad Request and an informative error message.",
                    "The product stock becomes negative (-3).",
                    "The server crashes.",
                    "The order is placed with a random product."
                ],
                correct_answer="The API rejects the transaction with HTTP 400 Bad Request and an informative error message.",
                explanation="Inventory validation checks prevent negative stock and invalid orders."
            ),
            QuizQuestionBlueprint(
                question="What method formats datetime objects into standardized ISO-8601 strings (e.g. `2026-09-30T10:00:00`) for JSON APIs?",
                options=["datetime.isoformat()", "datetime.to_json()", "str(datetime)", "datetime.export()"],
                correct_answer="datetime.isoformat()",
                explanation="`.isoformat()` produces universally recognizable ISO-8601 date strings for frontend parsing."
            )
        ],
        is_project_day=True,
        project_name="E-Commerce RESTful API Major Project"
    ),

    # -------------------------------------------------------------
    # DAY 35
    # -------------------------------------------------------------
    DayBlueprint(
        order=35,
        title="Day 35: Asynchronous Background Tasks with Celery & Redis",
        concept="Offloading slow operations (email dispatch, video rendering, report generation) to Celery worker processes",
        analogy="Think of Celery like hiring a delivery courier for a busy bakery. When a customer orders a birthday cake, the counter clerk (Flask web worker) shouldn't jump in a delivery van and drive across the city for 45 minutes while other customers wait in line. Instead, the clerk hands the box to a courier (Celery worker via Redis message queue) and immediately attends to the next customer!",
        theory_sections=[
            {
                "heading": "The Blocking Request Anti-Pattern",
                "body": "If an HTTP request performs a task that takes 5 seconds (such as sending an SMTP email or generating an invoice PDF), the user's browser freezes waiting for the response, and that web worker cannot serve other visitors. Heavy background tasks must be offloaded to an asynchronous task queue."
            },
            {
                "heading": "Celery Architecture with Redis Broker",
                "body": "Celery is an asynchronous distributed task queue. Flask submits task parameters to a message broker (Redis). Independent Celery worker processes pick up tasks from Redis, execute them in the background, and store results. The Flask route immediately responds with HTTP 202 Accepted."
            }
        ],
        code_snippets=[
            {
                "title": "Instantiating Celery with Redis Broker",
                "code": "from flask import Flask\nfrom celery import Celery\n\ndef make_celery(app):\n    celery = Celery(\n        app.import_name,\n        broker=app.config['CELERY_BROKER_URL'],\n        backend=app.config['CELERY_RESULT_BACKEND']\n    )\n    celery.conf.update(app.config)\n    return celery\n\napp = Flask(__name__)\napp.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'\napp.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'\n\ncelery = make_celery(app)"
            },
            {
                "title": "Defining an Asynchronous Background Task",
                "code": "import time\n\n@celery.task\ndef send_welcome_email(user_email, name):\n    # Simulate slow SMTP network request\n    print(f'Starting email dispatch to {user_email}...')\n    time.sleep(5)\n    print(f'Email successfully sent to {user_email}!')\n    return {'status': 'sent', 'recipient': user_email}"
            },
            {
                "title": "Dispatching Task from Flask Route with .delay()",
                "code": "@app.route('/api/signup', methods=['POST'])\ndef signup():\n    data = request.get_json()\n    # .delay() pushes task to Redis and returns immediately without blocking!\n    task = send_welcome_email.delay(data['email'], data['name'])\n    \n    # Returns 202 Accepted with task tracking ID\n    return jsonify({\n        'message': 'Signup successful! Welcome email is being sent.',\n        'task_id': task.id\n    }), 202"
            },
            {
                "title": "Checking Task Execution Status",
                "code": "@app.route('/api/task-status/<task_id>')\ndef get_status(task_id):\n    task = send_welcome_email.AsyncResult(task_id)\n    return jsonify({\n        'task_id': task_id,\n        'state': task.state,\n        'result': task.result if task.ready() else None\n    })"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Background Task Dispatcher",
            description="Write a Python mock script that demonstrates dispatching a task with `.delay()` and returning a task status dictionary containing 'task_id' and 'status': 'queued'.",
            starter_code="# TODO: Implement task dispatch simulation\n",
            solution_code="class MockTask:\n    def __init__(self, task_id):\n        self.id = task_id\n\ndef dispatch_async(job_name, *args):\n    task = MockTask('uuid-1234-5678')\n    return {'task_id': task.id, 'status': 'queued', 'job': job_name}\n\nprint(dispatch_async('generate_report', 101))",
            expected_output="{'task_id': 'uuid-1234-5678', 'status': 'queued', 'job': 'generate_report'}"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What method is called on a Celery task function to dispatch it asynchronously to the worker queue?",
                options=[".delay(*args, **kwargs)", ".run_async()", ".dispatch()", ".background()"],
                correct_answer=".delay(*args, **kwargs)",
                explanation="`.delay()` is the standard shortcut to serialize arguments and enqueue the task."
            ),
            QuizQuestionBlueprint(
                question="What role does Redis play in a Celery + Flask architecture?",
                options=[
                    "It acts as the in-memory message broker that queues tasks between Flask and Celery workers.",
                    "It stores HTML templates.",
                    "It compiles Python code into C.",
                    "It acts as the DNS server."
                ],
                correct_answer="It acts as the in-memory message broker that queues tasks between Flask and Celery workers.",
                explanation="Redis buffers tasks in memory until Celery workers pull and process them."
            ),
            QuizQuestionBlueprint(
                question="What HTTP status code is standard for requests that successfully accept background work for later processing?",
                options=["202 Accepted", "200 OK", "201 Created", "204 No Content"],
                correct_answer="202 Accepted",
                explanation="HTTP 202 Accepted means the request has been accepted for processing, but processing is not complete."
            ),
            QuizQuestionBlueprint(
                question="Why should slow third-party API calls (like sending emails) never be executed synchronously in a Flask route?",
                options=[
                    "They block the web worker thread, freezing the user's browser and reducing server request capacity.",
                    "They cause database table corruption.",
                    "Flask throws an AsyncViolationError.",
                    "Browsers do not support requests longer than 100 milliseconds."
                ],
                correct_answer="They block the web worker thread, freezing the user's browser and reducing server request capacity.",
                explanation="Blocking calls tie up WSGI worker threads, severely degrading throughput."
            ),
            QuizQuestionBlueprint(
                question="How can a client monitor the progress of a background task dispatched via Celery?",
                options=[
                    "By querying a status endpoint with the task's unique UUID tracking ID (`AsyncResult(task_id)`).",
                    "By refreshing the entire operating system.",
                    "Celery tasks cannot be tracked.",
                    "By reading the server's CPU temperature."
                ],
                correct_answer="By querying a status endpoint with the task's unique UUID tracking ID (`AsyncResult(task_id)`).",
                explanation="`AsyncResult(task_id).state` returns status flags like PENDING, STARTED, and SUCCESS."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 36
    # -------------------------------------------------------------
    DayBlueprint(
        order=36,
        title="Day 36: High-Performance Caching with Flask-Caching & Redis",
        concept="Accelerating database queries and route rendering using memory caching and @cache.cached decorators",
        analogy="Think of caching like a student keeping sticky notes on their desk instead of walking to the university library 50 times a day. If you already calculated the answer to a complex math problem 5 minutes ago, you just glance at the sticky note on your desk (`Redis Cache`) in 1 millisecond instead of recalculating for 10 minutes!",
        theory_sections=[
            {
                "heading": "Why Caching is Critical for High-Traffic Apps",
                "body": "Database queries and template rendering require CPU, memory, and disk I/O. If 1,000 visitors load the homepage simultaneously, querying the database 1,000 times for identical data is inefficient. Caching stores the pre-rendered response in fast in-memory storage (Redis), serving subsequent requests in microseconds."
            },
            {
                "heading": "Using Flask-Caching Decorators",
                "body": "Flask-Caching provides `@cache.cached(timeout=60)`, which caches the entire route response for 60 seconds. For caching individual expensive function calculations based on arguments, use `@cache.memoize(timeout=300)`. Cache keys can be invalidated manually when underlying data updates using `cache.delete()`."
            }
        ],
        code_snippets=[
            {
                "title": "Configuring Flask-Caching with Redis Backend",
                "code": "from flask import Flask, jsonify\nfrom flask_caching import Cache\nimport time\n\napp = Flask(__name__)\n\n# Configure Redis cache backend\napp.config['CACHE_TYPE'] = 'RedisCache'\napp.config['CACHE_REDIS_URL'] = 'redis://localhost:6379/1'\napp.config['CACHE_DEFAULT_TIMEOUT'] = 300\n\ncache = Cache(app)"
            },
            {
                "title": "Caching an Entire View with @cache.cached",
                "code": "@app.route('/api/stats')\n@cache.cached(timeout=60) # Caches response for 60 seconds\ndef get_heavy_stats():\n    print('Executing expensive computation...')\n    time.sleep(2) # Simulates heavy calculation\n    return jsonify({\n        'active_users': 14820,\n        'total_revenue': 892000,\n        'cached_at': time.time()\n    })"
            },
            {
                "title": "Function Memoization with @cache.memoize",
                "code": "@cache.memoize(timeout=600)\ndef calculate_user_reputation(user_id):\n    # Caches result based on the user_id argument value\n    print(f'Calculating reputation score for user {user_id}...')\n    return user_id * 42 + 7"
            },
            {
                "title": "Manual Cache Invalidation",
                "code": "@app.route('/api/update-catalog', methods=['POST'])\ndef update_catalog():\n    # Purge cached catalog view so users see fresh data immediately\n    cache.delete('view//api/stats')\n    return jsonify({'message': 'Catalog updated and cache purged!'})"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="In-Memory Cache Simulator",
            description="Implement a simple Python caching decorator `simple_cache(ttl_seconds)` that stores function results in a dictionary and serves cached data if called within the TTL window.",
            starter_code="import time\n\n# TODO: Implement simple_cache decorator\n",
            solution_code="import time\n\ncache_store = {}\n\ndef simple_cache(key, val, ttl=60):\n    cache_store[key] = {'val': val, 'expires': time.time() + ttl}\n\ndef get_cache(key):\n    item = cache_store.get(key)\n    if item and time.time() < item['expires']:\n        return item['val']\n    return None\n\nsimple_cache('rate', 25.5, ttl=100)\nprint('Cached Rate:', get_cache('rate'))",
            expected_output="Cached Rate: 25.5"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What decorator in Flask-Caching stores the rendered output of a view for a given number of seconds?",
                options=["@cache.cached(timeout=60)", "@cache.store(60)", "@cache.view()", "@app.cache_route()"],
                correct_answer="@cache.cached(timeout=60)",
                explanation="`@cache.cached(timeout=seconds)` caches the view's return value."
            ),
            QuizQuestionBlueprint(
                question="What is the difference between `@cache.cached` and `@cache.memoize`?",
                options=[
                    "`cached` caches the route URL; `memoize` caches function results based on the specific arguments passed.",
                    "`memoize` only works with templates.",
                    "`cached` is deprecated.",
                    "`memoize` does not support timeouts."
                ],
                correct_answer="`cached` caches the route URL; `memoize` caches function results based on the specific arguments passed.",
                explanation="`memoize` hashes the function arguments to key separate cache entries for each input."
            ),
            QuizQuestionBlueprint(
                question="What is 'cache invalidation' in web performance engineering?",
                options=[
                    "Purging or updating cached entries when the underlying database data changes so users don't see stale information.",
                    "Deleting the entire database.",
                    "Disabling the cache permanently.",
                    "Restarting the operating system."
                ],
                correct_answer="Purging or updating cached entries when the underlying database data changes so users don't see stale information.",
                explanation="Cache invalidation prevents users from seeing stale data after an update occurs."
            ),
            QuizQuestionBlueprint(
                question="Why is in-memory Redis preferred over simple filesystem caching for production web clusters?",
                options=[
                    "Redis is shared across multiple server nodes and runs at RAM speed with zero disk I/O latency.",
                    "Redis is built into Python by default.",
                    "Filesystem cache can only hold 10 items.",
                    "Redis encrypts images."
                ],
                correct_answer="Redis is shared across multiple server nodes and runs at RAM speed with zero disk I/O latency.",
                explanation="Redis provides centralized, lightning-fast in-memory caching accessible by all app instances."
            ),
            QuizQuestionBlueprint(
                question="What happens when a cache entry's `timeout` duration expires?",
                options=[
                    "The cache key is evicted; the next request will execute the view and recalculate the fresh result.",
                    "The server throws a 504 Gateway Timeout.",
                    "The web server restarts.",
                    "The browser crashes."
                ],
                correct_answer="The cache key is evicted; the next request will execute the view and recalculate the fresh result.",
                explanation="Expired keys trigger a cache miss, prompting the application to regenerate fresh data."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 37 (Project)
    # -------------------------------------------------------------
    DayBlueprint(
        order=37,
        title="Day 37: Real-Time Live Chat with Flask-SocketIO Project",
        concept="Developing bi-directional, full-duplex communication channels using WebSockets and SocketIO rooms",
        analogy="Think of HTTP like sending letters in the mail: you send a letter (request), and wait for a reply (response). Think of WebSockets like an open telephone call between you and your friend: both of you can speak and listen simultaneously at the exact same millisecond without redialing the phone number!",
        theory_sections=[
            {
                "heading": "HTTP Polling vs WebSockets",
                "body": "Traditional HTTP requires clients to poll the server repeatedly (`GET /messages` every 2 seconds) to receive updates, wasting immense network bandwidth. WebSockets establish a single persistent, bi-directional TCP connection, allowing the server to push real-time events to connected clients with sub-millisecond latency."
            },
            {
                "heading": "Flask-SocketIO Architecture: Rooms and Broadcasting",
                "body": "Flask-SocketIO integrates WebSocket communication into Flask. You listen for events using `@socketio.on('event_name')`, send messages with `emit('event_name', data, broadcast=True)`, and organize users into private chat channels using `join_room(room_name)` and `leave_room(room_name)`."
            }
        ],
        code_snippets=[
            {
                "title": "Configuring Flask-SocketIO (server.py)",
                "code": "from flask import Flask, render_template, request\nfrom flask_socketio import SocketIO, emit, join_room, leave_room\n\napp = Flask(__name__)\napp.config['SECRET_KEY'] = 'socketio-chat-secret'\n\n# Initialize SocketIO with cross-origin support\nsocketio = SocketIO(app, cors_allowed_origins='*')\n\n@app.route('/')\ndef chat_page():\n    return render_template('chat.html')\n\nif __name__ == '__main__':\n    # Note: Use socketio.run instead of app.run!\n    socketio.run(app, debug=True, port=5000)"
            },
            {
                "title": "Handling SocketIO Events and Broadcasting",
                "code": "@socketio.on('send_message')\ndef handle_send_message(data):\n    user = data.get('username', 'Anonymous')\n    text = data.get('message', '')\n    room = data.get('room', 'general')\n    \n    payload = {'user': user, 'text': text}\n    # Broadcast message to all connected clients in the specified room\n    emit('receive_message', payload, to=room)"
            },
            {
                "title": "Managing Chat Rooms (join_room & leave_room)",
                "code": "@socketio.on('join')\ndef on_join(data):\n    username = data['username']\n    room = data['room']\n    join_room(room)\n    emit('system_notification', {'msg': f'{username} has joined {room}.'}, to=room)\n\n@socketio.on('leave')\ndef on_leave(data):\n    username = data['username']\n    room = data['room']\n    leave_room(room)\n    emit('system_notification', {'msg': f'{username} has left {room}.'}, to=room)"
            },
            {
                "title": "Client-Side WebSocket Connection (chat.html)",
                "code": "<!-- Include Socket.IO client library -->\n<script src=\"https://cdn.socket.io/4.7.2/socket.io.min.js\"></script>\n<script>\n    const socket = io();\n    \n    // Connect to general room\n    socket.emit('join', { username: 'Zubair', room: 'general' });\n    \n    // Listen for incoming messages\n    socket.on('receive_message', (data) => {\n        console.log(`${data.user}: ${data.text}`);\n        // Append message to UI DOM\n    });\n    \n    // Send message to server\n    function sendMessage(text) {\n        socket.emit('send_message', { username: 'Zubair', message: text, room: 'general' });\n    }\n</script>"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Chat Message Payload Validator",
            description="Write a function `validate_chat_payload(data)` that checks if 'username' (3-20 chars) and 'message' (1-200 chars) are present and valid, returning (is_valid, sanitized_dict).",
            starter_code="def validate_chat_payload(data):\n    # TODO: Validate chat payload\n    pass\n",
            solution_code="def validate_chat_payload(data):\n    user = data.get('username', '').strip()\n    msg = data.get('message', '').strip()\n    if not (3 <= len(user) <= 20) or not (1 <= len(msg) <= 200):\n        return (False, None)\n    return (True, {'username': user, 'message': msg})\n\nprint(validate_chat_payload({'username': 'Ali', 'message': 'Hello team!'}))",
            expected_output="(True, {'username': 'Ali', 'message': 'Hello team!'})"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What protocol do WebSockets use to maintain a persistent bi-directional communication channel?",
                options=["ws:// and wss:// over TCP", "http:// over UDP", "ftp://", "smtp://"],
                correct_answer="ws:// and wss:// over TCP",
                explanation="WebSockets upgrade standard HTTP connections to `ws://` (or encrypted `wss://`) over TCP."
            ),
            QuizQuestionBlueprint(
                question="How do you launch a Flask-SocketIO application in Python instead of using `app.run()`?",
                options=["socketio.run(app)", "app.socketio_start()", "flask.start_sockets()", "run_websocket(app)"],
                correct_answer="socketio.run(app)",
                explanation="`socketio.run(app)` handles the asynchronous WSGI server (like Eventlet or Gevent)."
            ),
            QuizQuestionBlueprint(
                question="What parameter in `emit()` sends an event to every client in a specific channel?",
                options=["to='room_name'", "channel='room_name'", "target='room_name'", "group='room_name'"],
                correct_answer="to='room_name'",
                explanation="`emit('event', data, to='room_name')` routes the message to all clients in that room."
            ),
            QuizQuestionBlueprint(
                question="What decorator handles custom incoming WebSocket messages sent by clients?",
                options=["@socketio.on('event_name')", "@socketio.listen()", "@app.websocket()", "@socket.route()"],
                correct_answer="@socketio.on('event_name')",
                explanation="`@socketio.on('event_name')` binds an event listener to incoming messages with that tag."
            ),
            QuizQuestionBlueprint(
                question="What function adds the current client socket connection into a named channel room?",
                options=["join_room('room_name')", "add_to_room()", "socket.enter_room()", "subscribe()"],
                correct_answer="join_room('room_name')",
                explanation="`join_room('room_name')` subscribes the active client session to that room's broadcast events."
            )
        ],
        is_project_day=True,
        project_name="Real-Time Live Chat with Flask-SocketIO"
    ),

    # -------------------------------------------------------------
    # DAY 38
    # -------------------------------------------------------------
    DayBlueprint(
        order=38,
        title="Day 38: Unit Testing Flask Applications with Pytest",
        concept="Writing automated test suites using pytest fixtures, Flask test client, and database assertions",
        analogy="Think of automated unit testing like the safety crash-test facility of an automotive company. Before a newly designed car is allowed on public highways with families inside, engineers crash-test the brakes, airbags, and seatbelts in a closed laboratory (`pytest`). If any test fails, the car stays in the shop until fixed!",
        theory_sections=[
            {
                "heading": "Why Automated Testing is Mandatory",
                "body": "Manually clicking around your website after every small code edit is slow, tedious, and misses regression bugs. Automated unit testing verifies that endpoints, database models, and authentication logic continue working reliably every time you make changes."
            },
            {
                "heading": "The Flask Test Client and Pytest Fixtures",
                "body": "Flask includes a built-in test client (`app.test_client()`) that simulates HTTP requests (GET, POST, headers, cookies) entirely in memory without launching a real web server. Using `pytest` fixtures, you spin up isolated test databases, run assertions on status codes and JSON responses, and reset state."
            }
        ],
        code_snippets=[
            {
                "title": "Configuring Pytest Fixtures (conftest.py)",
                "code": "import pytest\nfrom app import create_app\nfrom extensions import db\nfrom config import TestingConfig\n\n@pytest.fixture\ndef app():\n    app = create_app(TestingConfig)\n    with app.app_context():\n        db.create_all()\n        yield app\n        db.session.remove()\n        db.drop_all()\n\n@pytest.fixture\ndef client(app):\n    # Provides simulated HTTP test client\n    return app.test_client()"
            },
            {
                "title": "Testing HTTP GET and Status Codes (test_routes.py)",
                "code": "def test_homepage_status(client):\n    response = client.get('/')\n    assert response.status_code == 200\n    assert b'Welcome to Hunar Cycle' in response.data"
            },
            {
                "title": "Testing POST API Endpoints with JSON Payloads",
                "code": "def test_create_user_api(client):\n    payload = {'email': 'test@example.com', 'password': 'Password123!'}\n    response = client.post('/api/users', json=payload)\n    \n    assert response.status_code == 201\n    json_data = response.get_json()\n    assert json_data['email'] == 'test@example.com'\n    assert 'id' in json_data"
            },
            {
                "title": "Testing Authenticated Routes with Headers",
                "code": "def test_protected_route_requires_auth(client):\n    # Unauthenticated request should fail\n    res = client.get('/api/protected')\n    assert res.status_code == 401\n    \n    # Request with valid simulated Bearer token\n    res_auth = client.get('/api/protected', headers={'Authorization': 'Bearer test-valid-token'})\n    assert res_auth.status_code == 200"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Endpoint Test Assertion Script",
            description="Write a test function `test_status_endpoint(client)` that makes a GET request to '/health', asserting status_code == 200 and JSON response['status'] == 'ok'.",
            starter_code="# TODO: Implement test_status_endpoint\ndef test_status_endpoint(client):\n    pass\n",
            solution_code="def test_status_endpoint(client):\n    response = client.get('/health')\n    assert response.status_code == 200\n    data = response.get_json()\n    assert data['status'] == 'ok'\n    print('Test passed: Health endpoint verified!')",
            expected_output="Health endpoint test verified"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What method on a Flask application provides a simulated HTTP client for unit tests?",
                options=["app.test_client()", "app.get_client()", "app.client()", "app.simulate()"],
                correct_answer="app.test_client()",
                explanation="`app.test_client()` creates a test client that sends mock requests to Flask's WSGI interface."
            ),
            QuizQuestionBlueprint(
                question="What pytest decorator defines reusable setup and teardown components (like test apps or mock databases)?",
                options=["@pytest.fixture", "@pytest.setup", "@pytest.component", "@pytest.dependency"],
                correct_answer="@pytest.fixture",
                explanation="`@pytest.fixture` functions provide dependencies that test functions receive as arguments."
            ),
            QuizQuestionBlueprint(
                question="How do you parse the JSON response body from a test client response object?",
                options=["response.get_json()", "response.json()", "json.loads(response.data)", "Both response.get_json() and json.loads()"],
                correct_answer="Both response.get_json() and json.loads()",
                explanation="`response.get_json()` is Flask's convenience helper; `json.loads(response.data)` also works."
            ),
            QuizQuestionBlueprint(
                question="What parameter is passed to `client.post()` to automatically encode a payload as JSON and set headers?",
                options=["client.post('/url', json=payload)", "client.post('/url', data=payload)", "client.post('/url', body=payload)", "client.post('/url', payload=payload)"],
                correct_answer="client.post('/url', json=payload)",
                explanation="The `json=` keyword argument serializes the dictionary and sets `Content-Type: application/json`."
            ),
            QuizQuestionBlueprint(
                question="Why is it best practice to use in-memory SQLite (`sqlite:///:memory:`) during unit test suites?",
                options=[
                    "It is extremely fast, runs completely in RAM, and resets cleanly between test suites.",
                    "Because PostgreSQL cannot run tests.",
                    "It prevents internet connection timeouts.",
                    "It bypasses authentication checks."
                ],
                correct_answer="It is extremely fast, runs completely in RAM, and resets cleanly between test suites.",
                explanation="In-memory databases execute in microseconds without leaving residual disk clutter."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 39
    # -------------------------------------------------------------
    DayBlueprint(
        order=39,
        title="Day 39: Environment Configuration & Gunicorn Production Server",
        concept="Preparing Flask applications for enterprise deployment with python-dotenv and Gunicorn WSGI workers",
        analogy="Think of Flask's built-in development server (`app.run()`) like a bicycle: great for cruising around your neighborhood driveway while learning. But when you need to transport 50 passengers on the highway, you need an industrial multi-cylinder bus engine (`Gunicorn` with multiple worker processes)!",
        theory_sections=[
            {
                "heading": "The 12-Factor App & Environment Variables",
                "body": "Never hardcode passwords, secret keys, or database URLs in your Git repository. The Twelve-Factor App methodology mandates storing configuration in environment variables. Using `python-dotenv`, Flask automatically loads `.env` files locally while reading system environment variables in production."
            },
            {
                "heading": "Production WSGI Servers (Gunicorn)",
                "body": "Flask's development server is single-threaded and not designed for security or concurrency. Production deployments use a Production WSGI HTTP Server like **Gunicorn** (Green Unicorn). Gunicorn manages a master process and forks multiple worker processes to handle hundreds of concurrent requests in parallel."
            }
        ],
        code_snippets=[
            {
                "title": "Loading Secrets from .env with python-dotenv",
                "code": "# .env file (add this to .gitignore!)\n# SECRET_KEY=f9bf78b9a18ce6d46a0c66a0b5\n# DATABASE_URL=postgresql://user:pass@db-host:5432/proddb\n# FLASK_ENV=production\n\nimport os\nfrom dotenv import load_dotenv\n\n# Load variables from .env into os.environ\nload_dotenv()\n\nsecret_key = os.getenv('SECRET_KEY')\ndatabase_url = os.getenv('DATABASE_URL')"
            },
            {
                "title": "Configuring Gunicorn CLI Command",
                "code": "# In production terminal (Linux/macOS):\n# gunicorn --workers=4 --bind=0.0.0.0:8000 'app:create_app()'\n\n# Formula for optimal worker count: (2 * NUM_CORES) + 1\n# Example on a 2-Core VM: (2 * 2) + 1 = 5 workers"
            },
            {
                "title": "Dedicated Gunicorn Config File (gunicorn.conf.py)",
                "code": "import multiprocessing\n\nbind = \"0.0.0.0:8000\"\nworkers = multiprocessing.cpu_count() * 2 + 1\nworker_class = \"gevent\" # Asynchronous worker model\ntimeout = 120\nkeepalive = 5\naccesslog = \"/var/log/gunicorn/access.log\"\nerrorlog = \"/var/log/gunicorn/error.log\""
            },
            {
                "title": "Reverse Proxy Architecture (Nginx + Gunicorn)",
                "code": "# Standard Enterprise Architecture:\n# [Client Browser] -> HTTPS (Port 443) -> [Nginx Reverse Proxy]\n#                                                 |\n#                                                 v (Port 8000)\n#                                       [Gunicorn WSGI Master]\n#                                        /    |    \\    \\\n#                                      [W1]  [W2]  [W3]  [W4] (Flask instances)"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Optimal Worker Calculator",
            description="Write a function `calculate_gunicorn_workers(cpu_cores)` that returns the recommended Gunicorn worker count using the standard formula `(2 * cpu_cores) + 1`.",
            starter_code="def calculate_gunicorn_workers(cpu_cores):\n    # TODO: Calculate worker count\n    pass\n",
            solution_code="def calculate_gunicorn_workers(cpu_cores):\n    return (2 * cpu_cores) + 1\n\nprint('Recommended Workers for 4 Cores:', calculate_gunicorn_workers(4))",
            expected_output="Recommended Workers for 4 Cores: 9"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Why is Flask's built-in development server (`app.run()`) unsuitable for production deployment?",
                options=[
                    "It is single-threaded, lacks process concurrency, and is not audited for production security vulnerabilities.",
                    "It cannot connect to PostgreSQL.",
                    "It cannot serve HTML files.",
                    "It requires a graphical desktop screen."
                ],
                correct_answer="It is single-threaded, lacks process concurrency, and is not audited for production security vulnerabilities.",
                explanation="Flask's dev server is designed for local debugging, not handling concurrent traffic spikes."
            ),
            QuizQuestionBlueprint(
                question="What is the standard formula recommended by Gunicorn documentation to calculate the optimal worker count?",
                options=["(2 * CPU_CORES) + 1", "CPU_CORES * 4", "CPU_CORES * 10", "Fixed at 8 workers"],
                correct_answer="(2 * CPU_CORES) + 1",
                explanation="The standard rule of thumb for Gunicorn CPU-bound workers is `(2 * num_cores) + 1`."
            ),
            QuizQuestionBlueprint(
                question="What library loads key-value pairs from a local `.env` file into `os.environ`?",
                options=["python-dotenv", "flask-env", "env-loader", "config-parser"],
                correct_answer="python-dotenv",
                explanation="`python-dotenv` reads `.env` files and populates Python's `os.environ` dictionary."
            ),
            QuizQuestionBlueprint(
                question="Why should `.env` files always be included in `.gitignore`?",
                options=[
                    "To prevent committing sensitive API keys, database passwords, and secrets into source control.",
                    "Because Git cannot track hidden files.",
                    "Because .env files corrupt Git branches.",
                    "To reduce repository download time."
                ],
                correct_answer="To prevent committing sensitive API keys, database passwords, and secrets into source control.",
                explanation="Committing `.env` files leaks passwords and cryptographic keys to anyone with repo access."
            ),
            QuizQuestionBlueprint(
                question="In a production architecture, what web server typically sits in front of Gunicorn to handle SSL and static files?",
                options=["Nginx (or Apache)", "Node.js", "Redis", "SQLite"],
                correct_answer="Nginx (or Apache)",
                explanation="Nginx acts as a reverse proxy, terminating SSL, buffering slow clients, and serving static files directly."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 40 (Capstone)
    # -------------------------------------------------------------
    DayBlueprint(
        order=40,
        title="Day 40: Dockerizing & Cloud Deployment Capstone",
        concept="Packaging Flask applications into containerized Docker images and orchestrating with Docker Compose",
        analogy="Think of Docker like standardized shipping containers on cargo ships. Before shipping containers, loading different shapes of cars, bananas, and furniture onto a ship was chaotic and took days. A Docker container packages your exact Python version, dependencies, and code into one standard cargo box that runs identically on your laptop, AWS, Google Cloud, or Azure!",
        theory_sections=[
            {
                "heading": "The Power of Containerization with Docker",
                "body": "'It worked on my machine but broke on the server' is the most common complaint in software engineering. Docker packages your Python runtime, system libraries, code, and dependencies into an immutable container image, guaranteeing that your application executes identically in development, staging, and production."
            },
            {
                "heading": "Multi-Container Orchestration with Docker Compose",
                "body": "Modern web systems are composed of multiple services: the Flask web server, a PostgreSQL database, and a Redis cache. `docker-compose.yml` allows you to define, network, and boot up this entire multi-container infrastructure with a single terminal command: `docker compose up -d`."
            }
        ],
        code_snippets=[
            {
                "title": "Production Dockerfile for Flask",
                "code": "# Use official lightweight Python base image\nFROM python:3.11-slim\n\n# Prevent Python from writing .pyc files and buffer stdout\nENV PYTHONDONTWRITEBYTECODE=1\nENV PYTHONUNBUFFERED=1\n\nWORKDIR /app\n\n# Install system dependencies\nRUN apt-get update && apt-get install -y --no-install-recommends gcc libpq-dev && rm -rf /var/lib/apt/lists/*\n\n# Copy requirements first to leverage Docker layer caching\nCOPY requirements.txt .\nRUN pip install --no-cache-dir -r requirements.txt\n\n# Copy source code\nCOPY . .\n\n# Expose Gunicorn port\nEXPOSE 8000\n\n# Run with production Gunicorn server\nCMD [\"gunicorn\", \"--workers=3\", \"--bind=0.0.0.0:8000\", \"run:app\"]"
            },
            {
                "title": "Multi-Service Orchestration (docker-compose.yml)",
                "code": "version: '3.8'\n\nservices:\n  web:\n    build: .\n    ports:\n      - \"8000:8000\"\n    environment:\n      - DATABASE_URL=postgresql://admin:secret123@db:5432/flaskdb\n      - REDIS_URL=redis://redis:6379/0\n      - SECRET_KEY=prod-super-secret\n    depends_on:\n      - db\n      - redis\n\n  db:\n    image: postgres:15-alpine\n    environment:\n      - POSTGRES_USER=admin\n      - POSTGRES_PASSWORD=secret123\n      - POSTGRES_DB=flaskdb\n    volumes:\n      - postgres_data:/var/lib/postgresql/data\n\n  redis:\n    image: redis:7-alpine\n    ports:\n      - \"6379:6379\"\n\nvolumes:\n  postgres_data:"
            },
            {
                "title": "Essential Docker CLI Commands",
                "code": "# Build image:\n# docker build -t my-flask-app:latest .\n\n# Run container:\n# docker run -d -p 8000:8000 --env-file .env my-flask-app:latest\n\n# Start full stack with Docker Compose:\n# docker compose up --build -d\n\n# View live logs:\n# docker compose logs -f web"
            },
            {
                "title": "Container Healthcheck Endpoint",
                "code": "@app.route('/healthz')\ndef healthcheck():\n    # Docker and Kubernetes ping this endpoint to verify container readiness\n    try:\n        db.session.execute(db.text('SELECT 1'))\n        return jsonify({'status': 'healthy', 'db': 'ok'}), 200\n    except Exception as e:\n        return jsonify({'status': 'unhealthy', 'error': str(e)}), 500"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Docker Compose Service Validator",
            description="Write a Python script that verifies if required services ('web', 'db', 'redis') are present in a mock docker-compose services dictionary.",
            starter_code="compose_config = {\n    'services': {'web': {}, 'db': {}}\n}\n# TODO: Validate that web, db, and redis are defined\n",
            solution_code="compose_config = {\n    'services': {'web': {}, 'db': {}, 'redis': {}}\n}\nrequired = {'web', 'db', 'redis'}\nmissing = required - set(compose_config['services'].keys())\nif not missing:\n    print('All core services configured in docker-compose!')\nelse:\n    print(f'Missing services: {missing}')",
            expected_output="All core services configured in docker-compose!"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Why is `COPY requirements.txt .` followed by `RUN pip install` placed before `COPY . .` in a Dockerfile?",
                options=[
                    "To leverage Docker layer caching so dependencies are not reinstalled every time source code changes.",
                    "Because pip refuses to run if Python files exist in the directory.",
                    "To reduce image size to zero bytes.",
                    "It is required by Docker syntax."
                ],
                correct_answer="To leverage Docker layer caching so dependencies are not reinstalled every time source code changes.",
                explanation="Docker caches unchanged layers, drastically speeding up subsequent image builds."
            ),
            QuizQuestionBlueprint(
                question="What terminal command starts all services defined in a `docker-compose.yml` file in the background?",
                options=["docker compose up -d", "docker start all", "docker compose run", "docker launch"],
                correct_answer="docker compose up -d",
                explanation="`docker compose up -d` boots containers in detached (background) mode."
            ),
            QuizQuestionBlueprint(
                question="Why is persistent data stored in a Docker `volume` for database services like PostgreSQL?",
                options=[
                    "Containers are ephemeral; without volumes, all database data is erased when the container stops or restarts.",
                    "PostgreSQL cannot write to container hard drives.",
                    "To compress database tables.",
                    "To enable multi-threading."
                ],
                correct_answer="Containers are ephemeral; without volumes, all database data is erased when the container stops or restarts.",
                explanation="Volumes map storage outside the ephemeral container lifecycle to preserve data."
            ),
            QuizQuestionBlueprint(
                question="What instruction in a Dockerfile defines the default command executed when a container boots?",
                options=["CMD", "START", "RUN", "BOOT"],
                correct_answer="CMD",
                explanation="`CMD [\"executable\", \"arg1\", ...]` specifies the container entrypoint process."
            ),
            QuizQuestionBlueprint(
                question="What is the purpose of a `/healthz` endpoint in containerized cloud deployments (Kubernetes / AWS ECS)?",
                options=[
                    "It allows cloud orchestrators to periodically probe if the container is healthy and automatically restart it if unresponsive.",
                    "It measures server electricity usage.",
                    "It generates API documentation.",
                    "It sends marketing telemetry to Docker Inc."
                ],
                correct_answer="It allows cloud orchestrators to periodically probe if the container is healthy and automatically restart it if unresponsive.",
                explanation="Healthcheck probes tell load balancers and orchestrators whether to route traffic to the container."
            )
        ],
        is_project_day=True,
        project_name="Dockerizing & Cloud Deployment Capstone"
    ),
]
