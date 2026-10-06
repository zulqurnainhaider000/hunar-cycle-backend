"""
Course Blueprint & Universal Validation Standards
Enforces the mandatory template for all courses on the platform:
- One Topic Per Day
- Deep ELI5 Theory Content with Real-World Analogy
- 4-5 Progressive Code Snippets
- Daily Coding Challenge
- Exactly 5 Multiple-Choice Questions per Day linked to the LessonStep
"""

from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any


@dataclass
class QuizQuestionBlueprint:
    question: str
    options: List[str]
    correct_answer: str
    explanation: Optional[str] = None

    def validate(self, day_number: int, q_index: int):
        if not self.question or len(self.question.strip()) < 10:
            raise ValueError(f"Day {day_number} Quiz #{q_index}: Question text is too short or empty.")
        if len(self.options) != 4:
            raise ValueError(f"Day {day_number} Quiz #{q_index}: Must have exactly 4 options, got {len(self.options)}.")
        if self.correct_answer not in self.options:
            raise ValueError(f"Day {day_number} Quiz #{q_index}: correct_answer '{self.correct_answer}' must be one of the options.")


@dataclass
class CodingChallengeBlueprint:
    title: str
    description: str
    starter_code: str
    solution_code: str
    expected_output: Optional[str] = None


@dataclass
class DayBlueprint:
    order: int
    title: str
    concept: str
    analogy: str
    theory_sections: List[Dict[str, str]] # e.g. [{"heading": "...", "body": "..."}]
    code_snippets: List[Dict[str, str]]    # e.g. [{"title": "...", "code": "..."}]
    coding_challenge: Any                  # CodingChallengeBlueprint or dict
    quizzes: List[Any]                     # List[QuizQuestionBlueprint] or list of dicts
    is_project_day: bool = False
    project_name: Optional[str] = None

    def __post_init__(self):
        # Normalize coding_challenge if passed as a dictionary
        if isinstance(self.coding_challenge, dict):
            self.coding_challenge = CodingChallengeBlueprint(
                title=self.coding_challenge.get('title', 'Daily Coding Challenge'),
                description=self.coding_challenge.get('description') or self.coding_challenge.get('instructions', ''),
                starter_code=self.coding_challenge.get('starter_code', ''),
                solution_code=self.coding_challenge.get('solution_code', ''),
                expected_output=self.coding_challenge.get('expected_output')
            )

        # Normalize quizzes if passed as dictionaries
        normalized_quizzes = []
        for q in self.quizzes:
            if isinstance(q, dict):
                normalized_quizzes.append(
                    QuizQuestionBlueprint(
                        question=q.get('question', ''),
                        options=q.get('options', []),
                        correct_answer=q.get('correct_answer', ''),
                        explanation=q.get('explanation')
                    )
                )
            else:
                normalized_quizzes.append(q)
        self.quizzes = normalized_quizzes

    def validate(self):
        if not (1 <= self.order <= 365):
            raise ValueError(f"Day order must be positive integer, got {self.order}")
        if not self.title or not self.concept or not self.analogy:
            raise ValueError(f"Day {self.order}: title, concept, and analogy must not be empty.")
        if len(self.code_snippets) < 2:
            raise ValueError(f"Day {self.order}: Must contain at least 2 code snippets, got {len(self.code_snippets)}.")
        if len(self.quizzes) != 5:
            raise ValueError(f"Day {self.order}: Must contain exactly 5 quizzes, got {len(self.quizzes)}.")
        for idx, q in enumerate(self.quizzes, start=1):
            q.validate(self.order, idx)

    def generate_markdown(self) -> str:
        """
        Compiles the structured day content into rich, standardized long-form Markdown
        strictly following the format:
        Theory (ELI5 + Analogy) -> Progressive Code Snippets -> Daily Coding Challenge
        """
        md_lines = []
        md_lines.append(f"# {self.title}")
        md_lines.append(f"**Core Concept**: *{self.concept}*\n")
        
        # Real-World Analogy (ELI5)
        md_lines.append(f"## 💡 Real-World Analogy (Explain Like I'm 5)\n")
        md_lines.append(f"> {self.analogy}\n")
        
        # In-Depth Theory Sections
        for section in self.theory_sections:
            md_lines.append(f"## {section['heading']}\n")
            body_content = section.get('body') or section.get('content') or ''
            md_lines.append(f"{body_content}\n")

        # Code Walkthroughs
        md_lines.append("## 💻 Progressive Code Examples\n")
        for idx, snippet in enumerate(self.code_snippets, start=1):
            md_lines.append(f"### Example {idx}: {snippet['title']}\n")
            if 'explanation' in snippet:
                md_lines.append(f"{snippet['explanation']}\n")
            lang = snippet.get('language', 'python')
            md_lines.append(f"```{lang}\n{snippet['code'].strip()}\n```\n")

        # Daily Coding Challenge
        md_lines.append("## 🎯 Daily Coding Challenge\n")
        md_lines.append(f"### {self.coding_challenge.title}\n")
        md_lines.append(f"{self.coding_challenge.description}\n")
        
        if self.coding_challenge.starter_code:
            md_lines.append("**Starter Code:**\n")
            md_lines.append(f"```python\n{self.coding_challenge.starter_code.strip()}\n```\n")

        if self.coding_challenge.expected_output:
            md_lines.append("**Expected Output:**\n")
            md_lines.append(f"```text\n{self.coding_challenge.expected_output.strip()}\n```\n")

        return "\n".join(md_lines)

    def get_consolidated_code_snippet(self) -> str:
        """
        Consolidates the code snippets into an executable Python file string for testing/IDE.
        """
        chunks = []
        for idx, snippet in enumerate(self.code_snippets, start=1):
            chunks.append(f"# --- Example {idx}: {snippet['title']} ---")
            chunks.append(snippet['code'].strip())
            chunks.append("")
        
        chunks.append("# --- Daily Challenge Solution ---")
        chunks.append(self.coding_challenge.solution_code.strip())
        return "\n".join(chunks)


@dataclass
class CourseBlueprint:
    title: str
    category: str
    description: str
    color: str
    days: List[DayBlueprint] = field(default_factory=list)

    def validate(self):
        if not self.title or not self.category:
            raise ValueError("Course title and category cannot be empty.")
        if len(self.days) == 0:
            raise ValueError("Course must have at least 1 day.")
        
        # Verify sequence
        orders = [d.order for d in self.days]
        if orders != list(range(1, len(self.days) + 1)):
            raise ValueError(f"Days must be sequentially ordered from 1 to {len(self.days)}. Got: {orders}")

        for day in self.days:
            day.validate()
