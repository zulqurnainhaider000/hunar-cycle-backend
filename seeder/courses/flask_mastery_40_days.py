"""
Complete Web Development with Flask 40-Day Curriculum Blueprint
Assembles all 40 days of topic-per-day lessons, deep ELI5 analogies,
code snippets, daily coding challenges, project days, and 5 MCQs per day.
"""

from seeder.course_blueprint import CourseBlueprint
from seeder.courses.flask_curriculum_days_1_10 import DAYS_1_TO_10
from seeder.courses.flask_curriculum_days_11_20 import DAYS_11_TO_20
from seeder.courses.flask_curriculum_days_21_30 import DAYS_21_TO_30
from seeder.courses.flask_curriculum_days_31_40 import DAYS_31_TO_40

# Consolidate all 40 days in strict sequential order
ALL_40_DAYS = DAYS_1_TO_10 + DAYS_11_TO_20 + DAYS_21_TO_30 + DAYS_31_TO_40

FLASK_MASTERY_COURSE_BLUEPRINT = CourseBlueprint(
    title="Web Development with Flask",
    category="TECH",
    description=(
        "The definitive 40-Day Flask Web Development Mastery Roadmap. "
        "Enforced universal topic-per-day architecture: Basics & Setup, Jinja2 Templates, "
        "Flask-WTF Forms, State Management, SQLAlchemy ORM, RBAC Security, Blueprints, "
        "RESTful APIs, Celery & WebSockets, Testing with Pytest, and Docker Deployment. "
        "Features 40 hands-on coding challenges and 200 knowledge verification quizzes."
    ),
    color="#10B981",
    days=ALL_40_DAYS
)
