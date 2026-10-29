"""
Language & Global Communication Mastery Blueprint
Comprehensive curriculum covering conversational fluency, English grammar fundamentals,
business correspondence, active listening, and cross-cultural communication.
"""

from seeder.course_blueprint import (
    CourseBlueprint,
    DayBlueprint,
    QuizQuestionBlueprint,
    CodingChallengeBlueprint,
)

DAYS = [
    DayBlueprint(
        order=1,
        title="Day 1: Foundations of Clear English & Active Vocabulary",
        concept="Fluency is built on high-frequency core vocabulary and confident sentence syntax, not memorizing obscure dictionaries.",
        analogy="Learning a language is like learning to play the guitar. You only need 4 fundamental chords to play 80% of all popular songs. In English, mastering the 500 most frequent words gives you comprehension of most daily conversations.",
        theory_sections=[
            {
                "heading": "The 80/20 Rule in Language Acquisition",
                "body": "The top 1,000 words in the English language account for over 85% of speech in typical daily and professional interactions. Focusing on active retrieval of these core verbs and connecting words yields 10x faster conversational fluency than passive grammar drilling."
            },
            {
                "heading": "The Power of Collocations",
                "body": "Native speakers think in word clusters called collocations (e.g., 'make a decision', 'take a break', 'catch a flight'). Learning phrases as unified chunks eliminates unnatural word-by-word mental translation."
            }
        ],
        code_snippets=[
            {
                "title": "Vocabulary Frequency Analyzer (Python)",
                "explanation": "Analyzes a transcript to identify high-frequency words and vocabulary richness.",
                "language": "python",
                "code": """def analyze_vocabulary_richness(text: str):
    words = text.lower().split()
    unique_words = set(words)
    total_words = len(words)
    lexical_density = len(unique_words) / total_words if total_words > 0 else 0
    return total_words, len(unique_words), round(lexical_density * 100, 2)

total, unique, density = analyze_vocabulary_richness("Practice daily to speak clearly and listen actively in every conversation")
print(f"Total: {total} | Unique: {unique} | Lexical Density: {density}%")"""
            },
            {
                "title": "Collocation Pairing Validator",
                "explanation": "Validates common natural verb-noun combinations in professional English.",
                "language": "python",
                "code": """NATURAL_COLLOCATIONS = {
    'decision': ['make', 'reach', 'postpone'],
    'mistake': ['make', 'correct', 'admit'],
    'progress': ['make', 'track', 'evaluate'],
}

def is_natural_collocation(verb: str, noun: str) -> bool:
    allowed = NATURAL_COLLOCATIONS.get(noun.lower(), [])
    return verb.lower() in allowed

print("make a decision:", is_natural_collocation("make", "decision")) # True
print("do a mistake:", is_natural_collocation("do", "mistake"))       # False (Say 'make a mistake')"""
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Word Count & Fluency Metric",
            description="Write a function `calculate_speaking_rate(total_words, minutes)` that computes Words Per Minute (WPM) rounded to 1 decimal place.",
            starter_code="""def calculate_speaking_rate(total_words: int, minutes: float) -> float:
    # Your code here
    pass""",
            solution_code="""def calculate_speaking_rate(total_words: int, minutes: float) -> float:
    if minutes <= 0:
        return 0.0
    return round(total_words / minutes, 1)""",
            expected_output="140.0"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is a 'collocation' in language study?",
                options=[
                    "A natural combination of words that frequently occur together",
                    "A punctuation mark used to separate independent clauses",
                    "A rare idiom used only in ancient legal manuscripts",
                    "A grammatical error caused by incorrect capitalization"
                ],
                correct_answer="A natural combination of words that frequently occur together",
                explanation="Collocations are pairs or groups of words that habitually co-occur, such as 'make an effort' instead of 'do an effort'."
            ),
            QuizQuestionBlueprint(
                question="Which of the following is the natural English collocation?",
                options=[
                    "Make a mistake",
                    "Do a mistake",
                    "Perform an error",
                    "Produce a mistake"
                ],
                correct_answer="Make a mistake",
                explanation="In standard English, the natural verb paired with 'mistake' is 'make'."
            ),
            QuizQuestionBlueprint(
                question="Why is chunking phrases more effective than translating word-by-word?",
                options=[
                    "It bypasses the slow mental translation step and improves fluency",
                    "It eliminates the need to speak with any accents",
                    "It is legally required when drafting business contracts",
                    "It automatically doubles your vocabulary overnight"
                ],
                correct_answer="It bypasses the slow mental translation step and improves fluency",
                explanation="Learning chunks enables instantaneous speech retrieval without translating single words from your native language."
            ),
            QuizQuestionBlueprint(
                question="What is the average conversational speaking rate for standard English?",
                options=[
                    "130 to 160 words per minute",
                    "30 to 50 words per minute",
                    "300 to 450 words per minute",
                    "10 to 20 words per minute"
                ],
                correct_answer="130 to 160 words per minute",
                explanation="A comfortable conversational and presentation pace ranges between 130 and 160 words per minute."
            ),
            QuizQuestionBlueprint(
                question="In active listening, what does 'paraphrasing' demonstrate?",
                options=[
                    "You comprehended the speaker's core message and verified understanding",
                    "You disagree with everything the speaker just said",
                    "You want to immediately change the topic of conversation",
                    "You are testing the speaker's grammatical accuracy"
                ],
                correct_answer="You comprehended the speaker's core message and verified understanding",
                explanation="Paraphrasing shows the speaker you heard and processed their thoughts in your own words."
            )
        ]
    ),
    DayBlueprint(
        order=2,
        title="Day 2: Professional Business Writing & Executive Email Etiquette",
        concept="Executive communication prioritizes brevity, clarity, and clear calls-to-action (CTA).",
        analogy="Think of a professional email like a billboard on a highway. Drivers are traveling at 70 mph; if your billboard has 500 words of fine print, no one will read it. You need a bold headline and a single clear exit sign.",
        theory_sections=[
            {
                "heading": "The BLUF Framework (Bottom Line Up Front)",
                "body": "Busy executives and clients skim messages in seconds. Start with your primary request or decision (the BLUF) in the opening sentence. Provide supporting context and bullet points underneath."
            },
            {
                "heading": "Tone and Register: Polite Yet Decisive",
                "body": "Avoid passive-aggressive phrasing like 'Per my last email'. Instead, use objective, collaborative language: 'As discussed on Tuesday' or 'Following up to ensure we stay on schedule'."
            }
        ],
        code_snippets=[
            {
                "title": "Email Subject Line Auditor (Python)",
                "explanation": "Validates whether an email subject line is concise and actionable.",
                "language": "python",
                "code": """def audit_subject_line(subject: str) -> dict:
    char_len = len(subject)
    has_action = any(tag in subject.upper() for tag in ['ACTION', 'URGENT', 'UPDATE', 'APPROVAL', 'REVIEW'])
    is_ideal_length = 30 <= char_len <= 60
    return {
        'length': char_len,
        'ideal_length': is_ideal_length,
        'action_oriented': has_action,
        'grade': 'A' if is_ideal_length and has_action else 'B' if is_ideal_length else 'C'
    }

print(audit_subject_line("[ACTION REQUIRED] Q3 Budget Review due Thursday"))"""
            },
            {
                "title": "Tone Replacer for Professional Correspondence",
                "explanation": "Replaces outdated or friction-heavy phrases with modern executive alternatives.",
                "language": "python",
                "code": """PROFESSIONAL_REPLACEMENTS = {
    "per my last email": "as discussed earlier",
    "sorry for the delay": "thank you for your patience",
    "obviously": "as noted in the findings",
    "as soon as possible": "by Friday at 3:00 PM EST"
}

def polish_email_draft(text: str) -> str:
    cleaned = text
    for old, modern in PROFESSIONAL_REPLACEMENTS.items():
        cleaned = cleaned.replace(old, modern)
    return cleaned

print(polish_email_draft("Sorry for the delay, please send the report as soon as possible."))"""
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Readability Score Estimator",
            description="Write a function `calculate_average_sentence_length(text)` that returns the average number of words per sentence rounded to 1 decimal place.",
            starter_code="""def calculate_average_sentence_length(text: str) -> float:
    # Your code here
    pass""",
            solution_code="""def calculate_average_sentence_length(text: str) -> float:
    sentences = [s.strip() for s in text.split('.') if s.strip()]
    if not sentences:
        return 0.0
    total_words = sum(len(s.split()) for s in sentences)
    return round(total_words / len(sentences), 1)""",
            expected_output="8.5"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What does the BLUF acronym stand for in professional communication?",
                options=[
                    "Bottom Line Up Front",
                    "Basic Language Under Format",
                    "Business Logistics Utility Factor",
                    "Better Listening Using Feedback"
                ],
                correct_answer="Bottom Line Up Front",
                explanation="BLUF means putting the essential conclusion or request at the very beginning of the message."
            ),
            QuizQuestionBlueprint(
                question="Which subject line is most effective for executive correspondence?",
                options=[
                    "[ACTION REQUIRED] Contract approval by Friday 5 PM",
                    "Hey quick question about that thing",
                    "Important updates you should read whenever you get a second",
                    "FYI details attached here"
                ],
                correct_answer="[ACTION REQUIRED] Contract approval by Friday 5 PM",
                explanation="It specifies the exact action needed, the topic, and the hard deadline with zero ambiguity."
            ),
            QuizQuestionBlueprint(
                question="What is a more collaborative professional alternative to 'Sorry for the delay'?",
                options=[
                    "Thank you for your patience",
                    "I was extremely busy with more important clients",
                    "You should have reminded me earlier",
                    "Per my previous messages"
                ],
                correct_answer="Thank you for your patience",
                explanation="'Thank you for your patience' focuses on gratitude toward the client rather than highlighting your own delay."
            ),
            QuizQuestionBlueprint(
                question="What is the recommended average sentence length for high-clarity business writing?",
                options=[
                    "15 to 20 words per sentence",
                    "60 to 80 words per sentence",
                    "1 to 3 words per sentence",
                    "No punctuation is required in emails"
                ],
                correct_answer="15 to 20 words per sentence",
                explanation="Sentences averaging 15 to 20 words maximize reading retention and minimize cognitive fatigue."
            ),
            QuizQuestionBlueprint(
                question="Every effective business email should conclude with:",
                options=[
                    "A clear and unambiguous Call to Action (CTA) or next step",
                    "A lengthy legal disclaimer exceeding three paragraphs",
                    "An apology for taking up the reader's time",
                    "A list of five unrelated links and personal social media profiles"
                ],
                correct_answer="A clear and unambiguous Call to Action (CTA) or next step",
                explanation="A definitive CTA tells the recipient exactly who is responsible for the next step and when it is expected."
            )
        ]
    )
]

LANGUAGE_MASTERY_COURSE_BLUEPRINT = CourseBlueprint(
    title="Professional English & Global Communication",
    category="Language",
    description=(
        "Master the art of clear, persuasive, and globally competitive English. "
        "Learn natural conversational fluency, executive email writing, assertive business negotiation, "
        "and presentation delivery designed for multinational teams and remote environments."
    ),
    color="#F59E0B",
    days=DAYS
)
