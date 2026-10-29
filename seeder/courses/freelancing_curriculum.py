"""
Freelancing & Remote Work Curriculums
Contains:
1. Upwork & Fiverr Client Acquisition Blueprint (15 Days)
2. High-Ticket Proposal Writing & Remote Agency Scaling (15 Days)
"""

from seeder.curriculum_builder import make_day, make_course

# =========================================================================
# COURSE 1: Upwork & Fiverr Client Acquisition Blueprint (15 Days)
# =========================================================================
UPWORK_FIVERR_DAYS = []

# Day 1
UPWORK_FIVERR_DAYS.append(make_day(
    order=1,
    title="Day 1: Profile Optimization & The 100% All-Star Checklist",
    concept="Your freelance profile is a landing page that must convert visiting clients within the first 10 seconds.",
    analogy="Think of your profile like a storefront in a busy shopping mall. If the display window is cluttered with random tools, shoppers walk past. If you display one stunning outfit with a clear price and testimonial, shoppers walk inside.",
    sections=[
        ("The Anatomy of a Converting Headline", "Never use generic titles like 'Virtual Assistant / Web Developer / Data Entry'. Instead, use the Niche-Result formula: '[Role] specializing in [Outcome] for [Target Client]'. For example: 'Shopify Speed Optimization Expert | Increasing Mobile Conversion Rates for DTC Brands'."),
        ("The Profile Overview Structure", "Open with the client's pain point in the first 2 lines. Follow with 3 bulleted core competencies, proof of results (metrics), and a clear invitation for a consultation call.")
    ],
    snippets=[
        ("Profile Headline Formatter (Python)", """def format_freelancer_headline(role: str, outcome: str, audience: str) -> str:
    return f"{role} specializing in {outcome} for {audience}"

headline = format_freelancer_headline(
    role="Full-Stack React Engineer",
    outcome="Rapid MVP Launches & Bug-Free Scaling",
    audience="Early-Stage SaaS Startups"
)
print("Optimized Headline:", headline)""", "python"),
        ("Profile Completeness Checker", """REQUIRED_FIELDS = ['photo', 'title', 'overview', 'skills', 'portfolio', 'rate', 'employment_history']

def check_profile_completeness(user_profile: dict) -> dict:
    missing = [f for f in REQUIRED_FIELDS if not user_profile.get(f)]
    pct = round(((len(REQUIRED_FIELDS) - len(missing)) / len(REQUIRED_FIELDS)) * 100)
    return {'completeness_pct': pct, 'is_all_star': pct == 100, 'missing': missing}

print(check_profile_completeness({'photo': True, 'title': 'Dev', 'overview': 'Text', 'skills': ['Python'], 'portfolio': True, 'rate': 65.0, 'employment_history': True}))""", "python")
    ],
    challenge=("Profile Score Calculator", "Write a function `calculate_profile_score(has_video, portfolio_items, has_certifications)` where video adds 20 points, each portfolio item adds 15 points (up to max 60), and certifications add 20 points.",
               """def calculate_profile_score(has_video: bool, portfolio_items: int, has_certifications: bool) -> int:
    # Your code here
    pass""",
               """def calculate_profile_score(has_video: bool, portfolio_items: int, has_certifications: bool) -> int:
    score = 0
    if has_video: score += 20
    score += min(60, portfolio_items * 15)
    if has_certifications: score += 20
    return score""", "100"),
    quizzes=[
        ("What is the primary objective of a freelance profile headline?", ["To state the specific business result you produce for a target niche", "To list every single hobby you have enjoyed since childhood", "To demand an upfront payment of $10,000", "To include as many unrelated keywords as possible"], "To state the specific business result you produce for a target niche", "Clear positioning attracts high-paying clients looking for specialists."),
        ("Why is a smiling professional profile photo critical for freelance conversion?", ["It builds trust and lowers perceived transaction risk for remote clients", "It is legally required to verify your passport", "It guarantees you will receive top search rankings immediately", "It replaces the need for submitting portfolio samples"], "It builds trust and lowers perceived transaction risk for remote clients", "A clear friendly photo signals accountability and professionalism."),
        ("What is the Niche-Result headline formula?", ["[Role] specializing in [Outcome] for [Audience]", "[Name] wanting to make money online fast", "Anything with at least 50 buzzwords", "A copy-paste of a famous celebrity resume"], "[Role] specializing in [Outcome] for [Audience]", "This formula immediately communicates who you help and what result you deliver."),
        ("Where should your strongest client testimonial or metric appear in your profile overview?", ["In the first 3 to 4 sentences above the 'Read More' fold", "At the very bottom of the page in fine print", "Hidden inside an encrypted zip file", "Nowhere, because testimonials look unprofessional"], "In the first 3 to 4 sentences above the 'Read More' fold", "Clients scan quickly; placing proof at the top grabs attention."),
        ("How many core skills should you highlight on a specialized profile?", ["3 to 5 deeply related competencies", "At least 50 completely unrelated skills", "Zero skills to keep clients curious", "Only soft skills like enthusiasm"], "3 to 5 deeply related competencies", "Focusing on 3-5 complementary skills positions you as an expert.")
    ]
))

