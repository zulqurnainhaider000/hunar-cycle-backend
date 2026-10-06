"""
Complete Database Management 40-Day Curriculum Blueprint
Assembles all 40 days of topic-per-day lessons, deep ELI5 analogies,
progressive code snippets, daily coding challenges, project days, and 5 MCQs per day.
"""

from seeder.course_blueprint import CourseBlueprint
from seeder.courses.database_curriculum_days_1_10 import DAYS_1_TO_10
from seeder.courses.database_curriculum_days_11_20 import DAYS_11_TO_20
from seeder.courses.database_curriculum_days_21_30 import DAYS_21_TO_30
from seeder.courses.database_curriculum_days_31_40 import DAYS_31_TO_40

# Consolidate all 40 days in strict sequential order
ALL_40_DAYS = DAYS_1_TO_10 + DAYS_11_TO_20 + DAYS_21_TO_30 + DAYS_31_TO_40

DATABASE_MASTERY_COURSE_BLUEPRINT = CourseBlueprint(
    title="Database Management",
    category="TECH",
    description=(
        "The comprehensive 40-Day Database Management Mastery Roadmap. "
        "Enforced universal topic-per-day architecture: Database Fundamentals, Relational Models & Keys, "
        "Basic & Advanced SQL (DDL, DML, DQL, Aggregation, JOINs, Subqueries, CTEs, Window Functions), "
        "Database Normalization & Constraints, Programmability (Stored Procedures, UDFs, Triggers), "
        "ACID Transactions & Concurrency Control, Deadlock Resolution, B-Tree Indexing & Query Plans, "
        "NoSQL Paradigms (MongoDB, Redis, Cassandra, Neo4j), Administration & Security, and Cloud Architecture with OLTP/OLAP. "
        "Features 40 hands-on coding challenges and 200 knowledge verification quizzes."
    ),
    color="#0284C7",
    days=ALL_40_DAYS
)
