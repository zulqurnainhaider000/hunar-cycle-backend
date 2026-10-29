"""
Freelancing, Remote Client Acquisition & Agency Scaling Blueprint
Comprehensive curriculum covering winning proposals, client psychology, pricing strategies,
contracts and escrow, scope management, and high-ticket client acquisition.
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
        title="Day 1: The High-Converting Freelance Proposal Framework",
        concept="Clients don't hire skills; they hire solutions that save time, reduce risk, and generate revenue.",
        analogy="Imagine having a burst pipe flooding your basement at 2 AM. You call a plumber. If they spend 20 minutes reciting where they went to high school and listing their favorite wrenches, you hang up. You hire the plumber who says: 'I know how to shut off the main valve, and I can be at your door in 15 minutes.' Your proposal must be the 15-minute emergency plumber.",
        theory_sections=[
            {
                "heading": "The 4-Part Winning Proposal Structure",
                "body": "Part 1 (The Hook): Acknowledge their specific problem in the first 2 lines without generic greetings. Part 2 (The Diagnosis): Demonstrate why the problem exists. Part 3 (The Action Plan): Outline a concise 3-step execution timeline. Part 4 (The Low-Friction Call-to-Action): Ask a direct, low-commitment question."
            },
            {
                "heading": "Avoiding the 'Me-Monster' Trap",
                "body": "Never start a proposal with 'I am an experienced developer with 5 years of experience...'. Over 90% of applicants do this and get immediately archived. Flip the lens from 'Me' to 'You': 'Your app needs faster load times to prevent bounce rates; here is how we fix it.'"
            }
        ],
        code_snippets=[
            {
                "title": "Proposal Quality Scorer (Python)",
                "explanation": "Scans proposal drafts to penalize self-absorbed phrasing and reward client-centric focus.",
                "language": "python",
                "code": """def score_freelance_proposal(proposal: str) -> dict:
    words = proposal.lower().split()
    i_count = sum(words.count(w) for w in ['i', "i'm", 'my', 'me'])
    you_count = sum(words.count(w) for w in ['you', "you're", 'your'])
    
    ratio = round(you_count / i_count, 2) if i_count > 0 else 5.0
    grade = 'Top Rated' if ratio >= 1.5 else 'Needs Work (Focus on the Client)'
    return {'i_mentions': i_count, 'you_mentions': you_count, 'client_focus_ratio': ratio, 'verdict': grade}

draft = "I can build your project. My skills include Python and I have worked with many companies."
print("Proposal Audit:", score_freelance_proposal(draft))"""
            },
            {
                "title": "Value-Based Pricing Calculator",
                "explanation": "Calculates project fees based on expected business impact rather than arbitrary hourly rates.",
                "language": "python",
                "code": """def calculate_value_based_fee(client_annual_gain: float, capture_pct: float = 10.0) -> float:
    # Capturing 10% of the value created for the client
    return round(client_annual_gain * (capture_pct / 100.0), 2)

