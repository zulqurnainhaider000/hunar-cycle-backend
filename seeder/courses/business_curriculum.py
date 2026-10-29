"""
Business & Marketing Curriculums
Contains:
1. Modern Business Fundamentals & Strategy (15 Days)
2. Digital Marketing, Sales Funnels & Growth Hacking (15 Days)
"""

from seeder.curriculum_builder import make_day, make_course

# =========================================================================
# COURSE 1: Modern Business Fundamentals & Strategy (15 Days)
# =========================================================================
BUSINESS_DAYS = []

biz_titles = {
    1: ("Value Creation Engine & Identifying Market Friction", "Every profitable business solves an urgent, expensive problem for a clearly defined audience.", "A water filtration station in a desert town; if water is abundant, nobody pays, but if the well is muddy, clean water provides indispensable value."),
    2: ("The Business Model Canvas & Value Propositions", "Map the 9 building blocks that transform resources into profitable customer value.", "A blueprint for a skyscraper; you must understand the foundation, elevator shafts, and wiring before pouring concrete."),
    3: ("Customer Acquisition Cost (CAC) & Lifetime Value (LTV)", "Unit economics dictate scalability; LTV must be at least 3x greater than CAC.", "A vending machine where you insert $1 and receive $3 every time; as long as the machine works, you feed it coins all day."),
    4: ("Unit Economics & Gross Margin Optimization", "Gross margin determines how much cash remains to fund operating expenses and growth.", "The net height of a ship's hull above the waterline; higher margins give you buffer to survive stormy economic waters."),
    5: ("Break-Even Volume Analysis & Overhead Cost Structures", "Break-even is the milestone where total revenues equal fixed and variable costs.", "Reaching orbital velocity; once a rocket escapes Earth's gravity, it no longer needs maximum fuel burn to stay in orbit."),
    6: ("Working Capital, Cash Flow Runway & Burn Rate", "Cash is oxygen; companies don't go out of business from lack of profit, they die from lack of cash.", "A scuba diver monitoring oxygen tanks; when the tank hits zero, you drown, regardless of how much treasure you found on the seafloor."),
    7: ("Competitive Moats: Network Effects, Switching Costs & Brand", "Sustainable competitive advantages protect high profits from encroaching rivals.", "A medieval castle surrounded by a deep, shark-filled water moat; competitors cannot easily cross the threshold."),
    8: ("Porter's Five Forces & Industry Attractiveness", "Industry structure dictates long-term profitability more than company effort alone.", "Sailing with the wind at your back in a high-tide channel versus rowing against a hurricane in a swamp."),
    9: ("Price Elasticity of Demand & Value-Based Pricing Models", "Pricing power is the ultimate litmus test of product desirability and brand moats.", "Apple raising iPhone prices by $100 and seeing sales increase, because customers value the ecosystem over pure commodity cost."),
    10: ("Key Performance Indicators (KPIs) & OKR Frameworks", "Align teams behind measurable Objectives and Key Results that move the needle.", "A pilot's cockpit dashboard showing altitude, airspeed, and fuel instead of looking out the window and guessing."),
    11: ("Talent Density, Hiring & High-Performance Culture", "A small team of A-players outperforms a massive bureaucracy of average performers.", "A special forces squad executing a surgical night mission compared to a thousand uncoordinated recruits."),
    12: ("Supply Chain Management & Strategic Vendor Negotiations", "Resilient supply chains balance just-in-time efficiency with redundancy buffers.", "A bridge supported by multiple redundant suspension cables; if one snaps during a storm, the bridge remains standing."),
    13: ("Corporate Financial Statements: P&L, Balance Sheet & Cash Flow", "Financial statements are the scoreboard of business; mastering them allows objective auditing.", "The medical vital signs chart of a patient: pulse, blood pressure, and oxygen saturation tell the physician the true story."),
    14: ("Enterprise Risk Management & Scenario Planning", "Identify low-probability, high-impact black swan events before they strike.", "Carrying fire insurance and installing sprinkler systems before the building is even constructed."),
    15: ("Capstone: Constructing a 3-Year Strategic Business Plan", "Synthesize operations, financials, marketing, and leadership into an investor-ready plan.", "You have evolved from an employee into a visionary, quantitative business executive.")
}

