"""
Complete Python Mastery 35-Day Curriculum Blueprint
Assembles all 35 days of topic-per-day lessons, deep ELI5 analogies,
code snippets, daily coding challenges, project days, and 5 MCQs per day.
"""

from seeder.course_blueprint import CourseBlueprint
from courses.python_curriculum_days_1_10 import DAYS_1_TO_10
from courses.python_curriculum_days_11_20 import DAYS_11_TO_20
from courses.python_curriculum_days_21_30 import DAYS_21_TO_30
from courses.python_curriculum_days_31_35 import DAYS_31_TO_35

# Consolidate all 35 days in sequential order
ALL_35_DAYS = DAYS_1_TO_10 + DAYS_11_TO_20 + DAYS_21_TO_30 + DAYS_31_TO_35

PYTHON_MASTERY_COURSE_BLUEPRINT = CourseBlueprint(
    title="Python Programming Fundamentals",
    category="TECH",
    description=(
        "The definitive 35-Day Python Mastery Journey. Built on an enforced "
        "topic-per-day architecture: deep beginner-friendly theory with ELI5 real-world "
        "analogies, 4-5 progressive code walkthroughs, daily hands-on coding challenges, "
        "5 multi-choice knowledge verification quizzes each day, and 6 full-scale project days."
    ),
    color="#3B82F6",
    days=ALL_35_DAYS
)