# If a redesigned checkout flow makes the client $200,000 extra per year:
fee = calculate_value_based_fee(200000.0, capture_pct=10.0)
print(f"Value-Based Project Fee: ${fee:,.2f}")"""
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Effective Hourly Rate Calculator",
            description="Write a function `effective_hourly_rate(fixed_project_fee, total_hours_worked)` that computes the realized hourly rate rounded to 2 decimal places.",
            starter_code="""def effective_hourly_rate(fixed_project_fee: float, total_hours_worked: float) -> float:
    # Your code here
    pass""",
            solution_code="""def effective_hourly_rate(fixed_project_fee: float, total_hours_worked: float) -> float:
    if total_hours_worked <= 0:
        return 0.0
    return round(fixed_project_fee / total_hours_worked, 2)""",
            expected_output="125.0"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Why is starting a proposal with 'I am an expert with 5 years experience' ineffective?",
                options=[
                    "It focuses on the freelancer rather than addressing the client's urgent problem",
                    "It is against the terms of service of freelance platforms",
                    "It guarantees that the client will demand a 50% discount",
                    "It causes the proposal to be marked as spam by automated algorithms"
                ],
                correct_answer="It focuses on the freelancer rather than addressing the client's urgent problem",
                explanation="Clients care about their own problems and outcomes; proposals should lead with the client's goals."
            ),
            QuizQuestionBlueprint(
                question="What is 'Value-Based Pricing' in freelance consulting?",
                options=[
                    "Pricing your services based on the financial ROI created for the client rather than billable hours",
                    "Discounting your hourly rate to the lowest possible bid to win the auction",
                    "Billing exactly $10 per hour for all work regardless of difficulty",
                    "Charging clients exclusively in gift cards"
                ],
                correct_answer="Pricing your services based on the financial ROI created for the client rather than billable hours",
                explanation="Value-based pricing aligns your compensation with the business value generated for the client."
            ),
            QuizQuestionBlueprint(
                question="What is the recommended client-centric ratio of 'You/Your' vs 'I/Me' in high-converting proposals?",
                options=[
                    "At least 1.5 to 2 times more 'You' mentions than 'I'",
                    "Zero 'You' mentions and 100% 'I' mentions",
                    "Exactly 1:1 parity at all times",
                    "It makes no difference in conversion rates"
                ],
                correct_answer="At least 1.5 to 2 times more 'You' mentions than 'I'",
                explanation="Highlighting the client's situation (You/Your) twice as much as yourself establishes instant rapport."
            ),
            QuizQuestionBlueprint(
                question="What is the most effective Call to Action (CTA) at the end of a proposal?",
                options=[
                    "A low-friction, specific question (e.g., 'Are you free for a brief 10-minute discovery call this Thursday?')",
                    "Demanding an upfront payment of $10,000 before answering any questions",
                    "Ending with no question and waiting for the client to guess what to do next",
                    "Providing links to 20 different social media profiles"
                ],
                correct_answer="A low-friction, specific question (e.g., 'Are you free for a brief 10-minute discovery call this Thursday?')",
                explanation="A low-friction CTA makes replying effortless and removes decision paralysis."
            ),
            QuizQuestionBlueprint(
                question="In freelance project agreements, what does 'Scope Creep' mean?",
                options=[
                    "Uncontrolled expansion of project deliverables beyond the original agreed contract without additional compensation",
                    "A software bug that creeps into the codebase over time",
                    "A client who sends emails late in the evening",
                    "When a project finishes ahead of schedule"
                ],
                correct_answer="Uncontrolled expansion of project deliverables beyond the original agreed contract without additional compensation",
                explanation="Scope creep happens when new features are added without increasing the budget or adjusting the deadline."
            )
        ]
    ),
    DayBlueprint(
        order=2,
        title="Day 2: Contracts, Milestone Escrow & Managing Client Expectations",
        concept="Clear milestone escrow contracts protect both your cash flow and your professional relationship.",
        analogy="Think of a freelance milestone agreement like a staircase. You don't jump to the top floor in one giant leap hoping someone catches you. You take one step, confirm it is solid (escrow funded), complete the step (client approval), get paid, and take the next step.",
        theory_sections=[
            {
                "heading": "The Golden Rule of Freelancing: Never Work Without Escrow",
                "body": "Before writing a single line of code or designing a single wireframe, verify that the active milestone is funded in escrow. Working on promises leads to delayed payments and non-payment disputes."
            },
            {
                "heading": "Handling Scope Expansion Diplomatically",
                "body": "Never respond to extra client requests with an aggressive 'No'. Use the consultative approach: 'I'd love to build that feature! Since it's outside our initial milestone, let's finish Phase 1 first and create a Phase 2 milestone for $500 to add it next week.'"
            }
        ],
        code_snippets=[
            {
                "title": "Milestone Escrow Scheduler (Python)",
                "explanation": "Generates a balanced 3-phase milestone disbursement structure.",
                "language": "python",
                "code": """def generate_milestones(total_budget: float) -> list:
    return [
        {'phase': '1. Discovery & Wireframes', 'pct': 25, 'amount': total_budget * 0.25, 'status': 'Funded First'},
        {'phase': '2. Core Implementation', 'pct': 50, 'amount': total_budget * 0.50, 'status': 'Funded on Phase 1 Completion'},
        {'phase': '3. Testing & Final Handoff', 'pct': 25, 'amount': total_budget * 0.25, 'status': 'Funded on Phase 2 Completion'}
    ]