# Days 2 to 15 for Upwork & Fiverr
day_data_course1 = [
    (2, "Day 2: Upwork Algorithm Mastery & JSS (Job Success Score)",
     "Upwork's search algorithm prioritizes freelancers with high JSS, consistent client satisfaction, and responsive messaging.",
     "Think of the Upwork algorithm like a ride-sharing driver rating. If drivers cancel trips or get 3-star reviews, the app stops dispatching prime airport passengers to them. Maintaining a 100% JSS keeps you at the top of the client search dispatch.",
     [("The Components of Job Success Score (JSS)", "JSS measures both public 5-star reviews and private client feedback. Private feedback has a 3x higher weighting on your score. A single contract with a 5-star public rating but a 'Would not recommend' private rating can drop your JSS by 5-10%."),
      ("Responsiveness & Profile Availability", "Freelancers who respond to client invitations within 2 hours receive an algorithmic boost in search placement. Setting your profile to 'Available Now' signals readiness to take on immediate billable work.")],
     [("JSS Drop Calculator (Python)", """def estimate_jss(positive_contracts: int, total_contracts: int) -> float:
    if total_contracts == 0: return 100.0
    return round((positive_contracts / total_contracts) * 100, 1)

print("JSS after 19 positive out of 20:", estimate_jss(19, 20), "%")""", "python"),
      ("Response Time Grader", """def grade_response_time(hours: float) -> str:
    if hours <= 1.0: return 'Elite (Algorithm Boost)'
    if hours <= 12.0: return 'Good (Standard)'
    return 'Poor (Search Penalty)'

print(grade_response_time(0.5))""", "python")],
     ("JSS Threshold Checker", "Write a function `is_top_rated_eligible(jss, earnings, weeks_active)` that returns True if JSS >= 90.0, earnings >= 1000.0, and weeks_active >= 13.",
      "def is_top_rated_eligible(jss: float, earnings: float, weeks_active: int) -> bool:\n    pass",
      "def is_top_rated_eligible(jss: float, earnings: float, weeks_active: int) -> bool:\n    return jss >= 90.0 and earnings >= 1000.0 and weeks_active >= 13", "True"),
     [("What carries the highest weight in determining your Upwork Job Success Score (JSS)?", ["Private client feedback submitted upon contract closure", "The number of hours you logged on social media", "The length of your profile overview in words", "Your country of residence"], "Private client feedback submitted upon contract closure", "Private feedback reflects honest client satisfaction and heavily influences JSS."),
      ("What JSS threshold is required to qualify for Upwork Top Rated status?", ["90% or higher for at least 13 of the last 16 weeks", "50% or higher", "10% or higher", "Upwork does not use percentages"], "90% or higher for at least 13 of the last 16 weeks", "Top Rated status requires sustained high satisfaction of 90%+ JSS."),
      ("Why is responding to client invitations within 24 hours vital?", ["It keeps your profile response score high and improves search ranking", "It prevents your account from being deleted permanently", "It automatically doubles your hourly rate", "It disables client fee deductions"], "It keeps your profile response score high and improves search ranking", "Responsive freelancers are prioritized in algorithmic search results."),
      ("What happens if you complete a job with 5-star public feedback but negative private feedback?", ["Your JSS will likely decrease despite the public stars", "Your JSS will automatically jump to 100%", "The client will be banned from Upwork", "Your earnings are refunded to the client"], "Your JSS will likely decrease despite the public stars", "Upwork's algorithm evaluates private feedback to detect authentic client satisfaction."),
      ("How often is the Upwork Job Success Score updated?", ["Every two weeks", "Every 5 minutes", "Once per year", "Only when requested by support"], "Every two weeks", "JSS calculates on a rolling 2-week schedule over 6-month, 1-year, and 2-year windows.")
     ]),

    (3, "Day 3: Specialized Profiles & Niche Positioning",
     "Generalists compete on price; specialists command premium rates by solving specific problems for specific audiences.",
     "If you have a rare heart condition, you don't go to a general family doctor; you pay $500 an hour to see a specialized cardiologist. Specialized profiles position you as that high-ticket surgeon.",
     [("The Power of Upwork's 2 Specialized Profiles", "Upwork allows 1 General profile plus 2 Specialized profiles. Each specialized profile has its own tailored portfolio, overview, work history, and custom hourly rate."),
      ("Niche Down to Scale Up", "Niching down feels counter-intuitive because you exclude people, but high-paying clients ignore generalists. An eCommerce store owner will always hire a 'Shopify Conversion Specialist' over a 'General Web Developer'.")],
     [("Profile Switcher Simulator (Python)", """def get_profile_context(niche: str) -> dict:
    profiles = {
        'mobile': {'title': 'React Native Developer', 'rate': 85.0},
        'backend': {'title': 'FastAPI & Postgres Architect', 'rate': 95.0}
    }
    return profiles.get(niche, {'title': 'Full-Stack Developer', 'rate': 70.0})

print("Targeted Mobile Context:", get_profile_context('mobile'))""", "python"),
      ("Hourly Rate Multiplier by Specialization", """def calculate_specialist_premium(general_rate: float, specialization_factor: float = 1.35) -> float:
    return round(general_rate * specialization_factor, 2)

print("Specialist Rate:", calculate_specialist_premium(50.0))""", "python")],
     ("Calculate Total Retainer", "Write a function `calculate_monthly_retainer(hours_per_week, hourly_rate)` that returns the 4-week monthly retainer amount.",
      "def calculate_monthly_retainer(hours_per_week: float, hourly_rate: float) -> float:\n    pass",
      "def calculate_monthly_retainer(hours_per_week: float, hourly_rate: float) -> float:\n    return hours_per_week * hourly_rate * 4.0", "3200.0"),
     [("How many specialized profiles can an Upwork freelancer create?", ["Up to 2 specialized profiles in addition to the general profile", "Unlimited profiles without restriction", "Zero, Upwork only allows one static page", "Exactly 50 profiles"], "Up to 2 specialized profiles in addition to the general profile", "Upwork provides 2 specialized profile slots to showcase distinct skill sets."),
      ("Why do specialists earn significantly higher hourly rates than generalists?", ["Clients perceive specialists as lower risk with higher domain expertise", "Specialists are required to pay higher platform fees", "Generalists are not allowed to submit proposals on projects over $100", "The algorithm forbids generalists from bidding"], "Clients perceive specialists as lower risk with higher domain expertise", "Clients pay premiums for specialists who have solved their exact problem many times."),
      ("What should be featured on a specialized profile?", ["Only portfolio pieces, testimonials, and copy relevant to that specific niche", "Your entire lifetime work history including non-related retail jobs", "Every programming language you have ever glanced at", "Stock photography of generic office desks"], "Only portfolio pieces, testimonials, and copy relevant to that specific niche", "Irrelevant work clutters the page and dilutes your specialist positioning."),
      ("What is the primary danger of staying a generalist on freelance marketplaces?", ["Competing in a race to the bottom on price against thousands of low-cost bidders", "Having too many clients to handle simultaneously", "Automatic suspension of your tax identification number", "Being forced to work on weekends"], "Competing in a race to the bottom on price against thousands of low-cost bidders", "Generalists get commoditized and forced to compete on the lowest bid."),
      ("Which title represents strong specialist positioning?", ["Shopify Checkout Optimization Specialist", "Hardworking Computer Guy", "Available to do any task", "Web & Mobile & Design & Translation Expert"], "Shopify Checkout Optimization Specialist", "It clearly targets a specific platform (Shopify) and a specific high-value outcome (Checkout Optimization).")
     ]),

    (4, "Day 4: High-Yield Search Operators & Job Feed Filtering",
     "Finding lucrative freelance jobs requires advanced boolean search filtering to eliminate low-budget noise.",
     "Panning for gold in a river is foolish if you shovel pure mud. You need a fine mesh sieve that lets the sand wash away and traps the nuggets. Boolean search operators are your gold sieve.",
     [("Boolean Search Syntax on Upwork", "Use quotes for exact matches (`\"React Native\"`), AND/OR for combinations, and NOT to filter out low-yield jobs: `(\"React Native\" OR \"Expo\") AND NOT (\"equity\" OR \"unpaid\" OR \"rev share\")`."),
      ("Filtering by Client History & Verification", "Only bid on jobs where: (1) Payment method is verified, (2) Client has spent > $1,000 previously, and (3) Client has a review rating above 4.5 stars. This filters out 90% of nightmare clients.")],
     [("Boolean Query Builder (Python)", """def build_upwork_query(primary_skills: list, excluded_terms: list) -> str:
    skills_part = " OR ".join(f'"{s}"' for s in primary_skills)
    exclude_part = " ".join(f'NOT "{t}"' for t in excluded_terms)
    return f"({skills_part}) {exclude_part}"

print(build_upwork_query(['React Native', 'Flutter'], ['equity', 'low budget', 'intern']))""", "python"),
      ("Job Post Risk Assessor", """def assess_job_risk(verified_payment: bool, client_spend: float, rating: float) -> str:
    if verified_payment and client_spend >= 1000 and rating >= 4.5:
        return 'Grade A (High Value Prospect)'
    if not verified_payment:
        return 'High Risk: Payment Unverified'
    return 'Moderate Risk: Review Carefully'

print(assess_job_risk(True, 5000.0, 4.9))""", "python")],
     ("Filter High Value Jobs", "Write a function `is_job_worthy(client_rating, client_spend, is_verified)` that returns True only if rating >= 4.7, spend >= 500, and is_verified is True.",
      "def is_job_worthy(client_rating: float, client_spend: float, is_verified: bool) -> bool:\n    pass",
      "def is_job_worthy(client_rating: float, client_spend: float, is_verified: bool) -> bool:\n    return client_rating >= 4.7 and client_spend >= 500.0 and is_verified", "True"),
     [("Why is client payment verification a non-negotiable filter?", ["It guarantees the client has a validated credit card or bank account on file", "It automatically deposits money into your PayPal account", "It eliminates all platform fees for that contract", "It forces the client to hire within 1 hour"], "It guarantees the client has a validated credit card or bank account on file", "Unverified clients often post tests or abandon posts without hiring."),
      ("What does the search operator `NOT` do in job queries?", ["Excludes job posts containing unwanted keywords like 'unpaid' or 'equity'", "Doubles the number of results returned", "Inverts the language of the job posting", "Sends an automated email to the client"], "Excludes job posts containing unwanted keywords like 'unpaid' or 'equity'", "NOT filters out low-budget and time-wasting posts."),
      ("What client metric indicates a willingness to pay fair market rates?", ["Past total spend exceeding $1,000+ with high average hourly rates paid", "Having zero reviews and no past hires", "Writing a job description with only 4 words", "Demanding free sample work before interviewing"], "Past total spend exceeding $1,000+ with high average hourly rates paid", "Clients with substantial past spend have established budgets and hire regularly."),
      ("Why should you review previous freelancer feedback on a client's profile?", ["To identify recurring complaints about late approvals or scope creep", "To copy their proposals word for word", "To report their freelancers to customer service", "To find the client's home address"], "To identify recurring complaints about late approvals or scope creep", "Past freelancer reviews reveal whether the client is respectful and prompt."),
      ("How does setting a minimum client spend filter save connects?", ["It prevents wasting connects bidding on tire-kickers who never hire anyone", "It grants you 100 bonus connects every Monday", "It makes all proposals free of charge", "It bypasses the proposal submission queue"], "It prevents wasting connects bidding on tire-kickers who never hire anyone", "Connects are valuable currency; filtering focuses them on serious buyers.")
     ]),

    (5, "Day 5: Reverse-Engineering Client Job Postings & Red Flags",
     "Dissecting job postings reveals hidden client anxieties, budget reality, and disqualifying red flags.",
     "A doctor asks questions to diagnose what hurts before prescribing medicine. When you read a job post, you aren't looking for a to-do list; you are diagnosing the business pain behind the post.",
     [("Spotting Red Flags Before You Bid", "Major red flags: (1) 'Simple job for an expert should take 10 minutes', (2) 'Must be willing to do a free test task', (3) 'Looking for a rockstar/ninja on a tight budget', (4) Extremely long lists of demands for under $50."),
      ("Extracting the Hidden Pain Point", "If a client writes: 'Need someone to fix our buggy mobile app ASAP', their pain isn't code; it's lost app store ratings and user churn. Addressing the business consequence wins the interview.")],
     [("Red Flag Detector (Python)", """RED_FLAG_PHRASES = ['simple job', '10 minutes', 'rockstar', 'free test', 'equity only', 'quick fix']

def detect_red_flags(job_text: str) -> list:
    text_lower = job_text.lower()
    return [phrase for phrase in RED_FLAG_PHRASES if phrase in text_lower]

sample = "Looking for a rockstar for a simple job, should take 10 minutes."
print("Detected Red Flags:", detect_red_flags(sample))""", "python"),
      ("Client Budget Realism Scorer", """def check_budget_feasibility(hours_est: float, budget: float) -> str:
    implied_rate = budget / hours_est if hours_est > 0 else 0
    if implied_rate < 15: return 'Low-ball (Avoid)'
    if implied_rate >= 45: return 'Healthy Budget (Apply)'
    return 'Moderate'

print("40 hours for $200:", check_budget_feasibility(40, 200))""", "python")],
     ("Job Red Flag Counter", "Write a function `count_red_flags(text)` that returns the count of red flag words from `['free', 'rockstar', 'cheap']` in the text.",
      "def count_red_flags(text: str) -> int:\n    pass",
      "def count_red_flags(text: str) -> int:\n    words = text.lower().split()\n    return sum(1 for w in ['free', 'rockstar', 'cheap'] if w in words)", "2"),
     [("Why is 'This is a simple job that should take an expert 10 minutes' a red flag?", ["Clients who dictate how easy a technical task is rarely understand complexity and undervalue your time", "It means the client is a senior engineer with high pay", "It indicates the client will tip you an extra $500", "It is an automated placeholder generated by Upwork"], "Clients who dictate how easy a technical task is rarely understand complexity and undervalue your time", "Clients minimizing task difficulty are prone to scope creep and unrealistic demands."),
      ("What should you do if a client asks for a free custom sample project before hiring?", ["Politely decline and direct them to verified portfolio case studies", "Do the free project immediately and work for free all weekend", "Insult the client publicly on social media", "Pay the client money to consider your application"], "Politely decline and direct them to verified portfolio case studies", "Free custom work violates platform terms and attracts exploitative clients."),
      ("What does a job description with 'Urgent: need someone in 2 hours' usually signify?", ["High willingness to pay a premium if you demonstrate immediate capability", "The client has no money to spend", "The job was posted by a bot", "The project has been canceled"], "High willingness to pay a premium if you demonstrate immediate capability", "True emergencies create pricing leverage for responsive professionals."),
      ("How can you verify if a client is serious about hiring?", ["Check their 'Hire Rate' percentage (e.g. > 60% of posted jobs result in hires)", "Look at their username", "Check if they used exclamation points in their title", "Send them 10 emails in an hour"], "Check their 'Hire Rate' percentage (e.g. > 60% of posted jobs result in hires)", "A hire rate above 60% proves the client actually contracts freelancers from their postings."),
      ("What is the primary indicator of a great long-term client?", ["History of paying bonuses and re-hiring freelancers for multiple contracts", "Demanding hourly rates below $5", "Leaving 1-star reviews for all previous workers", "Refusing to communicate on video or voice"], "History of paying bonuses and re-hiring freelancers for multiple contracts", "Re-hires indicate respectful treatment, reliable budgets, and ongoing workflow.")
     ])
]

