"""
Complete APIs & Web Services Architecture 60-Day Curriculum Blueprint
Assembles all 60 days of topic-per-day lessons, deep ELI5 analogies,
progressive code snippets, daily API challenges, milestone projects, and 5 MCQs per day.
"""

from seeder.course_blueprint import CourseBlueprint
from seeder.courses.api_curriculum_days_1_15 import DAYS_1_TO_15
from seeder.courses.api_curriculum_days_16_30 import DAYS_16_TO_30
from seeder.courses.api_curriculum_days_31_45 import DAYS_31_TO_45
from seeder.courses.api_curriculum_days_46_60 import DAYS_46_TO_60

# Consolidate all 60 days in strict sequential order
ALL_60_DAYS = DAYS_1_TO_15 + DAYS_16_TO_30 + DAYS_31_TO_45 + DAYS_46_TO_60

API_MASTERY_COURSE_BLUEPRINT = CourseBlueprint(
    title="Complete APIs & Web Services Architecture",
    category="TECH",
    description=(
        "The definitive 60-Day APIs & Web Services Architecture Roadmap. "
        "Enforced universal topic-per-day architecture across 9 core phases: "
        "Phase 1: API Fundamentals & Architectures (Web Services vs APIs, REST/SOAP/RPC/GraphQL, JSON vs XML, Sync vs Async); "
        "Phase 2: HTTP Protocol & Core Concepts (Request/Response Cycle, HTTP Verbs, Status Codes 1xx-5xx, Headers, URI/URL/URN); "
        "Phase 3: REST Architecture (6 Constraints, Statelessness, Cacheability, Uniform Interface, Layered System, Resources & Nouns, HATEOAS, Day 18 Milestone); "
        "Phase 4: API Design & Best Practices (Plural Naming, Full CRUD, Filtering/Sorting/Searching, Offset vs Cursor Pagination, URI/Header Versioning, Idempotency, RFC 7807 Errors, Day 26 Milestone); "
        "Phase 5: API Security & Authentication (API Keys, Basic vs Bearer, JWT Signature & Claims, OAuth 2.0 & OIDC, CORS & Preflight, Rate Limiting, OWASP API Top 10, Day 34 Milestone); "
        "Phase 6: API Integration & Consumption (Postman/cURL, Fetch/Axios/Requests, DTOs & Deserialization, Error Handling & Timeouts, Async Concurrency, Client Pagination, Exponential Backoff & Jitter); "
        "Phase 7: Real-Time & Advanced Integration (Webhooks & HMAC Signatures, WebSockets Full-Duplex, Server-Sent Events, Polling vs Long Polling vs Sockets, GraphQL SDL/Resolvers/DataLoader, gRPC & Protocol Buffers); "
        "Phase 8: Documentation & Quality Engineering (OpenAPI 3.0 / Swagger, ReDoc & DX, Unit Testing & Mocking, Integration Testing & Mock Servers, k6 & Artillery Load Testing); "
        "Phase 9: API Management, DevOps & Architecture (API Gateways Kong/NGINX, Microservices & Service Mesh, Multi-tier Caching with Redis & ETag, Observability & Distributed Tracing with OpenTelemetry, CI/CD with Contract Testing, API Monetization with Stripe, and Day 60 Capstone Enterprise API Architecture). "
        "Features 60 hands-on coding challenges and 300 knowledge verification quizzes."
    ),
    color="#0EA5E9",
    days=ALL_60_DAYS
)
