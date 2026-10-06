import time
from prisma import Prisma

def get_domain_snippet(module_name, day):
    mn = module_name.lower()
    
    # 1. Medical Billing
    if any(k in mn for k in ["medical", "billing", "claim", "hipaa", "insurance", "rcm", "clearinghouse", "denial", "credentialing"]):
        if day <= 7:
            return """// CMS-1500 Claim Payload Structure (JSON)
{
  "patient": {
    "id": "PT-99384",
    "name": "John Doe",
    "dob": "1985-10-12",
    "insurance_id": "INS-4829104"
  },
  "provider": { "npi": "1234567890" },
  "diagnosis_codes": ["J01.90", "R05"],
  "status": "DRAFT"
}"""
        elif day <= 14:
            return """// EDI 837 Professional Claim Segment (Excerpt)
NM1*85*2*HOSPITAL INC*****XX*1234567890~
HL*1**20*1~
PRV*BI*PXC*207Q00000X~
SBR*P*18*******CI~
// This structure is the industry standard for transmitting
// healthcare claims electronically to clearinghouses."""
        elif day <= 21:
            return """// Denial Management Audit Log
[ERROR: CO-16] Claim lacks information needed for adjudication.
[ACTION REQUIRED]
1. Verify patient insurance eligibility on Date of Service.
2. Check CPT/ICD-10 crosswalk for medical necessity.
3. Attach required clinical documentation.
4. Resubmit within 30-day timely filing limit."""
        elif day <= 28:
            return """// HIPAA Compliance Checklist (Internal Audit)
- [x] All PHI transmitted via TLS 1.2+ encryption.
- [x] Role-Based Access Control (RBAC) active for billing staff.
- [ ] BAA (Business Associate Agreements) signed with all clearinghouses.
- [x] Session timeout set to 15 minutes for idle terminals."""
        else:
            return """// Capstone: Automated RCM Pipeline
function processClaimBatch(batchId) {
    console.log(`[RCM] Initiating scrubbing for batch: ${batchId}`);
    const passed = claimScrubber.validate(batchId);
    if (passed) {
        clearinghouseAPI.transmit(batchId);
        console.log(`[RCM] Batch transmitted successfully.`);
    } else {
        console.error(`[RCM] Scrubbing failed. Routing to AR team.`);
    }
}"""

    # 2. Crypto & Trading
    elif any(k in mn for k in ["crypto", "trading", "defi", "stock", "budget", "macroeconomics", "risk", "spot"]):
        if day <= 7:
            return """// Market Data Payload (WebSocket)
{
  "asset": "BTC/USD",
  "price": 64230.50,
  "volume_24h": "1.2B",
  "trend": "BULLISH",
  "support_level": 62000,
  "resistance_level": 65500
}"""
        elif day <= 14:
            return """# Risk Management Calculator (Python)
def calculate_position_size(account_balance, risk_pct, stop_loss_pct):
    risk_amount = account_balance * (risk_pct / 100)
    position_size = risk_amount / (stop_loss_pct / 100)
    return position_size

# Example: $10,000 account, risking 2%, with a 5% stop loss
size = calculate_position_size(10000, 2, 5)
print(f"Max Position Size: ${size}")"""
        elif day <= 21:
            return """// Smart Contract Snippet (Solidity) - Liquidity Pool
function addLiquidity(uint amountTokenA, uint amountTokenB) external {
    require(amountTokenA > 0 && amountTokenB > 0, "Zero amount");
    tokenA.transferFrom(msg.sender, address(this), amountTokenA);
    tokenB.transferFrom(msg.sender, address(this), amountTokenB);
    uint liquidity = calculateLiquidity(amountTokenA, amountTokenB);
    _mint(msg.sender, liquidity);
}"""
        elif day <= 28:
            return """// Trading Bot Algorithm (Moving Average Crossover)
if short_term_ma > long_term_ma and previous_short <= previous_long:
    execute_trade(action="BUY", size=calculated_size)
    log("Golden Cross Detected. Executing Long Position.")
elif short_term_ma < long_term_ma and previous_short >= previous_long:
    execute_trade(action="SELL", size=calculated_size)
    log("Death Cross Detected. Liquidating Position.")"""
        else:
            return """// Capstone: Automated Portfolio Rebalancer
{
  "portfolio_target": {
    "BTC": "40%",
    "ETH": "30%",
    "STABLES": "30%"
  },
  "rebalance_threshold": "5%",
  "action": "Triggering smart contract routing to restore target allocations via DEX aggregators."
}"""

    # 3. Design / UI / UX
    elif any(k in mn for k in ["design", "ui", "ux", "graphic", "typography", "color", "illustration", "portfolio"]):
        if day <= 7:
            return """/* Core Design Tokens (CSS Variables) */
:root {
  /* Color Palette */
  --primary-color: #3B82F6;
  --secondary-color: #10B981;
  --bg-color: #F8FAFC;
  --text-main: #1E293B;
  
  /* Typography */
  --font-heading: 'Inter', sans-serif;
  --font-body: 'Roboto', sans-serif;
  --spacing-md: 16px;
}"""
        elif day <= 14:
            return """<!-- Accessible UI Component -->
<button 
  class="btn-primary flex items-center justify-center gap-2 rounded-lg"
  aria-label="Submit Payment Form"
  aria-disabled="false">
  <span>Submit Payment</span>
  <svg class="icon-spinner hidden" aria-hidden="true"></svg>
</button>
<!-- Note: Always ensure contrast ratios meet WCAG AA standards (4.5:1) -->"""
        elif day <= 21:
            return """// UI Animation Sequence (Framer Motion / React)
const slideUpVariant = {
  hidden: { opacity: 0, y: 20 },
  visible: { 
    opacity: 1, 
    y: 0,
    transition: { duration: 0.4, ease: "easeOut" }
  }
};
// Use micro-interactions to guide the user's eye without overwhelming them."""
        elif day <= 28:
            return """/* Advanced Responsive Grid (CSS Grid) */
.dashboard-layout {
  display: grid;
  grid-template-columns: 250px 1fr 300px;
  grid-template-areas: 
    "sidebar header panel"
    "sidebar main panel";
  gap: 1.5rem;
}

@media (max-width: 1024px) {
  .dashboard-layout {
    grid-template-columns: 1fr;
    grid-template-areas: 
      "header"
      "main";
  }
}"""
        else:
            return """// Capstone: Design System JSON Export
{
  "system_name": "Nova UI Kit",
  "version": "1.0.0",
  "components": [
    { "name": "PrimaryButton", "states": ["default", "hover", "disabled", "loading"] },
    { "name": "DataCard", "variants": ["elevated", "outlined", "flat"] }
  ],
  "accessibility_score": "98/100"
}"""

    # 4. Networking
    elif any(k in mn for k in ["network", "osi", "tcp", "ip ", "routing", "dns", "wireless", "troubleshooting", "firewall"]):
        if day <= 7:
            return """# Basic Network Interface Configuration (Linux)
auto eth0
iface eth0 inet static
    address 192.168.1.50
    netmask 255.255.255.0
    gateway 192.168.1.1
    dns-nameservers 8.8.8.8 1.1.1.1"""
        elif day <= 14:
            return """! Cisco IOS Router OSPF Configuration
router ospf 10
 router-id 1.1.1.1
 network 10.0.0.0 0.255.255.255 area 0
 network 192.168.1.0 0.0.0.255 area 1
 passive-interface GigabitEthernet0/1
! This establishes dynamic routing between internal subnets."""
        elif day <= 21:
            return """# Iptables Firewall Rule (Security)
# Drop all incoming traffic by default
iptables -P INPUT DROP
# Allow established connections
iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
# Allow HTTP/HTTPS traffic
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
iptables -A INPUT -p tcp --dport 443 -j ACCEPT"""
        elif day <= 28:
            return """# Advanced BGP Troubleshooting Log
BGP routing table entry for 10.100.0.0/16, version 42
Paths: (2 available, best #1)
  Local
    192.168.50.2 from 192.168.50.2 (10.0.0.2)
      Origin IGP, metric 0, localpref 100, valid, internal, best
      Community: 65000:100
# Ensure route reflectors are passing the correct communities."""
        else:
            return """# Capstone: Cloud VPC Terraform Configuration
resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"
  enable_dns_support = true
  enable_dns_hostnames = true
  tags = { Name = "Production-VPC" }
}
# Deploys a complete virtual network architecture."""

    # 5. Freelancing & Soft Skills
    elif any(k in mn for k in ["freelanc", "profile", "proposal", "client", "gig", "bidding", "agency", "time management"]):
        if day <= 7:
            return """// Freelancer Profile Optimization Template
[Headline]: Expert React Native Developer | Top Rated | 5+ Yrs Exp
[Overview]:
Hi, I'm [Name]. I specialize in building cross-platform mobile apps that scale.
My tech stack: React Native, Expo, Node.js, and Firebase.
I focus on writing clean, maintainable code and providing daily communication.
Let's turn your idea into a deployed app."""
        elif day <= 14:
            return """// Winning Proposal Script (The 'Hook')
Hi [Client Name],
I saw you need a custom e-commerce solution built on Shopify. 
I recently completed a similar project for [Brand Name] that increased their conversion rate by 15%.
I can start by auditing your current theme to identify the slow-loading bottlenecks.
Are you available for a quick 10-minute call tomorrow to discuss the architecture?
Best, [Your Name]"""
        elif day <= 21:
            return """// Project Scope & Escrow Agreement
Project: Mobile App MVP Development
Milestone 1 (20%): UI/UX Wireframes & Database Schema Design.
Milestone 2 (40%): Frontend Implementation & API Integration.
Milestone 3 (40%): Bug Fixing, QA Testing, and App Store Submission.
*Note: No work commences until the current milestone is fully funded in Escrow.*"""
        elif day <= 28:
            return """// Client Feedback & Revision Management
When dealing with scope creep, use this professional pushback:
"Hi [Client], I'm happy to add the social media sharing feature! 
Since this wasn't in our original scope document, it will require an additional 5 hours of work. 
I can send over a new milestone for $250. Should we proceed with adding it, or stick to the original plan?"""
        else:
            return """// Capstone: Agency Scaling CRM Dashboard
{
  "active_clients": 12,
  "monthly_recurring_revenue": "$14,500",
  "pipeline": [
    {"lead": "TechCorp", "status": "Proposal Sent", "value": "$5,000"},
    {"lead": "Local Gym", "status": "Contract Signed", "value": "$2,000"}
  ],
  "contractors": 3
}"""

    # 6. Culinary & Recipes
    elif any(k in mn for k in ["recipe", "food", "baking", "diet", "sweet", "hygiene", "beverage", "spice"]):
        if day <= 7:
            return """// Standard Recipe Structure (JSON Schema)
{
  "recipe": "Classic Chicken Karahi",
  "prep_time_mins": 15,
  "cook_time_mins": 30,
  "ingredients": [
    {"item": "Bone-in Chicken", "qty": "1 kg"},
    {"item": "Tomatoes (pureed)", "qty": "500g"},
    {"item": "Ginger-Garlic Paste", "qty": "2 tbsp"}
  ],
  "spice_level": "Medium-High"
}"""
        elif day <= 14:
            return """// Food Safety & Temp Log
CRITICAL CONTROL POINT (CCP): Meat internal temperature.
- Chicken must reach an internal temp of 165°F (74°C).
- Ground beef must reach 160°F (71°C).
- Danger Zone: 40°F - 140°F (Bacteria multiplies rapidly).
Action: Never leave perishable food at room temp for over 2 hours."""
        elif day <= 21:
            return """// Baker's Percentage Formula
In professional baking, all ingredients are a percentage of total flour weight.
Flour: 1000g (100%)
Water: 700g (70% Hydration)
Salt: 20g (2%)
Yeast: 10g (1%)
This allows you to scale recipes infinitely without losing the exact texture."""
        elif day <= 28:
            return """// Spice Blending Profile (Garam Masala)
Ratio by weight for perfect balance:
- Cumin Seeds: 40%
- Coriander Seeds: 30%
- Black Peppercorns: 10%
- Cardamom (Green): 10%
- Cloves & Cinnamon: 10%
Dry roast on low heat until fragrant before grinding to release essential oils."""
        else:
            return """// Capstone: Professional Catering Menu Plan
{
  "event": "Wedding Reception for 200",
  "menu_costing": {
    "food_cost_per_head": "$12.50",
    "selling_price_per_head": "$45.00",
    "gross_margin": "72%"
  },
  "execution_timeline": "Prep 2 days prior. Cook sauces 1 day prior. Fire proteins 2 hrs before service."
}"""

    # 7. Languages
    elif any(k in mn for k in ["german", "chinese", "french", "english", "vocabulary", "grammar", "pronunciation", "writing", "idiom"]):
        if day <= 7:
            return """// Language Acquisition Structure
Topic: Formal vs. Informal Greetings
[English] "Hello, how are you?"
[Formal] Use this with strangers, elders, or in business settings.
[Informal] Use this with friends and family.
*Grammar Rule*: Pay attention to pronoun shifts (e.g., 'Sie' vs 'du' in German, 'Vous' vs 'tu' in French)."""
        elif day <= 14:
            return """// Sentence Structure Breakdown
Subject + Verb + Object (SVO)
The foundation of clarity in communication.
Example: "The company [Subject] launched [Verb] a new product [Object]."
When using passive voice, the object becomes the focus:
"A new product was launched by the company." 
*Tip*: Avoid passive voice in professional writing to maintain a strong, active tone."""
        elif day <= 21:
            return """// Professional Writing Example (Email)
Subject: Action Required - Q3 Marketing Report
Hi Team,
Please review the attached Q3 Marketing Report. We need to finalize the budget adjustments by Thursday at 5 PM EST.
Key areas to review:
1. Ad spend efficiency.
2. Conversion rate drops in September.
Let me know if you have any questions.
Best, [Name]"""
        elif day <= 28:
            return """// Phonetics and Pronunciation Guide
The Schwa Sound /ə/
It is the most common vowel sound in the English language. 
It sounds like a very short, relaxed 'uh'.
Examples:
- The 'a' in "about" (/əˈbaʊt/)
- The 'e' in "taken" (/ˈteɪkən/)
Mastering the schwa is the key to sounding fluent and natural."""
        else:
            return """// Capstone: Conversational Roleplay Transcript
Scenario: Negotiating a business contract.
Person A: "We love the proposal, but the timeline is slightly too aggressive."
Person B: "I understand your concern. If we extend the deadline by two weeks, would you be open to adjusting the milestone payments?"
Person A: "That sounds like a fair compromise. Let's draft the revision."
Goal: Maintain professional tone, use industry vocabulary, and resolve conflict."""

    # 8. Web / App / Programming (Default Tech)
    elif any(k in mn for k in ["react", "flask", "app", "git", "api", "software", "development", "cybersecurity"]):
        if day <= 7:
            return """// Initial Tech Environment Setup
import { AppRegistry } from 'react-native';
import App from './App';
import { name as appName } from './app.json';

// Ensure the root component is registered
AppRegistry.registerComponent(appName, () => App);
console.log('Environment booted successfully.');"""
        elif day <= 14:
            return """// RESTful API Endpoint (Flask/Python)
@app.route('/api/v1/users', methods=['GET'])
def get_users():
    try:
        users = db.query(User).all()
        return jsonify({"status": "success", "data": [u.serialize() for u in users]}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500"""
        elif day <= 21:
            return """// State Management (React/Redux)
const userSlice = createSlice({
  name: 'user',
  initialState: { profile: null, isAuthenticated: false },
  reducers: {
    loginSuccess: (state, action) => {
      state.profile = action.payload;
      state.isAuthenticated = true;
    },
    logout: (state) => {
      state.profile = null;
      state.isAuthenticated = false;
    }
  }
});"""
        elif day <= 28:
            return """// Security: JWT Middleware Validation
const authenticateToken = (req, res, next) => {
  const authHeader = req.headers['authorization'];
  const token = authHeader && authHeader.split(' ')[1];
  
  if (token == null) return res.sendStatus(401);
  
  jwt.verify(token, process.env.TOKEN_SECRET, (err, user) => {
    if (err) return res.sendStatus(403);
    req.user = user;
    next();
  });
};"""
        else:
            return """// Capstone: Production Deployment Pipeline
name: CI/CD Pipeline
on: [push]
jobs:
  build_and_deploy:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Install Dependencies
      run: npm ci
    - name: Run Unit Tests
      run: npm test
    - name: Deploy to Server
      run: ./deploy.sh production"""

    # 9. Business / General (Fallback for others)
    else:
        if day <= 7:
            return """// Business Strategy Model: SWOT Analysis
[Strengths]: Strong brand loyalty, proprietary technology.
[Weaknesses]: High overhead costs, limited distribution channels.
[Opportunities]: Expansion into emerging markets, new demographic targeting.
[Threats]: Aggressive competitor pricing, shifting regulatory laws."""
        elif day <= 14:
            return """// Retail & POS Inventory Tracking Logic
function processSale(itemCode, quantity) {
    const item = database.find(itemCode);
    if (item.stock >= quantity) {
        item.stock -= quantity;
        recordRevenue(item.price * quantity);
        if (item.stock <= item.reorder_threshold) {
            triggerReorderAlert(item);
        }
    } else {
        alert("Insufficient stock to complete sale.");
    }
}"""
        elif day <= 21:
            return """// Financial Accounting: P&L Statement Structure
INCOME:
  Gross Sales:          $150,000
  Cost of Goods Sold:  -$60,000
  -----------------------------
  Gross Profit:         $90,000

EXPENSES:
  Payroll:             -$30,000
  Rent & Utilities:    -$15,000
  Marketing:            -$5,000
  -----------------------------
  Net Profit:           $40,000 (26.6% Margin)"""
        elif day <= 28:
            return """// KPI Dashboard Metrics (JSON format)
{
  "Customer_Acquisition_Cost_CAC": "$45.00",
  "Lifetime_Value_LTV": "$350.00",
  "LTV_to_CAC_Ratio": "7.7x (Healthy)",
  "Monthly_Churn_Rate": "2.1%",
  "Net_Promoter_Score_NPS": 68
}"""
        else:
            return """// Capstone: Complete Business Plan Execution
Executive Summary: Launching a B2B SaaS platform for inventory management.
Target Market: Mid-sized retail operations (5-50 locations).
Monetization: $199/month subscription tier.
Year 1 Goal: 100 active subscriptions ($238k ARR).
Execution: Aggressive LinkedIn outreach and attending 3 major retail trade shows."""

