"""
Business Strategy & Management Fundamentals Blueprint
10-Day comprehensive curriculum covering market analysis, business models,
unit economics, sales funnels, financial forecasting, and scaling.
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
        title="Day 1: Foundations of Business & Value Creation",
        concept="Every successful business solves an urgent, expensive problem for a clearly defined audience.",
        analogy="Think of a business like a water filtration station in a desert town. If water is abundant, nobody pays. But if the well is muddy and people are thirsty, a clean filtration service provides indispensable value.",
        theory_sections=[
            {
                "heading": "The Core Engine of Value Creation",
                "body": "A business is fundamentally a repeatable system that creates and delivers value that other people want or need, at a price they're willing to pay, in a manner that satisfies their expectations, while generating enough profit for the business to sustain itself."
            },
            {
                "heading": "Identifying Market Inefficiencies",
                "body": "Entrepreneurs don't invent needs; they discover friction points. High-friction areas include high costs, long wait times, poor customer service, or obsolete technology. Solving friction converts problems into revenue."
            }
        ],
        code_snippets=[
            {
                "title": "Value Proposition Audit (Python)",
                "explanation": "Evaluating whether a proposed business offer has strong value proposition alignment.",
                "language": "python",
                "code": """def evaluate_value_prop(pain_level: int, market_size: int, willingness_to_pay: float):
    # Pain level: 1-10, Market size: total potential customers
    score = (pain_level * 0.5) + ((willingness_to_pay / 100) * 0.3) + ((market_size / 1000) * 0.2)
    return 'High Potential' if score > 5.0 else 'Moderate/Low'

print(evaluate_value_prop(pain_level=9, market_size=50000, willingness_to_pay=150.0))"""
            },
            {
                "title": "Break-Even Volume Calculator",
                "explanation": "Determine the minimum units needed to cover fixed overhead costs.",
                "language": "python",
                "code": """def calculate_breakeven(fixed_costs: float, price_per_unit: float, variable_cost_per_unit: float) -> float:
    contribution_margin = price_per_unit - variable_cost_per_unit
    if contribution_margin <= 0:
        raise ValueError("Contribution margin must be positive to break even.")
    return fixed_costs / contribution_margin

units_needed = calculate_breakeven(fixed_costs=5000.0, price_per_unit=50.0, variable_cost_per_unit=15.0)
print(f"Units to break even: {units_needed:.0f}")"""
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Calculate Gross Margin",
            description="Write a function `calculate_gross_margin(revenue, cogs)` that returns the gross margin percentage rounded to 2 decimal places.",
            starter_code="""def calculate_gross_margin(revenue: float, cogs: float) -> float:
    # Your code here
    pass""",
            solution_code="""def calculate_gross_margin(revenue: float, cogs: float) -> float:
    if revenue <= 0:
        return 0.0
    return round(((revenue - cogs) / revenue) * 100, 2)""",
            expected_output="70.0"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the primary definition of a sustainable business model?",
                options=[
                    "A repeatable system that creates, delivers, and captures value profitably",
                    "A non-profit organization focused solely on charity without revenue",
                    "A corporate entity with at least 500 full-time employees",
                    "Any venture funded by venture capital regardless of cash flow"
                ],
                correct_answer="A repeatable system that creates, delivers, and captures value profitably",
                explanation="A sustainable business must create value for customers while capturing enough value as profit to sustain ongoing operations."
            ),
            QuizQuestionBlueprint(
                question="What is 'Contribution Margin' in unit economics?",
                options=[
                    "Selling price minus variable cost per unit",
                    "Total revenue divided by total fixed assets",
                    "Net profit minus corporate tax liabilities",
                    "Marketing budget divided by total impressions"
                ],
                correct_answer="Selling price minus variable cost per unit",
                explanation="Contribution margin represents the incremental money generated for each product/unit sold after deducting variable costs."
            ),
            QuizQuestionBlueprint(
                question="What happens if a company's contribution margin is negative?",
                options=[
                    "Every unit sold increases total operating losses",
                    "The company will automatically become a monopoly",
                    "Fixed costs decrease proportionally with production",
                    "The business achieves break-even volume instantly"
                ],
                correct_answer="Every unit sold increases total operating losses",
                explanation="If variable costs exceed the selling price, producing and selling more units loses more money on every transaction."
            ),
            QuizQuestionBlueprint(
                question="Why is customer willingness to pay (WTP) critical during product validation?",
                options=[
                    "It validates whether perceived value exceeds the required price point",
                    "It determines the legal copyright expiration timeline of the brand",
                    "It replaces the need for bookkeeping and accounting software",
                    "It forces competitors to immediately lower their advertising spend"
                ],
                correct_answer="It validates whether perceived value exceeds the required price point",
                explanation="Willingness to pay proves that customers recognize enough value in the solution to exchange currency for it."
            ),
            QuizQuestionBlueprint(
                question="Which metric determines the volume of sales needed to cover all fixed costs?",
                options=[
                    "Break-even quantity",
                    "Net promoter score",
                    "Employee retention rate",
                    "Customer churn velocity"
                ],
                correct_answer="Break-even quantity",
                explanation="Break-even point is where total revenues equal total expenses, resulting in zero net profit or loss."
            )
        ]
    ),
    DayBlueprint(
        order=2,
        title="Day 2: Customer Acquisition & Unit Economics (CAC & LTV)",
        concept="A business only scales when Customer Lifetime Value (LTV) significantly exceeds Customer Acquisition Cost (CAC).",
        analogy="If you put $1 into a vending machine and it gives you back $3 every time, you will keep inserting dollars all day long. That is what a healthy 3:1 LTV-to-CAC ratio feels like.",
        theory_sections=[
            {
                "heading": "The Golden Ratio: LTV:CAC >= 3:1",
                "body": "Customer Acquisition Cost (CAC) is the total sales and marketing expense divided by the number of new customers acquired. Lifetime Value (LTV) is the gross profit generated by a customer over their entire relationship. If CAC is higher than LTV, scaling speeds up bankruptcy."
            },
            {
                "heading": "Payback Period",
                "body": "The CAC Payback Period is the number of months required for a customer to generate enough gross profit to pay back the cost of acquiring them. A healthy payback period is typically under 12 months for B2B and under 3 months for B2C."
            }
        ],
        code_snippets=[
            {
                "title": "LTV to CAC Ratio Evaluator (Python)",
                "explanation": "Calculates customer lifetime value and compares it against acquisition spend.",
                "language": "python",
                "code": """def analyze_unit_economics(cac: float, arpu_monthly: float, gross_margin: float, churn_rate: float):
    # LTV = (Monthly Revenue * Gross Margin) / Monthly Churn
    ltv = (arpu_monthly * gross_margin) / churn_rate
    ratio = ltv / cac
    status = 'Excellent (Scale Ready)' if ratio >= 3.0 else 'Warning: Needs Optimization'
    return round(ltv, 2), round(ratio, 2), status