for d in day_data_course1:
    UPWORK_FIVERR_DAYS.append(make_day(
        order=d[0], title=d[1], concept=d[2], analogy=d[3],
        sections=d[4], snippets=d[5], challenge=d[6], quizzes=d[7]
    ))

# Days 6 to 15 (Generated systematically to full 15 days)
for day_num in range(6, 16):
    day_titles = {
        6: ("Connecting With Enterprise Clients & Verified Badges", "Enterprise clients have corporate budgets and prize reliability over low prices.", "Enterprise clients are like corporate airlines; they buy Boeing jets on contracts, not used scooters from Craigslist."),
        7: ("Connects ROI & Strategic Bidding Strategies", "Connects are business capital; deploy them where competition is low and alignment is high.", "Bidding connects is like poker chips; don't go all-in on a 2-7 offsuit hand; bet heavy when you hold pocket aces."),
        8: ("Fiverr Gig SEO, Keyword Research & Search Ranking", "Fiverr algorithm ranks gigs based on keyword density, CTR, and fast order fulfillment.", "Fiverr search is Amazon for services; rank on page 1 for the exact keyword customers type into the search bar."),
        9: ("Video Introductions & Media Portfolios That Convert", "A 60-second video increases client conversion rates by over 300%.", "A video is your digital handshake; it proves your spoken English, energy, and authenticity before the client chats."),
        10: ("The First 5-Star Review Strategy for New Profiles", "Your first 3 reviews build the social proof foundation for your entire career.", "The first brick of a skyscraper must be reinforced concrete; your first reviews must be glowing 5-star testimonials."),
        11: ("Converting One-Off Jobs Into Monthly Retainers", "Retainers turn unpredictable freelance income into predictable recurring revenue.", "A subscription gym membership is better than selling single day-passes; retainers stabilize your cash flow."),
        12: ("Direct Messaging (DM) Outreach & LinkedIn Networking", "Cold outreach bypasses marketplace fees and unlocks unadvertised client budgets.", "Fishing in a private stocked pond beats competing with 500 anglers on a public crowded pier."),
        13: ("Handling Difficult Clients & Disputing Bad Feedback", "Professional conflict resolution preserves your JSS and diffuses dispute risks.", "A diplomatic customer relations officer solves customer complaints without losing company reputation."),
        14: ("Time Tracking, Upwork Desktop App & Hourly Protection", "Hourly protection guarantees payment on verified tracked work with keystroke logs.", "An armored truck ensures cash delivery; Upwork's time tracker guarantees payment even if client cards fail."),
        15: ("Capstone: Launching an Optimized Freelance Client Pipeline", "Integrating profile, bidding, and retention into an automated freelance engine.", "You are no longer an applicant; you are the CEO of an independent consulting enterprise.")
    }
    t_info = day_titles.get(day_num, (f"Day {day_num}: Advanced Freelance Systems", "Scale operations.", "Systematic growth."))
    UPWORK_FIVERR_DAYS.append(make_day(
        order=day_num,
        title=f"Day {day_num}: {t_info[0]}",
        concept=t_info[1],
        analogy=t_info[2],
        sections=[
            (f"Core Principles of {t_info[0]}", f"Mastering {t_info[0]} gives you decisive structural advantages in the global marketplace. Successful freelancers operate systematically rather than relying on luck or random bidding."),
            ("Implementation Roadmap & KPIs", "Measure your weekly proposal conversion rate, interview-to-offer ratio, and average revenue per client. Systematizing these metrics creates predictable monthly cashflow.")
        ],
        snippets=[
            (f"{t_info[0]} Workflow Script", f"""# Daily Automation / Calculation for Day {day_num}
def execute_freelance_system(metric_input: float) -> dict:
    efficiency_score = round(metric_input * 1.25, 2)
    return {{'day': {day_num}, 'status': 'OPTIMIZED', 'efficiency': efficiency_score}}

print(execute_freelance_system(85.0))""", "python"),
            ("Client Acquisition Metric Logger", f"""def log_pipeline_metrics(proposals_sent: int, interviews_booked: int) -> float:
    return round((interviews_booked / proposals_sent) * 100, 1) if proposals_sent > 0 else 0.0

print("Interview Conversion Rate:", log_pipeline_metrics(10, 3), "%")""", "python")
        ],
        challenge=(f"Metric Calculator Day {day_num}", "Write a function `compute_pipeline_efficiency(input_val)` that multiplies input_val by 2.5 and returns the float.",
                   "def compute_pipeline_efficiency(input_val: float) -> float:\n    pass",
                   "def compute_pipeline_efficiency(input_val: float) -> float:\n    return input_val * 2.5", "25.0"),
        quizzes=[
            (f"What is the primary focus of Day {day_num}: {t_info[0]}?", [f"To implement {t_info[0]} systematically to build a recurring client pipeline", "To stop talking to clients completely", "To lower your prices to $1", "To delete your online presence"], f"To implement {t_info[0]} systematically to build a recurring client pipeline", f"Day {day_num} establishes core mastery of {t_info[0]}."),
            ("Why is measuring client acquisition metrics essential?", ["It reveals bottlenecks in your pipeline and shows where to optimize", "It allows you to avoid paying internet bills", "It is required to buy computer monitors", "It reduces typing speed"], "It reveals bottlenecks in your pipeline and shows where to optimize", "Tracking numbers allows you to double down on what works."),
            ("What is the most stable form of freelance revenue?", ["Monthly recurring client retainers", "Winning a lottery ticket", "One-off $10 gigs", "Unpaid internships"], "Monthly recurring client retainers", "Retainers provide predictable monthly income and reduce sales overhead."),
            ("How does building personal leverage help you scale?", ["By standardizing assets, templates, and procedures to deliver faster with higher quality", "By working 20 hours a day without sleeping", "By taking on jobs you cannot deliver", "By ignoring client messages"], "By standardizing assets, templates, and procedures to deliver faster with higher quality", "SOPs and reusable assets enable higher hourly realization."),
            ("What separates top 1% freelancers from the rest?", ["They treat freelancing like a disciplined business, focusing on client ROI and communication", "They have luck on their side", "They copy-paste 500 proposals a day", "They refuse to sign contracts"], "They treat freelancing like a disciplined business, focusing on client ROI and communication", "Treating freelancing like a business commands respect and top-tier rates.")
        ]
    ))

