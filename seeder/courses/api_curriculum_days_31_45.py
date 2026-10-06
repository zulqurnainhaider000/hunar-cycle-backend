"""
Complete APIs & Web Services Architecture Curriculum - Days 31 to 45
Phase 5: API Security & Authentication - Part 2 (Days 31-34)
Phase 6: API Integration (Consuming APIs) (Days 35-41)
Phase 7: Advanced Integration Concepts - Part 1 (Days 42-45 of 42-48)
"""

from seeder.course_blueprint import DayBlueprint, QuizQuestionBlueprint, CodingChallengeBlueprint

DAYS_31_TO_45 = [
    # ----------------------------------------------------
    # Day 31: CORS (Cross-Origin Resource Sharing)
    # ----------------------------------------------------
    DayBlueprint(
        order=31,
        title="Day 31: CORS (Cross-Origin Resource Sharing)",
        concept="Mastering browser security: the Same-Origin Policy (SOP), CORS headers (`Access-Control-Allow-Origin`), and handling preflight `OPTIONS` requests.",
        analogy="CORS is a security guard stationed at your web browser's front door. The guard says: 'You loaded this webpage from `frontend.com`, but the JavaScript is trying to secretly talk to `api.bank.com`. I won't let you talk to the bank unless the bank explicitly gives written permission in advance!'",
        theory_sections=[
            {
                "heading": "The Same-Origin Policy (SOP)",
                "body": (
                    "Web browsers enforce the **Same-Origin Policy** to protect users from malicious scripts. "
                    "An **Origin** is defined by three tuples: **Protocol (Scheme) + Hostname + Port**.\n"
                    "- `https://myapp.com:443` and `https://myapp.com:8080` are DIFFERENT origins (different ports).\n"
                    "- `http://myapp.com` and `https://myapp.com` are DIFFERENT origins (different protocols).\n"
                    "By default, browsers block JavaScript from reading HTTP responses from a different origin."
                )
            },
            {
                "heading": "How CORS Works",
                "body": (
                    "**CORS (Cross-Origin Resource Sharing)** is a mechanism that allows servers to declare which origins are permitted to access their resources. "
                    "The server communicates this via HTTP response headers:\n"
                    "- `Access-Control-Allow-Origin`: Allowed domain (e.g. `https://myapp.com` or `*` for public APIs).\n"
                    "- `Access-Control-Allow-Methods`: Permitted verbs (`GET, POST, PUT, DELETE, OPTIONS`).\n"
                    "- `Access-Control-Allow-Headers`: Allowed custom headers (`Content-Type, Authorization`).\n"
                    "- `Access-Control-Allow-Credentials`: Allows sending cookies/auth across origins."
                )
            },
            {
                "heading": "Preflight Requests (`OPTIONS`)",
                "body": (
                    "For 'unsafe' requests (e.g. methods other than GET/POST, or requests with `application/json` or `Authorization` headers), "
                    "the browser automatically sends an HTTP `OPTIONS` **preflight request** before sending the actual request. "
                    "If the server doesn't respond with valid CORS headers, the browser blocks the real request and logs the dreaded "
                    "`'CORS error'` in the developer console!"
                )
            }
        ],
        code_snippets=[
            {
                "title": "Configuring CORS in Express.js",
                "code": "const express = require('express');\nconst cors = require('cors');\nconst app = express();\n\n// Specific whitelisted origins with credentials support:\nconst corsOptions = {\n    origin: ['https://admin.mycompany.com', 'https://mycompany.com'],\n    methods: ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'],\n    allowedHeaders: ['Content-Type', 'Authorization', 'X-Requested-With'],\n    credentials: true\n};\n\napp.use(cors(corsOptions));",
                "explanation": "Production configuration of CORS middleware in Node.js."
            },
            {
                "title": "Manual CORS Headers in Python Flask",
                "code": "from flask import Flask, make_response\n\napp = Flask(__name__)\n\n@app.after_request\ndef add_cors_headers(response):\n    # Allow specific origin:\n    response.headers['Access-Control-Allow-Origin'] = 'https://dashboard.example.com'\n    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'\n    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'\n    return response",
                "explanation": "Global after_request handler injecting CORS headers in Flask."
            },
            {
                "title": "Anatomy of an OPTIONS Preflight Exchange",
                "code": "# 1. Browser sends preflight check:\n# OPTIONS /api/v1/orders HTTP/1.1\n# Host: api.store.com\n# Origin: https://front.store.com\n# Access-Control-Request-Method: DELETE\n# Access-Control-Request-Headers: Authorization\n\n# 2. Server approves:\n# HTTP/1.1 204 No Content\n# Access-Control-Allow-Origin: https://front.store.com\n# Access-Control-Allow-Methods: GET, POST, DELETE, OPTIONS\n# Access-Control-Allow-Headers: Authorization\n# Access-Control-Max-Age: 86400 (Cache preflight for 24 hours!)",
                "explanation": "Preflight negotiation flow before actual DELETE request."
            },
            {
                "title": "Crucial Truth: CORS is a BROWSER Mechanism",
                "code": "# Important developer insight:\n# CORS is enforced STRICTLY by Web Browsers (Chrome, Safari, Firefox)!\n# Server-to-server calls (Python requests, cURL, Postman) NEVER trigger CORS\n# and can query any server without restriction.",
                "explanation": "CORS exists to protect browser users, not server-to-server calls."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Inject CORS Header into Flask Response",
            description="Write a Flask endpoint `/api/public-data` that returns `{'status': 'ok'}` with the response header `Access-Control-Allow-Origin: *`.",
            starter_code="from flask import Flask, jsonify\napp = Flask(__name__)\n\n# Implement public CORS route\n",
            solution_code="from flask import Flask, jsonify\napp = Flask(__name__)\n\n@app.route('/api/public-data')\ndef public_data():\n    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': '*'}",
            expected_output="{'status': 'ok'}, Access-Control-Allow-Origin: *"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What three components define an 'Origin' in the browser's Same-Origin Policy?",
                options=[
                    "Protocol (Scheme), Hostname, and Port",
                    "IP Address, Operating System, and Browser Name",
                    "Username, Password, and Domain",
                    "Path, Query, and Fragment"
                ],
                correct_answer="Protocol (Scheme), Hostname, and Port",
                explanation="An origin is defined by scheme + host + port. If any of the three differ, it is cross-origin."
            ),
            QuizQuestionBlueprint(
                question="Does a CORS error occur when you execute an API request using cURL or Python's `requests` library in the terminal?",
                options=[
                    "No, CORS is a security mechanism enforced strictly by web browsers to protect end-users; cURL and backend scripts ignore CORS",
                    "Yes, cURL always fails on CORS",
                    "Only on Windows terminal",
                    "Only if using VPN"
                ],
                correct_answer="No, CORS is a security mechanism enforced strictly by web browsers to protect end-users; cURL and backend scripts ignore CORS",
                explanation="CORS is a browser-only security feature; backend clients do not enforce it."
            ),
            QuizQuestionBlueprint(
                question="Which HTTP method does a web browser send automatically as a 'preflight' check before executing an unsafe cross-origin request?",
                options=["OPTIONS", "HEAD", "TRACE", "POST"],
                correct_answer="OPTIONS",
                explanation="Browsers issue an `OPTIONS` preflight request to verify server permissions."
            ),
            QuizQuestionBlueprint(
                question="Which HTTP response header tells the browser which external origins are allowed to read the API response?",
                options=["Access-Control-Allow-Origin", "Allow-Domain", "Origin-Permitted", "CORS-Security-Key"],
                correct_answer="Access-Control-Allow-Origin",
                explanation="`Access-Control-Allow-Origin` specifies allowed calling origins."
            ),
            QuizQuestionBlueprint(
                question="What is the purpose of the `Access-Control-Max-Age` header in a preflight response?",
                options=[
                    "It tells the browser how many seconds it can cache the preflight approval without sending repeated OPTIONS checks",
                    "It specifies the user's age",
                    "It sets the server timeout",
                    "It expires user passwords"
                ],
                correct_answer="It tells the browser how many seconds it can cache the preflight approval without sending repeated OPTIONS checks",
                explanation="Caching preflight checks with `Access-Control-Max-Age` eliminates redundant round-trips."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 32: Rate Limiting & Throttling
    # ----------------------------------------------------
    DayBlueprint(
        order=32,
        title="Day 32: Rate Limiting & Throttling (Protecting APIs from Abuse)",
        concept="Engineering API defense mechanisms: Token Bucket, Leaky Bucket, and Sliding Window rate limiting algorithms with Redis and standard HTTP 429 response headers.",
        analogy="Rate limiting is like a nightclub bouncer only letting in 5 people per minute, or an arcade token machine: you get 10 tokens; when you run out of tokens, you have to wait for the machine to refill before playing another game.",
        theory_sections=[
            {
                "heading": "Why Rate Limiting is Non-Negotiable",
                "body": (
                    "Without rate limiting, any malicious bot, misconfigured client loop, or DDoS attack can overwhelm your database, "
                    "exhaust server memory, and run up astronomical cloud infrastructure bills. "
                    "Rate limiting caps the number of requests a client (identified by IP or API Key) can make within a time window."
                )
            },
            {
                "heading": "Core Rate Limiting Algorithms",
                "body": (
                    "1. **Fixed Window Counter**: Divides time into fixed buckets (e.g. 1 minute). Flaw: allows traffic bursts at the boundary edge (e.g. 100 requests at 11:59 and 100 at 12:00 = 200 in 2 seconds!).\n"
                    "2. **Sliding Window Log / Counter**: Smooths boundary bursts by calculating a weighted average of previous and current windows.\n"
                    "3. **Token Bucket**: Bucket holds up to $B$ tokens. Refills at a constant rate $r$ tokens/sec. Allows controlled bursts up to bucket capacity.\n"
                    "4. **Leaky Bucket**: Requests enter a queue and leak out at a strictly constant rate. Smooths bursty traffic into steady streams."
                )
            },
            {
                "heading": "Standard Rate Limit Response Headers",
                "body": (
                    "Informative APIs return standard headers with every response:\n"
                    "- `RateLimit-Limit`: Maximum requests permitted per window (e.g. `100`).\n"
                    "- `RateLimit-Remaining`: Remaining request quota (e.g. `4`).\n"
                    "- `RateLimit-Reset`: Unix timestamp when the quota resets.\n"
                    "- `Retry-After`: Sent on `429 Too Many Requests` telling client how many seconds to wait."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Sliding Window Rate Limiter with Redis in Python",
                "code": "import time\nimport redis\n\nr = redis.Redis(host='localhost', port=6379, db=0)\n\ndef is_rate_limited(client_ip: str, limit: int = 100, window_seconds: int = 60) -> tuple[bool, int]:\n    current_time = time.time()\n    key = f\"rate:{client_ip}\"\n    pipeline = r.pipeline()\n    \n    # 1. Remove timestamps older than the active window:\n    pipeline.zremrangebyscore(key, 0, current_time - window_seconds)\n    # 2. Count requests in active window:\n    pipeline.zcard(key)\n    # 3. Add current request timestamp:\n    pipeline.zadd(key, {str(current_time): current_time})\n    # 4. Set TTL on the key:\n    pipeline.expire(key, window_seconds)\n    \n    _, request_count, _, _ = pipeline.execute()\n    remaining = max(0, limit - request_count)\n    \n    if request_count > limit:\n        return True, 0  # Blocked! (429)\n    return False, remaining",
                "explanation": "Sliding window log algorithm using Redis Sorted Sets (ZSET)."
            },
            {
                "title": "Rate Limiting Middleware in Express with express-rate-limit",
                "code": "const rateLimit = require('express-rate-limit');\n\nconst apiLimiter = rateLimit({\n    windowMs: 15 * 60 * 1000, // 15 minutes\n    max: 100, // Limit each IP to 100 requests per windowMs\n    standardHeaders: true, // Return RateLimit-* headers\n    legacyHeaders: false,\n    message: {\n        error: 'Too Many Requests',\n        message: 'You have exceeded the 100 requests per 15-minute quota.'\n    }\n});\n\napp.use('/api/', apiLimiter);",
                "explanation": "Standard Express rate limiting middleware."
            },
            {
                "title": "Sample 429 Too Many Requests Response",
                "code": "# Response from throttled server:\nHTTP/1.1 429 Too Many Requests\nContent-Type: application/json\nRetry-After: 45\nRateLimit-Limit: 100\nRateLimit-Remaining: 0\nRateLimit-Reset: 1767139245\n\n{\n  \"error\": \"Rate limit exceeded\",\n  \"retry_after_seconds\": 45\n}",
                "explanation": "429 response informing client of remaining wait duration."
            },
            {
                "title": "Tiered Rate Limiting Strategy",
                "code": "# Free Tier:         60 requests / minute\n# Pro Tier:        1000 requests / minute\n# Enterprise Tier: 5000 requests / minute\n# Tier assigned via authenticated API Key rather than IP address!",
                "explanation": "Differentiating rate quotas based on subscription tier."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Check Rate Limit Threshold",
            description="Write a Python function `check_quota(count: int, max_limit: int) -> tuple[int, int]` that returns status code 200 and remaining quota if count < max_limit, else returns status code 429 and 0.",
            starter_code="def check_quota(count: int, max_limit: int) -> tuple[int, int]:\n    # Return (status_code, remaining)\n    pass",
            solution_code="def check_quota(count: int, max_limit: int) -> tuple[int, int]:\n    if count < max_limit:\n        return (200, max_limit - count - 1)\n    return (429, 0)",
            expected_output="(200, remaining) or (429, 0)"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Which HTTP status code is officially designated for clients that exceed their allocated rate limit quota?",
                options=["429 Too Many Requests", "403 Forbidden", "503 Service Unavailable", "400 Bad Request"],
                correct_answer="429 Too Many Requests",
                explanation="`429 Too Many Requests` indicates the client has been rate-limited / throttled."
            ),
            QuizQuestionBlueprint(
                question="What header should accompany a `429 Too Many Requests` response to tell the client how many seconds to wait before retrying?",
                options=["Retry-After", "Wait-Seconds", "Backoff-Time", "Cool-Down"],
                correct_answer="Retry-After",
                explanation="The `Retry-After` header indicates how many seconds to pause before sending requests again."
            ),
            QuizQuestionBlueprint(
                question="What is a major architectural flaw of the 'Fixed Window Counter' rate limiting algorithm?",
                options=[
                    "It allows traffic bursts up to twice the permitted limit across the boundary edge between two adjacent windows",
                    "It cannot count numbers above 10",
                    "It only works on Mondays",
                    "It requires XML formatting"
                ],
                correct_answer="It allows traffic bursts up to twice the permitted limit across the boundary edge between two adjacent windows",
                explanation="Fixed windows can permit 2x bursts at the boundary edge (end of window 1 + start of window 2)."
            ),
            QuizQuestionBlueprint(
                question="Which in-memory data store is universally favored for managing distributed rate limiting counters across scalable microservice clusters?",
                options=["Redis", "PostgreSQL", "SQLite", "CSV files"],
                correct_answer="Redis",
                explanation="Redis provides ultra-fast in-memory atomic operations and automatic TTL expiration."
            ),
            QuizQuestionBlueprint(
                question="Why is rate-limiting by API Key / User ID superior to rate-limiting strictly by IP address for authenticated APIs?",
                options=[
                    "Multiple users behind corporate NATs or university Wi-Fi share a single public IP address, which could unfairly penalize innocent users",
                    "IP addresses change every millisecond",
                    "API keys take up less memory than IP addresses",
                    "IP addresses are illegal to inspect"
                ],
                correct_answer="Multiple users behind corporate NATs or university Wi-Fi share a single public IP address, which could unfairly penalize innocent users",
                explanation="IP rate limiting can accidentally throttle entire corporate or university networks sharing a single NAT gateway."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 33: API Security Best Practices (OWASP API Top 10)
    # ----------------------------------------------------
    DayBlueprint(
        order=33,
        title="Day 33: API Security Best Practices & OWASP API Top 10",
        concept="Hardening APIs against production exploits: BOLA (Broken Object Level Authorization), Mass Assignment, SQL Injection, XSS, and CSRF.",
        analogy="You locked your front door with a fancy fingerprint lock (Authentication). But once inside, the hotel guest can turn any doorknob down the hallway and open other people's bedrooms (BOLA / Broken Object Level Authorization). API security ensures both the front door and every individual bedroom are secured.",
        theory_sections=[
            {
                "heading": "The OWASP API Security Top 10",
                "body": (
                    "The Open Web Application Security Project (OWASP) maintains a dedicated API Top 10 list. The #1 most critical vulnerability is:\n"
                    "**BOLA (Broken Object Level Authorization)** / IDOR (Insecure Direct Object Reference).\n"
                    "- An attacker logs in as User 5, and then sends `GET /api/v1/invoices/99` or `DELETE /api/v1/users/42`.\n"
                    "- If the API checks *'Is this a logged-in user?'* but forgets to check *'Does this invoice BELONG to this user?'*, the attacker accesses sensitive records!"
                )
            },
            {
                "heading": "Mass Assignment Vulnerabilities",
                "body": (
                    "When frameworks automatically bind incoming JSON payloads directly to database models:\n"
                    "`user.update(request.json)`\n"
                    "If an attacker injects `{\"is_admin\": true}` into their profile update payload, the server accidentally elevates their privileges! "
                    "Always use explicit DTOs/Schemas (Pydantic / Joi) with whitelisted fields."
                )
            },
            {
                "heading": "SQL Injection & XSS in APIs",
                "body": (
                    "- **SQL Injection**: Never concatenate strings into SQL queries (`WHERE id = '\" + id + \"'`). Always use parameterized queries or ORMs.\n"
                    "- **Content-Type Sniffing**: Set `X-Content-Type-Options: nosniff` to prevent browsers from interpreting JSON as executable HTML/JS."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Preventing BOLA (Broken Object Level Authorization)",
                "code": "# ❌ VULNERABLE TO BOLA:\n@app.route('/api/invoices/<id>')\ndef get_invoice(id):\n    # Only checks if logged in, DOES NOT check ownership!\n    return db.query(\"SELECT * FROM invoices WHERE id = ?\", id)\n\n# ✅ SECURED AGAINST BOLA:\n@app.route('/api/invoices/<id>')\ndef get_invoice_safe(id):\n    current_user_id = g.user.id\n    # Explicitly enforce user tenancy:\n    invoice = db.query(\"SELECT * FROM invoices WHERE id = ? AND user_id = ?\", id, current_user_id)\n    if not invoice:\n        return jsonify({'error': 'Invoice not found'}), 404\n    return jsonify(invoice)",
                "explanation": "Always scope database queries to the authenticated tenant."
            },
            {
                "title": "Preventing Mass Assignment via Pydantic Whitelisting",
                "code": "from pydantic import BaseModel\n\n# ❌ Bad: blindly saving request.json to DB allows setting is_admin=True\n\n# ✅ Safe: Explicit DTO only permits updating name and bio:\nclass UserProfileUpdate(BaseModel):\n    name: str | None = None\n    bio: str | None = None\n    # is_admin and role are strictly excluded from update schema!",
                "explanation": "Input sanitization and explicit field whitelisting."
            },
            {
                "title": "Parameterized Queries Preventing SQL Injection",
                "code": "# ❌ DANGEROUS SQL INJECTION:\n# cursor.execute(f\"SELECT * FROM users WHERE email = '{user_input}'\")\n\n# ✅ SAFE PARAMETERIZED QUERY (Database driver escapes parameters):\ncursor.execute(\"SELECT * FROM users WHERE email = %s\", (user_input,))",
                "explanation": "Never concatenate raw user input into SQL strings."
            },
            {
                "title": "Security Headers Middleware (Helmet)",
                "code": "// In Express.js, use Helmet to set standard security headers:\nconst helmet = require('helmet');\napp.use(helmet());\n// Sets: X-Content-Type-Options, Strict-Transport-Security, X-Frame-Options",
                "explanation": "Automated security headers injection."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Secure BOLA Vulnerability in Query",
            description="Write a function `fetch_order(order_id: int, user_id: int, db_orders: list) -> dict | None` that returns the order matching `order_id` ONLY if `order['user_id'] == user_id`. Otherwise return None.",
            starter_code="def fetch_order(order_id: int, user_id: int, db_orders: list) -> dict | None:\n    # Implement secure query check\n    pass",
            solution_code="def fetch_order(order_id: int, user_id: int, db_orders: list) -> dict | None:\n    for order in db_orders:\n        if order['id'] == order_id and order['user_id'] == user_id:\n            return order\n    return None",
            expected_output="order if owned by user_id, None otherwise"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is BOLA (Broken Object Level Authorization), the #1 vulnerability on the OWASP API Security Top 10?",
                options=[
                    "When an authenticated user can access, modify, or delete another user's private data simply by guessing or substituting their resource ID in the URL",
                    "When a user forgets their password",
                    "When an API server runs out of disk space",
                    "When a database runs without a password"
                ],
                correct_answer="When an authenticated user can access, modify, or delete another user's private data simply by guessing or substituting their resource ID in the URL",
                explanation="BOLA occurs when code fails to check whether the requesting user owns the targeted object ID."
            ),
            QuizQuestionBlueprint(
                question="What is the 'Mass Assignment' vulnerability in REST APIs?",
                options=[
                    "When a backend blindly binds all fields from a client JSON payload to database models, allowing attackers to inject fields like `\"is_admin\": true`",
                    "When a teacher assigns homework to an entire school",
                    "When multiple servers run the same code",
                    "When an API has more than 10 endpoints"
                ],
                correct_answer="When a backend blindly binds all fields from a client JSON payload to database models, allowing attackers to inject fields like `\"is_admin\": true`",
                explanation="Mass assignment exploits automatic object mapping by injecting privileged attributes."
            ),
            QuizQuestionBlueprint(
                question="What is the primary method to permanently prevent SQL Injection in database queries?",
                options=[
                    "Using parameterized queries (prepared statements) where the database driver separates SQL code from user data",
                    "Deleting all SQL databases and using text files",
                    "Blocking the letters 'S', 'Q', and 'L'",
                    "Making all API endpoints public"
                ],
                correct_answer="Using parameterized queries (prepared statements) where the database driver separates SQL code from user data",
                explanation="Parameterized queries treat user input strictly as literal values, never as executable SQL."
            ),
            QuizQuestionBlueprint(
                question="Why should an API return `404 Not Found` instead of `403 Forbidden` when a user attempts to access an object ID that belongs to someone else?",
                options=[
                    "To prevent Resource Enumeration: returning 403 confirms the resource exists, whereas 404 hides whether the ID exists at all",
                    "Because 404 runs faster than 403",
                    "Because 403 is an invalid code",
                    "To save server memory"
                ],
                correct_answer="To prevent Resource Enumeration: returning 403 confirms the resource exists, whereas 404 hides whether the ID exists at all",
                explanation="Returning 404 prevents attackers from probing the existence of private ID values."
            ),
            QuizQuestionBlueprint(
                question="What does the `X-Content-Type-Options: nosniff` header do?",
                options=[
                    "Prevents browsers from MIME-sniffing a response away from the declared Content-Type, mitigating script injection attacks",
                    "Speeds up network downloads",
                    "Encodes images with compression",
                    "Prevents users from smelling computers"
                ],
                correct_answer="Prevents browsers from MIME-sniffing a response away from the declared Content-Type, mitigating script injection attacks",
                explanation="`nosniff` forces browsers to honor the declared Content-Type."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 34 (Project): Secure API Gateway Authentication & JWT Verification Middleware
    # ----------------------------------------------------
    DayBlueprint(
        order=34,
        title="Day 34 (Project): Secure API Gateway Authentication & JWT Middleware Lab",
        concept="Milestone Security Lab: Building an end-to-end authentication gatekeeper in Python Flask/FastAPI with JWT verification, role-based access control (RBAC), and rate limiting.",
        analogy="Today you are building the security gatehouse for an international embassy. Anyone without an authentic diplomatic passport (JWT) is stopped at the gate; diplomats are directed to the ambassador lounge, while maintenance staff are restricted to the basement (RBAC).",
        theory_sections=[
            {
                "heading": "Lab Architecture",
                "body": (
                    "In this milestone security lab, you will build an API gateway protection layer:\n"
                    "1. `/api/v1/auth/login`: Accepts credentials, verifies password, and issues signed HS256 JWT.\n"
                    "2. `jwt_required` decorator: Intercepts `Authorization: Bearer <token>`, validates signature and expiration.\n"
                    "3. `roles_required(['ADMIN'])`: Enforces Role-Based Access Control (RBAC).\n"
                    "4. In-memory sliding window rate limiter."
                )
            },
            {
                "heading": "Security Constraints Enforced",
                "body": (
                    "- Tokens expire after 30 minutes.\n"
                    "- Invalid or expired tokens return 401 Unauthorized.\n"
                    "- Valid users attempting admin actions return 403 Forbidden.\n"
                    "- Constant-time password hashing comparison."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Complete Authentication and RBAC Middleware Implementation",
                "code": "from flask import Flask, request, jsonify\nfrom functools import wraps\nimport jwt, time\n\napp = Flask(__name__)\nSECRET_KEY = \"embassy_security_secret_2026\"\n\n# Custom JWT Verification Decorator\ndef token_required(f):\n    @wraps(f)\n    def decorated(*args, **kwargs):\n        auth_header = request.headers.get('Authorization')\n        if not auth_header or not auth_header.startswith('Bearer '):\n            return jsonify({'error': 'Unauthorized', 'detail': 'Bearer token required'}), 401\n        token = auth_header.split(' ')[1]\n        try:\n            payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])\n            request.user = payload\n        except jwt.ExpiredSignatureError:\n            return jsonify({'error': 'Unauthorized', 'detail': 'Token expired'}), 401\n        except jwt.InvalidTokenError:\n            return jsonify({'error': 'Unauthorized', 'detail': 'Invalid token signature'}), 401\n        return f(*args, **kwargs)\n    return decorated\n\n# RBAC Role Checker\ndef roles_required(allowed_roles):\n    def decorator(f):\n        @wraps(f)\n        def decorated(*args, **kwargs):\n            user_role = getattr(request, 'user', {}).get('role')\n            if user_role not in allowed_roles:\n                return jsonify({'error': 'Forbidden', 'detail': 'Insufficient permissions'}), 403\n            return f(*args, **kwargs)\n        return decorated\n    return decorator",
                "explanation": "Production JWT validation and Role-Based Access Control decorators."
            },
            {
                "title": "Login and Protected Route Endpoints",
                "code": "@app.route('/api/v1/auth/login', methods=['POST'])\ndef login():\n    body = request.json or {}\n    # In production: verify hashed password from DB\n    if body.get('username') == 'alice' and body.get('password') == 'pass123':\n        token = jwt.encode({\n            'sub': 'usr-42',\n            'username': 'alice',\n            'role': 'ADMIN',\n            'exp': int(time.time()) + 1800\n        }, SECRET_KEY, algorithm='HS256')\n        return jsonify({'access_token': token, 'token_type': 'Bearer'}), 200\n    return jsonify({'error': 'Invalid credentials'}), 401\n\n@app.route('/api/v1/admin/vault', methods=['GET'])\n@token_required\n@roles_required(['ADMIN'])\ndef access_vault():\n    return jsonify({'vault_code': 'SECRET-9988-ACCESS-GRANTED'})\n\n@app.route('/api/v1/public/ping')\ndef ping():\n    return jsonify({'status': 'alive'})",
                "explanation": "Protected and public endpoints demonstrating full security chain."
            },
            {
                "title": "Verifying Security Flow via Terminal",
                "code": "# 1. Call protected route without token -> 401 Unauthorized\ncurl http://localhost:5000/api/v1/admin/vault -i\n\n# 2. Login to get token:\nTOKEN=$(curl -s -X POST http://localhost:5000/api/v1/auth/login \\\n  -H \"Content-Type: application/json\" \\\n  -d '{\"username\": \"alice\", \"password\": \"pass123\"}' | jq -r .access_token)\n\n# 3. Call protected route with token -> 200 OK + Secret!\ncurl http://localhost:5000/api/v1/admin/vault -H \"Authorization: Bearer $TOKEN\"",
                "explanation": "Terminal test script verifying security lifecycle."
            },
            {
                "title": "Expected Verification Output",
                "code": "# Test 1: No Header -> HTTP/1.1 401 Unauthorized\n# Test 2: Login -> 200 OK (access_token received)\n# Test 3: Authenticated Request -> HTTP/1.1 200 OK\n# Payload: {\"vault_code\": \"SECRET-9988-ACCESS-GRANTED\"}",
                "explanation": "Expected verification results."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Build RBAC Guard Decorator",
            description="Write a Python decorator `require_admin(func)` that checks if `request.user['role'] == 'ADMIN'`. If so, execute `func()`; else return `({'error': 'Forbidden'}, 403)`.",
            starter_code="from functools import wraps\n# Implement require_admin\n",
            solution_code="from functools import wraps\ndef require_admin(func):\n    @wraps(func)\n    def wrapper(*args, **kwargs):\n        user = getattr(request, 'user', {})\n        if user.get('role') != 'ADMIN':\n            return {'error': 'Forbidden'}, 403\n        return func(*args, **kwargs)\n    return wrapper",
            expected_output="Executes function if role is ADMIN, returns 403 otherwise"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="In our Security Gateway project, what status code is returned if a user presents an expired JWT token?",
                options=["401 Unauthorized", "403 Forbidden", "404 Not Found", "500 Server Error"],
                correct_answer="401 Unauthorized",
                explanation="An expired token is an invalid credential, resulting in 401 Unauthorized."
            ),
            QuizQuestionBlueprint(
                question="What status code is returned when a valid, authenticated user with role `MEMBER` tries to access an endpoint decorated with `@roles_required(['ADMIN'])`?",
                options=["403 Forbidden", "401 Unauthorized", "400 Bad Request", "405 Method Not Allowed"],
                correct_answer="403 Forbidden",
                explanation="The user is authenticated (not 401), but lacks the necessary permission (403 Forbidden)."
            ),
            QuizQuestionBlueprint(
                question="Why should JWT signing secrets be loaded from environment variables rather than hardcoded in source code?",
                options=[
                    "Hardcoded secrets committed to version control repositories allow anyone reading the codebase to forge administrative tokens",
                    "Environment variables run 10x faster",
                    "Python cannot read strings in code",
                    "Hardcoded keys crash Git"
                ],
                correct_answer="Hardcoded secrets committed to version control repositories allow anyone reading the codebase to forge administrative tokens",
                explanation="Leaked signing keys allow attackers to forge tokens with arbitrary roles."
            ),
            QuizQuestionBlueprint(
                question="What does the `@wraps(f)` decorator from Python's `functools` module do when writing API middleware?",
                options=[
                    "It preserves the original function's name and docstring, preventing Flask route registration collisions",
                    "It encrypts the function",
                    "It converts the function to JavaScript",
                    "It automatically creates a database"
                ],
                correct_answer="It preserves the original function's name and docstring, preventing Flask route registration collisions",
                explanation="`@wraps(f)` preserves endpoint names, preventing route overwrite errors in web frameworks."
            ),
            QuizQuestionBlueprint(
                question="What is the recommended token lifespan (TTL) for an API Access Token in a secure OAuth/JWT architecture?",
                options=[
                    "Short-lived (15 to 60 minutes), paired with a revocable Refresh Token",
                    "10 years",
                    "Exactly 1 millisecond",
                    "Tokens should never expire"
                ],
                correct_answer="Short-lived (15 to 60 minutes), paired with a revocable Refresh Token",
                explanation="Short access token lifespans minimize exposure if a token is intercepted."
            )
        ],
        is_project_day=True,
        project_name="Secure API Gateway Authentication & JWT Verification Middleware"
    ),

    # ----------------------------------------------------
    # Day 35: API Testing Tools (Postman, Insomnia, cURL)
    # ----------------------------------------------------
    DayBlueprint(
        order=35,
        title="Day 35: API Testing Tools (Postman, Insomnia, and cURL CLI Mastery)",
        concept="Mastering developer tooling for API exploration and automated contract verification: Postman environments and collections, Insomnia, and expert cURL command-line mastery.",
        analogy="You are an audio sound engineer. You don't test your speakers by playing an entire album to an arena; you use a frequency generator and an oscilloscope (cURL and Postman) to test exact frequencies, measure sound levels (headers and status codes), and isolate problems.",
        theory_sections=[
            {
                "heading": "The Developer's API Toolkit",
                "body": (
                    "Before writing frontend client code, developers verify backend endpoints using dedicated testing tools:\n"
                    "1. **cURL**: The universal command-line data transfer tool available on every server, terminal, and CI pipeline.\n"
                    "2. **Postman**: The industry-standard GUI platform for API development, environments, automated collection tests, and mock servers.\n"
                    "3. **Insomnia**: A lightweight, developer-focused, open-source alternative to Postman known for fast startup and clean design."
                )
            },
            {
                "heading": "Postman Environments and Variables",
                "body": (
                    "Hardcoding `https://staging-api.com` in 50 requests is painful. "
                    "Postman **Environments** let you define variables like `{{base_url}}` and `{{auth_token}}`. "
                    "You can write Postman Tests in JavaScript to automatically save the JWT token from `/login` into an environment variable!"
                )
            },
            {
                "heading": "The Essential cURL Flags",
                "body": (
                    "- `-X <METHOD>`: Specify HTTP method (`GET`, `POST`, `DELETE`).\n"
                    "- `-H \"Header: Value\"`: Pass custom request headers.\n"
                    "- `-d '{\"key\": \"val\"}'`: Pass request body payload.\n"
                    "- `-i`: Include HTTP response headers in output.\n"
                    "- `-s`: Silent mode (hide progress meter).\n"
                    "- `-L`: Follow 3xx redirects automatically."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Mastering cURL Commands",
                "code": "# 1. Simple GET request with verbose header logging:\ncurl -v https://api.example.com/v1/users\n\n# 2. POST JSON payload with Bearer authentication:\ncurl -X POST https://api.example.com/v1/users \\\n  -H \"Content-Type: application/json\" \\\n  -H \"Authorization: Bearer eyJhbGci...\" \\\n  -d '{\"name\": \"Alice\", \"role\": \"Lead\"}' -i\n\n# 3. Download file and follow redirects (-L -o):\ncurl -L -o download.zip https://api.example.com/export",
                "explanation": "Essential cURL commands for daily API development."
            },
            {
                "title": "Postman Automated Test Script in JavaScript",
                "code": "// Inside Postman 'Scripts' -> 'Post-response' tab:\npm.test(\"Status code is 201 Created\", function () {\n    pm.response.to.have.status(201);\n});\n\npm.test(\"Response time is less than 200ms\", function () {\n    pm.expect(pm.response.responseTime).to.be.below(200);\n});\n\n// Automatically save JWT token for subsequent requests:\nconst jsonData = pm.response.json();\npm.environment.set(\"jwt_token\", jsonData.access_token);",
                "explanation": "Postman test script asserting status and saving token variable."
            },
            {
                "title": "Exporting and Running Postman Collections in CI (Newman)",
                "code": "# Run full Postman automated test collection in terminal or GitHub Actions CI:\nnpm install -g newman\n\nnewman run my_api_collection.json -e staging_environment.json",
                "explanation": "Newman CLI executing Postman collections headlessly in CI."
            },
            {
                "title": "cURL Timing and Latency Profiling",
                "code": "# Profile exact network latency breakdown with cURL:\ncurl -w \"DNS: %{time_namelookup}s | Connect: %{time_connect}s | TTFB: %{time_starttransfer}s | Total: %{time_total}s\\n\" \\\n  -o /dev/null -s https://api.github.com",
                "explanation": "Measures DNS lookup, TCP connect, Time-To-First-Byte, and total latency."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Formulate cURL POST Command",
            description="Write a complete single-line cURL command to send a `POST` request to `https://api.dev.io/login` with header `Content-Type: application/json` and data `'{\"user\": \"admin\"}'`.",
            starter_code="# Write cURL command\n",
            solution_code="curl -X POST https://api.dev.io/login -H \"Content-Type: application/json\" -d '{\"user\": \"admin\"}'",
            expected_output="curl -X POST https://api.dev.io/login -H \"Content-Type: application/json\" -d '{\"user\": \"admin\"}'"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Which flag passed to `curl` specifies custom HTTP request headers (like `Authorization` or `Content-Type`)?",
                options=["-H", "-X", "-d", "-u"],
                correct_answer="-H",
                explanation="`-H` (or `--header`) adds a custom header to the request."
            ),
            QuizQuestionBlueprint(
                question="What is Newman in the Postman API development ecosystem?",
                options=[
                    "A command-line collection runner that allows executing Postman test suites in terminal and CI/CD automation pipelines",
                    "A graphical text editor",
                    "A database server",
                    "A replacement for Git"
                ],
                correct_answer="A command-line collection runner that allows executing Postman test suites in terminal and CI/CD automation pipelines",
                explanation="Newman is Postman's CLI runner used for headless test execution in CI/CD."
            ),
            QuizQuestionBlueprint(
                question="Which cURL flag ensures that the client automatically follows HTTP 3xx redirection responses to the new destination?",
                options=["-L (or --location)", "-R", "-f", "-F"],
                correct_answer="-L (or --location)",
                explanation="`-L` directs cURL to follow any `Location` redirect headers."
            ),
            QuizQuestionBlueprint(
                question="Why are Postman Environments valuable when testing APIs across different development stages?",
                options=[
                    "They allow switching base URLs (e.g. `{{base_url}}`) and auth tokens between Localhost, Staging, and Production without editing individual requests",
                    "They simulate weather environments",
                    "They speed up computer fans",
                    "They encrypt your home network"
                ],
                correct_answer="They allow switching base URLs (e.g. `{{base_url}}`) and auth tokens between Localhost, Staging, and Production without editing individual requests",
                explanation="Environments decouple request configurations from environment-specific hostnames and tokens."
            ),
            QuizQuestionBlueprint(
                question="What does the `-i` flag do in a cURL command?",
                options=[
                    "Includes the HTTP response headers in the terminal output along with the body",
                    "Enables interactive mode",
                    "Ignores SSL certificates",
                    "Inverts the colors of the terminal"
                ],
                correct_answer="Includes the HTTP response headers in the terminal output along with the body",
                explanation="`-i` (or `--include`) prints response headers followed by the payload."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 36: HTTP Clients in Code (Fetch, Axios, Python Requests)
    # ----------------------------------------------------
    DayBlueprint(
        order=36,
        title="Day 36: HTTP Clients in Code (Fetch API, Axios, and Python Requests)",
        concept="Integrating backend APIs across programming languages: comparing browser Fetch API, Axios (interceptors, auto-JSON), Python Requests, and TCP connection pooling.",
        analogy="You can send a parcel through the postal service using a bicycle messenger, a freight truck, or an express courier service. In code, whether you use native `fetch()`, `axios`, or Python `requests`, they all package your data into the exact same standardized HTTP envelope.",
        theory_sections=[
            {
                "heading": "The Role of HTTP Client Libraries",
                "body": (
                    "While cURL is great for terminal testing, software applications consume APIs programmatically through HTTP client libraries. "
                    "Different libraries offer different levels of abstraction regarding JSON serialization, error handling, and connection pooling."
                )
            },
            {
                "heading": "Native `fetch()` vs `Axios` in JavaScript",
                "body": (
                    "1. **Browser `fetch()` (Native)**:\n"
                    "   - Built into modern browsers and Node.js 18+.\n"
                    "   - Gotcha: `fetch()` **does NOT reject the Promise on HTTP 4xx or 5xx errors!** You must manually check `if (!response.ok)`!\n"
                    "   - Requires two steps to get JSON: `const res = await fetch(); const data = await res.json();`.\n"
                    "2. **Axios**:\n"
                    "   - Automatically parses JSON responses.\n"
                    "   - Automatically throws an error on 4xx/5xx responses.\n"
                    "   - Features **Interceptors** (pre-request token injection and global error handling)."
                )
            },
            {
                "heading": "Python `requests` and Session Connection Pooling",
                "body": (
                    "In Python, the `requests` library is the gold standard. "
                    "Using `requests.Session()` reuses underlying TCP socket connections (`keep-alive`), "
                    "cutting latency by up to 60% by eliminating repeated TCP/TLS handshakes!"
                )
            }
        ],
        code_snippets=[
            {
                "title": "Consuming API via Native JavaScript Fetch",
                "code": "// Native Fetch pattern:\nasync function getUser(userId) {\n    const response = await fetch(`https://api.example.com/users/${userId}`, {\n        headers: { 'Accept': 'application/json' }\n    });\n    \n    // CRITICAL: Fetch does NOT throw on 404 or 500!\n    if (!response.ok) {\n        throw new Error(`HTTP Error ${response.status}: ${response.statusText}`);\n    }\n    \n    const data = await response.json();\n    return data;\n}",
                "explanation": "Native fetch error handling pattern."
            },
            {
                "title": "Axios with Request and Response Interceptors",
                "code": "import axios from 'axios';\n\nconst apiClient = axios.create({\n    baseURL: 'https://api.example.com/v1',\n    timeout: 5000\n});\n\n// Request Interceptor: Automatically attach Bearer token to EVERY outgoing request\napiClient.interceptors.request.use(config => {\n    const token = localStorage.getItem('access_token');\n    if (token) {\n        config.headers.Authorization = `Bearer ${token}`;\n    }\n    return config;\n});\n\n// Response Interceptor: Global 401 Unauthorized handler\napiClient.interceptors.response.use(\n    response => response.data, // Automatically unwraps .data\n    error => {\n        if (error.response?.status === 401) {\n            window.location.href = '/login'; // Auto-logout\n        }\n        return Promise.reject(error);\n    }\n);",
                "explanation": "Axios instance with global token injection and auto-logout interceptor."
            },
            {
                "title": "Python Requests with Persistent Session Pooling",
                "code": "import requests\n\n# Creating a Session reuses the TCP connection across multiple requests:\nsession = requests.Session()\nsession.headers.update({'Authorization': 'Bearer token_abc123'})\n\n# Fast execution: eliminates redundant TCP/TLS handshakes\nres1 = session.get('https://api.example.com/v1/profile')\nres2 = session.get('https://api.example.com/v1/settings')\n\nprint(res1.status_code, res2.status_code)",
                "explanation": "Session connection pooling drastically accelerates multi-request workflows."
            },
            {
                "title": "Feature Comparison Table",
                "code": "# Feature             | Native fetch() | Axios          | Python requests\n# --------------------+----------------+----------------+----------------\n# Environment         | Browser/NodeJS | Browser/NodeJS | Python\n# Throws on 4xx/5xx   | NO (Manual ok) | YES            | NO (Use raise_for_status)\n# Auto JSON Parse     | NO (res.json())| YES (res.data) | NO (res.json())\n# Interceptors        | NO             | YES            | NO (Custom Adapter)",
                "explanation": "Comparison of HTTP client mechanics."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Implement Python Safe Request with raise_for_status",
            description="Write a Python function `safe_fetch_json(url: str) -> dict | None` using `requests.get` and `res.raise_for_status()`. Catch `requests.RequestException` and return None on any failure.",
            starter_code="import requests\ndef safe_fetch_json(url: str) -> dict | None:\n    # Implement safe request\n    pass",
            solution_code="import requests\ndef safe_fetch_json(url: str) -> dict | None:\n    try:\n        res = requests.get(url, timeout=5)\n        res.raise_for_status()\n        return res.json()\n    except requests.RequestException:\n        return None",
            expected_output="JSON dict on success, None on HTTP failure"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is a major trap developers encounter when using the browser's native `fetch()` API?",
                options=[
                    "`fetch()` does NOT reject the Promise on HTTP 4xx or 5xx errors; developers must manually verify `response.ok`",
                    "`fetch()` cannot send JSON",
                    "`fetch()` only works on Google Chrome",
                    "`fetch()` requires a paid subscription"
                ],
                correct_answer="`fetch()` does NOT reject the Promise on HTTP 4xx or 5xx errors; developers must manually verify `response.ok`",
                explanation="Native `fetch()` only rejects on network failures, not on HTTP error status codes like 404 or 500."
            ),
            QuizQuestionBlueprint(
                question="What feature of Axios allows developers to automatically attach an Authorization header to every outgoing request without duplicating code?",
                options=["Request Interceptors", "CSS Stylesheets", "Database triggers", "Service Workers"],
                correct_answer="Request Interceptors",
                explanation="Axios interceptors intercept and transform requests before they are dispatched."
            ),
            QuizQuestionBlueprint(
                question="Why is using `requests.Session()` in Python drastically faster than calling `requests.get()` repeatedly in a loop?",
                options=[
                    "`requests.Session()` reuses the underlying TCP socket connection (HTTP Keep-Alive), eliminating repeated TCP and TLS handshakes",
                    "It bypasses internet security",
                    "It runs Python code in C++",
                    "It downloads data before you ask for it"
                ],
                correct_answer="`requests.Session()` reuses the underlying TCP socket connection (HTTP Keep-Alive), eliminating repeated TCP and TLS handshakes",
                explanation="Connection pooling avoids the overhead of establishing new TCP and TLS handshakes for each request."
            ),
            QuizQuestionBlueprint(
                question="Which method in Python's `requests` library automatically raises an HTTPError if the response status code was 4xx or 5xx?",
                options=["response.raise_for_status()", "response.verify_success()", "response.throw_if_error()", "response.check()"],
                correct_answer="response.raise_for_status()",
                explanation="`raise_for_status()` raises an HTTPError for non-2xx responses."
            ),
            QuizQuestionBlueprint(
                question="Where does Axios store the automatically parsed JSON response payload?",
                options=["In `response.data`", "In `response.json()`", "In `response.body`", "In `response.payload`"],
                correct_answer="In `response.data`",
                explanation="Axios automatically unpacks and parses the body into the `.data` property."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 37: Handling API Responses (Parsing & DTOs)
    # ----------------------------------------------------
    DayBlueprint(
        order=37,
        title="Day 37: Handling API Responses (Parsing, Serialization & DTOs)",
        concept="Protecting codebases from brittle API schemas: robust serialization, deserialization, type safety with DTOs (Data Transfer Objects), and Pydantic validation.",
        analogy="Raw API data is like raw uninspected lumber delivered to a construction site: it could be warped, full of termites, or have hidden nails. A DTO (Data Transfer Object) is the quality inspector who tests the wood, smooths the edges, and guarantees it matches the exact specifications before you build a house with it.",
        theory_sections=[
            {
                "heading": "The Danger of Loose Dictionaries",
                "body": (
                    "In JavaScript or Python, it is tempting to consume API responses as raw loose dictionaries: `user['profile']['address']['zip']`. "
                    "If the backend renames `zip` to `postal_code` or sends `null` for `address`, your application crashes with an unhandled "
                    "`TypeError: cannot read property of undefined`! "
                    "Production applications always deserialize external responses into structured **DTOs (Data Transfer Objects)**."
                )
            },
            {
                "heading": "What is a DTO (Data Transfer Object)?",
                "body": (
                    "A DTO is an object whose sole purpose is to encapsulate data for transmission and enforce type contracts. "
                    "In Python, **Pydantic** or `dataclasses` are the standard; in TypeScript, **Zod** or interface types guarantee runtime schema validation."
                )
            },
            {
                "heading": "Handling Inconsistent API Types",
                "body": (
                    "External APIs frequently return inconsistent types (e.g. returning `\"price\": \"49.99\"` as a string instead of a float, "
                    "or `\"status\": 1` instead of `\"ACTIVE\"`). "
                    "DTO validators automatically coerce and normalize these types at the boundary of your application."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Robust Response Validation with Pydantic in Python",
                "code": "from pydantic import BaseModel, Field, HttpUrl\nfrom datetime import datetime\n\n# Define the strict contract expected from external API:\nclass UserDTO(BaseModel):\n    id: int\n    username: str\n    email: str\n    is_verified: bool = False\n    website: HttpUrl | None = None\n    created_at: datetime\n\n# Simulated raw external API response with string dates and numbers:\nraw_api_response = {\n    \"id\": \"42\",  # Note: string number!\n    \"username\": \"alice_dev\",\n    \"email\": \"alice@dev.io\",\n    \"created_at\": \"2026-09-30T12:00:00Z\"\n}\n\n# Pydantic coerces types and validates schema automatically:\nuser = UserDTO.model_validate(raw_api_response)\nprint(f\"Parsed User ID: {user.id} (Type: {type(user.id)})\")\nprint(f\"Parsed Date: {user.created_at.year}\")",
                "explanation": "Pydantic guarantees runtime type safety and automatic coercion."
            },
            {
                "title": "Runtime Schema Validation in TypeScript with Zod",
                "code": "import { z } from 'zod';\n\n// Define runtime schema contract:\nconst ProductSchema = z.object({\n    id: z.number(),\n    title: z.string(),\n    price: z.number().positive(),\n    tags: z.array(z.string()).default([])\n});\n\ntype Product = z.infer<typeof ProductSchema>;\n\nasync function fetchProduct(id: number): Promise<Product> {\n    const res = await fetch(`https://api.shop.com/products/${id}`);\n    const rawJson = await res.json();\n    \n    // Throws clear validation error if API sent invalid schema:\n    return ProductSchema.parse(rawJson);\n}",
                "explanation": "Zod ensures runtime data integrity matching TypeScript types."
            },
            {
                "title": "Defensive Navigation / Optional Chaining",
                "code": "// When inspecting unvalidated JSON, always use optional chaining (?.) and nullish coalescing (??):\nconst city = response?.data?.user?.address?.city ?? 'Unknown City';\n\n# Python equivalent using .get():\ncity = response.get('data', {}).get('user', {}).get('address', {}).get('city', 'Unknown City')",
                "explanation": "Prevents catastrophic runtime crashes from missing nested keys."
            },
            {
                "title": "DTO Boundary Architecture",
                "code": "# [External Untrusted API] ---> (Raw JSON String) \n#                                    |\n#                                    v\n#                         [ DTO Validation Layer ]\n#                                    |\n#                                    v\n# [Your Clean Business Logic] <--- (Validated Typed Object)",
                "explanation": "DTOs insulate application core from external schema chaos."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Parse Response with Pydantic",
            description="Define a Pydantic model `Item(BaseModel)` with required `id: int` and `title: str`. Parse dict `{'id': '10', 'title': 'Test'}` and return the integer `id`.",
            starter_code="from pydantic import BaseModel\n\n# Define Item and parse dict\n",
            solution_code="from pydantic import BaseModel\n\nclass Item(BaseModel):\n    id: int\n    title: str\n\nitem = Item.model_validate({'id': '10', 'title': 'Test'})\nresult = item.id",
            expected_output="10 (as integer)"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the primary architectural purpose of a DTO (Data Transfer Object) when consuming third-party APIs?",
                options=[
                    "To validate, coerce, and guarantee type safety of external payloads at the boundary, insulating internal business logic from third-party schema changes",
                    "To convert code to machine language",
                    "To encrypt the database",
                    "To make network requests faster"
                ],
                correct_answer="To validate, coerce, and guarantee type safety of external payloads at the boundary, insulating internal business logic from third-party schema changes",
                explanation="DTOs enforce schema contracts and prevent nested runtime crashes."
            ),
            QuizQuestionBlueprint(
                question="What happens in Python when code accesses `data['user']['profile']['email']` and the `profile` key is missing in the JSON response?",
                options=[
                    "It raises a `KeyError` exception and crashes the application unless explicitly handled",
                    "It returns `None` silently",
                    "It creates an empty profile automatically",
                    "It retries the API request"
                ],
                correct_answer="It raises a `KeyError` exception and crashes the application unless explicitly handled",
                explanation="Direct dictionary bracket indexing raises a KeyError if a key is absent."
            ),
            QuizQuestionBlueprint(
                question="Which popular Python library is standard for data modeling and parsing using Python type annotations?",
                options=["Pydantic", "NumPy", "Tkinter", "Matplotlib"],
                correct_answer="Pydantic",
                explanation="Pydantic is the leading data validation and parsing library in Python."
            ),
            QuizQuestionBlueprint(
                question="In JavaScript/TypeScript, what operator prevents crashes when accessing deeply nested properties that might be null or undefined (e.g. `res?.user?.address`)?",
                options=["Optional Chaining operator (`?.`)", "Double equal (`==`)", "Ternary operator (`?:`)", "Spread operator (`...`)"],
                correct_answer="Optional Chaining operator (`?.`)",
                explanation="Optional chaining (`?.`) short-circuits to `undefined` instead of throwing an error."
            ),
            QuizQuestionBlueprint(
                question="What is the term for converting an incoming JSON string into an in-memory typed object?",
                options=["Deserialization (or Unmarshaling)", "Compilation", "Compression", "Interpolation"],
                correct_answer="Deserialization (or Unmarshaling)",
                explanation="Deserialization transforms text/byte streams into in-memory program objects."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 38: Robust Error Handling (Try/Catch & Status Checks)
    # ----------------------------------------------------
    DayBlueprint(
        order=38,
        title="Day 38: Robust Error Handling in API Integrations",
        concept="Engineering fault-tolerant API clients: catching network timeouts, handling HTTP error status codes, parsing non-JSON error payloads, and circuit breaker basics.",
        analogy="Driving a car with defensive driving: You don't just assume every other car will obey green lights. You wear a seatbelt, check your blind spots, and watch for unexpected road hazards. Defensive API integration anticipates server crashes, timeouts, and corrupted data.",
        theory_sections=[
            {
                "heading": "The 4 Classes of API Failures",
                "body": (
                    "When calling an external API, failure can occur at four distinct layers:\n"
                    "1. **Transport / Network Failure**: DNS lookup fails, internet connection dropped, TCP socket reset (`ConnectionError`).\n"
                    "2. **Timeout Failure**: Server accepted connection but took too long to send data (`Timeout`). Always configure explicit timeouts!\n"
                    "3. **HTTP Protocol Errors**: Server returned `4xx` (Client error) or `5xx` (Server crash).\n"
                    "4. **Payload Parsing Error**: Server returned HTML error page (e.g. Cloudflare 502 page) instead of expected JSON (`JSONDecodeError`)."
                )
            },
            {
                "heading": "The Golden Rule: ALWAYS Set Explicit Timeouts",
                "body": (
                    "By default, many HTTP client libraries (including Python `requests`) **have NO timeout**! "
                    "If an external server hangs, your application thread will hang **forever**, exhausting thread pools and crashing your entire system. "
                    "Never write `requests.get(url)` without `timeout=(connect_timeout, read_timeout)`."
                )
            },
            {
                "heading": "Parsing Non-JSON Error Responses",
                "body": (
                    "When an API gateway or reverse proxy crashes (502/504), it often returns a raw HTML page: `'<html><head><title>502 Bad Gateway</title>...'`. "
                    "Blindly calling `response.json()` will raise a fatal `JSONDecodeError`. "
                    "Always check status codes and inspect headers before parsing."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Bulletproof Python API Client Pattern",
                "code": "import requests\nfrom requests.exceptions import Timeout, ConnectionError, HTTPError\n\ndef call_external_api(url, payload):\n    try:\n        # Always set explicit timeout: (connect timeout 3.05s, read timeout 10s)\n        response = requests.post(url, json=payload, timeout=(3.05, 10))\n        \n        # Raises HTTPError for 4xx or 5xx codes:\n        response.raise_for_status()\n        \n        return response.json()\n        \n    except Timeout:\n        print(\"⏳ Request timed out! External server is overloaded.\")\n        return None\n    except ConnectionError:\n        print(\"🔌 Network connection dropped or DNS lookup failed.\")\n        return None\n    except HTTPError as e:\n        # Check if server provided RFC 7807 JSON error or raw text:\n        try:\n            err_data = response.json()\n            print(f\"Server Error [{response.status_code}]: {err_data.get('detail')}\")\n        except Exception:\n            print(f\"Server Error [{response.status_code}]: {response.text[:100]}\")\n        return None\n    except Exception as e:\n        print(f\"Unexpected error: {e}\")\n        return None",
                "explanation": "Comprehensive exception handling covering all failure modes."
            },
            {
                "title": "Handling Errors in JavaScript with Axios",
                "code": "import axios from 'axios';\n\nasync function createOrder(orderData) {\n    try {\n        const response = await axios.post('/api/v1/orders', orderData, {\n            timeout: 5000 // 5s timeout\n        });\n        return response.data;\n    } catch (error) {\n        if (error.response) {\n            // The server responded with status outside 2xx (4xx/5xx)\n            console.error(`Status: ${error.response.status}`, error.response.data);\n        } else if (error.request) {\n            // The request was made but NO response was received (Network / Timeout)\n            console.error('No response received from server. Check network connection.');\n        } else {\n            // Something happened in setting up the request\n            console.error('Request setup error:', error.message);\n        }\n        throw error;\n    }\n}",
                "explanation": "Categorizing Axios errors into response errors, request errors, and setup errors."
            },
            {
                "title": "Circuit Breaker Concept",
                "code": "# [Normal: Closed] --- (5 consecutive failures) ---> [Open: Fast Fail]\n# Client calls API                                    Client skips network calls\n#                                                    immediately returns fallback\n#         ^                                                |\n#         +--- (Test call succeeds) --- [Half-Open] <------+ (After 60s)",
                "explanation": "Circuit breaker design pattern preventing cascading failures."
            },
            {
                "title": "Catching HTML Error Pages Gracefully",
                "code": "def parse_safe_json(response):\n    content_type = response.headers.get('Content-Type', '')\n    if 'application/json' in content_type:\n        return response.json()\n    # Fallback if server sent raw HTML error page:\n    return {'raw_error': response.text[:200]}",
                "explanation": "Inspects Content-Type before attempting JSON parsing."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Implement Timeout Handler in Requests",
            description="Write a Python function `fetch_with_timeout(url: str, sec: int) -> str` that calls `requests.get` with timeout `sec`. Catch `requests.exceptions.Timeout` and return string 'TIMEOUT', or return response text on success.",
            starter_code="import requests\ndef fetch_with_timeout(url: str, sec: int) -> str:\n    # Implement timeout handling\n    pass",
            solution_code="import requests\ndef fetch_with_timeout(url: str, sec: int) -> str:\n    try:\n        return requests.get(url, timeout=sec).text\n    except requests.exceptions.Timeout:\n        return 'TIMEOUT'",
            expected_output="'TIMEOUT' when call times out, text otherwise"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What happens if a developer does NOT specify a timeout parameter in Python's `requests.get(url)` and the external server hangs indefinitely?",
                options=[
                    "The client application thread will block and hang indefinitely, potentially exhausting server worker threads and crashing your system",
                    "Python automatically terminates the request after 3 seconds",
                    "The operating system reboots",
                    "It converts the request to a background thread"
                ],
                correct_answer="The client application thread will block and hang indefinitely, potentially exhausting server worker threads and crashing your system",
                explanation="By default, Python `requests` has no timeout; threads wait indefinitely until the socket times out (often hours)."
            ),
            QuizQuestionBlueprint(
                question="Why can calling `response.json()` fail with a `JSONDecodeError` even when an HTTP request connects successfully?",
                options=[
                    "When an intermediate proxy or server crashes (e.g. Cloudflare 502/504), it often returns an HTML error page instead of valid JSON",
                    "JSON can only be parsed on Mondays",
                    "Because computers cannot read numbers",
                    "Only on Python 2"
                ],
                correct_answer="When an intermediate proxy or server crashes (e.g. Cloudflare 502/504), it often returns an HTML error page instead of valid JSON",
                explanation="Gateway errors frequently return raw HTML error pages that fail JSON parsing."
            ),
            QuizQuestionBlueprint(
                question="What is the purpose of the 'Circuit Breaker' architectural pattern in microservices and API integrations?",
                options=[
                    "To stop sending requests to a failing service after repeated failures (fast-failing immediately) to prevent cascading outages and allow the downstream service to recover",
                    "To cut physical internet wires",
                    "To turn off server power supplies",
                    "To encrypt database passwords"
                ],
                correct_answer="To stop sending requests to a failing service after repeated failures (fast-failing immediately) to prevent cascading outages and allow the downstream service to recover",
                explanation="Circuit breakers trip open when failures exceed thresholds, failing fast without overloading damaged backends."
            ),
            QuizQuestionBlueprint(
                question="In Axios error handling, what condition indicates that the network connection failed and NO response was received from the server?",
                options=["`error.request` exists, but `error.response` is undefined", "`error.response.status === 200`", "`error.code === 0`", "`error.name === 'Success'"],
                correct_answer="`error.request` exists, but `error.response` is undefined",
                explanation="`error.request` with no `error.response` indicates the request was dispatched but no server response arrived."
            ),
            QuizQuestionBlueprint(
                question="When configuring network timeouts, what are the two distinct phases that can be tuned?",
                options=[
                    "Connect Timeout (time to establish TCP connection) and Read Timeout (time waiting for server to send response bytes)",
                    "Morning Timeout and Evening Timeout",
                    "Upload Timeout and Download Timeout",
                    "CPU Timeout and RAM Timeout"
                ],
                correct_answer="Connect Timeout (time to establish TCP connection) and Read Timeout (time waiting for server to send response bytes)",
                explanation="Connect timeout covers TCP/TLS handshake; read timeout covers byte streaming latency."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 39: Asynchronous Programming (Promises & Async/Await)
    # ----------------------------------------------------
    DayBlueprint(
        order=39,
        title="Day 39: Asynchronous Programming (Promises, Async/Await & Concurrent API Calls)",
        concept="Mastering non-blocking asynchronous concurrency: JavaScript Promises, `async/await`, Python `asyncio` and `httpx`, and firing concurrent API requests with `Promise.all`.",
        analogy="Synchronous cooking is waiting for water to boil for 10 minutes doing nothing, then chopping onions for 5 minutes, then cooking. Asynchronous cooking is putting the water on the stove, and while the water heats in the background, you chop the onions. You get twice as much done in the same amount of time.",
        theory_sections=[
            {
                "heading": "Why Asynchronous API Calls?",
                "body": (
                    "Network operations are I/O bound. While your computer waits for a remote server 3,000 miles away to respond (taking 200ms), "
                    "the CPU is sitting idle 99.9% of the time. "
                    "Asynchronous programming releases the execution thread during I/O wait, allowing single-threaded runtimes (like Node.js or Python asyncio) "
                    "to handle thousands of concurrent requests."
                )
            },
            {
                "heading": "Sequential vs Concurrent API Execution",
                "body": (
                    "Suppose you need to fetch User, Orders, and Notifications:\n"
                    "- **Sequential (Slow)**: `await getUser()` (200ms) + `await getOrders()` (200ms) + `await getNotifications()` (200ms) = **600ms total**!\n"
                    "- **Concurrent (`Promise.all` / `asyncio.gather`)**: Fire all 3 requests in parallel! Total time = **200ms** (the slowest single call)."
                )
            },
            {
                "heading": "`Promise.all` vs `Promise.allSettled`",
                "body": (
                    "- `Promise.all`: Fails fast. If any single promise rejects, the entire batch rejects.\n"
                    "- `Promise.allSettled`: Waits for all requests to finish, returning an array of outcomes (fulfilled or rejected) for each."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Concurrent API Calls in JavaScript with Promise.all",
                "code": "async function loadDashboardData(userId) {\n    console.time('DashboardLoad');\n    \n    // Fire all three API calls in parallel:\n    const [user, orders, notifications] = await Promise.all([\n        fetch(`/api/v1/users/${userId}`).then(r => r.json()),\n        fetch(`/api/v1/users/${userId}/orders`).then(r => r.json()),\n        fetch(`/api/v1/users/${userId}/notifications`).then(r => r.json())\n    ]);\n    \n    console.timeEnd('DashboardLoad'); // ~200ms instead of ~600ms!\n    return { user, orders, notifications };\n}",
                "explanation": "Executes 3 independent API requests concurrently."
            },
            {
                "title": "Asynchronous Concurrent API Calls in Python (httpx & asyncio)",
                "code": "import asyncio\nimport httpx\n\nasync function_fetch_all():\n    async with httpx.AsyncClient() as client:\n        # Dispatch concurrent async requests:\n        tasks = [\n            client.get('https://api.github.com/users/octocat'),\n            client.get('https://api.github.com/users/torvalds'),\n            client.get('https://api.github.com/users/gvanrossum')\n        ]\n        responses = await asyncio.gather(*tasks)\n        for r in responses:\n            print(r.status_code, r.json()['name'])\n\n# asyncio.run(function_fetch_all())",
                "explanation": "Using Python's modern httpx async library with asyncio.gather."
            },
            {
                "title": "Graceful Degradation with Promise.allSettled",
                "code": "const results = await Promise.allSettled([\n    fetchUserData(),\n    fetchOptionalWeatherWidget() // Might fail!\n]);\n\nconst user = results[0].status === 'fulfilled' ? results[0].value : null;\nconst weather = results[1].status === 'fulfilled' ? results[1].value : 'Weather unavailable';",
                "explanation": "Prevents non-critical API failure from crashing the entire page."
            },
            {
                "title": "Async/Await Try-Catch Error Flow",
                "code": "async function safeAsyncApi() {\n    try {\n        const res = await fetch('https://api.broken.com');\n        const data = await res.json();\n        return data;\n    } catch (err) {\n        console.error('Handled cleanly in catch block:', err.message);\n        return { fallback: true };\n    }\n}",
                "explanation": "Clean synchronous-looking syntax for async error handling."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Async Function Fetching Multiple URLs in Python",
            description="Write a Python async function `fetch_status_codes(urls: list)` using `httpx.AsyncClient` and `asyncio.gather` that returns a list of integer status codes for the provided URLs.",
            starter_code="import asyncio, httpx\n\nasync def fetch_status_codes(urls: list) -> list:\n    # Implement async gather\n    pass",
            solution_code="import asyncio, httpx\n\nasync def fetch_status_codes(urls: list) -> list:\n    async with httpx.AsyncClient() as client:\n        tasks = [client.get(u) for u in urls]\n        responses = await asyncio.gather(*tasks)\n        return [r.status_code for r in responses]",
            expected_output="[200, 200, ...]"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="If you have 3 independent API calls that each take 200ms to respond, what is the total execution time when firing them concurrently with `Promise.all` vs sequentially with `await`?",
                options=[
                    "~200ms concurrently vs ~600ms sequentially",
                    "~600ms concurrently vs ~200ms sequentially",
                    "Zero milliseconds",
                    "Concurrently takes longer due to CPU throttling"
                ],
                correct_answer="~200ms concurrently vs ~600ms sequentially",
                explanation="Concurrent requests execute in parallel; total latency matches the slowest single request."
            ),
            QuizQuestionBlueprint(
                question="What is the difference between `Promise.all` and `Promise.allSettled` in JavaScript?",
                options=[
                    "`Promise.all` rejects immediately if ANY single promise fails; `Promise.allSettled` waits for all promises to finish regardless of success or failure",
                    "`Promise.allSettled` only works on Android",
                    "`Promise.all` is synchronous; `Promise.allSettled` is asynchronous",
                    "There is no difference"
                ],
                correct_answer="`Promise.all` rejects immediately if ANY single promise fails; `Promise.allSettled` waits for all promises to finish regardless of success or failure",
                explanation="`Promise.allSettled` is resilient: it returns the individual fulfillment/rejection status of every promise."
            ),
            QuizQuestionBlueprint(
                question="Why can single-threaded event-loop runtimes like Node.js handle 10,000 concurrent network API requests without freezing?",
                options=[
                    "Network operations are I/O bound; Node.js offloads socket waiting to the operating system kernel and resumes JavaScript execution only when data arrives",
                    "Node.js uses 10,000 CPU cores",
                    "JavaScript runs in kernel space",
                    "Node.js deletes waiting requests"
                ],
                correct_answer="Network operations are I/O bound; Node.js offloads socket waiting to the operating system kernel and resumes JavaScript execution only when data arrives",
                explanation="Non-blocking event-driven I/O delegates socket waiting to OS polling primitives (epoll/kqueue)."
            ),
            QuizQuestionBlueprint(
                question="Which modern Python HTTP client library natively supports `async/await` syntax alongside synchronous calls?",
                options=["httpx", "urllib", "requests (standard)", "ftplib"],
                correct_answer="httpx",
                explanation="`httpx` provides a full async API compatible with `asyncio`."
            ),
            QuizQuestionBlueprint(
                question="What keyword in modern JavaScript and Python allows writing asynchronous Promise code that looks and reads like clean synchronous code?",
                options=["async / await", "thread / join", "fork / exec", "loop / defer"],
                correct_answer="async / await",
                explanation="`async/await` provides syntactic sugar over Promises/Futures for readable non-blocking code."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 40: Client-Side Pagination & Infinite Scroll Handling
    # ----------------------------------------------------
    DayBlueprint(
        order=40,
        title="Day 40: Client-Side Pagination & Infinite Scroll Handling",
        concept="Engineering seamless consumer-side pagination: managing pagination state in React/Vue/mobile, handling infinite scroll triggers, and caching previous pages.",
        analogy="Reading a long scroll: In traditional pagination, you read page 1, close the book, and open page 2. In infinite scroll, every time your eyes reach the bottom of the parchment, an invisible assistant glues the next 10 feet of parchment onto the bottom so you never stop reading.",
        theory_sections=[
            {
                "heading": "Client-Side Pagination Architectures",
                "body": (
                    "Consuming paginated APIs requires robust state management on the client:\n"
                    "1. **Traditional Numbered Pages** (Tables / Admin Dashboards): State stores `currentPage` and `totalPages`. "
                    "Changing page replaces the current list.\n"
                    "2. **Infinite Scroll / Load More** (Mobile Apps / Feeds): State **appends** new items to the existing array: "
                    "`items = [...prevItems, ...newItems]`. State tracks `nextCursor` or `hasMore` boolean."
                )
            },
            {
                "heading": "Detecting the Scroll Threshold",
                "body": (
                    "In modern web and mobile apps, infinite scroll uses the **Intersection Observer API**. "
                    "A sentinel `<div>` is placed at the bottom of the list. When the sentinel scrolls into the viewport, "
                    "the client automatically triggers the fetch for the next page."
                )
            },
            {
                "heading": "Preventing Concurrent Race Conditions",
                "body": (
                    "If a user scrolls rapidly, the client must prevent firing duplicate requests for the same page. "
                    "Use an `isLoading` lock or abort controller: if `isLoading == true`, ignore subsequent scroll triggers until the active fetch completes."
                )
            }
        ],
        code_snippets=[
            {
                "title": "React Infinite Scroll Hook Pattern",
                "code": "import { useState, useEffect } from 'react';\n\nfunction useInfiniteFeed() {\n    const [posts, setPosts] = useState([]);\n    const [cursor, setCursor] = useState(null);\n    const [hasMore, setHasMore] = useState(true);\n    const [isLoading, setIsLoading] = useState(false);\n\n    const loadMore = async () => {\n        if (isLoading || !hasMore) return; // Prevent duplicate requests\n        setIsLoading(true);\n        \n        try {\n            const url = cursor ? `/api/v1/feed?cursor=${cursor}` : '/api/v1/feed';\n            const res = await fetch(url);\n            const data = await res.json();\n            \n            // Append new items to existing list:\n            setPosts(prev => [...prev, ...data.data]);\n            setCursor(data.next_cursor);\n            setHasMore(Boolean(data.next_cursor));\n        } finally {\n            setIsLoading(false);\n        }\n    };\n\n    return { posts, loadMore, hasMore, isLoading };\n}",
                "explanation": "Custom React hook managing cursor pagination and append state."
            },
            {
                "title": "Intersection Observer Sentinel Trigger",
                "code": "// Set up observer to trigger loadMore when sentinel enters screen:\nconst observer = new IntersectionObserver((entries) => {\n    if (entries[0].isIntersecting && hasMore && !isLoading) {\n        loadMore();\n    }\n}, { threshold: 0.8 });\n\nobserver.observe(document.getElementById('sentinel'));",
                "explanation": "IntersectionObserver triggers fetch automatically upon scrolling."
            },
            {
                "title": "Client Pagination State Model",
                "code": "# Client State Shape:\n# {\n#   items: [Item1, Item2, Item3, ... Item50],\n#   page: 3,\n#   cursor: \"eyJpZCI6NTB9\",\n#   isLoading: false,\n#   hasMore: true,\n#   error: null\n# }",
                "explanation": "Standard reactive state model for infinite lists."
            },
            {
                "title": "Deduplicating Appended Items",
                "code": "# Guard against duplicate items if server data shifted:\ndef append_unique(existing_items, new_items):\n    seen_ids = {item['id'] for item in existing_items}\n    return existing_items + [item for item in new_items if item['id'] not in seen_ids]",
                "explanation": "Deduplication logic preventing duplicate UI keys."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Deduplicate Paginated List Items",
            description="Write a Python function `merge_unique(current: list, incoming: list) -> list` that appends items from `incoming` to `current` by unique 'id' key.",
            starter_code="def merge_unique(current: list, incoming: list) -> list:\n    # Merge unique by id\n    pass",
            solution_code="def merge_unique(current: list, incoming: list) -> list:\n    seen = {item['id'] for item in current}\n    return current + [item for item in incoming if item['id'] not in seen]",
            expected_output="Deduplicated combined list"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Why must an infinite scroll client maintain an `isLoading` lock variable during data fetching?",
                options=[
                    "To prevent rapid scroll events from triggering multiple duplicate requests for the exact same page simultaneously",
                    "To save battery power",
                    "To enable dark mode",
                    "Because browsers crash after 5 requests"
                ],
                correct_answer="To prevent rapid scroll events from triggering multiple duplicate requests for the exact same page simultaneously",
                explanation="An `isLoading` guard prevents race conditions and duplicate fetch calls."
            ),
            QuizQuestionBlueprint(
                question="Which modern browser API allows detecting when a user has scrolled to the bottom of a list without listening to performance-heavy scroll events?",
                options=["Intersection Observer API", "Geolocation API", "Battery API", "Canvas API"],
                correct_answer="Intersection Observer API",
                explanation="The Intersection Observer API asynchronously observes when target elements enter the viewport."
            ),
            QuizQuestionBlueprint(
                question="In client state management for infinite feeds, how are newly fetched page items combined with existing items?",
                options=[
                    "They are appended to the existing array (e.g. `[...prevItems, ...newItems]`)",
                    "They completely overwrite the existing array",
                    "They are saved to a cookie",
                    "They are deleted"
                ],
                correct_answer="They are appended to the existing array (e.g. `[...prevItems, ...newItems]`)",
                explanation="Infinite feeds concatenate new pages onto the existing item array."
            ),
            QuizQuestionBlueprint(
                question="What signal tells the frontend client that it has reached the very last page and should stop attempting to fetch more items?",
                options=[
                    "The server returns `next_cursor: null` or an empty data array `data: []`",
                    "The server closes the user's account",
                    "The phone vibrates",
                    "The browser crashes"
                ],
                correct_answer="The server returns `next_cursor: null` or an empty data array `data: []`",
                explanation="A null cursor or empty collection indicates the end of the dataset."
            ),
            QuizQuestionBlueprint(
                question="What client-side issue occurs if a user navigates away from an infinite scroll page and returns later without state caching?",
                options=[
                    "Scroll restoration fails; the user loses their place and is bounced back to item #1 on page 1",
                    "The browser memory is deleted",
                    "The server permanently locks the user out",
                    "The screen flips upside down"
                ],
                correct_answer="Scroll restoration fails; the user loses their place and is bounced back to item #1 on page 1",
                explanation="Without client state caching, returning users lose their scroll offset."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 41: Retry Mechanisms & Exponential Backoff with Jitter
    # ----------------------------------------------------
    DayBlueprint(
        order=41,
        title="Day 41: Retry Mechanisms & Exponential Backoff with Jitter",
        concept="Engineering resilient distributed API clients: handling transient network blips, exponential backoff formulas, and injecting randomized jitter to prevent the 'Thundering Herd' problem.",
        analogy="You call a friend whose phone is busy. You don't redial every 0.1 seconds (annoying them and jamming the line). You wait 2 seconds, then 4 seconds, then 8 seconds (Exponential Backoff). If 10,000 people all call at once, you also add a random few seconds of delay (Jitter) so everyone doesn't hit the phone line at the exact same millisecond.",
        theory_sections=[
            {
                "heading": "Transient vs Permanent Failures",
                "body": (
                    "In distributed systems, networks are inherently unreliable (micro-disconnections, brief server restarts). "
                    "Retrying is effective for **Transient Failures**:\n"
                    "- `429 Too Many Requests` (Rate limit exceeded)\n"
                    "- `503 Service Unavailable`\n"
                    "- `504 Gateway Timeout`\n"
                    "- Network socket timeouts.\n"
                    "**Never retry Permanent Failures** (e.g. `400 Bad Request`, `401 Unauthorized`, `404 Not Found`)! Retrying a bad password 10 times will never make it succeed."
                )
            },
            {
                "heading": "Exponential Backoff Formula",
                "body": (
                    "Instead of retrying immediately, wait exponentially longer between attempts:\n"
                    "$$\\text{Delay} = \\text{BaseDelay} \\times 2^{\\text{attempt}}$$\n"
                    "- Attempt 1: 1s\n"
                    "- Attempt 2: 2s\n"
                    "- Attempt 3: 4s\n"
                    "- Attempt 4: 8s"
                )
            },
            {
                "heading": "The Thundering Herd Problem & Full Jitter",
                "body": (
                    "If a data center reboots, 100,000 mobile clients disconnect simultaneously. "
                    "If all 100,000 clients retry with pure exponential backoff at exactly 1s, 2s, and 4s, "
                    "they hit the recovering server with synchronized tsunami waves of requests, crashing it again! "
                    "**Jitter adds randomness**: `Delay = random(0, BaseDelay * 2^attempt)`. "
                    "This spreads traffic evenly across the timeline, allowing the server to heal."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Exponential Backoff with Full Jitter in Python",
                "code": "import time\nimport random\nimport requests\n\ndef request_with_backoff(url, max_retries=5, base_delay=1.0, max_delay=32.0):\n    for attempt in range(max_retries):\n        try:\n            response = requests.get(url, timeout=5)\n            # Only retry transient server errors (500, 502, 503, 504, 429):\n            if response.status_code in [429, 500, 502, 503, 504]:\n                raise requests.RequestException(f\"Status {response.status_code}\")\n            return response.json()\n            \n        except requests.RequestException as e:\n            if attempt == max_retries - 1:\n                raise Exception(f\"Max retries reached. Last error: {e}\")\n                \n            # Exponential backoff formula with Full Jitter:\n            calculated_delay = min(max_delay, base_delay * (2 ** attempt))\n            jittered_delay = random.uniform(0, calculated_delay)\n            \n            print(f\"⚠️ Attempt {attempt + 1} failed. Backing off for {jittered_delay:.2f}s...\")\n            time.sleep(jittered_delay)",
                "explanation": "AWS-recommended Full Jitter exponential backoff implementation."
            },
            {
                "title": "Using urllib3 Built-in Retry Adapter",
                "code": "from requests.adapters import HTTPAdapter\nfrom urllib3.util.retry import Retry\nimport requests\n\n# Configure enterprise-grade automatic retries in requests:\nretry_strategy = Retry(\n    total=4,\n    backoff_factor=1.5, # 1.5s, 3s, 6s...\n    status_forcelist=[429, 500, 502, 503, 504],\n    allowed_methods=[\"HEAD\", \"GET\", \"OPTIONS\", \"PUT\", \"DELETE\"] # Avoid retrying unsafe POST!\n)\n\nadapter = HTTPAdapter(max_retries=retry_strategy)\nsession = requests.Session()\nsession.mount(\"https://\", adapter)\n\n# Automatically retries transient failures with backoff:\nres = session.get('https://api.service.com/data')",
                "explanation": "Native urllib3 retry strategy attached to Requests session."
            },
            {
                "title": "Thundering Herd Visualized",
                "code": "# Without Jitter (Synchronized Waves Crush Server):\n# Sec 1: [10,000 reqs]  <--- Server CRASHES again!\n# Sec 2: [10,000 reqs]  <--- Server CRASHES again!\n\n# With Full Jitter (Evenly Distributed Traffic):\n# Sec 0.2: [50 reqs], Sec 0.5: [80 reqs], Sec 1.1: [60 reqs] <--- Server recovers smoothly!",
                "explanation": "Illustrates how randomness dissolves server traffic spikes."
            },
            {
                "title": "Honoring the Retry-After Header",
                "code": "# If server returns 429 with explicit Retry-After header, always respect it:\nretry_after = response.headers.get('Retry-After')\nif retry_after:\n    sleep_time = int(retry_after)\n    time.sleep(sleep_time)",
                "explanation": "Server-mandated wait overrides client calculation."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Calculate Exponential Backoff Delay",
            description="Write a Python function `get_backoff_delay(attempt: int, base: float = 1.0) -> float` that returns `base * (2 ** attempt)`.",
            starter_code="def get_backoff_delay(attempt: int, base: float = 1.0) -> float:\n    # Return exponential delay\n    pass",
            solution_code="def get_backoff_delay(attempt: int, base: float = 1.0) -> float:\n    return base * (2 ** attempt)",
            expected_output="1.0 for attempt 0, 2.0 for attempt 1, 4.0 for attempt 2"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the 'Thundering Herd' problem in distributed API architectures?",
                options=[
                    "When thousands of clients all retry failed requests at the exact same synchronized timestamp, overwhelming a recovering server with traffic spikes",
                    "When cows enter a server farm",
                    "When database tables run out of memory",
                    "When code has too many comments"
                ],
                correct_answer="When thousands of clients all retry failed requests at the exact same synchronized timestamp, overwhelming a recovering server with traffic spikes",
                explanation="Synchronized client retries create repeating tsunami waves of traffic."
            ),
            QuizQuestionBlueprint(
                question="Why is adding 'Jitter' (randomized delay variance) critical in exponential backoff algorithms?",
                options=[
                    "It spreads out client retry attempts across time, breaking up synchronized waves and preventing the Thundering Herd",
                    "It makes the computer run cooler",
                    "It encrypts the retry packets",
                    "It bypasses firewalls"
                ],
                correct_answer="It spreads out client retry attempts across time, breaking up synchronized waves and preventing the Thundering Herd",
                explanation="Jitter introduces randomness to disperse client request bursts evenly."
            ),
            QuizQuestionBlueprint(
                question="Which of the following HTTP status codes should NEVER be automatically retried by a client?",
                options=["400 Bad Request (or 401 Unauthorized)", "503 Service Unavailable", "504 Gateway Timeout", "429 Too Many Requests"],
                correct_answer="400 Bad Request (or 401 Unauthorized)",
                explanation="400 indicates client syntax errors; retrying identical bad input will always fail."
            ),
            QuizQuestionBlueprint(
                question="Why should clients generally avoid automatically retrying non-idempotent `POST` requests without an Idempotency Key?",
                options=[
                    "Retrying a failed or timed-out POST request might result in duplicate orders, duplicate bank charges, or duplicate records",
                    "POST requests cannot be retried in HTTP",
                    "Browsers forbid POST retries",
                    "It consumes 100x more bandwidth"
                ],
                correct_answer="Retrying a failed or timed-out POST request might result in duplicate orders, duplicate bank charges, or duplicate records",
                explanation="If the server received the POST but the response dropped, retrying creates duplicates unless protected by idempotency."
            ),
            QuizQuestionBlueprint(
                question="If an API returns a `429 Too Many Requests` response with a `Retry-After: 30` header, what should the client do?",
                options=[
                    "Sleep and pause for at least 30 seconds before attempting to send another request",
                    "Immediately send 30 requests",
                    "Cancel the user's account",
                    "Retry in 1 millisecond"
                ],
                correct_answer="Sleep and pause for at least 30 seconds before attempting to send another request",
                explanation="The `Retry-After` header dictates the server's mandatory cooling-off period."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 42: Webhooks (Reverse APIs / Event-driven responses)
    # ----------------------------------------------------
    DayBlueprint(
        order=42,
        title="Day 42: Webhooks (Reverse APIs & Event-Driven Architecture)",
        concept="Mastering Webhooks: push notifications for servers, HMAC SHA-256 signature verification, idempotent processing, and dead-letter queues.",
        analogy="Standard API is you calling the pizza parlor every 2 minutes: 'Is my pizza ready? Is my pizza ready?'. A Webhook is giving the pizza parlor your home address and telling them: 'Ring my doorbell when the pizza is ready.' They come to your door and deliver the pizza (HTTP POST).",
        theory_sections=[
            {
                "heading": "What is a Webhook?",
                "body": (
                    "A **Webhook** (often called a 'Reverse API' or 'HTTP push') is a way for an app to provide other applications with real-time information. "
                    "Unlike typical APIs where you poll for data, a webhook delivers data to other applications **as it happens**.\n"
                    "- Provider: Stripe, GitHub, Shopify.\n"
                    "- Consumer: Your backend server providing a public webhook endpoint (`https://my-app.com/webhooks/stripe`)."
                )
            },
            {
                "heading": "Verifying Webhook Signatures (HMAC SHA-256)",
                "body": (
                    "Because your webhook endpoint is public on the internet, **anyone could send fake fake payment events**! "
                    "To prevent forgery, webhook providers sign the payload using a shared webhook secret and **HMAC SHA-256**. "
                    "They send the signature in a header (e.g. `Stripe-Signature` or `X-Hub-Signature-256`). "
                    "Your server recalculates the HMAC hash and rejects the payload if it doesn't match."
                )
            },
            {
                "heading": "The 3 Golden Rules of Webhook Handlers",
                "body": (
                    "1. **Acknowledge Fast (Return 200 OK in < 2 seconds)**: Do heavy processing (sending emails, updating inventory) asynchronously in a background job (Celery/BullMQ). "
                    "If you take 10 seconds, the provider assumes you died and retries repeatedly!\n"
                    "2. **Idempotency**: Providers guarantee *at-least-once* delivery. You *will* receive duplicate webhook events. Always check if the event ID was already processed.\n"
                    "3. **Verify Signatures on RAW Body**: Do not parse JSON before verifying HMAC; whitespace changes break hashes!"
                )
            }
        ],
        code_snippets=[
            {
                "title": "Verifying HMAC SHA-256 Webhook Signature in Python",
                "code": "import hmac\nimport hashlib\nfrom flask import Flask, request, jsonify\n\napp = Flask(__name__)\nWEBHOOK_SECRET = b\"whsec_test_secret_key_9988\"\n\n@app.route('/api/webhooks/github', methods=['POST'])\ndef handle_github_webhook():\n    signature_header = request.headers.get('X-Hub-Signature-256')\n    if not signature_header:\n        return jsonify({'error': 'Missing signature'}), 401\n        \n    # 1. Compute expected HMAC hash on RAW request body:\n    raw_body = request.get_data()\n    computed_hash = 'sha256=' + hmac.new(WEBHOOK_SECRET, raw_body, hashlib.sha256).hexdigest()\n    \n    # 2. Constant-time comparison to prevent timing attacks:\n    if not hmac.compare_digest(signature_header, computed_hash):\n        return jsonify({'error': 'Invalid signature'}), 401\n        \n    # 3. Signature verified! Process event payload:\n    event_data = request.json\n    print(f\"Verified event: {event_data.get('action')}\")\n    \n    # Always return 200 OK fast!\n    return jsonify({'status': 'received'}), 200",
                "explanation": "Production HMAC verification protecting against spoofing."
            },
            {
                "title": "Testing Webhooks Locally with ngrok / Localtunnel",
                "code": "# Webhook providers cannot send POST requests to 'localhost:5000'!\n# Use ngrok to expose your local dev server via a secure public tunnel:\nngrok http 5000\n\n# Output gives public URL:\n# Forwarding https://7a4e8c1d.ngrok.io -> http://localhost:5000\n# Paste https://7a4e8c1d.ngrok.io/api/webhooks into Stripe/GitHub settings!",
                "explanation": "Tunneling local server to public internet for webhook testing."
            },
            {
                "title": "Stripe Webhook Verification Library Example",
                "code": "import stripe\n\n@app.route('/webhook', methods=['POST'])\ndef stripe_webhook():\n    payload = request.data\n    sig_header = request.headers.get('Stripe-Signature')\n    try:\n        event = stripe.Webhook.construct_event(payload, sig_header, WEBHOOK_SECRET)\n    except (ValueError, stripe.error.SignatureVerificationError):\n        return 'Bad signature', 400\n        \n    if event['type'] == 'checkout.session.completed':\n        enqueue_order_fulfillment(event['data']['object'])\n    return '', 200",
                "explanation": "SDK helper for webhook verification."
            },
            {
                "title": "Webhook Retry Policy",
                "code": "# If your server returns 500 or times out, Stripe retries on an exponential schedule:\n# - Attempt 1: Immediate\n# - Attempt 2: After 5 mins\n# - Attempt 3: After 30 mins\n# - Attempt 4: After 2 hours\n# Continues retrying for up to 3 days before dropping to Dead-Letter Queue!",
                "explanation": "Illustrates why idempotency is mandatory for webhook receivers."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Compute HMAC SHA-256 Signature",
            description="Write a Python function `sign_payload(secret: bytes, body: bytes) -> str` that computes and returns the hex digest of an HMAC-SHA256 signature.",
            starter_code="import hmac, hashlib\ndef sign_payload(secret: bytes, body: bytes) -> str:\n    # Return hex digest\n    pass",
            solution_code="import hmac, hashlib\ndef sign_payload(secret: bytes, body: bytes) -> str:\n    return hmac.new(secret, body, hashlib.sha256).hexdigest()",
            expected_output="64-character hex string"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Why is a Webhook often described as a 'Reverse API'?",
                options=[
                    "Instead of the client making requests to the server, the server initiates an HTTP POST request to the client's URL when an event occurs",
                    "Webhooks run in reverse chronological order",
                    "Webhooks reverse the bytes in a JSON payload",
                    "Webhooks only accept DELETE requests"
                ],
                correct_answer="Instead of the client making requests to the server, the server initiates an HTTP POST request to the client's URL when an event occurs",
                explanation="Webhooks reverse the initiator role: the provider calls the consumer."
            ),
            QuizQuestionBlueprint(
                question="Why must incoming webhook payloads be cryptographically verified using HMAC SHA-256 signatures?",
                options=[
                    "Because webhook endpoints are public URLs; without signature verification, attackers could send fake payment events and fraud your system",
                    "To compress the JSON payload",
                    "Because webhooks do not work over HTTPS",
                    "To translate the payload into English"
                ],
                correct_answer="Because webhook endpoints are public URLs; without signature verification, attackers could send fake payment events and fraud your system",
                explanation="HMAC signatures prove that the payload originated from the authentic provider and was not tampered with."
            ),
            QuizQuestionBlueprint(
                question="Why is it critical for a webhook handler endpoint to return a `200 OK` response within 1-2 seconds?",
                options=[
                    "If the handler takes too long processing, the provider will assume the server crashed and trigger aggressive duplicate retries",
                    "The browser will close",
                    "The server will be deleted",
                    "Webhooks only exist for 2 seconds"
                ],
                correct_answer="If the handler takes too long processing, the provider will assume the server crashed and trigger aggressive duplicate retries",
                explanation="Fast acknowledgment prevents providers from triggering unnecessary retries."
            ),
            QuizQuestionBlueprint(
                question="Why must webhook handlers be designed to be strictly IDEMPOTENT?",
                options=[
                    "Webhook providers guarantee 'at-least-once' delivery; network hiccups mean your server WILL occasionally receive duplicate events",
                    "Because webhooks are written in Python",
                    "Idempotency speeds up database indexing",
                    "Because Stripe requires all users to be idempotent"
                ],
                correct_answer="Webhook providers guarantee 'at-least-once' delivery; network hiccups mean your server WILL occasionally receive duplicate events",
                explanation="Network retries cause duplicate deliveries; handlers must track event IDs to prevent duplicate actions."
            ),
            QuizQuestionBlueprint(
                question="Which utility tool is widely used by developers to tunnel local development servers (`localhost:5000`) to a public URL to test webhooks?",
                options=["ngrok", "Docker", "Git", "Webpack"],
                correct_answer="ngrok",
                explanation="`ngrok` exposes local ports through secure public tunnels for webhook testing."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 43: WebSockets (Real-time bidirectional communication)
    # ----------------------------------------------------
    DayBlueprint(
        order=43,
        title="Day 43: WebSockets (Real-Time Bidirectional Full-Duplex Communication)",
        concept="Architecting real-time communication: protocol upgrade handshake (`101 Switching Protocols`), full-duplex TCP streaming, framing, and heartbeat pings.",
        analogy="HTTP is like sending letters back and forth: you mail a letter, wait for a reply, and the mailbox closes. A WebSocket is like picking up a direct telephone call: the line stays open continuously, and both people can talk and listen at the exact same millisecond without hanging up.",
        theory_sections=[
            {
                "heading": "The Limitations of HTTP for Real-Time",
                "body": (
                    "HTTP is fundamentally unidirectional and half-duplex: only the client can speak, and the server can only respond. "
                    "For live chat apps, multiplayer gaming, financial stock tickers, and collaborative editing (Google Docs), "
                    "repeated HTTP polling wastes enormous bandwidth on repetitive headers."
                )
            },
            {
                "heading": "How WebSockets Work (RFC 6455)",
                "body": (
                    "The **WebSocket Protocol (`ws://` and `wss://`)** provides persistent, low-latency, full-duplex communication over a single TCP socket:\n"
                    "1. **The Handshake**: Client sends standard HTTP request with `Upgrade: websocket` and `Connection: Upgrade`.\n"
                    "2. **The Upgrade**: Server responds with `HTTP/1.1 101 Switching Protocols`.\n"
                    "3. **The Stream**: The HTTP connection transitions into a bi-directional WebSocket connection. "
                    "Both client and server can transmit lightweight binary/text frames (with only 2 to 10 bytes of frame overhead instead of 800 bytes of HTTP headers!)."
                )
            },
            {
                "heading": "Heartbeats (Ping / Pong)",
                "body": (
                    "Intermediate routers, firewalls, and load balancers aggressively close idle TCP sockets. "
                    "WebSockets maintain liveness by sending periodic lightweight **Ping / Pong frames** every 30 seconds."
                )
            }
        ],
        code_snippets=[
            {
                "title": "WebSocket Server in Python (websockets library)",
                "code": "import asyncio\nimport websockets\n\nCONNECTED_CLIENTS = set()\n\nasync def chat_handler(websocket):\n    CONNECTED_CLIENTS.add(websocket)\n    try:\n        # Listen for messages continuously over persistent socket:\n        async for message in websocket:\n            print(f\"Received: {message}\")\n            # Broadcast message to all connected users:\n            for client in CONNECTED_CLIENTS:\n                if client != websocket:\n                    await client.send(f\"Echo: {message}\")\n    finally:\n        CONNECTED_CLIENTS.remove(websocket)\n\n# start_server = websockets.serve(chat_handler, \"localhost\", 8765)",
                "explanation": "Asynchronous WebSocket broadcast server."
            },
            {
                "title": "Native WebSocket Client in JavaScript",
                "code": "// Connect to secure WebSocket server:\nconst socket = new WebSocket('wss://api.example.com/chat');\n\nsocket.onopen = (event) => {\n    console.log('✅ Connected to WebSocket!');\n    socket.send(JSON.stringify({ type: 'GREETING', text: 'Hello Server!' }));\n};\n\nsocket.onmessage = (event) => {\n    const data = JSON.parse(event.data);\n    console.log('Live message received:', data);\n};\n\nsocket.onclose = () => console.log('Socket closed');\nsocket.onerror = (err) => console.error('Socket error:', err);",
                "explanation": "Native browser WebSocket client handling lifecycle events."
            },
            {
                "title": "The 101 Handshake Wire Exchange",
                "code": "# Client -> Server (HTTP):\n# GET /chat HTTP/1.1\n# Host: server.example.com\n# Upgrade: websocket\n# Connection: Upgrade\n# Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==\n# Sec-WebSocket-Version: 13\n\n# Server -> Client (HTTP):\n# HTTP/1.1 101 Switching Protocols\n# Upgrade: websocket\n# Connection: Upgrade\n# Sec-WebSocket-Accept: s3pPLMBiTxaQ9kYGzzhZRbK+xOo=",
                "explanation": "Cryptographic nonce handshake transitioning protocol."
            },
            {
                "title": "HTTP Polling vs WebSocket Overhead",
                "code": "# Metric             | HTTP Polling (1/sec) | WebSocket Persistent\n# -------------------+----------------------+---------------------\n# Header Overhead    | ~800 bytes / request | ~2-6 bytes / frame\n# Latency            | Polling interval gap | ~1 millisecond\n# Bidirectional      | No (Client-pull only)| Yes (Full Duplex)\n# Connection Lifetime| Ephemeral            | Long-lived persistent",
                "explanation": "Quantitative comparison highlighting WebSocket efficiency."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Create WebSocket Message Dispatcher",
            description="Write a Python class `SocketRoom` with `clients` set, `join(ws)`, and `broadcast(msg)` that calls `ws.send(msg)` for each client in the set.",
            starter_code="class SocketRoom:\n    def __init__(self):\n        self.clients = set()\n    # Implement join and broadcast\n",
            solution_code="class SocketRoom:\n    def __init__(self):\n        self.clients = set()\n    def join(self, ws):\n        self.clients.add(ws)\n    def broadcast(self, msg):\n        for c in self.clients:\n            c.send(msg)",
            expected_output="Calls send on all registered clients"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What HTTP status code is sent by the server to confirm successful upgrade to the WebSocket protocol?",
                options=["101 Switching Protocols", "200 OK", "204 No Content", "301 Redirect"],
                correct_answer="101 Switching Protocols",
                explanation="`101 Switching Protocols` signals protocol upgrade to WebSockets."
            ),
            QuizQuestionBlueprint(
                question="What is the primary difference between half-duplex and full-duplex communication?",
                options=[
                    "In half-duplex, only one party can send data at a time; in full-duplex (WebSockets), both client and server can transmit simultaneously over the open socket",
                    "Full-duplex only works in California",
                    "Half-duplex runs on batteries",
                    "There is no difference"
                ],
                correct_answer="In half-duplex, only one party can send data at a time; in full-duplex (WebSockets), both client and server can transmit simultaneously over the open socket",
                explanation="WebSockets provide full-duplex bidirectional streaming."
            ),
            QuizQuestionBlueprint(
                question="Why are periodic 'Ping / Pong' heartbeat frames sent over persistent WebSocket connections?",
                options=[
                    "To prevent intermediate NAT gateways, firewalls, and load balancers from killing idle TCP connections",
                    "To measure player score in games",
                    "To download music",
                    "To compress the database"
                ],
                correct_answer="To prevent intermediate NAT gateways, firewalls, and load balancers from killing idle TCP connections",
                explanation="Heartbeats keep stateful NAT firewalls from closing idle socket connections."
            ),
            QuizQuestionBlueprint(
                question="What is the URI scheme prefix used for encrypted, secure WebSocket connections?",
                options=["`wss://`", "`https://`", "`ws-secure://`", "`ssl-socket://`"],
                correct_answer="`wss://`",
                explanation="`wss://` (WebSocket Secure) operates over TLS on port 443."
            ),
            QuizQuestionBlueprint(
                question="Roughly how much header overhead does a single WebSocket data frame have compared to an HTTP/1.1 request?",
                options=[
                    "~2 to 10 bytes for WebSockets vs ~500 to 1,000 bytes for HTTP",
                    "WebSockets have more overhead than HTTP",
                    "Exactly 1 megabyte",
                    "Zero bytes"
                ],
                correct_answer="~2 to 10 bytes for WebSockets vs ~500 to 1,000 bytes for HTTP",
                explanation="WebSocket framing adds only 2-10 bytes of overhead per message."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 44: SSE (Server-Sent Events)
    # ----------------------------------------------------
    DayBlueprint(
        order=44,
        title="Day 44: SSE (Server-Sent Events: Streaming Unidirectional Data)",
        concept="Evaluating Server-Sent Events (SSE): HTTP-native unidirectional real-time streaming, `text/event-stream` MIME type, automatic reconnection, and powering AI LLM token streams.",
        analogy="A WebSocket is a two-way phone call. Server-Sent Events (SSE) is an old-fashioned ticker-tape machine or FM radio broadcast: the news studio transmits continuous text updates down the wire into your living room, and your radio listens silently without talking back.",
        theory_sections=[
            {
                "heading": "What are Server-Sent Events (SSE)?",
                "body": (
                    "**Server-Sent Events (SSE)** is an HTTP-standard technology (HTML5) that allows a server to push real-time data "
                    "down to a client over a single long-lived standard HTTP connection. "
                    "Unlike WebSockets, SSE is strictly **unidirectional (Server to Client only)**."
                )
            },
            {
                "heading": "Why SSE is Booming: The AI LLM Revolution",
                "body": (
                    "Whenever you use ChatGPT, Claude, or modern AI assistants, and you watch words appear on the screen one token at a time: "
                    "**that is Server-Sent Events in action!** "
                    "Because the user only sends their prompt once (via POST), and the server streams tokens back for 30 seconds, "
                    "SSE is drastically simpler, more lightweight, and easier to scale than WebSockets."
                )
            },
            {
                "heading": "Key Advantages of SSE over WebSockets",
                "body": (
                    "1. **Standard HTTP**: Runs over standard HTTP/1.1 or HTTP/2. No custom protocols, no proxy blocking, works through all corporate firewalls.\n"
                    "2. **Built-in Reconnection**: If the network drops, browsers automatically reconnect and send `Last-Event-ID` to resume streaming without data loss!\n"
                    "3. **Simple Text Protocol**: Events are plain text formatted with `data: ...\\n\\n`."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Streaming AI Tokens with SSE in Python Flask",
                "code": "import time\nfrom flask import Flask, Response\n\napp = Flask(__name__)\n\n@app.route('/api/v1/stream-ai-response')\ndef stream_ai():\n    def generate_tokens():\n        tokens = [\"Hello\", \"!\", \" How\", \" can\", \" I\", \" assist\", \" you\", \" today\", \"?\"]\n        for token in tokens:\n            time.sleep(0.1) # Simulate LLM inference delay\n            # SSE format strictly requires 'data: <payload>\\n\\n':\n            yield f\"data: {token}\\n\\n\"\n            \n    return Response(generate_tokens(), mimetype='text/event-stream')",
                "explanation": "Yielding SSE token chunks with text/event-stream MIME type."
            },
            {
                "title": "Consuming SSE in Browser via EventSource API",
                "code": "// Built-in browser EventSource API:\nconst eventSource = new EventSource('/api/v1/stream-ai-response');\n\neventSource.onmessage = (event) => {\n    const token = event.data;\n    document.getElementById('chat-box').innerHTML += token;\n};\n\neventSource.onerror = (err) => {\n    console.log('Stream finished or connection dropped');\n    eventSource.close();\n};",
                "explanation": "Native browser consumption using EventSource interface."
            },
            {
                "title": "SSE Wire Format Specification",
                "code": "# Official SSE framing syntax:\n# event: customEventName (optional)\n# id: 42 (optional - used for auto-resume)\n# retry: 10000 (optional - reconnect delay in ms)\n# data: {\"temperature\": 24.5}\n# \\n\\n (Mandatory double newline ends the message!)",
                "explanation": "Wire format with ID and retry parameters."
            },
            {
                "title": "WebSocket vs SSE Feature Comparison",
                "code": "# Feature           | WebSockets              | Server-Sent Events (SSE)\n# ------------------+-------------------------+-------------------------\n# Direction         | Bidirectional (Full)    | Unidirectional (Server->Client)\n# Protocol          | Custom (ws:// / wss://) | Standard HTTP (http://)\n# Reconnection      | Manual code required    | Automatic by browser\n# Proxy/Firewall    | Sometimes blocked       | Never blocked (pure HTTP)\n# Prime Use Case    | Multiplayer Gaming/Chat | AI Streaming / Live Feeds",
                "explanation": "Strategic architectural comparison."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Format Server-Sent Event Message",
            description="Write a Python function `format_sse(data: str, event: str = None) -> str` that formats an SSE string ending with double newline `\\n\\n`.",
            starter_code="def format_sse(data: str, event: str = None) -> str:\n    # Format SSE payload\n    pass",
            solution_code="def format_sse(data: str, event: str = None) -> str:\n    result = \"\"\n    if event:\n        result += f\"event: {event}\\n\"\n    result += f\"data: {data}\\n\\n\"\n    return result",
            expected_output="'data: Hello\\n\\n' or with event prefix"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the official MIME content type required for Server-Sent Events (SSE)?",
                options=["text/event-stream", "application/sse", "text/plain", "application/stream+json"],
                correct_answer="text/event-stream",
                explanation="SSE streams must declare `Content-Type: text/event-stream`."
            ),
            QuizQuestionBlueprint(
                question="Why is Server-Sent Events (SSE) heavily preferred over WebSockets for AI chat applications (like ChatGPT token streaming)?",
                options=[
                    "Because communication is strictly one-way (server pushing tokens to user); SSE is simpler, runs on standard HTTP, and has automatic reconnection",
                    "Because WebSockets cannot send text",
                    "Because SSE was invented by OpenAI",
                    "Because WebSockets cost money"
                ],
                correct_answer="Because communication is strictly one-way (server pushing tokens to user); SSE is simpler, runs on standard HTTP, and has automatic reconnection",
                explanation="One-way streaming benefits from SSE's HTTP simplicity and automatic browser reconnection."
            ),
            QuizQuestionBlueprint(
                question="Which built-in browser JavaScript API is used to consume Server-Sent Events?",
                options=["EventSource", "WebSocket", "FetchStream", "PushReceiver"],
                correct_answer="EventSource",
                explanation="The native browser API for consuming SSE is `EventSource`."
            ),
            QuizQuestionBlueprint(
                question="What character sequence terminates an individual message block in the SSE text format?",
                options=["Two consecutive newline characters (`\\n\\n`)", "A semicolon", "A closing tag `</event>`", "An EOF byte"],
                correct_answer="Two consecutive newline characters (`\\n\\n`)",
                explanation="The SSE specification requires a blank line (`\\n\\n`) to dispatch the event."
            ),
            QuizQuestionBlueprint(
                question="What header does the browser automatically send when reconnecting to an SSE stream to resume from where it dropped off?",
                options=["Last-Event-ID", "Resume-From", "ETag", "If-Modified-Since"],
                correct_answer="Last-Event-ID",
                explanation="Browsers transmit `Last-Event-ID` upon reconnection to resume missed events."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 45: Polling vs Long Polling vs Webhooks vs WebSockets
    # ----------------------------------------------------
    DayBlueprint(
        order=45,
        title="Day 45: Polling vs Long Polling vs Webhooks vs WebSockets",
        concept="The Ultimate Real-Time Decision Matrix: contrasting short polling, long polling (Comet), webhooks, WebSockets, and SSE across latency, scalability, and complexity.",
        analogy="Waiting for a package:\n- Short Polling: Running to the front door every 10 seconds to check the porch.\n- Long Polling: Opening the front door and standing on the porch staring at the road until the delivery truck drives up.\n- Webhooks: Giving the delivery company your phone number to text you.\n- WebSockets: Building a private pneumatic tube directly between the warehouse and your living room.",
        theory_sections=[
            {
                "heading": "The Real-Time Architectural Landscape",
                "body": (
                    "When designing modern systems, choosing the correct communication pattern directly impacts server load, "
                    "battery life, and operational costs. There is no silver bullet; each pattern fulfills specific trade-offs."
                )
            },
            {
                "heading": "1. Short Polling",
                "body": (
                    "- Client fires `GET /status` every $N$ seconds.\n"
                    "- Pros: Dead simple to implement, works anywhere, 100% stateless.\n"
                    "- Cons: Terrible waste of server CPU and bandwidth (95% of responses return empty data)."
                )
            },
            {
                "heading": "2. Long Polling (Comet)",
                "body": (
                    "- Client sends request; server **holds the connection open** until data becomes available (or timeout).\n"
                    "- Once data arrives, server responds, client immediately opens a new long-poll connection.\n"
                    "- Pros: Lower latency than short polling, works over plain HTTP.\n"
                    "- Cons: Ties up server connection threads; re-establishing connections still incurs overhead."
                )
            },
            {
                "heading": "3. The Architectural Decision Tree",
                "body": (
                    "- Need server-to-server notifications? -> **Webhooks**.\n"
                    "- Need bidirectional real-time with sub-millisecond latency (Gaming/Chat)? -> **WebSockets**.\n"
                    "- Need unidirectional streaming from server to browser (AI/Stock Ticker)? -> **SSE**.\n"
                    "- Infrequent updates (> 5 minutes) on simple apps? -> **Short Polling**."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Comprehensive Architecture Decision Matrix",
                "code": "# Technology    | Direction | Protocol   | Latency   | Server Load | Best Use Case\n# --------------+-----------+------------+-----------+-------------+-------------------------\n# Short Polling | Client->S | HTTP       | High      | Extremely H | Simple infrequent status\n# Long Polling  | Client->S | HTTP (Hold)| Medium    | High        | Legacy fallback chat\n# Webhooks      | Server->S | HTTP POST  | Immediate | Minimal     | Payment/Git event notify\n# SSE           | Server->C | HTTP Stream| Real-Time | Low         | AI LLM tokens, tickers\n# WebSockets    | Full-Dup  | TCP (ws://)| Real-Time | Efficient   | Multiplayer games, chat",
                "explanation": "Master trade-off comparison matrix."
            },
            {
                "title": "Long Polling Server Implementation in Python",
                "code": "import time\nfrom flask import Flask, request, jsonify\n\napp = Flask(__name__)\nMESSAGES = []\n\n@app.route('/api/v1/poll-chat')\ndef long_poll():\n    last_seen_count = int(request.args.get('count', 0))\n    timeout = 25  # Hold connection up to 25 seconds\n    start = time.time()\n    \n    # Hold connection open waiting for new data:\n    while time.time() - start < timeout:\n        if len(MESSAGES) > last_seen_count:\n            # New message arrived! Return immediately:\n            return jsonify({'messages': MESSAGES[last_seen_count:]})\n        time.sleep(0.5)\n        \n    # Timeout reached with no new messages: return 204 or empty list\n    return jsonify({'messages': []}), 200",
                "explanation": "Server holding connection until event occurs or timeout elapses."
            },
            {
                "title": "Short Polling Client Loop in JavaScript",
                "code": "function startShortPolling() {\n    setInterval(async () => {\n        const res = await fetch('/api/v1/notifications');\n        const data = await res.json();\n        if (data.has_unread) {\n            showBadge(data.count);\n        }\n    }, 30000); // Polls every 30 seconds\n}",
                "explanation": "Simple client polling implementation."
            },
            {
                "title": "Architectural Summary",
                "code": "# Rule of Thumb:\n# If bidirectional -> WebSocket\n# If streaming text/data down -> SSE\n# If server-to-server -> Webhook\n# If infrequent check -> Short Poll",
                "explanation": "Quick heuristic guide for engineering teams."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Implement Real-Time Technology Selector",
            description="Write a Python function `choose_realtime_tech(is_bidirectional: bool, is_server_to_server: bool) -> str` that returns 'Webhook' if server-to-server, 'WebSocket' if bidirectional, and 'SSE' otherwise.",
            starter_code="def choose_realtime_tech(is_bidirectional: bool, is_server_to_server: bool) -> str:\n    # Return tech string\n    pass",
            solution_code="def choose_realtime_tech(is_bidirectional: bool, is_server_to_server: bool) -> str:\n    if is_server_to_server:\n        return 'Webhook'\n    if is_bidirectional:\n        return 'WebSocket'\n    return 'SSE'",
            expected_output="'Webhook', 'WebSocket', or 'SSE'"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Which technology is best suited when a payment gateway (like Stripe) needs to inform an e-commerce backend that a customer completed a checkout?",
                options=["Webhooks", "WebSockets", "Short Polling", "SSE"],
                correct_answer="Webhooks",
                explanation="Webhooks are the industry standard for event-driven server-to-server notifications."
            ),
            QuizQuestionBlueprint(
                question="What is the primary operational difference between Short Polling and Long Polling?",
                options=[
                    "In short polling, the server responds immediately whether data exists or not; in long polling, the server holds the HTTP connection open until new data arrives or timeout occurs",
                    "Long polling requires satellite internet",
                    "Short polling runs only on microservices",
                    "There is no difference"
                ],
                correct_answer="In short polling, the server responds immediately whether data exists or not; in long polling, the server holds the HTTP connection open until new data arrives or timeout occurs",
                explanation="Long polling suspends response delivery until events occur, reducing wasted polling loops."
            ),
            QuizQuestionBlueprint(
                question="For a multiplayer online browser game requiring sub-10ms two-way inputs between player and server, which technology is mandatory?",
                options=["WebSockets", "Webhooks", "SSE", "Short Polling"],
                correct_answer="WebSockets",
                explanation="Low-latency bidirectional streaming requires full-duplex WebSockets."
            ),
            QuizQuestionBlueprint(
                question="Why is Short Polling considered an anti-pattern for high-frequency updates?",
                options=[
                    "Over 95% of polling requests return empty data, wasting massive amounts of server CPU, database capacity, and network bandwidth on repetitive HTTP headers",
                    "It causes computers to shut down",
                    "Short polling is illegal",
                    "It only works on Android"
                ],
                correct_answer="Over 95% of polling requests return empty data, wasting massive amounts of server CPU, database capacity, and network bandwidth on repetitive HTTP headers",
                explanation="Repetitive empty poll requests burn bandwidth and server compute."
            ),
            QuizQuestionBlueprint(
                question="Which real-time pattern is uniquely designed for unidirectional (server-to-client) streaming over native HTTP with automatic browser reconnection?",
                options=["SSE (Server-Sent Events)", "WebSockets", "RPC", "UDP"],
                correct_answer="SSE (Server-Sent Events)",
                explanation="SSE provides HTTP-native unidirectional streaming with built-in reconnection."
            )
        ]
    )
]
