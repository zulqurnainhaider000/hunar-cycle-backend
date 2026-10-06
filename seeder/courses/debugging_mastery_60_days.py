"""
Complete Debugging & Problem Solving 60-Day Curriculum Blueprint
Assembles all 60 days of topic-per-day lessons, deep ELI5 analogies,
progressive code snippets, daily debugging challenges, milestone projects, and 5 MCQs per day.
"""

from seeder.course_blueprint import CourseBlueprint
from seeder.courses.debugging_curriculum_days_1_15 import DAYS_1_TO_15
from seeder.courses.debugging_curriculum_days_16_30 import DAYS_16_TO_30
from seeder.courses.debugging_curriculum_days_31_45 import DAYS_31_TO_45
from seeder.courses.debugging_curriculum_days_46_60 import DAYS_46_TO_60

# Consolidate all 60 days in strict sequential order
ALL_60_DAYS = DAYS_1_TO_15 + DAYS_16_TO_30 + DAYS_31_TO_45 + DAYS_46_TO_60

DEBUGGING_MASTERY_COURSE_BLUEPRINT = CourseBlueprint(
    title="Debugging & Problem Solving",
    category="TECH",
    description=(
        "Master the art and science of debugging, systematic troubleshooting, and engineering problem-solving. "
        "A rigorous 60-Day immersive curriculum covering: "
        "Module 1: Problem Solving Fundamentals & Mindset (Bug taxonomy, Developer Mindset, Algorithm Design, Flowcharts, Divide & Conquer, Error Types); "
        "Module 2: Basic Debugging Strategies (Reproducing bugs, Rubber Duck Debugging, Wolf Fence / Binary Search Debugging, Print vs Log, RTFM & Docs, Smart Googling & GitHub Issues); "
        "Module 3: Reading Errors & Exception Handling (Error message anatomy, Stack Traces, Try/Catch/Except/Finally, Custom Exceptions, Defensive Programming, Fail-Safe Input Processor Project); "
        "Module 4: Using IDE Debugger Tools (Visual Debuggers, Breakpoints, Conditional Breakpoints, Stepping, Watches, Dynamic Expressions, Call Stack Inspection); "
        "Module 5: Web & Frontend Debugging (Browser DevTools, Console APIs, DOM & CSS Debugging, Network Panel, Storage & Cookies, Responsive & Mobile Simulation); "
        "Module 6: Backend, API & Database Debugging (Postman/Insomnia, HTTP Status Codes 400s vs 500s, Database Slow Queries & Locks, SQL EXPLAIN Profiling, Broken REST API Fix Project); "
        "Module 7: Logging & Monitoring (Logging vs Prints, Log Levels, Structured JSON Logging, ELK & Centralized Logging, Sentry Crash Tracking, APM Datadog/New Relic); "
        "Module 8: Complex Bugs & Concurrency Issues (Memory Leaks & Heap Dumps, Code Profiling, Garbage Collection Tuning, Race Conditions & Deadlocks, Infinite Loop Circuit Breakers); "
        "Module 9: Production Level Debugging (Local Reproduction of Prod Bugs, Remote Debugging & SSH Tunnels, Core Dumps & GDB, Root Cause Analysis & 5 Whys, Incident Post-Mortems); "
        "Module 10: Bug Prevention & Testing (Static Analysis & Linters, Code Reviews & Pair Programming, Unit Testing with PyTest/Jest, Test-Driven Development TDD, Integration Testing, E2E Testing with Playwright, CI/CD Quality Gates, Day 60 Capstone: The Great Bug Hunt). "
        "Features 60 practical debugging challenges with broken starter code, fixed solutions, and 300 knowledge verification quizzes."
    ),
    color="#EF4444",
    days=ALL_60_DAYS
)
