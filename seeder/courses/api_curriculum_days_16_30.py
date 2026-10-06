"""
Complete APIs & Web Services Architecture Curriculum - Days 16 to 30
Phase 3: REST Architecture (The Core Rules) - Part 2 (Days 16-18)
Phase 4: API Design & Best Practices (Building APIs) (Days 19-26)
Phase 5: API Security & Authentication - Part 1 (Days 27-30 of 27-34)
"""

from seeder.course_blueprint import DayBlueprint, QuizQuestionBlueprint, CodingChallengeBlueprint

DAYS_16_TO_30 = [
    # ----------------------------------------------------
    # Day 16: Resources & Resource Identifiers (Nouns, Not Verbs)
    # ----------------------------------------------------
    DayBlueprint(
        order=16,
        title="Day 16: Resources & Resource Identifiers (Nouns, Not Verbs)",
        concept="Designing clean, intuitive RESTful URIs by modeling resources as plural nouns and using HTTP verbs for actions rather than embedding verbs in endpoints.",
        analogy="Think of a library catalog. The cards in the catalog are labeled with subjects and book titles (nouns: 'Books', 'Authors', 'Magazines'). You don't have a card called 'PleaseGiveMeThisBookNow()'; your action (checking out or returning) is separate from the noun on the card.",
        theory_sections=[
            {
                "heading": "The Cardinal Rule of RESTful URI Design",
                "body": (
                    "> **\"URIs must identify Resources (nouns), NEVER actions (verbs)!\"**\n\n"
                    "The most common mistake junior developers make is embedding actions into the URL path:\n"
                    "- ❌ `POST /api/createUser`\n"
                    "- ❌ `GET /api/getUserById?id=42`\n"
                    "- ❌ `POST /api/deleteProduct/10`\n"
                    "In REST, the HTTP verb *is* the action. The URI *is* the resource.\n"
                    "- ✅ `POST /api/users` (Create user)\n"
                    "- ✅ `GET /api/users/42` (Retrieve user)\n"
                    "- ✅ `DELETE /api/products/10` (Delete product)"
                )
            },
            {
                "heading": "Collection Resources vs Singleton Resources",
                "body": (
                    "REST divides endpoints into two primary patterns:\n"
                    "1. **Collection Resource**: Represents a set or list of entities. Always named with a plural noun: `/users`, `/articles`, `/invoices`.\n"
                    "2. **Singleton / Instance Resource**: Represents a single entity within a collection: `/users/42`, `/articles/101`.\n"
                    "Occasionally, singletons with no collection exist, such as `/profile` (the currently authenticated user's settings)."
                )
            },
            {
                "heading": "Handling Non-CRUD Actions in REST",
                "body": (
                    "What about operations that don't map neatly to CRUD, such as 'resending a verification email' or 'canceling an order'?\n"
                    "- Approach 1 (Sub-resource creation): `POST /orders/42/cancellations`\n"
                    "- Approach 2 (State patch): `PATCH /orders/42` with body `{\"status\": \"canceled\"}`\n"
                    "- Approach 3 (Controller sub-resource): `POST /users/42/resend-verification`"
                )
            }
        ],
        code_snippets=[
            {
                "title": "Anti-Pattern vs RESTful URI Comparison",
                "code": "# Bad (RPC-Style Verbs in URL)       | Clean RESTful Equivalent\n# ------------------------------------+------------------------------------\n# GET /api/getAllCustomers           | GET /api/customers\n# POST /api/createNewCustomer        | POST /api/customers\n# POST /api/updateCustomer?id=12     | PUT /api/customers/12 (or PATCH)\n# GET /api/deleteCustomer/12         | DELETE /api/customers/12\n# GET /api/searchBooksByAuthor?auth=J | GET /api/books?author=J",
                "explanation": "Translates RPC action-oriented URLs into canonical RESTful noun-based patterns."
            },
            {
                "title": "Collection and Singleton Routing in Express",
                "code": "const express = require('express');\nconst app = express();\n\n// Collection Resource (/products)\napp.get('/api/v1/products', (req, res) => {\n    res.json([{ id: 1, name: 'Keyboard' }, { id: 2, name: 'Mouse' }]);\n});\n\n// Singleton Resource (/products/:id)\napp.get('/api/v1/products/:id', (req, res) => {\n    res.json({ id: req.params.id, name: 'Keyboard', price: 99.00 });\n});",
                "explanation": "Express routing distinguishing between collection list and individual entity."
            },
            {
                "title": "Nested Sub-Resource Hierarchies",
                "code": "# Representing natural parent-child relationships in URLs:\n# Users have Orders, Orders have Line Items:\n\n# List all orders belonging to user 42:\nGET /api/v1/users/42/orders\n\n# Create a new order for user 42:\nPOST /api/v1/users/42/orders\n\n# Fetch a specific order #108 belonging to user 42:\nGET /api/v1/users/42/orders/108",
                "explanation": "Nested hierarchical URIs reflect domain data relationships."
            },
            {
                "title": "Limiting Nesting Depth (Rule of Thumb)",
                "code": "# Anti-pattern: Deep nesting becomes unreadable and brittle:\n# GET /api/v1/regions/north/stores/5/aisles/3/shelves/2/products/99\n\n# Best Practice: Avoid nesting deeper than 2 levels! Flatten to direct singleton:\n# GET /api/v1/products/99",
                "explanation": "Keep URI hierarchies shallow to maintain developer sanity."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Refactor RPC Route to RESTful Pattern",
            description="Write down the proper RESTful HTTP method and URL path for an endpoint previously called `POST /api/v1/modifyUserPassword?userId=77`.",
            starter_code="# Method: ?\n# URL: ?\n",
            solution_code="# Method: PATCH\n# URL: /api/v1/users/77/password",
            expected_output="PATCH /api/v1/users/77/password"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="According to REST design standards, which grammatical type should be used for naming resource URIs?",
                options=["Plural Nouns (e.g. `/users`, `/products`)", "Verbs (e.g. `/getUsers`, `/deleteItem`)", "Adverbs", "Abbreviations only"],
                correct_answer="Plural Nouns (e.g. `/users`, `/products`)",
                explanation="URIs identify resources (nouns), while the HTTP method specifies the action (verb)."
            ),
            QuizQuestionBlueprint(
                question="Why is `GET /api/deleteUser?id=5` considered a dangerous anti-pattern in web architecture?",
                options=[
                    "`GET` must be safe and idempotent; search crawlers or browser pre-fetching could trigger `GET` requests and accidentally delete user accounts",
                    "URLs with numbers are illegal in HTTP",
                    "GET requests can only be sent by iPhones",
                    "It causes database encryption failure"
                ],
                correct_answer="`GET` must be safe and idempotent; search crawlers or browser pre-fetching could trigger `GET` requests and accidentally delete user accounts",
                explanation="GET must never alter server state; search bots aggressively crawl GET links."
            ),
            QuizQuestionBlueprint(
                question="What is the difference between a Collection resource and a Singleton resource?",
                options=[
                    "A Collection represents a list of entities (`/orders`); a Singleton represents a specific unique entity (`/orders/123`)",
                    "A Collection is stored on the client; a Singleton is on the server",
                    "A Collection is written in C++; a Singleton is written in Python",
                    "A Collection requires payment; a Singleton is free"
                ],
                correct_answer="A Collection represents a list of entities (`/orders`); a Singleton represents a specific unique entity (`/orders/123`)",
                explanation="Collections group multiple entities; singletons identify individual instances."
            ),
            QuizQuestionBlueprint(
                question="What is the recommended rule of thumb regarding the maximum nesting depth for RESTful resource paths?",
                options=[
                    "Limit nesting to a maximum of 2 levels (e.g. `/users/1/orders`); deeper resources should be addressed directly by their own ID",
                    "At least 10 levels deep",
                    "Never use any slashes",
                    "Only 1 level allowed in the entire API"
                ],
                correct_answer="Limit nesting to a maximum of 2 levels (e.g. `/users/1/orders`); deeper resources should be addressed directly by their own ID",
                explanation="Deeply nested URIs become unwieldy; flattening to top-level singletons improves readability."
            ),
            QuizQuestionBlueprint(
                question="How should a non-CRUD action like 'canceling an order' be modeled cleanly in a RESTful API?",
                options=[
                    "Either as a state update (`PATCH /orders/42` with `{\"status\": \"canceled\"}`) or as a sub-resource (`POST /orders/42/cancellations`)",
                    "By creating a new database table called `CanceledOrders`",
                    "By running a SQL command directly in the URL",
                    "By sending an email to the server administrator"
                ],
                correct_answer="Either as a state update (`PATCH /orders/42` with `{\"status\": \"canceled\"}`) or as a sub-resource (`POST /orders/42/cancellations`)",
                explanation="State changes map to PATCH on the resource or POST to an action sub-resource."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 17: HATEOAS (Hypermedia as the Engine of Application State)
    # ----------------------------------------------------
    DayBlueprint(
        order=17,
        title="Day 17: HATEOAS (Hypermedia as the Engine of Application State)",
        concept="Exploring the pinnacle of the Richardson Maturity Model: embedding dynamic hypermedia controls (links) into API payloads to guide client state navigation.",
        analogy="When you visit a website, you don't memorize every URL before opening the browser. You go to the homepage, and the page provides clickable hyperlinks to 'Next Page', 'Edit Profile', and 'Log Out'. HATEOAS brings clickable hyperlinks directly into JSON payloads so mobile and web apps know what actions are currently valid.",
        theory_sections=[
            {
                "heading": "What is HATEOAS?",
                "body": (
                    "**HATEOAS (Hypermedia As The Engine Of Application State)** is a constraint of the REST application architecture. "
                    "In a HATEOAS-compliant API, the server's response does not just return raw data—it includes **hypermedia links** "
                    "informing the client what actions can be taken next from this current state."
                )
            },
            {
                "heading": "The Richardson Maturity Model (Level 3)",
                "body": (
                    "Leonard Richardson proposed a 4-tier model for evaluating REST compliance:\n"
                    "- **Level 0 (The Swamp of POX)**: One URI, one HTTP verb (POST) for everything (XML-RPC/SOAP).\n"
                    "- **Level 1 (Resources)**: Multiple individual resource URIs, but still using only POST or GET.\n"
                    "- **Level 2 (HTTP Verbs)**: Standard resource URIs + correct HTTP verbs (GET, POST, PUT, DELETE) + proper status codes (most modern APIs stop here!).\n"
                    "- **Level 3 (Hypermedia Controls)**: HATEOAS. Responses contain dynamic navigational links."
                )
            },
            {
                "heading": "Real-World Value: Dynamic Permissions",
                "body": (
                    "If an order is in status `SHIPPED`, the server includes a link to `track_shipment`, but **omits** the link to `cancel_order`. "
                    "The frontend doesn't need hardcoded conditional logic; if the cancel link is absent in the JSON, the UI simply hides the Cancel button!"
                )
            }
        ],
        code_snippets=[
            {
                "title": "HATEOAS JSON Response Example (HAL Format)",
                "code": "# Response from GET /api/v1/bank-accounts/98234\n# Payload contains account data PLUS hypermedia links:\n{\n  \"account_number\": \"98234\",\n  \"balance\": 1420.50,\n  \"status\": \"ACTIVE\",\n  \"_links\": {\n    \"self\":     { \"href\": \"/api/v1/bank-accounts/98234\" },\n    \"deposit\":  { \"href\": \"/api/v1/bank-accounts/98234/deposits\", \"method\": \"POST\" },\n    \"withdraw\": { \"href\": \"/api/v1/bank-accounts/98234/withdrawals\", \"method\": \"POST\" },\n    \"statement\":{ \"href\": \"/api/v1/bank-accounts/98234/statements/latest\" }\n  }\n}",
                "explanation": "HAL (Hypertext Application Language) links embedded in JSON payload."
            },
            {
                "title": "State-Dependent Links in Python API",
                "code": "def serialize_order(order):\n    links = {\n        \"self\": f\"/api/v1/orders/{order.id}\"\n    }\n    # Conditionally expose actions based on business state:\n    if order.status == 'PENDING':\n        links[\"cancel\"] = f\"/api/v1/orders/{order.id}/cancel\"\n        links[\"payment\"] = f\"/api/v1/orders/{order.id}/pay\"\n    elif order.status == 'SHIPPED':\n        links[\"tracking\"] = f\"/api/v1/orders/{order.id}/tracking\"\n        \n    return {\n        \"id\": order.id,\n        \"total\": order.total,\n        \"status\": order.status,\n        \"_links\": links\n    }",
                "explanation": "Server drives client behavior dynamically by providing or withholding action links."
            },
            {
                "title": "The Richardson Maturity Model",
                "code": "# Level 3: Hypermedia Controls (HATEOAS - Glory of REST)\n#   ^\n# Level 2: HTTP Verbs (GET/POST/PUT/DELETE) + Status Codes (Standard Web APIs)\n#   ^\n# Level 1: Individual Resource URIs (/users, /orders)\n#   ^\n# Level 0: The Swamp of POX (Single endpoint, single verb e.g. /endpoint.php)",
                "explanation": "The 4 levels of the Richardson Maturity Model."
            },
            {
                "title": "JSON:API Standard Hypermedia Structure",
                "code": "# Standardized JSON:API pagination links:\n{\n  \"data\": [{ \"type\": \"articles\", \"id\": \"1\" }],\n  \"links\": {\n    \"self\": \"https://example.com/articles?page[number]=3\",\n    \"first\": \"https://example.com/articles?page[number]=1\",\n    \"prev\": \"https://example.com/articles?page[number]=2\",\n    \"next\": \"https://example.com/articles?page[number]=4\",\n    \"last\": \"https://example.com/articles?page[number]=10\"\n  }\n}",
                "explanation": "JSON:API specification using HATEOAS links for client pagination navigation."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Add HATEOAS Links to User Object",
            description="Write a Python function `add_hateoas(user_id: int, is_admin: bool) -> dict` returning a dict containing `_links` with `self: f'/users/{user_id}'`, and if `is_admin` is True, also includes `admin_delete: f'/users/{user_id}'`.",
            starter_code="def add_hateoas(user_id: int, is_admin: bool) -> dict:\n    # Return links dict\n    pass",
            solution_code="def add_hateoas(user_id: int, is_admin: bool) -> dict:\n    links = {'self': f'/users/{user_id}'}\n    if is_admin:\n        links['admin_delete'] = f'/users/{user_id}'\n    return {'_links': links}",
            expected_output="{'_links': {'self': '/users/1', ...}}"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What does the acronym HATEOAS stand for in REST architectural theory?",
                options=[
                    "Hypermedia As The Engine Of Application State",
                    "Hypertext Automated Transfer Protocol Endpoint System",
                    "Host Application Transmission Encryption Over All Servers",
                    "Hierarchical Architecture Testing Engine On App State"
                ],
                correct_answer="Hypermedia As The Engine Of Application State",
                explanation="HATEOAS stands for Hypermedia As The Engine Of Application State."
            ),
            QuizQuestionBlueprint(
                question="At what level of the Richardson Maturity Model does an API implement HATEOAS hypermedia links?",
                options=["Level 3", "Level 2", "Level 1", "Level 0"],
                correct_answer="Level 3",
                explanation="Level 3 represents the highest maturity tier: hypermedia-driven controls."
            ),
            QuizQuestionBlueprint(
                question="How does HATEOAS simplify frontend UI client logic?",
                options=[
                    "The frontend does not need hardcoded rules about valid state transitions; it checks if action links are provided in the server payload",
                    "It makes CSS styling obsolete",
                    "It generates JavaScript code automatically",
                    "It reduces database query times to zero"
                ],
                correct_answer="The frontend does not need hardcoded rules about valid state transitions; it checks if action links are provided in the server payload",
                explanation="The server dynamically directs the client's available actions via links in the response."
            ),
            QuizQuestionBlueprint(
                question="Which popular JSON specification uses an `_links` object containing `self` and related action URLs?",
                options=["HAL (Hypertext Application Language)", "SOAP", "YAML", "GraphQL Schema"],
                correct_answer="HAL (Hypertext Application Language)",
                explanation="HAL is a popular media type convention for representing HATEOAS links in JSON."
            ),
            QuizQuestionBlueprint(
                question="Why do many real-world production APIs stop at Richardson Maturity Model Level 2 rather than implementing Level 3 (HATEOAS)?",
                options=[
                    "Level 2 is simpler to implement and consume; client developers often prefer fixed API documentation and simple JSON models without link parsing overhead",
                    "Level 3 is illegal under web standards",
                    "Level 3 does not work with smartphones",
                    "Level 3 requires XML"
                ],
                correct_answer="Level 2 is simpler to implement and consume; client developers often prefer fixed API documentation and simple JSON models without link parsing overhead",
                explanation="Most engineering teams find Level 2 (HTTP verbs + URIs + status codes) to be the sweet spot of simplicity."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 18 (Project): RESTful E-Commerce Resource Modeling
    # ----------------------------------------------------
    DayBlueprint(
        order=18,
        title="Day 18 (Project): RESTful E-Commerce Resource Modeling Lab",
        concept="Milestone Design Lab: Modeling a complete enterprise e-commerce domain using strict RESTful resource hierarchies, noun identifiers, and state-driven payloads.",
        analogy="Today you are the chief city architect. Before builders pour concrete (writing database tables and code), you must draft the official master map (the API specification) showing every street, avenue, and building in the city.",
        theory_sections=[
            {
                "heading": "Project Objective",
                "body": (
                    "In this milestone architecture lab, you will design the comprehensive API contract for an enterprise e-commerce platform:\n"
                    "1. Users & Profiles (`/users`)\n"
                    "2. Product Catalog & Categories (`/products`, `/categories`)\n"
                    "3. Shopping Cart (`/carts`)\n"
                    "4. Orders & Fulfillment (`/orders`)\n"
                    "5. Payment Transactions (`/orders/{id}/payments`)"
                )
            },
            {
                "heading": "Strict REST Criteria Enforced",
                "body": (
                    "- Plural noun naming conventions exclusively.\n"
                    "- Max 2 levels of URL nesting.\n"
                    "- Correct HTTP verb assignment (GET, POST, PUT, PATCH, DELETE).\n"
                    "- Proper HTTP status code mappings (200, 201 + Location, 204, 400, 404).\n"
                    "- Standardized JSON request and response payloads."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Complete E-Commerce API Contract Specification",
                "code": "# Endpoint Blueprint:\n# --------------------------------------------------------------------------\n# METHOD | URI                              | PURPOSE             | STATUS\n# -------+----------------------------------+---------------------+-----------\n# GET    | /api/v1/products                 | List products       | 200 OK\n# POST   | /api/v1/products                 | Create product      | 201 Created\n# GET    | /api/v1/products/{id}            | Get product details | 200 OK\n# PATCH  | /api/v1/products/{id}            | Update price/stock  | 200 OK\n# DELETE | /api/v1/products/{id}            | Archive product     | 204 No Content\n# POST   | /api/v1/carts                    | Initialize cart     | 201 Created\n# POST   | /api/v1/carts/{id}/items         | Add item to cart    | 200 OK\n# POST   | /api/v1/orders                   | Checkout cart       | 201 Created\n# POST   | /api/v1/orders/{id}/payments     | Process payment     | 201 Created",
                "explanation": "Production-grade RESTful API contract for an e-commerce platform."
            },
            {
                "title": "Python Flask Implementation of Cart Sub-Resource",
                "code": "from flask import Flask, request, jsonify\n\napp = Flask(__name__)\n\n# Adding item to shopping cart sub-resource:\n@app.route('/api/v1/carts/<cart_id>/items', methods=['POST'])\ndef add_cart_item(cart_id):\n    data = request.json\n    if not data or 'product_id' not in data or 'quantity' not in data:\n        return jsonify({'error': 'product_id and quantity required'}), 400\n        \n    # Simulate adding item\n    item = {'product_id': data['product_id'], 'quantity': data['quantity']}\n    return jsonify({\n        'cart_id': cart_id,\n        'items': [item],\n        'subtotal': 49.99\n    }), 200",
                "explanation": "Sub-resource cart endpoint in Flask."
            },
            {
                "title": "Order State Transitions Response",
                "code": "# GET /api/v1/orders/ord-902\n{\n  \"order_id\": \"ord-902\",\n  \"customer_id\": \"usr-14\",\n  \"status\": \"PAYMENT_PENDING\",\n  \"total_cents\": 9999,\n  \"currency\": \"USD\",\n  \"items\": [\n    {\"sku\": \"PROD-1\", \"qty\": 2, \"price_cents\": 4999}\n  ],\n  \"created_at\": \"2026-09-30T14:00:00Z\"\n}",
                "explanation": "Standardized JSON payload design for financial transactions."
            },
            {
                "title": "cURL Testing Suite for Lab",
                "code": "# Test creating an order via terminal:\ncurl -X POST https://api.shop.com/api/v1/orders \\\n  -H \"Content-Type: application/json\" \\\n  -d '{\"cart_id\": \"cart-88\", \"shipping_address_id\": \"addr-1\"}' -i",
                "explanation": "cURL command validating API contract."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Build Order Checkout Endpoint",
            description="Implement a Flask endpoint `POST /api/v1/orders` that accepts JSON with `cart_id`, generates order_id 'ord-101', and returns status 201 with header `Location: /api/v1/orders/ord-101`.",
            starter_code="from flask import Flask, request, jsonify\napp = Flask(__name__)\n\n# Implement order creation\n",
            solution_code="from flask import Flask, request, jsonify\napp = Flask(__name__)\n\n@app.route('/api/v1/orders', methods=['POST'])\ndef create_order():\n    data = request.json or {}\n    order_id = 'ord-101'\n    return jsonify({'order_id': order_id, 'cart_id': data.get('cart_id')}), 201, {'Location': f'/api/v1/orders/{order_id}'}",
            expected_output="{'order_id': 'ord-101', ...}, 201, Location: /api/v1/orders/ord-101"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Which URI correctly models adding an item to user 42's shopping cart according to RESTful hierarchy?",
                options=[
                    "`POST /api/v1/carts/42/items`",
                    "`POST /api/v1/addItemToUserCart?user=42`",
                    "`GET /api/v1/user/42/add-cart-item`",
                    "`PUT /api/v1/items/add/42`"
                ],
                correct_answer="`POST /api/v1/carts/42/items`",
                explanation="`POST /carts/42/items` uses plural nouns and maps item creation to the cart sub-collection."
            ),
            QuizQuestionBlueprint(
                question="What HTTP status code should be returned when an order is created successfully during checkout?",
                options=["201 Created", "200 OK", "202 Accepted", "302 Found"],
                correct_answer="201 Created",
                explanation="`201 Created` is the standard response for creating new resources."
            ),
            QuizQuestionBlueprint(
                question="Why should prices in an e-commerce API response preferably be represented in integer cents (e.g. `price_cents: 4999`) rather than floating point numbers (`price: 49.99`)?",
                options=[
                    "Floating-point numbers in computer hardware suffer from binary rounding errors (e.g. 0.1 + 0.2 = 0.30000000000000004); integer cents prevent financial discrepancies",
                    "Integers run faster on mobile phones",
                    "JSON does not support decimals",
                    "Cents take up less disk space"
                ],
                correct_answer="Floating-point numbers in computer hardware suffer from binary rounding errors (e.g. 0.1 + 0.2 = 0.30000000000000004); integer cents prevent financial discrepancies",
                explanation="Financial APIs (like Stripe) use integer cents to eliminate floating-point precision flaws."
            ),
            QuizQuestionBlueprint(
                question="How should a customer's product reviews be nested under products?",
                options=[
                    "`GET /api/v1/products/12/reviews`",
                    "`GET /api/v1/getReviewsForProduct12`",
                    "`POST /api/v1/showReviews/12`",
                    "`GET /api/v1/all-reviews-by-product-id-12`"
                ],
                correct_answer="`GET /api/v1/products/12/reviews`",
                explanation="Sub-resources capture natural relationships: `/products/{id}/reviews`."
            ),
            QuizQuestionBlueprint(
                question="What HTTP method should be used to archive or cancel a product catalog listing without deleting database records?",
                options=[
                    "`PATCH /api/v1/products/12` with body `{\"status\": \"archived\"}` (or `DELETE` if hard removal)",
                    "`GET /api/v1/products/12?action=archive`",
                    "`POST /api/v1/archive`",
                    "`OPTIONS /api/v1/products/12`"
                ],
                correct_answer="`PATCH /api/v1/products/12` with body `{\"status\": \"archived\"}` (or `DELETE` if hard removal)",
                explanation="Soft deletion or status updates are performed via partial modification (PATCH)."
            )
        ],
        is_project_day=True,
        project_name="RESTful E-Commerce Resource Modeling Lab"
    ),

    # ----------------------------------------------------
    # Day 19: Endpoint Naming Conventions
    # ----------------------------------------------------
    DayBlueprint(
        order=19,
        title="Day 19: Endpoint Naming Conventions (Plural Nouns, Hierarchy & Cases)",
        concept="Mastering production URI styling conventions: kebab-case vs snake_case, pluralization standards, reserved characters, and casing consistency.",
        analogy="Street names in a modern planned city: all avenues follow the same numbering system, street signs use the same clear font, and there are no confusing spelling variations. Consistency in API naming is what prevents developers from pulling their hair out.",
        theory_sections=[
            {
                "heading": "The 5 Golden Rules of URI Styling",
                "body": (
                    "To ensure maximum developer ergonomics and clarity across international teams, follow these five rules:\n"
                    "1. **Use Plural Nouns for Collections**: `/users`, `/invoices`, `/devices` (never singular `/user`).\n"
                    "2. **Use Lowercase Letters**: URIs are technically case-sensitive per RFC 3986 (`/Users` != `/users`), but lowercase avoids cross-platform casing bugs.\n"
                    "3. **Use Kebab-Case for Multi-Word Paths**: Use hyphens (`/flight-bookings`), NOT underscores (`/flight_bookings`) and NOT camelCase (`/flightBookings`). Hyphens are recommended by Google and web standards.\n"
                    "4. **Never Use File Extensions in URLs**: Do not use `/users.json` or `/report.xml`; use the `Accept` header for content negotiation.\n"
                    "5. **Do Not Include Trailing Slashes**: Treat `/users` and `/users/` consistently by redirecting or standardizing on no trailing slash."
                )
            },
            {
                "heading": "Casing Consistency Across the API",
                "body": (
                    "- **URI Paths**: kebab-case (`/user-accounts/123/login-history`).\n"
                    "- **Query Parameters**: snake_case (`?created_after=2026-01-01&sort_by=price`) or camelCase.\n"
                    "- **JSON Payload Keys**: Pick one standard (camelCase is industry standard for JS/TypeScript; snake_case for Python) and enforce it 100% across all endpoints!"
                )
            }
        ],
        code_snippets=[
            {
                "title": "Good vs Bad URI Examples",
                "code": "# ❌ BAD URI EXAMPLES:\n# /api/get_user_profile\n# /api/Users\n# /api/user_accounts/123\n# /api/customers.json\n# /api/user/10/cart/\n\n# ✅ PROFESSIONAL RESTFUL URIs:\n# /api/v1/users\n# /api/v1/users/123\n# /api/v1/user-accounts/123\n# /api/v1/customers (with Accept: application/json)\n# /api/v1/users/10/cart",
                "explanation": "Side-by-side comparison of naming anti-patterns vs clean standards."
            },
            {
                "title": "Strict Path Normalization Middleware in Express",
                "code": "const express = require('express');\nconst app = express();\n\n// Middleware: strip trailing slashes for uniformity\napp.use((req, res, next) => {\n    if (req.path.substr(-1) === '/' && req.path.length > 1) {\n        const query = req.url.slice(req.path.length);\n        res.redirect(301, req.path.slice(0, -1) + query);\n    } else {\n        next();\n    }\n});",
                "explanation": "Enforces no-trailing-slash consistency via 301 redirection."
            },
            {
                "title": "Query Parameter Casing Convention",
                "code": "# Filtering with consistent snake_case query params:\n# GET /api/v1/flight-tickets?departure_date=2026-10-15&max_price=450&seat_type=economy",
                "explanation": "Clear parameter semantics for search and filter parameters."
            },
            {
                "title": "JSON Key Casing (camelCase vs snake_case)",
                "code": "// camelCase (Recommended for Web/Mobile JavaScript ecosystem):\n{\n  \"userId\": 42,\n  \"firstName\": \"Alice\",\n  \"createdAt\": \"2026-09-30T12:00:00Z\"\n}\n\n// snake_case (Common in Python/Ruby ecosystems):\n{\n  \"user_id\": 42,\n  \"first_name\": \"Alice\",\n  \"created_at\": \"2026-09-30T12:00:00Z\"\n}",
                "explanation": "Consistency is key: never mix both in the same API!"
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Normalize URI to Standard REST Kebab-Case",
            description="Write a Python function `normalize_path(entity_name: str) -> str` that converts a multi-word entity like 'UserAccount' or 'user_account' to a plural kebab-case path: e.g. 'UserAccount' -> '/api/v1/user-accounts'.",
            starter_code="def normalize_path(entity_name: str) -> str:\n    # Return normalized plural kebab-case URI\n    pass",
            solution_code="import re\ndef normalize_path(entity_name: str) -> str:\n    s = re.sub('(.)([A-Z][a-z]+)', r'\\1-\\2', entity_name)\n    kebab = re.sub('([a-z0-9])([A-Z])', r'\\1-\\2', s).lower().replace('_', '-')\n    if not kebab.endswith('s'):\n        kebab += 's'\n    return f'/api/v1/{kebab}'",
            expected_output="/api/v1/user-accounts"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Which delimiter is officially recommended by Google and web standards for multi-word URI path segments?",
                options=["Hyphens (`kebab-case`, e.g. `/user-profiles`)", "Underscores (`snake_case`)", "Spaces (`%20`)", "Periods (`.`)"],
                correct_answer="Hyphens (`kebab-case`, e.g. `/user-profiles`)",
                explanation="Hyphens (`kebab-case`) are the standard for web URIs and recognized by search engines."
            ),
            QuizQuestionBlueprint(
                question="Why should resource collection endpoints use plural nouns (`/users`) instead of singular nouns (`/user`)?",
                options=[
                    "Because a collection endpoint fundamentally represents a container of multiple items; `/users/1` naturally reads as item 1 within the users collection",
                    "Singular nouns are not valid in URLs",
                    "Plural nouns take up less bandwidth",
                    "Plural nouns encrypt the data"
                ],
                correct_answer="Because a collection endpoint fundamentally represents a container of multiple items; `/users/1` naturally reads as item 1 within the users collection",
                explanation="Plural nouns provide a consistent mental model for collections and singletons."
            ),
            QuizQuestionBlueprint(
                question="Should file extensions like `.json` or `.xml` be included in clean RESTful URI paths (e.g. `/api/v1/users.json`)?",
                options=[
                    "No, format should be negotiated via the HTTP `Accept` header rather than hardcoded into the URI",
                    "Yes, every URL must end in `.json`",
                    "Only if using Windows servers",
                    "Only for image files"
                ],
                correct_answer="No, format should be negotiated via the HTTP `Accept` header rather than hardcoded into the URI",
                explanation="Content negotiation via `Accept` headers decouples the URI from representation format."
            ),
            QuizQuestionBlueprint(
                question="What is the recommended policy regarding trailing slashes in URIs (`/users` vs `/users/`)?",
                options=[
                    "Standardize on one convention (typically without trailing slash) and redirect the other using 301 Moved Permanently",
                    "Allow both to return completely different data",
                    "Return a 500 error for trailing slashes",
                    "Delete the database if a trailing slash is sent"
                ],
                correct_answer="Standardize on one convention (typically without trailing slash) and redirect the other using 301 Moved Permanently",
                explanation="Standardizing prevents duplicate-content caching and routing ambiguity."
            ),
            QuizQuestionBlueprint(
                question="Why should URI path segments always be written in strictly lowercase letters?",
                options=[
                    "Because per RFC 3986, URLs are case-sensitive; lowercase prevents accidental routing mismatches across operating systems",
                    "Uppercase letters are illegal on the internet",
                    "Lowercase letters make code compile faster",
                    "Routers cannot read uppercase letters"
                ],
                correct_answer="Because per RFC 3986, URLs are case-sensitive; lowercase prevents accidental routing mismatches across operating systems",
                explanation="Lowercase standard eliminates cross-platform casing bugs and routing inconsistencies."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 20: Implementing CRUD Operations
    # ----------------------------------------------------
    DayBlueprint(
        order=20,
        title="Day 20: Implementing Full CRUD Operations (REST Patterns)",
        concept="Engineering complete, robust CRUD APIs: handling Create, Read, Update (Full/Partial), and Delete with exact HTTP verbs, request parsing, and status codes.",
        analogy="CRUD is the bread-and-butter mechanics of every database on Earth: Create (POSTing a new post on social media), Read (browsing your feed), Update (editing a typo in your caption), and Delete (removing an embarrassing photo).",
        theory_sections=[
            {
                "heading": "The 5 Standard CRUD Endpoints",
                "body": (
                    "Every production resource typically implements this canonical interface:\n"
                    "1. `POST /resources`: **Create** a new entity. Returns `201 Created` with `Location` header.\n"
                    "2. `GET /resources`: **Read** paginated list. Returns `200 OK`.\n"
                    "3. `GET /resources/{id}`: **Read** specific entity. Returns `200 OK` or `404 Not Found`.\n"
                    "4. `PUT /resources/{id}` or `PATCH /resources/{id}`: **Update** entity. Returns `200 OK` (or `204 No Content`).\n"
                    "5. `DELETE /resources/{id}`: **Delete** entity. Returns `204 No Content` (or `200 OK`)."
                )
            },
            {
                "heading": "Validating Inputs and Handling Edge Cases",
                "body": (
                    "Robust CRUD APIs do not just handle the 'happy path'. They rigorously validate incoming data:\n"
                    "- Missing required fields -> `400 Bad Request`.\n"
                    "- Unique constraint collisions (e.g. duplicate email) -> `409 Conflict`.\n"
                    "- Non-existent IDs -> `404 Not Found`.\n"
                    "- Invalid data types -> `422 Unprocessable Entity`."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Complete Flask In-Memory CRUD Implementation",
                "code": "from flask import Flask, request, jsonify\n\napp = Flask(__name__)\nDB = {}\nCOUNTER = 1\n\n# 1. CREATE\n@app.route('/api/v1/tasks', methods=['POST'])\ndef create_task():\n    global COUNTER\n    data = request.json or {}\n    if 'title' not in data:\n        return jsonify({'error': 'title is required'}), 400\n    task = {'id': COUNTER, 'title': data['title'], 'done': False}\n    DB[COUNTER] = task\n    COUNTER += 1\n    return jsonify(task), 201, {'Location': f'/api/v1/tasks/{task[\"id\"]}'}\n\n# 2. READ (List)\n@app.route('/api/v1/tasks', methods=['GET'])\ndef list_tasks():\n    return jsonify(list(DB.values())), 200\n\n# 3. READ (Single)\n@app.route('/api/v1/tasks/<int:id>', methods=['GET'])\ndef get_task(id):\n    if id not in DB:\n        return jsonify({'error': 'Task not found'}), 404\n    return jsonify(DB[id]), 200\n\n# 4. UPDATE (Partial)\n@app.route('/api/v1/tasks/<int:id>', methods=['PATCH'])\ndef patch_task(id):\n    if id not in DB:\n        return jsonify({'error': 'Task not found'}), 404\n    data = request.json or {}\n    if 'title' in data: DB[id]['title'] = data['title']\n    if 'done' in data: DB[id]['done'] = data['done']\n    return jsonify(DB[id]), 200\n\n# 5. DELETE\n@app.route('/api/v1/tasks/<int:id>', methods=['DELETE'])\ndef delete_task(id):\n    if id not in DB:\n        return jsonify({'error': 'Task not found'}), 404\n    del DB[id]\n    return '', 204",
                "explanation": "Production pattern for full CRUD lifecycle in Flask."
            },
            {
                "title": "Testing CRUD Operations via cURL",
                "code": "# Create:\ncurl -X POST http://localhost:5000/api/v1/tasks -H \"Content-Type: application/json\" -d '{\"title\": \"Study REST\"}'\n\n# Read:\ncurl http://localhost:5000/api/v1/tasks/1\n\n# Patch:\ncurl -X PATCH http://localhost:5000/api/v1/tasks/1 -H \"Content-Type: application/json\" -d '{\"done\": true}'\n\n# Delete:\ncurl -X DELETE http://localhost:5000/api/v1/tasks/1 -i",
                "explanation": "cURL testing script exercising every CRUD verb."
            },
            {
                "title": "409 Conflict for Duplicate Entities",
                "code": "# When attempting to register an email that already exists in DB:\n# HTTP/1.1 409 Conflict\n# Content-Type: application/json\n#\n# {\n#   \"error\": \"Conflict\",\n#   \"message\": \"User with email alice@dev.io already exists\"\n# }",
                "explanation": "409 Conflict signals state collisions."
            },
            {
                "title": "CRUD Status Code Matrix",
                "code": "# Action   | Verb   | Success Status | Failure Statuses\n# ---------+--------+----------------+--------------------\n# Create   | POST   | 201 Created    | 400 Bad Request, 409 Conflict\n# Read     | GET    | 200 OK         | 404 Not Found\n# Replace  | PUT    | 200 OK         | 400 Bad Request, 404 Not Found\n# Patch    | PATCH  | 200 OK         | 400 Bad Request, 404 Not Found\n# Delete   | DELETE | 204 No Content | 404 Not Found",
                "explanation": "Standard status code matrix for CRUD."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Handle 404 in CRUD Get Endpoint",
            description="Write a Flask endpoint `GET /api/v1/items/<int:item_id>` using a dict `ITEMS = {1: 'Pen'}`. Return `{'item': ITEMS[item_id]}` with 200 if found; else return `{'error': 'Not Found'}` with status code 404.",
            starter_code="from flask import Flask, jsonify\napp = Flask(__name__)\nITEMS = {1: 'Pen'}\n\n# Implement get endpoint\n",
            solution_code="from flask import Flask, jsonify\napp = Flask(__name__)\nITEMS = {1: 'Pen'}\n\n@app.route('/api/v1/items/<int:item_id>')\ndef get_item(item_id):\n    if item_id in ITEMS:\n        return jsonify({'item': ITEMS[item_id]}), 200\n    return jsonify({'error': 'Not Found'}), 404",
            expected_output="200 if item exists, 404 if item missing"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What HTTP status code should be returned when a client attempts to register an account with an email address that already exists in the database?",
                options=["409 Conflict", "400 Bad Request", "404 Not Found", "500 Server Error"],
                correct_answer="409 Conflict",
                explanation="`409 Conflict` indicates that the request conflicts with current server state (e.g. duplicate key)."
            ),
            QuizQuestionBlueprint(
                question="What is the expected HTTP response status code when a `DELETE` request successfully removes a resource and returns no payload?",
                options=["204 No Content", "200 OK", "201 Created", "304 Not Modified"],
                correct_answer="204 No Content",
                explanation="`204 No Content` signals that the deletion succeeded and no response body is sent."
            ),
            QuizQuestionBlueprint(
                question="When implementing a `GET /resources/{id}` endpoint, what should the API return if the provided `{id}` does not exist?",
                options=[
                    "`404 Not Found` with an informative JSON error message",
                    "`200 OK` with an empty string",
                    "`500 Internal Server Error`",
                    "`204 No Content`"
                ],
                correct_answer="`404 Not Found` with an informative JSON error message",
                explanation="`404 Not Found` informs the client that the requested entity does not exist."
            ),
            QuizQuestionBlueprint(
                question="Which HTTP verb should be paired with `/api/v1/articles` to create a new article in the collection?",
                options=["POST", "GET", "PUT", "PATCH"],
                correct_answer="POST",
                explanation="POSTing to a collection URI creates a new subordinate resource."
            ),
            QuizQuestionBlueprint(
                question="What is the status code `422 Unprocessable Entity` commonly used for in modern APIs?",
                options=[
                    "Semantic validation errors (e.g., the JSON syntax is valid, but an age field contains a negative number)",
                    "Server hardware crashes",
                    "Database outages",
                    "Network disconnections"
                ],
                correct_answer="Semantic validation errors (e.g., the JSON syntax is valid, but an age field contains a negative number)",
                explanation="`422 Unprocessable Entity` indicates well-formed syntax that fails business validation rules."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 21: Query Parameters for Filtering, Sorting, aur Searching
    # ----------------------------------------------------
    DayBlueprint(
        order=21,
        title="Day 21: Query Parameters for Filtering, Sorting, and Searching",
        concept="Designing clean, predictable query parameters to filter, sort, and search collection resources without creating bloated custom endpoints.",
        analogy="Walking into a shoe store: You don't ask the clerk to build a new store for every shoe size (`/shoes-size-10-color-red`). You look at the general shoe section and apply filters: `?size=10&color=red&sort=-price`.",
        theory_sections=[
            {
                "heading": "Why Use Query Parameters?",
                "body": (
                    "In RESTful architecture, the path identifies the **Resource Collection** (`/api/v1/products`). "
                    "Query parameters (the portion after the `?`) are used to **filter, sort, search, and paginate** that collection. "
                    "Query parameters do not alter the identity of the resource; they refine the subset returned."
                )
            },
            {
                "heading": "Standard Query Parameter Patterns",
                "body": (
                    "1. **Filtering**: Direct attribute matching: `?category=electronics&status=in_stock`.\n"
                    "2. **Sorting**: Industry standard uses `sort` with a minus prefix (`-`) for descending order: `?sort=-created_at,price`.\n"
                    "3. **Full-Text Searching**: Use `q` or `search`: `?q=wireless+headphones`.\n"
                    "4. **Field Selection (Sparse Fieldsets)**: Request only specific fields to save bandwidth: `?fields=id,name,price`."
                )
            },
            {
                "heading": "Range and Comparison Operators",
                "body": (
                    "How to handle greater-than or less-than? Common conventions:\n"
                    "- Suffixes: `?price_gte=50&price_lte=200`\n"
                    "- Square Brackets: `?price[gte]=50&price[lte]=200`"
                )
            }
        ],
        code_snippets=[
            {
                "title": "Filtering, Sorting, and Searching in Flask",
                "code": "from flask import Flask, request, jsonify\n\napp = Flask(__name__)\n\nPRODUCTS = [\n    {\"id\": 1, \"name\": \"Mechanical Keyboard\", \"category\": \"tech\", \"price\": 120},\n    {\"id\": 2, \"name\": \"Coffee Mug\", \"category\": \"kitchen\", \"price\": 15},\n    {\"id\": 3, \"name\": \"Gaming Mouse\", \"category\": \"tech\", \"price\": 60},\n]\n\n@app.route('/api/v1/products')\ndef get_products():\n    results = PRODUCTS\n    \n    # 1. Filtering by category:\n    category = request.args.get('category')\n    if category:\n        results = [p for p in results if p['category'] == category]\n        \n    # 2. Searching by keyword (q):\n    query = request.args.get('q')\n    if query:\n        results = [p for p in results if query.lower() in p['name'].lower()]\n        \n    # 3. Sorting (?sort=price or ?sort=-price):\n    sort_by = request.args.get('sort')\n    if sort_by:\n        reverse = sort_by.startswith('-')\n        field = sort_by.lstrip('-')\n        if field in ['price', 'name']:\n            results = sorted(results, key=lambda p: p[field], reverse=reverse)\n            \n    return jsonify(results)",
                "explanation": "Implementation of filtering, search query 'q', and sorting logic."
            },
            {
                "title": "Real-World Query String Examples",
                "code": "# Search tech products under $100 sorted by lowest price first:\nGET /api/v1/products?category=tech&price_lte=100&sort=price\n\n# Search users created in 2026 returning only id and email:\nGET /api/v1/users?created_after=2026-01-01&fields=id,email",
                "explanation": "Clean combinations of query parameters in API requests."
            },
            {
                "title": "FastAPI Query Parameter Type Validation",
                "code": "from fastapi import FastAPI, Query\n\napp = FastAPI()\n\n@app.get(\"/api/v1/items\")\ndef search_items(\n    q: str | None = Query(default=None, max_length=50),\n    min_price: float = Query(default=0.0, ge=0.0),\n    limit: int = Query(default=20, le=100)\n):\n    return {\"query\": q, \"min_price\": min_price, \"limit\": limit}",
                "explanation": "FastAPI automatically validates parameter types and ranges."
            },
            {
                "title": "Sparse Fieldsets Concept (GraphQL in REST)",
                "code": "# Fetching 1000 users with full profile data wastes megabytes of network data.\n# Sparse fieldsets let the client request only what it needs:\nGET /api/v1/users?fields=id,username\n\n# Response contains ONLY id and username, stripping out 40 other fields!",
                "explanation": "Sparse fieldsets reduce bandwidth footprint."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Extract and Filter List via Query Param",
            description="Write a Python Flask endpoint `/api/filter` that reads query parameter `role` and filters list `[{'user': 'A', 'role': 'admin'}, {'user': 'B', 'role': 'user'}]` returning only matching objects.",
            starter_code="from flask import Flask, request, jsonify\napp = Flask(__name__)\nUSERS = [{'user': 'A', 'role': 'admin'}, {'user': 'B', 'role': 'user'}]\n\n# Implement filter endpoint\n",
            solution_code="from flask import Flask, request, jsonify\napp = Flask(__name__)\nUSERS = [{'user': 'A', 'role': 'admin'}, {'user': 'B', 'role': 'user'}]\n\n@app.route('/api/filter')\ndef filter_users():\n    role = request.args.get('role')\n    if role:\n        return jsonify([u for u in USERS if u['role'] == role])\n    return jsonify(USERS)",
            expected_output="[{'user': 'A', 'role': 'admin'}] when role=admin"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the conventional prefix used in `sort` query parameters (e.g. `?sort=-created_at`) to designate DESCENDING order?",
                options=["A minus sign (`-`)", "An exclamation mark (`!`)", "The word `DESC`", "A tilde (`~`)"],
                correct_answer="A minus sign (`-`)",
                explanation="A leading `-` (e.g. `?sort=-price`) is the universal REST convention for descending order."
            ),
            QuizQuestionBlueprint(
                question="What is the conventional query parameter key used for full-text search across an API collection?",
                options=["`q` (or `search`)", "`find`", "`keyword_lookup`", "`query_string_text`"],
                correct_answer="`q` (or `search`)",
                explanation="The single-letter `q` (short for query) is standard across Google, GitHub, and major APIs."
            ),
            QuizQuestionBlueprint(
                question="What is the technique called when a client requests only specific fields (e.g. `?fields=id,name`) to reduce response payload size?",
                options=["Sparse Fieldsets", "Data Compression", "Database Masking", "JSON Minification"],
                correct_answer="Sparse Fieldsets",
                explanation="Sparse fieldsets allow clients to restrict returned attributes to save bandwidth."
            ),
            QuizQuestionBlueprint(
                question="Should filtering parameters be part of the URI path (e.g. `/products/electronics/in-stock`) or query parameters (e.g. `/products?category=electronics`)?",
                options=[
                    "Query parameters are preferred for optional filters, sorting, and search because they refine the collection without altering resource identity",
                    "Path parameters must always be used for every filter",
                    "Query parameters are not allowed in REST",
                    "It makes no difference"
                ],
                correct_answer="Query parameters are preferred for optional filters, sorting, and search because they refine the collection without altering resource identity",
                explanation="Paths identify the canonical resource; query parameters refine and filter the representation."
            ),
            QuizQuestionBlueprint(
                question="How are multiple query parameters combined in a URL query string?",
                options=["With an ampersand (`&`)", "With a comma (`,`)", "With a slash (`/`)", "With a space (` `)"],
                correct_answer="With an ampersand (`&`)",
                explanation="The ampersand `&` is the standard separator between query key-value pairs."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 22: Pagination Strategies (Offset vs Cursor-based)
    # ----------------------------------------------------
    DayBlueprint(
        order=22,
        title="Day 22: Pagination Strategies (Offset-Based vs Cursor-Based)",
        concept="Architecting scalable API pagination: evaluating classic Offset-based pagination against high-performance Cursor-based / Keyset pagination for massive databases.",
        analogy="Offset pagination is flipping through a 1,000-page book by counting every single page from page 1: '1, 2, 3... 500'. Cursor pagination is sticking a physical bookmark on page 500: tomorrow you open directly to the bookmark instantly in 0.1 seconds.",
        theory_sections=[
            {
                "heading": "Why Pagination is Mandatory",
                "body": (
                    "If a database contains 5,000,000 products, running `SELECT * FROM products` without pagination will exhaust server RAM, "
                    "lock the database, and crash the client browser. "
                    "All production collection endpoints must enforce default and maximum page limits."
                )
            },
            {
                "heading": "1. Offset-Based Pagination (`limit` & `offset` or `page` & `page_size`)",
                "body": (
                    "- Syntax: `/api/v1/products?limit=20&offset=40` (or `?page=3&page_size=20`).\n"
                    "- SQL Equivalent: `SELECT * FROM products LIMIT 20 OFFSET 40;`\n"
                    "- **Pros**: Easy to implement; allows jumping directly to any arbitrary page (e.g. 'Go to Page 42').\n"
                    "- **Cons (The Offset Flaw)**:\n"
                    "  1. Performance degrades catastrophically at high offsets (e.g. `OFFSET 1000000` forces the database to read and discard 1 million rows in memory!).\n"
                    "  2. **Page Drift**: If a new item is inserted while a user is reading page 1, when they click page 2, the last item from page 1 shifts to page 2 and is seen twice!"
                )
            },
            {
                "heading": "2. Cursor-Based / Keyset Pagination",
                "body": (
                    "- Syntax: `/api/v1/feed?limit=20&cursor=eyJpZCI6MTAxfQ==`\n"
                    "- SQL Equivalent: `SELECT * FROM feed WHERE id > 101 ORDER BY id ASC LIMIT 20;`\n"
                    "- **Pros**: $O(1)$ constant-time database performance using indexes, zero page drift, perfect for mobile infinite scroll feeds (Instagram, Twitter).\n"
                    "- **Cons**: Cannot jump to arbitrary pages (can only navigate 'next' and 'previous')."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Offset Pagination Implementation in Python",
                "code": "from flask import Flask, request, jsonify\n\napp = Flask(__name__)\nALL_ITEMS = list(range(1, 101))  # 100 items\n\n@app.route('/api/v1/numbers')\ndef get_numbers():\n    # Default limit=10, max limit=50 to prevent abuse\n    limit = min(int(request.args.get('limit', 10)), 50)\n    offset = int(request.args.get('offset', 0))\n    \n    paginated = ALL_ITEMS[offset:offset + limit]\n    \n    return jsonify({\n        'total': len(ALL_ITEMS),\n        'limit': limit,\n        'offset': offset,\n        'data': paginated\n    })",
                "explanation": "Offset-based pagination with limit caps."
            },
            {
                "title": "Cursor-Based Pagination Implementation",
                "code": "import base64\n\n@app.route('/api/v1/timeline')\ndef get_timeline():\n    cursor = request.args.get('cursor')\n    last_id = 0\n    if cursor:\n        # Decode cursor token\n        last_id = int(base64.b64decode(cursor).decode())\n        \n    # In production SQL: SELECT * FROM posts WHERE id > last_id ORDER BY id ASC LIMIT 10\n    items = [{'id': i, 'text': f'Post #{i}'} for i in range(last_id + 1, last_id + 11)]\n    \n    next_cursor = None\n    if items:\n        next_cursor = base64.b64encode(str(items[-1]['id']).encode()).decode()\n        \n    return jsonify({\n        'data': items,\n        'next_cursor': next_cursor\n    })",
                "explanation": "Cursor-based pagination encoding the last record pointer."
            },
            {
                "title": "Comparison Summary",
                "code": "# Feature           | Offset-Based         | Cursor-Based\n# ------------------+----------------------+--------------------------\n# Jump to page 50   | Supported            | Impossible (Next/Prev only)\n# Database Speed    | O(N) Slow on high N  | O(1) Ultra-fast with index\n# Page Drift / Dupes| Prone to duplicates  | Immune to duplicates\n# Best For          | Admin Tables / Search| Mobile Infinite Scroll",
                "explanation": "Trade-off analysis between offset and cursor pagination."
            },
            {
                "title": "Link Headers for Pagination (RFC 5988)",
                "code": "# Professional APIs (like GitHub) transmit pagination URLs in Link header:\n# Link: <https://api.github.com/users?page=3>; rel=\"next\",\n#       <https://api.github.com/users?page=50>; rel=\"last\",\n#       <https://api.github.com/users?page=1>; rel=\"first\",\n#       <https://api.github.com/users?page=1>; rel=\"prev\"",
                "explanation": "Using standard HTTP Link headers for pagination controls."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Implement Offset Paginated Slice",
            description="Write a Python function `paginate(items: list, page: int, page_size: int) -> dict` that returns a dict `{'data': sliced_list, 'total_pages': N}`.",
            starter_code="import math\ndef paginate(items: list, page: int, page_size: int) -> dict:\n    # Return paginated slice and total_pages\n    pass",
            solution_code="import math\ndef paginate(items: list, page: int, page_size: int) -> dict:\n    start = (page - 1) * page_size\n    end = start + page_size\n    total_pages = math.ceil(len(items) / page_size) if page_size > 0 else 0\n    return {'data': items[start:end], 'total_pages': total_pages}",
            expected_output="{'data': [...], 'total_pages': ...}"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Why does Offset-based pagination (`OFFSET 1000000 LIMIT 20`) suffer severe performance degradation in relational databases?",
                options=[
                    "The database engine must read and scan all 1,000,000 previous rows into memory before discarding them to return the 20 requested rows",
                    "The database runs out of disk space",
                    "SQL queries cannot have numbers over 1,000",
                    "Offset pagination deletes indexes"
                ],
                correct_answer="The database engine must read and scan all 1,000,000 previous rows into memory before discarding them to return the 20 requested rows",
                explanation="High offsets force databases to evaluate and discard massive volumes of candidate rows."
            ),
            QuizQuestionBlueprint(
                question="What is 'Page Drift' in offset-based pagination?",
                options=[
                    "When items are inserted or deleted while a user navigates pages, causing items to shift positions and appear duplicated or missed",
                    "When web pages drift across the computer screen",
                    "When the server clock drifts out of sync",
                    "When a user switches WiFi networks"
                ],
                correct_answer="When items are inserted or deleted while a user navigates pages, causing items to shift positions and appear duplicated or missed",
                explanation="Offset pagination suffers from record shifting when database writes occur during client navigation."
            ),
            QuizQuestionBlueprint(
                question="Which pagination strategy is ideal for real-time mobile infinite-scroll feeds (like Twitter or Instagram)?",
                options=["Cursor-based pagination", "Offset-based pagination", "Alphabetical pagination", "CSV export"],
                correct_answer="Cursor-based pagination",
                explanation="Cursor pagination prevents duplicates and executes in constant time using indexed primary keys."
            ),
            QuizQuestionBlueprint(
                question="What is a major limitation of Cursor-based pagination compared to Offset pagination?",
                options=[
                    "Clients cannot jump directly to an arbitrary page (e.g. 'Jump to Page 15'); they can only navigate sequentially forward or backward",
                    "Cursor pagination cannot work with JSON",
                    "Cursor pagination is only supported by Python",
                    "Cursor pagination requires flash drives"
                ],
                correct_answer="Clients cannot jump directly to an arbitrary page (e.g. 'Jump to Page 15'); they can only navigate sequentially forward or backward",
                explanation="Cursors are relative pointers; calculating arbitrary future page offsets is impossible without traversing."
            ),
            QuizQuestionBlueprint(
                question="Which standard HTTP header can be used to return next, previous, and last pagination URLs per RFC 5988?",
                options=["Link", "Pagination-Urls", "Next-Page", "Location"],
                correct_answer="Link",
                explanation="The `Link` header provides standard hypermedia relationships (`rel=\"next\"`, `rel=\"prev\"`)."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 23: API Versioning (URI, Header, Query)
    # ----------------------------------------------------
    DayBlueprint(
        order=23,
        title="Day 23: API Versioning (URI, Header, and Query Versioning)",
        concept="Safely evolving APIs over time without breaking existing client integrations: comparing URI path versioning, custom header versioning, and query parameter versioning.",
        analogy="Imagine an electrical power company changing the wall socket design. They don't rip out the sockets in 10 million homes overnight (breaking everyone's toaster). They provide universal adapters or maintain both standard and modern sockets side-by-side. API versioning prevents breaking existing client apps.",
        theory_sections=[
            {
                "heading": "The Inevitability of API Evolution",
                "body": (
                    "APIs are contracts. If you rename a field from `user_name` to `username` or change a response schema, "
                    "every mobile app installed on thousands of user phones will crash instantly unless they update their app. "
                    "Versioning allows running the old contract and the new contract simultaneously."
                )
            },
            {
                "heading": "The 3 Major Versioning Strategies",
                "body": (
                    "1. **URI Path Versioning (Most Popular)**:\n"
                    "   - Example: `https://api.example.com/v1/users` vs `/v2/users`\n"
                    "   - Pros: Explicit, easy to test in browsers, easy to route via API Gateways/NGINX.\n"
                    "   - Cons: Violates pure REST theory that a resource should have a single canonical URI.\n\n"
                    "2. **Header Versioning (Custom Header / Accept Header)**:\n"
                    "   - Example: `X-API-Version: 2` or `Accept: application/vnd.company.v2+json` (Content Negotiation).\n"
                    "   - Pros: Keeps URIs clean; conceptually pure REST.\n"
                    "   - Cons: Harder to test in browsers; requires configuring headers in every client.\n\n"
                    "3. **Query Parameter Versioning**:\n"
                    "   - Example: `https://api.example.com/users?version=2`\n"
                    "   - Pros: Easy to test; easy to provide default fallbacks.\n"
                    "   - Cons: Clutters query string logic."
                )
            },
            {
                "heading": "When Should You Bump a Major Version?",
                "body": (
                    "- **Breaking Changes (Require v2)**: Deleting an endpoint, removing/renaming a field, changing data types (e.g. number to string), changing authentication.\n"
                    "- **Non-Breaking Changes (No version bump)**: Adding a new optional endpoint, adding a new field to an existing JSON response."
                )
            }
        ],
        code_snippets=[
            {
                "title": "URI Path Versioning in Express.js",
                "code": "const express = require('express');\nconst app = express();\n\n// V1 Controller (Legacy support)\napp.get('/api/v1/users/:id', (req, res) => {\n    res.json({ id: req.params.id, user_name: 'alice_dev' }); // Old field name\n});\n\n// V2 Controller (Modern schema)\napp.get('/api/v2/users/:id', (req, res) => {\n    res.json({ id: req.params.id, username: 'alice_dev', email: 'alice@dev.io' });\n});",
                "explanation": "Running concurrent versions side-by-side using path prefixes."
            },
            {
                "title": "Header-Based Versioning Middleware in Flask",
                "code": "from flask import Flask, request, jsonify\n\napp = Flask(__name__)\n\n@app.route('/api/users/<id>')\ndef get_user(id):\n    # Read version from custom header, defaulting to v1:\n    version = request.headers.get('X-API-Version', '1')\n    \n    if version == '2':\n        return jsonify({'id': id, 'name': {'first': 'Jane', 'last': 'Doe'}})\n    return jsonify({'id': id, 'name': 'Jane Doe'})",
                "explanation": "Dynamic response generation based on request headers."
            },
            {
                "title": "Accept Header (Vendor Content Negotiation)",
                "code": "# Stripe and GitHub style content negotiation:\n# Client requests specific version via Accept header:\nGET /users/42 HTTP/1.1\nHost: api.github.com\nAccept: application/vnd.github.v3+json",
                "explanation": "Vendor media type versioning."
            },
            {
                "title": "Deprecation Warnings via Sunset Header (RFC 8594)",
                "code": "# When an API version is planned for retirement, notify clients with Sunset header:\n# HTTP/1.1 200 OK\n# Deprecation: @1767139200\n# Sunset: Wed, 31 Dec 2026 23:59:59 GMT\n# Link: <https://api.dev.com/docs/migration-v2>; rel=\"sunset\"",
                "explanation": "Standard RFC 8594 Sunset headers announcing API retirement."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Implement Header-Based Version Switcher",
            description="Write a Flask route `/api/items` that returns `{'schema': 'v2'}` if header `X-Version` is '2', otherwise returns `{'schema': 'v1'}`.",
            starter_code="from flask import Flask, request, jsonify\napp = Flask(__name__)\n\n# Implement version switcher\n",
            solution_code="from flask import Flask, request, jsonify\napp = Flask(__name__)\n\n@app.route('/api/items')\ndef items():\n    if request.headers.get('X-Version') == '2':\n        return jsonify({'schema': 'v2'})\n    return jsonify({'schema': 'v1'})",
            expected_output="{'schema': 'v2'} when X-Version is 2"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Which API versioning method is the most widely adopted across modern tech companies (e.g. Twitter, Slack, Google) due to its simplicity and explicit routing?",
                options=["URI Path Versioning (e.g. `/api/v1/users`)", "Header Versioning", "DNS Subdomain Versioning", "Query Parameter Versioning"],
                correct_answer="URI Path Versioning (e.g. `/api/v1/users`)",
                explanation="URI path versioning is unambiguous, easily tested, and trivially routed by reverse proxies."
            ),
            QuizQuestionBlueprint(
                question="Which of the following changes to an API endpoint is considered a 'Breaking Change' requiring a new major version?",
                options=[
                    "Removing an existing field from a JSON response or renaming it",
                    "Adding a new optional field to a response body",
                    "Optimizing database query performance",
                    "Fixing a server-side memory leak"
                ],
                correct_answer="Removing an existing field from a JSON response or renaming it",
                explanation="Deleting or renaming fields breaks existing client deserializers."
            ),
            QuizQuestionBlueprint(
                question="How does Content Negotiation / Accept Header versioning specify the desired API version?",
                options=[
                    "Using a custom vendor MIME type in the `Accept` header (e.g. `Accept: application/vnd.company.v2+json`)",
                    "By creating a new HTML page",
                    "By calling customer support",
                    "In the URL query parameter"
                ],
                correct_answer="Using a custom vendor MIME type in the `Accept` header (e.g. `Accept: application/vnd.company.v2+json`)",
                explanation="Vendor media types specify representations through standard content negotiation."
            ),
            QuizQuestionBlueprint(
                question="What official HTTP response header defined in RFC 8594 communicates to clients the exact date when an API version will be permanently shut down?",
                options=["Sunset", "Retire-At", "Expiration-Date", "Dead-Line"],
                correct_answer="Sunset",
                explanation="The `Sunset` header indicates when a resource or API version will become unresponsive."
            ),
            QuizQuestionBlueprint(
                question="Why is changing an API contract without versioning particularly catastrophic for mobile apps (iOS / Android)?",
                options=[
                    "Because users do not update mobile apps immediately; older app builds will crash for weeks until updated via app stores",
                    "Mobile phones cannot read JSON",
                    "Apple and Google will sue the developer",
                    "Mobile apps do not use HTTP"
                ],
                correct_answer="Because users do not update mobile apps immediately; older app builds will crash for weeks until updated via app stores",
                explanation="Mobile apps have delayed update cycles; legacy API contracts must be maintained concurrently."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 24: Idempotency in APIs (Safe vs Unsafe methods)
    # ----------------------------------------------------
    DayBlueprint(
        order=24,
        title="Day 24: Idempotency in APIs (Safe vs Unsafe Methods)",
        concept="Mastering mathematical idempotency in distributed systems: guaranteeing that duplicate requests (retried on network glitches) produce the exact same server state.",
        analogy="An elevator call button is idempotent: pressing the button 1 time calls the elevator; pressing the button 20 times still calls the elevator exactly once. An ATM withdrawal button is NOT idempotent: pressing 'Withdraw $100' twenty times drains $2,000 from your bank account!",
        theory_sections=[
            {
                "heading": "What is Idempotency?",
                "body": (
                    "In mathematics and computer science, an operation is **Idempotent** if applying it multiple times produces the exact same result "
                    "as applying it once:\n"
                    "$$f(f(x)) = f(x)$$\n"
                    "In HTTP APIs, an idempotent method can be executed multiple identical times on the server, and the resulting state of the server remains unchanged."
                )
            },
            {
                "heading": "Idempotency Matrix of HTTP Verbs",
                "body": (
                    "- `GET`: **Idempotent & Safe**. Reading data 100 times doesn't change data.\n"
                    "- `HEAD`, `OPTIONS`: **Idempotent & Safe**.\n"
                    "- `PUT`: **Idempotent (Unsafe)**. Setting `{\"name\": \"Alice\"}` 100 times leaves the record named 'Alice'.\n"
                    "- `DELETE`: **Idempotent (Unsafe)**. Deleting resource #42 once removes it. Calling delete 10 more times still leaves it deleted (even if status changes from 204 to 404, the *server state* is identical!).\n"
                    "- `POST`: **NOT Idempotent**. Calling `POST /orders` 5 times creates 5 distinct orders and charges the card 5 times!\n"
                    "- `PATCH`: **Generally NOT Idempotent** (e.g. `PATCH` with `{\"increment\": 1}` changes state on every call)."
                )
            },
            {
                "heading": "Making POST Idempotent via Idempotency Keys",
                "body": (
                    "If a network drops during checkout, the client doesn't know if the charge succeeded. If the client retries, how do you prevent double-charging? "
                    "The client generates a unique UUID (**Idempotency-Key**) and sends it in the header: `Idempotency-Key: 7b9a4c1d-...`. "
                    "The server saves the key in Redis. If a second request arrives with that same key, the server skips processing and returns the cached original response!"
                )
            }
        ],
        code_snippets=[
            {
                "title": "Idempotency Matrix Overview",
                "code": "# HTTP Method | Safe? | Idempotent? | Calling 5 times creates duplicates?\n# ------------+-------+-------------+------------------------------------\n# GET         | YES   | YES         | NO (Read-only)\n# PUT         | NO    | YES         | NO (Replaces state to same value)\n# DELETE      | NO    | YES         | NO (Resource remains deleted)\n# POST        | NO    | NO          | YES (Creates 5 separate records!)\n# PATCH       | NO    | NO / MAYBE  | DEPENDS (Incrementing modifies state)",
                "explanation": "Complete matrix of HTTP verb safety and idempotency."
            },
            {
                "title": "Stripe-Style Idempotency Key Handling in Python",
                "code": "from flask import Flask, request, jsonify\nimport redis\n\napp = Flask(__name__)\nr = redis.Redis(host='localhost', port=6379, db=0)\n\n@app.route('/api/v1/charges', methods=['POST'])\ndef create_charge():\n    idempotency_key = request.headers.get('Idempotency-Key')\n    if not idempotency_key:\n        return jsonify({'error': 'Idempotency-Key header missing'}), 400\n        \n    # Check if we already processed this exact request key:\n    cached_response = r.get(f\"idempotency:{idempotency_key}\")\n    if cached_response:\n        # Return identical previous response without re-charging card!\n        return cached_response, 200, {'Content-Type': 'application/json'}\n        \n    # Process financial charge...\n    response_data = '{\"charge_id\": \"ch_9823\", \"status\": \"paid\", \"amount\": 5000}'\n    # Cache response for 24 hours in Redis:\n    r.setex(f\"idempotency:{idempotency_key}\", 86400, response_data)\n    \n    return response_data, 201, {'Content-Type': 'application/json'}",
                "explanation": "Redis-backed idempotency key interceptor preventing duplicate billing."
            },
            {
                "title": "Generating Idempotency Key on Client Side",
                "code": "// Client generating unique UUID v4 before making payment request:\nconst idempotencyKey = crypto.randomUUID();\n\nconst response = await fetch('/api/v1/charges', {\n    method: 'POST',\n    headers: {\n        'Content-Type': 'application/json',\n        'Idempotency-Key': idempotencyKey\n    },\n    body: JSON.stringify({ amount: 5000, currency: 'usd' })\n});",
                "explanation": "Client attaches UUID for safe retries."
            },
            {
                "title": "Why PUT is Idempotent while POST is Not",
                "code": "# PUT specifies the exact target URI and state:\nPUT /users/42 HTTP/1.1\n{\"email\": \"alice@dev.io\"}\n# Executing this 10 times -> User 42 still has email alice@dev.io.\n\n# POST appends to collection with server-generated ID:\nPOST /users HTTP/1.1\n{\"email\": \"alice@dev.io\"}\n# Executing this 10 times -> Creates 10 user rows with IDs 1, 2, 3... 10!",
                "explanation": "Demonstrates why PUT is idempotent and POST is not."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Implement In-Memory Idempotency Filter",
            description="Write a Python class `IdempotencyFilter` with a method `process_request(key: str, payload: dict) -> tuple` that caches payloads by key. If the key exists, return (cached_payload, False). If new, store it and return (payload, True).",
            starter_code="class IdempotencyFilter:\n    def __init__(self):\n        self.cache = {}\n    def process_request(self, key: str, payload: dict) -> tuple:\n        pass",
            solution_code="class IdempotencyFilter:\n    def __init__(self):\n        self.cache = {}\n    def process_request(self, key: str, payload: dict) -> tuple:\n        if key in self.cache:\n            return (self.cache[key], False)\n        self.cache[key] = payload\n        return (payload, True)",
            expected_output="(payload, True) on first call, (payload, False) on retry"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Which of the following HTTP methods is NOT idempotent according to the HTTP specification?",
                options=["POST", "GET", "PUT", "DELETE"],
                correct_answer="POST",
                explanation="POST is inherently non-idempotent; repeated requests create duplicate subordinate resources."
            ),
            QuizQuestionBlueprint(
                question="Why is the `DELETE` HTTP method classified as idempotent even though a second call might return `404 Not Found` instead of `204 No Content`?",
                options=[
                    "Because idempotency refers to the resulting state of the server (the resource remains deleted), not the status code",
                    "Because DELETE only works once per day",
                    "Because DELETE does not delete anything",
                    "It is actually not idempotent"
                ],
                correct_answer="Because idempotency refers to the resulting state of the server (the resource remains deleted), not the status code",
                explanation="Server state is identical after 1 or 100 DELETE calls: the resource is absent."
            ),
            QuizQuestionBlueprint(
                question="How do payment APIs like Stripe and PayPal enable clients to safely retry `POST /charges` requests after network dropouts without double-charging?",
                options=[
                    "Clients attach a unique UUID in an `Idempotency-Key` header; the server recognizes retried keys and returns cached responses",
                    "Clients call the bank directly",
                    "Stripe disables retries",
                    "By converting POST into GET"
                ],
                correct_answer="Clients attach a unique UUID in an `Idempotency-Key` header; the server recognizes retried keys and returns cached responses",
                explanation="Idempotency keys allow safe retries by matching and returning existing charge records."
            ),
            QuizQuestionBlueprint(
                question="What is the distinction between a 'Safe' method and an 'Idempotent' method?",
                options=[
                    "Safe methods do not modify server state at all (read-only); Idempotent methods may modify state, but repeated calls leave state identical",
                    "Safe methods require passwords; Idempotent methods do not",
                    "There is no distinction",
                    "Safe methods run over HTTPS; Idempotent methods run over HTTP"
                ],
                correct_answer="Safe methods do not modify server state at all (read-only); Idempotent methods may modify state, but repeated calls leave state identical",
                explanation="All safe methods are idempotent (e.g. GET), but not all idempotent methods are safe (e.g. PUT/DELETE mutate state)."
            ),
            QuizQuestionBlueprint(
                question="Why is `PUT` idempotent while `PATCH` can be non-idempotent?",
                options=[
                    "`PUT` completely replaces the resource with a fixed value; `PATCH` instructions can specify incremental modifications (e.g. 'add $5')",
                    "`PUT` is encrypted; `PATCH` is not",
                    "`PUT` is only used on Sundays",
                    "`PATCH` is an unofficial method"
                ],
                correct_answer="`PUT` completely replaces the resource with a fixed value; `PATCH` instructions can specify incremental modifications (e.g. 'add $5')",
                explanation="Setting a fixed value is idempotent; applying relative delta operations alters state on every execution."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 25: Payload Formatting & Standardized Errors (RFC 7807)
    # ----------------------------------------------------
    DayBlueprint(
        order=25,
        title="Day 25: Payload Formatting & Standardized Errors (RFC 7807 Problem Details)",
        concept="Eliminating chaotic API error formats by adopting standard response envelopes and RFC 7807 'Problem Details for HTTP APIs'.",
        analogy="Imagine driving in a foreign country where every traffic light is different: one intersection uses blue lights, another flashes words, and another honks a horn. You will crash. Standardizing API errors (RFC 7807) makes every error light recognizable across the entire digital world.",
        theory_sections=[
            {
                "heading": "The Chaos of Inconsistent Error Responses",
                "body": (
                    "In amateur APIs, different endpoints return different error structures:\n"
                    "- Endpoint A: `{\"error\": \"Invalid email\"}`\n"
                    "- Endpoint B: `{\"message\": \"User not found\", \"code\": 404}`\n"
                    "- Endpoint C: `{\"success\": false, \"err_msg\": \"Failed\"}`\n"
                    "Frontend engineers have to write dozens of ugly `try/catch` checks for every route."
                )
            },
            {
                "heading": "The Standard: RFC 7807 (Problem Details for HTTP APIs)",
                "body": (
                    "The IETF formalized **RFC 7807** (media type `application/problem+json`) providing a machine-readable schema for API errors:\n"
                    "- `type`: A URI reference identifying the problem type.\n"
                    "- `title`: A short, human-readable summary of the problem type (should not change from occurrence to occurrence).\n"
                    "- `status`: The HTTP status code.\n"
                    "- `detail`: A human-readable explanation specific to this occurrence.\n"
                    "- `instance`: A URI reference identifying the specific occurrence of the problem.\n"
                    "- `invalid_params`: Optional list of specific validation failures."
                )
            },
            {
                "heading": "Data Envelopes: To Wrap or Not to Wrap?",
                "body": (
                    "Historically, APIs wrapped responses in a top-level `{\"data\": [...]}` envelope. "
                    "Modern consensus:\n"
                    "- For collections, provide metadata objects: `{\"data\": [...], \"pagination\": {...}}`.\n"
                    "- For singletons, returning the resource directly `{\"id\": 1, \"name\": \"...\"}` is clean and idiomatic."
                )
            }
        ],
        code_snippets=[
            {
                "title": "RFC 7807 Standard Error Response",
                "code": "# Response: HTTP/1.1 400 Bad Request\n# Content-Type: application/problem+json\n{\n  \"type\": \"https://example.com/probs/out-of-credit\",\n  \"title\": \"You do not have enough credit.\",\n  \"status\": 400,\n  \"detail\": \"Your current balance is 30, but that costs 50.\",\n  \"instance\": \"/account/12345/msgs/abc\",\n  \"balance\": 30\n}",
                "explanation": "RFC 7807 compliant problem details schema."
            },
            {
                "title": "Validation Error with RFC 7807 in Python Flask",
                "code": "from flask import Flask, request, jsonify\n\napp = Flask(__name__)\n\n@app.route('/api/v1/users', methods=['POST'])\ndef create_user():\n    data = request.json or {}\n    errors = []\n    if 'email' not in data or '@' not in data['email']:\n        errors.append({'name': 'email', 'reason': 'Must be a valid email address'})\n    if 'age' in data and data['age'] < 18:\n        errors.append({'name': 'age', 'reason': 'User must be at least 18 years old'})\n        \n    if errors:\n        problem = {\n            'type': 'https://api.dev.com/errors/validation-error',\n            'title': 'Input Validation Failed',\n            'status': 422,\n            'detail': 'One or more fields failed validation.',\n            'invalid_params': errors\n        }\n        return jsonify(problem), 422, {'Content-Type': 'application/problem+json'}\n        \n    return jsonify({'status': 'created'}), 201",
                "explanation": "Detailed field-level validation errors following RFC 7807."
            },
            {
                "title": "Client-Side Universal Error Parser",
                "code": "async function apiRequest(url, options) {\n    const response = await fetch(url, options);\n    if (!response.ok) {\n        const error = await response.json();\n        // Standard RFC 7807 handling:\n        console.error(`[${error.status}] ${error.title}: ${error.detail}`);\n        if (error.invalid_params) {\n            error.invalid_params.forEach(p => console.warn(`- ${p.name}: ${p.reason}`));\n        }\n        throw error;\n    }\n    return response.json();\n}",
                "explanation": "Client-side consumption of predictable error schemas."
            },
            {
                "title": "Standard Pagination Envelope",
                "code": "# Clean, standardized paginated collection payload:\n{\n  \"data\": [\n    {\"id\": 1, \"name\": \"Keyboard\"},\n    {\"id\": 2, \"name\": \"Mouse\"}\n  ],\n  \"pagination\": {\n    \"current_page\": 1,\n    \"per_page\": 2,\n    \"total_items\": 42,\n    \"total_pages\": 21\n  }\n}",
                "explanation": "Decouples resource entities from metadata."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Format RFC 7807 Error Response",
            description="Write a Python function `build_problem(status: int, title: str, detail: str) -> dict` returning an RFC 7807 complaint dict with keys 'type', 'title', 'status', and 'detail'.",
            starter_code="def build_problem(status: int, title: str, detail: str) -> dict:\n    # Return RFC 7807 dict\n    pass",
            solution_code="def build_problem(status: int, title: str, detail: str) -> dict:\n    return {\n        'type': 'about:blank',\n        'title': title,\n        'status': status,\n        'detail': detail\n    }",
            expected_output="{'type': 'about:blank', 'title': '...', 'status': 400, 'detail': '...'}"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What official IETF specification establishes standard machine-readable error schemas for HTTP APIs?",
                options=["RFC 7807 (Problem Details for HTTP APIs)", "RFC 2616", "RFC 8259", "RFC 1918"],
                correct_answer="RFC 7807 (Problem Details for HTTP APIs)",
                explanation="RFC 7807 defines standard problem details formatting for HTTP APIs."
            ),
            QuizQuestionBlueprint(
                question="What is the official MIME media type for an RFC 7807 error payload?",
                options=["application/problem+json", "application/error+json", "text/problem", "application/bad-request"],
                correct_answer="application/problem+json",
                explanation="RFC 7807 designates `application/problem+json` as the standard Content-Type."
            ),
            QuizQuestionBlueprint(
                question="In RFC 7807, what does the `title` field represent?",
                options=[
                    "A short, human-readable summary of the problem type that remains consistent across occurrences",
                    "The author's job title",
                    "The HTML page title",
                    "The server hostname"
                ],
                correct_answer="A short, human-readable summary of the problem type that remains consistent across occurrences",
                explanation="The `title` provides a stable conceptual summary of the problem type."
            ),
            QuizQuestionBlueprint(
                question="Why is returning `{\"success\": true, \"data\": ...}` or generic non-standard error structures problematic for API consumers?",
                options=[
                    "Clients cannot write generic, reusable error-handling middleware and must write custom parsing logic for every single endpoint",
                    "It causes internet routers to drop packets",
                    "It consumes 100x more CPU power",
                    "It violates international copyright law"
                ],
                correct_answer="Clients cannot write generic, reusable error-handling middleware and must write custom parsing logic for every single endpoint",
                explanation="Inconsistent error formats force frontend clients to write fragile, fragmented error handling."
            ),
            QuizQuestionBlueprint(
                question="In RFC 7807, which field provides the specific contextual explanation for this particular error occurrence?",
                options=["detail", "title", "type", "instance"],
                correct_answer="detail",
                explanation="`detail` contains the specific human-readable explanation of what went wrong in this request."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 26 (Project): Complete Production-Grade CRUD REST API with Pagination & Versioning
    # ----------------------------------------------------
    DayBlueprint(
        order=26,
        title="Day 26 (Project): Complete Production-Grade CRUD REST API Lab",
        concept="Milestone Coding Lab: Building a production-ready REST API implementing versioning (`/v1`), full CRUD operations, pagination, filtering, and RFC 7807 error handling.",
        analogy="Today is taking your driver's license test after weeks of learning traffic rules. You will assemble all the rules of Phase 4 into a working, tested, production-grade microservice backend.",
        theory_sections=[
            {
                "heading": "Lab Requirements",
                "body": (
                    "In this milestone engineering project, you will build a complete 'Article Publishing & Moderation' API:\n"
                    "1. **Versioning**: Route prefixed under `/api/v1/articles`.\n"
                    "2. **CRUD**: Implement GET (list), POST (create), GET (single), PATCH (update), DELETE (remove).\n"
                    "3. **Pagination**: Implement `limit` and `offset` with total count.\n"
                    "4. **Filtering**: Allow filtering by `?status=published` and search `?q=keyword`.\n"
                    "5. **RFC 7807**: Return standard Problem Details on 400 and 404 errors."
                )
            },
            {
                "heading": "Verification Criteria",
                "body": (
                    "- POST returns 201 with `Location` header.\n"
                    "- DELETE returns 204 No Content.\n"
                    "- Invalid inputs return 422 or 400 with `application/problem+json`.\n"
                    "- Missing IDs return 404."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Complete Production CRUD Microservice in Flask",
                "code": "from flask import Flask, request, jsonify, Response\nimport math\n\napp = Flask(__name__)\n\nARTICLES = {}\nID_SEQ = 1\n\n# Helper: RFC 7807 Error Builder\ndef problem_response(status, title, detail):\n    payload = jsonify({'type': 'about:blank', 'title': title, 'status': status, 'detail': detail})\n    return payload, status, {'Content-Type': 'application/problem+json'}\n\n# 1. CREATE\n@app.route('/api/v1/articles', methods=['POST'])\ndef create_article():\n    global ID_SEQ\n    body = request.get_json(silent=True) or {}\n    if not body.get('title') or not body.get('content'):\n        return problem_response(400, 'Invalid Input', 'title and content are required')\n        \n    article = {\n        'id': ID_SEQ,\n        'title': body['title'],\n        'content': body['content'],\n        'status': body.get('status', 'draft')\n    }\n    ARTICLES[ID_SEQ] = article\n    ID_SEQ += 1\n    return jsonify(article), 201, {'Location': f'/api/v1/articles/{article[\"id\"]}'}\n\n# 2. LIST (with Pagination & Filtering)\n@app.route('/api/v1/articles', methods=['GET'])\ndef list_articles():\n    items = list(ARTICLES.values())\n    status_filter = request.args.get('status')\n    if status_filter:\n        items = [a for a in items if a['status'] == status_filter]\n    q = request.args.get('q')\n    if q:\n        items = [a for a in items if q.lower() in a['title'].lower()]\n        \n    limit = min(int(request.args.get('limit', 10)), 50)\n    offset = int(request.args.get('offset', 0))\n    \n    return jsonify({\n        'data': items[offset:offset+limit],\n        'pagination': {'total': len(items), 'limit': limit, 'offset': offset}\n    }), 200",
                "explanation": "Production-grade implementation of Create and List with pagination/filtering."
            },
            {
                "title": "Single Resource, Patch, and Delete Implementation",
                "code": "# 3. GET SINGLE\n@app.route('/api/v1/articles/<int:id>', methods=['GET'])\ndef get_single(id):\n    if id not in ARTICLES:\n        return problem_response(404, 'Not Found', f'Article {id} does not exist')\n    return jsonify(ARTICLES[id]), 200\n\n# 4. PATCH\n@app.route('/api/v1/articles/<int:id>', methods=['PATCH'])\ndef patch_article(id):\n    if id not in ARTICLES:\n        return problem_response(404, 'Not Found', f'Article {id} does not exist')\n    body = request.json or {}\n    if 'title' in body: ARTICLES[id]['title'] = body['title']\n    if 'content' in body: ARTICLES[id]['content'] = body['content']\n    if 'status' in body: ARTICLES[id]['status'] = body['status']\n    return jsonify(ARTICLES[id]), 200\n\n# 5. DELETE\n@app.route('/api/v1/articles/<int:id>', methods=['DELETE'])\ndef delete_article(id):\n    if id not in ARTICLES:\n        return problem_response(404, 'Not Found', f'Article {id} does not exist')\n    del ARTICLES[id]\n    return '', 204",
                "explanation": "Read, partial update, and deletion handlers."
            },
            {
                "title": "Verifying API via Automated Test Script",
                "code": "# Python script executing full verification cycle:\nimport requests\n\nBASE = 'http://localhost:5000/api/v1/articles'\n\n# Create\nres = requests.post(BASE, json={'title': 'REST Guide', 'content': 'Deep dive'})\nassert res.status_code == 201\nart_id = res.json()['id']\n\n# Read\nres = requests.get(f'{BASE}/{art_id}')\nassert res.status_code == 200\n\n# Delete\nres = requests.delete(f'{BASE}/{art_id}')\nassert res.status_code == 204\n\n# Verify 404 after delete\nres = requests.get(f'{BASE}/{art_id}')\nassert res.status_code == 404\nprint('✅ ALL TESTS PASSED!')",
                "explanation": "Automated verification suite validating endpoint contracts."
            },
            {
                "title": "Execution Terminal Output",
                "code": "# Running verification:\n# POST /api/v1/articles -> 201 Created (Location: /api/v1/articles/1)\n# GET /api/v1/articles/1 -> 200 OK\n# PATCH /api/v1/articles/1 -> 200 OK\n# DELETE /api/v1/articles/1 -> 204 No Content\n# GET /api/v1/articles/1 -> 404 Not Found (application/problem+json)",
                "explanation": "Expected lifecycle logs."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Complete Article API Endpoint",
            description="Write a complete Flask route `POST /api/v1/posts` that accepts `{'title': str}`, returns 400 with RFC 7807 JSON if title is missing, or returns 201 with `{'id': 1, 'title': title}` and `Location: /api/v1/posts/1`.",
            starter_code="from flask import Flask, request, jsonify\napp = Flask(__name__)\n\n# Implement endpoint\n",
            solution_code="from flask import Flask, request, jsonify\napp = Flask(__name__)\n\n@app.route('/api/v1/posts', methods=['POST'])\ndef add_post():\n    data = request.json or {}\n    if not data.get('title'):\n        return jsonify({'type': 'about:blank', 'title': 'Bad Request', 'status': 400}), 400, {'Content-Type': 'application/problem+json'}\n    return jsonify({'id': 1, 'title': data['title']}), 201, {'Location': '/api/v1/posts/1'}",
            expected_output="201 with Location header on success, 400 problem on error"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="In our production CRUD project, what status code and header must be returned when a new article is created?",
                options=[
                    "`201 Created` with a `Location: /api/v1/articles/{id}` header",
                    "`200 OK` with zero headers",
                    "`204 No Content` with an ETag",
                    "`302 Found` with a cookie"
                ],
                correct_answer="`201 Created` with a `Location: /api/v1/articles/{id}` header",
                explanation="Standard REST requires 201 Created accompanied by the Location header of the new resource."
            ),
            QuizQuestionBlueprint(
                question="Why is capping the `limit` parameter (e.g. `limit = min(requested_limit, 50)`) critical on collection endpoints?",
                options=[
                    "It prevents malicious or buggy clients from requesting `?limit=5000000` and crashing the server by exhausting memory",
                    "It makes the database smaller on disk",
                    "It allows HTML formatting",
                    "It bypasses authentication"
                ],
                correct_answer="It prevents malicious or buggy clients from requesting `?limit=5000000` and crashing the server by exhausting memory",
                explanation="Limit bounding protects databases and application memory from unbounded extraction attacks."
            ),
            QuizQuestionBlueprint(
                question="What should the Content-Type header be set to when returning an RFC 7807 error payload?",
                options=["application/problem+json", "text/html", "application/json", "text/plain"],
                correct_answer="application/problem+json",
                explanation="`application/problem+json` is the standardized media type for RFC 7807 problem details."
            ),
            QuizQuestionBlueprint(
                question="If a client attempts to execute `DELETE /api/v1/articles/999` and article 999 does not exist, what status code should be returned?",
                options=["404 Not Found", "200 OK", "500 Server Error", "409 Conflict"],
                correct_answer="404 Not Found",
                explanation="Targeting a non-existent singleton instance returns 404 Not Found."
            ),
            QuizQuestionBlueprint(
                question="Which HTTP method allows updating only the `title` of an article without re-sending its `content`?",
                options=["PATCH", "PUT", "POST", "GET"],
                correct_answer="PATCH",
                explanation="PATCH is explicitly designed for partial field updates."
            )
        ],
        is_project_day=True,
        project_name="Complete Production-Grade CRUD REST API Lab"
    ),

    # ----------------------------------------------------
    # Day 27: API Keys & Client Secrets
    # ----------------------------------------------------
    DayBlueprint(
        order=27,
        title="Day 27: API Keys & Client Secrets (Identity & Metering)",
        concept="Implementing API Key authentication: cryptographic generation, header transmission, rate metering, secret rotation, and server-to-server security.",
        analogy="An API Key is like a membership barcode at Costco. You scan it at the door: it identifies which company or account you belong to, checks if your subscription is paid up, and meters how many items you are allowed to buy today.",
        theory_sections=[
            {
                "heading": "What is an API Key?",
                "body": (
                    "An **API Key** is a long, cryptographically random string (e.g. `api_key_51Mz...`) generated by an API provider "
                    "to identify the calling application. API keys are primarily used for **machine-to-machine (server-to-server)** communication "
                    "and API usage tracking (metering/billing)."
                )
            },
            {
                "heading": "API Key vs User Credentials",
                "body": (
                    "- **API Keys identify the APPLICATION / PROJECT**, not the individual human user.\n"
                    "- API keys should **NEVER be committed to Git** or embedded in public client-side JavaScript or mobile apps (decompilation will reveal them!).\n"
                    "- Best practice: Store API keys in environment variables on your backend server."
                )
            },
            {
                "heading": "Transmission Patterns",
                "body": (
                    "1. **Custom Header (Recommended)**: `X-API-Key: <key>`\n"
                    "2. **Authorization Header**: `Authorization: ApiKey <key>`\n"
                    "3. **Query Parameter (Discouraged)**: `?api_key=<key>` (Vulnerable! Leaks into web server access logs and browser histories)."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Generating Cryptographically Secure API Keys in Python",
                "code": "import secrets\n\ndef generate_api_key(prefix=\"demo_key\") -> str:\n    # Generate 32 bytes of secure random entropy:\n    random_token = secrets.token_urlsafe(32)\n    return f\"{prefix}_{random_token}\"\n\nprint(generate_api_key())\n# Output: demo_key_8f3a1d9e5b2c4a7e9f1a2b3c4d5e6f7a8b9c0d1e2f3",
                "explanation": "Uses secrets module for cryptographically strong random token generation."
            },
            {
                "title": "API Key Authentication Middleware in Flask",
                "code": "from flask import Flask, request, jsonify\nimport hmac\n\napp = Flask(__name__)\n\n# Stored hashed keys in database:\nVALID_API_KEYS = {\n    'demo_key_secret123': {'account_id': 'acct_01', 'tier': 'enterprise'}\n}\n\n@app.before_request\ndef authenticate_api_key():\n    if request.path.startswith('/api/'):\n        api_key = request.headers.get('X-API-Key')\n        if not api_key or api_key not in VALID_API_KEYS:\n            return jsonify({'error': 'Unauthorized', 'message': 'Valid X-API-Key header required'}), 401\n            \n        # Attach authenticated tenant to request context:\n        request.tenant = VALID_API_KEYS[api_key]",
                "explanation": "Global middleware verifying API key before routing requests."
            },
            {
                "title": "Transmitting API Key via cURL",
                "code": "# Secure header transmission:\ncurl -X GET https://api.service.com/v1/metrics \\\n  -H \"X-API-Key: demo_key_secret123\"",
                "explanation": "Transmitting API key via custom header."
            },
            {
                "title": "API Key Rotation Strategy",
                "code": "# Dual-key rotation lifecycle:\n# 1. Account holds Primary Key and Secondary Key simultaneously.\n# 2. To rotate, application switches backend to Secondary Key.\n# 3. Old Primary Key is invalidated.\n# 4. Zero downtime during key migration!",
                "explanation": "Dual-key architecture prevents service outages during security rotation."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Implement API Key Checker",
            description="Write a function `validate_key(key: str, valid_keys: set) -> bool` using constant-time comparison `secrets.compare_digest` to prevent timing attacks.",
            starter_code="import secrets\ndef validate_key(key: str, valid_keys: set) -> bool:\n    # Implement secure constant-time check\n    pass",
            solution_code="import secrets\ndef validate_key(key: str, valid_keys: set) -> bool:\n    for valid in valid_keys:\n        if secrets.compare_digest(key, valid):\n            return True\n    return False",
            expected_output="True if key matches, False otherwise"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the primary operational distinction between an API Key and user login credentials?",
                options=[
                    "An API Key identifies and meters the calling client application/project, whereas user credentials identify an individual human user",
                    "API keys only work on Linux servers",
                    "User credentials can only be used once per day",
                    "There is no distinction"
                ],
                correct_answer="An API Key identifies and meters the calling client application/project, whereas user credentials identify an individual human user",
                explanation="API keys authenticate applications and manage metering quotas."
            ),
            QuizQuestionBlueprint(
                question="Why is passing API keys in URL query parameters (e.g. `?api_key=secret123`) considered a security vulnerability?",
                options=[
                    "Query strings are logged in plain text in server access logs, browser history, and proxy logs, exposing the secret key",
                    "Query parameters are blocked by firewalls",
                    "URLs cannot hold letters",
                    "Query strings take 10x longer to process"
                ],
                correct_answer="Query strings are logged in plain text in server access logs, browser history, and proxy logs, exposing the secret key",
                explanation="URLs are routinely stored in plain text logs, leaking sensitive credentials."
            ),
            QuizQuestionBlueprint(
                question="Why should private backend API keys (like a Stripe Secret Key) NEVER be embedded inside client-side React code or mobile apps?",
                options=[
                    "Anyone can inspect frontend browser source code or decompile mobile APKs to extract the secret key and impersonate your account",
                    "React cannot read strings",
                    "Mobile phones will overheat",
                    "Stripe will delete your account instantly"
                ],
                correct_answer="Anyone can inspect frontend browser source code or decompile mobile APKs to extract the secret key and impersonate your account",
                explanation="Client-side code is entirely readable by end-users; private keys must remain on secure servers."
            ),
            QuizQuestionBlueprint(
                question="Which standard Python module is recommended for generating cryptographically secure random API keys?",
                options=["secrets", "random", "math", "os.path"],
                correct_answer="secrets",
                explanation="The `secrets` module provides cryptographically strong pseudo-random number generation."
            ),
            QuizQuestionBlueprint(
                question="What is the architectural purpose of providing 'Dual API Keys' (Primary and Secondary) in cloud developer dashboards?",
                options=[
                    "To enable zero-downtime key rotation: clients can transition to the secondary key before invalidating the compromised primary key",
                    "To allow two people to code at once",
                    "To double the API speed",
                    "To bypass billing"
                ],
                correct_answer="To enable zero-downtime key rotation: clients can transition to the secondary key before invalidating the compromised primary key",
                explanation="Dual keys allow seamless rotation without taking production systems offline."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 28: Basic Authentication vs Bearer Tokens
    # ----------------------------------------------------
    DayBlueprint(
        order=28,
        title="Day 28: Basic Authentication vs Bearer Tokens",
        concept="Contrasting HTTP Basic Authentication (Base64 credentials) with token-based Bearer authentication (`Authorization: Bearer <token>`).",
        analogy="Basic Authentication is taping your actual house keys to every letter you mail. A Bearer Token is a hotel keycard: it doesn't have your name or permanent house lock on it; it only opens Room 302 for the next 24 hours, and if you lose it, the front desk can deactivate it instantly.",
        theory_sections=[
            {
                "heading": "HTTP Basic Authentication (RFC 7617)",
                "body": (
                    "In Basic Authentication, the client combines username and password with a colon (`username:password`), "
                    "encodes it in **Base64**, and sends it in the header:\n"
                    "`Authorization: Basic YWxhZGRpbjpvcGVuc2VzYW1l`\n"
                    "**Crucial Warning**: Base64 is **NOT ENCRYPTION!** It is an encoding that anyone can decode in 0.001 seconds. "
                    "Basic Auth must **ALWAYS** be transmitted over HTTPS."
                )
            },
            {
                "heading": "Bearer Token Authentication (RFC 6750)",
                "body": (
                    "In Bearer authentication, the client authenticates once (e.g. login) and receives an opaque or signed token. "
                    "For all subsequent requests, the client sends:\n"
                    "`Authorization: Bearer <token>`\n"
                    "The term 'Bearer' literally means: *'Whoever bears (holds) this token is granted access'*. "
                    "The client never sends raw passwords on routine API calls."
                )
            },
            {
                "heading": "Key Security Advantages of Tokens",
                "body": (
                    "1. Passwords are only transmitted once across the network (at login).\n"
                    "2. Tokens have strict **expiration times** (TTL, e.g. 15 minutes).\n"
                    "3. Tokens can have granular **scopes** (e.g. read-only permissions).\n"
                    "4. Tokens can be revoked without forcing the user to change their actual password."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Deconstructing Basic Auth Base64 in Python",
                "code": "import base64\n\n# Client creates Basic Auth header:\ncredentials = \"alice:supersecretpassword\"\nencoded = base64.b64encode(credentials.encode()).decode()\nheader_val = f\"Basic {encoded}\"\nprint(f\"Header: Authorization: {header_val}\")\n# Output: Basic YWxpY2U6c3VwZXJzZWNyZXRwYXNzd29yZA==\n\n# Anyone intercepting the header can decode it instantly:\ndecoded = base64.b64decode(encoded).decode()\nprint(f\"Decoded credentials: {decoded}\")",
                "explanation": "Proves that Base64 encoding provides zero encryption security."
            },
            {
                "title": "Verifying Basic Auth in Flask",
                "code": "from flask import Flask, request, jsonify\n\napp = Flask(__name__)\n\n@app.route('/api/basic-secure')\ndef basic_secure():\n    auth = request.authorization\n    if not auth or auth.username != 'admin' or auth.password != 'secret123':\n        # Prompt browser for credentials:\n        return ('Unauthorized', 401, {'WWW-Authenticate': 'Basic realm=\"Login Required\"'})\n    return jsonify({'msg': 'Authenticated via Basic Auth'})",
                "explanation": "Using Flask's built-in request.authorization helper."
            },
            {
                "title": "Parsing Bearer Tokens in Node.js",
                "code": "const express = require('express');\nconst app = express();\n\nconst authenticateBearer = (req, res, next) => {\n    const authHeader = req.headers['authorization'];\n    if (!authHeader || !authHeader.startsWith('Bearer ')) {\n        return res.status(401).json({ error: 'Bearer token required' });\n    }\n    const token = authHeader.split(' ')[1];\n    if (token !== 'valid_session_token_xyz') {\n        return res.status(403).json({ error: 'Invalid or expired token' });\n    }\n    next();\n};\n\napp.get('/api/v1/protected', authenticateBearer, (req, res) => {\n    res.json({ secret: 'Classified data' });\n});",
                "explanation": "Express middleware extracting and validating Bearer tokens."
            },
            {
                "title": "Comparison Summary",
                "code": "# Criterion         | Basic Authentication      | Bearer Token Authentication\n# ------------------+---------------------------+----------------------------\n# Sent Data         | Username:Password (Base64)| Opaque string or signed JWT\n# Password Exposure | Sent with every request!  | Sent ONLY once at login\n# Expiration        | Never expires             | Short-lived (e.g. 15 mins)\n# Granular Scopes   | No                        | Yes (Read, Write, Admin)",
                "explanation": "Side-by-side architectural trade-offs."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Extract Bearer Token from Header String",
            description="Write a Python function `extract_bearer(header: str) -> str | None` that extracts the token substring from an 'Authorization' header string formatted as 'Bearer <token>'. Return None if prefix is missing.",
            starter_code="def extract_bearer(header: str) -> str | None:\n    # Extract token\n    pass",
            solution_code="def extract_bearer(header: str) -> str | None:\n    if header and header.startswith('Bearer '):\n        return header.split(' ', 1)[1].strip()\n    return None",
            expected_output="'my_token' when header is 'Bearer my_token'"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Is Base64 encoding used in HTTP Basic Authentication considered a form of encryption?",
                options=[
                    "No, Base64 is purely an encoding scheme that can be trivially reversed in milliseconds by anyone; it provides zero confidentiality without HTTPS",
                    "Yes, Base64 is military-grade AES encryption",
                    "Yes, it requires a private key to decode",
                    "Only on Windows"
                ],
                correct_answer="No, Base64 is purely an encoding scheme that can be trivially reversed in milliseconds by anyone; it provides zero confidentiality without HTTPS",
                explanation="Base64 encodes binary to ASCII without any secret key or encryption."
            ),
            QuizQuestionBlueprint(
                question="What is the literal meaning of the word 'Bearer' in Bearer token authentication?",
                options=[
                    "Whoever possesses (bears) the token is granted access, regardless of who originally requested it",
                    "The token is heavy like a bear",
                    "The token is made by Apple",
                    "The server bears the cost of the token"
                ],
                correct_answer="Whoever possesses (bears) the token is granted access, regardless of who originally requested it",
                explanation="Bearer authentication grants authorization to the entity presenting the valid token."
            ),
            QuizQuestionBlueprint(
                question="Why is Bearer token authentication significantly safer than Basic authentication for routine API calls?",
                options=[
                    "The user's actual password is sent across the network only once at login; subsequent requests use short-lived, revocable tokens",
                    "Tokens don't use internet bandwidth",
                    "Basic authentication was deleted from the internet",
                    "Bearer tokens cannot be intercepted"
                ],
                correct_answer="The user's actual password is sent across the network only once at login; subsequent requests use short-lived, revocable tokens",
                explanation="Tokens minimize raw password exposure across networks."
            ),
            QuizQuestionBlueprint(
                question="What HTTP header does a server return with a `401 Unauthorized` status code to challenge a client for Basic Auth credentials?",
                options=["WWW-Authenticate: Basic realm=\"...\"", "Challenge: Basic", "Authenticate-Now: true", "Prompt: Password"],
                correct_answer="WWW-Authenticate: Basic realm=\"...\"",
                explanation="`WWW-Authenticate` informs user agents which authentication scheme is expected."
            ),
            QuizQuestionBlueprint(
                question="What header format correctly presents a Bearer token named `xyz123`?",
                options=["Authorization: Bearer xyz123", "Bearer: xyz123", "Token: Bearer xyz123", "Auth-Token: xyz123"],
                correct_answer="Authorization: Bearer xyz123",
                explanation="The standard header format is `Authorization: Bearer <token>`."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 29: JWT (JSON Web Tokens) - Structure, Signing, aur Verification
    # ----------------------------------------------------
    DayBlueprint(
        order=29,
        title="Day 29: JWT (JSON Web Tokens): Structure, Signing, and Verification",
        concept="Deep architectural dissection of RFC 7519 JSON Web Tokens: Header, Payload (Claims), Signature, Symmetric (HS256) vs Asymmetric (RS256) signing, and token validation.",
        analogy="A JWT is like a tamper-evident holographic concert wristband. The wristband has printed text (Payload: 'VIP Access, Valid until Midnight') and an official metallic holographic seal (Signature). If anyone uses a pen to change 'General Admission' to 'VIP', the holographic seal breaks and the bouncer rejects it instantly.",
        theory_sections=[
            {
                "heading": "The Anatomy of a JWT",
                "body": (
                    "A **JSON Web Token (JWT)** is a compact, URL-safe means of representing claims to be transferred between two parties. "
                    "A JWT string consists of three distinct parts separated by dots (`.`):\n"
                    "```text\n"
                    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkFsaWNlIiwiYWRtaW4iOnRydWUsImV4cCI6MTY5NTAwMDAwMH0.7a4e8c1d5f2a1b9e3f4a5c6d7e8f9a0b1c2d3e4f\n"
                    "   [Part 1: Header (Red)]           .            [Part 2: Payload (Purple)]             .         [Part 3: Signature (Cyan)]\n"
                    "```\n"
                    "1. **Header**: Contains metadata: algorithm (`alg`: HS256/RS256) and token type (`typ`: JWT).\n"
                    "2. **Payload**: The claims/data (`sub`: subject, `exp`: expiration timestamp, `role`: admin).\n"
                    "3. **Signature**: Cryptographic hash generated by combining Header + Payload + Secret Key."
                )
            },
            {
                "heading": "Standard Registered Claims",
                "body": (
                    "- `sub` (Subject): The user ID.\n"
                    "- `exp` (Expiration Time): Unix epoch timestamp after which token is invalid.\n"
                    "- `iat` (Issued At): When the token was created.\n"
                    "- `iss` (Issuer): Who created the token (e.g. `auth.company.com`)."
                )
            },
            {
                "heading": "Symmetric (HS256) vs Asymmetric (RS256) Signing",
                "body": (
                    "- **HS256 (HMAC SHA-256)**: Single shared secret key. Fast, but both signer and verifier must know the same secret key.\n"
                    "- **RS256 (RSA Signature with SHA-256)**: Asymmetric keypair. The auth server signs with a **Private Key**; microservices verify using a public **Public Key** without being able to forge tokens!"
                )
            }
        ],
        code_snippets=[
            {
                "title": "Creating and Signing a JWT in Python (PyJWT)",
                "code": "import jwt\nimport time\n\nSECRET_KEY = \"super_secret_company_key_2026\"\n\n# Payload with standard claims (exp, sub) and custom claims (role):\npayload = {\n    \"sub\": \"user_42\",\n    \"name\": \"Alice Dev\",\n    \"role\": \"SUPER_ADMIN\",\n    \"iat\": int(time.time()),\n    \"exp\": int(time.time()) + 3600  # Expires in 1 hour\n}\n\n# Sign token using HMAC SHA-256:\ntoken = jwt.encode(payload, SECRET_KEY, algorithm=\"HS256\")\nprint(f\"Generated JWT:\\n{token}\")",
                "explanation": "Generates a signed JWT with expiration and role claims."
            },
            {
                "title": "Verifying and Decoding a JWT",
                "code": "# Verifying token signature and validating expiration:\ntry:\n    decoded = jwt.decode(token, SECRET_KEY, algorithms=[\"HS256\"])\n    print(f\"Valid Token! User: {decoded['sub']}, Role: {decoded['role']}\")\nexcept jwt.ExpiredSignatureError:\n    print(\"❌ Token has expired!\")\nexcept jwt.InvalidTokenError:\n    print(\"❌ Invalid token signature or corrupted payload!\")",
                "explanation": "Validates cryptographic signature and checks expiration automatically."
            },
            {
                "title": "How Signature Verification Works Mathematically",
                "code": "# The signature is computed as:\n# Signature = HMACSHA256(\n#    base64UrlEncode(header) + \".\" + base64UrlEncode(payload),\n#    secret_key\n# )\n# If a hacker edits payload \"role\": \"user\" -> \"role\": \"admin\",\n# the signature will not match unless they know the secret_key!",
                "explanation": "Mathematical integrity guarantees tamper-evidence."
            },
            {
                "title": "Security Warning: The 'none' Algorithm Vulnerability",
                "code": "# Never allow the 'none' algorithm in verification middleware:\n# Attackers used to send: {\"alg\": \"none\"} with no signature!\n# Modern libraries (like PyJWT) block 'none' algorithm by default.",
                "explanation": "Famous historical security vulnerability in JWT parsers."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Decode and Verify JWT Token",
            description="Write a Python function `verify_token(token: str, secret: str) -> dict | None` that decodes an HS256 token and returns the payload dict, or returns None if the token is invalid or expired.",
            starter_code="import jwt\ndef verify_token(token: str, secret: str) -> dict | None:\n    # Implement verification\n    pass",
            solution_code="import jwt\ndef verify_token(token: str, secret: str) -> dict | None:\n    try:\n        return jwt.decode(token, secret, algorithms=['HS256'])\n    except jwt.PyJWTError:\n        return None",
            expected_output="payload dict if valid, None if invalid"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What are the three components that make up a JSON Web Token (JWT), in order?",
                options=[
                    "Header, Payload, Signature",
                    "Username, Password, Domain",
                    "Key, Hash, Encryption",
                    "Prefix, Body, Suffix"
                ],
                correct_answer="Header, Payload, Signature",
                explanation="A JWT is formatted as `Header.Payload.Signature`."
            ),
            QuizQuestionBlueprint(
                question="Is the Payload of a standard JWT encrypted and hidden from the client by default?",
                options=[
                    "No, the payload is only Base64URL-encoded (tamper-evident, but easily readable by anyone who decodes it); do NOT store sensitive secrets like passwords in JWT payloads",
                    "Yes, JWTs are military-grade encrypted",
                    "Only on Linux servers",
                    "Only if using HTTPS"
                ],
                correct_answer="No, the payload is only Base64URL-encoded (tamper-evident, but easily readable by anyone who decodes it); do NOT store sensitive secrets like passwords in JWT payloads",
                explanation="JWTs provide integrity/signing, not confidentiality/encryption (unless using JWE)."
            ),
            QuizQuestionBlueprint(
                question="What does the standard registered claim `exp` represent in a JWT payload?",
                options=[
                    "Expiration time (as a Unix epoch timestamp) after which the token must be rejected",
                    "Experience points of the user",
                    "The export format of the database",
                    "The expected response size"
                ],
                correct_answer="Expiration time (as a Unix epoch timestamp) after which the token must be rejected",
                explanation="`exp` defines the expiration timestamp verified by parsers."
            ),
            QuizQuestionBlueprint(
                question="What is the advantage of using asymmetric RS256 (RSA) signing over symmetric HS256 for microservice architectures?",
                options=[
                    "The authentication service signs tokens with a private key, while dozens of internal microservices can verify tokens using the public key without needing the signing key",
                    "RS256 is 100x faster than HS256",
                    "RS256 tokens never expire",
                    "RS256 does not require internet"
                ],
                correct_answer="The authentication service signs tokens with a private key, while dozens of internal microservices can verify tokens using the public key without needing the signing key",
                explanation="Public keys can be distributed safely to verifiers without risking token forgery."
            ),
            QuizQuestionBlueprint(
                question="What happens if an attacker modifies the payload of a JWT from `\"role\": \"user\"` to `\"role\": \"admin\"`?",
                options=[
                    "The signature verification will fail on the server because the attacker does not possess the secret signing key required to recompute a valid signature",
                    "The server will grant admin access automatically",
                    "The client's computer will lock up",
                    "The token will be deleted"
                ],
                correct_answer="The signature verification will fail on the server because the attacker does not possess the secret signing key required to recompute a valid signature",
                explanation="Modifying any byte in the header or payload breaks the signature verification."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 30: OAuth 2.0 (Authorization Framework) & OpenID Connect
    # ----------------------------------------------------
    DayBlueprint(
        order=30,
        title="Day 30: OAuth 2.0 & OpenID Connect (Delegated Authorization)",
        concept="Demystifying modern authentication infrastructure: OAuth 2.0 roles (Resource Owner, Client, Authorization Server, Resource Server), Authorization Code Flow with PKCE, and OpenID Connect (OIDC).",
        analogy="OAuth 2.0 is like a valet parking key for your car. You don't give the valet your master house key; you give them a restricted valet key that only starts the engine and drives 2 miles per hour, but cannot open your trunk or glove compartment.",
        theory_sections=[
            {
                "heading": "What Problem Does OAuth 2.0 Solve?",
                "body": (
                    "Before OAuth, if you wanted an app (e.g. Yelp) to find your friends on Facebook, Yelp asked you for your Facebook username and password! "
                    "This anti-pattern is catastrophic: Yelp could read your private messages and do anything on your account. "
                    "**OAuth 2.0 is an Authorization Framework** that allows third-party applications to obtain limited access to a user's resources "
                    "without ever seeing the user's password."
                )
            },
            {
                "heading": "The 4 Core Roles in OAuth 2.0",
                "body": (
                    "1. **Resource Owner**: The human user who owns the data.\n"
                    "2. **Client**: The third-party application requesting access (e.g. Spotify app).\n"
                    "3. **Authorization Server**: The server that authenticates the user and issues tokens (e.g. Google Accounts).\n"
                    "4. **Resource Server**: The API hosting the protected data (e.g. Google Drive API, Google Contacts API)."
                )
            },
            {
                "heading": "The Golden Flow: Authorization Code with PKCE",
                "body": (
                    "1. User clicks 'Log in with Google'.\n"
                    "2. User is redirected to Google's consent screen showing requested **scopes** (`read:contacts`).\n"
                    "3. User approves. Google redirects back to Client with a temporary **Authorization Code**.\n"
                    "4. Client's backend exchanges the Authorization Code + Secret (or PKCE verifier) for an **Access Token**.\n"
                    "5. Client uses Access Token to query the Resource Server API."
                )
            },
            {
                "heading": "OAuth 2.0 vs OpenID Connect (OIDC)",
                "body": (
                    "- **OAuth 2.0 is for AUTHORIZATION** ('Can this app access your photos?'). It issues an **Access Token**.\n"
                    "- **OpenID Connect (OIDC) is for AUTHENTICATION** ('Who is this user?'). It adds an **ID Token** (a JWT) on top of OAuth 2.0 to provide single sign-on (SSO) identity."
                )
            }
        ],
        code_snippets=[
            {
                "title": "OAuth 2.0 Authorization Request",
                "code": "# 1. Redirect user to Authorization Server:\nhttps://accounts.google.com/o/oauth2/v2/auth?\n  client_id=my_app_client_id_123&\n  redirect_uri=https://myapp.com/callback&\n  response_type=code&\n  scope=openid%20profile%20email&\n  state=csrf_security_token_abc&\n  code_challenge=pkce_challenge_hash",
                "explanation": "Browser initiates OAuth consent screen."
            },
            {
                "title": "Exchanging Authorization Code for Tokens",
                "code": "# 2. Backend exchanges temporary code for Access Token + ID Token:\nPOST /oauth/token HTTP/1.1\nHost: accounts.google.com\nContent-Type: application/x-www-form-urlencoded\n\ngrant_type=authorization_code&\ncode=4/0AY0e-g7a4e8c1...&\nredirect_uri=https://myapp.com/callback&\nclient_id=my_app_client_id_123&\nclient_secret=super_secret_client_secret_xyz",
                "explanation": "Server-to-server token exchange."
            },
            {
                "title": "Token Response with ID Token and Access Token",
                "code": "# Response from Authorization Server:\n{\n  \"access_token\": \"ya29.a0AfH6SM...\",  // Used to call APIs (OAuth 2.0)\n  \"token_type\": \"Bearer\",\n  \"expires_in\": 3600,\n  \"refresh_token\": \"1//04b2c1d...\", // Used to get new access token\n  \"id_token\": \"eyJhbGciOiJSUz...\"     // User identity profile (OIDC)\n}",
                "explanation": "Tokens returned for API access and user identity."
            },
            {
                "title": "Refresh Token Grant Flow",
                "code": "# When access token expires after 1 hour, refresh silently without prompting user:\nPOST /oauth/token HTTP/1.1\nHost: accounts.google.com\n\ngrant_type=refresh_token&\nrefresh_token=1//04b2c1d...&\nclient_id=my_app_client_id_123&\nclient_secret=my_secret",
                "explanation": "Silent refresh without user re-authentication."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Build OAuth Authorization URL",
            description="Write a Python function `build_auth_url(client_id: str, redirect_uri: str, scope: str) -> str` that formats the standard OAuth 2.0 authorization URL for endpoint 'https://auth.dev.com/authorize' with response_type 'code'.",
            starter_code="def build_auth_url(client_id: str, redirect_uri: str, scope: str) -> str:\n    # Return formatted authorization URL\n    pass",
            solution_code="from urllib.parse import urlencode\ndef build_auth_url(client_id: str, redirect_uri: str, scope: str) -> str:\n    params = {'client_id': client_id, 'redirect_uri': redirect_uri, 'scope': scope, 'response_type': 'code'}\n    return f'https://auth.dev.com/authorize?{urlencode(params)}'",
            expected_output="https://auth.dev.com/authorize?client_id=...&response_type=code..."
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the foundational architectural difference between OAuth 2.0 and OpenID Connect (OIDC)?",
                options=[
                    "OAuth 2.0 is for delegated Authorization ('What resources can this app access?'); OpenID Connect is an identity layer on top of OAuth for Authentication ('Who is this user?')",
                    "OAuth is for Google; OIDC is for Microsoft",
                    "OAuth is for databases; OIDC is for servers",
                    "There is no difference"
                ],
                correct_answer="OAuth 2.0 is for delegated Authorization ('What resources can this app access?'); OpenID Connect is an identity layer on top of OAuth for Authentication ('Who is this user?')",
                explanation="OAuth 2.0 handles permissions (Access Token); OIDC handles identity (ID Token)."
            ),
            QuizQuestionBlueprint(
                question="In OAuth 2.0, what token is issued to allow an application to silently obtain a new Access Token without prompting the user to log in again?",
                options=["Refresh Token", "ID Token", "Authorization Code", "Magic Link"],
                correct_answer="Refresh Token",
                explanation="Refresh Tokens are long-lived tokens exchanged for fresh access tokens."
            ),
            QuizQuestionBlueprint(
                question="Why is the Authorization Code Flow with PKCE (Proof Key for Code Exchange) recommended over the legacy Implicit Grant for mobile and single-page apps (SPAs)?",
                options=[
                    "PKCE eliminates client secret storage in public clients and dynamically cryptographically binds code exchanges, preventing token interception attacks",
                    "PKCE runs without internet",
                    "PKCE is 100x smaller in size",
                    "PKCE does not require HTTPS"
                ],
                correct_answer="PKCE eliminates client secret storage in public clients and dynamically cryptographically binds code exchanges, preventing token interception attacks",
                explanation="PKCE protects public clients where storing client secrets is insecure."
            ),
            QuizQuestionBlueprint(
                question="In the OAuth 2.0 framework, what role is fulfilled by the human user who owns the account data?",
                options=["The Resource Owner", "The Client", "The Resource Server", "The Authorization Server"],
                correct_answer="The Resource Owner",
                explanation="The user granting permission is officially designated as the Resource Owner."
            ),
            QuizQuestionBlueprint(
                question="What parameter is passed in the OAuth authorization URL to limit access strictly to requested resources (e.g. `read:photos`)?",
                options=["scope", "permission", "limit", "access_level"],
                correct_answer="scope",
                explanation="The `scope` parameter defines the exact permissions requested from the user."
            )
        ]
    )
]