print("Milestone Schedule ($4,000 project):")
for m in generate_milestones(4000.0):
    print(f"  • {m['phase']}: ${m['amount']:,.2f} ({m['status']})")"""
            },
            {
                "title": "Revision Limit Verifier",
                "explanation": "Tracks contractually allowed revisions to prevent uncompensated rework.",
                "language": "python",
                "code": """def check_revision_status(completed_rounds: int, contract_limit: int = 2) -> dict:
    remaining = contract_limit - completed_rounds
    return {
        'completed': completed_rounds,
        'remaining_included': max(0, remaining),
        'requires_extra_billing': completed_rounds >= contract_limit
    }

print("Round 2 status:", check_revision_status(2, contract_limit=2))"""
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Escrow Platform Fee Deductor",
            description="Write a function `calculate_net_payout(gross_amount, platform_fee_pct=10.0)` that returns the net payout after deducting the platform fee, rounded to 2 decimal places.",
            starter_code="""def calculate_net_payout(gross_amount: float, platform_fee_pct: float = 10.0) -> float:
    # Your code here
    pass""",
            solution_code="""def calculate_net_payout(gross_amount: float, platform_fee_pct: float = 10.0) -> float:
    net = gross_amount * (1.0 - (platform_fee_pct / 100.0))
    return round(net, 2)""",
            expected_output="900.0"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Why is funded escrow mandatory before starting project work?",
                options=[
                    "It guarantees the client has committed funds and ensures payment upon approved delivery",
                    "It automatically registers your freelance business with the IRS",
                    "It allows you to bypass client revisions entirely",
                    "It prevents the client from reviewing your deliverables"
                ],
                correct_answer="It guarantees the client has committed funds and ensures payment upon approved delivery",
                explanation="Escrow secures funds with a neutral third party, protecting the freelancer against non-payment."
            ),
            QuizQuestionBlueprint(
                question="How should a freelancer professionally handle a client requesting additional features not in the contract?",
                options=[
                    "Welcome the addition and provide a separate milestone quote with additional budget and timeline",
                    "Refuse to answer the client's messages for three days",
                    "Work 40 hours overtime for free without mentioning it",
                    "Cancel the contract immediately and demand full payment"
                ],
                correct_answer="Welcome the addition and provide a separate milestone quote with additional budget and timeline",
                explanation="Positioning extra requests as an exciting Phase 2 milestone preserves the relationship while ensuring you are paid."
            ),
            QuizQuestionBlueprint(
                question="What is the purpose of specifying a 'revision limit' in a freelance agreement?",
                options=[
                    "Prevents endless subjective iterations and sets clear expectations for feedback rounds",
                    "Stops the client from downloading the final project files",
                    "Eliminates all communication between client and contractor",
                    "Allows the freelancer to deliver low quality work"
                ],
                correct_answer="Prevents endless subjective iterations and sets clear expectations for feedback rounds",
                explanation="Setting 2-3 structured revision rounds forces clients to consolidate feedback instead of dribbling endless changes."
            ),
            QuizQuestionBlueprint(
                question="What should be included in every project deliverable handoff?",
                options=[
                    "Clean organized source files, documentation, and a brief walkthrough video",
                    "Only raw code without any instructions or passwords",
                    "An invoice for unexpected unapproved charges",
                    "A link to an expired temporary file sharing service"
                ],
                correct_answer="Clean organized source files, documentation, and a brief walkthrough video",
                explanation="Providing clear documentation and a short video walkthrough leaves a 5-star impression and generates repeat referrals."
            ),
            QuizQuestionBlueprint(
                question="What is the single most valuable source of high-paying freelance clients?",
                options=[
                    "Repeat business and direct referrals from satisfied previous clients",
                    "Sending 1,000 generic copy-pasted messages to random LinkedIn users",
                    "Bidding $5 on public entry-level job posts",
                    "Purchasing outdated email contact lists online"
                ],
                correct_answer="Repeat business and direct referrals from satisfied previous clients",
                explanation="Satisfied clients have zero acquisition cost, high trust, and refer peers with similar budgets."
            )
        ]
    )
]

FREELANCING_MASTERY_COURSE_BLUEPRINT = CourseBlueprint(
    title="Freelancing Mastery & Remote Client Acquisition",
    category="Freelancing & Remote Work",
    description=(
        "The complete roadmap to earning a full-time income as a high-ticket freelancer or agency owner. "
        "Master high-converting proposal frameworks, value-based pricing, milestone escrow contracts, "
        "client communication psychology, and systematic referral acquisition."
    ),
    color="#10B981",
    days=DAYS
)