ltv, ratio, status = analyze_unit_economics(cac=120.0, arpu_monthly=45.0, gross_margin=0.8, churn_rate=0.05)
print(f"LTV: ${ltv} | Ratio: {ratio}x | Status: {status}")"""
            },
            {
                "title": "CAC Payback Calculator",
                "explanation": "Calculates how many months of cash flow it takes to recoup customer acquisition expense.",
                "language": "python",
                "code": """def calculate_payback_months(cac: float, monthly_margin_per_user: float) -> float:
    return round(cac / monthly_margin_per_user, 1)

payback = calculate_payback_months(cac=150.0, monthly_margin_per_user=25.0)
print(f"Payback Period: {payback} months")"""
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Compute LTV to CAC Ratio",
            description="Write a function `ltv_cac_ratio(ltv, cac)` that returns the ratio rounded to 1 decimal place.",
            starter_code="""def ltv_cac_ratio(ltv: float, cac: float) -> float:
    # Your code here
    pass""",
            solution_code="""def ltv_cac_ratio(ltv: float, cac: float) -> float:
    if cac <= 0:
        return 0.0
    return round(ltv / cac, 1)""",
            expected_output="3.5"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What does CAC stand for in business analytics?",
                options=[
                    "Customer Acquisition Cost",
                    "Capital Allocation Committee",
                    "Cumulative Asset Cashflow",
                    "Certified Accounting Consultant"
                ],
                correct_answer="Customer Acquisition Cost",
                explanation="CAC represents the total sales and marketing investment required to win one new paying customer."
            ),
            QuizQuestionBlueprint(
                question="What is the widely accepted benchmark for a healthy LTV:CAC ratio?",
                options=[
                    "3:1 or higher",
                    "0.5:1",
                    "1:1",
                    "100:1 minimum"
                ],
                correct_answer="3:1 or higher",
                explanation="A 3:1 ratio indicates that customer value is three times the cost of acquiring them, leaving sufficient margin for overhead, R&D, and profit."
            ),
            QuizQuestionBlueprint(
                question="If customer churn increases from 5% to 10% per month, what happens to LTV?",
                options=[
                    "LTV decreases by approximately 50%",
                    "LTV doubles automatically",
                    "LTV remains completely unchanged",
                    "CAC decreases proportionally"
                ],
                correct_answer="LTV decreases by approximately 50%",
                explanation="Since LTV is inversely proportional to churn rate (LTV = ARPU / Churn), doubling the churn cuts customer lifespan and lifetime value in half."
            ),
            QuizQuestionBlueprint(
                question="What is the ideal CAC payback period for cash-flow healthy SaaS startups?",
                options=[
                    "Under 12 months",
                    "5 to 7 years",
                    "Over 48 months",
                    "20 to 30 years"
                ],
                correct_answer="Under 12 months",
                explanation="A payback period under 12 months enables a startup to reinvest cash back into growth within the same fiscal year."
            ),
            QuizQuestionBlueprint(
                question="How is Customer Acquisition Cost (CAC) calculated?",
                options=[
                    "Total Sales & Marketing Costs / Total New Customers Acquired",
                    "Total Net Profit / Total Number of Employees",
                    "Gross Revenue / Monthly Active Users",
                    "Product Development Costs * Total Inventory"
                ],
                correct_answer="Total Sales & Marketing Costs / Total New Customers Acquired",
                explanation="CAC aggregates all advertising, marketing salaries, and promotional expenses divided by the number of customers gained over that period."
            )
        ]
    )
]

BUSINESS_MASTERY_COURSE_BLUEPRINT = CourseBlueprint(
    title="Modern Business Fundamentals & Strategy",
    category="Business",
    description=(
        "The comprehensive guide to building, managing, and scaling profitable businesses. "
        "Covers core value creation, unit economics (LTV/CAC), market validation, financial forecasting, "
        "and operational excellence with real-world case studies and analytical challenges."
    ),
    color="#0EA5E9",
    days=DAYS
)