for day_num in range(1, 16):
    t_info = biz_titles.get(day_num, (f"Day {day_num}: Business Leadership", "Execute strategic operations.", "Systematic leadership."))
    BUSINESS_DAYS.append(make_day(
        order=day_num,
        title=f"Day {day_num}: {t_info[0]}",
        concept=t_info[1],
        analogy=t_info[2],
        sections=[
            (f"Executive Analysis of {t_info[0]}", f"Mastering {t_info[0]} allows founders and executives to make capital allocation decisions with mathematical confidence and strategic foresight."),
            ("Operational Implementation & Performance Metrics", "Deploy frameworks to streamline workflow, eliminate operational waste, and maximize return on invested capital (ROIC).")
        ],
        snippets=[
            (f"{t_info[0]} Financial Modeling (Python)", f"""def calculate_business_kpi_{day_num}(revenue: float, costs: float) -> dict:
    operating_profit = round(revenue - costs, 2)
    margin_pct = round((operating_profit / revenue) * 100, 1) if revenue > 0 else 0.0
    return {{'day': {day_num}, 'operating_profit': operating_profit, 'margin_pct': margin_pct}}

print(calculate_business_kpi_{day_num}(50000.0, 32000.0))""", "python"),
            ("Burn Rate & Runway Calculator", f"""def calculate_cash_runway(current_cash: float, monthly_burn: float) -> float:
    return round(current_cash / monthly_burn, 1) if monthly_burn > 0 else 999.0

print("Cash Runway:", calculate_cash_runway(250000.0, 18000.0), "months")""", "python")
        ],
        challenge=(f"Business Metrics Challenge Day {day_num}", "Write a function `calculate_net_profit_margin(revenue, net_income)` that returns the net margin percentage rounded to 1 decimal place.",
                   "def calculate_net_profit_margin(revenue: float, net_income: float) -> float:\n    pass",
                   "def calculate_net_profit_margin(revenue: float, net_income: float) -> float:\n    if revenue <= 0: return 0.0\n    return round((net_income / revenue) * 100, 1)", "22.5"),
        quizzes=[
            (f"What is the strategic objective of {t_info[0]}?", [f"To leverage {t_info[0]} to drive sustainable profit, moat protection, and customer value", "To spend all company cash immediately", "To avoid filing corporate financial statements", "To fire all sales representatives"], f"To leverage {t_info[0]} to drive sustainable profit, moat protection, and customer value", f"Day {day_num} focuses on {t_info[0]}."),
            ("Why is maintaining a 3:1 LTV-to-CAC ratio critical for growth?", ["It guarantees customer gross profits exceed acquisition expenses by 3x, funding operations", "It eliminates all advertising competition", "It reduces employee income taxes to zero", "It makes all inventory free of charge"], "It guarantees customer gross profits exceed acquisition expenses by 3x, funding operations", "A 3:1 ratio leaves ample margin for product development, support, and healthy profit."),
            ("What is the difference between cash flow and accounting profit?", ["Profit counts revenue when earned; cash flow tracks actual physical cash entering and leaving the bank", "There is zero difference", "Cash flow only applies to non-profit charities", "Accounting profit is measured in gold bars"], "Profit counts revenue when earned; cash flow tracks actual physical cash entering and leaving the bank", "A profitable company can go bankrupt if cash is tied up in unpaid invoices while bills come due."),
            ("What creates a powerful 'Network Effect' moat?", ["The product becomes more valuable to existing users as each new user joins (e.g. marketplaces)", "Spending $1 million on newspaper billboards", "Registering a dot-com domain name", "Having the lowest prices in town"], "The product becomes more valuable to existing users as each new user joins (e.g. marketplaces)", "Network effects make it virtually impossible for new entrants to displace incumbents."),
            ("What is the primary purpose of an OKR framework?", ["Aligning the entire company around measurable, ambitious objectives with tracked key results", "Replacing all software with paper notebooks", "Assigning blame when projects miss deadlines", "Tracking daily employee bathroom breaks"], "Aligning the entire company around measurable, ambitious objectives with tracked key results", "OKRs connect high-level strategy with daily execution across all departments.")
        ]
    ))

BUSINESS_STRATEGY_BLUEPRINT = make_course(
    title="Modern Business Fundamentals & Strategy",
    category="Business",
    description=(
        "The complete 15-Day MBA-grade masterclass on business architecture, unit economics, and strategic scaling. "
        "Master the Value Creation Engine, LTV/CAC ratios, break-even mechanics, Porter's Five Forces, "
        "competitive moats, P&L financial statements, and OKR organizational execution."
    ),
    color="#0EA5E9",
    days=BUSINESS_DAYS
)


