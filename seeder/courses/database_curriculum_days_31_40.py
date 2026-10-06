"""
Database Management 40-Day Curriculum - Module 7 (Part 2), Module 8, Module 9 & Module 10 (Days 31 to 40)
Module 7: Performance Tuning & Optimization (Days 31-32)
Module 8: NoSQL Databases (Days 33-36)
Module 9: Database Administration & Security (Days 37-38)
Module 10: Big Data, Scaling & Cloud (Days 39-40)
"""

from seeder.course_blueprint import DayBlueprint, QuizQuestionBlueprint, CodingChallengeBlueprint

DAYS_31_TO_40 = [
    # -------------------------------------------------------------
    # DAY 31
    # -------------------------------------------------------------
    DayBlueprint(
        order=31,
        title="Day 31: Query Optimization & Sargability (Table Scans to Index Seeks)",
        concept="Eliminating query antipatterns: Sargable predicates (Search Argument Able), preventing function wraps on indexed columns, and optimizing JOINs",
        analogy="Think of a phonebook sorted alphabetically by last name. If you search for 'People whose last name starts with B' (**Sargable Query**), you jump straight to letter B in 2 seconds. But if someone asks: 'Find all people whose last name, when reversed and converted to lowercase, ends in the letter z' (**Non-Sargable Query**), the alphabetical index is completely useless! You must read every single page and reverse every single name by hand.",
        theory_sections=[
            {
                "heading": "What is a 'Sargable' Query?",
                "body": "A query is **Sargable (Search Argument Able)** if the database engine can take direct advantage of an index to perform an index seek rather than scanning the entire table. The most common cause of non-sargable queries is wrapping an indexed column inside a function in the `WHERE` clause (e.g. `WHERE YEAR(created_at) = 2026`)."
            },
            {
                "heading": "Common Optimization Techniques",
                "body": "(1) Replace column functions with range bounds (`created_at >= '2026-01-01' AND created_at < '2027-01-01'`); (2) Avoid leading wildcards (`LIKE '%smith'`) which defeat B-Trees; (3) Eliminate `SELECT *` to allow Index-Only Scans; (4) Replace `IN (subquery)` with `EXISTS` or `JOIN` on high-cardinality tables."
            }
        ],
        code_snippets=[
            {
                "title": "Non-Sargable vs Sargable Date Query",
                "language": "sql",
                "code": "-- NON-SARGABLE: Wrapping column in DATE() destroys index seek!\n-- Forces a full Sequential Table Scan of 1,000,000 rows:\nSELECT id FROM orders WHERE DATE(created_at) = '2026-09-01';\n\n-- SARGABLE: Range comparison preserves B-Tree index seek (O(log N)):\nSELECT id FROM orders \nWHERE created_at >= '2026-09-01 00:00:00' \n  AND created_at <  '2026-09-02 00:00:00';",
                "explanation": "Replacing functional wrappers with range boundaries enables fast B-Tree index seeks."
            },
            {
                "title": "Fixing Leading Wildcards with Full-Text Search",
                "language": "sql",
                "code": "-- NON-SARGABLE: Leading wildcard cannot use standard B-Tree:\n-- SELECT * FROM products WHERE description LIKE '%wireless%';\n\n-- SARGABLE: Using PostgreSQL Full-Text Search (GIN Index):\nCREATE INDEX idx_products_fts ON products USING GIN(to_tsvector('english', description));\n\nSELECT id, title \nFROM products \nWHERE to_tsvector('english', description) @@ to_tsquery('english', 'wireless');",
                "explanation": "GIN full-text indexes optimize substring and vocabulary queries that defeat standard B-Trees."
            },
            {
                "title": "Avoiding Implicit Type Coercion Antipattern",
                "language": "sql",
                "code": "-- Phone is VARCHAR. Passing an integer forces type conversion on every row (Seq Scan):\n-- SELECT * FROM users WHERE phone_number = 923001234567;\n\n-- SARGABLE: Pass matching string type literal directly:\nSELECT id, full_name FROM users WHERE phone_number = '923001234567';",
                "explanation": "Passing mismatched data types forces per-row casting, nullifying index scans."
            },
            {
                "title": "Covering Index for Index-Only Scans (Zero Heap Fetch)",
                "language": "sql",
                "code": "-- Create covering index including payload columns\nCREATE INDEX idx_users_lookup ON users(email) INCLUDE (full_name, role);\n\n-- Index-Only Scan: Fetches email, full_name, and role directly from index RAM!\nSELECT email, full_name, role FROM users WHERE email = 'ali@hunar.app';",
                "explanation": "`INCLUDE` attaches non-key payload attributes directly to index leaf pages for index-only retrieval."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Sargable Query Checker",
            description="Write a Python function `is_sargable(where_clause: str) -> bool` that flags queries as non-sargable (`False`) if they contain leading wildcards (`LIKE '%...`) or common function calls on columns (`YEAR(`, `DATE(`, `LOWER(`).",
            starter_code="def is_sargable(where_clause: str) -> bool:\n    # Return False if common non-sargable patterns exist\n    pass",
            solution_code="def is_sargable(where_clause: str) -> bool:\n    bad_patterns = [\"like '%\", 'like \"%', 'year(', 'date(', 'lower(', 'upper(']\n    w = where_clause.lower()\n    return not any(p in w for p in bad_patterns)",
            expected_output="is_sargable(\"created_at >= '2026-01-01'\") == True, is_sargable(\"date(created_at) = '2026-01-01'\") == False"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What makes an SQL query predicate 'Sargable' (Search Argument Able)?",
                options=[
                    "It is written in a way that allows the database engine to utilize an index directly for rapid seeks",
                    "It has no WHERE clause",
                    "It runs only in web browsers",
                    "It contains no numbers"
                ],
                correct_answer="It is written in a way that allows the database engine to utilize an index directly for rapid seeks",
                explanation="Sargability means a predicate can leverage index trees without resorting to table scans."
            ),
            QuizQuestionBlueprint(
                question="Why does writing `WHERE YEAR(birth_date) = 2000` cause a slow Sequential Table Scan even if an index exists on `birth_date`?",
                options=[
                    "Because the YEAR() function must be evaluated on every single row before comparing, blinding the B-Tree index",
                    "Because YEAR() is not a valid SQL function",
                    "Because dates cannot be indexed",
                    "Because the year 2000 was a leap year"
                ],
                correct_answer="Because the YEAR() function must be evaluated on every single row before comparing, blinding the B-Tree index",
                explanation="Applying functions to indexed columns prevents the engine from seeking directly into the sorted index."
            ),
            QuizQuestionBlueprint(
                question="How should `WHERE DATE(order_time) = '2026-05-15'` be rewritten to make it sargable?",
                options=[
                    "`WHERE order_time >= '2026-05-15 00:00:00' AND order_time < '2026-05-16 00:00:00'`",
                    "`WHERE order_time LIKE '%2026-05-15%'`",
                    "`WHERE CAST(order_time AS TEXT) = '2026-05-15'`",
                    "`WHERE order_time != NULL`"
                ],
                correct_answer="`WHERE order_time >= '2026-05-15 00:00:00' AND order_time < '2026-05-16 00:00:00'`",
                explanation="Range bounds compare raw column values directly, preserving B-Tree index seeking."
            ),
            QuizQuestionBlueprint(
                question="Why can't a standard B-Tree index accelerate a query like `WHERE username LIKE '%smith'`?",
                options=[
                    "Because B-Trees are sorted by prefix; a leading wildcard (`%`) means matching characters could be anywhere, forcing a full scan",
                    "Because usernames cannot contain the letter s",
                    "Because LIKE queries only work on integers",
                    "Because strings cannot be indexed in SQL"
                ],
                correct_answer="Because B-Trees are sorted by prefix; a leading wildcard (`%`) means matching characters could be anywhere, forcing a full scan",
                explanation="Leading wildcards negate prefix sorting in B-Trees, requiring full sequential scans."
            ),
            QuizQuestionBlueprint(
                question="What is a 'Covering Index'?",
                options=[
                    "An index that contains all the columns requested by a query, allowing the database to satisfy the query entirely from RAM without visiting the table heap",
                    "An index that covers the server with a plastic case",
                    "An index that encrypts the table",
                    "A primary key with 50 columns"
                ],
                correct_answer="An index that contains all the columns requested by a query, allowing the database to satisfy the query entirely from RAM without visiting the table heap",
                explanation="Covering indexes satisfy queries entirely within index memory, eliminating table heap lookups."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 32
    # -------------------------------------------------------------
    DayBlueprint(
        order=32,
        title="Day 32: Database Caching Strategies (Redis & Memcached)",
        concept="Alleviating database load with in-memory caching: Cache-Aside, Write-Through, Write-Back, TTL expiration, and Cache Invalidation",
        analogy="Think of a database cache like keeping cold sodas in a small mini-fridge right beside your couch. If you get thirsty, you check the mini-fridge first (**Cache Hit** - 2 milliseconds). If the mini-fridge is empty (**Cache Miss**), you walk down two flights of stairs to the basement storage cellar to get a can (**Database Read** - 50 milliseconds) and place an extra can in your mini-fridge for next time!",
        theory_sections=[
            {
                "heading": "Why Primary Databases Need Caching Layers",
                "body": "Relational databases read from persistent SSDs and manage transactional locks, typically handling 2,000 to 10,000 queries per second per node. In-memory data stores like **Redis** or **Memcached** store data directly in RAM, effortlessly handling 200,000+ operations per second with sub-millisecond latencies, protecting the primary database from read spikes."
            },
            {
                "heading": "Caching Design Patterns & Invalidation",
                "body": "**Cache-Aside (Lazy Loading)**: The application checks cache first; on a miss, reads from DB and populates cache. **Write-Through**: Updates cache and DB simultaneously. Phil Karlton famously noted: *'There are only two hard things in Computer Science: cache invalidation and naming things.'* Always pair cache entries with a **Time-To-Live (TTL)** expiration to avoid serving stale data."
            }
        ],
        code_snippets=[
            {
                "title": "Implementing the Cache-Aside Pattern with Redis in Python",
                "language": "python",
                "code": "import redis\nimport json\n\nr = redis.Redis(host='localhost', port=6379, db=0)\n\ndef get_course_details(course_id: str, db_connection):\n    cache_key = f'course:{course_id}'\n    \n    # 1. Check Redis in-memory cache first (Sub-millisecond)\n    cached_data = r.get(cache_key)\n    if cached_data:\n        return json.loads(cached_data) # Cache Hit!\n        \n    # 2. Cache Miss: Query PostgreSQL\n    course = db_connection.fetch_one('SELECT * FROM courses WHERE id = %s', (course_id,))\n    \n    # 3. Store in cache with 1-hour Time-To-Live (TTL = 3600 seconds)\n    if course:\n        r.setex(cache_key, 3600, json.dumps(course))\n        \n    return course",
                "explanation": "Cache-Aside checks memory first, falling back to PostgreSQL on cache misses and setting a TTL."
            },
            {
                "title": "Cache Invalidation upon Database Update (Preventing Stale Data)",
                "language": "python",
                "code": "def update_course_title(course_id: str, new_title: str, db_connection):\n    # 1. Update PostgreSQL source of truth\n    db_connection.execute('UPDATE courses SET title = %s WHERE id = %s', (new_title, course_id))\n    \n    # 2. Invalidate / Purge old cached data immediately!\n    r.delete(f'course:{course_id}')",
                "explanation": "Purging cache keys on database updates prevents clients from reading stale data."
            },
            {
                "title": "Inspecting Redis Cache Keys and TTL via CLI",
                "language": "bash",
                "code": "# Connect to redis-cli and check key TTL\nredis-cli GET course:eb5c65b0\nredis-cli TTL course:eb5c65b0 # Returns remaining seconds (e.g. 3412)\nredis-cli INFO stats           # Displays keyspace_hits and keyspace_misses",
                "explanation": "Commands to inspect cached JSON payloads, check time-to-live expiration, and measure hit ratios."
            },
            {
                "title": "Rate Limiting Queries Using Redis INCR and EXPIRE",
                "language": "python",
                "code": "def is_rate_limited(user_ip: str, limit: int = 100) -> bool:\n    key = f'rate:{user_ip}'\n    current_requests = r.incr(key)\n    if current_requests == 1:\n        r.expire(key, 60) # 1 minute window\n    return current_requests > limit",
                "explanation": "Redis provides atomic counters for rate limiting, protecting the database from API spam."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Cache Hit Ratio Calculator",
            description="Write a Python function `calculate_cache_hit_ratio(hits: int, misses: int) -> float` that returns the percentage of hits as a float between 0.0 and 100.0, rounded to 2 decimal places. Return 0.0 if total requests are 0.",
            starter_code="def calculate_cache_hit_ratio(hits: int, misses: int) -> float:\n    # Return hit ratio percentage\n    pass",
            solution_code="def calculate_cache_hit_ratio(hits: int, misses: int) -> float:\n    total = hits + misses\n    if total <= 0:\n        return 0.0\n    return round((hits / total) * 100.0, 2)",
            expected_output="calculate_cache_hit_ratio(850, 150) == 85.0, calculate_cache_hit_ratio(0, 0) == 0.0"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the difference in storage medium between Redis and PostgreSQL?",
                options=[
                    "Redis stores primary data in volatile system RAM (ultra-fast); PostgreSQL persists data to physical SSD/disk storage with transaction logs",
                    "Redis is stored on paper; PostgreSQL runs in the cloud",
                    "PostgreSQL only stores pictures; Redis only stores numbers",
                    "There is no difference"
                ],
                correct_answer="Redis stores primary data in volatile system RAM (ultra-fast); PostgreSQL persists data to physical SSD/disk storage with transaction logs",
                explanation="RAM provides sub-millisecond data access, making in-memory stores ideal for caching."
            ),
            QuizQuestionBlueprint(
                question="How does the 'Cache-Aside' (Lazy Loading) pattern work?",
                options=[
                    "The application looks for data in cache first; if missing (miss), it queries the database and populates the cache for future requests",
                    "The database is deleted every morning",
                    "All queries bypass the database completely",
                    "Data is saved directly to USB drives"
                ],
                correct_answer="The application looks for data in cache first; if missing (miss), it queries the database and populates the cache for future requests",
                explanation="Cache-Aside lazily populates cached entries on demand following cache misses."
            ),
            QuizQuestionBlueprint(
                question="What is 'TTL' (Time-To-Live) in a caching layer?",
                options=[
                    "An expiration timer after which the cached key is automatically deleted from memory to prevent permanent stale data",
                    "The total battery life of the server",
                    "The ping latency between client and router",
                    "The time it takes to compile SQL"
                ],
                correct_answer="An expiration timer after which the cached key is automatically deleted from memory to prevent permanent stale data",
                explanation="TTL ensures cache keys expire automatically, bounding the window of stale data."
            ),
            QuizQuestionBlueprint(
                question="What is a 'Cache Stampede' (Thundering Herd)?",
                options=[
                    "When a popular cached key expires and thousands of concurrent requests all hit the primary database simultaneously to recalculate it",
                    "When a server overheats",
                    "When a table has too many foreign keys",
                    "When users type too fast"
                ],
                correct_answer="When a popular cached key expires and thousands of concurrent requests all hit the primary database simultaneously to recalculate it",
                explanation="A cache stampede overwhelms the database when a high-traffic cache key expires."
            ),
            QuizQuestionBlueprint(
                question="What should occur to the cache key `user:42` when User #42 updates their profile in the database?",
                options=[
                    "The cache key should be deleted (invalidated) or updated immediately to prevent serving outdated data",
                    "Nothing, cache should never be changed",
                    "The user's account should be deactivated",
                    "The database server should reboot"
                ],
                correct_answer="The cache key should be deleted (invalidated) or updated immediately to prevent serving outdated data",
                explanation="Invalidating the cache key on write ensures subsequent reads fetch fresh data from the database."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 33
    # -------------------------------------------------------------
    DayBlueprint(
        order=33,
        title="Day 33: The CAP Theorem & Document Databases (MongoDB)",
        concept="Understanding distributed trade-offs with the CAP Theorem and developing dynamic schema applications with MongoDB document stores",
        analogy="Think of the CAP Theorem like a group of friends sharing notes during an exam over walkie-talkies. **Consistency** means everyone has the exact same page answer. **Availability** means if you ask anyone a question, they must answer immediately. **Partition Tolerance** means someone cut the walkie-talkie wire! If the wire is cut, you must choose: either refuse to answer until the wire is fixed (**Consistency over Availability**), or give your best guess immediately (**Availability over Consistency**). You can't have both during a network split!",
        theory_sections=[
            {
                "heading": "Eric Brewer's CAP Theorem",
                "body": "In a distributed data store, you can guarantee at most two of three properties: **Consistency (C)** (every read receives the most recent write or an error), **Availability (A)** (every request receives a non-error response), and **Partition Tolerance (P)** (the system continues to operate despite network packet loss or dropped connections). Because network partitions are inevitable in real-world networks, distributed systems must choose between **CP** (e.g. MongoDB, HBase) or **AP** (e.g. Cassandra, DynamoDB)."
            },
            {
                "heading": "Document Stores & BSON Architecture",
                "body": "Document databases like **MongoDB** store data as flexible, hierarchical BSON (Binary JSON) documents. Unlike rigid relational schemas, documents within the same collection can have varying fields, nested sub-documents, and arrays. This eliminates complex joins for hierarchical business objects like user profiles and product catalogs."
            }
        ],
        code_snippets=[
            {
                "title": "BSON Document Model with Nested Objects and Arrays",
                "language": "json",
                "code": "{\n  \"_id\": \"66fb01a912e4\",\n  \"title\": \"Database Management Course\",\n  \"category\": \"TECH\",\n  \"tags\": [\"SQL\", \"NoSQL\", \"PostgreSQL\", \"MongoDB\"],\n  \"instructor\": {\n    \"name\": \"Dr. Arsalan\",\n    \"rating\": 4.9\n  },\n  \"modules\": [\n    { \"module\": 1, \"title\": \"Fundamentals\", \"days\": 4 }\n  ]\n}",
                "explanation": "MongoDB stores rich, nested hierarchical structures directly within a single self-contained BSON document."
            },
            {
                "title": "CRUD Operations in MongoDB Shell / PyMongo",
                "language": "javascript",
                "code": "// Insert Document\ndb.courses.insertOne({\n  title: 'Mobile App Development',\n  category: 'TECH',\n  studentsEnrolled: 1250\n});\n\n// Query Document with Filter\ndb.courses.find({ category: 'TECH', studentsEnrolled: { $gte: 1000 } });\n\n// Atomic Field Update\ndb.courses.updateOne(\n  { title: 'Mobile App Development' },\n  { $inc: { studentsEnrolled: 1 } }\n);",
                "explanation": "MongoDB uses JSON-like query filters and operators (`$gte`, `$inc`, `$set`)."
            },
            {
                "title": "Aggregation Pipeline in MongoDB",
                "language": "javascript",
                "code": "// Multi-stage aggregation pipeline: Match -> Group -> Sort\ndb.orders.aggregate([\n  { $match: { status: 'completed' } },\n  { $group: {\n      _id: '$category',\n      totalRevenue: { $sum: '$amount' },\n      orderCount: { $sum: 1 }\n  }},\n  { $sort: { totalRevenue: -1 } }\n]);",
                "explanation": "The aggregation pipeline transforms documents through stages, equivalent to SQL GROUP BY."
            },
            {
                "title": "Creating Indexes in MongoDB for High Performance",
                "language": "javascript",
                "code": "// Single field index\ndb.courses.createIndex({ title: 1 });\n\n// Compound index on category (asc) and studentsEnrolled (desc)\ndb.courses.createIndex({ category: 1, studentsEnrolled: -1 });",
                "explanation": "Indexes in MongoDB provide B-Tree performance on document fields and nested attributes."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="CAP Theorem Trade-Off Classifier",
            description="Write a Python function `classify_cap_choice(prioritizes_consistency: bool) -> str` that returns `'CP (Consistency & Partition Tolerance)'` if True, and `'AP (Availability & Partition Tolerance)'` if False.",
            starter_code="def classify_cap_choice(prioritizes_consistency: bool) -> str:\n    # Return CAP classification during network partition\n    pass",
            solution_code="def classify_cap_choice(prioritizes_consistency: bool) -> str:\n    if prioritizes_consistency:\n        return 'CP (Consistency & Partition Tolerance)'\n    return 'AP (Availability & Partition Tolerance)'",
            expected_output="classify_cap_choice(True) == 'CP (Consistency & Partition Tolerance)'"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="According to the CAP Theorem, why can't a distributed database guarantee both Consistency and Availability during a network partition?",
                options=[
                    "Because if network communication between nodes breaks (partition), nodes must either reject requests (sacrificing Availability) or serve potentially outdated data (sacrificing Consistency)",
                    "Because hard drives cannot store both numbers and text at the same time",
                    "Because computers lack enough memory",
                    "The CAP theorem only applies to laptops"
                ],
                correct_answer="Because if network communication between nodes breaks (partition), nodes must either reject requests (sacrificing Availability) or serve potentially outdated data (sacrificing Consistency)",
                explanation="During a network partition, a distributed system must choose between returning an error (CP) or stale data (AP)."
            ),
            QuizQuestionBlueprint(
                question="What data format does MongoDB use internally to store documents on disk?",
                options=[
                    "BSON (Binary JSON)",
                    "Plain CSV",
                    "HTML5",
                    "Assembly Code"
                ],
                correct_answer="BSON (Binary JSON)",
                explanation="MongoDB encodes documents in BSON (Binary JSON), extending JSON with datatypes like Date and ObjectId."
            ),
            QuizQuestionBlueprint(
                question="What is a major advantage of Document Databases (like MongoDB) over traditional Relational Schemas?",
                options=[
                    "Dynamic schemas that accommodate varying fields, embedded sub-documents, and arrays without rigid table migrations",
                    "They do not require computer memory",
                    "They make all queries run without an operating system",
                    "They never need backups"
                ],
                correct_answer="Dynamic schemas that accommodate varying fields, embedded sub-documents, and arrays without rigid table migrations",
                explanation="Document databases support flexible schemas and nested objects, aligning naturally with object-oriented code."
            ),
            QuizQuestionBlueprint(
                question="In MongoDB, what corresponds conceptually to an SQL 'Table'?",
                options=[
                    "Collection",
                    "Document",
                    "Row",
                    "Relation"
                ],
                correct_answer="Collection",
                explanation="In MongoDB terminology, a Collection is a grouped set of Documents, analogous to an SQL Table."
            ),
            QuizQuestionBlueprint(
                question="Which MongoDB operator atomically increments a numeric field by a specified value?",
                options=[
                    "$inc",
                    "$plus",
                    "$add",
                    "$increment"
                ],
                correct_answer="$inc",
                explanation="The `$inc` operator atomically increments a numeric attribute by a designated step."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 34
    # -------------------------------------------------------------
    DayBlueprint(
        order=34,
        title="Day 34: Key-Value Stores (Redis Architecture & Data Structures)",
        concept="Mastering in-memory key-value data structures: Strings, Hashes, Lists, Sets, Sorted Sets (ZSET), and Pub/Sub messaging",
        analogy="Think of a Key-Value Store like a giant wall of Amazon delivery lockers. Each locker has an exact barcode label on the door (the Key). You don't have to search inside other lockers. You scan the barcode (`GET user:100`), the door pops open in 0.1 milliseconds, and you retrieve whatever package you placed inside (the Value). Inside that locker, Redis lets you store strings, lists, or even sorted leaderboards!",
        theory_sections=[
            {
                "heading": "The Anatomy of a Key-Value Store",
                "body": "A Key-Value store represents the simplest and fastest NoSQL data model. Every data item is addressed by a unique string key. Redis (Remote Dictionary Server) elevates this concept by offering rich, in-memory data structures: Strings, Hashes, Lists, Sets, Sorted Sets (`ZSET`), Bitmaps, and HyperLogLogs. Operating purely in RAM with an asynchronous event loop, Redis delivers sub-millisecond responses."
            },
            {
                "heading": "Redis Persistence: RDB vs AOF",
                "body": "Although Redis is an in-memory store, it provides two persistent durability options: (1) **RDB (Redis Database Snapshot)** creates point-in-time binary snapshots of RAM to disk at specified intervals; (2) **AOF (Append-Only File)** logs every write command sequentially to an append-only log on disk, providing near-zero data loss."
            }
        ],
        code_snippets=[
            {
                "title": "Redis Strings & Hashes for Object Storage",
                "language": "bash",
                "code": "# String with 60-second TTL\nSET session:token_abc \"user_id_42\" EX 60\nGET session:token_abc\n\n# Hash data structure for structured user objects (like an in-memory row)\nHSET user:42 name \"Zainab\" email \"z@h.app\" credits 150\nHGET user:42 name\nHINCRBY user:42 credits 25 # Atomically increments credits to 175",
                "explanation": "Hashes allow reading and atomically modifying individual fields of an object without re-serializing."
            },
            {
                "title": "Redis Lists: Real-Time FIFO Queue",
                "language": "bash",
                "code": "# Push items to queue head\nLPUSH task_queue \"send_welcome_email:42\"\nLPUSH task_queue \"process_payment:101\"\n\n# Worker pops item from queue tail (FIFO)\nRPOP task_queue # Returns 'send_welcome_email:42'",
                "explanation": "Lists provide O(1) push and pop operations, powering fast background task queues."
            },
            {
                "title": "Redis Sorted Sets (ZSET): Real-Time Gaming Leaderboard",
                "language": "bash",
                "code": "# Add players with scores to a sorted set\nZADD game_leaderboard 1450 \"PlayerAlpha\"\nZADD game_leaderboard 1890 \"PlayerBravo\"\nZADD game_leaderboard 1200 \"PlayerCharlie\"\n\n# Retrieve top 2 highest scores with ranks in O(log N)\nZREVRANGE game_leaderboard 0 1 WITHSCORES",
                "explanation": "Sorted Sets maintain an automatically ordered ranking based on floating-point scores."
            },
            {
                "title": "Redis Pub/Sub Real-Time Broadcast Pattern",
                "language": "python",
                "code": "import redis\n\nr = redis.Redis()\n\n# Publisher sends notifications to a topic channel\ndef broadcast_announcement(channel: str, message: str):\n    r.publish(channel, message)\n\n# Subscriber listens on the channel\ndef listen_announcements(channel: str):\n    pubsub = r.pubsub()\n    pubsub.subscribe(channel)\n    for msg in pubsub.listen():\n        if msg['type'] == 'message':\n            print('Received Broadcast:', msg['data'].decode())",
                "explanation": "Pub/Sub allows broadcasting instant event notifications across multiple subscribed services."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Redis Key Namespace Formatter",
            description="Write a Python function `build_redis_key(domain: str, entity_id: str, field: str = '') -> str` that formats standard colon-separated Redis keys (e.g. `'user:101:profile'`).",
            starter_code="def build_redis_key(domain: str, entity_id: str, field: str = '') -> str:\n    # Return formatted colon-separated key\n    pass",
            solution_code="def build_redis_key(domain: str, entity_id: str, field: str = '') -> str:\n    if field and field.strip():\n        return f\"{domain.strip()}:{entity_id.strip()}:{field.strip()}\"\n    return f\"{domain.strip()}:{entity_id.strip()}\"",
            expected_output="build_redis_key('user', '42', 'session') == 'user:42:session'"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the primary advantage of storing data in a Key-Value store like Redis?",
                options=[
                    "Sub-millisecond query latency and extreme read/write throughput because all operations execute in RAM",
                    "It automatically creates SQL tables",
                    "It can only be accessed using C++",
                    "It requires no electricity"
                ],
                correct_answer="Sub-millisecond query latency and extreme read/write throughput because all operations execute in RAM",
                explanation="In-memory execution and direct key hashing yield unmatched speed."
            ),
            QuizQuestionBlueprint(
                question="Which Redis data structure is ideal for maintaining a real-time gaming or leaderboard ranking?",
                options=[
                    "Sorted Set (ZSET)",
                    "String",
                    "Bitmap",
                    "Hash"
                ],
                correct_answer="Sorted Set (ZSET)",
                explanation="Sorted Sets (ZSET) order elements by score using skip lists and hash tables, perfect for leaderboards."
            ),
            QuizQuestionBlueprint(
                question="What is the difference between RDB and AOF persistence in Redis?",
                options=[
                    "RDB creates point-in-time binary snapshots; AOF logs every single write command sequentially to an append-only log",
                    "RDB is for audio; AOF is for video",
                    "RDB deletes the database; AOF saves it",
                    "There is no difference"
                ],
                correct_answer="RDB creates point-in-time binary snapshots; AOF logs every single write command sequentially to an append-only log",
                explanation="RDB saves periodic snapshots; AOF logs operations continuously for durability."
            ),
            QuizQuestionBlueprint(
                question="What command atomically increments an integer value stored inside a Redis key?",
                options=[
                    "INCR",
                    "ADD_ONE",
                    "PLUS",
                    "STEP"
                ],
                correct_answer="INCR",
                explanation="`INCR key_name` atomically increments numerical values by 1."
            ),
            QuizQuestionBlueprint(
                question="Can Redis be used as a Message Broker between distributed microservices?",
                options=[
                    "Yes, using Redis Pub/Sub channels or Redis Streams",
                    "No, Redis is strictly a relational database",
                    "Only on Windows 95",
                    "Only for text files smaller than 10 bytes"
                ],
                correct_answer="Yes, using Redis Pub/Sub channels or Redis Streams",
                explanation="Redis Pub/Sub and Streams provide messaging capabilities between microservices."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 35
    # -------------------------------------------------------------
    DayBlueprint(
        order=35,
        title="Day 35: Column-Family Stores (Apache Cassandra Architecture)",
        concept="Handling petabyte-scale, high-velocity write workloads: Masterless peer-to-peer rings, LSM-Trees, Memtables, SSTables, and CQL",
        analogy="Think of Apache Cassandra like a decentralized group of 12 dispatchers seated in a round circle with walkie-talkies. There is no single 'boss dispatcher' (no master node; masterless architecture). If two dispatchers take a coffee break or their equipment breaks down, the other 10 dispatchers keep logging delivery trucks without pausing. Writes are stamped into an instant memory notebook (**Memtable**) and dumped to disk in batches (**SSTable**) at blinding speeds!",
        theory_sections=[
            {
                "heading": "Masterless Ring Architecture & High Availability",
                "body": "Traditional databases use a primary-replica model where writes fail if the primary goes down. **Apache Cassandra** uses a peer-to-peer, masterless ring architecture based on Amazon's Dynamo paper and Google's Bigtable. Every node is identical; any node can accept reads or writes (**AP system** in the CAP Theorem). Replication factors ensure data survives hardware failures with zero downtime."
            },
            {
                "heading": "Write Path: CommitLog, Memtable & SSTables",
                "body": "Cassandra achieves unmatched write performance by never doing random disk overwrites. Writes are appended sequentially to a **CommitLog** on disk for crash durability, stored in an in-memory **Memtable**, and periodically flushed as immutable **SSTables (Sorted String Tables)** to disk. Periodic **Compaction** merges duplicate SSTables in the background."
            }
        ],
        code_snippets=[
            {
                "title": "Creating a Keyspace and Table in Cassandra Query Language (CQL)",
                "language": "sql",
                "code": "-- Keyspace: Analogous to a Database Schema in RDBMS\nCREATE KEYSPACE telemetry_data\nWITH replication = {'class': 'SimpleStrategy', 'replication_factor': 3};\n\nUSE telemetry_data;\n\n-- Column-Family Table with Partition Key and Clustering Column\nCREATE TABLE sensor_readings (\n    device_id UUID,\n    recorded_date DATE,\n    reading_timestamp TIMESTAMP,\n    temperature FLOAT,\n    humidity FLOAT,\n    PRIMARY KEY ((device_id, recorded_date), reading_timestamp)\n) WITH CLUSTERING ORDER BY (reading_timestamp DESC);",
                "explanation": "CQL defines partition keys for data distribution across the ring and clustering columns for physical sorting."
            },
            {
                "title": "Writing High-Velocity Time-Series Data in CQL",
                "language": "sql",
                "code": "INSERT INTO sensor_readings (device_id, recorded_date, reading_timestamp, temperature, humidity)\nVALUES (\n    a1b2c3d4-e5f6-7a8b-9c0d-1e2f3a4b5c6d,\n    '2026-09-30',\n    toTimestamp(now()),\n    24.8,\n    55.2\n);",
                "explanation": "Writes are appended to the Memtable and CommitLog in microseconds."
            },
            {
                "title": "Querying Time-Series Data by Partition Key",
                "language": "sql",
                "code": "-- Fast sequential slice query on a single partition\nSELECT reading_timestamp, temperature, humidity\nFROM sensor_readings\nWHERE device_id = a1b2c3d4-e5f6-7a8b-9c0d-1e2f3a4b5c6d\n  AND recorded_date = '2026-09-30'\nLIMIT 50;",
                "explanation": "Cassandra queries must specify partition keys to route directly to target nodes."
            },
            {
                "title": "Configuring Tunable Consistency in Cassandra Client",
                "language": "python",
                "code": "from cassandra.cluster import Cluster\nfrom cassandra import ConsistencyLevel\nfrom cassandra.query import SimpleStatement\n\ncluster = Cluster(['192.168.1.10', '192.168.1.11'])\nsession = cluster.connect('telemetry_data')\n\n# Configure QUORUM consistency: (N/2 + 1) nodes must acknowledge write\nquery = SimpleStatement(\n    'INSERT INTO sensor_readings (device_id, recorded_date, reading_timestamp, temperature) VALUES (%s, %s, %s, %s)',\n    consistency_level=ConsistencyLevel.QUORUM\n)",
                "explanation": "Tunable consistency lets developers choose between ONE, QUORUM, or ALL consistency levels per query."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Quorum Calculator for Distributed Nodes",
            description="Write a Python function `calculate_quorum_size(replication_factor: int) -> int` that calculates the strict quorum majority `(N // 2) + 1`. Return 0 for invalid node counts.",
            starter_code="def calculate_quorum_size(replication_factor: int) -> int:\n    # Calculate Quorum majority size\n    pass",
            solution_code="def calculate_quorum_size(replication_factor: int) -> int:\n    if replication_factor <= 0:\n        return 0\n    return (replication_factor // 2) + 1",
            expected_output="calculate_quorum_size(3) == 2, calculate_quorum_size(5) == 3"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the primary architectural differentiator of Apache Cassandra compared to master-replica databases?",
                options=[
                    "It has a masterless, decentralized peer-to-peer ring architecture with no single point of failure",
                    "It does not use hard drives",
                    "It only runs on Raspberry Pi computers",
                    "It requires manual table creation in Excel"
                ],
                correct_answer="It has a masterless, decentralized peer-to-peer ring architecture with no single point of failure",
                explanation="In Cassandra, all nodes are peers; any node can coordinate reads and writes with zero downtime."
            ),
            QuizQuestionBlueprint(
                question="Why is Apache Cassandra capable of absorbing massive, petabyte-scale write workloads?",
                options=[
                    "Writes are appended sequentially to a CommitLog and in-memory Memtable, avoiding random disk seeks entirely",
                    "It deletes all old data automatically",
                    "It refuses to store text strings",
                    "It runs without electricity"
                ],
                correct_answer="Writes are appended sequentially to a CommitLog and in-memory Memtable, avoiding random disk seeks entirely",
                explanation="LSM-tree sequential write append mechanics eliminate expensive random disk I/O."
            ),
            QuizQuestionBlueprint(
                question="What query language is used to interact with Apache Cassandra?",
                options=[
                    "CQL (Cassandra Query Language)",
                    "HTML",
                    "GraphQL only",
                    "Bash"
                ],
                correct_answer="CQL (Cassandra Query Language)",
                explanation="CQL provides an SQL-like declarative interface for querying Column-Family tables."
            ),
            QuizQuestionBlueprint(
                question="What is a 'Memtable' in Cassandra's storage engine?",
                options=[
                    "An in-memory write buffer where data is stored and sorted before being flushed to SSTables on disk",
                    "A table that holds user passwords",
                    "A memory test utility",
                    "A table that is deleted when the query finishes"
                ],
                correct_answer="An in-memory write buffer where data is stored and sorted before being flushed to SSTables on disk",
                explanation="Memtables hold active writes in RAM, flushing immutable SSTables to disk once full."
            ),
            QuizQuestionBlueprint(
                question="What is 'Tunable Consistency' in Apache Cassandra?",
                options=[
                    "The ability to configure per-query consistency levels (e.g. ONE, QUORUM, ALL) based on application SLA requirements",
                    "A tool for tuning guitar musical instruments",
                    "A setting that turns the database into a relational database",
                    "A method to fix syntax errors"
                ],
                correct_answer="The ability to configure per-query consistency levels (e.g. ONE, QUORUM, ALL) based on application SLA requirements",
                explanation="Developers can choose per query whether to require ONE, QUORUM, or ALL node acknowledgments."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 36
    # -------------------------------------------------------------
    DayBlueprint(
        order=36,
        title="Day 36: Graph Databases (Neo4j & Cypher Query Language)",
        concept="Modeling densely connected data: Nodes, Relationships, Properties, and traversing social networks and fraud graphs with Cypher",
        analogy="Think of a Graph Database like a social map of mutual friends at a giant wedding party. In an RDBMS, finding 'friends of friends who like Italian food' requires joining 6 giant tables together through foreign keys, causing the server CPU to smoke! In a Graph Database like Neo4j, every person is a circle (Node) holding hands with their friends via physical pointers (Relationships). Finding a mutual friend is as simple as following the handshake in 1 millisecond!",
        theory_sections=[
            {
                "heading": "The Labeled Property Graph Model",
                "body": "In a graph database, data is represented as: (1) **Nodes** (entities like `:Person`, `:Product`), (2) **Relationships** (directed connections like `[:FRIENDS_WITH]`, `[:PURCHASED]`), and (3) **Properties** (key-value pairs stored on both nodes and relationships). Graph databases utilize **Index-Free Adjacency**: each node acts as a pointer directly to its neighbors, making traversal time O(1) per step regardless of total database size."
            },
            {
                "heading": "Cypher Query Language (Declarative ASCII-Art Queries)",
                "body": "Cypher uses visual ASCII-art pattern matching: `(p:Person)-[:PURCHASED]->(b:Book)`. Round parentheses `()` denote nodes; square brackets inside arrows `-[:TYPE]->` denote directed relationships. This makes queries for social networks, fraud detection, recommendation engines, and supply chain graphs vastly simpler and faster than 8-way SQL joins."
            }
        ],
        code_snippets=[
            {
                "title": "Creating Graph Nodes and Directed Relationships in Cypher",
                "language": "cypher",
                "code": "// Create two Person nodes and a mutual relationship\nCREATE (ali:Person {name: 'Ali Khan', age: 26})\nCREATE (zainab:Person {name: 'Zainab Bibi', age: 24})\nCREATE (react_course:Course {title: 'Mobile App Development', fee: 150})\n\n// Create directed relationships with properties\nCREATE (ali)-[:FRIENDS_WITH {since: 2022}]->(zainab)\nCREATE (ali)-[:ENROLLED_IN {date: '2026-09-01'}]->(react_course)\nCREATE (zainab)-[:ENROLLED_IN {date: '2026-09-05'}]->(react_course);",
                "explanation": "Creates nodes with properties and links them with typed, attributed relationships."
            },
            {
                "title": "Traversing Connections: Friends of Friends (Recommendation Query)",
                "language": "cypher",
                "code": "// Find courses that friends of Ali are enrolled in (Social Recommendation)\nMATCH (me:Person {name: 'Ali Khan'})-[:FRIENDS_WITH]->(friend:Person)-[:ENROLLED_IN]->(recommended:Course)\nWHERE NOT (me)-[:ENROLLED_IN]->(recommended)\nRETURN recommended.title, COUNT(friend) AS friend_count\nORDER BY friend_count DESC;",
                "explanation": "Expresses multi-hop relationship traversals using intuitive ASCII pattern matching."
            },
            {
                "title": "Finding the Shortest Path Between Two Nodes (Degrees of Separation)",
                "language": "cypher",
                "code": "// Find the shortest network path between two people\nMATCH (p1:Person {name: 'Ali Khan'}), (p2:Person {name: 'Sara Ahmed'})\nM = shortestPath((p1)-[:FRIENDS_WITH*..6]-(p2))\nRETURN M, length(M) AS degrees_of_separation;",
                "explanation": "`shortestPath` computes the minimal hops between distant nodes across millions of connections."
            },
            {
                "title": "Executing Cypher Queries from Python with Neo4j Driver",
                "language": "python",
                "code": "from neo4j import GraphDatabase\n\nuri = 'neo4j://localhost:7687'\nauth = ('neo4j', 'master_password')\n\nwith GraphDatabase.driver(uri, auth=auth) as driver:\n    with driver.session() as session:\n        result = session.run(\n            'MATCH (p:Person)-[:ENROLLED_IN]->(c:Course {title: $title}) RETURN p.name AS student',\n            title='Mobile App Development'\n        )\n        for record in result:\n            print('Enrolled Student:', record['student'])",
                "explanation": "Python backend services interact with Neo4j drivers using parameterized Cypher statements."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Cypher Node Syntax Generator",
            description="Write a Python function `build_cypher_node(label: str, properties: dict) -> str` that formats a valid Cypher node representation, e.g. `(:Person {name: 'Alice', age: 30})`.",
            starter_code="def build_cypher_node(label: str, properties: dict) -> str:\n    # Generate Cypher node pattern string\n    pass",
            solution_code="def build_cypher_node(label: str, properties: dict) -> str:\n    props = []\n    for k, v in properties.items():\n        val_str = f\"'{v}'\" if isinstance(v, str) else str(v)\n        props.append(f\"{k}: {val_str}\")\n    return f\"(:{label} {{{', '.join(props)}}})\"",
            expected_output="build_cypher_node('Person', {'name': 'Alice', 'age': 30}) == \"(:Person {name: 'Alice', age: 30})\""
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What are the three fundamental building blocks of a Graph Database model (like Neo4j)?",
                options=[
                    "Nodes (entities), Relationships (connections), and Properties (key-value attributes on both)",
                    "Rows, Columns, and Primary Keys",
                    "HTML, CSS, and JavaScript",
                    "Packets, Sockets, and Routers"
                ],
                correct_answer="Nodes (entities), Relationships (connections), and Properties (key-value attributes on both)",
                explanation="Graph databases model domains using Nodes, Relationships, and Properties."
            ),
            QuizQuestionBlueprint(
                question="What is 'Index-Free Adjacency' in graph database architecture?",
                options=[
                    "Each node holds direct physical memory pointers to its adjacent neighbor nodes, making traversal O(1) per step regardless of total database size",
                    "A database with no indexes allowed",
                    "A database that runs without a primary key",
                    "An open-source license format"
                ],
                correct_answer="Each node holds direct physical memory pointers to its adjacent neighbor nodes, making traversal O(1) per step regardless of total database size",
                explanation="Index-free adjacency enables constant-time pointer traversals without expensive index lookups."
            ),
            QuizQuestionBlueprint(
                question="What query language is used by Neo4j for declarative pattern-matching queries?",
                options=[
                    "Cypher",
                    "GraphQL",
                    "SQL-92",
                    "Regex"
                ],
                correct_answer="Cypher",
                explanation="Cypher uses ASCII-art syntax `(node)-[:REL]->(node)` for intuitive graph querying."
            ),
            QuizQuestionBlueprint(
                question="Which use case is ideally suited for a Graph Database over an RDBMS?",
                options=[
                    "Fraud ring detection, social network analysis, and recommendation engines requiring deep multi-hop relationship traversals",
                    "Standard single-table payroll check printing",
                    "Storing raw CCTV video streams",
                    "Basic key-value session caching"
                ],
                correct_answer="Fraud ring detection, social network analysis, and recommendation engines requiring deep multi-hop relationship traversals",
                explanation="Graph databases excel when queries navigate complex, interconnected networks of relationships."
            ),
            QuizQuestionBlueprint(
                question="How does Cypher visually represent a directed relationship from Person to Book in its syntax?",
                options=[
                    "(p:Person)-[:PURCHASED]->(b:Book)",
                    "Person JOIN Book ON id",
                    "Person.connect(Book)",
                    "Book <- Person"
                ],
                correct_answer="(p:Person)-[:PURCHASED]->(b:Book)",
                explanation="Parentheses represent nodes `()`, and arrows `-[:TYPE]->` represent directed relationships."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 37
    # -------------------------------------------------------------
    DayBlueprint(
        order=37,
        title="Day 37: Database Administration (RBAC, Backup & Disaster Recovery)",
        concept="Securing and maintaining enterprise database infrastructure: Role-Based Access Control, Physical vs Logical Backups, and Point-In-Time Recovery (PITR)",
        analogy="Think of database administration like guarding and maintaining a royal treasury. **RBAC** ensures the castle cook only has keys to the spice pantry (read-only on recipes), while only the chief treasurer has keys to the gold vault. **Backups** are like creating an exact duplicate wax mold of every coin every night (**Physical Backup**). If a dragon burns the castle at 2:15 PM, **Point-In-Time Recovery** rewinds the security ledger to 2:14 PM so not a single gold coin is lost!",
        theory_sections=[
            {
                "heading": "Role-Based Access Control (RBAC) & Principle of Least Privilege",
                "body": "Never connect production applications using the superuser `postgres` or `root` account. Under the **Principle of Least Privilege**, create distinct roles with granular permissions: readonly roles (`GRANT SELECT ON ...`), application read-write roles (`GRANT SELECT, INSERT, UPDATE, DELETE ON ...`), and migration roles with DDL privileges. Revoke all public schema creation permissions."
            },
            {
                "heading": "Logical vs Physical Backups & Point-in-Time Recovery (PITR)",
                "body": "**Logical Backups** (`pg_dump`) generate SQL text scripts containing DDL and INSERT statements; they are portable across versions but slow to restore on multi-terabyte databases. **Physical Backups** (`pg_basebackup`) copy the raw disk blocks directly, restoring at disk speeds. When combined with continuous **WAL Archiving**, databases achieve **Point-In-Time Recovery (PITR)**, allowing administrators to restore the database to any exact second in the past."
            }
        ],
        code_snippets=[
            {
                "title": "Configuring Roles and Granular RBAC Permissions",
                "language": "sql",
                "code": "-- 1. Create a Read-Only Analyst Role\nCREATE ROLE readonly_analyst WITH LOGIN PASSWORD 'secure_analyst_pwd';\nGRANT CONNECT ON DATABASE production_db TO readonly_analyst;\nGRANT USAGE ON SCHEMA public TO readonly_analyst;\nGRANT SELECT ON ALL TABLES IN SCHEMA public TO readonly_analyst;\n\n-- 2. Create Application Read-Write Role (No DDL DROP/ALTER rights!)\nCREATE ROLE app_service_user WITH LOGIN PASSWORD 'prod_app_secret';\nGRANT CONNECT ON DATABASE production_db TO app_service_user;\nGRANT USAGE ON SCHEMA public TO app_service_user;\nGRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO app_service_user;\nGRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO app_service_user;",
                "explanation": "Enforces least privilege by separating read-only reporting roles from application write roles."
            },
            {
                "title": "Executing Logical Backups with pg_dump",
                "language": "bash",
                "code": "# Dump entire production database to compressed custom format\npg_dump -h db.internal -U postgres -F c -b -v -f prod_backup_$(date +%Y%m%d).dump production_db\n\n# Restore from compressed dump with parallel jobs\npg_restore -h new_db.internal -U postgres -d production_db -j 4 -v prod_backup_20260930.dump",
                "explanation": "pg_dump exports portable logical backups; pg_restore reconstructs schemas with parallel threads."
            },
            {
                "title": "Setting Up Continuous WAL Archiving for PITR",
                "language": "ini",
                "code": "# postgresql.conf settings for Point-In-Time Recovery\nwal_level = replica\narchive_mode = on\narchive_command = 'test ! -f /mnt/wal_archive/%f && cp %p /mnt/wal_archive/%f'\narchive_timeout = 300 # Flush WAL at least every 5 minutes",
                "explanation": "Continuous WAL archiving enables point-in-time recovery to any historical second."
            },
            {
                "title": "Performing Point-In-Time Recovery (recovery.signal)",
                "language": "ini",
                "code": "# Place recovery.signal in data directory and configure target timestamp:\n# recovery.signal\nrestore_command = 'cp /mnt/wal_archive/%f %p'\nrecovery_target_time = '2026-09-30 14:14:00+00'\nrecovery_target_action = 'promote'",
                "explanation": "Replays WAL files up to the target timestamp, stopping right before an accidental table drop."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="RBAC Grant Statement Formatter",
            description="Write a Python function `format_grant_sql(privileges: list[str], table: str, role: str) -> str` that produces a valid `GRANT <privs> ON TABLE <table_name> TO <role_name>;` SQL string.",
            starter_code="def format_grant_sql(privileges: list[str], table: str, role: str) -> str:\n    # Return formatted GRANT SQL statement\n    pass",
            solution_code="def format_grant_sql(privileges: list[str], table: str, role: str) -> str:\n    priv_str = ', '.join([p.upper().strip() for p in privileges])\n    return f\"GRANT {priv_str} ON TABLE {table} TO {role};\"",
            expected_output="format_grant_sql(['SELECT', 'INSERT'], 'orders', 'app_user') == 'GRANT SELECT, INSERT ON TABLE orders TO app_user;'"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the Principle of Least Privilege in database security?",
                options=[
                    "Every user and application service should be granted only the minimum permissions necessary to perform their job and nothing more",
                    "All users should share the master root password",
                    "Databases should run without authentication",
                    "Developers should have full DROP TABLE privileges in production"
                ],
                correct_answer="Every user and application service should be granted only the minimum permissions necessary to perform their job and nothing more",
                explanation="Least privilege restricts access rights to prevent accidental or malicious data modification."
            ),
            QuizQuestionBlueprint(
                question="What is the difference between a Logical Backup (`pg_dump`) and a Physical Backup (`pg_basebackup`)?",
                options=[
                    "Logical backups export SQL commands and DDL scripts; Physical backups copy raw data files and disk blocks directly",
                    "Logical backups only backup text; Physical backups only backup numbers",
                    "Physical backups can only be written on floppy disks",
                    "There is no difference"
                ],
                correct_answer="Logical backups export SQL commands and DDL scripts; Physical backups copy raw data files and disk blocks directly",
                explanation="Logical backups export portable SQL statements; physical backups mirror raw filesystem clusters."
            ),
            QuizQuestionBlueprint(
                question="What capability does continuous WAL archiving provide during database recovery?",
                options=[
                    "Point-In-Time Recovery (PITR), allowing the database to be restored to any exact second before a disaster occurred",
                    "It automatically doubles the network bandwidth",
                    "It creates automated UI interfaces",
                    "It eliminates the need for passwords"
                ],
                correct_answer="Point-In-Time Recovery (PITR), allowing the database to be restored to any exact second before a disaster occurred",
                explanation="Replaying archived WAL logs enables point-in-time recovery up to any desired timestamp."
            ),
            QuizQuestionBlueprint(
                question="Why is connecting a public web API using the `postgres` superuser considered a critical security vulnerability?",
                options=[
                    "If an attacker discovers an SQL Injection vulnerability, they gain total administrative control over the entire database server and host OS",
                    "It causes the database to delete all indexes",
                    "The superuser account is only valid for 1 hour",
                    "Superuser queries run 10x slower"
                ],
                correct_answer="If an attacker discovers an SQL Injection vulnerability, they gain total administrative control over the entire database server and host OS",
                explanation="Superusers bypass all security checks; compromising a superuser connection grants full system control."
            ),
            QuizQuestionBlueprint(
                question="What command restores a database from a custom-format dump generated with `pg_dump -F c`?",
                options=[
                    "pg_restore",
                    "pg_load",
                    "sql_import",
                    "db_rebuild"
                ],
                correct_answer="pg_restore",
                explanation="`pg_restore` is the dedicated PostgreSQL utility for restoring custom or directory format archives."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 38
    # -------------------------------------------------------------
    DayBlueprint(
        order=38,
        title="Day 38: Database Security (SQL Injection, Encryption & Audit)",
        concept="Hardening databases against attacks: SQL Injection prevention with parameterized queries, Data at Rest (TDE), TLS in transit, and continuous monitoring",
        analogy="Think of SQL Injection like ordering at a drive-thru microphone. You say: 'I want a burger.' But a hacker whispers into the microphone: 'I want a burger; AND OPEN THE SAFE AND THROW ALL THE CASH OUT THE WINDOW; --'. If the drive-thru computer blindly sends that whole string to the kitchen robot, the robot robs the safe! Parameterized queries put the order onto a pre-printed form where the kitchen only reads burger orders—treating everything else as harmless plain text!",
        theory_sections=[
            {
                "heading": "The Anatomy & Elimination of SQL Injection (SQLi)",
                "body": "SQL Injection occurs when untrusted user input is directly concatenated into a SQL statement. The input breaks out of the data context and enters the command interpreter, allowing attackers to bypass authentication (`' OR '1'='1`), extract sensitive tables, or delete data. **The absolute defense is Parameterized Queries (Prepared Statements)**: user inputs are sent separately as raw parameters, never parsed as executable SQL."
            },
            {
                "heading": "Encryption: Data in Transit vs Data at Rest",
                "body": "**Data in Transit** is secured using TLS/SSL encryption, preventing man-in-the-middle sniffing of queries and credentials. **Data at Rest** is secured using Transparent Data Encryption (TDE), encrypting underlying data files and WAL blocks on disk with AES-256 so stolen physical SSDs cannot be mounted or read without the cryptographic key."
            }
        ],
        code_snippets=[
            {
                "title": "Vulnerable String Concatenation vs Secure Parameterized Query",
                "language": "python",
                "code": "# FATAL SECURITY VULNERABILITY (SQL Injection):\n# userInput = \"admin' OR '1'='1\"\n# query = f\"SELECT * FROM users WHERE username = '{userInput}';\" # EXECUTABLE SQL INJECTED!\n\n# SECURE: Parameterized Query (Prepared Statement)\n# Input is treated strictly as data literals; injection is mathematically impossible!\ncursor.execute(\n    'SELECT id, username, password_hash FROM users WHERE username = %s AND is_active = %s;',\n    (user_input, True)\n)",
                "explanation": "Parameterized queries decouple query logic from data inputs, neutralizing SQL injection."
            },
            {
                "title": "Enforcing Mandatory SSL/TLS in PostgreSQL (pg_hba.conf)",
                "language": "text",
                "code": "# pg_hba.conf: Reject all unencrypted plaintext connections!\n# TYPE  DATABASE        USER            ADDRESS                 METHOD\nhostssl all             all             0.0.0.0/0               scram-sha-256\n# Connections without SSL certificate encryption are blocked immediately.",
                "explanation": "`hostssl` mandates that all network connections use TLS/SSL encryption."
            },
            {
                "title": "Column-Level Sensitive Data Encryption with pgcrypto",
                "language": "sql",
                "code": "-- Enable cryptographic extension\nCREATE EXTENSION IF NOT EXISTS pgcrypto;\n\n-- Encrypt sensitive National ID or Credit Card at column level using AES\nINSERT INTO user_confidential (user_id, encrypted_cnic)\nVALUES (\n    42,\n    pgp_sym_encrypt('42101-1234567-1', 'SuperSecretMasterKey2026')\n);\n\n-- Decrypt only when authorized\nSELECT pgp_sym_decrypt(encrypted_cnic, 'SuperSecretMasterKey2026') AS cnic\nFROM user_confidential\nWHERE user_id = 42;",
                "explanation": "pgcrypto encrypts sensitive columns with AES sym-encryption directly inside the database."
            },
            {
                "title": "Continuous Database Query Monitoring with pg_stat_statements",
                "language": "sql",
                "code": "-- Identify slowest queries and anomalous spikes across all connections\nSELECT \n    round(total_exec_time::numeric, 2) AS total_time_ms,\n    calls,\n    round(mean_exec_time::numeric, 2) AS avg_time_ms,\n    query\nFROM pg_stat_statements\nORDER BY total_exec_time DESC\nLIMIT 10;",
                "explanation": "pg_stat_statements tracks execution metrics across all queries, pinpointing anomalies and slow queries."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="SQL Injection Danger Detector",
            description="Write a Python function `detect_sqli_risk(raw_sql: str) -> bool` that returns `True` if a raw SQL string contains direct Python string formatting interpolation markers (`%s` with `%`, `.format(`, or `f\"...{`) rather than parameterized driver tuples.",
            starter_code="def detect_sqli_risk(raw_sql: str) -> bool:\n    # Return True if SQL string uses dangerous string interpolation\n    pass",
            solution_code="def detect_sqli_risk(raw_sql: str) -> bool:\n    s = raw_sql.strip()\n    dangerous_markers = ['.format(', 'f\"', \"f'\", '% (']\n    return any(m in s for m in dangerous_markers)",
            expected_output="detect_sqli_risk(\"SELECT * FROM users WHERE name = '\" + u) == False, detect_sqli_risk(\"f'SELECT * FROM users WHERE id = {uid}'\") == True"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the single most effective defense against SQL Injection attacks?",
                options=[
                    "Using Parameterized Queries (Prepared Statements) for all user inputs",
                    "Replacing all database passwords every 24 hours",
                    "Writing all table names in uppercase",
                    "Running the database on port 80"
                ],
                correct_answer="Using Parameterized Queries (Prepared Statements) for all user inputs",
                explanation="Parameterized queries pass parameters separately from executable code, neutralizing injection."
            ),
            QuizQuestionBlueprint(
                question="What is 'Transparent Data Encryption' (TDE)?",
                options=[
                    "Encrypting database data files and transaction logs on physical storage at rest using keys like AES-256",
                    "Making all database tables public for everyone to see",
                    "Deleting passwords from database memory",
                    "Writing queries in plaintext"
                ],
                correct_answer="Encrypting database data files and transaction logs on physical storage at rest using keys like AES-256",
                explanation="TDE encrypts files at rest, protecting physical media against unauthorized extraction."
            ),
            QuizQuestionBlueprint(
                question="What does an attacker achieve with the classic `' OR '1'='1` injection on a login form?",
                options=[
                    "The OR condition evaluates to TRUE for all rows, bypassing password authentication and returning the first account (often admin)",
                    "It converts the user's password into 1",
                    "It causes the user's monitor to restart",
                    "It downloads a PDF of the database"
                ],
                correct_answer="The OR condition evaluates to TRUE for all rows, bypassing password authentication and returning the first account (often admin)",
                explanation="Injecting `' OR '1'='1` creates a tautology that always evaluates to TRUE, bypassing checks."
            ),
            QuizQuestionBlueprint(
                question="What PostgreSQL extension provides cryptographic hashing and AES encryption functions inside SQL?",
                options=[
                    "pgcrypto",
                    "pg_ssl",
                    "crypto_db",
                    "sec_shield"
                ],
                correct_answer="pgcrypto",
                explanation="`pgcrypto` provides cryptographic algorithms (SHA, AES, Blowfish) directly in PostgreSQL."
            ),
            QuizQuestionBlueprint(
                question="What is the role of `pg_stat_statements` in database monitoring?",
                options=[
                    "It tracks execution statistics, total runtimes, and invocation counts across all normalized queries run on the server",
                    "It blocks all connections from mobile devices",
                    "It generates invoices for database hosting",
                    "It compiles SQL into JavaScript"
                ],
                correct_answer="It tracks execution statistics, total runtimes, and invocation counts across all normalized queries run on the server",
                explanation="pg_stat_statements gathers execution metrics, pinpointing high-latency queries and performance regressions."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 39
    # -------------------------------------------------------------
    DayBlueprint(
        order=39,
        title="Day 39: Scaling Databases - Vertical vs Horizontal, Replication & Sharding",
        concept="Scaling systems to millions of users: Scale-Up vs Scale-Out, Read Replicas, Primary-Replica streaming, and Horizontal Sharding partitions",
        analogy="Think of database scaling like transporting goods for a growing company. **Vertical Scaling (Scale Up)** is buying a bigger, faster monster truck with 16 wheels and a giant engine (putting 128 CPU cores and 1TB RAM in one server—expensive and hits physical limits). **Horizontal Scaling (Scale Out)** is buying a fleet of 50 normal vans driving in parallel. One van delivers to Karachi, one to Lahore, and one to Islamabad (**Sharding / Partitioning**)!",
        theory_sections=[
            {
                "heading": "Vertical Scaling vs Horizontal Scaling",
                "body": "**Vertical Scaling (Scale-Up)** involves upgrading hardware specifications (CPU, RAM, NVMe SSDs). It requires zero application code changes, but hits strict hardware ceilings and financial diminishing returns. **Horizontal Scaling (Scale-Out)** adds more server nodes working in unison, providing virtually unlimited capacity."
            },
            {
                "heading": "Replication & Sharding Architecture",
                "body": "**Read Replication**: A single Primary node handles all writes (`INSERT`, `UPDATE`), streaming its Write-Ahead Log to multiple read-only Replica nodes that handle user reads. **Horizontal Sharding**: When a dataset outgrows a single machine's disk or write capacity, tables are partitioned across multiple independent database nodes using a **Shard Key** (e.g. `hash(user_id) % num_shards`)."
            }
        ],
        code_snippets=[
            {
                "title": "Primary-Replica Streaming Replication Configuration (PostgreSQL)",
                "language": "ini",
                "code": "# On Primary node (postgresql.conf):\nwal_level = replica\nmax_wal_senders = 10\nwal_keep_size = 1024MB\n\n# On Read Replica node (postgresql.conf):\nprimary_conninfo = 'host=primary.db.internal port=5432 user=rep_user password=secret'\nhot_standby = on # Allows read-only queries while continuously replaying WAL",
                "explanation": "Configures real-time streaming replication from primary to read-only replica nodes."
            },
            {
                "title": "Application-Level Read/Write Splitting with Python",
                "language": "python",
                "code": "import psycopg2\n\n# Write pool connects strictly to Primary\nprimary_conn = psycopg2.connect('host=db-primary.internal user=app')\n\n# Read pool connects to Load-Balanced Read Replicas\nreplica_conn = psycopg2.connect('host=db-replica-lb.internal user=app')\n\ndef create_order(user_id, amount):\n    # Direct all writes to Primary\n    with primary_conn.cursor() as cur:\n        cur.execute('INSERT INTO orders (user_id, amount) VALUES (%s, %s);', (user_id, amount))\n        \ndef fetch_user_orders(user_id):\n    # Offload all heavy reads to Replicas!\n    with replica_conn.cursor() as cur:\n        cur.execute('SELECT * FROM orders WHERE user_id = %s;', (user_id,))\n        return cur.fetchall()",
                "explanation": "Directs writes to the primary while distributing read loads across read replicas."
            },
            {
                "title": "PostgreSQL Native Declarative Partitioning (Range Sharding)",
                "language": "sql",
                "code": "-- Master partitioned table\nCREATE TABLE order_events (\n    event_id SERIAL,\n    event_date DATE NOT NULL,\n    payload JSONB,\n    PRIMARY KEY (event_id, event_date)\n) PARTITION BY RANGE (event_date);\n\n-- Child partitions for specific calendar years\nCREATE TABLE order_events_2025 PARTITION OF order_events\n    FOR VALUES FROM ('2025-01-01') TO ('2026-01-01');\n\nCREATE TABLE order_events_2026 PARTITION OF order_events\n    FOR VALUES FROM ('2026-01-01') TO ('2027-01-01');",
                "explanation": "Declarative partitioning splits large tables into manageable child partitions by date range."
            },
            {
                "title": "Hash-Based Shard Router Algorithm",
                "language": "python",
                "code": "import hashlib\n\nSHARD_NODES = ['db-shard-1.internal', 'db-shard-2.internal', 'db-shard-3.internal', 'db-shard-4.internal']\n\ndef get_shard_host_for_user(user_id: str) -> str:\n    # Consistent hash distribution across shard nodes\n    hash_val = int(hashlib.md5(user_id.encode()).hexdigest(), 16)\n    shard_index = hash_val % len(SHARD_NODES)\n    return SHARD_NODES[shard_index]",
                "explanation": "Hashes the shard key to route operations deterministically to the target database node."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Consistent Hash Shard Router",
            description="Write a Python function `route_to_shard(key: str, total_shards: int) -> int` that computes the MD5 hash of `key` as an integer and returns the 0-based shard index `hash_int % total_shards`.",
            starter_code="def route_to_shard(key: str, total_shards: int) -> int:\n    # Compute 0-based shard index\n    pass",
            solution_code="import hashlib\n\ndef route_to_shard(key: str, total_shards: int) -> int:\n    if total_shards <= 0:\n        return 0\n    hash_int = int(hashlib.md5(key.encode()).hexdigest(), 16)\n    return hash_int % total_shards",
            expected_output="route_to_shard('user_1042', 4) in [0, 1, 2, 3]"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the fundamental difference between Vertical Scaling (Scale Up) and Horizontal Scaling (Scale Out)?",
                options=[
                    "Vertical Scaling adds more CPU/RAM to a single machine; Horizontal Scaling adds more independent machine nodes to a cluster",
                    "Vertical scaling is for databases; Horizontal scaling is only for web browsers",
                    "Horizontal scaling is strictly illegal in cloud environments",
                    "There is no difference"
                ],
                correct_answer="Vertical Scaling adds more CPU/RAM to a single machine; Horizontal Scaling adds more independent machine nodes to a cluster",
                explanation="Scale Up upgrades hardware capacity on a single node; Scale Out distributes load across multiple nodes."
            ),
            QuizQuestionBlueprint(
                question="What is a 'Read Replica' in database architecture?",
                options=[
                    "A read-only copy of the primary database that asynchronously replays write logs, offloading read query traffic from the primary node",
                    "A physical copy of the database printed on paper",
                    "A tool for creating fake data",
                    "A replica that only runs on weekends"
                ],
                correct_answer="A read-only copy of the primary database that asynchronously replays write logs, offloading read query traffic from the primary node",
                explanation="Read replicas replicate state from the primary to serve read queries at high concurrency."
            ),
            QuizQuestionBlueprint(
                question="What is 'Database Sharding'?",
                options=[
                    "Partitioning rows of a large dataset across multiple independent database servers based on a shard key",
                    "Deleting old tables",
                    "Compressing tables into ZIP files",
                    "Restoring backups after a crash"
                ],
                correct_answer="Partitioning rows of a large dataset across multiple independent database servers based on a shard key",
                explanation="Sharding distributes subsets of data across separate database instances to scale write throughput."
            ),
            QuizQuestionBlueprint(
                question="What is 'Replication Lag' in an asynchronous primary-replica database setup?",
                options=[
                    "The slight time delay between when a write commits on the primary and when it is replayed on the read replica",
                    "The time it takes to boot the computer",
                    "A network error that deletes rows",
                    "A database shutdown command"
                ],
                correct_answer="The slight time delay between when a write commits on the primary and when it is replayed on the read replica",
                explanation="Replication lag is the delay before asynchronous writes reflect on replica nodes."
            ),
            QuizQuestionBlueprint(
                question="Why is choosing an effective 'Shard Key' critical in sharded database architectures?",
                options=[
                    "A bad shard key leads to 'Hotspots' where a single shard receives 90% of traffic, defeating the purpose of distributed scaling",
                    "It changes the color of the database console",
                    "It determines how much the cloud provider charges for electricity",
                    "Shard keys are optional and never used"
                ],
                correct_answer="A bad shard key leads to 'Hotspots' where a single shard receives 90% of traffic, defeating the purpose of distributed scaling",
                explanation="Uniform shard key distribution prevents unbalanced hotspots on individual database nodes."
            )
        ]
    ),

    # -------------------------------------------------------------
    # DAY 40
    # -------------------------------------------------------------
    DayBlueprint(
        order=40,
        title="Day 40 (Capstone Project): Cloud Databases (OLTP vs OLAP) - E-Commerce Cloud DB Architecture",
        concept="Architecting a complete production cloud database infrastructure: Managed Cloud SQL/RDS (OLTP), Snowflake/BigQuery (OLAP), Read Replicas, and CDC Pipelines",
        analogy="Think of enterprise cloud database architecture like a global retail empire. The checkout cash registers in thousands of retail stores must scan items in 100 milliseconds without freezing (**OLTP - Row-Oriented, High Concurrency Transactions**). At midnight, automated freight carriers transport carbon-copy receipts (**CDC / ETL Pipeline**) to the headquarters mega-vault (**OLAP Data Warehouse - Columnar, Deep Analytical Queries**) where executives run 5-year sales trends without slowing down store cash registers!",
        theory_sections=[
            {
                "heading": "OLTP vs OLAP Architectural Separation",
                "body": "**OLTP (Online Transaction Processing)** databases (e.g. AWS Aurora PostgreSQL, Google Cloud SQL) are row-oriented engines optimized for millions of atomic, fast, sub-second single-row lookups and updates. **OLAP (Online Analytical Processing)** data warehouses (e.g. Snowflake, Google BigQuery, ClickHouse) are columnar engines optimized for aggregations across billions of historical records. Running complex multi-year analytics directly on production OLTP databases exhausts CPU and crashes customer checkout flows."
            },
            {
                "heading": "Change Data Capture (CDC) & The Modern Data Stack",
                "body": "Modern architectures bridge OLTP and OLAP using **Change Data Capture (CDC)** (e.g. Debezium, Kafka). CDC monitors the database's Write-Ahead Log (WAL) in real time, streaming row changes into analytical data lakes without placing query load on the operational database."
            }
        ],
        code_snippets=[
            {
                "title": "Production E-Commerce OLTP Schema (PostgreSQL Cloud SQL / Aurora)",
                "language": "sql",
                "code": "-- High-concurrency transactional schema with strict constraints\nCREATE TABLE customers (\n    customer_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),\n    email VARCHAR(120) UNIQUE NOT NULL,\n    full_name VARCHAR(100) NOT NULL,\n    tier VARCHAR(20) DEFAULT 'bronze'\n);\n\nCREATE TABLE orders (\n    order_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),\n    customer_id UUID NOT NULL REFERENCES customers(customer_id),\n    status VARCHAR(20) NOT NULL CHECK (status IN ('pending', 'paid', 'shipped', 'cancelled')),\n    total_cents BIGINT NOT NULL CHECK (total_cents >= 0),\n    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP\n);\n\nCREATE INDEX idx_orders_customer_status ON orders(customer_id, status);",
                "explanation": "Row-oriented, highly normalized OLTP schema for transactional checkout consistency."
            },
            {
                "title": "OLAP Columnar Fact Table (Snowflake / BigQuery DDL)",
                "language": "sql",
                "code": "-- OLAP Columnar Data Warehouse Star Schema (Fact Table)\nCREATE TABLE fact_daily_sales (\n    date_key INT NOT NULL,              -- Foreign key to dim_date\n    product_key INT NOT NULL,           -- Foreign key to dim_product\n    customer_key INT NOT NULL,          -- Foreign key to dim_customer\n    channel_key INT NOT NULL,           -- Foreign key to dim_channel\n    quantity_sold INT NOT NULL,\n    total_revenue_cents BIGINT NOT NULL,\n    profit_margin_percent DECIMAL(5, 2)\n) CLUSTER BY (date_key, channel_key);",
                "explanation": "Columnar fact table designed for multi-million row aggregations and business intelligence reports."
            },
            {
                "title": "Simulating Change Data Capture (CDC) Event Stream",
                "language": "json",
                "code": "{\n  \"source\": \"ecommerce_oltp.public.orders\",\n  \"op\": \"u\",\n  \"before\": {\n    \"order_id\": \"d3b07384\",\n    \"status\": \"pending\"\n  },\n  \"after\": {\n    \"order_id\": \"d3b07384\",\n    \"status\": \"paid\",\n    \"paid_at\": \"2026-09-30T17:30:00Z\"\n  },\n  \"ts_ms\": 1790789400000\n}",
                "explanation": "Debezium/Kafka CDC payload capturing transactional row changes from the WAL for streaming to OLAP."
            },
            {
                "title": "High-Performance OLAP Analytical Query (Year-over-Year Revenue)",
                "language": "sql",
                "code": "-- Columnar analytical query scanning billions of rows in seconds\nSELECT \n    d.year,\n    d.quarter,\n    p.category,\n    SUM(f.total_revenue_cents) / 100.0 AS quarterly_revenue_usd,\n    ROUND(AVG(f.profit_margin_percent), 2) AS avg_margin\nFROM fact_daily_sales f\nJOIN dim_date d ON f.date_key = d.date_key\nJOIN dim_product p ON f.product_key = p.product_key\nWHERE d.year IN (2025, 2026)\nGROUP BY d.year, d.quarter, p.category\nORDER BY d.year, d.quarter, quarterly_revenue_usd DESC;",
                "explanation": "Scans compressed column blocks across millions of records without locking operational transaction tables."
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Workload Classifier: OLTP vs OLAP",
            description="Write a Python function `classify_workload(is_subsecond_single_row: bool, involves_billions_aggregation: bool) -> str` that returns `'OLTP'` for fast single-row transactions, `'OLAP'` for heavy multi-row aggregations, and `'Hybrid'` otherwise.",
            starter_code="def classify_workload(is_subsecond_single_row: bool, involves_billions_aggregation: bool) -> str:\n    # Return 'OLTP', 'OLAP', or 'Hybrid'\n    pass",
            solution_code="def classify_workload(is_subsecond_single_row: bool, involves_billions_aggregation: bool) -> str:\n    if is_subsecond_single_row and not involves_billions_aggregation:\n        return 'OLTP'\n    elif involves_billions_aggregation and not is_subsecond_single_row:\n        return 'OLAP'\n    return 'Hybrid'",
            expected_output="classify_workload(True, False) == 'OLTP', classify_workload(False, True) == 'OLAP'"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the primary difference between OLTP and OLAP database systems?",
                options=[
                    "OLTP is row-oriented and optimized for high-concurrency transactional lookups and writes; OLAP is columnar and optimized for massive historical analytical aggregations",
                    "OLTP only works on laptops; OLAP only works on supercomputers",
                    "OLAP cannot store numbers",
                    "There is no difference in architecture"
                ],
                correct_answer="OLTP is row-oriented and optimized for high-concurrency transactional lookups and writes; OLAP is columnar and optimized for massive historical analytical aggregations",
                explanation="OLTP handles low-latency operational transactions; OLAP handles heavy analytics over massive historical datasets."
            ),
            QuizQuestionBlueprint(
                question="Why is it considered bad engineering practice to run multi-year analytics queries directly on production OLTP databases?",
                options=[
                    "The massive table scans exhaust CPU, saturate memory buffers, and acquire locks that slow down or crash customer checkout transactions",
                    "It converts the database into a NoSQL database",
                    "It causes internet service providers to block your domain",
                    "It deletes all primary keys"
                ],
                correct_answer="The massive table scans exhaust CPU, saturate memory buffers, and acquire locks that slow down or crash customer checkout transactions",
                explanation="Heavy analytical workloads compete for CPU, RAM, and locks with critical operational user transactions."
            ),
            QuizQuestionBlueprint(
                question="What is 'Change Data Capture' (CDC) in modern cloud data architectures?",
                options=[
                    "A design pattern that reads transaction logs (WAL) in real time to stream database changes into analytical warehouses or search indexes without impacting OLTP performance",
                    "A tool for changing passwords",
                    "A software that tracks keyboard keystrokes",
                    "A method for editing HTML files"
                ],
                correct_answer="A design pattern that reads transaction logs (WAL) in real time to stream database changes into analytical warehouses or search indexes without impacting OLTP performance",
                explanation="CDC tails transaction logs to stream real-time updates to downstream warehouses and caches without querying tables."
            ),
            QuizQuestionBlueprint(
                question="Which of the following is an example of a modern Cloud OLAP Data Warehouse?",
                options=[
                    "Google BigQuery / Snowflake",
                    "Redis",
                    "SQLite",
                    "Memcached"
                ],
                correct_answer="Google BigQuery / Snowflake",
                explanation="Google BigQuery and Snowflake are columnar cloud data warehouses built specifically for OLAP workloads."
            ),
            QuizQuestionBlueprint(
                question="What is the benefit of a managed cloud database service (such as AWS RDS or Google Cloud SQL)?",
                options=[
                    "Automated OS patching, automated point-in-time backups, high availability failover, and hardware scaling managed by the cloud provider",
                    "Free internet for all users",
                    "It writes all application code automatically",
                    "It prevents developers from making syntax errors"
                ],
                correct_answer="Automated OS patching, automated point-in-time backups, high availability failover, and hardware scaling managed by the cloud provider",
                explanation="Managed services eliminate infrastructure maintenance overhead by automating provisioning, backups, and failover."
            )
        ],
        is_project_day=True,
        project_name="E-Commerce Cloud Database Architecture Capstone"
    )
]
