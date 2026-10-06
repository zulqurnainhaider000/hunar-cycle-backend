"""
Complete Mobile App Development 40-Day Curriculum Blueprint
Assembles all 40 days of topic-per-day lessons, deep ELI5 analogies,
progressive code snippets, daily coding challenges, project days, and 5 MCQs per day.
"""

from seeder.course_blueprint import CourseBlueprint
from seeder.courses.mobile_curriculum_days_1_10 import DAYS_1_TO_10
from seeder.courses.mobile_curriculum_days_11_20 import DAYS_11_TO_20
from seeder.courses.mobile_curriculum_days_21_30 import DAYS_21_TO_30
from seeder.courses.mobile_curriculum_days_31_40 import DAYS_31_TO_40

# Consolidate all 40 days in strict sequential order
ALL_40_DAYS = DAYS_1_TO_10 + DAYS_11_TO_20 + DAYS_21_TO_30 + DAYS_31_TO_40

MOBILE_MASTERY_COURSE_BLUEPRINT = CourseBlueprint(
    title="Mobile App Development",
    category="TECH",
    description=(
        "The comprehensive 40-Day Mobile App Development Mastery Roadmap. "
        "Enforced universal topic-per-day architecture: App Basics & UI (React Native & Flutter), "
        "Stack & Tab Navigation, State Management (Redux/Context), APIs & Networking, "
        "Local Storage (SQLite/AsyncStorage), Device Hardware & Biometrics, Firebase & Cloud BaaS, "
        "Micro-Interactions & Lottie Animations, MVVM Architecture, and App Store Publishing with CI/CD. "
        "Features 40 hands-on coding challenges and 200 knowledge verification quizzes."
    ),
    color="#6366F1",
    days=ALL_40_DAYS
)