# =========================================================================
# COURSE 2: Digital Marketing, Sales Funnels & Growth Hacking (15 Days)
# =========================================================================
MARKETING_DAYS = []

mkt_titles = {
    1: ("The Modern Marketing Funnel: AIDA & The Flywheel", "Marketing moves prospects through Awareness, Interest, Desire, and Action into loyal brand promoters.", "A funnel filters river water; you catch thousands of liters at the top, filter out sediment, and collect pure crystal-clear drinking water at the spout."),
    2: ("Customer Personas & Identifying The Core Pain Point", "Targeting everyone targets no one; define your Ideal Customer Profile (ICP) down to their deepest anxieties.", "A sniper rifle with a calibrated scope hitting a bullseye at 1,000 yards versus blindfolding yourself and firing a shotgun in a forest."),
    3: ("Organic Content Strategy: The Hub-and-Spoke SEO Model", "Anchor broad topics with pillar pages and capture long-tail search traffic with supporting articles.", "The hub of a bicycle wheel connecting dozens of strong metal spokes; all search traffic flows into the central core asset."),
    4: ("High-Converting Landing Page Architecture & Copywriting", "Landing pages have a single conversion goal; remove all distractions and write benefits over features.", "A one-way street with no side turns; the driver has only one clear, brightly lit destination ahead."),
    5: ("Paid Advertising: Meta Ads vs Google Search Intent", "Google captures existing high-intent demand; Meta interrupts passive users with irresistible creative hooks.", "Google is a customer walking into a hardware store asking for a wrench; Meta is an inventor demoing an amazing gadget at a mall kiosk."),
    6: ("Lead Magnets & High-Value Content Upgrades", "Offer an indispensable quick-win resource in exchange for an email address.", "A sample of freshly baked bread at the bakery door; once you taste the quality, you gladly buy the whole loaf."),
    7: ("Email Marketing Automation: The 5-Day Welcome Sequence", "Nurture new subscribers into paying clients on autopilot using behavioral triggers.", "A friendly, expert tour guide showing visitors around a museum, answering questions and pointing out masterpieces."),
    8: ("A/B Split Testing & Conversion Rate Optimization (CRO)", "Never guess what converts; run scientific tests changing single variables to double revenue.", "A chemist running controlled experiments in test tubes; keeping temperature constant while testing which catalyst produces the crystal."),
    9: ("Social Proof Architecture: Case Studies & Video Reviews", "Prospects don't believe what you say about yourself; they believe what previous customers say.", "Walking down a street with two restaurants: one is empty, the other has a line around the block; you naturally join the line."),
    10: ("Influencer Partnerships & High-Leverage Affiliates", "Borrow trust from established creators to access pre-built, highly engaged audiences.", "Having the most popular student in school introduce you to everyone at the party on your first day."),
    11: ("Referral Loops & The Viral Growth Coefficient (K-Factor)", "Design built-in product mechanics where using the product naturally invites new users.", "Sending a Dropbox invite because you need more shared folder space, or PayPal giving $10 for inviting friends."),
    12: ("Customer Onboarding & Minimizing Time-to-Value (TTV)", "The fastest way to eliminate churn is getting users to their first 'Aha!' moment in under 5 minutes.", "Unboxing an Apple iPhone; the battery is pre-charged, the screen lights up instantly, and setup takes 30 seconds."),
    13: ("Marketing Analytics, UTM Tracking & Attribution Models", "Measure exactly which marketing channels and ad campaigns generate profitable revenue.", "A cash register that records not just the sale, but exactly which street sign and advertisement the customer saw before walking in."),
    14: ("Account-Based Marketing (ABM) for High-Ticket B2B", "Treat each target enterprise corporate account as a personalized market of one.", "A diplomatic envoy crafting a custom treaty for a specific kingdom rather than dropping leaflets over an ocean."),
    15: ("Capstone: Launching an Omnichannel Growth Funnel", "Integrate organic content, paid acquisition, email nurture, and referral loops into a growth engine.", "You are a master growth architect capable of scaling digital brands to millions in revenue.")
}