def generate_content_for_day(day, module_name):
    # Base structure
    base_intro = f"Welcome to Day {day} of your 30-Day journey mastering {module_name}! "
    code_snippet = get_domain_snippet(module_name, day)
    
    if 1 <= day <= 7:
        title = f"Day {day}: Fundamentals & Core Theory of {module_name}"
        content = base_intro + f"""
## Understanding the Basics of {module_name}
The first week of any mastery course is dedicated to building an unshakeable foundation. When dealing with {module_name}, the terminology and basic workflows are critical. Unlike advanced subjects where you can skip straight to implementation, {module_name} requires a deep understanding of its underlying architecture.

History has shown that experts in {module_name} spend 80% of their time planning and 20% executing. Why? Because the fundamental rules govern everything that follows. In today's highly competitive tech and business environment, having a superficial understanding of {module_name} will lead to catastrophic failures at scale.

## Real-World Application
Imagine a global enterprise trying to scale their operations. If their foundation in {module_name} is weak, the entire system collapses under load. Professionals use these exact concepts we are covering today to ensure stability. For example, when consulting for Fortune 500 companies, the very first audit usually uncovers glaring mistakes in these basic {module_name} principles. By mastering this today, you are already ahead of 90% of your peers.

## The Theory of Operation
Let's break down how this works under the hood. The core mechanism of {module_name} revolves around input processing and structured output delivery. Whether it's code, design, or business strategy, the inputs must be sanitized, categorized, and evaluated. As you progress, you will notice that {module_name} is not just a tool, but a complete paradigm shift in how you solve problems. Always remember: measure twice, cut once.

## Summary & Best Practices
- Never skip the planning phase.
- Always validate your initial assumptions regarding {module_name}.
- Keep your workflows modular and easy to debug.
- Document your progress, as the complexity will ramp up significantly in Week 2.
"""
    
    elif 8 <= day <= 14:
        title = f"Day {day}: Intermediate Workflows in {module_name}"
        content = base_intro + f"""
## Diving Deeper into {module_name}
Now that the foundation is laid, it is time to look at intermediate workflows. {module_name} really starts to shine when you combine basic tools into complex pipelines. The difference between an amateur and a professional is how they handle data and process flow in {module_name}.

## Handling Complexity
As your projects grow in size, managing the state of {module_name} becomes your primary challenge. You cannot rely on simple, linear thinking anymore. You must anticipate edge cases. What happens if the input is corrupted? What happens if the market changes? In {module_name}, robust error handling and agile adaptation are mandatory. This week, we focus heavily on creating modular, reusable assets that can survive in unpredictable environments.

## Real-World Industry Example
Let's look at a modern tech startup utilizing {module_name}. They don't just build a product; they build a system. When they deploy {module_name} to millions of users, they use intermediate strategies like load balancing, component recycling, and aggressive caching. If you are applying this to a non-tech field, the equivalent is delegating tasks, standardizing operating procedures, and creating feedback loops. Without these intermediate steps, scaling is physically impossible.

## Key Takeaways for Today
- Modularity is your best friend. Break massive {module_name} tasks into micro-tasks.
- Assume your first iteration will fail. Build in mechanisms to catch those failures gracefully.
- Start analyzing your workflow for bottlenecks. If a process takes too long, it needs optimization.
- Prepare yourself for Week 3, where we will strip away the safety wheels and tackle raw, unoptimized data.
"""
    
    elif 15 <= day <= 21:
        title = f"Day {day}: Advanced Methodologies for {module_name}"
        content = base_intro + f"""
## The Advanced Architecture of {module_name}
Welcome to Week 3. You are now entering the advanced tier of {module_name}. The concepts covered here are often only understood by Senior-level practitioners. We are moving away from \"how to use the tool\" and shifting entirely into \"how to architect the system.\"

## Optimization and Scale
At this level, making it work is no longer enough. It must work fast, efficiently, and flawlessly. Optimization in {module_name} requires a deep understanding of memory management, resource allocation, and algorithmic complexity. Even in non-technical fields, this equates to time-motion studies, extreme financial auditing, and hyper-targeted marketing. Every single millisecond, or every single cent, counts.

## Real-World Case Study
Consider a massive multinational corporation implementing {module_name}. They have petabytes of data or thousands of employees. A 1% inefficiency in their {module_name} strategy costs them tens of millions of dollars annually. To solve this, they deploy advanced processing, distributed logic, and highly decoupled micro-architectures. In today's lesson, we will simulate exactly how these corporations audit and refactor their legacy systems into highly performant engines.

## Advanced Strategies
- **Decoupling**: Never let two separate systems depend entirely on each other. If one goes down, the other must survive.
- **Asynchronous Execution**: Do not wait for slow processes. Move them to the background and keep the main thread moving.
- **Profiling**: Never guess what is slow. Measure it. Use data to drive your optimization decisions in {module_name}.
"""
        
    elif 22 <= day <= 28:
        title = f"Day {day}: Expert Masterclass in {module_name}"
        content = base_intro + f"""
## The Final Polish
Week 4 is the Masterclass. You possess all the knowledge needed to execute {module_name} at an elite level. Now, we focus on polish, security, and edge-case survival. 

## Security and Compliance
A massive aspect of professional {module_name} is ensuring it cannot be exploited. In software, this means preventing injections and memory leaks. In business, it means strict legal compliance, contract negotiation, and intellectual property protection. An expert in {module_name} does not just build things; they build impenetrable things. Today's lesson dives deep into threat modeling. We will intentionally try to break our own {module_name} systems to see where they fail.

## Real-World Failure Example
In 2017, a major corporation ignored these exact expert principles in {module_name}. A simple unhandled exception caused a cascading failure that wiped out their entire database, costing them billions. They assumed the \"happy path\" would always occur. Experts know the happy path is a myth. You must design for failure. Today, we will implement Chaos Engineering—randomly shutting down parts of our {module_name} strategy to guarantee the rest of the system stays online.

## Final Preparations
- Audit your entire workflow from Day 1 to Day {day-1}.
- Implement strict testing protocols. If it isn't tested, it is broken.
- Prepare your presentation layer. How you communicate your mastery of {module_name} to stakeholders is just as important as the execution.
"""
        
    else:
        title = f"Day {day}: The {module_name} Capstone Project"
        content = base_intro + f"""
## The Ultimate Capstone
You have reached the pinnacle. Days 29 and 30 are completely dedicated to the {module_name} Capstone Project. This is an unguided, comprehensive exam of your abilities. You must build a fully functional, production-ready implementation of {module_name} from absolute scratch.

## Project Requirements
Your capstone must incorporate:
1. The foundational structures we built in Week 1.
2. The modular workflows and error handling from Week 2.
3. The hyper-optimizations and architectures from Week 3.
4. The bulletproof security protocols from Week 4.

## The Real-World Deployment
Once your capstone is complete, you will theoretically deploy this to a live environment. In a real-world scenario, this is where you hand off the project to the client, push the code to a production server, or launch the marketing campaign to millions. The stakes are high, but your preparation in {module_name} has been exhaustive.

## Graduation
Upon completing this capstone, you are no longer a student. You are an elite practitioner of {module_name}. You have the muscle memory, the theoretical understanding, and the practical portfolio to prove your worth in the global market. Congratulations, and good luck on the final execution!
"""

    return title, content, code_snippet