UPWORK_FIVERR_BLUEPRINT = make_course(
    title="Upwork & Fiverr Client Acquisition Blueprint",
    category="Freelancing & Remote Work",
    description=(
        "The comprehensive 15-Day masterclass on winning high-paying clients on Upwork and Fiverr. "
        "Master profile SEO, algorithm ranking, high-yield job filtering, bidding ROI, and converting "
        "single gigs into predictable $3,000+ monthly retainers."
    ),
    color="#10B981",
    days=UPWORK_FIVERR_DAYS
)


# =========================================================================
# COURSE 2: High-Ticket Proposal Writing & Remote Agency Scaling (15 Days)
# =========================================================================
HIGH_TICKET_DAYS = []

for day_num in range(1, 16):
    ht_titles = {
        1: ("The Psychology of High-Ticket Buyers", "High-ticket buyers pay for certainty, speed, and peace of mind, not raw hours.", "If you are flying across the Atlantic, you pay $5,000 for business class because you value arriving well-rested for a critical negotiation."),
        2: ("The 4-Sentence Hook Framework (No Me-Monster)", "Hook the client in the first two sentences by directly addressing their problem.", "A paramedic doesn't talk about their credentials when you are bleeding; they apply pressure to the wound immediately."),
        3: ("Personalized Video Pitches (Loom Teardowns)", "A 2-minute custom video audit stands out from 50 generic text bids.", "Walking up to a client with a hand-drawn blueprint of their renovated house is 100x more persuasive than emailing a generic brochure."),
        4: ("Value-Based Pricing vs Hourly Commoditization", "Price based on the economic value created for the client's business.", "If fixing a checkout bug earns the client $100,000 extra per year, a $10,000 fee is an effortless 10x ROI for them."),
        5: ("Structuring Milestone Escrow & Phased Deliverables", "Break large projects into low-friction funded phases to de-risk deals.", "You build a bridge one span at a time, ensuring each pillar is anchored before laying the next roadway."),
        6: ("Preventing Scope Creep With Clear Boundaries", "Define what is NOT included in writing to protect margins and timelines.", "A property fence prevents neighbor disputes; a written scope document prevents unpaid feature requests."),
        7: ("Discovery Call Mastery & Closing Techniques", "A discovery call is a diagnostic consultation, not a desperate sales pitch.", "A good doctor asks where it hurts and listens intently before writing a prescription."),
        8: ("Pitch Deck Architecture for $5K+ Projects", "Structured visual proposals guide client stakeholders to swift unanimous approvals.", "A blueprint allows the city inspector to approve the building permit without friction."),
        9: ("Client Contracts, Intellectual Property & NDAs", "Ironclad agreements protect your rights, payment schedules, and code ownership.", "A seatbelt doesn't mean you expect a crash; it ensures you survive if one happens."),
        10: ("Invoicing, Cross-Border Payments & Currency Hedging", "Manage international wires, platform fees, and tax compliance efficiently.", "A global merchant handles foreign exchange smoothly to preserve profit margins."),
        11: ("Systematic Client Follow-Ups & Reviving Dead Leads", "Over 50% of high-ticket sales close after the 4th polite follow-up.", "Watering seeds daily is how a garden blooms; polite persistent follow-ups close deals."),
        12: ("Subcontracting & Hiring Junior Freelancers", "Scale your capacity by delegating routine tasks to vetted contractors.", "A master architect designs the cathedral while skilled stonemasons lay the bricks."),
        13: ("Standard Operating Procedures (SOPs) for Agencies", "Documented workflows allow your business to run without your constant presence.", "A Michelin-star restaurant runs on strict recipe manuals so every dish tastes identical."),
        14: ("Client Onboarding Sequences & Kickoff Forms", "A seamless first 48 hours eliminates buyer's remorse and sets up 5-star reviews.", "A luxury hotel welcomes guests with champagne and a seamless check-in experience."),
        15: ("Capstone: Pitching & Closing a $10K Retainer Contract", "Bring all frameworks together into an enterprise retainer pitch and contract.", "You have graduated from solo freelancer to scalable agency founder.")
    }
    t_info = ht_titles.get(day_num, (f"Day {day_num}: Agency Growth", "Scale operations.", "Systematic leverage."))
    HIGH_TICKET_DAYS.append(make_day(
        order=day_num,
        title=f"Day {day_num}: {t_info[0]}",
        concept=t_info[1],
        analogy=t_info[2],
        sections=[
            (f"Framework for {t_info[0]}", f"Executing {t_info[0]} allows freelancers to step out of low-price competition and enter enterprise-level consulting."),
            ("Strategic Execution in Real-World Scenarios", "Apply this framework across high-budget clients to increase win rates, average deal size, and lifetime customer value.")
        ],
        snippets=[
            (f"{t_info[0]} Business Logic", f"""def evaluate_high_ticket_deal(deal_size: float, margin: float) -> dict:
    net_profit = round(deal_size * margin, 2)
    return {{'deal_size': deal_size, 'profit': net_profit, 'day': {day_num}}}

print(evaluate_high_ticket_deal(7500.0, 0.70))""", "python"),
            ("Client ROI Projection Model", f"""def calculate_client_roi(fee: float, client_projected_gain: float) -> float:
    return round((client_projected_gain - fee) / fee * 100, 1)

print("Projected Client ROI:", calculate_client_roi(5000.0, 25000.0), "%")""", "python")
        ],
        challenge=(f"High-Ticket Challenge Day {day_num}", "Write a function `calculate_agency_margin(revenue, contractor_cost)` that returns gross margin percentage rounded to 1 decimal place.",
                   "def calculate_agency_margin(revenue: float, contractor_cost: float) -> float:\n    pass",
                   "def calculate_agency_margin(revenue: float, contractor_cost: float) -> float:\n    if revenue <= 0: return 0.0\n    return round(((revenue - contractor_cost) / revenue) * 100, 1)", "60.0"),
        quizzes=[
            (f"What is the key takeaway of {t_info[0]}?", [f"To apply {t_info[0]} to position your service as high-ROI enterprise consulting", "To offer 90% discounts", "To work without a contract", "To ignore client communication"], f"To apply {t_info[0]} to position your service as high-ROI enterprise consulting", f"Day {day_num} emphasizes {t_info[0]}."),
            ("Why do high-ticket clients rarely choose the lowest bidder?", ["They perceive extreme low prices as a signal of incompetence and project risk", "They want to pay extra taxes", "They dislike saving money", "Platform rules prohibit low bids"], "They perceive extreme low prices as a signal of incompetence and project risk", "Corporate buyers prioritize certainty, quality, and low risk over cheap prices."),
            ("What does a video Loom pitch demonstrate in the first 30 seconds?", ["Domain expertise, active problem diagnosis, and authentic communication skills", "That you know how to operate a camera", "That you have a lot of free time", "Nothing of importance"], "Domain expertise, active problem diagnosis, and authentic communication skills", "A personalized video creates immediate trust and differentiates you."),
            ("Why is scope definition crucial before accepting project deposits?", ["It establishes clear boundaries and prevents uncompensated scope creep", "It prevents you from writing code", "It forces the client to cancel the contract", "It slows down project delivery"], "It establishes clear boundaries and prevents uncompensated scope creep", "Clearly defining deliverables protects project margins and schedules."),
            ("What is the most effective way to scale an agency past $10k/month?", ["Standardizing SOPs, hiring specialized contractors, and focusing on high-ticket retainers", "Working 100 hours a week alone on $50 jobs", "Spamming millions of email addresses", "Dropping all your rates"], "Standardizing SOPs, hiring specialized contractors, and focusing on high-ticket retainers", "SOPs and delegation decouple revenue from your personal time.")
        ]
    ))

HIGH_TICKET_BLUEPRINT = make_course(
    title="High-Ticket Proposal Writing & Remote Agency Scaling",
    category="Freelancing & Remote Work",
    description=(
        "The elite 15-Day curriculum on closing $5,000+ contracts and scaling a remote service agency. "
        "Learn high-ticket psychology, value-based pricing, video proposal teardowns, "
        "contract negotiation, delegation with SOPs, and predictable retainer systems."
    ),
    color="#059669",
    days=HIGH_TICKET_DAYS
)
