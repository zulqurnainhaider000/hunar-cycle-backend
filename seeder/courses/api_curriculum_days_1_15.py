"""
Complete APIs & Web Services Architecture Curriculum - Days 1 to 15
Phase 1: API & Web Services Fundamentals (Days 1-5)
Phase 2: HTTP Protocol & Core Concepts (Days 6-12)
Phase 3: REST Architecture (The Core Rules) - Part 1 (Days 13-15 of 13-18)
"""

from seeder.course_blueprint import DayBlueprint, QuizQuestionBlueprint, CodingChallengeBlueprint

DAYS_1_TO_15 = [
    # ----------------------------------------------------
    # Day 1: API (Application Programming Interface) kya hai?
    # ----------------------------------------------------
    DayBlueprint(
        order=1,
        title="Day 1: What is an API? (Application Programming Interface)",
        concept="Understanding the fundamental definition, purpose, and role of an API as an abstraction contract between software applications.",
        analogy="Think of an API like a waiter in a restaurant. You are the customer (the Client/Frontend), the kitchen is the database/server (Backend), and the menu is the API documentation. You don't walk into the kitchen to cook; you tell the waiter your order, the waiter delivers it to the kitchen, and brings back your delicious food.",
        theory_sections=[
            {
                "heading": "What Exactly is an API?",
                "body": (
                    "An **API (Application Programming Interface)** is a formalized set of rules, protocols, and tools that allows different software "
                    "applications to communicate with each other. It defines the kinds of requests that can be made, how to make them, "
                    "the data formats that must be used, and the conventions expected in responses."
                )
            },
            {
                "heading": "The Abstraction and Encapsulation Power",
                "body": (
                    "APIs provide abstraction. When an Uber app needs to calculate a route, it doesn't build satellite mapping technology from scratch; "
                    "it calls the Google Maps API. When an e-commerce site processes a credit card, it delegates security to Stripe's API. "
                    "The consumer only cares about inputs and outputs, not the internal code implementation."
                )
            },
            {
                "heading": "Types of APIs Across the Stack",
                "body": (
                    "- **Hardware/OS APIs**: POSIX, Windows Win32, or camera APIs on iOS/Android.\n"
                    "- **Library/Language APIs**: Methods provided by Python's `math` library or Java standard library.\n"
                    "- **Web APIs / Network APIs**: Interfaces accessed over HTTP/HTTPS across a network (e.g. GitHub API, Weather API)."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Consuming a Public Web API with Python",
                "code": "import requests\n\n# Making an HTTP GET request to a public API endpoint:\nresponse = requests.get('https://api.github.com/users/octocat')\n\nif response.status_code == 200:\n    user_data = response.json()\n    print(f\"Username: {user_data['login']}\")\n    print(f\"Public Repos: {user_data['public_repos']}\")",
                "explanation": "A client requests JSON data from GitHub's REST API over HTTPS."
            },
            {
                "title": "Minimal API Producer with Flask",
                "code": "from flask import Flask, jsonify\n\napp = Flask(__name__)\n\n# Exposing an API endpoint contract:\n@app.route('/api/v1/health', methods=['GET'])\ndef health_check():\n    return jsonify({\n        'status': 'healthy',\n        'uptime_seconds': 1420,\n        'database': 'connected'\n    }), 200\n\nif __name__ == '__main__':\n    app.run(port=5000)",
                "explanation": "Defines an API route that serializes internal state into a structured JSON response."
            },
            {
                "title": "Client-Server API Communication Flow",
                "code": "# [Client (React / Mobile App)] \n#            |\n#            | 1. HTTP Request (GET /api/v1/products)\n#            v\n# [API Gateway / Web Server (Flask / Node.js)]\n#            |\n#            | 2. SQL Query (SELECT * FROM products)\n#            v\n# [Database (PostgreSQL / Redis)]\n#            |\n#            | 3. Query Results\n#            v\n# [API Server transforms data to JSON]\n#            |\n#            | 4. HTTP Response (200 OK + JSON payload)\n#            v\n# [Client renders UI]",
                "explanation": "Architectural lifecycle of a standard Web API transaction."
            },
            {
                "title": "Consuming API via cURL in the Terminal",
                "code": "# Fetching API data directly from the command line:\ncurl -X GET https://jsonplaceholder.typicode.com/todos/1\n\n# Output:\n# {\n#   \"userId\": 1,\n#   \"id\": 1,\n#   \"title\": \"delectus aut autem\",\n#   \"completed\": false\n# }",
                "explanation": "Using cURL as a quick command-line client to test API endpoints."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Create Health Check API Endpoint",
            description="Write a Python Flask API endpoint for route '/api/ping' returning JSON {'message': 'pong'} with status code 200.",
            starter_code="from flask import Flask, jsonify\n\napp = Flask(__name__)\n\n# Define /api/ping route\n",
            solution_code="from flask import Flask, jsonify\n\napp = Flask(__name__)\n\n@app.route('/api/ping', methods=['GET'])\ndef ping():\n    return jsonify({'message': 'pong'}), 200",
            expected_output="{'message': 'pong'}, 200"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What does the acronym API stand for in software engineering?",
                options=[
                    "Application Programming Interface",
                    "Automated Protocol Integration",
                    "Asynchronous Process Interconnect",
                    "Advanced Programming Instruction"
                ],
                correct_answer="Application Programming Interface",
                explanation="API stands for Application Programming Interface—a contract for software communication."
            ),
            QuizQuestionBlueprint(
                question="In the classic restaurant analogy, which role corresponds directly to the API?",
                options=[
                    "The Waiter (who carries requests to the kitchen and delivers the food back)",
                    "The Kitchen Chef (the database)",
                    "The Customer (the client)",
                    "The Cash Register"
                ],
                correct_answer="The Waiter (who carries requests to the kitchen and delivers the food back)",
                explanation="The waiter abstracts the kitchen's inner workings and delivers structured requests and responses."
            ),
            QuizQuestionBlueprint(
                question="Which of the following is a primary benefit of using APIs in modern software development?",
                options=[
                    "Abstraction: developers can utilize complex third-party features (e.g. Stripe, Google Maps) without knowing internal code",
                    "APIs eliminate the need for computer programming languages",
                    "APIs make servers immune to power outages",
                    "APIs double the speed of hardware processors"
                ],
                correct_answer="Abstraction: developers can utilize complex third-party features (e.g. Stripe, Google Maps) without knowing internal code",
                explanation="APIs abstract underlying implementation details behind clean, predictable contracts."
            ),
            QuizQuestionBlueprint(
                question="Can an API exist purely on a single computer without any internet connection?",
                options=[
                    "Yes, Operating System APIs (like POSIX or Windows API) and library APIs operate completely offline",
                    "No, all APIs require a worldwide web connection by definition",
                    "Only if using satellite internet",
                    "Only if written in HTML"
                ],
                correct_answer="Yes, Operating System APIs (like POSIX or Windows API) and library APIs operate completely offline",
                explanation="Web APIs communicate over networks, but OS and library APIs operate locally."
            ),
            QuizQuestionBlueprint(
                question="What format is most universally returned by modern Web APIs when communicating with frontend clients?",
                options=["JSON (JavaScript Object Notation)", "PDF", "Raw Assembly Code", "MP3 Audio"],
                correct_answer="JSON (JavaScript Object Notation)",
                explanation="JSON is the lightweight, human-readable lingua franca of modern Web APIs."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 2: Web Services vs APIs mein farq
    # ----------------------------------------------------
    DayBlueprint(
        order=2,
        title="Day 2: Web Services vs APIs (The Critical Differences)",
        concept="Dissecting the nuanced distinction between Web Services and APIs: 'All Web Services are APIs, but not all APIs are Web Services'.",
        analogy="All apples are fruits, but not all fruits are apples. Similarly, all Web Services are APIs (they provide interfaces), but not all APIs are Web Services (some APIs are local libraries, hardware drivers, or non-network interfaces).",
        theory_sections=[
            {
                "heading": "The Golden Venn Diagram",
                "body": (
                    "The relationship between APIs and Web Services is a strict subset hierarchy:\n"
                    "> **\"All Web Services are APIs, but not all APIs are Web Services.\"**\n\n"
                    "- An **API** is any interface allowing two software components to talk (local memory, DLLs, OS system calls, or network).\n"
                    "- A **Web Service** is specifically an API that operates **strictly over a network** using standard web communication protocols (HTTP, XML-RPC, SOAP, WSDL)."
                )
            },
            {
                "heading": "Architectural Comparison Matrix",
                "body": (
                    "1. **Network Requirement**: APIs can run locally in-memory (e.g., `Math.floor()` in JS); Web Services *must* have a network.\n"
                    "2. **Protocol Style**: Web Services typically require specific messaging formats (historically SOAP with heavy XML schemas and WSDL contracts). Web APIs (REST) use lightweight HTTP/JSON.\n"
                    "3. **Coupling**: Traditional Web Services (SOAP) are tightly coupled with strict schemas; modern Web APIs (REST/JSON) are loosely coupled."
                )
            },
            {
                "heading": "The Evolution from SOAP Web Services to RESTful APIs",
                "body": (
                    "In the 1990s and early 2000s, enterprise 'Web Services' relied heavily on XML, SOAP (Simple Object Access Protocol), "
                    "and complex WSDL (Web Services Description Language) definitions. "
                    "Modern software shifted toward lightweight RESTful HTTP APIs."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Local API (Not a Web Service) Example",
                "code": "import math\n\n# This is an API method call inside local Python runtime:\n# No network connection, no HTTP, no IP address involved.\nradius = 5\narea = math.pi * math.pow(radius, 2)\nprint(f\"Circle Area: {area}\")",
                "explanation": "A programming language library API operating purely in local RAM."
            },
            {
                "title": "Legacy SOAP Web Service Request (Heavy XML Envelope)",
                "code": "<!-- A classic SOAP Web Service XML envelope over HTTP -->\n<soapenv:Envelope xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\"\n                  xmlns:web=\"http://example.com/webservice\">\n   <soapenv:Header/>\n   <soapenv:Body>\n      <web:GetAccountBalance>\n         <web:AccountNumber>987654321</web:AccountNumber>\n      </web:GetAccountBalance>\n   </soapenv:Body>\n</soapenv:Envelope>",
                "explanation": "SOAP requires strict XML contracts and headers."
            },
            {
                "title": "Modern RESTful Web API Request (Lightweight JSON)",
                "code": "# Modern Web API equivalent over HTTP/JSON:\n# GET /api/v1/accounts/987654321/balance HTTP/1.1\n# Host: api.bank.com\n# Authorization: Bearer eyJhbGci...\n\n# Response:\n# {\n#   \"account_number\": \"987654321\",\n#   \"balance\": 14500.50,\n#   \"currency\": \"USD\"\n# }",
                "explanation": "Simple, lightweight JSON payload accessed via standard URI."
            },
            {
                "title": "Comparison Summary",
                "code": "# Property          | General API         | Web Service (e.g. SOAP)\n# ------------------+---------------------+------------------------\n# Needs Network     | No (can be local)   | Yes (strictly network)\n# Data Format       | Any (Objects, JSON) | Strictly XML/WSDL\n# Transport         | Function calls/IPC  | HTTP, SMTP, TCP\n# Weight            | Lightweight         | Heavyweight contracts",
                "explanation": "Core distinctions between general APIs and traditional Web Services."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Identify API Type via Function",
            description="Write a Python function `classify_interface(requires_network: bool, format_type: str) -> str` that returns 'Web Service' if network is True and format is 'XML', 'REST Web API' if network is True and format is 'JSON', and 'Local API' if network is False.",
            starter_code="def classify_interface(requires_network: bool, format_type: str) -> str:\n    # Return classification string\n    pass",
            solution_code="def classify_interface(requires_network: bool, format_type: str) -> str:\n    if not requires_network:\n        return 'Local API'\n    if format_type.upper() == 'XML':\n        return 'Web Service'\n    return 'REST Web API'",
            expected_output="Local API, Web Service, REST Web API"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Which statement accurately describes the relationship between APIs and Web Services?",
                options=[
                    "All Web Services are APIs, but not all APIs are Web Services",
                    "All APIs are Web Services, but not all Web Services are APIs",
                    "Web Services and APIs are completely unrelated technologies",
                    "Web Services run on phones; APIs only run on supercomputers"
                ],
                correct_answer="All Web Services are APIs, but not all APIs are Web Services",
                explanation="Web Services are a specific network-based subset of the broader API category."
            ),
            QuizQuestionBlueprint(
                question="Which of the following is an example of an API that is NOT a Web Service?",
                options=[
                    "The Python `math` module library interface (`math.sqrt`)",
                    "The GitHub REST API over HTTPS",
                    "The Stripe Payments API",
                    "The OpenWeatherMap API"
                ],
                correct_answer="The Python `math` module library interface (`math.sqrt`)",
                explanation="The `math` module is a local in-memory library API; it does not operate over a network."
            ),
            QuizQuestionBlueprint(
                question="What markup language was historically mandatory for traditional Web Services like SOAP?",
                options=["XML", "JSON", "Markdown", "YAML"],
                correct_answer="XML",
                explanation="Traditional SOAP Web Services rely strictly on XML envelopes and schemas."
            ),
            QuizQuestionBlueprint(
                question="What does WSDL stand for in traditional Web Services architecture?",
                options=[
                    "Web Services Description Language",
                    "Wide Server Database Link",
                    "Web System Dynamic Logic",
                    "Wireless Service Domain List"
                ],
                correct_answer="Web Services Description Language",
                explanation="WSDL is an XML-based file describing the methods, parameters, and endpoints of a Web Service."
            ),
            QuizQuestionBlueprint(
                question="Why did the software industry predominantly shift from SOAP Web Services to RESTful APIs?",
                options=[
                    "REST uses lightweight JSON and native HTTP verbs, reducing bandwidth, parsing complexity, and architectural overhead",
                    "SOAP was banned by the W3C",
                    "XML cannot be sent over the internet anymore",
                    "JSON is encrypted by default"
                ],
                correct_answer="REST uses lightweight JSON and native HTTP verbs, reducing bandwidth, parsing complexity, and architectural overhead",
                explanation="REST with JSON is significantly faster, simpler, and less verbose than SOAP with XML."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 3: API Architecture Styles (REST, SOAP, RPC, GraphQL)
    # ----------------------------------------------------
    DayBlueprint(
        order=3,
        title="Day 3: API Architecture Styles (REST, SOAP, RPC, GraphQL)",
        concept="Comparing the four major API architecture paradigms: Resource-oriented REST, Action-oriented RPC/gRPC, Contract-driven SOAP, and Query-driven GraphQL.",
        analogy="Buying food in different ways: SOAP is signing a 10-page legal contract at a bank; REST is ordering items off a fixed diner menu; RPC is calling your chef friend and shouting 'CookBurger(well_done=True)'; GraphQL is building your own custom burger ingredient-by-ingredient on a touch screen.",
        theory_sections=[
            {
                "heading": "The 4 Dominant Architectural Styles",
                "body": (
                    "Different business and system requirements demand different communication patterns:\n"
                    "1. **REST (Representational State Transfer)**: Resource-based, leverages HTTP verbs (GET, POST, PUT, DELETE) on URIs. The web standard.\n"
                    "2. **RPC / gRPC (Remote Procedure Call)**: Action-based. Calls a function on a remote computer as if it were a local function (e.g. `calculateTax(orderId)`). gRPC uses HTTP/2 and Protobuf for ultra-fast microservices.\n"
                    "3. **SOAP (Simple Object Access Protocol)**: Strict, XML-based, highly standardized contract protocol. Common in banking, telecommunications, and legacy enterprises.\n"
                    "4. **GraphQL**: Query language developed by Meta. Allows clients to request exactly the fields they need, eliminating over-fetching and under-fetching."
                )
            },
            {
                "heading": "Resource-Oriented vs Action-Oriented",
                "body": (
                    "- **REST is Resource-Oriented**: Focuses on *things* (nouns): `/users/42`, `/orders`.\n"
                    "- **RPC is Action-Oriented**: Focuses on *verbs/procedures*: `/getUserById`, `/cancelOrder`, `/sendInvoice`."
                )
            },
            {
                "heading": "When to Use What?",
                "body": (
                    "- **REST**: Public APIs, CRUD web apps, standard mobile backends.\n"
                    "- **GraphQL**: Complex frontends with nested relations where bandwidth is critical (mobile apps).\n"
                    "- **gRPC**: Low-latency, internal inter-microservice communication.\n"
                    "- **SOAP**: Strict regulatory financial transactions requiring ACID compliance and WS-Security."
                )
            }
        ],
        code_snippets=[
            {
                "title": "REST Style Request",
                "code": "# REST: HTTP Verb + Noun Resource URL\nGET /api/v1/users/42 HTTP/1.1\nHost: api.example.com\n\n# Server responds with full User resource representation (fixed shape)",
                "explanation": "Resource-oriented interaction with standard HTTP verbs."
            },
            {
                "title": "RPC (Remote Procedure Call) Style Request",
                "code": "# JSON-RPC: Calling a remote method explicitly with parameters\nPOST /rpc HTTP/1.1\nContent-Type: application/json\n\n{\n  \"jsonrpc\": \"2.0\",\n  \"method\": \"calculateUserDiscount\",\n  \"params\": {\"userId\": 42, \"coupon\": \"SUMMER\"},\n  \"id\": 1\n}",
                "explanation": "Action-oriented remote method execution."
            },
            {
                "title": "GraphQL Query Request",
                "code": "# GraphQL: Client requests exact fields desired\nPOST /graphql HTTP/1.1\nContent-Type: application/json\n\n{\n  user(id: 42) {\n    name\n    email\n    orders(limit: 2) {\n      total\n    }\n  }\n}",
                "explanation": "Query-driven specification preventing over-fetching."
            },
            {
                "title": "Style Architecture Decision Matrix",
                "code": "# Style    | Focus    | Transport | Payload  | Best Use Case\n# ---------+----------+-----------+----------+--------------------------\n# REST     | Nouns    | HTTP/1.1  | JSON     | Public Web APIs & CRUD\n# GraphQL  | Queries  | HTTP/1.1  | JSON     | Dynamic Complex Frontends\n# gRPC     | Actions  | HTTP/2    | Protobuf | Internal Microservices\n# SOAP     | Contract | HTTP/SMTP | XML      | Banking & Enterprise Leg",
                "explanation": "Architectural selection guide."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Convert RPC Endpoint to RESTful Endpoint",
            description="Write down the RESTful URL and HTTP method equivalent for the RPC action `POST /api/v1/getAllActiveUsers`.",
            starter_code="# Method: ?\n# URL: ?\n",
            solution_code="# Method: GET\n# URL: /api/v1/users?status=active",
            expected_output="GET /api/v1/users?status=active"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Which API architecture style focuses strictly on 'Resources' (nouns) manipulated via standard HTTP verbs?",
                options=["REST", "RPC", "SOAP", "WebSockets"],
                correct_answer="REST",
                explanation="REST is inherently resource-oriented, using nouns for URLs and HTTP verbs for actions."
            ),
            QuizQuestionBlueprint(
                question="What key architectural advantage does GraphQL provide over standard REST endpoints?",
                options=[
                    "Clients can request the exact fields they need in a single query, preventing over-fetching and under-fetching",
                    "GraphQL does not require a web server",
                    "GraphQL eliminates the need for databases",
                    "GraphQL automatically encrypts all computer files"
                ],
                correct_answer="Clients can request the exact fields they need in a single query, preventing over-fetching and under-fetching",
                explanation="GraphQL solves over-fetching and under-fetching by letting clients specify the exact response shape."
            ),
            QuizQuestionBlueprint(
                question="Which API architecture style is widely chosen for high-performance internal microservices due to its use of HTTP/2 and binary Protocol Buffers (Protobuf)?",
                options=["gRPC", "SOAP", "REST", "JSON-P"],
                correct_answer="gRPC",
                explanation="gRPC offers ultra-low latency and compact binary serialization over HTTP/2."
            ),
            QuizQuestionBlueprint(
                question="An API endpoint formatted as `POST /executeOrderTransfer` is characteristic of which paradigm?",
                options=["RPC (Remote Procedure Call)", "Strict RESTful", "SOAP WSDL", "CSS"],
                correct_answer="RPC (Remote Procedure Call)",
                explanation="Endpoints containing verbs and action names are typical of RPC (Remote Procedure Call)."
            ),
            QuizQuestionBlueprint(
                question="In banking and enterprise financial systems, why is SOAP sometimes still required instead of REST?",
                options=[
                    "Strict WS-Security compliance, built-in ACID transaction support, and formal schema contracts",
                    "SOAP is faster than binary gRPC",
                    "SOAP requires no network bandwidth",
                    "Banks are legally prohibited from using JSON"
                ],
                correct_answer="Strict WS-Security compliance, built-in ACID transaction support, and formal schema contracts",
                explanation="SOAP features mature enterprise specifications for end-to-end security and ACID transactions."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 4: Data Formats: JSON vs XML
    # ----------------------------------------------------
    DayBlueprint(
        order=4,
        title="Day 4: Data Formats: JSON vs XML",
        concept="Comparing serialization data formats in web communications: parsing speed, human readability, schema validation, and payload footprint.",
        analogy="XML is like a government legal document with heavy wax seals and formal boilerplate (`<user><name>John</name></user>`). JSON is like a clean Post-it note with key-value pairs (`{\"name\": \"John\"}`). Both convey the same message, but one uses 5x less paper.",
        theory_sections=[
            {
                "heading": "The Rise of JSON Over XML",
                "body": (
                    "In early web services, **XML (eXtensible Markup Language)** was the undisputed king. "
                    "However, around 2005, Douglas Crockford popularized **JSON (JavaScript Object Notation)**. "
                    "Today, over 95% of public Web APIs default to JSON due to its compactness, simplicity, and native compatibility with JavaScript runtimes."
                )
            },
            {
                "heading": "Anatomy of JSON Data Types",
                "body": (
                    "JSON supports six primitive/composite types:\n"
                    "1. `String`: `\"hello\"`\n"
                    "2. `Number`: `42`, `3.1415`\n"
                    "3. `Boolean`: `true`, `false`\n"
                    "4. `Null`: `null`\n"
                    "5. `Array`: `[1, 2, 3]`\n"
                    "6. `Object`: `{\"key\": \"value\"}`"
                )
            },
            {
                "heading": "When is XML Still Preferred?",
                "body": (
                    "XML has powerful features that JSON lacks: attributes on tags, namespaces (preventing naming collisions), "
                    "and strict schema validation via **XSD (XML Schema Definition)**. "
                    "JSON has since countered with JSON Schema, but XML remains entrenched in legacy and publishing systems."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Same Data Represented in XML vs JSON",
                "code": "# XML (78 bytes, heavy closing tags):\n# <user id=\"101\">\n#    <name>Jane Doe</name>\n#    <role>Admin</role>\n# </user>\n\n# JSON (44 bytes, 43% smaller payload):\n# {\"id\": 101, \"name\": \"Jane Doe\", \"role\": \"Admin\"}",
                "explanation": "Illustrates payload efficiency and readability."
            },
            {
                "title": "Parsing and Serializing JSON in Python",
                "code": "import json\n\n# Python Dictionary to JSON String (Serialization):\nuser_dict = {'id': 101, 'name': 'Jane Doe', 'active': True}\njson_string = json.dumps(user_dict)\nprint(f\"Serialized: {json_string}\")\n\n# JSON String to Python Dictionary (Deserialization):\nparsed_dict = json.loads(json_string)\nprint(f\"User Name: {parsed_dict['name']}\")",
                "explanation": "Using json.dumps and json.loads for serialization and deserialization."
            },
            {
                "title": "Parsing JSON in Modern JavaScript",
                "code": "// JavaScript JSON handling\nconst jsonText = '{\"title\": \"Intro to APIs\", \"views\": 1250}';\n\n// Deserialize:\nconst course = JSON.parse(jsonText);\nconsole.log(course.title); // Output: Intro to APIs\n\n// Serialize:\nconst backToString = JSON.stringify(course);\nconsole.log(backToString);",
                "explanation": "Native browser and Node.js JSON parsing."
            },
            {
                "title": "MIME Types in HTTP Headers",
                "code": "# Requesting JSON data:\n# Accept: application/json\n# Content-Type: application/json\n\n# Requesting XML data:\n# Accept: application/xml\n# Content-Type: application/xml",
                "explanation": "Content-Type and Accept headers communicate the payload serialization format."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Convert Python Dict to Formatted JSON",
            description="Write Python code using the `json` module to serialize dictionary `{'course': 'REST APIs', 'rating': 5}` into a JSON string formatted with an indent of 2 spaces.",
            starter_code="import json\ndata = {'course': 'REST APIs', 'rating': 5}\n# Serialize with indent=2\n",
            solution_code="import json\ndata = {'course': 'REST APIs', 'rating': 5}\nresult = json.dumps(data, indent=2)",
            expected_output="{\n  \"course\": \"REST APIs\",\n  \"rating\": 5\n}"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Why is JSON drastically more popular than XML for modern Web and Mobile APIs?",
                options=[
                    "JSON is smaller in payload size, human-readable, and parses natively into JavaScript objects with zero configuration",
                    "XML was deprecated by the internet registry",
                    "JSON encrypts data automatically",
                    "XML cannot represent numbers"
                ],
                correct_answer="JSON is smaller in payload size, human-readable, and parses natively into JavaScript objects with zero configuration",
                explanation="JSON is lightweight, concise, and maps directly to native programming language data structures."
            ),
            QuizQuestionBlueprint(
                question="What is the official IANA MIME media type for JSON payloads transmitted over HTTP?",
                options=["application/json", "text/json", "data/json", "application/javascript"],
                correct_answer="application/json",
                explanation="The standard MIME type defined in RFC 8259 is `application/json`."
            ),
            QuizQuestionBlueprint(
                question="Which of the following data types is NOT natively supported in the JSON specification?",
                options=["Date / Time object", "Boolean", "Number", "Array"],
                correct_answer="Date / Time object",
                explanation="JSON has no native Date type; dates are transmitted as ISO 8601 formatted strings (e.g. '2026-09-30T12:00:00Z')."
            ),
            QuizQuestionBlueprint(
                question="What does 'Serialization' mean in the context of API data formats?",
                options=[
                    "Converting in-memory data structures (like objects or dictionaries) into a string/byte format (like JSON) for transmission over a network",
                    "Assigning a serial number to a server",
                    "Sorting data alphabetically",
                    "Deleting invalid data rows"
                ],
                correct_answer="Converting in-memory data structures (like objects or dictionaries) into a string/byte format (like JSON) for transmission over a network",
                explanation="Serialization transforms internal program objects into portable text/byte streams."
            ),
            QuizQuestionBlueprint(
                question="What feature gives XML an advantage in specialized regulatory environments over JSON?",
                options=[
                    "Native tag attributes, namespaces, and strict XSD schema validation contracts",
                    "XML files are 90% smaller than JSON",
                    "XML runs without electricity",
                    "XML requires no syntax closing tags"
                ],
                correct_answer="Native tag attributes, namespaces, and strict XSD schema validation contracts",
                explanation="XML supports namespaces, attributes, and formal XSD schema validation."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 5: Synchronous vs Asynchronous APIs
    # ----------------------------------------------------
    DayBlueprint(
        order=5,
        title="Day 5: Synchronous vs Asynchronous APIs",
        concept="Contrasting blocking request-response cycles with non-blocking asynchronous APIs (polling, webhooks, message brokers) for long-running workflows.",
        analogy="Synchronous is ordering fast food at the drive-thru window: you sit in your car blocking the lane until the bag is handed to you. Asynchronous is ordering a custom wedding cake: you place the order, receive a receipt number, go home, and they text you three days later when the cake is ready.",
        theory_sections=[
            {
                "heading": "Synchronous APIs (Blocking Request-Response)",
                "body": (
                    "In a **Synchronous API**, the client sends a request and waits (blocks) until the server completes processing and returns a response. "
                    "This is ideal for immediate operations: fetching user profiles, validating passwords, or reading a single database record (< 200ms)."
                )
            },
            {
                "heading": "The Danger of Long-Running Synchronous Calls",
                "body": (
                    "If an API endpoint triggers video transcoding (taking 5 minutes) or generating a massive 500-page PDF report, "
                    "holding an HTTP connection open causes browser timeouts (504 Gateway Timeout), exhausts server connection threads, "
                    "and ruins user experience."
                )
            },
            {
                "heading": "Asynchronous API Patterns",
                "body": (
                    "1. **202 Accepted + Polling**: Server immediately returns `202 Accepted` with a Job ID and a `Location: /jobs/123` header. The client polls the status periodically.\n"
                    "2. **Webhooks**: Client provides a callback URL (`https://my-app.com/webhook`). The server executes the task in the background and sends an HTTP POST request when complete.\n"
                    "3. **Event-Driven Messaging**: Server enqueues work into Kafka, RabbitMQ, or AWS SQS."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Synchronous Blocking Pattern",
                "code": "# Synchronous: Client thread hangs waiting for server calculation\n# Client -> [HTTP Request] -> Server (Wait 150ms) -> [HTTP 200 OK + Data] -> Client resumes",
                "explanation": "Immediate execution suitable for fast, lightweight transactions."
            },
            {
                "title": "Asynchronous 202 Accepted Response Pattern",
                "code": "# Client initiates heavy video export:\n# POST /api/v1/video/export\n#\n# Server immediately responds in 50ms with 202 Accepted:\n# HTTP/1.1 202 Accepted\n# Location: /api/v1/jobs/vid-9872\n# Content-Type: application/json\n#\n# {\n#   \"job_id\": \"vid-9872\",\n#   \"status\": \"queued\",\n#   \"estimated_time_seconds\": 180\n# }",
                "explanation": "Server returns immediately, freeing up the client."
            },
            {
                "title": "Client Status Polling Implementation",
                "code": "import time\nimport requests\n\ndef poll_job_status(job_id):\n    url = f\"https://api.example.com/api/v1/jobs/{job_id}\"\n    while True:\n        res = requests.get(url).json()\n        if res['status'] == 'completed':\n            print(f\"Download URL: {res['download_url']}\")\n            break\n        elif res['status'] == 'failed':\n            raise Exception(\"Job processing failed\")\n        print(\"Processing... checking again in 5s\")\n        time.sleep(5)",
                "explanation": "Client queries job status periodically until completion."
            },
            {
                "title": "Asynchronous Webhook Alternative",
                "code": "# Client tells server where to notify when done:\nPOST /api/v1/reports/annual HTTP/1.1\nContent-Type: application/json\n\n{\n  \"year\": 2026,\n  \"webhook_url\": \"https://client.com/api/webhooks/reports\"\n}\n\n# Server answers: 202 Accepted\n# 10 minutes later, Server POSTs payload directly to client's webhook_url!",
                "explanation": "Eliminates polling overhead by pushing notification on completion."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Design 202 Accepted Response Handler",
            description="Write a Python Flask endpoint `POST /api/v1/transcode` that simulates enqueueing a video job and returns status code 202 with JSON {'job_id': 'job-101', 'status': 'queued'}.",
            starter_code="from flask import Flask, jsonify\napp = Flask(__name__)\n\n# Implement POST /api/v1/transcode\n",
            solution_code="from flask import Flask, jsonify\napp = Flask(__name__)\n\n@app.route('/api/v1/transcode', methods=['POST'])\ndef transcode():\n    return jsonify({'job_id': 'job-101', 'status': 'queued'}), 202",
            expected_output="{'job_id': 'job-101', 'status': 'queued'}, 202"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What HTTP status code is officially designated for asynchronous requests that have been accepted for processing but are not yet complete?",
                options=["202 Accepted", "200 OK", "204 No Content", "301 Moved Permanently"],
                correct_answer="202 Accepted",
                explanation="HTTP `202 Accepted` indicates the request has been queued for background processing."
            ),
            QuizQuestionBlueprint(
                question="What problem occurs if a client attempts to execute a 10-minute database report using a synchronous HTTP call?",
                options=[
                    "The HTTP connection will likely suffer a 504 Gateway Timeout and tie up server worker threads",
                    "The database will automatically delete the table",
                    "The client's computer monitor will turn off",
                    "The request will automatically convert into a WebSocket"
                ],
                correct_answer="The HTTP connection will likely suffer a 504 Gateway Timeout and tie up server worker threads",
                explanation="Synchronous web connections time out after 30-60 seconds, causing gateway failures."
            ),
            QuizQuestionBlueprint(
                question="In an asynchronous polling pattern, which HTTP response header conventionally tells the client where to check job progress?",
                options=["Location", "Destination", "Redirect", "Next-Url"],
                correct_answer="Location",
                explanation="The `Location` header provides the URI for polling the status of the newly created background job."
            ),
            QuizQuestionBlueprint(
                question="How does a Webhook improve upon client-side polling for long-running background tasks?",
                options=[
                    "The server contacts the client via HTTP POST when the task is done, eliminating wasteful repeated polling requests",
                    "Webhooks run without internet",
                    "Webhooks make video rendering instantaneous",
                    "Webhooks replace the database"
                ],
                correct_answer="The server contacts the client via HTTP POST when the task is done, eliminating wasteful repeated polling requests",
                explanation="Webhooks are event-driven: the server notifies the client directly, saving bandwidth and polling overhead."
            ),
            QuizQuestionBlueprint(
                question="Which scenario is best suited for a Synchronous API rather than an Asynchronous API?",
                options=[
                    "Authenticating a user by username and password during login (< 100ms)",
                    "Rendering a 4K 2-hour movie file",
                    "Training a 100-million parameter Machine Learning model",
                    "Running a monthly payroll batch for 50,000 employees"
                ],
                correct_answer="Authenticating a user by username and password during login (< 100ms)",
                explanation="Low-latency, immediate-feedback transactions should always be synchronous."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 6: How HTTP Works (Request & Response Cycle)
    # ----------------------------------------------------
    DayBlueprint(
        order=6,
        title="Day 6: How HTTP Works (The Request & Response Cycle)",
        concept="Deconstructing the Hypertext Transfer Protocol: DNS resolution, TCP 3-way handshake, TLS termination, HTTP raw message structure, and stateless request-response loops.",
        analogy="HTTP is like formal letter writing. You address an envelope with a destination address, write an opening greeting with instructions (Request Line), include return address and date (Headers), and put a letter inside (Body). The recipient reads it and sends back a response letter with an official status stamp.",
        theory_sections=[
            {
                "heading": "The Life of an HTTP Request",
                "body": (
                    "When a client makes a request to `https://api.example.com/v1/users`, a multi-step sequence occurs:\n"
                    "1. **DNS Lookup**: Resolves hostname `api.example.com` to an IP address (e.g. `93.184.216.34`).\n"
                    "2. **TCP Handshake**: Establishes reliable transport connection via SYN, SYN-ACK, ACK.\n"
                    "3. **TLS Handshake**: Negotiates cryptographic encryption keys for HTTPS (port 443).\n"
                    "4. **HTTP Request Transmission**: Client sends ASCII/binary request stream.\n"
                    "5. **Server Processing**: Server parses request, interacts with databases, and prepares response.\n"
                    "6. **HTTP Response Transmission**: Server streams status code, headers, and payload back to client."
                )
            },
            {
                "heading": "Anatomy of an HTTP Request Message",
                "body": (
                    "```text\n"
                    "POST /api/v1/users HTTP/1.1           <-- Start Line (Method, Path, HTTP Version)\n"
                    "Host: api.example.com                 <-- Headers (Key-Value metadata)\n"
                    "Content-Type: application/json\n"
                    "Content-Length: 35\n"
                    "\n"
                    "{\"name\": \"Alice\", \"role\": \"Engineer\"} <-- Body / Payload\n"
                    "```"
                )
            },
            {
                "heading": "Anatomy of an HTTP Response Message",
                "body": (
                    "```text\n"
                    "HTTP/1.1 201 Created                  <-- Status Line (HTTP Version, Status Code, Reason)\n"
                    "Content-Type: application/json        <-- Response Headers\n"
                    "Date: Wed, 30 Sep 2026 12:00:00 GMT\n"
                    "\n"
                    "{\"id\": 42, \"name\": \"Alice\"}           <-- Response Body\n"
                    "```"
                )
            }
        ],
        code_snippets=[
            {
                "title": "Raw HTTP Socket Request via Telnet / Netcat",
                "code": "# Manually speaking raw HTTP/1.1 over a TCP socket connection:\n# nc api.github.com 80\n\nGET /users/octocat HTTP/1.1\r\nHost: api.github.com\r\nUser-Agent: RawSocketClient\r\nConnection: close\r\n\r\n",
                "explanation": "Illustrates that HTTP is plain text protocol over a TCP stream."
            },
            {
                "title": "Inspecting Raw HTTP Headers with cURL Verbose Mode",
                "code": "# Print entire request and response headers using -v flag:\ncurl -v https://httpbin.org/get\n\n# > GET /get HTTP/2\n# > Host: httpbin.org\n# > User-Agent: curl/8.4.0\n# < HTTP/2 200 \n# < date: Wed, 30 Sep 2026 12:00:00 GMT\n# < content-type: application/json",
                "explanation": "cURL verbose mode reveals underlying HTTP wire protocol exchange."
            },
            {
                "title": "HTTP/1.1 vs HTTP/2 vs HTTP/3",
                "code": "# HTTP/1.1: Plain text, Head-of-Line blocking, 1 request per TCP connection\n# HTTP/2:   Binary framing, multiplexing (many requests on 1 TCP connection), header compression (HPACK)\n# HTTP/3:   Runs over UDP using QUIC protocol, eliminates TCP head-of-line blocking",
                "explanation": "Generational evolution of HTTP protocol layers."
            },
            {
                "title": "Simple Python HTTP Server",
                "code": "from http.server import HTTPServer, BaseHTTPRequestHandler\n\nclass SimpleAPI(BaseHTTPRequestHandler):\n    def do_GET(self):\n        self.send_response(200)\n        self.send_header('Content-Type', 'text/plain')\n        self.end_headers()\n        self.wfile.write(b\"Hello from raw HTTP server!\")\n\n# server = HTTPServer(('localhost', 8080), SimpleAPI)\n# server.serve_forever()",
                "explanation": "Low-level Python handling of HTTP request/response stream."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Formulate Raw HTTP Request String",
            description="Write a multiline string representing a valid raw HTTP/1.1 GET request to host 'api.dev.io' for path '/status'. Remember the mandatory empty line at the end.",
            starter_code="raw_http_request = (\n    # Write raw HTTP request lines\n)\n",
            solution_code="raw_http_request = \"GET /status HTTP/1.1\\r\\nHost: api.dev.io\\r\\n\\r\\n\"",
            expected_output="GET /status HTTP/1.1\\r\\nHost: api.dev.io\\r\\n\\r\\n"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What transport layer protocol forms the underlying connection for standard HTTP/1.1 and HTTP/2?",
                options=["TCP (Transmission Control Protocol)", "UDP", "ICMP", "ARP"],
                correct_answer="TCP (Transmission Control Protocol)",
                explanation="HTTP/1.1 and HTTP/2 rely on reliable TCP socket connections."
            ),
            QuizQuestionBlueprint(
                question="What separates the HTTP header section from the HTTP body payload in a raw message?",
                options=[
                    "An empty line (two consecutive Carriage-Return Line-Feed `\\r\\n` characters)",
                    "A row of dashes `---`",
                    "An XML tag `<body-start>`",
                    "A semicolon `;`"
                ],
                correct_answer="An empty line (two consecutive Carriage-Return Line-Feed `\\r\\n` characters)",
                explanation="The HTTP specification dictates that headers end and the body begins after a blank CRLF line."
            ),
            QuizQuestionBlueprint(
                question="Which header is MANDATORY in all HTTP/1.1 requests to enable virtual hosting?",
                options=["Host", "User-Agent", "Accept", "Content-Type"],
                correct_answer="Host",
                explanation="RFC 2616 requires the `Host` header so servers hosting multiple domains know which site is requested."
            ),
            QuizQuestionBlueprint(
                question="What major advancement did HTTP/2 introduce over HTTP/1.1?",
                options=[
                    "Binary multiplexing: transmitting multiple concurrent requests/responses over a single TCP connection",
                    "Removal of status codes",
                    "Replacing JSON with XML",
                    "Requiring dial-up modems"
                ],
                correct_answer="Binary multiplexing: transmitting multiple concurrent requests/responses over a single TCP connection",
                explanation="HTTP/2 multiplexes concurrent request streams over a single connection, eliminating head-of-line blocking."
            ),
            QuizQuestionBlueprint(
                question="What does it mean that HTTP is fundamentally a 'stateless' protocol?",
                options=[
                    "The server does not retain client session data between individual requests; every request must carry all context needed to be fulfilled",
                    "HTTP servers cannot connect to databases",
                    "HTTP does not work outside the United States",
                    "HTTP connections are permanently open forever"
                ],
                correct_answer="The server does not retain client session data between individual requests; every request must carry all context needed to be fulfilled",
                explanation="Statelessness means each request is processed in complete isolation without server-side memory of prior requests."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 7: HTTP Methods / Verbs (GET, POST, PUT, PATCH, DELETE, OPTIONS)
    # ----------------------------------------------------
    DayBlueprint(
        order=7,
        title="Day 7: HTTP Methods / Verbs (GET, POST, PUT, PATCH, DELETE, OPTIONS)",
        concept="Mastering semantic HTTP verbs: safe vs unsafe methods, full replacement (PUT) vs partial update (PATCH), and pre-flight CORS negotiation (OPTIONS).",
        analogy="HTTP verbs are like grammar verbs in language: GET is 'read the book', POST is 'publish a new book', PUT is 'replace the entire book with a new edition', PATCH is 'fix the typo on page 5', and DELETE is 'throw the book in the shredder'.",
        theory_sections=[
            {
                "heading": "Semantic Meaning of Primary Verbs",
                "body": (
                    "Using correct HTTP verbs is the hallmark of professional API design:\n"
                    "- `GET`: Retrieve representation of a resource. Must be read-only and safe (no side effects).\n"
                    "- `POST`: Create a new subordinate resource, or trigger a non-idempotent action.\n"
                    "- `PUT`: Completely replace an existing resource with the provided payload (or create if absent).\n"
                    "- `PATCH`: Apply partial modifications to a resource (updates only provided fields).\n"
                    "- `DELETE`: Remove the specified resource permanently.\n"
                    "- `OPTIONS`: Query which HTTP methods and headers the server supports (critical for CORS)."
                )
            },
            {
                "heading": "PUT vs PATCH (The Classic Interview Question)",
                "body": (
                    "Imagine a user record: `{\"name\": \"Alice\", \"email\": \"alice@dev.io\", \"age\": 30}`.\n"
                    "- If you send `PATCH /users/1` with `{\"age\": 31}`, the server only updates `age`; name and email remain untouched.\n"
                    "- If you send `PUT /users/1` with `{\"age\": 31}`, the server **replaces the entire record**! Name and email will become null/blank unless provided!"
                )
            },
            {
                "heading": "Safe vs Unsafe Methods",
                "body": (
                    "An HTTP method is **Safe** if it does not alter server state. `GET`, `HEAD`, and `OPTIONS` are safe. "
                    "`POST`, `PUT`, `PATCH`, and `DELETE` are unsafe because they modify persistent data."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Mapping CRUD Operations to HTTP Verbs",
                "code": "# CRUD Operation | HTTP Verb | Target Endpoint         | Expected Status\n# ---------------+-----------+-------------------------+----------------\n# Create         | POST      | /api/v1/products        | 201 Created\n# Read (List)    | GET       | /api/v1/products        | 200 OK\n# Read (Single)  | GET       | /api/v1/products/42     | 200 OK\n# Replace (All)  | PUT       | /api/v1/products/42     | 200 OK\n# Update (Part)  | PATCH     | /api/v1/products/42     | 200 OK\n# Delete         | DELETE    | /api/v1/products/42     | 204 No Content",
                "explanation": "Standard RESTful verb and endpoint conventions."
            },
            {
                "title": "FastAPI Implementation of Multiple Verbs",
                "code": "from fastapi import FastAPI, status\nfrom pydantic import BaseModel\n\napp = FastAPI()\n\nclass ItemUpdate(BaseModel):\n    price: float | None = None\n    name: str | None = None\n\n@app.patch(\"/items/{item_id}\")\ndef update_partial_item(item_id: int, item: ItemUpdate):\n    # Only update fields that were provided in request\n    return {\"msg\": f\"Item {item_id} patched\", \"updates\": item.model_dump(exclude_unset=True)}",
                "explanation": "FastAPI PATCH endpoint selectively updating provided fields."
            },
            {
                "title": "Testing OPTIONS Pre-flight via cURL",
                "code": "# Query allowed methods on an endpoint:\ncurl -X OPTIONS https://api.example.com/api/v1/users -i\n\n# Response Header:\n# Allow: GET, POST, HEAD, OPTIONS",
                "explanation": "OPTIONS queries server capabilities."
            },
            {
                "title": "The HEAD Method (Headers Only)",
                "code": "# Fetch ONLY the headers without downloading the body payload:\ncurl -I https://api.github.com\n\n# Useful for checking file size (Content-Length) or cache validity (ETag)",
                "explanation": "HEAD mirrors GET but omits response body payload."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Implement DELETE Handler in Flask",
            description="Write a Flask endpoint for `DELETE /api/v1/users/<int:user_id>` that returns an empty body with status code 204 No Content.",
            starter_code="from flask import Flask\napp = Flask(__name__)\n\n# Implement DELETE endpoint\n",
            solution_code="from flask import Flask\napp = Flask(__name__)\n\n@app.route('/api/v1/users/<int:user_id>', methods=['DELETE'])\ndef delete_user(user_id):\n    # In production: delete from DB\n    return ('', 204)",
            expected_output="('', 204)"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the critical technical distinction between the `PUT` and `PATCH` methods in REST APIs?",
                options=[
                    "`PUT` completely replaces the target resource representation; `PATCH` applies partial modifications to specific fields",
                    "`PUT` creates databases; `PATCH` deletes them",
                    "`PATCH` is read-only; `PUT` is write-only",
                    "There is no difference; they are aliases for each other"
                ],
                correct_answer="`PUT` completely replaces the target resource representation; `PATCH` applies partial modifications to specific fields",
                explanation="PUT represents complete replacement; PATCH represents partial delta modification."
            ),
            QuizQuestionBlueprint(
                question="Which of the following HTTP methods is defined as 'Safe' (meaning it must never alter server state)?",
                options=["GET", "POST", "DELETE", "PATCH"],
                correct_answer="GET",
                explanation="GET is defined as Safe because calling it does not alter persistent server data."
            ),
            QuizQuestionBlueprint(
                question="What is the primary role of the `OPTIONS` HTTP method in web browser security?",
                options=[
                    "It acts as a CORS pre-flight check to ask the server which HTTP methods and headers are permitted before sending an unsafe request",
                    "It options out of database backups",
                    "It downloads optional software updates",
                    "It deletes optional user accounts"
                ],
                correct_answer="It acts as a CORS pre-flight check to ask the server which HTTP methods and headers are permitted before sending an unsafe request",
                explanation="Browsers send pre-flight OPTIONS requests to check cross-origin permissions."
            ),
            QuizQuestionBlueprint(
                question="Which HTTP verb should be used when a user clicks 'Log In' and submits credentials to receive a session token?",
                options=["POST", "GET", "HEAD", "TRACE"],
                correct_answer="POST",
                explanation="Credentials should never be sent via GET (which leaks passwords in URL parameters and server logs); POST transmits credentials securely in the body."
            ),
            QuizQuestionBlueprint(
                question="What standard HTTP status code should be returned after successfully deleting a resource via `DELETE` when no content is returned?",
                options=["204 No Content", "200 OK", "404 Not Found", "301 Redirect"],
                correct_answer="204 No Content",
                explanation="`204 No Content` indicates successful execution with an empty response payload."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 8: HTTP Status Codes: 1xx & 2xx Success (200, 201, 204)
    # ----------------------------------------------------
    DayBlueprint(
        order=8,
        title="Day 8: HTTP Status Codes: 1xx & 2xx Success (200, 201, 204)",
        concept="Mastering informational protocols (1xx) and standard success status codes (2xx): 200 OK, 201 Created with Location header, 202 Accepted, and 204 No Content.",
        analogy="Status codes are like universal hand gestures on a construction site. A 200 is a thumbs-up ('Got it, here is the tool'). A 201 is pointing to a newly erected wall ('Tool built from scratch and standing right there'). A 204 is an empty nod ('Task completed, nothing more to say').",
        theory_sections=[
            {
                "heading": "The Hierarchy of HTTP Status Codes",
                "body": (
                    "HTTP status codes are 3-digit integers categorized into five classes by their first digit:\n"
                    "- `1xx`: Informational (Request received, continuing process).\n"
                    "- `2xx`: Success (The action was successfully received, understood, and accepted).\n"
                    "- `3xx`: Redirection (Further action must be taken to complete request).\n"
                    "- `4xx`: Client Error (Request contains bad syntax or cannot be fulfilled).\n"
                    "- `5xx`: Server Error (The server failed to fulfill an apparently valid request)."
                )
            },
            {
                "heading": "The Core 2xx Success Codes",
                "body": (
                    "1. `200 OK`: Standard response for successful `GET`, `PUT`, or `PATCH` requests returning data.\n"
                    "2. `201 Created`: The request succeeded and led to the creation of a new resource (standard for `POST`). "
                    "Best practice: Include a `Location` header pointing to the URI of the newly created resource!\n"
                    "3. `202 Accepted`: Request accepted for background/asynchronous processing.\n"
                    "4. `204 No Content`: Action succeeded, but the response intentionally contains no body (common for `DELETE`)."
                )
            },
            {
                "heading": "1xx Informational Codes",
                "body": (
                    "- `100 Continue`: Initial headers received; client should proceed to send request body.\n"
                    "- `101 Switching Protocols`: Server agrees to switch protocols (used when upgrading an HTTP connection to a WebSocket!)."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Returning 201 Created with Location Header",
                "code": "from flask import Flask, request, jsonify\n\napp = Flask(__name__)\n\n@app.route('/api/v1/articles', methods=['POST'])\ndef create_article():\n    data = request.json\n    new_id = 842\n    response = jsonify({'id': new_id, 'title': data['title']})\n    # Set 201 Created status and Location header pointing to new resource:\n    return response, 201, {'Location': f'/api/v1/articles/{new_id}'}",
                "explanation": "Professional REST API practice: returning 201 with Location header."
            },
            {
                "title": "WebSocket Upgrade Protocol (101 Switching Protocols)",
                "code": "# Client initiates WebSocket handshake:\n# GET /chat HTTP/1.1\n# Upgrade: websocket\n# Connection: Upgrade\n\n# Server responds with 101 Switching Protocols:\n# HTTP/1.1 101 Switching Protocols\n# Upgrade: websocket\n# Connection: Upgrade",
                "explanation": "101 tells the client the socket connection is transitioning to WebSockets."
            },
            {
                "title": "Returning 204 No Content for DELETE",
                "code": "@app.route('/api/v1/articles/<int:article_id>', methods=['DELETE'])\ndef delete_article(article_id):\n    # DB deletion logic here...\n    return '', 204",
                "explanation": "204 signifies successful deletion without response payload."
            },
            {
                "title": "Summary of Core 2xx Status Codes",
                "code": "# Code | Name        | Standard Verb | Payload Present?\n# -----+-------------+---------------+-----------------\n# 200  | OK          | GET, PUT      | Yes\n# 201  | Created     | POST          | Yes (with Location header)\n# 202  | Accepted    | POST (Async)  | Yes (Job details)\n# 204  | No Content  | DELETE        | Strictly No",
                "explanation": "Quick reference for 2xx status codes."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Create Article with 201 and Location Header",
            description="Write a Python Flask endpoint `POST /api/v1/books` that returns `{'id': 1, 'title': 'Clean Code'}`, status code 201, and header `Location: /api/v1/books/1`.",
            starter_code="from flask import Flask, jsonify\napp = Flask(__name__)\n\n# Implement POST /api/v1/books\n",
            solution_code="from flask import Flask, jsonify\napp = Flask(__name__)\n\n@app.route('/api/v1/books', methods=['POST'])\ndef add_book():\n    return jsonify({'id': 1, 'title': 'Clean Code'}), 201, {'Location': '/api/v1/books/1'}",
            expected_output="{'id': 1, 'title': 'Clean Code'}, 201, Location: /api/v1/books/1"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Which HTTP status code should be returned when a new resource is successfully generated in the database via a `POST` request?",
                options=["201 Created", "200 OK", "204 No Content", "101 Switching Protocols"],
                correct_answer="201 Created",
                explanation="`201 Created` is the standard status code indicating a new resource was created."
            ),
            QuizQuestionBlueprint(
                question="What HTTP header should accompany a `201 Created` response to tell the client where to find the newly created resource?",
                options=["Location", "Destination", "Resource-URI", "Link-To"],
                correct_answer="Location",
                explanation="The `Location` header provides the direct URL of the newly created resource."
            ),
            QuizQuestionBlueprint(
                question="What distinguishes a `204 No Content` response from a `200 OK` response?",
                options=[
                    "`204 No Content` guarantees that the response body payload is completely empty",
                    "`204 No Content` indicates an error occurred",
                    "`204 No Content` deletes the client's cookies",
                    "`204 No Content` can only be sent on mobile phones"
                ],
                correct_answer="`204 No Content` guarantees that the response body payload is completely empty",
                explanation="`204` signifies success while explicitly stating no body content is returned."
            ),
            QuizQuestionBlueprint(
                question="Which 1xx status code is sent by a server to agree to upgrade an HTTP connection to a WebSocket connection?",
                options=["101 Switching Protocols", "100 Continue", "102 Processing", "200 OK"],
                correct_answer="101 Switching Protocols",
                explanation="`101 Switching Protocols` transitions client and server from HTTP to WebSockets."
            ),
            QuizQuestionBlueprint(
                question="If an API endpoint successfully updates a user profile via `PUT` and returns the updated JSON object, which status code is most appropriate?",
                options=["200 OK", "201 Created", "204 No Content", "100 Continue"],
                correct_answer="200 OK",
                explanation="`200 OK` represents successful retrieval or update when returning a response body."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 9: HTTP Status Codes: 3xx Redirection (301, 302, 304, 307)
    # ----------------------------------------------------
    DayBlueprint(
        order=9,
        title="Day 9: HTTP Status Codes: 3xx Redirection (301, 302, 304, 307)",
        concept="Understanding redirection flows: permanent relocations (301/308), temporary redirects (302/307), and web caching validation with 304 Not Modified.",
        analogy="A 301 redirect is permanently forwarding your mail when you buy a new house: the post office updates its permanent records. A 302 is forwarding mail while staying at a hotel for the weekend. A 304 is calling your mom and asking 'Did the family recipe change?', she says 'No', and you keep cooking with your existing recipe without sending a new one in the mail.",
        theory_sections=[
            {
                "heading": "Why Redirection Matters in APIs",
                "body": (
                    "When APIs evolve, endpoints get renamed, domain migrations occur, or SSL certificates are enforced (`http://` to `https://`). "
                    "3xx status codes instruct user agents, mobile apps, and search engines where to find the resource, accompanied by a `Location` header."
                )
            },
            {
                "heading": "Permanent vs Temporary Redirects",
                "body": (
                    "- `301 Moved Permanently`: The requested resource has definitively moved to the URL in `Location`. Browsers and SEO crawlers cache this aggressively.\n"
                    "- `302 Found` (Historically Temporary Redirect): Tells client to look at URL in `Location` temporarily. Flaw: historically, browsers rewrote POST to GET during 302!\n"
                    "- `307 Temporary Redirect`: Strictly guarantees that the **HTTP method will NOT change** (a POST remains a POST).\n"
                    "- `308 Permanent Redirect`: Permanent version of 307 (guarantees method remains unchanged)."
                )
            },
            {
                "heading": "The Powerhouse of Web Performance: 304 Not Modified",
                "body": (
                    "`304 Not Modified` is not a redirect to a different URL—it is a redirect to the **client's own local cache**! "
                    "When a client requests a resource with an `If-None-Match: \"etag-xyz\"` or `If-Modified-Since` header, "
                    "if the data hasn't changed, the server returns `304 Not Modified` with **zero body**. "
                    "This saves gigabytes of redundant database queries and network bandwidth worldwide."
                )
            }
        ],
        code_snippets=[
            {
                "title": "301 Permanent Redirect Response",
                "code": "# Client requests old endpoint:\n# GET /api/v1/old-users HTTP/1.1\n\n# Server responds with permanent move:\n# HTTP/1.1 301 Moved Permanently\n# Location: https://api.example.com/api/v2/users",
                "explanation": "Directs client and crawler to new permanent URI."
            },
            {
                "title": "Conditional GET and 304 Not Modified Handling",
                "code": "from flask import Flask, request, Response\n\napp = Flask(__name__)\n\nCURRENT_ETAG = '\"v1.4.2-asset\"'\n\n@app.route('/api/v1/app-config')\ndef get_config():\n    client_etag = request.headers.get('If-None-Match')\n    if client_etag == CURRENT_ETAG:\n        # Data hasn't changed! Send zero payload:\n        return Response(status=304)\n    \n    # Data changed or first visit: Send 200 OK + ETag\n    res = Response('{\"theme\": \"dark\", \"features\": [\"chat\"]}', status=200)\n    res.headers['ETag'] = CURRENT_ETAG\n    res.headers['Content-Type'] = 'application/json'\n    return res",
                "explanation": "Implements conditional caching using ETag and 304 Not Modified."
            },
            {
                "title": "Preserving POST Payloads with 307 Temporary Redirect",
                "code": "# If you redirect a POST request with 302, browsers might convert to GET.\n# Use 307 to guarantee the POST body is resent to new location:\n# HTTP/1.1 307 Temporary Redirect\n# Location: https://eu-api.example.com/api/v1/orders",
                "explanation": "Guarantees verb preservation across redirects."
            },
            {
                "title": "3xx Redirection Reference Table",
                "code": "# Code | Name                 | Duration  | Method Preserved?\n# -----+----------------------+-----------+------------------\n# 301  | Moved Permanently    | Permanent | May change to GET\n# 302  | Found                | Temporary | May change to GET\n# 304  | Not Modified         | Cache Hit | N/A (Zero Body)\n# 307  | Temporary Redirect   | Temporary | Strictly YES\n# 308  | Permanent Redirect   | Permanent | Strictly YES",
                "explanation": "Comparison of HTTP redirection behaviors."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Implement 304 Conditional Cache Check",
            description="Write a Python Flask endpoint `/api/version` that checks if the request header `If-None-Match` equals '\"1.0\"'. If so, return status 304. Otherwise, return '1.0' with status 200 and ETag '\"1.0\"'.",
            starter_code="from flask import Flask, request, Response\napp = Flask(__name__)\n\n# Implement conditional caching\n",
            solution_code="from flask import Flask, request, Response\napp = Flask(__name__)\n\n@app.route('/api/version')\ndef version():\n    if request.headers.get('If-None-Match') == '\"1.0\"':\n        return Response(status=304)\n    res = Response('1.0', status=200)\n    res.headers['ETag'] = '\"1.0\"'\n    return res",
            expected_output="304 on cache hit, 200 on cache miss"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What does an HTTP `304 Not Modified` status code communicate to the client?",
                options=[
                    "The resource has not changed since the client's last visit; the client should load its local cached copy with zero body transferred",
                    "The client's account has been suspended",
                    "The server database is corrupted",
                    "The resource has been deleted"
                ],
                correct_answer="The resource has not changed since the client's last visit; the client should load its local cached copy with zero body transferred",
                explanation="304 signals a cache hit, instructing the client to use its cached asset."
            ),
            QuizQuestionBlueprint(
                question="Which header does a client send to initiate a conditional cache check using an ETag?",
                options=["If-None-Match", "Check-Cache", "ETag-Verify", "If-Different"],
                correct_answer="If-None-Match",
                explanation="Clients pass their cached ETag hash in the `If-None-Match` header."
            ),
            QuizQuestionBlueprint(
                question="Why was HTTP `307 Temporary Redirect` introduced to supplement `302 Found`?",
                options=[
                    "To guarantee that the client does NOT change the HTTP method (a POST remains a POST across the redirect)",
                    "To speed up video streaming",
                    "To make redirection permanent",
                    "To encrypt the destination URL"
                ],
                correct_answer="To guarantee that the client does NOT change the HTTP method (a POST remains a POST across the redirect)",
                explanation="307 guarantees that the HTTP request method and body are preserved across redirection."
            ),
            QuizQuestionBlueprint(
                question="Which status code instructs search engines and clients that an API route has PERMANENTLY moved to a new URL?",
                options=["301 Moved Permanently", "302 Found", "304 Not Modified", "200 OK"],
                correct_answer="301 Moved Permanently",
                explanation="301 indicates permanent migration, causing search engines and caches to update indexes."
            ),
            QuizQuestionBlueprint(
                question="Which header contains the destination URL that the client must redirect to in a 3xx response?",
                options=["Location", "Destination", "Redirect-To", "Host"],
                correct_answer="Location",
                explanation="The `Location` header specifies the target URL of the redirection."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 10: HTTP Status Codes: 4xx Client Errors & 5xx Server Errors
    # ----------------------------------------------------
    DayBlueprint(
        order=10,
        title="Day 10: HTTP Status Codes: 4xx Client Errors & 5xx Server Errors",
        concept="Diagnosing failure states: distinguishing client-side mistakes (4xx) from backend server failures (5xx): 400, 401, 403, 404, 429, 500, 502, 503.",
        analogy="A 4xx error is trying to enter a movie theater with an expired ticket or bad money: YOU made the mistake (Client Error). A 5xx error is having a valid ticket, walking up to the screen, and seeing the movie projector explode in flames: the THEATER failed (Server Error).",
        theory_sections=[
            {
                "heading": "4xx: Client Error Status Codes",
                "body": (
                    "4xx status codes indicate the client did something wrong:\n"
                    "- `400 Bad Request`: Malformed syntax, invalid JSON, or failed input validation.\n"
                    "- `401 Unauthorized`: **Lacks authentication**. Client did not provide credentials, or the token is expired/invalid.\n"
                    "- `403 Forbidden`: **Lacks permission**. The server knows who you are, but you do not have permission to access this resource.\n"
                    "- `404 Not Found`: The requested URI does not exist on the server.\n"
                    "- `405 Method Not Allowed`: E.g. sending a `POST` to a route that only supports `GET`.\n"
                    "- `429 Too Many Requests`: Client exceeded rate limits (throttled)."
                )
            },
            {
                "heading": "5xx: Server Error Status Codes",
                "body": (
                    "5xx status codes indicate the server encountered an unexpected condition:\n"
                    "- `500 Internal Server Error`: Unhandled exception or crash in backend code.\n"
                    "- `502 Bad Gateway`: An API gateway or reverse proxy (NGINX) received an invalid response from upstream application server.\n"
                    "- `503 Service Unavailable`: Server is temporarily overloaded or undergoing maintenance.\n"
                    "- `504 Gateway Timeout`: The upstream server took too long to respond to the gateway."
                )
            },
            {
                "heading": "401 Unauthorized vs 403 Forbidden",
                "body": (
                    "A frequent point of confusion:\n"
                    "- **401 Unauthorized = 'Who are you?'** (Authentication failure).\n"
                    "- **403 Forbidden = 'I know who you are, but you cannot touch this!'** (Authorization/RBAC failure)."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Handling 400 Bad Request with Detailed Validation Errors",
                "code": "from flask import Flask, request, jsonify\n\napp = Flask(__name__)\n\n@app.route('/api/v1/register', methods=['POST'])\ndef register():\n    data = request.get_json(silent=True)\n    if not data or 'email' not in data:\n        # Return 400 Bad Request with actionable context:\n        return jsonify({\n            'error': 'Bad Request',\n            'message': \"Missing required field 'email'\"\n        }), 400\n    return jsonify({'status': 'registered'}), 201",
                "explanation": "Informative 400 error payload guiding the client to fix input."
            },
            {
                "title": "401 vs 403 Authentication vs Authorization Logic",
                "code": "@app.route('/api/v1/admin/dashboard')\ndef admin_dashboard():\n    token = request.headers.get('Authorization')\n    if not token:\n        # 401: You haven't proven who you are\n        return jsonify({'error': 'Authentication required'}), 401\n    \n    user = verify_jwt(token)\n    if user.role != 'SUPER_ADMIN':\n        # 403: We know who you are, but you are not allowed\n        return jsonify({'error': 'Insufficient permissions'}), 403\n        \n    return jsonify({'metrics': 'classified'})",
                "explanation": "Clear separation between 401 authentication and 403 authorization."
            },
            {
                "title": "Handling 429 Rate Limiting with Retry-After",
                "code": "# Server throttling a greedy client:\n# HTTP/1.1 429 Too Many Requests\n# Retry-After: 60\n# Content-Type: application/json\n#\n# {\n#   \"error\": \"Rate limit exceeded\",\n#   \"message\": \"You can only make 100 requests per minute. Try again in 60s.\"\n# }",
                "explanation": "429 informing client how long to wait before retrying."
            },
            {
                "title": "Proxy 502 vs 504 Architecture Flow",
                "code": "# Client <---> [NGINX Reverse Proxy] <---X---> [Flask App Server]\n# If Flask crashes / closes socket  --> NGINX returns 502 Bad Gateway\n# If Flask takes > 60s to respond   --> NGINX returns 504 Gateway Timeout",
                "explanation": "Illustrates how reverse proxies generate 502 vs 504 errors."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Implement Rate Limiting 429 Response",
            description="Write a Flask endpoint `/api/search` that returns a 429 Too Many Requests response with header `Retry-After: 30` and JSON `{'error': 'Throttled'}`.",
            starter_code="from flask import Flask, jsonify\napp = Flask(__name__)\n\n# Implement 429 handler\n",
            solution_code="from flask import Flask, jsonify\napp = Flask(__name__)\n\n@app.route('/api/search')\ndef search():\n    return jsonify({'error': 'Throttled'}), 429, {'Retry-After': '30'}",
            expected_output="{'error': 'Throttled'}, 429, Retry-After: 30"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the precise difference between HTTP `401 Unauthorized` and `403 Forbidden`?",
                options=[
                    "`401` means authentication is missing or invalid ('Who are you?'); `403` means identity is known but access is refused due to insufficient permissions",
                    "`401` is a server crash; `403` is a network disconnect",
                    "`401` is for desktop computers; `403` is for mobile phones",
                    "They mean the exact same thing"
                ],
                correct_answer="`401` means authentication is missing or invalid ('Who are you?'); `403` means identity is known but access is refused due to insufficient permissions",
                explanation="401 relates to authentication (credentials); 403 relates to authorization (permissions)."
            ),
            QuizQuestionBlueprint(
                question="Which status code should an API return when a client exceeds their allocated request rate quota?",
                options=["429 Too Many Requests", "400 Bad Request", "503 Service Unavailable", "418 I'm a teapot"],
                correct_answer="429 Too Many Requests",
                explanation="`429 Too Many Requests` is designated for rate limiting and throttling."
            ),
            QuizQuestionBlueprint(
                question="What does an HTTP `502 Bad Gateway` error mean when connecting through a reverse proxy like NGINX?",
                options=[
                    "The proxy server attempted to contact the backend application server (e.g. Node/Python), but received an invalid or closed socket response",
                    "The client's internet cable is unplugged",
                    "The user entered the wrong password",
                    "The database has run out of disk space"
                ],
                correct_answer="The proxy server attempted to contact the backend application server (e.g. Node/Python), but received an invalid or closed socket response",
                explanation="502 indicates a gateway/proxy received an invalid response from upstream servers."
            ),
            QuizQuestionBlueprint(
                question="If a client sends an HTTP `POST` request to an endpoint that only accepts `GET`, what status code should be returned?",
                options=["405 Method Not Allowed", "404 Not Found", "400 Bad Request", "501 Not Implemented"],
                correct_answer="405 Method Not Allowed",
                explanation="`405 Method Not Allowed` indicates the target resource exists, but the HTTP verb is forbidden."
            ),
            QuizQuestionBlueprint(
                question="Which status code indicates an unhandled syntax exception or unexpected crash inside the backend application code?",
                options=["500 Internal Server Error", "400 Bad Request", "404 Not Found", "502 Bad Gateway"],
                correct_answer="500 Internal Server Error",
                explanation="500 indicates unexpected backend failure or unhandled exception."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 11: HTTP Headers (Request, Response, Custom Headers)
    # ----------------------------------------------------
    DayBlueprint(
        order=11,
        title="Day 11: HTTP Headers (Request, Response, Custom Headers)",
        concept="Mastering HTTP headers: content negotiation (`Content-Type`, `Accept`), authorization (`Bearer`), caching controls, and custom metadata (`X-*`).",
        analogy="HTTP headers are like metadata stamps on shipping crates. The crate payload contains the actual merchandise (the body), but the headers tell the dock workers: 'Fragile (Content-Type)', 'Security Clearance Level 5 (Authorization)', and 'Keep Refrigerated Until October (Cache-Control)'.",
        theory_sections=[
            {
                "heading": "The Purpose of HTTP Headers",
                "body": (
                    "HTTP headers are case-insensitive key-value pairs separated by a colon (`:`). "
                    "They allow clients and servers to pass metadata about the request or response, including authentication tokens, "
                    "payload encodings, caching directives, and security constraints."
                )
            },
            {
                "heading": "Essential Request Headers",
                "body": (
                    "- `Authorization`: Carries credentials (e.g. `Bearer <jwt_token>` or `Basic <base64>`).\n"
                    "- `Accept`: Informs server which media types the client can understand (`application/json`).\n"
                    "- `Content-Type`: Tells the server the media format of the request payload.\n"
                    "- `User-Agent`: Identifies the client software/library (e.g. Chrome, Axios, Postman)."
                )
            },
            {
                "heading": "Content-Type vs Accept (Content Negotiation)",
                "body": (
                    "- `Content-Type` is about **WHAT I AM SENDING YOU**.\n"
                    "- `Accept` is about **WHAT I WANT YOU TO SEND ME BACK**."
                )
            },
            {
                "heading": "Custom and Modern Headers",
                "body": (
                    "Historically, custom proprietary headers began with `X-` (e.g., `X-Request-ID`, `X-RateLimit-Remaining`). "
                    "RFC 6648 officially deprecated the `X-` prefix, encouraging standard descriptive names (e.g., `RateLimit-Limit`)."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Reading and Setting Headers in Express.js",
                "code": "const express = require('express');\nconst app = express();\n\napp.get('/api/v1/profile', (req, res) => {\n    // Reading incoming request header:\n    const authHeader = req.headers['authorization'];\n    \n    // Setting outgoing response headers:\n    res.setHeader('Cache-Control', 'max-age=3600, public');\n    res.setHeader('X-Request-ID', 'req-98234-abc');\n    \n    res.json({ name: 'Alice', role: 'Developer' });\n});",
                "explanation": "Inspecting and dispatching HTTP headers in Node.js Express."
            },
            {
                "title": "Passing Headers in Python Requests",
                "code": "import requests\n\nheaders = {\n    'Authorization': 'Bearer my_secret_token_123',\n    'Accept': 'application/json',\n    'X-Client-Version': '2.4.0'\n}\n\nresponse = requests.get('https://api.example.com/data', headers=headers)\nprint(response.headers.get('Content-Type'))",
                "explanation": "Passing authorization and custom headers via Python."
            },
            {
                "title": "Common Security Response Headers",
                "code": "# Headers protecting against common web attacks:\n# Strict-Transport-Security: max-age=31536000; includeSubDomains\n# X-Content-Type-Options: nosniff\n# X-Frame-Options: DENY\n# Content-Security-Policy: default-src 'self'",
                "explanation": "Critical security headers hardening web servers."
            },
            {
                "title": "Inspecting Headers with cURL",
                "code": "# Fetch ONLY the headers (-I / --head):\ncurl -I https://httpbin.org/get\n\n# Output displays Server, Date, Content-Type, Content-Length",
                "explanation": "Fast header inspection via cURL."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Read and Echo Custom Header",
            description="Write a Flask endpoint `/api/echo-agent` that reads the `User-Agent` request header and returns it as JSON `{'client': agent}`.",
            starter_code="from flask import Flask, request, jsonify\napp = Flask(__name__)\n\n# Implement header reader\n",
            solution_code="from flask import Flask, request, jsonify\napp = Flask(__name__)\n\n@app.route('/api/echo-agent')\ndef echo_agent():\n    agent = request.headers.get('User-Agent', 'unknown')\n    return jsonify({'client': agent})",
            expected_output="{'client': 'curl/8.x'}"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the difference between the `Content-Type` and `Accept` HTTP headers?",
                options=[
                    "`Content-Type` indicates the data format sent in the current body; `Accept` tells the recipient what format the sender wants back",
                    "`Content-Type` is for passwords; `Accept` is for usernames",
                    "`Accept` is used only by servers; `Content-Type` is used only by clients",
                    "There is no difference"
                ],
                correct_answer="`Content-Type` indicates the data format sent in the current body; `Accept` tells the recipient what format the sender wants back",
                explanation="Content-Type describes the outgoing body; Accept requests a preferred incoming format."
            ),
            QuizQuestionBlueprint(
                question="Which standard HTTP header transmits authentication credentials such as a Bearer JWT token?",
                options=["Authorization", "Authentication", "Security-Token", "API-Key"],
                correct_answer="Authorization",
                explanation="The standard header for authentication credentials is `Authorization`."
            ),
            QuizQuestionBlueprint(
                question="Are HTTP header names case-sensitive according to the HTTP specification?",
                options=[
                    "No, HTTP header names are case-insensitive (`Content-Type` is identical to `content-type`)",
                    "Yes, headers must be strictly UPPERCASE",
                    "Yes, headers must be strictly lowercase",
                    "Only on Linux servers"
                ],
                correct_answer="No, HTTP header names are case-insensitive (`Content-Type` is identical to `content-type`)",
                explanation="Per RFC 7230, header field names are case-insensitive."
            ),
            QuizQuestionBlueprint(
                question="What does the `Cache-Control: no-cache` header directive instruct clients and proxies to do?",
                options=[
                    "It requires the client to revalidate the cache with the origin server before using a cached copy",
                    "It permanently disables all caching on the hard drive",
                    "It deletes all cookies",
                    "It speeds up page load by 10x"
                ],
                correct_answer="It requires the client to revalidate the cache with the origin server before using a cached copy",
                explanation="`no-cache` allows caching, but mandates origin validation before serving cached assets."
            ),
            QuizQuestionBlueprint(
                question="Why did RFC 6648 deprecate prefixing custom HTTP headers with `X-` (e.g. `X-Request-ID`)?",
                options=[
                    "Because when custom `X-` headers became industry standards, transitioning away from the `X-` prefix caused backwards compatibility breakage",
                    "Because `X` is an invalid ASCII letter",
                    "Because Twitter trademarked the letter X",
                    "Because `X-` headers take up too much memory"
                ],
                correct_answer="Because when custom `X-` headers became industry standards, transitioning away from the `X-` prefix caused backwards compatibility breakage",
                explanation="RFC 6648 deprecated `X-` because standardizing them later created painful migration issues."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 12: URI, URL, aur URN ka structure aur farq
    # ----------------------------------------------------
    DayBlueprint(
        order=12,
        title="Day 12: URI, URL, and URN: Structure and Differences",
        concept="Demystifying Web Resource Identifiers: the overarching URI concept, locators (URL), names (URN), and dissecting full URL anatomy.",
        analogy="Think of identifying a human being: A **URI** is any identifier for a person. A **URN** is their Social Security Number (it names WHO they are, regardless of where they live). A **URL** is their current home street address (it tells you WHERE and HOW to reach them).",
        theory_sections=[
            {
                "heading": "The Hierarchy: URI = URL + URN",
                "body": (
                    "Developers frequently use 'URL' and 'URI' interchangeably, but they have distinct technical definitions:\n"
                    "- **URI (Uniform Resource Identifier)**: The umbrella superset. Any string that identifies a resource.\n"
                    "- **URL (Uniform Resource Locator)**: A URI that specifies the **location** and the **mechanism** (protocol) to retrieve it (e.g., `https://example.com/index.html`).\n"
                    "- **URN (Uniform Resource Name)**: A URI that identifies a resource by a permanent **name** in a specific namespace, independent of location (e.g., `urn:isbn:0451450523`)."
                )
            },
            {
                "heading": "The 6 Components of a URL",
                "body": (
                    "```text\n"
                    "https://user:pass@api.example.com:8080/v1/products?category=books&sort=asc#reviews\n"
                    "  |          |            |          |       |                  |             |\n"
                    "Scheme    Userinfo       Host       Port    Path              Query        Fragment\n"
                    "```\n"
                    "1. **Scheme/Protocol**: `https` (how to communicate).\n"
                    "2. **Host**: `api.example.com` (domain name or IP address).\n"
                    "3. **Port**: `:8080` (network socket port; defaults to 80 for HTTP, 443 for HTTPS).\n"
                    "4. **Path**: `/v1/products` (hierarchical resource locator).\n"
                    "5. **Query String**: `?category=books&sort=asc` (filtering, sorting parameters).\n"
                    "6. **Fragment**: `#reviews` (client-side anchor; **never sent to the server**!)."
                )
            },
            {
                "heading": "Critical Rule: Fragments are Client-Only",
                "body": (
                    "The fragment identifier (`#anchor`) is parsed strictly by the web browser for scrolling or client-side routing. "
                    "HTTP clients **strip the fragment** before transmitting the request to the server."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Dissecting a URL in Python via urllib.parse",
                "code": "from urllib.parse import urlparse, parse_qs\n\nurl = 'https://api.shop.com:443/v1/items?search=laptop&page=2#specs'\nparsed = urlparse(url)\n\nprint(f\"Scheme:   {parsed.scheme}\")    # https\nprint(f\"Hostname: {parsed.hostname}\")  # api.shop.com\nprint(f\"Port:     {parsed.port}\")      # 443\nprint(f\"Path:     {parsed.path}\")      # /v1/items\nprint(f\"Query:    {parse_qs(parsed.query)}\") # {'search': ['laptop'], 'page': ['2']}\nprint(f\"Fragment: {parsed.fragment}\")  # specs",
                "explanation": "Programmatic decomposition of URL components."
            },
            {
                "title": "URL Encoding / Percent-Encoding",
                "code": "from urllib.parse import quote, unquote\n\n# Spaces and special characters must be percent-encoded in URLs:\nquery = \"rock & roll / 2026\"\nencoded = quote(query)\nprint(f\"Encoded: {encoded}\")  # rock%20%26%20roll%20%2F%202026\n\n# Decoding:\nprint(f\"Decoded: {unquote(encoded)}\")",
                "explanation": "Percent-encoding replaces unsafe ASCII characters in URIs."
            },
            {
                "title": "Examples of URNs vs URLs",
                "code": "# URLs (Specify WHERE and HOW to fetch):\n# https://en.wikipedia.org/wiki/API\n# ftp://files.example.com/archive.zip\n\n# URNs (Specify permanent WHAT identity):\n# urn:isbn:9780132350884 (Book identifier)\n# urn:ietf:rfc:2616 (RFC document identifier)\n# urn:uuid:f81d4fae-7dec-11d0-a765-00a0c91e6bf6",
                "explanation": "Contrasts locators (URLs) with persistent names (URNs)."
            },
            {
                "title": "URL Component Visual Map",
                "code": "# [ https ]:// [ api.dev.com ] : [ 443 ] / [ users/42 ] ? [ detail=full ] # [ top ]\n#  Protocol         Host          Port         Path             Query         Fragment\n# (How to talk)   (Where to go)  (Door)     (Which item)    (Options)      (Client-side)",
                "explanation": "Visual reference of full URL anatomy."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Parse Query String from URL",
            description="Write a Python function `get_query_param(url: str, param: str) -> str` using `urllib.parse` that extracts the single string value of `param` from a given URL.",
            starter_code="from urllib.parse import urlparse, parse_qs\n\ndef get_query_param(url: str, param: str) -> str:\n    # Parse URL and return param value\n    pass",
            solution_code="from urllib.parse import urlparse, parse_qs\n\ndef get_query_param(url: str, param: str) -> str:\n    parsed = urlparse(url)\n    queries = parse_qs(parsed.query)\n    return queries.get(param, [''])[0]",
            expected_output="Extracted param string"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Which statement correctly identifies the relationship between URI, URL, and URN?",
                options=[
                    "URI is the overarching umbrella category; both URLs (locators) and URNs (names) are specific types of URIs",
                    "URL is the umbrella; URI is an outdated term",
                    "URN is used only for email addresses",
                    "There is no difference; all three are synonyms"
                ],
                correct_answer="URI is the overarching umbrella category; both URLs (locators) and URNs (names) are specific types of URIs",
                explanation="A URI can be a locator (URL), a name (URN), or both."
            ),
            QuizQuestionBlueprint(
                question="What happens to the fragment portion of a URL (e.g. `#reviews`) when a web browser sends an HTTP request to an API server?",
                options=[
                    "The browser strips the fragment before transmission; the fragment is never sent across the network to the server",
                    "The server saves the fragment in the database",
                    "The server crashes if a fragment is present",
                    "The fragment is converted into an HTTP header"
                ],
                correct_answer="The browser strips the fragment before transmission; the fragment is never sent across the network to the server",
                explanation="Fragments are client-side navigation anchors handled entirely within the browser."
            ),
            QuizQuestionBlueprint(
                question="What character separates the URL path from the query parameters in a standard web URL?",
                options=["A question mark (`?`)", "An ampersand (`&`)", "A hashtag (`#`)", "A colon (`:`)"],
                correct_answer="A question mark (`?`)",
                explanation="The question mark `?` denotes the beginning of the query string."
            ),
            QuizQuestionBlueprint(
                question="What is the default port number assumed when connecting to a URL with the `https://` scheme if no explicit port is written?",
                options=["443", "80", "8080", "22"],
                correct_answer="443",
                explanation="HTTPS defaults to TCP port 443; plain HTTP defaults to port 80."
            ),
            QuizQuestionBlueprint(
                question="Why does `rock & roll` become `rock%20%26%20roll` when included in a URL query parameter?",
                options=[
                    "It has been percent-encoded to replace characters that have special reserved meanings in URLs (like spaces and ampersands)",
                    "It has been encrypted with AES-256",
                    "It is compressed to save space",
                    "The server corrupted the text"
                ],
                correct_answer="It has been percent-encoded to replace characters that have special reserved meanings in URLs (like spaces and ampersands)",
                explanation="Percent-encoding escapes reserved delimiter characters in URIs."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 13: REST (Representational State Transfer) kya hai?
    # ----------------------------------------------------
    DayBlueprint(
        order=13,
        title="Day 13: What is REST? (Representational State Transfer)",
        concept="Exploring the architectural philosophy of REST introduced by Roy Fielding in 2000: resource representations, state transitions, and decoupling.",
        analogy="Think of buying a house. You cannot pick up the physical brick house and mail it over the internet to a buyer. Instead, you send a photo and blueprint (a Representation). When the buyer signs paperwork, the ownership changes (State Transfer). REST is transferring representations of resources to change their state.",
        theory_sections=[
            {
                "heading": "The Origin of REST",
                "body": (
                    "In 2000, computer scientist **Roy Fielding** published his landmark PhD dissertation: "
                    "*'Architectural Styles and the Design of Network-based Software Architectures'*. "
                    "In chapter 5, he introduced **REST (Representational State Transfer)** as the architectural style that makes the World Wide Web scalable, "
                    "fault-tolerant, and universally interoperable."
                )
            },
            {
                "heading": "Deconstructing the Name",
                "body": (
                    "- **Resource**: Any entity or concept of interest that can be named (a user, a bank account, an order, a weather forecast).\n"
                    "- **Representation**: The format in which the resource is serialized and communicated (JSON, XML, HTML, PDF).\n"
                    "- **State Transfer**: When a client requests a resource representation, it transitions through states by executing actions (GET, POST, PUT, DELETE)."
                )
            },
            {
                "heading": "REST is an Architectural Style, NOT a Standard or Protocol!",
                "body": (
                    "A critical distinction: SOAP is an official W3C protocol with strict rigid rules. "
                    "REST is **not a protocol, library, or framework**; it is a set of **architectural design principles and constraints**. "
                    "You can build a REST API in Python, Go, Java, or PHP over HTTP."
                )
            }
        ],
        code_snippets=[
            {
                "title": "A Resource with Multiple Representations",
                "code": "# A single User resource (id: 42) can have multiple representations:\n\n# Representation A: application/json\n# {\"id\": 42, \"name\": \"Alice\", \"email\": \"alice@dev.io\"}\n\n# Representation B: text/csv\n# id,name,email\n# 42,Alice,alice@dev.io\n\n# Representation C: text/html\n# <div class=\"user\"><h1>Alice</h1><p>alice@dev.io</p></div>",
                "explanation": "A resource is separate from its serialized representation."
            },
            {
                "title": "State Transition Lifecycle",
                "code": "# Client enters state: Reviewing shopping cart\nGET /api/v1/cart\n\n# Client transitions to state: Order placed\nPOST /api/v1/orders\nPayload: {\"cart_id\": 101}\nResponse: 201 Created (Order #504)\n\n# Client transitions to state: Payment submitted\nPOST /api/v1/orders/504/payments\nResponse: 200 OK (Status: Paid)",
                "explanation": "Illustrates Representational State Transfer through sequential interactions."
            },
            {
                "title": "Roy Fielding's Core REST Tenet",
                "code": "# \"REST emphasizes scalability of component interactions, generality of interfaces,\n# independent deployment of components, and intermediary components to reduce latency,\n# enforce security and encapsulate legacy systems.\" — Dr. Roy Fielding",
                "explanation": "Foundational architectural goal of REST."
            },
            {
                "title": "RESTful Interface in FastAPI",
                "code": "from fastapi import FastAPI\n\napp = FastAPI()\n\n# Resources are addressed via clean, predictable URIs:\n@app.get(\"/api/v1/customers/{customer_id}\")\ndef get_customer(customer_id: int):\n    return {\"id\": customer_id, \"status\": \"active\"}",
                "explanation": "Modern resource routing in FastAPI."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Build Resource Representation Endpoint",
            description="Write a Flask endpoint `GET /api/v1/servers/<int:server_id>` that returns a JSON representation of a server resource: `{'id': server_id, 'status': 'running', 'region': 'us-east-1'}`.",
            starter_code="from flask import Flask, jsonify\napp = Flask(__name__)\n\n# Implement representation endpoint\n",
            solution_code="from flask import Flask, jsonify\napp = Flask(__name__)\n\n@app.route('/api/v1/servers/<int:server_id>')\ndef get_server(server_id):\n    return jsonify({'id': server_id, 'status': 'running', 'region': 'us-east-1'}), 200",
            expected_output="{'id': 1, 'status': 'running', 'region': 'us-east-1'}, 200"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Who originally defined the architectural style of REST in his 2000 doctoral dissertation?",
                options=["Dr. Roy Fielding", "Linus Torvalds", "Tim Berners-Lee", "Brendan Eich"],
                correct_answer="Dr. Roy Fielding",
                explanation="Dr. Roy Fielding introduced REST in his 2000 PhD dissertation at UC Irvine."
            ),
            QuizQuestionBlueprint(
                question="Is REST an official strict protocol standard or an architectural design style?",
                options=[
                    "It is an architectural design style composed of constraints, not a rigid protocol",
                    "It is a compiled binary protocol",
                    "It is an official law passed by the United Nations",
                    "It is a programming language"
                ],
                correct_answer="It is an architectural design style composed of constraints, not a rigid protocol",
                explanation="REST is a set of design principles and constraints rather than an enforced protocol."
            ),
            QuizQuestionBlueprint(
                question="In REST terminology, what is a 'Representation' of a resource?",
                options=[
                    "A specific serialized encoding (such as JSON or XML) of the current state of a resource",
                    "The physical server hard drive",
                    "The lawyer representing the company",
                    "The database password"
                ],
                correct_answer="A specific serialized encoding (such as JSON or XML) of the current state of a resource",
                explanation="A representation captures the state of a resource in a portable format like JSON."
            ),
            QuizQuestionBlueprint(
                question="Can a single REST resource have multiple different representations (e.g. JSON, XML, CSV)?",
                options=[
                    "Yes, a client can use the `Accept` header to negotiate whether it receives JSON, XML, or CSV",
                    "No, REST strictly forbids more than one representation",
                    "Only if using PHP",
                    "Only on weekends"
                ],
                correct_answer="Yes, a client can use the `Accept` header to negotiate whether it receives JSON, XML, or CSV",
                explanation="Content negotiation allows a single resource to be served in JSON, XML, or CSV."
            ),
            QuizQuestionBlueprint(
                question="What does the 'State Transfer' in REST signify?",
                options=[
                    "The client transitions through application states by receiving representations and initiating new actions",
                    "Transferring money between US states",
                    "Rebooting the server",
                    "Switching between WiFi and cellular data"
                ],
                correct_answer="The client transitions through application states by receiving representations and initiating new actions",
                explanation="Clients progress through application workflow states by interacting with representations."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 14: The 6 Constraints of REST
    # ----------------------------------------------------
    DayBlueprint(
        order=14,
        title="Day 14: The 6 Architectural Constraints of REST",
        concept="Mastering the six foundational architectural constraints that qualify an API as truly RESTful: Client-Server, Statelessness, Cacheability, Uniform Interface, Layered System, and Code on Demand.",
        analogy="Think of building a skyscraper. You can design it with any paint color or glass you want, but if you don't follow the 6 core structural engineering rules (foundation, weight distribution, fire exits, etc.), it is not a safe skyscraper. The 6 constraints are the engineering pillars of REST.",
        theory_sections=[
            {
                "heading": "The 6 Architectural Pillars",
                "body": (
                    "To be truly 'RESTful', an API architecture must adhere to six specific constraints:\n"
                    "1. **Client-Server Architecture**: Separation of concerns. The client handles UI/UX; the server handles data storage and business logic. Each can evolve independently.\n"
                    "2. **Statelessness**: Every request from client to server must contain all the information necessary to understand and complete the request. The server never stores client session state between requests.\n"
                    "3. **Cacheability**: Responses must implicitly or explicitly define themselves as cacheable or non-cacheable to eliminate redundant requests.\n"
                    "4. **Uniform Interface**: The defining feature of REST! Resources are uniquely identified, manipulated through representations, self-descriptive, and leverage hypermedia (HATEOAS).\n"
                    "5. **Layered System**: The client cannot tell whether it is connected directly to the end server, or to an intermediary proxy, load balancer, or CDN.\n"
                    "6. **Code on Demand (Optional)**: The only optional constraint! Servers can temporarily extend client functionality by transferring executable code (e.g., JavaScript scripts or WebAssembly)."
                )
            },
            {
                "heading": "Why These Constraints Matter",
                "body": (
                    "These six constraints were not chosen randomly; they were engineered to maximize **scalability**, "
                    "**modifiability**, **visibility**, **portability**, and **reliability** across planetary-scale distributed systems."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Constraint 1: Client-Server Separation",
                "code": "# Client (React / Swift iOS App) cares only about UI and user input:\n# fetch('/api/v1/orders')\n\n# Server (Go / Python) cares only about business logic and database:\n# db.Query(\"SELECT * FROM orders WHERE user_id = $1\")\n# Either can be rewritten from scratch without altering the other!",
                "explanation": "Strict decoupling enables multi-platform support (web, mobile, IoT)."
            },
            {
                "title": "Constraint 3: Cacheability Directives in Headers",
                "code": "# Server response explicitly declaring cache validity:\nHTTP/1.1 200 OK\nContent-Type: application/json\nCache-Control: public, max-age=86400\nETag: \"33a64df551425fcc55e4d42a148795d9f25f89d4\"\n\n# Clients and intermediate CDNs can safely cache this response for 24 hours!",
                "explanation": "Explicit cache directives prevent server overload."
            },
            {
                "title": "Constraint 5: Layered System Transparency",
                "code": "# [Client (Mobile App)] \n#          |\n#          v\n# [Cloudflare CDN (Edge Cache)]\n#          |\n#          v\n# [AWS ALB (Load Balancer)]\n#          |\n#          v\n# [Kong (API Gateway - Auth & Rate Limiting)]\n#          |\n#          v\n# [FastAPI Backend Service]\n# The client has no idea (and does not care) that 4 layers exist!",
                "explanation": "Layered systems allow inserting security and caching intermediaries transparently."
            },
            {
                "title": "Summary of the 6 Constraints",
                "code": "# 1. Client-Server      -> Separation of concerns\n# 2. Stateless          -> No server-side session memory\n# 3. Cacheable          -> Explicit cache headers\n# 4. Uniform Interface  -> Standardized resource interaction\n# 5. Layered System     -> Intermediaries (proxies/CDNs) allowed\n# 6. Code on Demand     -> (Optional) Transferring executable JS",
                "explanation": "Quick mental summary of the six constraints."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Inspect Cacheability Header Configuration",
            description="Write a Flask endpoint `/api/static-data` returning JSON `{'data': 'unchanging'}` with header `Cache-Control: public, max-age=3600` adhering to the Cacheability constraint.",
            starter_code="from flask import Flask, jsonify\napp = Flask(__name__)\n\n# Implement cacheable endpoint\n",
            solution_code="from flask import Flask, jsonify\napp = Flask(__name__)\n\n@app.route('/api/static-data')\ndef static_data():\n    return jsonify({'data': 'unchanging'}), 200, {'Cache-Control': 'public, max-age=3600'}",
            expected_output="{'data': 'unchanging'}, 200, Cache-Control: public, max-age=3600"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="How many foundational architectural constraints did Roy Fielding establish in the REST specification?",
                options=["6 (5 mandatory, 1 optional)", "4", "10", "12"],
                correct_answer="6 (5 mandatory, 1 optional)",
                explanation="REST defines 6 constraints: 5 mandatory and 1 optional (Code on Demand)."
            ),
            QuizQuestionBlueprint(
                question="Which of the six REST constraints is officially marked as OPTIONAL?",
                options=["Code on Demand", "Statelessness", "Client-Server", "Cacheability"],
                correct_answer="Code on Demand",
                explanation="Code on Demand (transferring executable code like JS applets) is the only optional constraint."
            ),
            QuizQuestionBlueprint(
                question="What does the 'Layered System' constraint enable in modern cloud infrastructure?",
                options=[
                    "It allows inserting proxies, API gateways, load balancers, and CDNs between client and server without the client needing to know",
                    "It requires applications to be written in at least 5 programming languages",
                    "It forces servers to use multi-layer hard drives",
                    "It encrypts the operating system"
                ],
                correct_answer="It allows inserting proxies, API gateways, load balancers, and CDNs between client and server without the client needing to know",
                explanation="Layered system architecture allows transparent intermediaries for caching, security, and load balancing."
            ),
            QuizQuestionBlueprint(
                question="What is the primary benefit of the 'Client-Server' constraint in REST?",
                options=[
                    "Separation of concerns: frontend user interfaces and backend data logic can evolve and scale independently",
                    "It eliminates the need for frontend developers",
                    "It prevents cyber attacks completely",
                    "It allows computers to run without RAM"
                ],
                correct_answer="Separation of concerns: frontend user interfaces and backend data logic can evolve and scale independently",
                explanation="Client-server separation allows independent evolution of user interfaces and backend storage."
            ),
            QuizQuestionBlueprint(
                question="Under the 'Uniform Interface' constraint, what must be true about resource representations?",
                options=[
                    "They should be self-descriptive and provide standard methods and hyperlinks for state navigation",
                    "They must all be written in binary machine code",
                    "They can only be requested once per day",
                    "They must always be under 100 bytes"
                ],
                correct_answer="They should be self-descriptive and provide standard methods and hyperlinks for state navigation",
                explanation="Uniform interfaces require standard identifiers, self-descriptive messages, and hypermedia controls."
            )
        ]
    ),

    # ----------------------------------------------------
    # Day 15: Statelessness in Depth (Statelessness constraint)
    # ----------------------------------------------------
    DayBlueprint(
        order=15,
        title="Day 15: Statelessness in Depth (The Engine of Scale)",
        concept="Deep dive into REST's most powerful constraint: Statelessness. Contrasting server-side session cookies with self-contained stateless tokens (JWT) for horizontal scaling.",
        analogy="Stateful is a small-town doctor who remembers your medical history in his head: you can ONLY visit that specific doctor. Stateless is an emergency room where you carry your complete medical chart on a laminated card in your wallet: ANY doctor at any hospital can treat you instantly without checking prior memories.",
        theory_sections=[
            {
                "heading": "What Does Statelessness Actually Mean?",
                "body": (
                    "In a stateless REST architecture:\n"
                    "> **\"No client session context is ever stored on the server between requests.\"**\n\n"
                    "Each incoming request must contain **every single piece of information** necessary for the server to authenticate, "
                    "authorize, and fulfill the request. If Request #2 arrives 1 millisecond after Request #1, the server treats Request #2 "
                    "as if it has never seen this client before in history."
                )
            },
            {
                "heading": "The Nightmare of Stateful Server Sessions",
                "body": (
                    "In legacy stateful architectures, logging in creates a session in the server's RAM (`session_id`). "
                    "If you scale to 10 server instances behind a load balancer, Request #1 lands on Server A. "
                    "When Request #2 lands on Server B, Server B has no memory of the session and kicks the user out! "
                    "Engineers had to use complex 'sticky sessions' or centralized session databases (Redis), creating single points of failure."
                )
            },
            {
                "heading": "How Statelessness Enables Infinite Horizontal Scaling",
                "body": (
                    "In a stateless API using tokens (like Bearer JWTs), the client sends the token in the `Authorization` header with every request. "
                    "The load balancer can route requests to Server 1, Server 42, or Server 99 randomly. "
                    "Any server can independently verify the cryptographic token and serve the response instantly! "
                    "Servers can crash, reboot, or autoscale from 10 to 1,000 nodes with zero session loss."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Stateful vs Stateless Server Architecture",
                "code": "# STATEFUL ANTI-PATTERN (Sticky Sessions Required):\n# Client -> [Load Balancer] -> Server 1 (Holds session in RAM!)\n# Next Request lands on Server 2 -> ERROR 401 Unauthorized (Session not found!)\n\n# STATELESS ARCHITECTURE (Infinite Scale):\n# Client attaches self-contained JWT token in Authorization header:\n# Client -> [Load Balancer] -> Server 1, 2, or 3 (Verifies token signature independently)\n# Every server is identical and interchangeable!",
                "explanation": "Demonstrates why statelessness is essential for modern cloud autoscale."
            },
            {
                "title": "Stateless Authentication Header in Practice",
                "code": "# Every request carries its own identity context:\nGET /api/v1/orders HTTP/1.1\nHost: api.example.com\nAuthorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c",
                "explanation": "Self-contained cryptographically signed token eliminates server session storage."
            },
            {
                "title": "FastAPI Stateless JWT Verification Middleware",
                "code": "from fastapi import FastAPI, Depends, HTTPException, Header\nimport jwt\n\napp = FastAPI()\nSECRET_KEY = \"super_secret_signing_key\"\n\ndef verify_stateless_user(authorization: str = Header(...)):\n    try:\n        token = authorization.split(\" \")[1]\n        # Cryptographically verifies payload without querying session storage:\n        payload = jwt.decode(token, SECRET_KEY, algorithms=[\"HS256\"])\n        return payload\n    except Exception:\n        raise HTTPException(status_code=401, detail=\"Invalid credentials\")\n\n@app.get(\"/api/v1/profile\")\ndef get_profile(user: dict = Depends(verify_stateless_user)):\n    return {\"user_id\": user[\"sub\"], \"data\": \"Stateless verification successful!\"}",
                "explanation": "Stateless verification in FastAPI using JWT headers."
            },
            {
                "title": "Trade-Offs of Statelessness",
                "code": "# Advantages:               # Disadvantages:\n# - Horizontal autoscaling   # - Larger network payload (tokens sent every time)\n# - Zero session storage     # - Token revocation is tricky (requires blocklists)\n# - Fault tolerance          # - Client must manage token persistence securely",
                "explanation": "Weighing benefits against token management overhead."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Implement Stateless Authorization Checker",
            description="Write a Python function `check_auth(headers: dict) -> bool` that returns True if the 'Authorization' header starts with 'Bearer ' and has length > 10, otherwise returns False.",
            starter_code="def check_auth(headers: dict) -> bool:\n    # Implement stateless check\n    pass",
            solution_code="def check_auth(headers: dict) -> bool:\n    auth = headers.get('Authorization', '')\n    return auth.startswith('Bearer ') and len(auth) > 10",
            expected_output="True for valid Bearer token, False otherwise"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the core principle of the 'Statelessness' constraint in REST APIs?",
                options=[
                    "The server must not store any client session context in its memory between requests; every request must be completely self-contained",
                    "Servers are not allowed to use databases",
                    "Clients cannot save their passwords",
                    "APIs can only be accessed from one country"
                ],
                correct_answer="The server must not store any client session context in its memory between requests; every request must be completely self-contained",
                explanation="Statelessness dictates that all context must accompany the request itself."
            ),
            QuizQuestionBlueprint(
                question="Why does statelessness make horizontal scaling across hundreds of cloud servers dramatically easier?",
                options=[
                    "Any server instance can fulfill any incoming request because no server relies on local memory or sticky sessions",
                    "Stateless servers do not require electricity",
                    "Stateless code executes at the speed of light",
                    "Stateless APIs do not require IP addresses"
                ],
                correct_answer="Any server instance can fulfill any incoming request because no server relies on local memory or sticky sessions",
                explanation="When servers hold no session memory, any node in the cluster can handle any request interchangeably."
            ),
            QuizQuestionBlueprint(
                question="What technology is widely used in modern REST APIs to achieve stateless authentication?",
                options=["JSON Web Tokens (JWT) in Authorization headers", "Floppy disks", "Server RAM sessions", "Telnet logins"],
                correct_answer="JSON Web Tokens (JWT) in Authorization headers",
                explanation="JWTs contain cryptographically signed identity payloads verified statelessly on each request."
            ),
            QuizQuestionBlueprint(
                question="What was a major disadvantage of legacy stateful session cookies when deploying behind load balancers?",
                options=[
                    "Load balancers required complex 'sticky sessions' to route a user back to the exact same server instance where their session RAM lived",
                    "Cookies could only hold 2 words",
                    "Stateful sessions only worked on Internet Explorer",
                    "Cookies were illegal under RFC 2616"
                ],
                correct_answer="Load balancers required complex 'sticky sessions' to route a user back to the exact same server instance where their session RAM lived",
                explanation="Sticky sessions bind clients to specific nodes, defeating true elastic load balancing."
            ),
            QuizQuestionBlueprint(
                question="What is one trade-off / drawback of the statelessness constraint?",
                options=[
                    "Network overhead increases slightly because authorization tokens and metadata must be sent across the wire with every single request",
                    "Stateless APIs cannot return JSON",
                    "Stateless APIs crash after 100 users",
                    "Stateless APIs cannot use HTTPS"
                ],
                correct_answer="Network overhead increases slightly because authorization tokens and metadata must be sent across the wire with every single request",
                explanation="Repetitive transmission of tokens increases per-request header overhead slightly."
            )
        ]
    )
]
