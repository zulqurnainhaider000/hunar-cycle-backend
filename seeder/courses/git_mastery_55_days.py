"""
Complete Git & Version Control System 55-Day Curriculum Blueprint
Assembles all 55 days of topic-per-day lessons, deep ELI5 analogies,
exact Git CLI commands, terminal outputs, daily coding/terminal challenges, project days, and 5 MCQs per day.
"""

from seeder.course_blueprint import CourseBlueprint
from seeder.courses.git_curriculum_days_1_15 import DAYS_1_TO_15
from seeder.courses.git_curriculum_days_16_30 import DAYS_16_TO_30
from seeder.courses.git_curriculum_days_31_42 import DAYS_31_TO_42
from seeder.courses.git_curriculum_days_43_55 import DAYS_43_TO_55

# Consolidate all 55 days in strict sequential order
ALL_55_DAYS = DAYS_1_TO_15 + DAYS_16_TO_30 + DAYS_31_TO_42 + DAYS_43_TO_55

GIT_MASTERY_COURSE_BLUEPRINT = CourseBlueprint(
    title="Git & Version Control System",
    category="TECH",
    description=(
        "The comprehensive 55-Day Git & Version Control System Roadmap. "
        "Enforced universal topic-per-day architecture: "
        "Version Control Foundation & Git Basics (Local/Centralized/DVCS, Git vs GitHub/GitLab, SSH & HTTPS Setup, Global & Local Config, git init & .git Anatomy, Three Trees Architecture, Daily Workflow, 50/72 Commit Rules, Log Visualizations, .gitignore Rules), "
        "Branching & Merging (HEAD Pointers, Branch Switching & Creation, Branch Renaming & Deletion, Fast-Forward vs 3-Way Merges, Conflict Resolution, Visual 3-Way Merge Tools), "
        "Remote Repositories (Remotes & Aliases, Cloning & Shallow Clones, Upstream Push Tracking, Fetching vs Pulling, Remote-Tracking Branches, Syncing Collaboration Lab), "
        "Undoing Changes (Unstaging with restore, Discarding Working Tree Changes, Amending Commits, Reset soft/mixed/hard, Reverting Public Commits), "
        "Advanced Git Operations (Stashing, Rebase vs Merge Golden Rule, Interactive Rebase, Squashing & Fixup, Cherry-Picking, SemVer Tagging, Reflog Black Box, Disaster Recovery Lab), "
        "Collaboration & Workflows (Forking Model, PRs/MRs Architecture, Empathetic Code Review, Gitflow vs GitHub Flow vs Trunk-Based Development), "
        "Debugging & Code Search (git blame, git grep, Automated Bug Hunting with git bisect, git diff variants), "
        "Git Internals & Expert Features (Blobs, Trees, Commits, SHA Hashes, Submodules, Git Worktrees, Pre-commit & Pre-push Hooks, Git LFS Large Files, Custom Aliases), and "
        "Standards & Automation (Conventional Commits, Semantic Versioning SemVer, GitHub Actions / GitLab CI, Automated Production CI/CD Pipeline Capstone). "
        "Features 55 hands-on terminal coding challenges and 275 verified knowledge verification quizzes."
    ),
    color="#F05032",
    days=ALL_55_DAYS
)