for day_num in range(1, 16):
    t_info = mkt_titles.get(day_num, (f"Day {day_num}: Growth Optimization", "Drive customer acquisition.", "Scale growth loops."))
    MARKETING_DAYS.append(make_day(
        order=day_num,
        title=f"Day {day_num}: {t_info[0]}",
        concept=t_info[1],
        analogy=t_info[2],
        sections=[
            (f"Growth Architecture of {t_info[0]}", f"Mastering {t_info[0]} gives companies a sustainable customer acquisition engine that compounds over time without burning capital on wasteful ads."),
            ("Conversion Optimization & Real-World Testing", "Analyze user drop-off points in the funnel, implement heatmaps, and optimize copy to maximize return on ad spend (ROAS).")
        ],
        snippets=[
            (f"{t_info[0]} Funnel Metrics (Python)", f"""def calculate_funnel_conversion_{day_num}(visitors: int, leads: int, sales: int) -> dict:
    lead_cvr = round((leads / visitors) * 100, 2) if visitors > 0 else 0.0
    sales_cvr = round((sales / leads) * 100, 2) if leads > 0 else 0.0
    return {{'day': {day_num}, 'lead_cvr': lead_cvr, 'sales_cvr': sales_cvr}}

print(calculate_funnel_conversion_{day_num}(10000, 850, 95))""", "python"),
            ("ROAS (Return on Ad Spend) Calculator", f"""def calculate_roas(revenue: float, ad_spend: float) -> float:
    return round(revenue / ad_spend, 2) if ad_spend > 0 else 0.0

print("Campaign ROAS ($25k rev on $5k ad spend):", calculate_roas(25000.0, 5000.0), "x")""", "python")
        ],
        challenge=(f"Marketing Challenge Day {day_num}", "Write a function `calculate_cpa(total_ad_spend, new_customers)` that returns Cost Per Acquisition (CPA) rounded to 2 decimal places.",
                   "def calculate_cpa(total_ad_spend: float, new_customers: int) -> float:\n    pass",
                   "def calculate_cpa(total_ad_spend: float, new_customers: int) -> float:\n    if new_customers <= 0: return 0.0\n    return round(total_ad_spend / new_customers, 2)", "45.5"),
        quizzes=[
            (f"What is the core function of {t_info[0]}?", [f"To leverage {t_info[0]} to drive scalable, high-converting customer acquisition and retention", "To post random memes on corporate social accounts", "To send unsolicited spam to random phone numbers", "To eliminate the website's checkout page"], f"To leverage {t_info[0]} to drive scalable, high-converting customer acquisition and retention", f"Day {day_num} focuses on {t_info[0]}."),
            ("What does ROAS stand for in paid media advertising?", ["Return on Ad Spend (Total Revenue generated divided by Ad Spend)", "Rate of Annual Sales", "Registered Online Affiliate Service", "Real Operating Asset Savings"], "Return on Ad Spend (Total Revenue generated divided by Ad Spend)", "ROAS measures the gross revenue generated for every dollar invested in advertising."),
            ("Why is focusing on benefits rather than features essential in copywriting?", ["Customers buy the positive emotional and financial outcome for themselves, not technical specs", "Features take up too many pixels on the screen", "Benefits are protected by federal trademark law", "Writing features is banned by ad platforms"], "Customers buy the positive emotional and financial outcome for themselves, not technical specs", "People buy the hole in the wall, not the drill bit; benefits communicate value."),
            ("What does an A/B split test require to be statistically valid?", ["Testing one single variable at a time on identical traffic samples until statistical significance is reached", "Changing the entire layout, price, and logo simultaneously", "Asking your family members which design they prefer", "Running the test for exactly 3 minutes"], "Testing one single variable at a time on identical traffic samples until statistical significance is reached", "Isolating one variable (e.g. headline) proves which element caused the conversion difference."),
            ("What is the Viral Coefficient (K-Factor) in growth engineering?", ["The number of new users each existing user generates; K > 1 indicates exponential viral growth", "The speed at which computer viruses spread", "The number of likes on a YouTube video", "The bounce rate of mobile visitors"], "The number of new users each existing user generates; K > 1 indicates exponential viral growth", "When K > 1, each user brings in more than one replacement, resulting in compounding virality.")
        ]
    ))

DIGITAL_MARKETING_BLUEPRINT = make_course(
    title="Digital Marketing, Sales Funnels & Growth Hacking",
    category="Business",
    description=(
        "The comprehensive 15-Day guide to modern digital marketing and customer acquisition. "
        "Master the AIDA funnel, customer personas, hub-and-spoke SEO, high-converting landing pages, "
        "Meta and Google Ads (ROAS), email drip automation, A/B split testing, and viral referral loops."
    ),
    color="#0284C7",
    days=MARKETING_DAYS
)