def generate_flashcards(lesson_id, step_id, day, module_name):
    # Generates exactly 5 flashcards per day based on the week's theme
    if 1 <= day <= 7:
        theme = "Fundamentals"
    elif 8 <= day <= 14:
        theme = "Intermediate Workflows"
    elif 15 <= day <= 21:
        theme = "Advanced Architecture"
    elif 22 <= day <= 28:
        theme = "Security and Mastery"
    else:
        theme = "Capstone Deployment"
        
    return [
        {"lessonId": lesson_id, "lessonStepId": step_id, "question": f"What is the primary focus of {theme} in {module_name}?", "answer": f"To establish a robust and highly scalable foundation for all {module_name} operations."},
        {"lessonId": lesson_id, "lessonStepId": step_id, "question": f"Why is error handling critical on Day {day} of {module_name}?", "answer": "Because assuming the 'happy path' leads to cascading system failures in real-world environments."},
        {"lessonId": lesson_id, "lessonStepId": step_id, "question": f"How do professionals optimize {module_name} tasks?", "answer": "By heavily utilizing modularity, profiling, and iterative optimization."},
        {"lessonId": lesson_id, "lessonStepId": step_id, "question": f"What happens if you skip the planning phase in {module_name}?", "answer": "The underlying architecture becomes fragile, making future scalability impossible without rewriting everything from scratch."},
        {"lessonId": lesson_id, "lessonStepId": step_id, "question": f"What is the ultimate goal of the Day {day} lesson for {module_name}?", "answer": "To transition from theoretical understanding to practical, production-ready execution."}
    ]

