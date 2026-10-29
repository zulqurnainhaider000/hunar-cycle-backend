"""
Curriculum Builder Helper
Utility to cleanly construct validated CourseBlueprints and DayBlueprints
with guaranteed compliance to the platform standards.
"""

from typing import List, Dict, Any, Tuple
from seeder.course_blueprint import (
    CourseBlueprint,
    DayBlueprint,
    QuizQuestionBlueprint,
    CodingChallengeBlueprint,
)

def make_day(
    order: int,
    title: str,
    concept: str,
    analogy: str,
    sections: List[Tuple[str, str]], # [(heading, body), ...]
    snippets: List[Tuple[str, str, str]], # [(title, code, lang), ...]
    challenge: Tuple[str, str, str, str, str], # (title, desc, starter, solution, expected_output)
    quizzes: List[Tuple[str, List[str], str, str]], # [(question, options, correct, explanation), ...] exactly 5
) -> DayBlueprint:
    """Constructs and validates a single DayBlueprint."""
    theory_sections = [{"heading": s[0], "body": s[1]} for s in sections]
    code_snippets = [
        {"title": sn[0], "code": sn[1], "language": sn[2], "explanation": f"Implementation walkthrough for {sn[0]}."}
        for sn in snippets
    ]
    coding_challenge = CodingChallengeBlueprint(
        title=challenge[0],
        description=challenge[1],
        starter_code=challenge[2],
        solution_code=challenge[3],
        expected_output=challenge[4]
    )
    quiz_blueprints = [
        QuizQuestionBlueprint(
            question=q[0],
            options=q[1],
            correct_answer=q[2],
            explanation=q[3]
        )
        for q in quizzes
    ]

    day = DayBlueprint(
        order=order,
        title=title,
        concept=concept,
        analogy=analogy,
        theory_sections=theory_sections,
        code_snippets=code_snippets,
        coding_challenge=coding_challenge,
        quizzes=quiz_blueprints
    )
    day.validate()
    return day

def make_course(
    title: str,
    category: str,
    description: str,
    color: str,
    days: List[DayBlueprint]
) -> CourseBlueprint:
    """Constructs and validates a CourseBlueprint."""
    course = CourseBlueprint(
        title=title,
        category=category,
        description=description,
        color=color,
        days=days
    )
    course.validate()
    return course
