"""
api_curriculum_days_46_60.py
Days 46 to 60 for Complete APIs & Web Services Architecture.
Covers:
- Phase 7 (Part 2): GraphQL Basics, Advanced GraphQL, gRPC & Protocol Buffers
- Phase 8: OpenAPI/Swagger Specifications, API Documentation & Developer Experience, Unit Testing APIs, Integration Testing & Mocking, Load & Performance Testing (k6, Artillery)
- Phase 9: API Gateways (Kong, NGINX), Microservices & Service Mesh, API Caching Strategies (ETag, Redis, CDN), Observability & Distributed Tracing, CI/CD & Contract Testing, API Monetization & Stripe Usage Billing, and Day 60 Capstone Enterprise API Architecture.
"""

from seeder.course_blueprint import DayBlueprint

DAYS_46_TO_60 = [
    # ---------------------------------------------------------
    # Day 46: GraphQL Basics: Schemas, Types, and Resolvers
    # ---------------------------------------------------------
    DayBlueprint(
        order=46,
        title="GraphQL Basics: Schemas, Types, and Resolvers",
        concept="GraphQL is an API query language and runtime developed by Meta that allows clients to request exactly the data they need through a single strongly-typed endpoint, solving over-fetching and under-fetching.",
        analogy="Think of REST like a fixed-price set buffet where you have to take whatever dishes are placed on your plate whether you eat them or not. GraphQL is an à la carte gourmet menu where you check off exactly 2 strawberries and 1 toast, and the kitchen brings exactly that.",
        theory_sections=[
            {
                "heading": "Why GraphQL? Over-fetching and Under-fetching",
                "content": (
                    "In REST APIs, mobile apps frequently suffer from two major problems:\n"
                    "1. **Over-fetching**: A mobile profile card only needs `username` and `avatar_url`, but `GET /users/42` returns 80 fields including billing address, hashed password metadata, order history, and preferences.\n"
                    "2. **Under-fetching (The N+1 API Problem)**: To render a dashboard, the client must call `GET /users/42`, then call `GET /users/42/posts` for 10 posts, then call `GET /posts/{id}/comments` 10 separate times (11 network roundtrips).\n\n"
                    "GraphQL solves both with a **single HTTP POST endpoint** (`/graphql`). The client sends a query document specifying the precise field tree required, and the server fulfills it in a single response."
                )
            },
            {
                "heading": "Schema Definition Language (SDL) & Type System",
                "content": (
                    "GraphQL is strictly typed. The schema is the contract between client and server. Core types include:\n"
                    "- **Scalar Types**: `Int`, `Float`, `String`, `Boolean`, and `ID` (unique serialized string identifier).\n"
                    "- **Object Types**: Custom structures containing fields (e.g. `type User { id: ID!, name: String!, posts: [Post!]! }`).\n"
                    "- **Non-Null Modifier (`!`)**: Guarantees the field will never be null.\n"
                    "- **List Modifier (`[...]`)**: An array of elements.\n"
                    "- **Root Types**: `type Query`, `type Mutation`, `type Subscription`."
                )
            },
            {
                "heading": "Resolvers: The Data Fetching Engine",
                "content": (
                    "Every field in a GraphQL schema is backed by a **Resolver** function. A resolver answers: 'How do I fetch the data for this specific field?'\n\n"
                    "Resolvers accept 4 standard arguments:\n"
                    "1. `parent` / `root`: The return value of the parent resolver in the field tree.\n"
                    "2. `args`: Arguments passed in the query (e.g., `user(id: 42)`).\n"
                    "3. `context`: Shared per-request state (current logged-in user, DB connections, DataLoader).\n"
                    "4. `info`: AST of the query and field metadata."
                )
            }
        ],
        code_snippets=[
            {
                "title": "GraphQL Schema Definition (SDL)",
                "language": "graphql",
                "code": (
                    "type User {\n"
                    "  id: ID!\n"
                    "  name: String!\n"
                    "  email: String!\n"
                    "  posts: [Post!]!\n"
                    "}\n\n"
                    "type Post {\n"
                    "  id: ID!\n"
                    "  title: String!\n"
                    "  content: String!\n"
                    "  author: User!\n"
                    "}\n\n"
                    "type Query {\n"
                    "  getUser(id: ID!): User\n"
                    "  allPosts(limit: Int = 10): [Post!]!\n"
                    "}"
                ),
                "explanation": "Defines the contract with non-nullable constraints and relations between User and Post."
            },
            {
                "title": "Client GraphQL Query Payload",
                "language": "graphql",
                "code": (
                    "# POST /graphql\n"
                    "query GetUserProfile($userId: ID!) {\n"
                    "  getUser(id: $userId) {\n"
                    "    name\n"
                    "    posts {\n"
                    "      title\n"
                    "    }\n"
                    "  }\n"
                    "}\n\n"
                    "# Variables: {\"userId\": \"101\"}"
                ),
                "explanation": "Client asks strictly for `name` and post `title`s. All other database fields are excluded from transmission."
            },
            {
                "title": "Python GraphQL Resolvers (Ariadne / Strawberry)",
                "language": "python",
                "code": (
                    "import strawberry\n"
                    "from typing import List\n\n"
                    "@strawberry.type\n"
                    "class Post:\n"
                    "    id: strawberry.ID\n"
                    "    title: str\n\n"
                    "@strawberry.type\n"
                    "class User:\n"
                    "    id: strawberry.ID\n"
                    "    name: str\n"
                    "    posts: List[Post]\n\n"
                    "@strawberry.type\n"
                    "class Query:\n"
                    "    @strawberry.field\n"
                    "    def get_user(self, info, id: strawberry.ID) -> User:\n"
                    "        # Context contains auth user and DB pool\n"
                    "        return User(id=id, name='Alice', posts=[Post(id='1', title='First API')])\n\n"
                    "schema = strawberry.Schema(query=Query)"
                ),
                "explanation": "Type-annotated Python GraphQL resolver matching the SDL specification."
            },
            {
                "title": "GraphQL JSON Server Response",
                "language": "json",
                "code": (
                    "{\n"
                    "  \"data\": {\n"
                    "    \"getUser\": {\n"
                    "      \"name\": \"Alice\",\n"
                    "      \"posts\": [\n"
                    "        { \"title\": \"First API\" }\n"
                    "      ]\n"
                    "    }\n"
                    "  }\n"
                    "}"
                ),
                "explanation": "GraphQL always returns an envelope with a top-level `data` key (or `errors` key if execution fails)."
            }
        ],
        coding_challenge={
            "title": "Simulate a GraphQL Field Extractor",
            "instructions": "Write a function `execute_graphql_mock(schema_db, query_fields)` that takes a database record and a list of requested field names, returning a dictionary containing only the requested fields under a `'data'` envelope.",
            "starter_code": (
                "def execute_graphql_mock(record: dict, requested_fields: list) -> dict:\n"
                "    # Filter record keys to only requested_fields and wrap in {'data': ...}\n"
                "    pass\n"
            ),
            "solution_code": (
                "def execute_graphql_mock(record: dict, requested_fields: list) -> dict:\n"
                "    filtered = {k: v for k, v in record.items() if k in requested_fields}\n"
                "    return {'data': filtered}\n\n"
                "user_db = {'id': '101', 'name': 'Amina', 'email': 'amina@test.com', 'ssn': '000-11-2222', 'role': 'admin'}\n"
                "print(execute_graphql_mock(user_db, ['name', 'role']))"
            ),
            "expected_output": "{'data': {'name': 'Amina', 'role': 'admin'}}"
        },
        quizzes=[
            {
                "question": "What primary problem does GraphQL solve compared to traditional REST APIs?",
                "options": [
                    "Over-fetching and under-fetching of data by allowing clients to specify exact fields",
                    "Replacing HTTPS encryption with faster plain TCP packets",
                    "Eliminating the need for databases on the backend",
                    "Guaranteeing that all API responses are cached forever"
                ],
                "correct_answer": "Over-fetching and under-fetching of data by allowing clients to specify exact fields",
                "explanation": "GraphQL allows clients to request exact fields across multiple entities in a single round-trip."
            },
            {
                "question": "What HTTP method does standard GraphQL client-to-server query execution typically use?",
                "options": [
                    "POST (with the query and variables in the JSON body)",
                    "DELETE",
                    "HEAD",
                    "PATCH"
                ],
                "correct_answer": "POST (with the query and variables in the JSON body)",
                "explanation": "Most GraphQL queries and mutations are dispatched via HTTP POST with `{ query: '...', variables: {...} }` in the JSON body."
            },
            {
                "question": "In GraphQL SDL, what does the exclamation mark (`!`) mean after a type like `String!`?",
                "options": [
                    "The field is non-nullable (it will never return null)",
                    "The field is deprecated",
                    "The field is encrypted with AES-256",
                    "The field is an array of strings"
                ],
                "correct_answer": "The field is non-nullable (it will never return null)",
                "explanation": "The exclamation mark indicates a non-nullable type; if null is returned, GraphQL raises an execution error."
            },
            {
                "question": "What is the function of a 'Resolver' in a GraphQL server?",
                "options": [
                    "It is the function responsible for fetching or computing the data for a specific schema field",
                    "It converts HTTP status codes to XML tags",
                    "It automatically generates database indexes",
                    "It compresses CSS stylesheets"
                ],
                "correct_answer": "It is the function responsible for fetching or computing the data for a specific schema field",
                "explanation": "Resolvers map GraphQL schema fields to underlying databases, microservices, or computation logic."
            },
            {
                "question": "What is the standard top-level JSON wrapper key in any successful GraphQL response?",
                "options": [
                    "data",
                    "results_payload",
                    "response_body",
                    "graphql_out"
                ],
                "correct_answer": "data",
                "explanation": "GraphQL specification mandates that resolved fields must be encapsulated inside a top-level `data` map."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 47: GraphQL Advanced: Mutations, Input Types & DataLoader
    # ---------------------------------------------------------
    DayBlueprint(
        order=47,
        title="GraphQL Advanced: Mutations, Input Types & DataLoader",
        concept="Advanced GraphQL encompasses write operations (Mutations), structured arguments (Input Types), and batching/caching techniques like DataLoader to prevent catastrophic N+1 database queries.",
        analogy="If a Query is reading a library book, a Mutation is writing a new chapter. And DataLoader is like a school bus that waits 5 milliseconds at the bus stop to pick up all 30 children together instead of making 30 individual taxi trips to school.",
        theory_sections=[
            {
                "heading": "Mutations: Modifying State",
                "content": (
                    "In GraphQL, read operations use `type Query`, while write operations (Create, Update, Delete) are declared under `type Mutation`.\n\n"
                    "A critical advantage of GraphQL mutations over REST `POST`/`PUT` is **immediate selection of updated state**: In a single mutation request, you can create a new post AND ask the server to immediately return the created post's `id`, formatted `createdAt` timestamp, and the author's new total post count."
                )
            },
            {
                "heading": "Input Object Types (`input`)",
                "content": (
                    "When passing multiple arguments to a mutation (e.g. creating a product with name, price, SKU, tags, inventory), listing individual parameters becomes messy. GraphQL provides the `input` keyword specifically for nested input arguments:\n\n"
                    "```graphql\n"
                    "input CreateProductInput {\n"
                    "  title: String!\n"
                    "  priceCents: Int!\n"
                    "  tags: [String!] = []\n"
                    "}\n"
                    "```\n"
                    "Input types cannot return fields or contain interfaces; they are purely deserialization contracts."
                )
            },
            {
                "heading": "The GraphQL N+1 Problem & DataLoader Solution",
                "content": (
                    "Suppose a query asks for 50 users and their recent 3 orders. If the `User.orders` resolver executes `SELECT * FROM orders WHERE user_id = ?` for each user sequentially, the database receives **1 + 50 = 51 queries**.\n\n"
                    "**DataLoader** solves this via **Batching & In-memory Per-Request Caching**:\n"
                    "1. It collects all `user_id` requests within a single tick of the event loop.\n"
                    "2. It combines them into a single SQL statement: `SELECT * FROM orders WHERE user_id IN (1, 2, ..., 50);`\n"
                    "3. It sorts the results and returns promises to the respective resolvers."
                )
            }
        ],
        code_snippets=[
            {
                "title": "GraphQL Mutation & Input Type Schema",
                "language": "graphql",
                "code": (
                    "input CreateArticleInput {\n"
                    "  title: String!\n"
                    "  body: String!\n"
                    "  tagList: [String!]\n"
                    "}\n\n"
                    "type ArticlePayload {\n"
                    "  article: Article\n"
                    "  errors: [String!]\n"
                    "}\n\n"
                    "type Mutation {\n"
                    "  createArticle(input: CreateArticleInput!): ArticlePayload!\n"
                    "}"
                ),
                "explanation": "Defines an input object and payload pattern returning both the created entity and domain errors."
            },
            {
                "title": "Executing a Mutation with Variables",
                "language": "graphql",
                "code": (
                    "mutation PublishPost($input: CreateArticleInput!) {\n"
                    "  createArticle(input: $input) {\n"
                    "    article {\n"
                    "      id\n"
                    "      title\n"
                    "      author { name }\n"
                    "    }\n"
                    "    errors\n"
                    "  }\n"
                    "}"
                ),
                "explanation": "Executes a write and immediately requests nested author information without a secondary round-trip."
            },
            {
                "title": "DataLoader Implementation (Python aiodataloader)",
                "language": "python",
                "code": (
                    "from aiodataloader import DataLoader\n\n"
                    "class OrderBatchLoader(DataLoader):\n"
                    "    async def batch_load_fn(self, user_ids):\n"
                    "        # Executes 1 SQL query for ALL user_ids combined\n"
                    "        # SELECT * FROM orders WHERE user_id IN (...)\n"
                    "        orders = await db.fetch_all_orders_for_users(user_ids)\n"
                    "        # Map orders back to matching user_id index\n"
                    "        grouped = {uid: [] for uid in user_ids}\n"
                    "        for o in orders:\n"
                    "            grouped[o.user_id].append(o)\n"
                    "        return [grouped[uid] for uid in user_ids]"
                ),
                "explanation": "Batches individual user order requests across the execution tree into a single vectorized query."
            },
            {
                "title": "DataLoader Resolver Usage",
                "language": "python",
                "code": (
                    "@strawberry.type\n"
                    "class User:\n"
                    "    id: strawberry.ID\n"
                    "    name: str\n\n"
                    "    @strawberry.field\n"
                    "    async def orders(self, info) -> list[Order]:\n"
                    "        # Does NOT hit database directly; registers with request loader\n"
                    "        loader = info.context['order_loader']\n"
                    "        return await loader.load(self.id)"
                ),
                "explanation": "Resolvers delegate fetching to the DataLoader instance attached to per-request context."
            }
        ],
        coding_challenge={
            "title": "Simulate DataLoader Key Batching",
            "instructions": "Write a class `SimpleBatcher` with method `queue(id)` and `flush(fetch_function)`. `queue` collects IDs. When `flush` is called, it passes the unique list of collected IDs to `fetch_function` once and returns the batch result.",
            "starter_code": (
                "class SimpleBatcher:\n"
                "    def __init__(self):\n"
                "        self.keys = []\n\n"
                "    def queue(self, key):\n"
                "        pass\n\n"
                "    def flush(self, fetch_fn):\n"
                "        pass\n"
            ),
            "solution_code": (
                "class SimpleBatcher:\n"
                "    def __init__(self):\n"
                "        self.keys = []\n\n"
                "    def queue(self, key):\n"
                "        self.keys.append(key)\n\n"
                "    def flush(self, fetch_fn):\n"
                "        unique_keys = list(set(self.keys))\n"
                "        self.keys = []\n"
                "        return fetch_fn(unique_keys)\n\n"
                "def mock_db_in_query(ids):\n"
                "    return f'SELECT * WHERE id IN {sorted(ids)}'\n\n"
                "batcher = SimpleBatcher()\n"
                "batcher.queue(10)\n"
                "batcher.queue(20)\n"
                "batcher.queue(10)\n"
                "print(batcher.flush(mock_db_in_query))"
            ),
            "expected_output": "SELECT * WHERE id IN [10, 20]"
        },
        quizzes=[
            {
                "question": "What is the primary difference between a GraphQL Query and a GraphQL Mutation?",
                "options": [
                    "Queries are for reading data; Mutations are for writing/modifying data on the server",
                    "Queries use WebSockets while Mutations only use UDP",
                    "Mutations cannot accept input arguments",
                    "Queries are only supported in mobile applications"
                ],
                "correct_answer": "Queries are for reading data; Mutations are for writing/modifying data on the server",
                "explanation": "By GraphQL convention and specification, Mutations perform state-modifying side effects, while Queries are read-only."
            },
            {
                "question": "Why is the DataLoader pattern critical in GraphQL backend servers?",
                "options": [
                    "It eliminates the N+1 database query problem by batching and caching field fetches",
                    "It converts JSON into binary protobuf automatically",
                    "It compresses HTTP responses with Brotli algorithms",
                    "It manages JWT token generation"
                ],
                "correct_answer": "It eliminates the N+1 database query problem by batching and caching field fetches",
                "explanation": "DataLoader collects individual resolver calls across the query graph and consolidates them into single batch queries."
            },
            {
                "question": "Which GraphQL keyword is used to declare complex structured arguments for mutations?",
                "options": [
                    "input",
                    "struct",
                    "payload",
                    "argset"
                ],
                "correct_answer": "input",
                "explanation": "The `input` keyword defines input object types specifically intended for query and mutation arguments."
            },
            {
                "question": "What unique capability does a GraphQL mutation offer compared to standard REST `POST` responses?",
                "options": [
                    "Clients can immediately specify the exact fields and nested relationships they want returned after the modification",
                    "Mutations automatically bypass database transaction locks",
                    "Mutations execute without an internet connection",
                    "Mutations are idempotent by default"
                ],
                "correct_answer": "Clients can immediately specify the exact fields and nested relationships they want returned after the modification",
                "explanation": "Clients can request the new object, updated timestamps, or nested related collections in the same mutation payload."
            },
            {
                "question": "At what lifecycle scope should DataLoader instances typically be initialized in a web server?",
                "options": [
                    "Per-request context (to ensure isolated caching across different user requests)",
                    "Globally across the entire lifetime of the server process",
                    "Only on server boot before any requests arrive",
                    "Stored permanently inside the client's localStorage"
                ],
                "correct_answer": "Per-request context (to ensure isolated caching across different user requests)",
                "explanation": "DataLoaders must be scoped per request so that one user does not see cached data belonging to another user."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 48: gRPC & Protocol Buffers (Protobuf) Basics
    # ---------------------------------------------------------
    DayBlueprint(
        order=48,
        title="gRPC & Protocol Buffers (Protobuf) Basics",
        concept="gRPC is a high-performance, open-source universal Remote Procedure Call (RPC) framework developed by Google that leverages HTTP/2 transport and Protocol Buffers for compact binary serialization.",
        analogy="If REST with JSON is sending a letter written in plain English inside a paper envelope, gRPC with Protobuf is transmitting military Morse code over a fiber-optic laser: it is unreadable to human eyes, but machines process it 10x faster using 80% less bandwidth.",
        theory_sections=[
            {
                "heading": "Why gRPC? Limitations of JSON/REST for Microservices",
                "content": (
                    "While JSON over HTTP/1.1 is human-readable and universal for public web clients, it has massive overhead for high-throughput internal microservice-to-microservice traffic:\n"
                    "- **Text Serialization Overhead**: Parsing ASCII strings, brackets, and quotes consumes heavy CPU cycles.\n"
                    "- **Large Payload Footprint**: Repeated JSON keys (`\"first_name\"`, `\"shipping_address\"`) waste network bytes.\n"
                    "- **No Strict Code Contract**: REST documentation easily goes out of sync with backend code.\n\n"
                    "gRPC solves this using **Protocol Buffers** (strongly-typed binary serialization) over **HTTP/2** (multiplexing multiple calls over a single TCP connection)."
                )
            },
            {
                "heading": "Protocol Buffers (`.proto`) and Field Tags",
                "content": (
                    "In a `.proto` file, you define services and message schemas. Each field is assigned a unique integer number called a **field tag** (e.g., `string email = 1;`).\n\n"
                    "During serialization, gRPC does not transmit field names like `'email'`. It only transmits tag numbers (`1`) and binary byte values! This is why Protobuf payloads are typically 70–80% smaller than identical JSON payloads."
                )
            },
            {
                "heading": "The 4 gRPC Communication Modes",
                "content": (
                    "1. **Unary RPC**: Standard Request-Response (Client sends 1 message, Server replies with 1 message).\n"
                    "2. **Server Streaming RPC**: Client sends 1 request, Server returns a stream of multiple responses (e.g. live stock ticker).\n"
                    "3. **Client Streaming RPC**: Client streams a sequence of messages (e.g. file chunk upload), Server replies with 1 status.\n"
                    "4. **Bidirectional Streaming RPC**: Both client and server send read-write message streams independently."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Protocol Buffer Definition (`user_service.proto`)",
                "language": "protobuf",
                "code": (
                    "syntax = \"proto3\";\n"
                    "package users;\n\n"
                    "message GetUserRequest {\n"
                    "  int64 user_id = 1;\n"
                    "}\n\n"
                    "message UserResponse {\n"
                    "  int64 id = 1;\n"
                    "  string full_name = 2;\n"
                    "  string email = 3;\n"
                    "  bool is_active = 4;\n"
                    "}\n\n"
                    "service UserService {\n"
                    "  rpc GetUser (GetUserRequest) returns (UserResponse);\n"
                    "  rpc StreamActivity (GetUserRequest) returns (stream UserResponse);\n"
                    "}"
                ),
                "explanation": "Defines typed messages and a service interface. Numbers 1, 2, 3 are binary wire tags."
            },
            {
                "title": "Compiling `.proto` to Python/Go/TS Stubs",
                "language": "bash",
                "code": (
                    "# Generate Python client stubs and server interfaces\n"
                    "python -m grpc_tools.protoc \\\n"
                    "  -I. \\\n"
                    "  --python_out=. \\\n"
                    "  --grpc_python_out=. \\\n"
                    "  user_service.proto\n\n"
                    "# Produces user_service_pb2.py and user_service_pb2_grpc.py"
                ),
                "explanation": "The protoc compiler generates strongly-typed client stubs and base classes in any supported language."
            },
            {
                "title": "gRPC Server Implementation in Python",
                "language": "python",
                "code": (
                    "import grpc\n"
                    "from concurrent import futures\n"
                    "import user_service_pb2 as pb\n"
                    "import user_service_pb2_grpc as pb_grpc\n\n"
                    "class UserServiceServicer(pb_grpc.UserServiceServicer):\n"
                    "    def GetUser(self, request, context):\n"
                    "        # Strongly typed request object with request.user_id\n"
                    "        if request.user_id <= 0:\n"
                    "            context.abort(grpc.StatusCode.INVALID_ARGUMENT, 'Invalid user ID')\n"
                    "        return pb.UserResponse(\n"
                    "            id=request.user_id,\n"
                    "            full_name='Tariq Aziz',\n"
                    "            email='tariq@example.com',\n"
                    "            is_active=True\n"
                    "        )\n\n"
                    "server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))\n"
                    "pb_grpc.add_UserServiceServicer_to_server(UserServiceServicer(), server)\n"
                    "server.add_insecure_port('[::]:50051')\n"
                    "server.start()"
                ),
                "explanation": "Implements the RPC method with native gRPC status codes and binary response generation."
            },
            {
                "title": "gRPC Client Calling the Remote Service",
                "language": "python",
                "code": (
                    "import grpc\n"
                    "import user_service_pb2 as pb\n"
                    "import user_service_pb2_grpc as pb_grpc\n\n"
                    "with grpc.insecure_channel('localhost:50051') as channel:\n"
                    "    stub = pb_grpc.UserServiceStub(channel)\n"
                    "    request = pb.GetUserRequest(user_id=42)\n"
                    "    response = stub.GetUser(request)\n"
                    "    print(f'User: {response.full_name}, Email: {response.email}')"
                ),
                "explanation": "Client calls remote method as if it were a local in-memory function call."
            }
        ],
        coding_challenge={
            "title": "Protobuf Tag-to-Field Encoder Simulation",
            "instructions": "Write a function `encode_protobuf_mock(field_tag_map, data_dict)` that serializes data into a simplified binary mock structure: a list of tuples `[(tag, value), ...]` ignoring fields that are None or not present in the tag map.",
            "starter_code": (
                "def encode_protobuf_mock(tag_map: dict, data: dict) -> list:\n"
                "    # Return list of (tag, value) tuples for existing non-null fields\n"
                "    pass\n"
            ),
            "solution_code": (
                "def encode_protobuf_mock(tag_map: dict, data: dict) -> list:\n"
                "    encoded = []\n"
                "    for field_name, tag in tag_map.items():\n"
                "        val = data.get(field_name)\n"
                "        if val is not None:\n"
                "            encoded.append((tag, val))\n"
                "    return sorted(encoded, key=lambda x: x[0])\n\n"
                "tag_mapping = {'user_id': 1, 'email': 2, 'phone': 3}\n"
                "payload = {'user_id': 105, 'email': 'dev@test.io', 'phone': None}\n"
                "print(encode_protobuf_mock(tag_mapping, payload))"
            ),
            "expected_output": "[(1, 105), (2, 'dev@test.io')]"
        },
        quizzes=[
            {
                "question": "What underlying transport protocol does gRPC use to achieve multiplexing and streaming?",
                "options": [
                    "HTTP/2",
                    "HTTP/0.9",
                    "FTP",
                    "Telnet"
                ],
                "correct_answer": "HTTP/2",
                "explanation": "gRPC relies on HTTP/2 for bidirectional streaming, header compression (HPACK), and multiplexing requests over one TCP socket."
            },
            {
                "question": "Why do Protocol Buffer payloads consume significantly less bandwidth than JSON?",
                "options": [
                    "Protobuf encodes data into binary and transmits field tag numbers instead of repetitive string field names",
                    "Protobuf automatically deletes all database records",
                    "Protobuf only allows 1 byte per message",
                    "Protobuf runs over raw Bluetooth only"
                ],
                "correct_answer": "Protobuf encodes data into binary and transmits field tag numbers instead of repetitive string field names",
                "explanation": "Field tag numbers (1, 2, 3) replace keys like 'first_name', resulting in extremely compact binary messages."
            },
            {
                "question": "What is the primary role of the `protoc` compiler in a gRPC development workflow?",
                "options": [
                    "It reads `.proto` files and automatically generates strongly typed client stubs and server boilerplate in multiple programming languages",
                    "It compiles Python code into C++ binaries",
                    "It runs SQL migrations",
                    "It formats HTML files for browser rendering"
                ],
                "correct_answer": "It reads `.proto` files and automatically generates strongly typed client stubs and server boilerplate in multiple programming languages",
                "explanation": "`protoc` translates the language-neutral `.proto` interface definitions into native target language classes."
            },
            {
                "question": "Which gRPC streaming pattern involves the client sending one request and receiving a continuous sequence of messages from the server?",
                "options": [
                    "Server Streaming RPC",
                    "Unary RPC",
                    "Client Streaming RPC",
                    "Circular Polling RPC"
                ],
                "correct_answer": "Server Streaming RPC",
                "explanation": "In Server Streaming RPC, the client sends a single request and gets a stream to read incoming messages sequentially."
            },
            {
                "question": "Where is gRPC most commonly adopted in modern software architecture?",
                "options": [
                    "Inter-service communication between backend microservices where low latency and high throughput are critical",
                    "Public browser frontend scripts interacting with legacy search engines",
                    "Rendering static HTML WordPress blogs",
                    "Writing simple Bash scripts"
                ],
                "correct_answer": "Inter-service communication between backend microservices where low latency and high throughput are critical",
                "explanation": "Microservice backends use gRPC for high-throughput, low-latency RPC communication with strict schema guarantees."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 49: API Specification Standards: OpenAPI & Swagger
    # ---------------------------------------------------------
    DayBlueprint(
        order=49,
        title="API Specification Standards: OpenAPI & Swagger",
        concept="The OpenAPI Specification (OAS) is a machine-readable, vendor-neutral standard for describing RESTful APIs in YAML or JSON, powering automated documentation, client SDK generation, and contract testing.",
        analogy="OpenAPI is like the architectural blueprint for an office skyscraper. The blueprint tells the electricians, plumbers, construction workers, and city inspectors exactly where every pipe, wire, and door is before any brick is laid.",
        theory_sections=[
            {
                "heading": "OpenAPI Specification vs Swagger",
                "content": (
                    "Engineers often use 'Swagger' and 'OpenAPI' interchangeably, but there is a clear distinction:\n"
                    "- **OpenAPI Specification (OAS)**: The open-source, industry-standard specification format maintained by the Linux Foundation (currently OpenAPI 3.0 / 3.1).\n"
                    "- **Swagger**: The suite of commercial and open-source tooling created by SmartBear (such as Swagger UI, Swagger Editor, and Swagger Codegen) that implements OAS."
                )
            },
            {
                "heading": "Core Anatomical Structure of an OAS 3.0 Document",
                "content": (
                    "An OpenAPI document is structured into mandatory key sections:\n"
                    "1. `openapi`: The version string (e.g. `3.0.3` or `3.1.0`).\n"
                    "2. `info`: API metadata (`title`, `version`, `description`, `contact`, `license`).\n"
                    "3. `servers`: Target environments (`https://api.domain.com/v1`, `http://localhost:8000`).\n"
                    "4. `paths`: The API endpoints and supported HTTP operations (`/users/{id}`, `get`, `post`).\n"
                    "5. `components`: Reusable schemas (`components.schemas.User`), security schemes (`BearerAuth`), and responses (`$ref`)."
                )
            },
            {
                "heading": "Design-First vs Code-First API Development",
                "content": (
                    "- **Design-First**: Product managers and engineers write the `openapi.yaml` contract before writing any backend code. Frontend and backend teams can work in parallel using mock servers generated from the specification.\n"
                    "- **Code-First**: Developers write controller code and annotations (e.g. FastAPI Pydantic models, Spring Boot `@Schema`), and the framework automatically generates the OpenAPI JSON at runtime."
                )
            }
        ],
        code_snippets=[
            {
                "title": "OpenAPI 3.0 YAML Document (`openapi.yaml`)",
                "language": "yaml",
                "code": (
                    "openapi: 3.0.3\n"
                    "info:\n"
                    "  title: User Directory API\n"
                    "  version: 1.0.0\n"
                    "  description: Core authentication and user management API\n"
                    "servers:\n"
                    "  - url: https://api.example.com/v1\n"
                    "    description: Production Server\n"
                    "paths:\n"
                    "  /users/{id}:\n"
                    "    get:\n"
                    "      summary: Retrieve user by ID\n"
                    "      parameters:\n"
                    "        - name: id\n"
                    "          in: path\n"
                    "          required: true\n"
                    "          schema:\n"
                    "            type: integer\n"
                    "      responses:\n"
                    "        '200':\n"
                    "          description: User found\n"
                    "          content:\n"
                    "            application/json:\n"
                    "              schema:\n"
                    "                $ref: '#/components/schemas/User'\n"
                    "        '404':\n"
                    "          description: User not found\n"
                    "components:\n"
                    "  schemas:\n"
                    "    User:\n"
                    "      type: object\n"
                    "      required: [id, username]\n"
                    "      properties:\n"
                    "        id:\n"
                    "          type: integer\n"
                    "        username:\n"
                    "          type: string"
                ),
                "explanation": "Standard OAS 3.0 document showing parameters, response status codes, and reusable component references."
            },
            {
                "title": "Automated OpenAPI Generation with FastAPI",
                "language": "python",
                "code": (
                    "from fastapi import FastAPI, Path\n"
                    "from pydantic import BaseModel, Field\n\n"
                    "app = FastAPI(title='User Directory API', version='1.0.0')\n\n"
                    "class UserSchema(BaseModel):\n"
                    "    id: int = Field(..., example=42)\n"
                    "    username: str = Field(..., min_length=3, example='johndoe')\n\n"
                    "@app.get('/users/{id}', response_model=UserSchema, summary='Retrieve user by ID')\n"
                    "def get_user(id: int = Path(..., gt=0)):\n"
                    "    return {'id': id, 'username': 'johndoe'}\n\n"
                    "# FastAPI automatically generates OpenAPI JSON at /openapi.json and Swagger at /docs"
                ),
                "explanation": "Code-first approach where Pydantic models automatically render interactive Swagger UI."
            },
            {
                "title": "Security Schemes in OpenAPI",
                "language": "yaml",
                "code": (
                    "components:\n"
                    "  securitySchemes:\n"
                    "    BearerJWT:\n"
                    "      type: http\n"
                    "      scheme: bearer\n"
                    "      bearerFormat: JWT\n"
                    "security:\n"
                    "  - BearerJWT: []"
                ),
                "explanation": "Enforces global JWT authorization across all endpoints defined in the specification."
            },
            {
                "title": "Generating Client SDK with OpenAPI CLI",
                "language": "bash",
                "code": (
                    "# Generate complete TypeScript Axios client from openapi.yaml\n"
                    "npx @openapitools/openapi-generator-cli generate \\\n"
                    "  -i openapi.yaml \\\n"
                    "  -g typescript-axios \\\n"
                    "  -o ./generated-client\n\n"
                    "# Developers can now import { UsersApi } from './generated-client'"
                ),
                "explanation": "Generates fully typed client SDKs in TypeScript, Java, Python, or Go directly from the contract."
            }
        ],
        coding_challenge={
            "title": "Generate Minimal OpenAPI Path Object",
            "instructions": "Write a function `build_openapi_path(endpoint, method, summary, response_schema_ref)` that constructs a Python dictionary corresponding to a valid OpenAPI 3.0 path specification item.",
            "starter_code": (
                "def build_openapi_path(endpoint: str, method: str, summary: str, schema_ref: str) -> dict:\n"
                "    # Return nested OpenAPI path dictionary\n"
                "    pass\n"
            ),
            "solution_code": (
                "def build_openapi_path(endpoint: str, method: str, summary: str, schema_ref: str) -> dict:\n"
                "    return {\n"
                "        endpoint: {\n"
                "            method.lower(): {\n"
                "                'summary': summary,\n"
                "                'responses': {\n"
                "                    '200': {\n"
                "                        'description': 'OK',\n"
                "                        'content': {\n"
                "                            'application/json': {\n"
                "                                'schema': {'$ref': f'#/components/schemas/{schema_ref}'}\n"
                "                            }\n"
                "                        }\n"
                "                    }\n"
                "                }\n"
                "            }\n"
                "        }\n"
                "    }\n\n"
                "print(build_openapi_path('/items', 'GET', 'List items', 'Item'))"
            ),
            "expected_output": "{'/items': {'get': {'summary': 'List items', 'responses': {'200': {'description': 'OK', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Item'}}}}}}}}"
        },
        quizzes=[
            {
                "question": "What is the relationship between Swagger and the OpenAPI Specification (OAS)?",
                "options": [
                    "OAS is the vendor-neutral standard specification; Swagger is a suite of tools (like Swagger UI) built around OAS",
                    "Swagger is for databases, while OAS is for CSS styles",
                    "They are competing proprietary protocols owned by Microsoft",
                    "OAS was discontinued in 2010 and replaced by Swagger"
                ],
                "correct_answer": "OAS is the vendor-neutral standard specification; Swagger is a suite of tools (like Swagger UI) built around OAS",
                "explanation": "The specification was donated to the Linux Foundation and renamed OpenAPI; Swagger remains the tool brand."
            },
            {
                "question": "What does `$ref: '#/components/schemas/User'` accomplish in an OpenAPI document?",
                "options": [
                    "It references a reusable data schema definition to prevent duplicate code across endpoints",
                    "It redirects the user's browser to an external website",
                    "It marks the field as a cryptographic hash",
                    "It executes a SQL query on server startup"
                ],
                "correct_answer": "It references a reusable data schema definition to prevent duplicate code across endpoints",
                "explanation": "`$ref` enables DRY (Don't Repeat Yourself) design by referencing shared schemas in `components.schemas`."
            },
            {
                "question": "Which philosophy advocates drafting the OpenAPI specification before implementing backend controller code?",
                "options": [
                    "Design-First (API-First)",
                    "Code-First",
                    "Waterfall Database Modeling",
                    "Chaos Engineering"
                ],
                "correct_answer": "Design-First (API-First)",
                "explanation": "Design-First allows frontend and backend teams to align on contracts and mock APIs before code is written."
            },
            {
                "question": "Which tool dynamically renders an interactive HTML webpage allowing developers to test API endpoints directly in the browser?",
                "options": [
                    "Swagger UI",
                    "Vim",
                    "Docker Daemon",
                    "PostgreSQL pg_dump"
                ],
                "correct_answer": "Swagger UI",
                "explanation": "Swagger UI reads OpenAPI YAML/JSON specs and generates interactive sandbox documentation."
            },
            {
                "question": "Under which top-level OpenAPI 3.x key are target environment base URLs declared?",
                "options": [
                    "servers",
                    "hosts",
                    "base_urls",
                    "deployments"
                ],
                "correct_answer": "servers",
                "explanation": "The `servers` array defines target base URLs (production, staging, mock) in OpenAPI 3.x."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 50: Writing Clear API Documentation & Developer Experience (DX)
    # ---------------------------------------------------------
    DayBlueprint(
        order=50,
        title="Writing Clear API Documentation & Developer Experience (DX)",
        concept="World-class API documentation provides accurate examples, realistic payloads, authentication guides, error troubleshooting, and SDKs, turning complex interfaces into seamless developer experiences (DX).",
        analogy="Documentation is like an instruction manual and dashboard for an exotic sports car. If the manual has missing pages, wrong gear indicators, or confusing warnings, even the most powerful engine is useless because the driver will crash on mile one.",
        theory_sections=[
            {
                "heading": "The 3 Pillars of API Documentation",
                "content": (
                    "High-quality API documentation requires three complementary elements:\n"
                    "1. **Reference Docs**: Comprehensive list of endpoints, verbs, parameters, types, headers, and HTTP status codes (e.g. Swagger UI, ReDoc).\n"
                    "2. **Quickstart Guides & Tutorials**: Step-by-step onboarding showing how to get an API key and make a successful 'Hello World' call in under 5 minutes.\n"
                    "3. **Guides & Conceptual Architecture**: Explaining webhooks, pagination, rate-limit headers, idempotency keys, and error recovery strategies."
                )
            },
            {
                "heading": "Documentation Tooling: ReDoc, Mintlify & Postman",
                "content": (
                    "- **ReDoc**: Generates clean 3-panel responsive web documentation (navigation on left, descriptions in center, code snippets/examples on right).\n"
                    "- **Mintlify / GitBook**: Modern documentation sites powered by MDX, combining interactive API sandboxes with rich Markdown guides.\n"
                    "- **Postman Collections & Run in Postman**: Allows third-party developers to import an entire ready-to-test workspace with preconfigured authentication in 1 click."
                )
            },
            {
                "heading": "Developer Experience (DX) Best Practices",
                "content": (
                    "- **Multi-Language Snippets**: Provide copy-pasteable snippets in cURL, JavaScript (Fetch/Axios), Python (Requests), and Go.\n"
                    "- **Real-World Examples**: Avoid generic `foo`/`bar` values. Use realistic business names, ISO dates (`2026-03-31T08:00:00Z`), and valid emails.\n"
                    "- **Exhaustive Error Codes**: Document every possible 4xx error code (e.g., `INSUFFICIENT_FUNDS`, `RATE_LIMIT_EXCEEDED`) and remediation steps."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Clear Endpoint Markdown Documentation Template",
                "language": "markdown",
                "code": (
                    "### Create Refund\n"
                    "`POST /v1/payments/{payment_id}/refunds`\n\n"
                    "Issues a full or partial refund for a settled payment.\n\n"
                    "#### Headers\n"
                    "| Header | Type | Required | Description |\n"
                    "| --- | --- | --- | --- |\n"
                    "| `Authorization` | `string` | Yes | Bearer API token |\n"
                    "| `Idempotency-Key` | `string` | Yes | UUID v4 to prevent duplicate refunds |\n\n"
                    "#### Request Body\n"
                    "```json\n"
                    "{\n"
                    "  \"amount_cents\": 2500,\n"
                    "  \"reason\": \"customer_request\"\n"
                    "}\n"
                    "```"
                ),
                "explanation": "Clear markdown documenting headers, URL parameters, required constraints, and realistic payload."
            },
            {
                "title": "Multi-Language cURL & Python Docs Snippets",
                "language": "bash",
                "code": (
                    "# cURL Example\n"
                    "curl -X POST https://api.stripe.com/v1/refunds \\\n"
                    "  -u sk_test_51Nz...: \\\n"
                    "  -d payment_intent=pi_3MtwBwLkd \\\n"
                    "  -d amount=1000\n\n"
                    "# Python (Requests)\n"
                    "import requests\n"
                    "response = requests.post(\n"
                    "    'https://api.stripe.com/v1/refunds',\n"
                    "    auth=('sk_test_51Nz...', ''),\n"
                    "    data={'payment_intent': 'pi_3MtwBwLkd', 'amount': 1000}\n"
                    ")"
                ),
                "explanation": "Providing code samples across popular client languages accelerates developer integration."
            },
            {
                "title": "Postman Collection v2.1 JSON Schema Snippet",
                "language": "json",
                "code": (
                    "{\n"
                    "  \"info\": {\n"
                    "    \"name\": \"FinTech Core API\",\n"
                    "    \"schema\": \"https://schema.getpostman.com/json/collection/v2.1.0/collection.json\"\n"
                    "  },\n"
                    "  \"item\": [\n"
                    "    {\n"
                    "      \"name\": \"Create Refund\",\n"
                    "      \"request\": {\n"
                    "        \"method\": \"POST\",\n"
                    "        \"header\": [{\"key\": \"Idempotency-Key\", \"value\": \"{{$guid}}\"}],\n"
                    "        \"url\": {\"raw\": \"{{base_url}}/v1/refunds\"}\n"
                    "      }\n"
                    "    }\n"
                    "  ]\n"
                    "}"
                ),
                "explanation": "Postman collection metadata allowing instant import with environment variables."
            },
            {
                "title": "Interactive Redoc HTML Embedding",
                "language": "html",
                "code": (
                    "<!DOCTYPE html>\n"
                    "<html>\n"
                    "  <head>\n"
                    "    <title>API Documentation</title>\n"
                    "    <meta charset=\"utf-8\"/>\n"
                    "    <script src=\"https://cdn.redoc.ly/redoc/latest/bundles/redoc.standalone.js\"></script>\n"
                    "  </head>\n"
                    "  <body>\n"
                    "    <redoc spec-url=\"/openapi.json\"></redoc>\n"
                    "  </body>\n"
                    "</html>"
                ),
                "explanation": "Serves a fast, responsive 3-panel API documentation portal directly from an OpenAPI specification."
            }
        ],
        coding_challenge={
            "title": "Format Markdown Table for API Query Parameters",
            "instructions": "Write a function `generate_param_table(params_list)` that takes a list of parameter dictionaries `[{'name': 'page', 'type': 'int', 'required': False, 'desc': 'Page number'}]` and returns a formatted Markdown table string.",
            "starter_code": (
                "def generate_param_table(params: list) -> str:\n"
                "    # Return GitHub-flavored markdown table\n"
                "    pass\n"
            ),
            "solution_code": (
                "def generate_param_table(params: list) -> str:\n"
                "    lines = [\n"
                "        '| Parameter | Type | Required | Description |',\n"
                "        '| --- | --- | --- | --- |'\n"
                "    ]\n"
                "    for p in params:\n"
                "        req = 'Yes' if p.get('required') else 'No'\n"
                "        lines.append(f\"| `{p['name']}` | `{p['type']}` | {req} | {p['desc']} |\")\n"
                "    return '\\n'.join(lines)\n\n"
                "sample = [{'name': 'limit', 'type': 'int', 'required': False, 'desc': 'Max records'}]\n"
                "print(generate_param_table(sample))"
            ),
            "expected_output": "| Parameter | Type | Required | Description |\n| --- | --- | --- | --- |\n| `limit` | `int` | No | Max records |"
        },
        quizzes=[
            {
                "question": "What does 'DX' stand for in the context of building and publishing web APIs?",
                "options": [
                    "Developer Experience",
                    "Database XML",
                    "Data Exchange",
                    "Direct Execution"
                ],
                "correct_answer": "Developer Experience",
                "explanation": "DX (Developer Experience) measures how easily, reliably, and happily engineers can integrate with your API."
            },
            {
                "question": "Why is it important to provide realistic data in API docs instead of values like 'foo' and 'bar'?",
                "options": [
                    "Realistic values demonstrate real validation constraints (e.g. ISO 8601 dates, E.164 phone numbers) and prevent integration confusion",
                    "Computers reject requests containing the word 'foo'",
                    "Databases crash if 'bar' is stored in a column",
                    "It is legally required by internet standards"
                ],
                "correct_answer": "Realistic values demonstrate real validation constraints (e.g. ISO 8601 dates, E.164 phone numbers) and prevent integration confusion",
                "explanation": "Real examples (e.g. `\"2026-04-01T12:00:00Z\"`) clarify formatting requirements and boundary conditions."
            },
            {
                "question": "What visual design layout makes tools like ReDoc popular for developer documentation?",
                "options": [
                    "A responsive 3-column layout featuring navigation on the left, explanations in the middle, and code samples on the right",
                    "A single massive text file without any CSS formatting",
                    "Flashing neon banners and video popups",
                    "An audio podcast player only"
                ],
                "correct_answer": "A responsive 3-column layout featuring navigation on the left, explanations in the middle, and code samples on the right",
                "explanation": "The 3-panel layout allows developers to read documentation and copy code snippets side-by-side."
            },
            {
                "question": "What is the primary benefit of publishing an official Postman Collection for your API?",
                "options": [
                    "External developers can import ready-made API requests with working parameters and auth in one click",
                    "It automatically fixes database bugs",
                    "It bypasses the need for API keys",
                    "It turns REST APIs into gRPC servers"
                ],
                "correct_answer": "External developers can import ready-made API requests with working parameters and auth in one click",
                "explanation": "Postman Collections allow developers to test API endpoints immediately without manually configuring URLs and headers."
            },
            {
                "question": "Which HTTP status code and response payload should be exhaustively documented for every mutation endpoint?",
                "options": [
                    "4xx client error status codes with standardized error codes and remediation details",
                    "100 Continue status only",
                    "Empty 204 No Content responses without any explanation",
                    "500 Internal Server Error stack traces"
                ],
                "correct_answer": "4xx client error status codes with standardized error codes and remediation details",
                "explanation": "Documenting error cases (400, 401, 403, 404, 409, 422) enables developers to handle edge cases gracefully."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 51: API Unit Testing & Mocking Controller Dependencies
    # ---------------------------------------------------------
    DayBlueprint(
        order=51,
        title="API Unit Testing & Mocking Controller Dependencies",
        concept="Unit testing validates API endpoints in isolation by mocking external dependencies (databases, payment gateways, email providers) to ensure controllers handle inputs, errors, and responses deterministically.",
        analogy="Testing an API controller with mocks is like a pilot training in a flight simulator. You test how the pilot reacts to an engine fire without having to actually set an airplane on fire mid-flight.",
        theory_sections=[
            {
                "heading": "Unit Testing vs Integration Testing for APIs",
                "content": (
                    "- **Unit Testing**: Tests an individual controller function or business logic service in complete isolation. All databases, external HTTP services, and messaging queues are replaced with in-memory **mocks** or **stubs**. Tests run in milliseconds.\n"
                    "- **Integration Testing**: Boots the actual database and services to verify that SQL queries, network connections, and migrations work together as an entire system."
                )
            },
            {
                "heading": "The AAA Pattern (Arrange, Act, Assert)",
                "content": (
                    "Every API unit test should follow the AAA structure:\n"
                    "1. **Arrange**: Set up test data, configure mocked service return values, and instantiate test client.\n"
                    "2. **Act**: Dispatch the HTTP request (e.g. `client.post('/orders', json={...})`).\n"
                    "3. **Assert**: Verify the HTTP status code, response headers, response JSON body, and ensure mocked methods were invoked with correct parameters."
                )
            },
            {
                "heading": "Mocking Strategies (unittest.mock, Jest)",
                "content": (
                    "When testing `POST /checkout`, we must never charge real credit cards on Stripe. We mock the payment gateway adapter:\n"
                    "- Verify success scenario: Mock returns `{ 'status': 'succeeded', 'charge_id': 'ch_123' }` -> Assert controller returns HTTP `201 Created`.\n"
                    "- Verify failure scenario: Mock raises `CardDeclinedException` -> Assert controller intercepts exception and returns HTTP `402 Payment Required` or `400 Bad Request`."
                )
            }
        ],
        code_snippets=[
            {
                "title": "API Controller to be Tested (FastAPI)",
                "language": "python",
                "code": (
                    "from fastapi import FastAPI, HTTPException, status\n"
                    "from pydantic import BaseModel\n\n"
                    "app = FastAPI()\n\n"
                    "class OrderRequest(BaseModel):\n"
                    "    product_id: int\n"
                    "    quantity: int\n\n"
                    "# Dependency to be mocked\n"
                    "def get_order_service():\n"
                    "    raise NotImplementedError('Real DB connection')\n\n"
                    "@app.post('/orders', status_code=status.HTTP_201_CREATED)\n"
                    "def create_order(payload: OrderRequest):\n"
                    "    service = get_order_service()\n"
                    "    order = service.place_order(payload.product_id, payload.quantity)\n"
                    "    if not order:\n"
                    "        raise HTTPException(status_code=400, detail='Insufficient stock')\n"
                    "    return {'order_id': order['id'], 'status': 'placed'}"
                ),
                "explanation": "Controller relies on `order_service` to execute business logic."
            },
            {
                "title": "PyTest Unit Test with Mocked Dependency",
                "language": "python",
                "code": (
                    "from unittest.mock import MagicMock, patch\n"
                    "from fastapi.testclient import TestClient\n"
                    "from main import app\n\n"
                    "client = TestClient(app)\n\n"
                    "@patch('main.get_order_service')\n"
                    "def test_create_order_success(mock_get_service):\n"
                    "    # Arrange\n"
                    "    mock_service = MagicMock()\n"
                    "    mock_service.place_order.return_value = {'id': 999, 'status': 'placed'}\n"
                    "    mock_get_service.return_value = mock_service\n\n"
                    "    # Act\n"
                    "    response = client.post('/orders', json={'product_id': 10, 'quantity': 2})\n\n"
                    "    # Assert\n"
                    "    assert response.status_code == 201\n"
                    "    assert response.json() == {'order_id': 999, 'status': 'placed'}\n"
                    "    mock_service.place_order.assert_called_once_with(10, 2)"
                ),
                "explanation": "Tests controller logic and asserts the mocked method was called with exact parameters."
            },
            {
                "title": "Testing Error Edge Cases (Insufficient Stock)",
                "language": "python",
                "code": (
                    "@patch('main.get_order_service')\n"
                    "def test_create_order_insufficient_stock(mock_get_service):\n"
                    "    # Arrange\n"
                    "    mock_service = MagicMock()\n"
                    "    mock_service.place_order.return_value = None  # Indicates failure\n"
                    "    mock_get_service.return_value = mock_service\n\n"
                    "    # Act\n"
                    "    res = client.post('/orders', json={'product_id': 10, 'quantity': 9999})\n\n"
                    "    # Assert\n"
                    "    assert res.status_code == 400\n"
                    "    assert res.json()['detail'] == 'Insufficient stock'"
                ),
                "explanation": "Confirms error conditions return correct HTTP 400 status codes without invoking real infrastructure."
            },
            {
                "title": "Jest / Supertest API Unit Test in Node.js",
                "language": "javascript",
                "code": (
                    "const request = require('supertest');\n"
                    "const app = require('./app');\n"
                    "const userService = require('./services/userService');\n\n"
                    "jest.mock('./services/userService');\n\n"
                    "describe('GET /users/:id', () => {\n"
                    "  it('should return 200 and user object when user exists', async () => {\n"
                    "    userService.findById.mockResolvedValue({ id: 1, name: 'Bilal' });\n\n"
                    "    const res = await request(app).get('/users/1');\n"
                    "    expect(res.statusCode).toEqual(200);\n"
                    "    expect(res.body.name).toEqual('Bilal');\n"
                    "  });\n"
                    "});"
                ),
                "explanation": "Demonstrates identical unit testing and mocking principles in JavaScript/Node.js."
            }
        ],
        coding_challenge={
            "title": "Test Assertion Runner for HTTP Status Codes",
            "instructions": "Write a function `assert_api_response(response_dict, expected_status, required_keys)` that checks whether `response_dict['status_code']` matches `expected_status` and whether all `required_keys` exist in `response_dict['json']`. Return True if passed, otherwise raise ValueError with details.",
            "starter_code": (
                "def assert_api_response(resp: dict, expected_status: int, required_keys: list) -> bool:\n"
                "    # Validate status and JSON schema keys\n"
                "    pass\n"
            ),
            "solution_code": (
                "def assert_api_response(resp: dict, expected_status: int, required_keys: list) -> bool:\n"
                "    if resp.get('status_code') != expected_status:\n"
                "        raise ValueError(f\"Status mismatch: got {resp.get('status_code')}, expected {expected_status}\")\n"
                "    body = resp.get('json', {})\n"
                "    for k in required_keys:\n"
                "        if k not in body:\n"
                "            raise ValueError(f\"Missing required key in response: {k}\")\n"
                "    return True\n\n"
                "mock_res = {'status_code': 200, 'json': {'id': 1, 'name': 'Ahmed'}}\n"
                "print(assert_api_response(mock_res, 200, ['id', 'name']))"
            ),
            "expected_output": "True"
        },
        quizzes=[
            {
                "question": "What is the primary goal of unit testing an API endpoint?",
                "options": [
                    "To test the controller and business logic in isolation without invoking real external systems like databases",
                    "To test internet cable bandwidth",
                    "To run penetration attacks against production servers",
                    "To test CSS font sizes on mobile devices"
                ],
                "correct_answer": "To test the controller and business logic in isolation without invoking real external systems like databases",
                "explanation": "Unit testing verifies isolated code units by substituting external dependencies with controlled mocks."
            },
            {
                "question": "What are the three steps of the standard AAA unit testing pattern?",
                "options": [
                    "Arrange, Act, Assert",
                    "Allocate, Authenticate, Authorize",
                    "Analyze, Archive, Abandon",
                    "Add, Alter, Append"
                ],
                "correct_answer": "Arrange, Act, Assert",
                "explanation": "Arrange (setup test doubles and state), Act (execute the target function), Assert (verify return values and effects)."
            },
            {
                "question": "Why should external services like Stripe or Twilio be mocked during unit tests?",
                "options": [
                    "To prevent accidental real monetary charges, avoid rate limits, and keep tests fast and deterministic",
                    "Because external services do not allow unit tests to run",
                    "Because mocks make the test run slower",
                    "Because Python cannot connect to external web APIs"
                ],
                "correct_answer": "To prevent accidental real monetary charges, avoid rate limits, and keep tests fast and deterministic",
                "explanation": "Mocking avoids real financial transactions, external network latency, and third-party downtime."
            },
            {
                "question": "What does `mock_service.place_order.assert_called_once_with(10, 2)` verify in a unit test?",
                "options": [
                    "That the method was executed exactly once with parameters 10 and 2",
                    "That the method threw an unhandled exception",
                    "That the database table had 10 columns and 2 rows",
                    "That the test was skipped"
                ],
                "correct_answer": "That the method was executed exactly once with parameters 10 and 2",
                "explanation": "Behavior verification ensures the controller routed correct arguments to the underlying service layer."
            },
            {
                "question": "Which HTTP status code should be asserted when testing an endpoint that successfully creates a new database record?",
                "options": [
                    "201 Created",
                    "200 OK",
                    "204 No Content",
                    "301 Moved Permanently"
                ],
                "correct_answer": "201 Created",
                "explanation": "RFC specifications dictate that successful entity creation should return HTTP status 201 Created."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 52: API Integration Testing & Mocking APIs (Mock Servers)
    # ---------------------------------------------------------
    DayBlueprint(
        order=52,
        title="API Integration Testing & Mocking APIs (Mock Servers)",
        concept="Integration testing validates the interplay between controllers, actual databases, and middleware, while mock servers (WireMock, Mockoon, MSW) simulate external third-party HTTP endpoints with fidelity.",
        analogy="If a unit test checks whether a single LEGO brick is intact, an integration test snaps 10 bricks together and shakes them to make sure the castle walls don't collapse.",
        theory_sections=[
            {
                "heading": "The Purpose of API Integration Testing",
                "content": (
                    "Unit tests can pass with 100% code coverage while the application completely fails in production due to:\n"
                    "- Broken SQL queries or schema migration mismatches.\n"
                    "- Misconfigured authentication middleware.\n"
                    "- CORS headers missing in the real HTTP pipeline.\n"
                    "- JSON deserialization discrepancies.\n\n"
                    "Integration tests run against a real application instance and a dedicated test database (often spun up inside Docker containers or SQLite in-memory)."
                )
            },
            {
                "heading": "Mock Servers: WireMock, Mockoon, and MSW",
                "content": (
                    "When your API integrates with upstream services (e.g. shipping carriers, tax calculators, weather APIs), integration tests need realistic HTTP endpoints that don't fail when the internet is down:\n"
                    "- **WireMock**: A popular standalone HTTP server that allows defining request matching (regex, headers, JSON body) and stubbing dynamic responses.\n"
                    "- **Mockoon**: A lightweight GUI tool to build local mock APIs in seconds.\n"
                    "- **MSW (Mock Service Worker)**: Intercepts network calls at the network level in Node.js and browsers without altering production API client code."
                )
            },
            {
                "heading": "Test Database Isolation (Transaction Rollbacks)",
                "content": (
                    "To prevent test pollution (Test A creating a user that breaks Test B):\n"
                    "1. Wrap each test inside a database transaction.\n"
                    "2. At the end of the test, roll back the transaction instead of committing.\n"
                    "3. Or use automated database truncating/seeding fixtures before each test suite."
                )
            }
        ],
        code_snippets=[
            {
                "title": "FastAPI Integration Test with Testcontainers / SQLite",
                "language": "python",
                "code": (
                    "import pytest\n"
                    "from sqlalchemy import create_engine\n"
                    "from sqlalchemy.orm import sessionmaker\n"
                    "from fastapi.testclient import TestClient\n"
                    "from main import app, get_db, Base\n\n"
                    "# Spin up in-memory clean database for integration run\n"
                    "SQLALCHEMY_TEST_DATABASE_URL = 'sqlite:///./test.db'\n"
                    "engine = create_engine(SQLALCHEMY_TEST_DATABASE_URL, connect_args={'check_same_thread': False})\n"
                    "TestingSessionLocal = sessionmaker(bind=engine)\n\n"
                    "@pytest.fixture(scope='function')\n"
                    "def db_session():\n"
                    "    Base.metadata.create_all(bind=engine)\n"
                    "    db = TestingSessionLocal()\n"
                    "    try:\n"
                    "        yield db\n"
                    "    finally:\n"
                    "        db.close()\n"
                    "        Base.metadata.drop_all(bind=engine)"
                ),
                "explanation": "Creates clean schema tables before each test and tears them down after, ensuring isolation."
            },
            {
                "title": "Testing Complete API Pipeline with Real DB",
                "language": "python",
                "code": (
                    "def test_full_user_registration_integration(db_session):\n"
                    "    client = TestClient(app)\n"
                    "    # 1. Register User\n"
                    "    res = client.post('/api/v1/users', json={'email': 'zain@work.com', 'password': 'Password123!'})\n"
                    "    assert res.status_code == 201\n"
                    "    user_id = res.json()['id']\n\n"
                    "    # 2. Login and get JWT\n"
                    "    login_res = client.post('/api/v1/auth/login', json={'email': 'zain@work.com', 'password': 'Password123!'})\n"
                    "    assert login_res.status_code == 200\n"
                    "    token = login_res.json()['access_token']\n\n"
                    "    # 3. Access Protected Route with Token\n"
                    "    auth_header = {'Authorization': f'Bearer {token}'}\n"
                    "    me_res = client.get('/api/v1/users/me', headers=auth_header)\n"
                    "    assert me_res.status_code == 200\n"
                    "    assert me_res.json()['email'] == 'zain@work.com'"
                ),
                "explanation": "Verifies complete multi-step integration across controllers, authentication middleware, and database tables."
            },
            {
                "title": "WireMock JSON Stub Mapping (`stub_weather.json`)",
                "language": "json",
                "code": (
                    "{\n"
                    "  \"request\": {\n"
                    "    \"method\": \"GET\",\n"
                    "    \"urlPattern\": \"/v1/weather\\\\?city=.*\"\n"
                    "  },\n"
                    "  \"response\": {\n"
                    "    \"status\": 200,\n"
                    "    \"headers\": {\"Content-Type\": \"application/json\"},\n"
                    "    \"jsonBody\": {\n"
                    "      \"city\": \"Lahore\",\n"
                    "      \"temperature_celsius\": 28.5,\n"
                    "      \"condition\": \"Sunny\"\n"
                    "    }\n"
                    "  }\n"
                    "}"
                ),
                "explanation": "WireMock stub intercepting external HTTP calls with deterministic canned JSON responses."
            },
            {
                "title": "MSW (Mock Service Worker) Network Handler in Node.js",
                "language": "javascript",
                "code": (
                    "import { http, HttpResponse } from 'msw';\n"
                    "import { setupServer } from 'msw/node';\n\n"
                    "export const handlers = [\n"
                    "  http.get('https://api.github.com/users/:username', ({ params }) => {\n"
                    "    return HttpResponse.json({\n"
                    "      login: params.username,\n"
                    "      public_repos: 42\n"
                    "    });\n"
                    "  })\n"
                    "];\n\n"
                    "export const server = setupServer(...handlers);"
                ),
                "explanation": "MSW intercepts external outbound requests in Node.js integration tests transparently."
            }
        ],
        coding_challenge={
            "title": "Build a Simple In-Memory Mock Server Registry",
            "instructions": "Write a class `MockServerRegistry` with methods `add_stub(method, url_path, status, body)` and `handle_request(method, url_path)`. If a matching stub exists, return `{'status': status, 'body': body}`. Otherwise return `{'status': 404, 'body': {'error': 'Stub not found'}}`.",
            "starter_code": (
                "class MockServerRegistry:\n"
                "    def __init__(self):\n"
                "        self.stubs = {}\n\n"
                "    def add_stub(self, method: str, path: str, status: int, body: dict):\n"
                "        pass\n\n"
                "    def handle_request(self, method: str, path: str) -> dict:\n"
                "        pass\n"
            ),
            "solution_code": (
                "class MockServerRegistry:\n"
                "    def __init__(self):\n"
                "        self.stubs = {}\n\n"
                "    def add_stub(self, method: str, path: str, status: int, body: dict):\n"
                "        key = (method.upper(), path)\n"
                "        self.stubs[key] = {'status': status, 'body': body}\n\n"
                "    def handle_request(self, method: str, path: str) -> dict:\n"
                "        key = (method.upper(), path)\n"
                "        return self.stubs.get(key, {'status': 404, 'body': {'error': 'Stub not found'}})\n\n"
                "mock = MockServerRegistry()\n"
                "mock.add_stub('GET', '/api/ping', 200, {'msg': 'pong'})\n"
                "print(mock.handle_request('GET', '/api/ping'))\n"
                "print(mock.handle_request('POST', '/api/ping'))"
            ),
            "expected_output": "{'status': 200, 'body': {'msg': 'pong'}}\n{'status': 404, 'body': {'error': 'Stub not found'}}"
        },
        quizzes=[
            {
                "question": "What is the primary difference between API Unit Tests and API Integration Tests?",
                "options": [
                    "Integration tests verify multiple components together (controllers, DB, middleware), while unit tests test components in isolation",
                    "Integration tests do not use code assertions",
                    "Unit tests are only run by product managers",
                    "Integration tests can only be run once per year"
                ],
                "correct_answer": "Integration tests verify multiple components together (controllers, DB, middleware), while unit tests test components in isolation",
                "explanation": "Integration tests prove that your API wiring, databases, serialization, and auth work in concert."
            },
            {
                "question": "What is 'test pollution' in database integration testing?",
                "options": [
                    "When data created by one test affects the outcome of subsequent tests, causing intermittent failures",
                    "When hard drive disk space is corrupted by dust",
                    "When SQL queries produce warning messages in stdout",
                    "When tests are written in multiple programming languages"
                ],
                "correct_answer": "When data created by one test affects the outcome of subsequent tests, causing intermittent failures",
                "explanation": "Leftover records in the test database can violate unique constraints or skew counts in later tests."
            },
            {
                "question": "What is WireMock primarily used for?",
                "options": [
                    "Simulating external HTTP web services with configurable request matching and canned responses",
                    "Testing physical Wi-Fi cable speeds",
                    "Generating frontend CSS wireframes",
                    "Encrypting hard drives"
                ],
                "correct_answer": "Simulating external HTTP web services with configurable request matching and canned responses",
                "explanation": "WireMock acts as a mock HTTP server to simulate third-party APIs during testing."
            },
            {
                "question": "How does MSW (Mock Service Worker) intercept API requests during testing?",
                "options": [
                    "At the network layer, without requiring modifications to the application's actual HTTP client code",
                    "By rewriting production database records",
                    "By blocking the operating system's firewall",
                    "By replacing the web browser with a terminal"
                ],
                "correct_answer": "At the network layer, without requiring modifications to the application's actual HTTP client code",
                "explanation": "MSW intercepts network calls at the protocol level, allowing application code to remain completely untouched."
            },
            {
                "question": "Which database practice ensures that each integration test starts with an isolated, clean state?",
                "options": [
                    "Executing tests inside rolled-back database transactions or dropping/re-migrating test tables per suite",
                    "Using production customer data directly",
                    "Disabling foreign key constraints permanently",
                    "Never cleaning up test records"
                ],
                "correct_answer": "Executing tests inside rolled-back database transactions or dropping/re-migrating test tables per suite",
                "explanation": "Transaction rollbacks or automated database cleanups guarantee zero state leakage between tests."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 53: API Load Testing & Performance Benchmarking (k6, Artillery)
    # ---------------------------------------------------------
    DayBlueprint(
        order=53,
        title="API Load Testing & Performance Benchmarking (k6, Artillery)",
        concept="Load testing simulates concurrent virtual users hitting API endpoints under realistic traffic patterns to discover bottlenecks, measure latency percentiles (p95/p99), and establish maximum Requests Per Second (RPS).",
        analogy="Load testing is like a suspension bridge weight test. Before allowing thousands of commuter vehicles on the highway bridge, engineers load it with 50 gravel trucks to ensure the steel cables don't buckle under rush-hour strain.",
        theory_sections=[
            {
                "heading": "Critical Load Testing Terminology",
                "content": (
                    "- **Virtual Users (VUs)**: Concurrent simulated clients executing test scripts in parallel.\n"
                    "- **RPS (Requests Per Second) / Throughput**: The volume of completed HTTP requests handled per second.\n"
                    "- **Latency Percentiles (p50, p95, p99)**: Arithmetic average latency is deceptive (one slow request gets hidden by 99 fast ones). Percentiles show the worst-case experience:\n"
                    "  - **p95**: 95% of all requests completed faster than this time.\n"
                    "  - **p99**: 99% of requests completed faster than this time; only 1% suffered worse latency.\n"
                    "- **Time to First Byte (TTFB)**: Time elapsed before the server begins sending the HTTP response."
                )
            },
            {
                "heading": "The 4 Types of Load Tests",
                "content": (
                    "1. **Smoke Test**: Minimal load (1–2 VUs) to verify test scripts and endpoints are functioning.\n"
                    "2. **Load Test**: Normal and peak anticipated traffic (e.g. 500 VUs ramping over 15 minutes) to benchmark system performance against SLAs.\n"
                    "3. **Stress Test**: Pushing traffic beyond expected capacity until the system breaks, discovering the breaking point and recovery behavior.\n"
                    "4. **Spike Test**: Sudden, violent bursts of traffic (e.g. 0 to 5,000 VUs in 30 seconds) simulating flash sales or viral news."
                )
            },
            {
                "heading": "Modern Tooling: k6 vs JMeter vs Artillery",
                "content": (
                    "- **k6 (Grafana)**: Modern, developer-centric tool written in Go with test scripts in JavaScript/ES6. Extremely lightweight, executes thousands of VUs from a single laptop.\n"
                    "- **Artillery**: Node.js-based load testing tool configured via YAML scripts, popular in serverless and CI/CD pipelines.\n"
                    "- **Apache JMeter**: Mature Java GUI tool; powerful for complex enterprise legacy protocols but resource-heavy."
                )
            }
        ],
        code_snippets=[
            {
                "title": "k6 Load Test Script (`load_test.js`)",
                "language": "javascript",
                "code": (
                    "import http from 'k6/http';\n"
                    "import { check, sleep } from 'k6';\n\n"
                    "// Define load stages (Ramping Virtual Users)\n"
                    "export const options = {\n"
                    "  stages: [\n"
                    "    { duration: '30s', target: 50 },  // Ramp up to 50 VUs\n"
                    "    { duration: '1m', target: 50 },   // Stay at 50 VUs\n"
                    "    { duration: '20s', target: 0 }    // Ramp down to 0\n"
                    "  ],\n"
                    "  thresholds: {\n"
                    "    http_req_duration: ['p(95)<300'], // 95% of requests must complete under 300ms\n"
                    "    http_req_failed: ['rate<0.01']     // Error rate must stay below 1%\n"
                    "  }\n"
                    "};\n\n"
                    "export default function () {\n"
                    "  const res = http.get('https://api.example.com/v1/products');\n"
                    "  check(res, {\n"
                    "    'status is 200': (r) => r.status === 200,\n"
                    "    'body has products': (r) => r.body.includes('products')\n"
                    "  });\n"
                    "  sleep(1);\n"
                    "}"
                ),
                "explanation": "Ramps up virtual users and validates Service Level Objectives (SLOs) via automated thresholds."
            },
            {
                "title": "Executing k6 Test via CLI",
                "language": "bash",
                "code": (
                    "# Run load test script locally\n"
                    "k6 run load_test.js\n\n"
                    "# Output summary includes:\n"
                    "# http_req_duration: avg=42ms min=12ms med=35ms max=412ms p(90)=88ms p(95)=120ms\n"
                    "# http_reqs: 14200 (236.6/s)\n"
                    "# checks: 100.00% ✓ 28400 ✗ 0"
                ),
                "explanation": "Executes performance suite and prints comprehensive throughput and latency distribution."
            },
            {
                "title": "Artillery YAML Configuration (`artillery.yml`)",
                "language": "yaml",
                "code": (
                    "config:\n"
                    "  target: 'https://api.example.com'\n"
                    "  phases:\n"
                    "    - duration: 60\n"
                    "      arrivalRate: 20 # 20 new users arriving per second\n"
                    "scenarios:\n"
                    "  - flow:\n"
                    "      - get:\n"
                    "          url: '/v1/users/42'\n"
                    "          headers:\n"
                    "            Authorization: 'Bearer {{ $env.API_KEY }}'"
                ),
                "explanation": "Artillery scenario modeling arrival rate of concurrent users against an authenticated route."
            },
            {
                "title": "Python Latency Percentile Calculator",
                "language": "python",
                "code": (
                    "import math\n\n"
                    "def calculate_percentiles(latencies_ms: list) -> dict:\n"
                    "    sorted_latencies = sorted(latencies_ms)\n"
                    "    n = len(sorted_latencies)\n"
                    "    def get_p(p):\n"
                    "        idx = min(math.ceil((p / 100) * n) - 1, n - 1)\n"
                    "        return sorted_latencies[max(0, idx)]\n"
                    "    return {\n"
                    "        'p50': get_p(50),\n"
                    "        'p95': get_p(95),\n"
                    "        'p99': get_p(99),\n"
                    "        'avg': round(sum(sorted_latencies) / n, 2)\n"
                    "    }\n\n"
                    "sample = [20, 25, 28, 30, 32, 35, 40, 50, 120, 450]\n"
                    "print(calculate_percentiles(sample))"
                ),
                "explanation": "Calculates p50, p95, and p99 percentiles from a collection of raw request latencies."
            }
        ],
        coding_challenge={
            "title": "Calculate 95th Percentile Latency",
            "instructions": "Write a function `p95_latency(latencies)` that takes a list of response times (integers or floats) and returns the 95th percentile value using nearest-rank method.",
            "starter_code": (
                "import math\n\n"
                "def p95_latency(latencies: list) -> float:\n"
                "    # Return 95th percentile latency\n"
                "    pass\n"
            ),
            "solution_code": (
                "import math\n\n"
                "def p95_latency(latencies: list) -> float:\n"
                "    if not latencies:\n"
                "        return 0.0\n"
                "    s = sorted(latencies)\n"
                "    idx = math.ceil(0.95 * len(s)) - 1\n"
                "    return s[min(max(0, idx), len(s) - 1)]\n\n"
                "times = [10, 12, 15, 20, 22, 25, 30, 35, 40, 50, 60, 70, 80, 90, 100, 120, 150, 200, 300, 1000]\n"
                "print(p95_latency(times))"
            ),
            "expected_output": "300"
        },
        quizzes=[
            {
                "question": "Why is p95 or p99 latency preferred over average (mean) latency when evaluating API performance?",
                "options": [
                    "Average latency hides slow outliers; percentiles reveal the worst-case latency experienced by the slowest 1% to 5% of users",
                    "Percentiles are calculated without math",
                    "Average latency is illegal under GDPR regulations",
                    "Percentiles only measure network cables"
                ],
                "correct_answer": "Average latency hides slow outliers; percentiles reveal the worst-case latency experienced by the slowest 1% to 5% of users",
                "explanation": "In an API with 99 fast requests (10ms) and 1 catastrophic freeze (10,000ms), the average looks acceptable while users suffer."
            },
            {
                "question": "What is the primary difference between a Load Test and a Stress Test?",
                "options": [
                    "A Load Test measures performance under expected peak traffic; a Stress Test pushes load beyond limits until the API breaks",
                    "Stress tests only use GET requests",
                    "Load tests are run manually by typing in browser tabs",
                    "Stress tests require disabling SSL certificates"
                ],
                "correct_answer": "A Load Test measures performance under expected peak traffic; a Stress Test pushes load beyond limits until the API breaks",
                "explanation": "Stress tests identify the catastrophic breaking point and test how gracefully the system recovers from overload."
            },
            {
                "question": "In k6 load testing scripts, what does a 'threshold' definition accomplish?",
                "options": [
                    "It defines programmatic pass/fail criteria (e.g. `p(95) < 200ms`) that can fail CI/CD build pipelines if violated",
                    "It limits the maximum file size of the codebase",
                    "It charges the user's credit card for test duration",
                    "It generates random passwords"
                ],
                "correct_answer": "It defines programmatic pass/fail criteria (e.g. `p(95) < 200ms`) that can fail CI/CD build pipelines if violated",
                "explanation": "Thresholds enforce Service Level Agreements (SLAs) directly inside continuous integration pipelines."
            },
            {
                "question": "What does 'VU' stand for in load testing frameworks like k6 and Artillery?",
                "options": [
                    "Virtual User",
                    "Variable URL",
                    "Verified UUID",
                    "Vector Unit"
                ],
                "correct_answer": "Virtual User",
                "explanation": "Virtual Users simulate independent client threads executing user journeys concurrently."
            },
            {
                "question": "What is a 'Spike Test' designed to evaluate?",
                "options": [
                    "How an API handles sudden, dramatic surges in traffic in seconds (e.g. a flash ticket sale or breaking news push)",
                    "How the server operates when unplugged from electricity",
                    "Whether code is formatted with Prettier",
                    "How the API responds to slow dial-up internet"
                ],
                "correct_answer": "How an API handles sudden, dramatic surges in traffic in seconds (e.g. a flash ticket sale or breaking news push)",
                "explanation": "Spike tests measure autoscaling reaction time and database connection pool behavior during sudden bursts."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 54: API Gateways: Kong, AWS API Gateway, and NGINX
    # ---------------------------------------------------------
    DayBlueprint(
        order=54,
        title="API Gateways: Kong, AWS API Gateway, and NGINX",
        concept="An API Gateway is a central entry point that sits between external clients and internal backend services, decoupling cross-cutting concerns like routing, SSL termination, rate limiting, and authentication.",
        analogy="An API Gateway is like the security check and front desk at the entrance of a high-security corporate skyscraper. Visitors don't wander directly into individual executive offices; they show their ID at the front desk, get screened, and are escorted to the right room.",
        theory_sections=[
            {
                "heading": "Why Use an API Gateway?",
                "content": (
                    "In a microservices architecture, having 50 different microservices directly exposed to the internet creates chaos:\n"
                    "- Every microservice would have to re-implement JWT verification, rate limiting, and CORS headers.\n"
                    "- Clients would need to know 50 different domain names and ports.\n"
                    "- Any refactoring of internal services breaks mobile apps.\n\n"
                    "An **API Gateway** provides a unified reverse-proxy facade. Clients only communicate with `https://api.company.com`, and the Gateway dispatches requests internally."
                )
            },
            {
                "heading": "Core Responsibilities of an API Gateway",
                "content": (
                    "1. **Reverse Proxy & Dynamic Routing**: Maps `/v1/users/*` to the User Service, and `/v1/billing/*` to the Billing Service.\n"
                    "2. **Authentication Offloading**: Verifies JWT signatures or API keys once at the edge. Downstream microservices can trust the parsed `X-User-ID` header.\n"
                    "3. **Traffic Management**: Enforces global rate limiting, IP whitelisting/blacklisting, circuit breakers, and canary deployments.\n"
                    "4. **Protocol Transformation**: Translates external HTTP/JSON requests into internal gRPC calls."
                )
            },
            {
                "heading": "Leading API Gateway Solutions",
                "content": (
                    "- **Kong Gateway**: Open-source, cloud-native gateway built on top of NGINX and OpenResty, extensible via Lua/Go/Python plugins.\n"
                    "- **AWS API Gateway**: Fully managed serverless gateway with native IAM auth and AWS Lambda integration.\n"
                    "- **NGINX / Envoy**: Ultra-high-performance reverse proxies often used as the foundation for modern cloud gateways."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Kong Declarative Gateway Configuration (`kong.yml`)",
                "language": "yaml",
                "code": (
                    "_format_version: '3.0'\n"
                    "services:\n"
                    "  - name: user-service\n"
                    "    url: http://user-backend.internal:8001\n"
                    "    routes:\n"
                    "      - name: user-routes\n"
                    "        paths:\n"
                    "          - /v1/users\n"
                    "    plugins:\n"
                    "      - name: key-auth\n"
                    "      - name: rate-limiting\n"
                    "        config:\n"
                    "          minute: 100\n"
                    "          policy: redis\n"
                    "          redis_host: redis.internal"
                ),
                "explanation": "Configures reverse proxy routing, API key verification, and distributed Redis rate limiting declaratively."
            },
            {
                "title": "NGINX Reverse Proxy Configuration (`nginx.conf`)",
                "language": "nginx",
                "code": (
                    "upstream auth_service {\n"
                    "    server 127.0.0.1:5001;\n"
                    "}\n\n"
                    "upstream order_service {\n"
                    "    server 127.0.0.1:5002;\n"
                    "}\n\n"
                    "server {\n"
                    "    listen 80;\n"
                    "    server_name api.example.com;\n\n"
                    "    location /auth/ {\n"
                    "        proxy_pass http://auth_service/;\n"
                    "        proxy_set_header Host $host;\n"
                    "        proxy_set_header X-Real-IP $remote_addr;\n"
                    "    }\n\n"
                    "    location /orders/ {\n"
                    "        proxy_pass http://order_service/;\n"
                    "        proxy_set_header Host $host;\n"
                    "    }\n"
                    "}"
                ),
                "explanation": "NGINX routes incoming URL prefixes to isolated internal microservice port clusters."
            },
            {
                "title": "FastAPI Downstream Service Consuming Gateway Headers",
                "language": "python",
                "code": (
                    "from fastapi import FastAPI, Header, HTTPException\n\n"
                    "app = FastAPI()\n\n"
                    "@app.get('/internal/orders')\n"
                    "def get_orders(x_user_id: str = Header(None)):\n"
                    "    # Downstream service does NOT re-verify JWT cryptographic signature.\n"
                    "    # It trusts X-User-ID injected securely by the API Gateway.\n"
                    "    if not x_user_id:\n"
                    "        raise HTTPException(status_code=401, detail='Missing Gateway context')\n"
                    "    return {'user_id': x_user_id, 'orders': ['order_1', 'order_2']}"
                ),
                "explanation": "Demonstrates auth offloading: gateway terminates auth and injects validated identity headers."
            },
            {
                "title": "AWS API Gateway OpenAPI Extension (`x-amazon-apigateway-integration`)",
                "language": "yaml",
                "code": (
                    "paths:\n"
                    "  /products:\n"
                    "    get:\n"
                    "      x-amazon-apigateway-integration:\n"
                    "        uri: arn:aws:apigateway:us-east-1:lambda:path/2015-03-31/functions/arn:aws:lambda:.../invocations\n"
                    "        httpMethod: POST\n"
                    "        type: aws_proxy\n"
                    "      responses:\n"
                    "        '200':\n"
                    "          description: OK"
                ),
                "explanation": "Maps API Gateway HTTP endpoint directly to a serverless AWS Lambda function."
            }
        ],
        coding_challenge={
            "title": "Simulate API Gateway URL Prefix Router",
            "instructions": "Write a function `gateway_route(incoming_path, routes_map)` where `routes_map` maps path prefixes to target upstream URLs. Return a dictionary `{'upstream_url': ..., 'target_path': ...}`. If no prefix matches, return None.",
            "starter_code": (
                "def gateway_route(path: str, routes: dict) -> dict:\n"
                "    # Match longest prefix and return upstream routing details\n"
                "    pass\n"
            ),
            "solution_code": (
                "def gateway_route(path: str, routes: dict) -> dict:\n"
                "    for prefix, upstream in sorted(routes.items(), key=lambda x: len(x[0]), reverse=True):\n"
                "        if path.startswith(prefix):\n"
                "            remaining = path[len(prefix):]\n"
                "            target = '/' + remaining.lstrip('/') if remaining else '/'\n"
                "            return {'upstream_url': upstream, 'target_path': target}\n"
                "    return None\n\n"
                "route_table = {'/v1/auth': 'http://auth-svc:5000', '/v1/billing': 'http://billing-svc:7000'}\n"
                "print(gateway_route('/v1/billing/invoices/10', route_table))"
            ),
            "expected_output": "{'upstream_url': 'http://billing-svc:7000', 'target_path': '/invoices/10'}"
        },
        quizzes=[
            {
                "question": "What is the primary role of an API Gateway in a modern microservices architecture?",
                "options": [
                    "A single reverse-proxy entry point that handles cross-cutting concerns like routing, rate limiting, and auth",
                    "A physical Wi-Fi router in the server room",
                    "A relational database storing user records",
                    "A compiler that translates Python into C++"
                ],
                "correct_answer": "A single reverse-proxy entry point that handles cross-cutting concerns like routing, rate limiting, and auth",
                "explanation": "The Gateway protects internal services from direct internet exposure and centralizes governance."
            },
            {
                "question": "What is 'Authentication Offloading' in an API Gateway?",
                "options": [
                    "The gateway validates JWTs or API keys at the edge, forwarding verified identity headers to internal services",
                    "Disabling all passwords on user accounts",
                    "Storing passwords in plain text on client phones",
                    "Requiring users to log in before every HTTP GET packet"
                ],
                "correct_answer": "The gateway validates JWTs or API keys at the edge, forwarding verified identity headers to internal services",
                "explanation": "Offloading relieves individual microservices from redundantly decrypting and verifying tokens."
            },
            {
                "question": "Which popular open-source API Gateway is built on top of NGINX and OpenResty?",
                "options": [
                    "Kong",
                    "Kubernetes",
                    "Docker Swarm",
                    "Apache Cassandra"
                ],
                "correct_answer": "Kong",
                "explanation": "Kong is built on NGINX and OpenResty to provide high performance and plugin extensibility."
            },
            {
                "question": "How does an API Gateway help protect internal microservices during a denial-of-service (DDoS) attempt?",
                "options": [
                    "By enforcing rate limiting and IP blocking at the perimeter before traffic hits internal backends",
                    "By turning off the database server",
                    "By clearing DNS records permanently",
                    "By returning 200 OK without executing any logic"
                ],
                "correct_answer": "By enforcing rate limiting and IP blocking at the perimeter before traffic hits internal backends",
                "explanation": "Perimeter rate limiting drops abusive traffic before it can consume internal database connections and CPU."
            },
            {
                "question": "What header does an upstream reverse proxy commonly attach to inform internal services of the original client IP?",
                "options": [
                    "X-Forwarded-For or X-Real-IP",
                    "Content-Disposition",
                    "Accept-Encoding",
                    "Strict-Transport-Security"
                ],
                "correct_answer": "X-Forwarded-For or X-Real-IP",
                "explanation": "`X-Forwarded-For` preserves the originating client IP address through reverse proxy hops."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 55: Microservices Architecture & Inter-Service API Communication
    # ---------------------------------------------------------
    DayBlueprint(
        order=55,
        title="Microservices Architecture & Inter-Service API Communication",
        concept="Microservices break applications into independently deployable domain services communicating synchronously (REST, gRPC) or asynchronously (Kafka, RabbitMQ) using patterns like BFF and Service Mesh.",
        analogy="A monolithic application is like a lone Swiss Army knife. A microservices architecture is like a specialized surgical team: one surgeon, one anesthesiologist, one scrub nurse, and one monitor technician, all communicating through clear protocols to perform surgery.",
        theory_sections=[
            {
                "heading": "Synchronous vs Asynchronous Inter-Service Communication",
                "content": (
                    "- **Synchronous (REST / gRPC)**: Service A calls Service B and blocks/awaits the response. Best for operations that require immediate validation (e.g. checking if a voucher code is valid during checkout). Risk: Cascading latency if Service B hangs.\n"
                    "- **Asynchronous (Event-Driven via Kafka / RabbitMQ)**: Service A publishes an event (`OrderCreated`) and resumes immediately. Services B (Inventory), C (Email), and D (Analytics) consume the event independently. Decouples system availability."
                )
            },
            {
                "heading": "The Backend for Frontend (BFF) Pattern",
                "content": (
                    "Different client interfaces require different data shapes:\n"
                    "- Mobile apps need small, bandwidth-friendly payloads with aggregated fields.\n"
                    "- Desktop web dashboards need large, dense data tables.\n"
                    "- Smart TVs or watch apps need minimal summaries.\n\n"
                    "The **BFF Pattern** deploys dedicated lightweight API gateway layers tailored specifically to each frontend platform (`mobile-bff`, `web-bff`), aggregating calls to internal core services."
                )
            },
            {
                "heading": "Service Mesh (Istio, Envoy) & Circuit Breakers",
                "content": (
                    "As the number of microservices grows to hundreds, managing service discovery, mTLS (mutual TLS) encryption, and retries in application code becomes impossible.\n\n"
                    "A **Service Mesh** injects a sidecar proxy (like Envoy) alongside every service container. The sidecar transparently manages:\n"
                    "- Automatic mTLS encryption between all services.\n"
                    "- **Circuit Breakers**: If Service B fails 50% of calls, the sidecar automatically trips open, failing fast to prevent thread starvation in Service A."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Circuit Breaker Pattern in Python (pybreaker)",
                "language": "python",
                "code": (
                    "import pybreaker\n"
                    "import requests\n\n"
                    "# Trip circuit if 5 consecutive failures occur; wait 60s before retry\n"
                    "db_breaker = pybreaker.CircuitBreaker(\n"
                    "    fail_max=5,\n"
                    "    reset_timeout=60\n"
                    ")\n\n"
                    "@db_breaker\n"
                    "def call_inventory_service(item_id):\n"
                    "    response = requests.get(f'http://inventory-svc/items/{item_id}', timeout=2.0)\n"
                    "    response.raise_for_status()\n"
                    "    return response.json()\n\n"
                    "# When circuit is OPEN, calls immediately raise CircuitBreakerError without hitting network"
                ),
                "explanation": "Circuit breaker prevents catastrophic cascading latency by failing fast when upstream services degrade."
            },
            {
                "title": "Backend for Frontend (BFF) Aggregator Endpoint",
                "language": "python",
                "code": (
                    "from fastapi import FastAPI\n"
                    "import httpx\n\n"
                    "app = FastAPI(title='Mobile BFF')\n\n"
                    "@app.get('/mobile/dashboard/{user_id}')\n"
                    "async def get_mobile_dashboard(user_id: int):\n"
                    "    async with httpx.AsyncClient() as client:\n"
                    "        # Parallel calls to internal microservices\n"
                    "        user_task = client.get(f'http://user-svc/users/{user_id}')\n"
                    "        orders_task = client.get(f'http://order-svc/orders?user_id={user_id}&limit=3')\n"
                    "        u_res, o_res = await asyncio.gather(user_task, orders_task)\n\n"
                    "    return {\n"
                    "        'user_name': u_res.json()['name'],\n"
                    "        'recent_orders': o_res.json()['items']\n"
                    "    }"
                ),
                "explanation": "BFF aggregates multiple backend services into a single tailored payload for mobile clients."
            },
            {
                "title": "Event-Driven Asynchronous Communication (RabbitMQ / Pika)",
                "language": "python",
                "code": (
                    "import pika, json\n\n"
                    "def publish_order_event(order_data):\n"
                    "    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq.internal'))\n"
                    "    channel = connection.channel()\n"
                    "    channel.exchange_declare(exchange='orders', exchange_type='fanout')\n\n"
                    "    message = json.dumps(order_data)\n"
                    "    channel.basic_publish(exchange='orders', routing_key='', body=message)\n"
                    "    print('Published OrderCreated event asynchronously')\n"
                    "    connection.close()"
                ),
                "explanation": "Publishes domain events to an exchange; consumer microservices react without blocking checkout."
            },
            {
                "title": "Service Mesh Envoy Sidecar Configuration Snippet",
                "language": "yaml",
                "code": (
                    "static_resources:\n"
                    "  listeners:\n"
                    "    - name: outbound_listener\n"
                    "      address:\n"
                    "        socket_address: { address: 0.0.0.0, port_value: 15001 }\n"
                    "      filter_chains:\n"
                    "        - filters:\n"
                    "            - name: envoy.filters.network.http_connection_manager\n"
                    "              typed_config:\n"
                    "                \"@type\": type.googleapis.com/envoy.extensions.filters.network.http_connection_manager.v3.HttpConnectionManager\n"
                    "                stat_prefix: egress_http"
                ),
                "explanation": "Envoy proxy intercepts network traffic transparently to inject mTLS and telemetry."
            }
        ],
        coding_challenge={
            "title": "Simulate Basic Circuit Breaker State Machine",
            "instructions": "Write a class `SimpleCircuitBreaker` with methods `record_success()` and `record_failure()`. If consecutive failures reach `fail_threshold`, set state to `'OPEN'`. If in `'OPEN'` state and `is_available()` is called, return False. When `record_success()` is called, reset failures to 0 and set state to `'CLOSED'`.",
            "starter_code": (
                "class SimpleCircuitBreaker:\n"
                "    def __init__(self, fail_threshold: int = 3):\n"
                "        self.state = 'CLOSED'\n"
                "        self.consecutive_fails = 0\n"
                "        self.threshold = fail_threshold\n\n"
                "    def record_failure(self):\n"
                "        pass\n\n"
                "    def record_success(self):\n"
                "        pass\n\n"
                "    def is_available(self) -> bool:\n"
                "        pass\n"
            ),
            "solution_code": (
                "class SimpleCircuitBreaker:\n"
                "    def __init__(self, fail_threshold: int = 3):\n"
                "        self.state = 'CLOSED'\n"
                "        self.consecutive_fails = 0\n"
                "        self.threshold = fail_threshold\n\n"
                "    def record_failure(self):\n"
                "        self.consecutive_fails += 1\n"
                "        if self.consecutive_fails >= self.threshold:\n"
                "            self.state = 'OPEN'\n\n"
                "    def record_success(self):\n"
                "        self.consecutive_fails = 0\n"
                "        self.state = 'CLOSED'\n\n"
                "    def is_available(self) -> bool:\n"
                "        return self.state != 'OPEN'\n\n"
                "cb = SimpleCircuitBreaker(fail_threshold=2)\n"
                "cb.record_failure()\n"
                "print(cb.is_available())\n"
                "cb.record_failure()\n"
                "print(cb.is_available())"
            ),
            "expected_output": "True\nFalse"
        },
        quizzes=[
            {
                "question": "What is the primary function of the Circuit Breaker pattern in microservice architectures?",
                "options": [
                    "To stop calling a failing service immediately and fail fast, preventing cascading system-wide outages",
                    "To reboot the physical server rack",
                    "To delete database tables when disk space is full",
                    "To encrypt credit card numbers in transit"
                ],
                "correct_answer": "To stop calling a failing service immediately and fail fast, preventing cascading system-wide outages",
                "explanation": "Circuit breakers trip open when downstream calls fail repeatedly, preserving threads and resources."
            },
            {
                "question": "What does 'BFF' stand for in frontend/backend architectural patterns?",
                "options": [
                    "Backend for Frontend",
                    "Binary File Formatter",
                    "Basic Functional Filter",
                    "Batch Fetching Framework"
                ],
                "correct_answer": "Backend for Frontend",
                "explanation": "BFF creates dedicated backend services tailored to the specific needs of individual frontend platforms (mobile, web)."
            },
            {
                "question": "Why is asynchronous event-driven communication (e.g. Kafka/RabbitMQ) often preferred over synchronous HTTP between microservices?",
                "options": [
                    "It decouples services so the publisher doesn't freeze or fail if consumer services are temporarily slow or offline",
                    "It makes networks run faster than the speed of light",
                    "It eliminates the need for software testing",
                    "It uses plain text passwords for simplicity"
                ],
                "correct_answer": "It decouples services so the publisher doesn't freeze or fail if consumer services are temporarily slow or offline",
                "explanation": "Event streaming allows services to publish events and move on without waiting on downstream consumers."
            },
            {
                "question": "In a Service Mesh architecture (e.g. Istio with Envoy), how is network traffic intercepted?",
                "options": [
                    "Via sidecar proxy containers deployed alongside each microservice container",
                    "By manually editing every Python script line-by-line",
                    "By replacing all Linux kernels with Windows 95",
                    "Through USB flash drives"
                ],
                "correct_answer": "Via sidecar proxy containers deployed alongside each microservice container",
                "explanation": "A sidecar proxy intercepts in-and-out traffic to handle routing, mTLS, metrics, and circuit breaking."
            },
            {
                "question": "What security mechanism does a Service Mesh commonly automate between internal microservices?",
                "options": [
                    "Mutual TLS (mTLS) zero-trust encryption and authentication",
                    "CAPTCHA image challenges",
                    "SMS two-factor text messages between servers",
                    "Disabling all firewall rules"
                ],
                "correct_answer": "Mutual TLS (mTLS) zero-trust encryption and authentication",
                "explanation": "Service meshes automatically issue, rotate, and verify mTLS certificates for secure service-to-service communication."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 56: API Caching Strategies: HTTP Caching, Redis & CDN Edge
    # ---------------------------------------------------------
    DayBlueprint(
        order=56,
        title="API Caching Strategies: HTTP Caching, Redis & CDN Edge",
        concept="API Caching stores precomputed responses across multiple layers (HTTP client cache, Edge CDN, and backend Redis memory) to reduce database load and deliver sub-millisecond responses.",
        analogy="Caching is like keeping a pitcher of cold water in your refrigerator door. Instead of walking out to the backyard well and pumping the handle every time you want a sip of water, you pour a glass instantly from the fridge.",
        theory_sections=[
            {
                "heading": "The 3 Layers of Modern API Caching",
                "content": (
                    "1. **Client / Browser Cache**: Governed by HTTP response headers (`Cache-Control: max-age=3600`). Prevents network requests entirely for fresh data.\n"
                    "2. **CDN / Edge Cache (Cloudflare, Fastly)**: Caches responses at globally distributed data centers close to the user. Edge servers fulfill requests in 10ms without hitting your origin server.\n"
                    "3. **Backend In-Memory Cache (Redis, Memcached)**: Caches raw database query results, computed session states, or rendered JSON fragments inside RAM (0.5ms latency)."
                )
            },
            {
                "heading": "Cache Invalidation & Freshness: ETag & 304 Not Modified",
                "content": (
                    "There are two hard things in Computer Science: cache invalidation and naming things.\n\n"
                    "- **Cache-Control Directives**:\n"
                    "  - `public`: Any cache (CDN, proxy, browser) may store the response.\n"
                    "  - `private`: Only the end-user client browser may cache it (never shared CDNs).\n"
                    "  - `no-cache`: Must revalidate with origin using `ETag` before serving.\n"
                    "  - `no-store`: Never write to disk or RAM anywhere (sensitive banking data).\n"
                    "- **Conditional Requests**: Client sends `If-None-Match: \"hash_123\"`. If data hasn't changed, server returns `304 Not Modified` with zero body bytes!"
                )
            },
            {
                "heading": "Cache Patterns: Cache-Aside vs Write-Through",
                "content": (
                    "- **Cache-Aside (Lazy Loading)**: Application checks Redis first. If Cache Hit, return data. If Cache Miss, query SQL database, write result into Redis with a TTL (Time-To-Live), and return to user.\n"
                    "- **Write-Through**: When writing data, update the database AND update the cache entry simultaneously inside the same operation."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Cache-Aside Pattern with Redis in Python",
                "language": "python",
                "code": (
                    "import redis, json\n\n"
                    "r = redis.Redis(host='localhost', port=6379, db=0)\n\n"
                    "def get_product(product_id: int) -> dict:\n"
                    "    cache_key = f'product:{product_id}'\n"
                    "    # 1. Check Redis Cache\n"
                    "    cached = r.get(cache_key)\n"
                    "    if cached:\n"
                    "        print('CACHE HIT')\n"
                    "        return json.loads(cached)\n\n"
                    "    # 2. CACHE MISS: Query Database\n"
                    "    print('CACHE MISS - Querying DB')\n"
                    "    product = db.query_product_by_id(product_id)\n\n"
                    "    # 3. Store in Redis with 600-second TTL\n"
                    "    r.setex(cache_key, 600, json.dumps(product))\n"
                    "    return product"
                ),
                "explanation": "Standard Cache-Aside pattern storing JSON string with automatic 10-minute expiration."
            },
            {
                "title": "ETag Generation and 304 Not Modified in FastAPI",
                "language": "python",
                "code": (
                    "import hashlib\n"
                    "from fastapi import FastAPI, Request, Response, status\n\n"
                    "app = FastAPI()\n\n"
                    "@app.get('/api/catalog')\n"
                    "def get_catalog(request: Request, response: Response):\n"
                    "    data = {'catalog_version': 4, 'items': ['Pen', 'Notebook']}\n"
                    "    body_str = json.dumps(data, sort_keys=True)\n"
                    "    etag = f'\"{hashlib.md5(body_str.encode()).hexdigest()}\"'\n\n"
                    "    if request.headers.get('if-none-match') == etag:\n"
                    "        return Response(status_code=status.HTTP_304_NOT_MODIFIED)\n\n"
                    "    response.headers['ETag'] = etag\n"
                    "    response.headers['Cache-Control'] = 'public, max-age=3600'\n"
                    "    return data"
                ),
                "explanation": "Generates MD5 ETag and short-circuits with 304 Not Modified if client already possesses fresh data."
            },
            {
                "title": "Cloudflare CDN Edge Cache Rules",
                "language": "nginx",
                "code": (
                    "# Origin HTTP Response Headers instructing Cloudflare Edge\n"
                    "HTTP/1.1 200 OK\n"
                    "Content-Type: application/json\n"
                    "Cache-Control: public, max-age=60, s-maxage=86400\n"
                    "# max-age=60: Browser caches for 60 seconds\n"
                    "# s-maxage=86400: Shared CDN Edge caches for 24 hours"
                ),
                "explanation": "Uses `s-maxage` to configure CDN edge caching duration independently from end-user browser caches."
            },
            {
                "title": "Cache Eviction on Data Modification",
                "language": "python",
                "code": (
                    "def update_product_price(product_id: int, new_price: float):\n"
                    "    # 1. Update primary database\n"
                    "    db.execute('UPDATE products SET price = ? WHERE id = ?', (new_price, product_id))\n\n"
                    "    # 2. Evict / Invalidate stale cache in Redis\n"
                    "    cache_key = f'product:{product_id}'\n"
                    "    r.delete(cache_key)\n"
                    "    print(f'Evicted {cache_key} from Redis')"
                ),
                "explanation": "Deletes the stale cache key upon update so the subsequent read automatically repopulates fresh state."
            }
        ],
        coding_challenge={
            "title": "Simulate In-Memory Cache with TTL",
            "instructions": "Write a class `SimpleTTLCache` with methods `set(key, value, ttl_seconds)` and `get(key, current_time)`. If the key exists and `current_time < expiry_time`, return the value. If expired or non-existent, return None.",
            "starter_code": (
                "class SimpleTTLCache:\n"
                "    def __init__(self):\n"
                "        self.store = {}\n\n"
                "    def set(self, key: str, value, ttl: float, now: float):\n"
                "        pass\n\n"
                "    def get(self, key: str, now: float):\n"
                "        pass\n"
            ),
            "solution_code": (
                "class SimpleTTLCache:\n"
                "    def __init__(self):\n"
                "        self.store = {}\n\n"
                "    def set(self, key: str, value, ttl: float, now: float):\n"
                "        self.store[key] = {'val': value, 'expiry': now + ttl}\n\n"
                "    def get(self, key: str, now: float):\n"
                "        item = self.store.get(key)\n"
                "        if not item:\n"
                "            return None\n"
                "        if now >= item['expiry']:\n"
                "            del self.store[key]\n"
                "            return None\n"
                "        return item['val']\n\n"
                "cache = SimpleTTLCache()\n"
                "cache.set('user:1', {'name': 'Sara'}, ttl=10, now=100.0)\n"
                "print(cache.get('user:1', now=105.0))\n"
                "print(cache.get('user:1', now=115.0))"
            ),
            "expected_output": "{'name': 'Sara'}\nNone"
        },
        quizzes=[
            {
                "question": "What is the primary difference between `Cache-Control: no-cache` and `Cache-Control: no-store`?",
                "options": [
                    "`no-cache` allows caching but forces revalidation before use; `no-store` forbids saving the response anywhere",
                    "`no-store` is for mobile only",
                    "`no-cache` deletes cookies",
                    "`no-store` stores data in RAM forever"
                ],
                "correct_answer": "`no-cache` allows caching but forces revalidation before use; `no-store` forbids saving the response anywhere",
                "explanation": "`no-store` ensures sensitive data never touches client disk or intermediate caches; `no-cache` allows caching with ETag revalidation."
            },
            {
                "question": "What HTTP status code is returned when a client sends `If-None-Match: \"etag\"` and the server detects no data changes?",
                "options": [
                    "304 Not Modified",
                    "200 OK",
                    "204 No Content",
                    "412 Precondition Failed"
                ],
                "correct_answer": "304 Not Modified",
                "explanation": "304 Not Modified instructs the client to render its local cached copy, transmitting zero body bytes across the network."
            },
            {
                "question": "In the Cache-Aside pattern, what does the application do on a Cache Miss?",
                "options": [
                    "It queries the database, writes the retrieved data into the cache with a TTL, and returns the data",
                    "It throws a 500 Internal Server Error",
                    "It shuts down the web server",
                    "It returns empty brackets `[]`"
                ],
                "correct_answer": "It queries the database, writes the retrieved data into the cache with a TTL, and returns the data",
                "explanation": "On a cache miss, the backend fetches from primary storage and lazy-loads the result into cache for subsequent callers."
            },
            {
                "question": "What does the `s-maxage` directive in a `Cache-Control` header specify?",
                "options": [
                    "The maximum caching time permitted on public shared caches like CDN edge nodes",
                    "The server CPU clock speed",
                    "The maximum size of uploaded files",
                    "The session timeout of user passwords"
                ],
                "correct_answer": "The maximum caching time permitted on public shared caches like CDN edge nodes",
                "explanation": "`s-maxage` overrides `max-age` specifically for shared proxy caches like Cloudflare and Akamai."
            },
            {
                "question": "Why is setting a TTL (Time-To-Live) crucial for keys stored in a Redis API cache?",
                "options": [
                    "To prevent stale data from lingering forever and stop RAM exhaustion by automatically expiring old keys",
                    "Because Redis automatically crashes after 1 hour without a TTL",
                    "To encrypt stored data using AES-GCM",
                    "To convert strings to integers"
                ],
                "correct_answer": "To prevent stale data from lingering forever and stop RAM exhaustion by automatically expiring old keys",
                "explanation": "TTLs bound memory consumption and provide an eventual-consistency backstop against stale cached state."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 57: API Observability: Distributed Tracing, Logs & Metrics
    # ---------------------------------------------------------
    DayBlueprint(
        order=57,
        title="API Observability: Distributed Tracing, Logs & Metrics",
        concept="API Observability uses the 3 pillars (Metrics, Structured Logs, and Distributed Tracing via OpenTelemetry) to diagnose production issues, track request journeys across microservices, and detect performance regressions.",
        analogy="If your API system is an ICU hospital patient, Metrics are the vital signs monitor (heart rate, blood pressure). Structured Logs are the doctor's chart notes. And Distributed Tracing is a radioactive dye injected into the bloodstream, showing the exact capillary pathway the dye travelled.",
        theory_sections=[
            {
                "heading": "The 3 Pillars of API Observability",
                "content": (
                    "1. **Metrics (Prometheus / Datadog)**: Numeric aggregations tracked over time (e.g. `http_requests_total`, `cpu_usage_percentage`, p99 latency). High-level alerts.\n"
                    "2. **Structured Logs (JSON format, Loki / ELK)**: Timestamped records detailing specific events with contextual key-value pairs (`user_id`, `tenant_id`, `error_stack`). Never use unstructured `print()`.\n"
                    "3. **Distributed Tracing (OpenTelemetry, Jaeger)**: Tracks a single user request as it traverses across 15 different microservices, databases, and message queues."
                )
            },
            {
                "heading": "Distributed Tracing Concepts: Trace ID, Span ID & W3C Trace Context",
                "content": (
                    "- **Trace**: The entire lifecycle journey of a request from client to edge gateway to downstream databases.\n"
                    "- **Span**: A single discrete unit of work within the trace (e.g. executing an SQL query, validating a JWT, or calling Redis). Spans have start times, durations, tags, and parent-child hierarchies.\n"
                    "- **W3C TraceContext (`traceparent` header)**: The standardized HTTP header propagated between services:\n"
                    "  `traceparent: 00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01`\n"
                    "  Encodes the version, 128-bit `trace_id`, 64-bit `parent_span_id`, and sampling flags."
                )
            },
            {
                "heading": "The RED Method for API Monitoring",
                "content": (
                    "Recommended by Google and Grafana for monitoring request-driven APIs:\n"
                    "- **Rate**: The number of requests your API is serving per second.\n"
                    "- **Errors**: The number of failed requests (HTTP 5xx status codes) per second.\n"
                    "- **Duration**: The amount of time those requests take (latency distribution)."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Structured JSON Logging in Python",
                "language": "python",
                "code": (
                    "import logging, json, time\n\n"
                    "class JSONFormatter(logging.Formatter):\n"
                    "    def format(self, record):\n"
                    "        log_obj = {\n"
                    "            'timestamp': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),\n"
                    "            'level': record.levelname,\n"
                    "            'message': record.getMessage(),\n"
                    "            'module': record.module,\n"
                    "            'trace_id': getattr(record, 'trace_id', None)\n"
                    "        }\n"
                    "        return json.dumps(log_obj)\n\n"
                    "handler = logging.StreamHandler()\n"
                    "handler.setFormatter(JSONFormatter())\n"
                    "logger = logging.getLogger('api')\n"
                    "logger.addHandler(handler)\n"
                    "logger.setLevel(logging.INFO)"
                ),
                "explanation": "Outputs structured JSON logs ingestible by Datadog, Grafana Loki, or Elasticsearch."
            },
            {
                "title": "OpenTelemetry Instrumentation in FastAPI",
                "language": "python",
                "code": (
                    "from fastapi import FastAPI\n"
                    "from opentelemetry import trace\n"
                    "from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor\n"
                    "from opentelemetry.sdk.trace import TracerProvider\n"
                    "from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter\n\n"
                    "# Setup OpenTelemetry Tracer\n"
                    "provider = TracerProvider()\n"
                    "provider.add_span_processor(BatchSpanProcessor(ConsoleSpanExporter()))\n"
                    "trace.set_tracer_provider(provider)\n\n"
                    "app = FastAPI()\n"
                    "# Automatically injects spans and propagates W3C traceparent headers\n"
                    "FastAPIInstrumentor.instrument_app(app)"
                ),
                "explanation": "Automates tracing across incoming HTTP requests and outbound downstream client calls."
            },
            {
                "title": "Prometheus Metric Instrumentation",
                "language": "python",
                "code": (
                    "from prometheus_client import Counter, Histogram, generate_latest\n"
                    "from fastapi import FastAPI, Response\n\n"
                    "app = FastAPI()\n\n"
                    "REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP Requests', ['method', 'endpoint', 'status'])\n"
                    "REQUEST_LATENCY = Histogram('http_request_duration_seconds', 'Request Latency', ['endpoint'])\n\n"
                    "@app.get('/metrics')\n"
                    "def metrics():\n"
                    "    return Response(content=generate_latest(), media_type='text/plain')"
                ),
                "explanation": "Exposes standard Prometheus scrape endpoint reporting RED metrics."
            },
            {
                "title": "W3C `traceparent` Header Propagation",
                "language": "python",
                "code": (
                    "import httpx\n\n"
                    "async def call_downstream_service(trace_id: str, span_id: str):\n"
                    "    # Formats W3C traceparent: 00-{trace_id}-{span_id}-01\n"
                    "    traceparent_header = f'00-{trace_id}-{span_id}-01'\n"
                    "    async with httpx.AsyncClient() as client:\n"
                    "        res = await client.get(\n"
                    "            'http://payment-svc/charges',\n"
                    "            headers={'traceparent': traceparent_header}\n"
                    "        )\n"
                    "    return res.json()"
                ),
                "explanation": "Propagates context so downstream services attach their child spans to the identical parent trace."
            }
        ],
        coding_challenge={
            "title": "Parse W3C Traceparent Header",
            "instructions": "Write a function `parse_traceparent(header_val)` that parses a W3C traceparent string `00-<trace_id>-<parent_id>-<flags>` and returns a dictionary `{'version': ..., 'trace_id': ..., 'parent_id': ..., 'sampled': bool}`. If invalid, return None.",
            "starter_code": (
                "def parse_traceparent(header: str) -> dict:\n"
                "    # Parse 4 dash-separated components of W3C traceparent\n"
                "    pass\n"
            ),
            "solution_code": (
                "def parse_traceparent(header: str) -> dict:\n"
                "    if not header or not isinstance(header, str):\n"
                "        return None\n"
                "    parts = header.strip().split('-')\n"
                "    if len(parts) != 4:\n"
                "        return None\n"
                "    version, trace_id, parent_id, flags = parts\n"
                "    if len(trace_id) != 32 or len(parent_id) != 16:\n"
                "        return None\n"
                "    return {\n"
                "        'version': version,\n"
                "        'trace_id': trace_id,\n"
                "        'parent_id': parent_id,\n"
                "        'sampled': flags == '01'\n"
                "    }\n\n"
                "sample_header = '00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01'\n"
                "print(parse_traceparent(sample_header))"
            ),
            "expected_output": "{'version': '00', 'trace_id': '4bf92f3577b34da6a3ce929d0e0e4736', 'parent_id': '00f067aa0ba902b7', 'sampled': True}"
        },
        quizzes=[
            {
                "question": "What are the three pillars of modern application observability?",
                "options": [
                    "Metrics, Logs, and Distributed Tracing",
                    "HTML, CSS, and JavaScript",
                    "CPU, RAM, and Hard Drive",
                    "GET, POST, and DELETE"
                ],
                "correct_answer": "Metrics, Logs, and Distributed Tracing",
                "explanation": "Metrics aggregate quantities over time, Logs record contextual events, and Traces follow individual request lifecycles."
            },
            {
                "question": "What does a 'Span' represent in distributed tracing systems like OpenTelemetry or Jaeger?",
                "options": [
                    "A single contiguous block of work with a start time and duration (e.g. an SQL query or HTTP call)",
                    "A database table index",
                    "An Ethernet cable between servers",
                    "A user's browser cookie"
                ],
                "correct_answer": "A single contiguous block of work with a start time and duration (e.g. an SQL query or HTTP call)",
                "explanation": "A span represents an individual operation; spans nest hierarchically to form a complete Trace."
            },
            {
                "question": "What does the standardized `traceparent` HTTP header enable?",
                "options": [
                    "Context propagation, allowing different microservices to link child spans to the identical overall user trace",
                    "Automated password hashing",
                    "Client-side image compression",
                    "Bypassing CORS protections"
                ],
                "correct_answer": "Context propagation, allowing different microservices to link child spans to the identical overall user trace",
                "explanation": "W3C TraceContext `traceparent` passes the Trace ID across service boundaries so tracing backends can correlate the distributed tree."
            },
            {
                "question": "What metrics are measured under the 'RED' method of API monitoring?",
                "options": [
                    "Rate (throughput), Errors (failures), and Duration (latency distribution)",
                    "RAM, Energy, and Disk",
                    "Read, Execute, and Delete",
                    "Redirection, Encryption, and Decryption"
                ],
                "correct_answer": "Rate (throughput), Errors (failures), and Duration (latency distribution)",
                "explanation": "The RED method focuses on consumer-affecting metrics: Rate of requests, Error count, and Duration (latency)."
            },
            {
                "question": "Why are structured JSON logs preferred over plain text strings in production API environments?",
                "options": [
                    "Structured logs are easily parsed, indexed, and filtered by aggregation engines like Datadog, Elasticsearch, or Loki",
                    "JSON logs consume zero disk space",
                    "Plain text logs cannot be printed to terminal screens",
                    "Structured logs run faster in Python"
                ],
                "correct_answer": "Structured logs are easily parsed, indexed, and filtered by aggregation engines like Datadog, Elasticsearch, or Loki",
                "explanation": "JSON log properties (e.g. `\"user_id\": 42`, `\"status\": 500`) can be queried instantaneously across millions of records."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 58: CI/CD Pipelines for APIs & Contract Testing
    # ---------------------------------------------------------
    DayBlueprint(
        order=58,
        title="CI/CD Pipelines for APIs & Contract Testing",
        concept="API CI/CD automates linting, OpenAPI specification validation (Spectral), contract testing (Pact), regression test suites, and zero-downtime canary deployments.",
        analogy="A CI/CD pipeline is like an automated vehicle assembly plant quality checkpoint. Before a car rolls off the factory floor, robotic sensors check the brake lines, laser-scan the door alignment, and test the airbags. If a single wire is loose, the conveyer belt halts automatically.",
        theory_sections=[
            {
                "heading": "Anatomy of an API CI/CD Pipeline",
                "content": (
                    "When an engineer pushes code or opens a Pull Request, the automated pipeline runs:\n"
                    "1. **Linting & Formatting**: Flake8, ESLint, Black, Prettier.\n"
                    "2. **Contract & Spec Linting**: Spectral scans `openapi.yaml` to ensure conventions (e.g. camelCase vs snake_case, descriptions present, tags defined).\n"
                    "3. **Automated Test Matrix**: Unit tests, integration tests against containerized PostgreSQL/Redis, and mocking stubs.\n"
                    "4. **Breaking Change Detection**: Tools like `oasdiff` or `openapi-diff` compare the PR's OpenAPI spec against the production spec to detect removed fields or altered endpoints."
                )
            },
            {
                "heading": "Consumer-Driven Contract Testing with Pact",
                "content": (
                    "In microservices, frontend and backend teams often break each other silently. **Contract Testing** bridges this gap:\n"
                    "- The **Consumer** (Mobile app / Frontend) defines expectations in a contract file (a 'Pact'): *'When I call `GET /users/1`, I require a string field named `email`.'*\n"
                    "- The **Provider** (Backend) pipeline verifies the contract against its actual API controllers.\n"
                    "- If a backend developer renames `email` to `user_email`, the contract test fails in CI *before* the backend code can be merged!"
                )
            },
            {
                "heading": "Zero-Downtime Deployment Strategies: Blue-Green vs Canary",
                "content": (
                    "- **Blue-Green Deployment**: Two identical environments. 'Blue' is live serving 100% traffic. 'Green' receives the new version. Once health checks pass, the router flips 100% traffic to Green instantly.\n"
                    "- **Canary Deployment**: The new version is deployed to 2% of users. The API gateway monitors error rates and latency. If metrics remain healthy over 30 minutes, traffic ramps to 10%, 50%, and 100%."
                )
            }
        ],
        code_snippets=[
            {
                "title": "GitHub Actions API CI Workflow (`.github/workflows/api-ci.yml`)",
                "language": "yaml",
                "code": (
                    "name: API CI Pipeline\n"
                    "on: [push, pull_request]\n\n"
                    "jobs:\n"
                    "  test:\n"
                    "    runs-on: ubuntu-latest\n"
                    "    services:\n"
                    "      postgres:\n"
                    "        image: postgres:15\n"
                    "        env:\n"
                    "          POSTGRES_DB: test_db\n"
                    "          POSTGRES_PASSWORD: secret\n"
                    "        ports: ['5432:5432']\n"
                    "    steps:\n"
                    "      - uses: actions/checkout@v3\n"
                    "      - uses: actions/setup-python@v4\n"
                    "        with: { python-version: '3.11' }\n"
                    "      - name: Install dependencies\n"
                    "        run: pip install -r requirements.txt pytest\n"
                    "      - name: Run Test Suite\n"
                    "        run: pytest --cov=app tests/"
                ),
                "explanation": "GitHub Actions pipeline spinning up a real PostgreSQL container service to execute automated test suites."
            },
            {
                "title": "Spectral OpenAPI Linting Ruleset (`.spectral.yaml`)",
                "language": "yaml",
                "code": (
                    "extends: 'spectral:oas'\n"
                    "rules:\n"
                    "  operation-description:\n"
                    "    description: Every endpoint operation must have a description.\n"
                    "    given: '$.paths.*[get,post,put,delete]'\n"
                    "    then:\n"
                    "      field: description\n"
                    "      function: defined\n"
                    "  path-keys-no-trailing-slash:\n"
                    "    given: '$.paths[*]~'\n"
                    "    then:\n"
                    "      function: pattern\n"
                    "      functionOptions:\n"
                    "        notMatch: '/$'"
                ),
                "explanation": "Enforces API governance rules such as mandatory endpoint descriptions and forbidding trailing slashes."
            },
            {
                "title": "Detecting Breaking Changes via CLI",
                "language": "bash",
                "code": (
                    "# Compare production OpenAPI spec with newly proposed spec\n"
                    "npx oasdiff -base https://api.prod.com/openapi.json -revision ./openapi.json -breaking\n\n"
                    "# Fails with exit code 1 if a field was deleted or required parameter added:\n"
                    "# 1 breaking change found: response property 'user_email' was removed from 200 response"
                ),
                "explanation": "Prevents catastrophic breaking changes from being published to production clients."
            },
            {
                "title": "Consumer Contract Verification with Pact (Python)",
                "language": "python",
                "code": (
                    "from pact import Consumer, Provider\n\n"
                    "pact = Consumer('WebDashboard').has_pact_with(Provider('UserService'))\n"
                    "pact.start_service()\n\n"
                    "# Define expectations\n"
                    "(\n"
                    "    pact.given('User 42 exists')\n"
                    "    .upon_receiving('A request for user 42')\n"
                    "    .with_request('GET', '/users/42')\n"
                    "    .will_respond_with(200, body={'id': 42, 'status': 'ACTIVE'})\n"
                    ")\n\n"
                    "with pact:\n"
                    "    # Verify client consumes mock successfully and exports pact JSON file\n"
                    "    res = requests.get('http://localhost:1234/users/42')\n"
                    "    assert res.json()['status'] == 'ACTIVE'"
                ),
                "explanation": "Defines an explicit contract that the backend provider must satisfy in CI."
            }
        ],
        coding_challenge={
            "title": "Detect Breaking Field Removals in API Schema",
            "instructions": "Write a function `detect_breaking_changes(old_schema, new_schema)` that compares dictionary keys. If any key that was present in `old_schema` is missing in `new_schema`, return a list of the removed keys (breaking changes). Otherwise return an empty list.",
            "starter_code": (
                "def detect_breaking_changes(old_schema: dict, new_schema: dict) -> list:\n"
                "    # Return list of deleted property keys\n"
                "    pass\n"
            ),
            "solution_code": (
                "def detect_breaking_changes(old_schema: dict, new_schema: dict) -> list:\n"
                "    old_keys = set(old_schema.keys())\n"
                "    new_keys = set(new_schema.keys())\n"
                "    removed = sorted(list(old_keys - new_keys))\n"
                "    return removed\n\n"
                "v1_fields = {'id': 'int', 'username': 'str', 'email': 'str'}\n"
                "v2_fields = {'id': 'int', 'username': 'str'}  # email removed\n"
                "print(detect_breaking_changes(v1_fields, v2_fields))"
            ),
            "expected_output": "['email']"
        },
        quizzes=[
            {
                "question": "What is the primary benefit of Consumer-Driven Contract Testing (e.g. with Pact)?",
                "options": [
                    "It ensures backend changes do not break frontend expectations before pull requests are merged",
                    "It eliminates the need to write unit tests",
                    "It automatically generates database tables",
                    "It speeds up internet connection bandwidth"
                ],
                "correct_answer": "It ensures backend changes do not break frontend expectations before pull requests are merged",
                "explanation": "Contract testing validates the integration contract between consumer and provider in CI pipelines."
            },
            {
                "question": "What is Spectral used for in an API development lifecycle?",
                "options": [
                    "A JSON/YAML linter for enforcing style guides and quality rules on OpenAPI documents",
                    "A SQL database query optimizer",
                    "An encryption algorithm for passwords",
                    "A tool for rendering React Native UI"
                ],
                "correct_answer": "A JSON/YAML linter for enforcing style guides and quality rules on OpenAPI documents",
                "explanation": "Spectral lints OpenAPI specs to enforce corporate naming conventions, required fields, and best practices."
            },
            {
                "question": "In a Canary Deployment strategy, how is traffic routed to the newly deployed API version?",
                "options": [
                    "A tiny percentage (e.g. 2%) is initially routed to the canary; traffic ramps up gradually as metrics remain healthy",
                    "100% of all traffic is switched immediately at midnight",
                    "Traffic is routed only to users whose names start with 'C'",
                    "All traffic is rejected for 24 hours"
                ],
                "correct_answer": "A tiny percentage (e.g. 2%) is initially routed to the canary; traffic ramps up gradually as metrics remain healthy",
                "explanation": "Canary deployments limit blast radius by verifying health on a small subset of production traffic."
            },
            {
                "question": "Which of the following modifications constitutes a breaking API change?",
                "options": [
                    "Removing an existing field from a 200 OK JSON response payload",
                    "Adding an optional query parameter to a GET endpoint",
                    "Adding a brand new endpoint that didn't exist before",
                    "Improving database query performance by 50%"
                ],
                "correct_answer": "Removing an existing field from a 200 OK JSON response payload",
                "explanation": "Existing mobile apps relying on that removed field will crash with null pointer exceptions."
            },
            {
                "question": "What is the role of a tool like `oasdiff` in a pull request workflow?",
                "options": [
                    "It compares the OpenAPI spec of the PR against production and fails the build if breaking changes are detected",
                    "It compresses image files",
                    "It formats Python code with PEP8",
                    "It checks whether credit card balances are sufficient"
                ],
                "correct_answer": "It compares the OpenAPI spec of the PR against production and fails the build if breaking changes are detected",
                "explanation": "`oasdiff` identifies deleted paths, altered types, or added required parameters, blocking breaking PRs."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 59: Monetizing APIs: SaaS Models & Stripe Usage Billing
    # ---------------------------------------------------------
    DayBlueprint(
        order=59,
        title="Monetizing APIs: SaaS Models & Stripe Usage Billing",
        concept="API Monetization turns your application endpoints into revenue-generating products using pricing tiers, metered usage billing (Stripe Invoicing), and real-time quota deduction.",
        analogy="API monetization is like municipal utilities. A homeowner can either pay a flat monthly fee for trash collection (Subscription Tier) or pay an exact metered bill per gallon of water used (Usage-Based Metering).",
        theory_sections=[
            {
                "heading": "API Monetization Pricing Models",
                "content": (
                    "1. **Tiered Subscriptions**: Flat monthly fee for a fixed bucket (e.g. Free: 1,000 req/mo, Pro: 100,000 req/mo for $49, Enterprise: Unlimited).\n"
                    "2. **Pay-As-You-Go (Metered Usage)**: Customers pay strictly for what they consume (e.g. OpenAI charging $0.002 per 1,000 tokens, Twilio charging $0.0075 per SMS).\n"
                    "3. **Freemium with Overage**: Free tier up to 10,000 calls; each additional call costs $0.001.\n"
                    "4. **Feature Gating**: Certain advanced endpoints (e.g. `/v1/ai/generate-video` or `/v1/reports/pdf`) are restricted to paying enterprise tiers."
                )
            },
            {
                "heading": "Stripe Metered Billing Architecture",
                "content": (
                    "Stripe provides the **Usage Records API** (`/v1/subscription_items/{id}/usage_records`):\n"
                    "1. When a user sends an API request, an API Gateway plugin increments a Redis counter.\n"
                    "2. An asynchronous background worker batches consumption events and reports them to Stripe:\n"
                    "   `stripe.SubscriptionItem.create_usage_record(sub_item_id, quantity=100, action='increment')`\n"
                    "3. At the end of the billing cycle, Stripe automatically aggregates the usage records and charges the customer's credit card."
                )
            },
            {
                "heading": "Quota Management & Hard vs Soft Caps",
                "content": (
                    "- **Hard Cap**: Request is immediately rejected with HTTP `402 Payment Required` or `429 Too Many Requests` when the monthly limit is exceeded.\n"
                    "- **Soft Cap**: The API continues processing requests, sends a warning email to the developer, and bills overage fees on the next invoice."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Reporting Metered Usage to Stripe in Python",
                "language": "python",
                "code": (
                    "import stripe, time\n\n"
                    "stripe.api_key = 'sk_test_demo_12345'\n\n"
                    "def report_api_usage(subscription_item_id: str, calls_made: int):\n"
                    "    # Reports metered consumption to Stripe Invoicing Engine\n"
                    "    record = stripe.SubscriptionItem.create_usage_record(\n"
                    "        subscription_item_id,\n"
                    "        quantity=calls_made,\n"
                    "        timestamp=int(time.time()),\n"
                    "        action='increment'\n"
                    "    )\n"
                    "    return record.id"
                ),
                "explanation": "Transmits metered consumption quantity directly to Stripe's automated billing infrastructure."
            },
            {
                "title": "FastAPI Quota Enforcement Middleware",
                "language": "python",
                "code": (
                    "import redis\n"
                    "from fastapi import FastAPI, Header, HTTPException, status\n\n"
                    "app = FastAPI()\n"
                    "r = redis.Redis(host='localhost', port=6379, db=0)\n\n"
                    "@app.middleware('http')\n"
                    "async def check_api_quota(request, call_next):\n"
                    "    api_key = request.headers.get('X-API-Key')\n"
                    "    if not api_key:\n"
                    "        return await call_next(request)\n\n"
                    "    # Check monthly usage quota in Redis\n"
                    "    quota_key = f'usage:{api_key}:2026-04'\n"
                    "    current_usage = r.incr(quota_key)\n"
                    "    limit = 1000  # Free tier max calls\n\n"
                    "    if current_usage > limit:\n"
                    "        raise HTTPException(\n"
                    "            status_code=status.HTTP_402_PAYMENT_REQUIRED,\n"
                    "            detail='Monthly API quota exceeded. Please upgrade your subscription.'\n"
                    "        )\n\n"
                    "    response = await call_next(request)\n"
                    "    response.headers['X-Quota-Remaining'] = str(max(0, limit - current_usage))\n"
                    "    return response"
                ),
                "explanation": "Enforces usage caps, returning HTTP 402 when quota limits are surpassed."
            },
            {
                "title": "Tiered Pricing JSON Schema",
                "language": "json",
                "code": (
                    "{\n"
                    "  \"plans\": [\n"
                    "    {\n"
                    "      \"id\": \"plan_free\",\n"
                    "      \"name\": \"Hobbyist\",\n"
                    "      \"price_cents\": 0,\n"
                    "      \"monthly_calls\": 1000,\n"
                    "      \"rate_limit_per_min\": 10\n"
                    "    },\n"
                    "    {\n"
                    "      \"id\": \"plan_pro\",\n"
                    "      \"name\": \"Scale\",\n"
                    "      \"price_cents\": 4900,\n"
                    "      \"monthly_calls\": 100000,\n"
                    "      \"overage_per_call_cents\": 0.1\n"
                    "    }\n"
                    "  ]\n"
                    "}"
                ),
                "explanation": "Data structure modeling subscription tiers, monthly quotas, and overage billing."
            },
            {
                "title": "Batching Usage Events Before Sending to Stripe",
                "language": "python",
                "code": (
                    "def flush_usage_buffer_to_stripe(redis_client):\n"
                    "    # Rather than calling Stripe HTTP on EVERY user call,\n"
                    "    # pull batched sums from Redis hash every 5 minutes\n"
                    "    usage_items = redis_client.hgetall('buffer:api_usage')\n"
                    "    for sub_item_id, count in usage_items.items():\n"
                    "        report_api_usage(sub_item_id.decode(), int(count))\n"
                    "    redis_client.delete('buffer:api_usage')"
                ),
                "explanation": "Batches usage events in memory to prevent overwhelming third-party billing APIs."
            }
        ],
        coding_challenge={
            "title": "Calculate Metered API Invoice Cost",
            "instructions": "Write a function `calculate_api_bill(plan_base_cost, included_calls, total_calls, overage_rate_per_call)` that returns the total billing amount. If `total_calls <= included_calls`, return `plan_base_cost`. Otherwise, add `(total_calls - included_calls) * overage_rate_per_call` to the base cost.",
            "starter_code": (
                "def calculate_api_bill(base: float, included: int, total: int, overage_rate: float) -> float:\n"
                "    # Return computed monthly invoice total\n"
                "    pass\n"
            ),
            "solution_code": (
                "def calculate_api_bill(base: float, included: int, total: int, overage_rate: float) -> float:\n"
                "    if total <= included:\n"
                "        return round(float(base), 2)\n"
                "    overage_calls = total - included\n"
                "    total_bill = base + (overage_calls * overage_rate)\n"
                "    return round(float(total_bill), 2)\n\n"
                "print(calculate_api_bill(base=49.00, included=10000, total=12500, overage_rate=0.01))"
            ),
            "expected_output": "74.0"
        },
        quizzes=[
            {
                "question": "What is 'Usage-Based Metered Billing' in an API SaaS business?",
                "options": [
                    "Charging customers dynamically based on the exact quantity of API requests or compute units they consumed in a billing cycle",
                    "Charging a flat $10 fee regardless of usage",
                    "Giving away all data completely free without revenue",
                    "Charging users every second via cash delivery"
                ],
                "correct_answer": "Charging customers dynamically based on the exact quantity of API requests or compute units they consumed in a billing cycle",
                "explanation": "Metered billing charges per consumption unit (e.g. $0.001 per call or per 1,000 tokens)."
            },
            {
                "question": "Which HTTP status code is most appropriate when an API client's prepaid quota is exhausted and payment is required to continue?",
                "options": [
                    "402 Payment Required",
                    "200 OK",
                    "302 Found",
                    "503 Service Unavailable"
                ],
                "correct_answer": "402 Payment Required",
                "explanation": "RFC 9110 specifies HTTP 402 Payment Required as the status for digital cash and quota payment exhaustion."
            },
            {
                "question": "Why should high-throughput APIs batch usage records in Redis before transmitting them to Stripe?",
                "options": [
                    "Making an HTTP call to Stripe on every incoming API request adds massive latency and hits Stripe rate limits",
                    "Because Stripe does not allow HTTPS connections",
                    "Because Redis is owned by Stripe",
                    "To hide usage numbers from the finance team"
                ],
                "correct_answer": "Making an HTTP call to Stripe on every incoming API request adds massive latency and hits Stripe rate limits",
                "explanation": "Aggregating in Redis RAM and reporting in batches (e.g. every 5 minutes) protects latency and respects billing limits."
            },
            {
                "question": "What is the difference between a 'Hard Cap' and a 'Soft Cap' on an API subscription?",
                "options": [
                    "A hard cap blocks further requests when the limit is reached; a soft cap allows requests to proceed and bills for overage",
                    "A hard cap is for enterprise; a soft cap is for mobile",
                    "A soft cap turns off server electricity",
                    "There is no difference"
                ],
                "correct_answer": "A hard cap blocks further requests when the limit is reached; a soft cap allows requests to proceed and bills for overage",
                "explanation": "Soft caps prioritize continuous business uptime by charging overage rates rather than severing client requests."
            },
            {
                "question": "What HTTP response header is commonly returned to inform clients of their remaining monthly call allowance?",
                "options": [
                    "X-Quota-Remaining or X-RateLimit-Remaining",
                    "Content-Disposition",
                    "Server-Timing",
                    "X-Powered-By"
                ],
                "correct_answer": "X-Quota-Remaining or X-RateLimit-Remaining",
                "explanation": "`X-Quota-Remaining` transparently communicates consumed vs remaining balance so clients can monitor allowance."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 60: Capstone Project: Enterprise API Platform Architecture
    # ---------------------------------------------------------
    DayBlueprint(
        order=60,
        title="Capstone Project: Enterprise API Platform Architecture",
        concept="The Capstone Project synthesizes all 60 days into an end-to-end production architecture: OpenAPI 3.0 specification, JWT auth, Token-Bucket rate limiting, Redis caching with ETag, Prometheus metrics, and automated resilience.",
        analogy="The Capstone Project is like conducting a world-class symphony orchestra. Every instrument we learned—the brass of HTTP verbs, the strings of REST conventions, the percussion of Redis caching, and the conductor of OpenTelemetry—now plays together in flawless harmony.",
        theory_sections=[
            {
                "heading": "The Production Enterprise API Blueprint",
                "content": (
                    "Over 60 days, we mastered the entire lifecycle of APIs and Web Services. In this final milestone, we unify:\n"
                    "- **Design & Contract**: OpenAPI 3.0 spec with strict schema validation.\n"
                    "- **Security**: JWT authentication middleware, CORS whitelist, and header sanitization.\n"
                    "- **Performance**: Token-Bucket rate limiting, Redis Cache-Aside, and conditional 304 ETag responses.\n"
                    "- **Observability**: W3C `traceparent` propagation, Prometheus RED metrics, and structured JSON logs.\n"
                    "- **Resilience**: Idempotency keys, circuit breaking, and RFC 7807 standardized problem details."
                )
            },
            {
                "heading": "Production Checklist Before Launch",
                "content": (
                    "Before opening your API to public third-party developers:\n"
                    "1. Are all endpoints versioned under `/v1/`?\n"
                    "2. Are all database write operations idempotent or protected with `Idempotency-Key` headers?\n"
                    "3. Is SSL/TLS 1.3 enforced everywhere with HSTS headers?\n"
                    "4. Are all sensitive fields (passwords, salts, billing secrets) excluded from responses?\n"
                    "5. Does the API return standardized error envelopes with domain error codes and documentation URLs?"
                )
            },
            {
                "heading": "Your Journey as an API Architect",
                "content": (
                    "You have progressed from understanding raw HTTP/1.1 byte packets to designing global, multi-region, distributed microservices architectures. You are equipped to build, document, test, secure, scale, and monetize resilient web services for enterprise engineering teams."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Production API Application Shell (FastAPI)",
                "language": "python",
                "code": (
                    "from fastapi import FastAPI, Depends, Request, Response, HTTPException, status\n"
                    "from fastapi.middleware.cors import CORSMiddleware\n"
                    "import time, uuid, hashlib\n\n"
                    "app = FastAPI(\n"
                    "    title='Enterprise Commerce Platform API',\n"
                    "    version='1.0.0',\n"
                    "    openapi_url='/api/v1/openapi.json',\n"
                    "    docs_url='/docs'\n"
                    ")\n\n"
                    "# 1. Security: CORS Whitelist\n"
                    "app.add_middleware(\n"
                    "    CORSMiddleware,\n"
                    "    allow_origins=['https://dashboard.company.com'],\n"
                    "    allow_credentials=True,\n"
                    "    allow_methods=['GET', 'POST', 'PUT', 'DELETE'],\n"
                    "    allow_headers=['Authorization', 'Content-Type', 'Idempotency-Key']\n"
                    ")"
                ),
                "explanation": "Configures production FastAPI application with strict CORS security, docs, and versioning."
            },
            {
                "title": "Unified Observability & Structured Request Pipeline",
                "language": "python",
                "code": (
                    "@app.middleware('http')\n"
                    "async def enterprise_observability_middleware(request: Request, call_next):\n"
                    "    request_id = request.headers.get('X-Request-ID', str(uuid.uuid4()))\n"
                    "    start_time = time.time()\n\n"
                    "    response = await call_next(request)\n"
                    "    duration_ms = round((time.time() - start_time) * 1000, 2)\n\n"
                    "    response.headers['X-Request-ID'] = request_id\n"
                    "    response.headers['Server-Timing'] = f'total;dur={duration_ms}'\n\n"
                    "    # Structured Log Output\n"
                    "    print(f'{{\"event\":\"http_request\",\"id\":\"{request_id}\",\"path\":\"{request.url.path}\",\"status\":{response.status_code},\"duration_ms\":{duration_ms}}}')\n"
                    "    return response"
                ),
                "explanation": "Injects correlation request IDs, Server-Timing telemetry, and structured execution logs."
            },
            {
                "title": "Enterprise RFC 7807 Standardized Error Handler",
                "language": "python",
                "code": (
                    "from fastapi.responses import JSONResponse\n\n"
                    "@app.exception_handler(HTTPException)\n"
                    "async def rfc7807_exception_handler(request: Request, exc: HTTPException):\n"
                    "    return JSONResponse(\n"
                    "        status_code=exc.status_code,\n"
                    "        media_type='application/problem+json',\n"
                    "        content={\n"
                    "            'type': f'https://api.example.com/errors/http-{exc.status_code}',\n"
                    "            'title': exc.detail,\n"
                    "            'status': exc.status_code,\n"
                    "            'instance': request.url.path,\n"
                    "            'request_id': request.headers.get('X-Request-ID', 'unknown')\n"
                    "        }\n"
                    "    )"
                ),
                "explanation": "Guarantees all error responses follow RFC 7807 problem details specification uniformly."
            },
            {
                "title": "Complete Protected Resource with Caching & ETag",
                "language": "python",
                "code": (
                    "@app.get('/api/v1/orders/{order_id}', summary='Get Order Details')\n"
                    "def get_order(order_id: int, request: Request, response: Response):\n"
                    "    # Mock Database Fetch\n"
                    "    order = {'id': order_id, 'total_cents': 9900, 'status': 'PAID'}\n"
                    "    body_str = json.dumps(order, sort_keys=True)\n"
                    "    etag = f'\"{hashlib.sha256(body_str.encode()).hexdigest()[:16]}\"'\n\n"
                    "    if request.headers.get('if-none-match') == etag:\n"
                    "        return Response(status_code=304)\n\n"
                    "    response.headers['ETag'] = etag\n"
                    "    response.headers['Cache-Control'] = 'private, max-age=120'\n"
                    "    return order"
                ),
                "explanation": "Combines resource representation, SHA-256 ETag generation, and 304 conditional short-circuiting."
            }
        ],
        coding_challenge={
            "title": "Build the Master Enterprise Health & Telemetry Check",
            "instructions": "Write a function `build_health_report(db_healthy, redis_healthy, version, uptime_secs)` that returns a dictionary. If both DB and Redis are healthy, set `'status': 'HEALTHY'` and `'http_code': 200`. If either is down, set `'status': 'DEGRADED'` and `'http_code': 503`.",
            "starter_code": (
                "def build_health_report(db_ok: bool, redis_ok: bool, version: str, uptime: float) -> dict:\n"
                "    # Return enterprise health check status and HTTP code\n"
                "    pass\n"
            ),
            "solution_code": (
                "def build_health_report(db_ok: bool, redis_ok: bool, version: str, uptime: float) -> dict:\n"
                "    all_healthy = db_ok and redis_ok\n"
                "    status_str = 'HEALTHY' if all_healthy else 'DEGRADED'\n"
                "    code = 200 if all_healthy else 503\n"
                "    return {\n"
                "        'http_code': code,\n"
                "        'body': {\n"
                "            'status': status_str,\n"
                "            'version': version,\n"
                "            'uptime_seconds': uptime,\n"
                "            'dependencies': {\n"
                "                'database': 'UP' if db_ok else 'DOWN',\n"
                "                'redis': 'UP' if redis_ok else 'DOWN'\n"
                "            }\n"
                "        }\n"
                "    }\n\n"
                "print(build_health_report(True, True, '1.0.0', 3600.0))\n"
                "print(build_health_report(True, False, '1.0.0', 3650.0))"
            ),
            "expected_output": "{'http_code': 200, 'body': {'status': 'HEALTHY', 'version': '1.0.0', 'uptime_seconds': 3600.0, 'dependencies': {'database': 'UP', 'redis': 'UP'}}}\n{'http_code': 503, 'body': {'status': 'DEGRADED', 'version': '1.0.0', 'uptime_seconds': 3650.0, 'dependencies': {'database': 'UP', 'redis': 'DOWN'}}}"
        },
        quizzes=[
            {
                "question": "What is the recommended HTTP status code for a health-check endpoint (`/healthz`) when an essential dependency (like the primary database) is down?",
                "options": [
                    "503 Service Unavailable",
                    "200 OK with `{'status': 'failed'}`",
                    "404 Not Found",
                    "301 Moved Permanently"
                ],
                "correct_answer": "503 Service Unavailable",
                "explanation": "Returning 503 signals load balancers (AWS ALB, Kubernetes) to remove the unhealthy instance from the rotation."
            },
            {
                "question": "Why is the `X-Request-ID` correlation header critical in enterprise API architectures?",
                "options": [
                    "It tracks a request's journey across multiple microservices and log aggregation systems for debugging",
                    "It encrypts the payload using RSA 4096",
                    "It verifies the user's password",
                    "It speeds up network fiber optic cables"
                ],
                "correct_answer": "It tracks a request's journey across multiple microservices and log aggregation systems for debugging",
                "explanation": "A unique Request ID ties together disparate log records across gateways, services, and databases."
            },
            {
                "question": "Which RFC standard defines the structured `application/problem+json` format for API error responses?",
                "options": [
                    "RFC 7807",
                    "RFC 2616",
                    "RFC 7230",
                    "RFC 1918"
                ],
                "correct_answer": "RFC 7807",
                "explanation": "RFC 7807 standardizes Problem Details for HTTP APIs (type, title, status, detail, instance)."
            },
            {
                "question": "Which combination of caching headers provides both local caching and fast revalidation when content changes?",
                "options": [
                    "`Cache-Control: private, max-age=60` and `ETag: \"hash\"`",
                    "`Cache-Control: no-store` and `Pragma: no-cache`",
                    "`Server: Apache` and `Content-Type: text/plain`",
                    "`Access-Control-Allow-Origin: *` only"
                ],
                "correct_answer": "`Cache-Control: private, max-age=60` and `ETag: \"hash\"`",
                "explanation": "Clients can cache locally for 60 seconds and perform conditional revalidations using ETags for 304 responses."
            },
            {
                "question": "What is the final and most important hallmark of a world-class API platform?",
                "options": [
                    "Reliability, security, predictable contracts, comprehensive documentation, and graceful error handling",
                    "Using every trendy new framework simultaneously",
                    "Never returning HTTP status codes other than 200",
                    "Requiring users to execute raw SQL queries"
                ],
                "correct_answer": "Reliability, security, predictable contracts, comprehensive documentation, and graceful error handling",
                "explanation": "Production-grade APIs prioritize reliability, security, strong contracts, intuitive DX, and predictability."
            }
        ]
    )
]