def seed():
    db = Prisma()
    db.connect()

    print("Fetching all lessons...")
    all_lessons = db.lesson.find_many()
    
    # EXCLUDE Python Programming Fundamentals
    lessons_to_process = [l for l in all_lessons if "Python Programming Fundamentals" not in l.title]
    
    print(f"Found {len(lessons_to_process)} modules to update with domain-specific snippets.")

    for lesson in lessons_to_process:
        print(f"\\nProcessing: {lesson.title}")
        
        # Cleanup existing steps and cards
        db.flashcard.delete_many(where={"lessonId": lesson.id})
        db.lessonstep.delete_many(where={"lessonId": lesson.id})
        
        steps_to_create = []
        # Generate 30 days
        for day in range(1, 31):
            title, content, code = generate_content_for_day(day, lesson.title)
            
            s = db.lessonstep.create({
                "lessonId": lesson.id,
                "order": day,
                "title": title,
                "content": content,
                "codeSnippet": code
            })
            steps_to_create.append(s)
            
        print(f"Created 30 Domain-Specific Lesson Steps for {lesson.title}.")
        
        # Generate 150 flashcards (5 per day)
        flashcards_data = []
        for s in steps_to_create:
            cards = generate_flashcards(lesson.id, s.id, s.order, lesson.title)
            flashcards_data.extend(cards)
            
        # Insert in batches
        batch_size = 50
        for i in range(0, len(flashcards_data), batch_size):
            batch = flashcards_data[i:i+batch_size]
            db.flashcard.create_many(data=batch)
            
        print(f"Created {len(flashcards_data)} Flashcards for {lesson.title}.")

    print("\\nSUCCESS: All modules updated with domain-specific examples!")
    db.disconnect()

if __name__ == "__main__":
    seed()
