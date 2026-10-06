"""
Cybersecurity & IT Fundamentals Curriculum - Days 16 to 30
Module 3 (Cont.): Cyber Security Foundations (Days 16-19)
Module 4: Threats, Attacks & Malware (Days 20-24)
Module 5: Identity & Access Management (IAM) (Days 25-30)

Universal Standard Compliant:
- ELI5 markdown theory with beginner analogies
- Shell / Python / configuration snippets
- Daily hands-on coding or practical challenge
- Exactly 5 MCQs per day (75 total for Days 16-30)
"""

from seeder.course_blueprint import DayBlueprint

DAYS_16_TO_30 = [
    # ---------------------------------------------------------
    # Day 16: The AAA Framework (Authentication, Authorization, Accounting)
    # ---------------------------------------------------------
    DayBlueprint(
        order=16,
        title="Day 16: The AAA Framework (Authentication, Authorization, Accounting)",
        concept="Understanding the fundamental access governance architecture: Authentication (proving identity), Authorization (determining permissions), and Accounting (logging and auditing activities).",
        analogy="Think of boarding an international airplane: Authentication is showing your passport to prove you are who you claim to be. Authorization is the gate agent checking your boarding pass to confirm you sit in seat 14B instead of the cockpit. Accounting is the airline's flight manifest log recording the exact second your ticket was scanned at the gate.",
        theory_sections=[
            {
                "heading": "The Three Pillars of AAA",
                "content": (
                    "The AAA framework governs every secure access control interaction:\n\n"
                    "1. **Authentication (Who are you?)**: Verifying the declared identity of a subject using credentials (passwords, biometrics, hardware tokens, Kerberos tickets).\n"
                    "2. **Authorization (What are you allowed to do?)**: Granting or denying access to specific resources based on access policies (e.g., standard users cannot delete customer databases).\n"
                    "3. **Accounting / Auditing (What did you do?)**: Generating an immutable, timestamped record of user sessions, commands executed, and files accessed. Essential for compliance and incident investigations."
                )
            },
            {
                "heading": "Centralized AAA Protocols in Enterprise Networks",
                "content": (
                    "Enterprises do not manage user accounts on individual routers or servers. Instead, they use centralized AAA servers:\n"
                    "- **RADIUS (Remote Authentication Dial-In User Service)**: Standard for Wi-Fi access (802.1X) and VPN connections.\n"
                    "- **TACACS+ (Terminal Access Controller Access-Control System Plus)**: Cisco protocol that completely separates authentication and authorization, encrypting the entire packet payload."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Inspecting Security Audit Logs (Windows Event Viewer & Linux auth.log)",
                "language": "bash",
                "code": (
                    "# Windows PowerShell: Querying Event ID 4624 (Successful Logon) and 4625 (Failed Logon):\n"
                    "Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4625} -MaxEvents 5 | Format-List\n\n"
                    "# Linux: Inspecting authentication attempts in system logs:\n"
                    "sudo grep 'Failed password' /var/log/auth.log\n"
                    "lastlog   # Shows the most recent login timestamp for all local users"
                ),
                "explanation": "Accounting records allow security analysts to detect brute-force attacks and establish audit trails during investigations."
            },
            {
                "title": "Python: Implementing an AAA Enforcement Engine",
                "language": "python",
                "code": (
                    "import time\n\n"
                    "class AAAEngine:\n"
                    "    def __init__(self):\n"
                    "        self.users = {'alice': 'hashed_secret_123'}\n"
                    "        self.permissions = {'alice': {'read', 'write'}}\n"
                    "        self.audit_log = []\n"
                    "    \n"
                    "    def authenticate(self, user: str, password_hash: str) -> bool:\n"
                    "        return self.users.get(user) == password_hash\n"
                    "    \n"
                    "    def authorize(self, user: str, action: str) -> bool:\n"
                    "        return action in self.permissions.get(user, set())\n"
                    "    \n"
                    "    def account(self, user: str, action: str, success: bool):\n"
                    "        record = f'[{time.strftime(\"%Y-%m-%d %H:%M:%S\")}] User={user} Action={action} Success={success}'\n"
                    "        self.audit_log.append(record)\n\n"
                    "engine = AAAEngine()\n"
                    "if engine.authenticate('alice', 'hashed_secret_123'):\n"
                    "    allowed = engine.authorize('alice', 'delete')\n"
                    "    engine.account('alice', 'delete', allowed)\n"
                    "print(engine.audit_log)"
                ),
                "explanation": "Illustrates programmatic separation of concerns across authentication, authorization, and accounting."
            }
        ],
        coding_challenge={
            "description": "Write a Python function `aaa_check(credentials_valid: bool, user_role: str, action: str) -> dict` that returns a dict `{'status': 'SUCCESS' or 'DENIED', 'reason': str}`. Deny if credentials are invalid ('AUTH_FAILED'), or if action is 'DELETE' and role is not 'ADMIN' ('UNAUTHORIZED').",
            "starter_code": (
                "def aaa_check(credentials_valid: bool, user_role: str, action: str) -> dict:\n"
                "    # Return {'status': 'SUCCESS' or 'DENIED', 'reason': str}\n"
                "    return {}\n\n"
                "print(aaa_check(False, 'ADMIN', 'READ'))\n"
                "print(aaa_check(True, 'USER', 'DELETE'))\n"
                "print(aaa_check(True, 'ADMIN', 'DELETE'))"
            ),
            "solution_code": (
                "def aaa_check(credentials_valid: bool, user_role: str, action: str) -> dict:\n"
                "    if not credentials_valid:\n"
                "        return {'status': 'DENIED', 'reason': 'AUTH_FAILED'}\n"
                "    if action.upper() == 'DELETE' and user_role.upper() != 'ADMIN':\n"
                "        return {'status': 'DENIED', 'reason': 'UNAUTHORIZED'}\n"
                "    return {'status': 'SUCCESS', 'reason': 'OK'}\n\n"
                "print(aaa_check(False, 'ADMIN', 'READ'))\n"
                "print(aaa_check(True, 'USER', 'DELETE'))\n"
                "print(aaa_check(True, 'ADMIN', 'DELETE'))"
            ),
            "expected_output": "{'status': 'DENIED', 'reason': 'AUTH_FAILED'}\n{'status': 'DENIED', 'reason': 'UNAUTHORIZED'}\n{'status': 'SUCCESS', 'reason': 'OK'}"
        },
        quizzes=[
            {
                "question": "What is the critical distinction between Authentication and Authorization in the AAA framework?",
                "options": [
                    "Authentication verifies who you are; Authorization determines what resources and actions you are permitted to access",
                    "Authentication is for Windows; Authorization is for Linux",
                    "Authentication checks credit card balances; Authorization logs off users",
                    "There is no difference; they are exact synonyms"
                ],
                "correct_answer": "Authentication verifies who you are; Authorization determines what resources and actions you are permitted to access",
                "explanation": "Authentication proves a subject's identity (login credentials), while authorization checks if that authenticated subject has permission for a specific file or action."
            },
            {
                "question": "Which component of the AAA framework is directly responsible for generating timestamped audit trails of user actions and resource consumption?",
                "options": ["Accounting", "Authentication", "Authorization", "Administration"],
                "correct_answer": "Accounting",
                "explanation": "Accounting records what actions a user took, when they logged in/out, and how many resources they consumed, serving as an evidentiary log."
            },
            {
                "question": "In Windows Event Logs, what does Event ID 4625 indicate to a security analyst?",
                "options": [
                    "An account failed to log on (failed authentication)",
                    "A successful operating system update",
                    "The computer was shut down cleanly",
                    "A new printer was installed"
                ],
                "correct_answer": "An account failed to log on (failed authentication)",
                "explanation": "Event ID 4625 records failed logon events, essential for detecting password spraying and brute-force intrusion attempts."
            },
            {
                "question": "Which enterprise protocol separates Authentication and Authorization into distinct functions and encrypts the entire packet payload?",
                "options": ["TACACS+", "RADIUS", "HTTP", "Telnet"],
                "correct_answer": "TACACS+",
                "explanation": "Cisco's TACACS+ separates authentication from authorization and encrypts the entire packet body, unlike RADIUS which only encrypts the password."
            },
            {
                "question": "Why is the Accounting pillar indispensable during post-breach digital forensics?",
                "options": [
                    "Without immutable accounting logs, it is impossible to reconstruct an attacker's lateral movements, timeline, or accessed files",
                    "Accounting logs automatically erase the attacker's laptop",
                    "Accounting pays the insurance company automatically",
                    "Accounting prevents computers from overheating"
                ],
                "correct_answer": "Without immutable accounting logs, it is impossible to reconstruct an attacker's lateral movements, timeline, or accessed files",
                "explanation": "Auditable accounting logs are the primary evidence investigators use to determine breach blast radius and prove regulatory compliance."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 17: Core Terminologies: Vulnerability, Threat, Risk, Exploit
    # ---------------------------------------------------------
    DayBlueprint(
        order=17,
        title="Day 17: Core Terminologies: Vulnerability, Threat, Risk, Exploit",
        concept="Dissecting the four core terminology pillars of cybersecurity risk management: Vulnerability (weakness), Threat (danger), Exploit (weapon), and Risk (probability times impact).",
        analogy="Think of a home: A wooden front door with a broken lock is a **Vulnerability** (a weakness). A burglar lurking down the street looking for houses to rob is a **Threat** (a potential danger). A crowbar custom-shaped to pry open that broken lock is an **Exploit** (the tool/mechanism). The likelihood of being robbed and losing $10,000 worth of jewelry is the **Risk**.",
        theory_sections=[
            {
                "heading": "The Fundamental Cybersecurity Equation",
                "content": (
                    "Security professionals use exact terminology to quantify risk:\n\n"
                    "1. **Vulnerability**: A flaw or weakness in software code, hardware design, or system configuration that could be exploited (e.g., unpatched software, weak password, open firewall port). Cataloged via **CVE (Common Vulnerabilities and Exposures)** IDs.\n"
                    "2. **Threat**: Any circumstance or entity with the potential to adversely impact an asset through unauthorized access, destruction, or denial of service. The actor causing the threat is a **Threat Actor**.\n"
                    "3. **Exploit**: A piece of software, script, payload, or sequence of commands that takes advantage of a specific vulnerability to compromise a system.\n"
                    "4. **Risk**: The financial or operational loss resulting from the combination of the likelihood of a threat exploiting a vulnerability and the severity of impact:\n"
                    "   `Risk = Likelihood x Impact`"
                )
            },
            {
                "heading": "Understanding CVSS (Common Vulnerability Scoring System)",
                "content": (
                    "The **CVSS score** is an open industry standard ranking vulnerability severity from 0.0 to 10.0:\n"
                    "- Low: 0.1 - 3.9\n"
                    "- Medium: 4.0 - 6.9\n"
                    "- High: 7.0 - 8.9\n"
                    "- Critical: 9.0 - 10.0 (e.g., Log4Shell, EternalBlue; allows remote unauthenticated root access)."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Searching the National Vulnerability Database (NVD) via cURL",
                "language": "bash",
                "code": (
                    "# Querying NVD API for critical CVEs matching a keyword:\n"
                    "curl -s \"https://services.nvd.nist.gov/rest/json/cves/2.0?keywordSearch=OpenSSL\" | jq '.vulnerabilities[0].cve.id'\n\n"
                    "# Inspecting CVE severity score:\n"
                    "# CVE-2021-44228 (Log4j): CVSS Base Score: 10.0 (CRITICAL)"
                ),
                "explanation": "Security teams automate API queries against vulnerability databases to discover newly published CVEs impacting their tech stack."
            },
            {
                "title": "Python: Calculating Risk Matrix Scores",
                "language": "python",
                "code": (
                    "def calculate_risk(likelihood: int, impact: int) -> dict:\n"
                    "    # Likelihood and Impact on 1 to 5 scale\n"
                    "    score = likelihood * impact\n"
                    "    level = 'LOW'\n"
                    "    if score >= 15:\n"
                    "        level = 'CRITICAL'\n"
                    "    elif score >= 10:\n"
                    "        level = 'HIGH'\n"
                    "    elif score >= 5:\n"
                    "        level = 'MEDIUM'\n"
                    "    return {'score': score, 'risk_level': level}\n\n"
                    "print(calculate_risk(likelihood=5, impact=4)) # e.g. Public unpatched RCE\n"
                    "print(calculate_risk(likelihood=1, impact=2)) # e.g. Obscure lab server"
                ),
                "explanation": "Standard risk quantification formula prioritizing remediation tickets based on risk score rather than theoretical flaw existence alone."
            }
        ],
        coding_challenge={
            "description": "Write a Python function `categorize_cvss(score: float) -> str` that returns 'NONE' if score == 0.0, 'LOW' if 0.1 <= score <= 3.9, 'MEDIUM' if 4.0 <= score <= 6.9, 'HIGH' if 7.0 <= score <= 8.9, and 'CRITICAL' if 9.0 <= score <= 10.0.",
            "starter_code": (
                "def categorize_cvss(score: float) -> str:\n"
                "    # Return 'NONE', 'LOW', 'MEDIUM', 'HIGH', or 'CRITICAL'\n"
                "    return ''\n\n"
                "print(categorize_cvss(9.8))\n"
                "print(categorize_cvss(5.3))\n"
                "print(categorize_cvss(2.1))"
            ),
            "solution_code": (
                "def categorize_cvss(score: float) -> str:\n"
                "    if score == 0.0:\n"
                "        return 'NONE'\n"
                "    elif 0.1 <= score <= 3.9:\n"
                "        return 'LOW'\n"
                "    elif 4.0 <= score <= 6.9:\n"
                "        return 'MEDIUM'\n"
                "    elif 7.0 <= score <= 8.9:\n"
                "        return 'HIGH'\n"
                "    elif 9.0 <= score <= 10.0:\n"
                "        return 'CRITICAL'\n"
                "    return 'INVALID'\n\n"
                "print(categorize_cvss(9.8))\n"
                "print(categorize_cvss(5.3))\n"
                "print(categorize_cvss(2.1))"
            ),
            "expected_output": "CRITICAL\nMEDIUM\nLOW"
        },
        quizzes=[
            {
                "question": "What is a 'Vulnerability' in cybersecurity terminology?",
                "options": [
                    "A flaw, bug, or weakness in a system or design that could be accidentally or maliciously exploited",
                    "A hacker sitting in a coffee shop",
                    "A malicious software program like ransomware",
                    "The physical computer keyboard"
                ],
                "correct_answer": "A flaw, bug, or weakness in a system or design that could be accidentally or maliciously exploited",
                "explanation": "A vulnerability is an inherent flaw (e.g., missing input validation in code, unpatched server) that creates a security exposure."
            },
            {
                "question": "What is the difference between a Vulnerability and an Exploit?",
                "options": [
                    "A vulnerability is the underlying weakness; an exploit is the actual code or technique designed to take advantage of that weakness",
                    "An exploit is a legal contract; a vulnerability is a computer brand",
                    "There is no difference; both mean a computer virus",
                    "Vulnerabilities only exist on smartphones, while exploits only exist on servers"
                ],
                "correct_answer": "A vulnerability is the underlying weakness; an exploit is the actual code or technique designed to take advantage of that weakness",
                "explanation": "The vulnerability is the hole in the armor; the exploit is the weapon specifically forged to strike through that hole."
            },
            {
                "question": "In security risk assessment formulas, how is 'Risk' calculated?",
                "options": [
                    "Risk = Likelihood x Impact",
                    "Risk = CPU Speed / RAM Size",
                    "Risk = Number of Employees + Firewalls",
                    "Risk = Total Hard Drive Megabytes"
                ],
                "correct_answer": "Risk = Likelihood x Impact",
                "explanation": "Risk represents the probability of a threat exploiting a vulnerability multiplied by the resulting business or financial harm (impact)."
            },
            {
                "question": "What does a CVSS Base Score of 9.8 indicate about a newly discovered software vulnerability?",
                "options": [
                    "It is a CRITICAL vulnerability that allows severe compromise (e.g., remote code execution without user interaction)",
                    "It is completely harmless and can be ignored",
                    "The vulnerability only impacts printer paper",
                    "The computer needs to be thrown in the trash"
                ],
                "correct_answer": "It is a CRITICAL vulnerability that allows severe compromise (e.g., remote code execution without user interaction)",
                "explanation": "CVSS scores between 9.0 and 10.0 are classified as Critical, typically representing unauthenticated remote code execution or data exposure."
            },
            {
                "question": "What is a 'Zero-Day' vulnerability?",
                "options": [
                    "A software security flaw unknown to the vendor, meaning zero days of patches or defenses currently exist to protect against it",
                    "A virus that deletes itself after zero minutes",
                    "A computer manufactured on the first day of the year",
                    "A free trial of antivirus software"
                ],
                "correct_answer": "A software security flaw unknown to the vendor, meaning zero days of patches or defenses currently exist to protect against it",
                "explanation": "A Zero-Day is unknown to the software developer, meaning threat actors can exploit it freely until discovered and patched."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 18: Types of Hackers (White Hat, Black Hat, Gray Hat)
    # ---------------------------------------------------------
    DayBlueprint(
        order=18,
        title="Day 18: Types of Hackers (White Hat, Black Hat, Gray Hat)",
        concept="Classifying hacker profiles based on legality, intent, and authorization: White Hat (ethical penetration testers), Black Hat (criminal cyber adversaries), and Gray Hat (unauthorized bug hunters who disclose responsibly).",
        analogy="Think of locksmiths: A White Hat is a certified locksmith hired by a homeowner to test if their front door can be picked, submitting a written report. A Black Hat is a burglar who picks the lock at midnight to steal the television. A Gray Hat picks the lock uninvited, leaves a note on the kitchen counter saying 'Your lock is broken, pay me $50 to fix it', and leaves without stealing anything.",
        theory_sections=[
            {
                "heading": "Hacker Hat Classifications",
                "content": (
                    "The term 'hacker' originated as an expert who creatively solves technical problems. In modern cybersecurity, hackers are categorized by motivation and legal permission:\n\n"
                    "1. **White Hat (Ethical Hackers)**: Work with explicit, written legal authorization. They perform penetration testing, vulnerability assessments, and red teaming to find and fix bugs before adversaries exploit them.\n"
                    "2. **Black Hat (Malicious Hackers / Cybercriminals)**: Operate illegally without authorization. Driven by financial theft, industrial espionage, extortion (ransomware), or political sabotage.\n"
                    "3. **Gray Hat**: Hack into systems without prior authorization, but without malicious intent to steal or destroy data. They often disclose vulnerabilities to the target company (or publicly if ignored), though their actions remain legally questionable."
                )
            },
            {
                "heading": "Rules of Engagement & Bug Bounty Programs",
                "content": (
                    "Ethical hackers operate under strict **Rules of Engagement (RoE)** and Scope definitions. Organizations run **Bug Bounty Programs** (via platforms like HackerOne and Bugcrowd), providing safe harbor and cash rewards to researchers who discover and responsibly disclose security flaws."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Inspecting a Security.txt Responsible Disclosure Policy",
                "language": "bash",
                "code": (
                    "# Most major companies publish an RFC 9116 security.txt file:\n"
                    "curl -s https://www.google.com/.well-known/security.txt\n\n"
                    "# Expected content:\n"
                    "# Contact: https://g.co/vulnz\n"
                    "# Encryption: https://services.google.com/html/contact/security-key.asc\n"
                    "# Policy: https://bughunters.google.com/about/rules"
                ),
                "explanation": "RFC 9116 security.txt files inform ethical security researchers how to legally report vulnerabilities without facing lawsuits."
            },
            {
                "title": "Python: Auditing URL Target Scope for Penetration Testing",
                "language": "python",
                "code": (
                    "import urllib.parse\n\n"
                    "def is_target_in_scope(target_url: str, authorized_domains: list) -> bool:\n"
                    "    parsed = urllib.parse.urlparse(target_url)\n"
                    "    hostname = parsed.hostname or ''\n"
                    "    for domain in authorized_domains:\n"
                    "        if hostname == domain or hostname.endswith('.' + domain):\n"
                    "            return True\n"
                    "    return False\n\n"
                    "scope = ['tesla.com', 'shop.tesla.com']\n"
                    "print('In Scope:', is_target_in_scope('https://shop.tesla.com/login', scope))\n"
                    "print('In Scope:', is_target_in_scope('https://third-party-billing.com', scope))"
                ),
                "explanation": "Ethical hackers strictly verify testing scope boundaries to avoid accidental illegal penetration testing of unauthorized third parties."
            }
        ],
        coding_challenge={
            "description": "Write a Python function `classify_hacker(has_authorization: bool, malicious_intent: bool) -> str` that returns 'WHITE_HAT' if authorized and not malicious, 'BLACK_HAT' if not authorized and malicious, 'GRAY_HAT' if not authorized and not malicious, and 'ROGUE_INSIDER' if authorized and malicious.",
            "starter_code": (
                "def classify_hacker(has_authorization: bool, malicious_intent: bool) -> str:\n"
                "    # Return 'WHITE_HAT', 'BLACK_HAT', 'GRAY_HAT', or 'ROGUE_INSIDER'\n"
                "    return ''\n\n"
                "print(classify_hacker(True, False))\n"
                "print(classify_hacker(False, True))\n"
                "print(classify_hacker(False, False))"
            ),
            "solution_code": (
                "def classify_hacker(has_authorization: bool, malicious_intent: bool) -> str:\n"
                "    if has_authorization and not malicious_intent:\n"
                "        return 'WHITE_HAT'\n"
                "    if not has_authorization and malicious_intent:\n"
                "        return 'BLACK_HAT'\n"
                "    if not has_authorization and not malicious_intent:\n"
                "        return 'GRAY_HAT'\n"
                "    return 'ROGUE_INSIDER'\n\n"
                "print(classify_hacker(True, False))\n"
                "print(classify_hacker(False, True))\n"
                "print(classify_hacker(False, False))"
            ),
            "expected_output": "WHITE_HAT\nBLACK_HAT\nGRAY_HAT"
        },
        quizzes=[
            {
                "question": "What is the single most critical legal factor that separates a White Hat ethical hacker from a Black Hat cybercriminal?",
                "options": [
                    "Written authorization and permission from the system owner prior to testing",
                    "The programming language they use to write exploits",
                    "Whether they use Windows or Linux",
                    "The color of clothing they wear"
                ],
                "correct_answer": "Written authorization and permission from the system owner prior to testing",
                "explanation": "Ethical hacking requires explicit, written legal authorization (Scope / Rules of Engagement). Hacking without permission violates computer crime laws."
            },
            {
                "question": "What defines a 'Gray Hat' hacker?",
                "options": [
                    "Someone who hacks into systems without authorization, but does not steal or destroy data, often disclosing the flaw to the owner",
                    "A retired hacker who no longer uses computers",
                    "An FBI cyber agent undercover in criminal forums",
                    "A hacker who only works during winter"
                ],
                "correct_answer": "Someone who hacks into systems without authorization, but does not steal or destroy data, often disclosing the flaw to the owner",
                "explanation": "Gray hats cross legal boundaries by hacking without permission, but their underlying intent is disclosure rather than theft or extortion."
            },
            {
                "question": "What is a 'Bug Bounty Program'?",
                "options": [
                    "A formal program managed by organizations offering financial rewards and legal safe harbor to ethical hackers for discovering and responsibly reporting bugs",
                    "An extermination service for office termites",
                    "A software tool that deletes computer files",
                    "A fine issued by the police for downloading music"
                ],
                "correct_answer": "A formal program managed by organizations offering financial rewards and legal safe harbor to ethical hackers for discovering and responsibly reporting bugs",
                "explanation": "Companies like Google, Apple, and banks invite ethical researchers to test their systems, paying bounties (often $500 to $100,000+) for valid vulnerability disclosures."
            },
            {
                "question": "What is the role of a 'Red Team' in enterprise security?",
                "options": [
                    "An internal or external offensive security team simulating realistic adversary attacks to test the organization's defenses",
                    "The team that writes marketing emails",
                    "The IT support desk that resets lost user passwords",
                    "The human resources department"
                ],
                "correct_answer": "An internal or external offensive security team simulating realistic adversary attacks to test the organization's defenses",
                "explanation": "Red Teams act as real-world adversaries to test people, processes, and technology, while the Blue Team defends the organization."
            },
            {
                "question": "What standard web file is hosted at `/.well-known/security.txt` on modern domains?",
                "options": [
                    "A standardized document informing security researchers how and where to report security vulnerabilities responsibly",
                    "A list of all company passwords",
                    "A virus scanner that runs inside Google Chrome",
                    "The website's advertising terms and conditions"
                ],
                "correct_answer": "A standardized document informing security researchers how and where to report security vulnerabilities responsibly",
                "explanation": "RFC 9116 establishes `security.txt` as the standard discovery mechanism for vulnerability disclosure contact information."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 19: Hacktivists, Script Kiddies, and Advanced Persistent Threats (APTs)
    # ---------------------------------------------------------
    DayBlueprint(
        order=19,
        title="Day 19: Hacktivists, Script Kiddies, and Advanced Persistent Threats (APTs)",
        concept="Analyzing threat actor taxonomy: Script Kiddies (low skill, automated tools), Hacktivists (politically motivated), Insiders (authorized employees), and Nation-State APTs (sophisticated, persistent, state-sponsored).",
        analogy="Think of military threats: A Script Kiddie is a kid throwing firecrackers in an alley using a store-bought lighter. A Hacktivist is a protest crowd painting political slogans on the city hall wall. An Insider Threat is a trusted guard opening the back door for a friend. An APT (Advanced Persistent Threat) is a stealth foreign military intelligence agency digging a secret tunnel into a nuclear facility over two years.",
        theory_sections=[
            {
                "heading": "Threat Actor Profiles and Motivations",
                "content": (
                    "Understanding *who* is attacking and *why* shapes incident response:\n\n"
                    "1. **Script Kiddies**: Low-skilled amateurs who download automated point-and-click exploit tools (e.g., LOIC, SQLmap) written by others. Motivated by bragging rights or curiosity. High volume, low sophistication.\n"
                    "2. **Hacktivists (e.g., Anonymous)**: Driven by political, ideological, religious, or environmental activism. Tactics: Website defacements, DDoS campaigns, and publishing leaked executive emails.\n"
                    "3. **Cybercriminals (Organized Crime)**: Highly organized syndicates running Ransomware-as-a-Service (RaaS) operations. Solely motivated by monetary extortion and wire fraud.\n"
                    "4. **Insider Threats**: Current or former employees, contractors, or business partners with legitimate access who misuse their privileges (maliciously or through negligence).\n"
                    "5. **APTs (Advanced Persistent Threats)**: Nation-state intelligence agencies or heavily funded military cyber units (e.g., Fancy Bear / APT28, Lazarus Group). Characteristics: Zero-day exploits, multi-year stealth persistence, supply chain compromises."
                )
            },
            {
                "heading": "The MITRE ATT&CK Framework",
                "content": (
                    "Security teams map threat actor behaviors using the **MITRE ATT&CK Matrix**, cataloging adversary Tactics, Techniques, and Procedures (TTPs) across the intrusion lifecycle (Reconnaissance -> Initial Access -> Lateral Movement -> Exfiltration)."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Mapping Known APT Groups and Nation-State Identifiers",
                "language": "bash",
                "code": (
                    "# Well-known Nation-State APT Groups tracked globally:\n"
                    "# APT28 / Fancy Bear (Russia - GRU): NotPetya, DNC breach\n"
                    "# APT38 / Lazarus Group (North Korea): WannaCry, Sony Pictures, Axie Infinity theft\n"
                    "# APT41 / Double Dragon (China): Healthcare & telecom espionage, supply chain backdoors\n"
                    "# APT33 / Elfin (Iran): Aerospace and energy sector wiper malware (Shamoon)"
                ),
                "explanation": "Threat intelligence feeds use standard APT designations to attribute cyber campaigns to specific state entities."
            },
            {
                "title": "Python: Classifying Threat Actor by Signature Indicators",
                "language": "python",
                "code": (
                    "def classify_threat_actor(indicators: dict) -> str:\n"
                    "    if indicators.get('uses_custom_zero_days') and indicators.get('dwell_time_months', 0) > 6:\n"
                    "        return 'APT (Advanced Persistent Threat) / Nation-State'\n"
                    "    if indicators.get('demands_crypto_ransom'):\n"
                    "        return 'Organized Cybercrime Syndicate'\n"
                    "    if indicators.get('public_political_defacement'):\n"
                    "        return 'Hacktivist'\n"
                    "    if indicators.get('uses_canned_scripts_only'):\n"
                    "        return 'Script Kiddie'\n"
                    "    return 'General Threat Actor'\n\n"
                    "print(classify_threat_actor({'uses_custom_zero_days': True, 'dwell_time_months': 14}))\n"
                    "print(classify_threat_actor({'demands_crypto_ransom': True}))"
                ),
                "explanation": "Threat intelligence triage logic mapping behavioral tactics to adversary categories."
            }
        ],
        coding_challenge={
            "description": "Write a Python function `triage_threat_level(actor_type: str) -> int` that maps 'SCRIPT_KIDDIE' -> 1, 'HACKTIVIST' -> 2, 'INSIDER' -> 3, 'CYBERCRIME' -> 4, and 'APT' -> 5. Return 0 for any unknown actor.",
            "starter_code": (
                "def triage_threat_level(actor_type: str) -> int:\n"
                "    # Return integer threat level 0 to 5\n"
                "    return 0\n\n"
                "print(triage_threat_level('APT'))\n"
                "print(triage_threat_level('SCRIPT_KIDDIE'))"
            ),
            "solution_code": (
                "def triage_threat_level(actor_type: str) -> int:\n"
                "    levels = {\n"
                "        'SCRIPT_KIDDIE': 1,\n"
                "        'HACKTIVIST': 2,\n"
                "        'INSIDER': 3,\n"
                "        'CYBERCRIME': 4,\n"
                "        'APT': 5\n"
                "    }\n"
                "    return levels.get(actor_type.upper(), 0)\n\n"
                "print(triage_threat_level('APT'))\n"
                "print(triage_threat_level('SCRIPT_KIDDIE'))"
            ),
            "expected_output": "5\n1"
        },
        quizzes=[
            {
                "question": "What distinguishes an Advanced Persistent Threat (APT) from a standard cybercriminal or script kiddie?",
                "options": [
                    "APTs are typically nation-state sponsored, possessing immense resources, custom zero-day exploits, and the ability to maintain undetected persistence for months or years",
                    "APTs only attack personal gaming consoles",
                    "APTs do not use computers",
                    "APTs always send paper letters in the mail before attacking"
                ],
                "correct_answer": "APTs are typically nation-state sponsored, possessing immense resources, custom zero-day exploits, and the ability to maintain undetected persistence for months or years",
                "explanation": "APTs are sophisticated state-sponsored intelligence units targeting defense, energy, and government sectors with long-term strategic espionage goals."
            },
            {
                "question": "What is a 'Script Kiddie'?",
                "options": [
                    "A low-skilled individual who executes pre-packaged, automated attack tools and scripts written by others without understanding how they work",
                    "A child who teaches computer programming classes",
                    "A software engineer who writes shell scripts for Linux",
                    "A technician who repairs broken monitors"
                ],
                "correct_answer": "A low-skilled individual who executes pre-packaged, automated attack tools and scripts written by others without understanding how they work",
                "explanation": "Script kiddies rely entirely on existing publicly available tools (like LOIC, DDoS botnets) for notoriety or disruption without deep technical skills."
            },
            {
                "question": "What is the primary motivation driving 'Hacktivist' groups such as Anonymous?",
                "options": [
                    "Promoting political, social, or ideological causes through website defacements, data leaks, and service disruption",
                    "Stealing credit cards for personal luxury shopping",
                    "Mining cryptocurrency on university servers",
                    "Selling computer hardware to schools"
                ],
                "correct_answer": "Promoting political, social, or ideological causes through website defacements, data leaks, and service disruption",
                "explanation": "Hacktivists use hacking as a form of civil disobedience and protest against governments, corporations, or human rights violations."
            },
            {
                "question": "Why are 'Insider Threats' (current or former employees) considered among the most dangerous security risks?",
                "options": [
                    "They already possess legitimate credentials, authorized physical access, and intimate knowledge of where valuable corporate data is stored",
                    "They cannot be prosecuted under the law",
                    "They have faster internet access at home",
                    "They are immune to computer viruses"
                ],
                "correct_answer": "They already possess legitimate credentials, authorized physical access, and intimate knowledge of where valuable corporate data is stored",
                "explanation": "Insiders bypass perimeter defenses because they already hold legitimate access rights and understand internal audit blind spots."
            },
            {
                "question": "What industry-standard knowledge base maps threat actor Tactics, Techniques, and Procedures (TTPs) across the entire cyber attack lifecycle?",
                "options": ["The MITRE ATT&CK Framework", "The Wikipedia Security Portal", "The IEEE Standard 802.11", "The Apache License 2.0"],
                "correct_answer": "The MITRE ATT&CK Framework",
                "explanation": "MITRE ATT&CK is the globally recognized matrix documenting real-world adversary behavioral techniques used by defenders to improve detection."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 20: Virus, Worms, Trojans & Logic Bombs
    # ---------------------------------------------------------
    DayBlueprint(
        order=20,
        title="Day 20: Virus, Worms, Trojans & Logic Bombs",
        concept="Differentiating between foundational malware categories based on infection vectors and propagation mechanisms: Viruses (requires user execution and file host), Worms (self-propagating across networks), Trojans (disguised as benign software), and Logic Bombs (time/condition-triggered payloads).",
        analogy="Think of bio-weapons and covert attacks: A Virus is a parasite that cannot move on its own; someone has to carry the infected apple to a party and take a bite. A Worm is a swarm of airborne locusts that flies across the city independently, entering every open window. A Trojan is the legendary Trojan Horse—a beautiful gift brought inside the castle walls that disgorges enemy soldiers at midnight. A Logic Bomb is a time bomb hidden in the basement set to detonate on the boss's birthday.",
        theory_sections=[
            {
                "heading": "Anatomy of Core Malware Types",
                "content": (
                    "Malware ('Malicious Software') is umbrella terminology for hostile code:\n\n"
                    "1. **Virus**: Attaches its malicious code to a legitimate host program or document (.exe, .docx macro). It **CANNOT spread without human interaction** (e.g., a user double-clicking an email attachment or launching an infected file).\n"
                    "2. **Worm**: Self-replicating and self-propagating. It **requires NO human interaction**. Worms exploit network protocol vulnerabilities to scan subnets and autonomously infect thousands of machines within minutes (e.g., Morris Worm, Blaster, Conficker).\n"
                    "3. **Trojan Horse**: Disguises itself as legitimate, useful software (e.g., a free game, cracked Photoshop, fake PDF invoice). Once executed by the victim, it deploys a covert backdoor or keylogger.\n"
                    "4. **Logic Bomb**: Malicious instructions embedded silently inside software that remain dormant until triggered by a specific condition (e.g., a specific calendar date, or when an administrator's user ID is deleted from HR payroll)."
                )
            },
            {
                "heading": "Historical Case Study: Stuxnet",
                "content": (
                    "Stuxnet (discovered 2010) was the world's first true cyber physical weapon. Combining a worm (propagating via 4 zero-days and USB drives) with a PLC rootkit, it silently manipulated Iran's uranium enrichment centrifuges to spin out of control while reporting normal status readings to operators."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Detecting Malicious Word Macros and Suspicious Process Lineage",
                "language": "bash",
                "code": (
                    "# Attack lineage: Microsoft Word spawning cmd.exe or powershell.exe:\n"
                    "# Legitimate: WINWORD.EXE -> (none)\n"
                    "# Malware:    WINWORD.EXE -> cmd.exe -> powershell.exe -Enc BAB4...\n\n"
                    "# Windows PowerShell command to detect suspicious office child processes:\n"
                    "Get-CimInstance Win32_Process | Where-Object {$_.ParentProcessId -in (Get-Process winword).Id}"
                ),
                "explanation": "Word documents launching command shells is the classic signature of macro-based Trojan dropper infections."
            },
            {
                "title": "Python: Demonstrating a Benign Logic Bomb Condition Trigger",
                "language": "python",
                "code": (
                    "import datetime\n\n"
                    "def logic_bomb_payload():\n"
                    "    return 'MALICIOUS_PAYLOAD_DETONATED: Core database files compromised!'\n\n"
                    "def execute_software(trigger_date: datetime.date):\n"
                    "    today = datetime.date.today()\n"
                    "    # Logic bomb waits for specific date before activating payload\n"
                    "    if today >= trigger_date:\n"
                    "        return logic_bomb_payload()\n"
                    "    return 'Normal software execution: Payroll processed smoothly.'\n\n"
                    "print(execute_software(datetime.date(2020, 1, 1)))\n"
                    "print(execute_software(datetime.date(2099, 1, 1)))"
                ),
                "explanation": "Demonstrates how logic bomb payloads remain dormant in codebases to evade short-term sandbox detonation tests."
            }
        ],
        coding_challenge={
            "description": "Write a Python function `classify_malware(requires_host_file: bool, self_propagates_over_network: bool, user_execution_required: bool) -> str` that returns 'WORM' if it self-propagates and requires no user execution, 'VIRUS' if it requires a host file and user execution, 'TROJAN' if no self-propagation and user execution without host attachment, and 'UNKNOWN' otherwise.",
            "starter_code": (
                "def classify_malware(requires_host_file: bool, self_propagates_over_network: bool, user_execution_required: bool) -> str:\n"
                "    # Return 'WORM', 'VIRUS', 'TROJAN', or 'UNKNOWN'\n"
                "    return ''\n\n"
                "print(classify_malware(False, True, False))\n"
                "print(classify_malware(True, False, True))"
            ),
            "solution_code": (
                "def classify_malware(requires_host_file: bool, self_propagates_over_network: bool, user_execution_required: bool) -> str:\n"
                "    if self_propagates_over_network and not user_execution_required:\n"
                "        return 'WORM'\n"
                "    if requires_host_file and user_execution_required and not self_propagates_over_network:\n"
                "        return 'VIRUS'\n"
                "    if not requires_host_file and not self_propagates_over_network and user_execution_required:\n"
                "        return 'TROJAN'\n"
                "    return 'UNKNOWN'\n\n"
                "print(classify_malware(False, True, False))\n"
                "print(classify_malware(True, False, True))"
            ),
            "expected_output": "WORM\nVIRUS"
        },
        quizzes=[
            {
                "question": "What is the primary difference between a Computer Virus and a Computer Worm?",
                "options": [
                    "A virus requires a host program and user execution to spread, whereas a worm self-replicates across networks autonomously without user intervention",
                    "A virus is hardware, while a worm is software",
                    "A worm only affects Apple Mac computers",
                    "A virus can be cured with medicine"
                ],
                "correct_answer": "A virus requires a host program and user execution to spread, whereas a worm self-replicates across networks autonomously without user intervention",
                "explanation": "Worms propagate automatically by scanning network ports and exploiting services, while viruses require a human to run the infected file."
            },
            {
                "question": "An email arrives with what looks like a harmless PDF invoice or free game, but running it secretly installs a remote backdoor. What type of malware is this?",
                "options": ["Trojan Horse", "Worm", "Logic Bomb", "Rootkit"],
                "correct_answer": "Trojan Horse",
                "explanation": "Trojans disguise their true malicious functionality behind a seemingly desirable, harmless facade to trick users into executing them."
            },
            {
                "question": "What is a 'Logic Bomb'?",
                "options": [
                    "Malicious code planted silently in a system that executes only when a specific trigger condition (such as a calendar date or employee termination) is met",
                    "A computer algorithm that solves math equations",
                    "An explosive detonator placed inside a power supply",
                    "A device that boosts Wi-Fi signal"
                ],
                "correct_answer": "Malicious code planted silently in a system that executes only when a specific trigger condition (such as a calendar date or employee termination) is met",
                "explanation": "Logic bombs lie dormant until specific parameters (e.g., Friday the 13th, or absence of an admin's account) trigger the payload."
            },
            {
                "question": "Which historic cyber weapon famously infected Iranian nuclear facilities by autonomously propagating via USB drives and manipulating industrial centrifuges?",
                "options": ["Stuxnet", "ILOVEYOU", "Conficker", "Melissa"],
                "correct_answer": "Stuxnet",
                "explanation": "Stuxnet was a military-grade cyber weapon designed to bridge air-gapped networks and sabotage Siemens programmable logic controllers (PLCs)."
            },
            {
                "question": "Why do security systems flag Word documents that attempt to spawn `cmd.exe` or `powershell.exe`?",
                "options": [
                    "Word processing documents should never legitimately launch administrative command shells; this behavior indicates a malicious macro dropper",
                    "Command prompt cannot read English text",
                    "Microsoft Word is incompatible with Windows",
                    "PowerShell uses too much monitor brightness"
                ],
                "correct_answer": "Word processing documents should never legitimately launch administrative command shells; this behavior indicates a malicious macro dropper",
                "explanation": "Office macros executing shell binaries is the hallmark signature of Trojan droppers delivering ransomware or Cobalt Strike beacons."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 21: Ransomware, Crypto-malware, Spyware, Adware, & Rootkits
    # ---------------------------------------------------------
    DayBlueprint(
        order=21,
        title="Day 21: Ransomware, Crypto-malware, Spyware, Adware, & Rootkits",
        concept="Analyzing modern high-impact malware strains: Ransomware (extortion via military-grade encryption), Spyware (covert monitoring), Adware (unwanted marketing monetization), and Rootkits (kernel-level stealth concealment).",
        analogy="Think of different home intruders: Ransomware is a burglar who puts titanium padlocks on your refrigerator and safe, demanding $5,000 cash for the combination. Spyware is a spy hiding in your closet bugging your phone calls. Adware is an annoying salesperson who papers your living room walls with billboard flyers every 10 seconds. A Rootkit is a ghost that rewrites the security camera footage so guards see an empty hallway while the ghost roams freely.",
        theory_sections=[
            {
                "heading": "Modern Specialized Malware Taxonomy",
                "content": (
                    "Malware has evolved from simple vandalism into a multi-billion dollar criminal industry:\n\n"
                    "1. **Ransomware**: Encrypts victim user documents, databases, and operating systems using asymmetric/symmetric cryptography (AES-256 + RSA-4096), deleting local Volume Shadow Copies. Operators demand cryptocurrency for decryption keys.\n"
                    "2. **Double / Triple Extortion**: In modern ransomware, attackers exfiltrate gigabytes of confidential data BEFORE encrypting systems. If the victim restores from backups, attackers threaten to publish the stolen records on the Dark Web.\n"
                    "3. **Spyware & Keyloggers**: Secretly monitors keystrokes, webcam feeds, clipboard copies, and microphone audio, exfiltrating credentials to Command and Control (C2) servers (e.g., Pegasus spyware).\n"
                    "4. **Rootkits**: Installs deep inside the OS kernel (Ring 0) or hypervisor. Hooks system APIs to hide its own files, processes, and network connections from task managers and antivirus scanners."
                )
            },
            {
                "heading": "Why Ransomware Deletes Volume Shadow Copies",
                "content": (
                    "Upon infection, Windows ransomware scripts immediately run:\n"
                    "`vssadmin.exe delete shadows /all /quiet`\n"
                    "This permanently destroys local Windows restore points, preventing victims from easily clicking 'Previous Versions' to restore encrypted files without paying."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Ransomware Telltale Execution Commands and Detection",
                "language": "bash",
                "code": (
                    "# Classic ransomware pre-encryption commands caught by EDR:\n"
                    "# 1. Delete volume shadow backups:\n"
                    "vssadmin.exe delete shadows /all /quiet\n"
                    "# 2. Disable Windows recovery startup error handling:\n"
                    "bcdedit.exe /set {default} bootstatuspolicy ignoreallfailures\n"
                    "bcdedit.exe /set {default} recoveryenabled no\n"
                    "# 3. Clear system event logs to hamper forensics:\n"
                    "wevtutil.exe cl Security"
                ),
                "explanation": "These exact process arguments immediately trigger high-priority alerts in Endpoint Detection & Response (EDR) agents."
            },
            {
                "title": "Python: Simulating Ransomware vs Benign File Access (Canary Files)",
                "language": "python",
                "code": (
                    "import os\n\n"
                    "class RansomwareCanary:\n"
                    "    def __init__(self, canary_path: str):\n"
                    "        self.canary_path = canary_path\n"
                    "        with open(canary_path, 'w') as f:\n"
                    "            f.write('CANARY_TRIPWIRE_DATA_DO_NOT_MODIFY')\n"
                    "    \n"
                    "    def check_for_ransomware(self) -> bool:\n"
                    "        with open(self.canary_path, 'r') as f:\n"
                    "            content = f.read()\n"
                    "        # If encrypted by ransomware, raw string will be mangled/ciphertext\n"
                    "        if content != 'CANARY_TRIPWIRE_DATA_DO_NOT_MODIFY':\n"
                    "            print('[ALERT] CANARY MODIFIED! ISOLATING HOST FROM NETWORK!')\n"
                    "            return True\n"
                    "        return False\n\n"
                    "canary = RansomwareCanary('canary_document.docx')\n"
                    "print('Ransomware Detected:', canary.check_for_ransomware())"
                ),
                "explanation": "Canary trap files allow defensive agents to detect bulk encryption in progress and sever network interfaces immediately."
            }
        ],
        coding_challenge={
            "description": "Write a Python function `detect_ransomware_behavior(process_args: list) -> bool` that returns True if any command argument contains 'delete shadows' or 'recoveryenabled no', otherwise False.",
            "starter_code": (
                "def detect_ransomware_behavior(process_args: list) -> bool:\n"
                "    # Return True if ransomware indicators match\n"
                "    return False\n\n"
                "print(detect_ransomware_behavior(['vssadmin.exe', 'delete', 'shadows', '/all']))\n"
                "print(detect_ransomware_behavior(['notepad.exe', 'my_notes.txt']))"
            ),
            "solution_code": (
                "def detect_ransomware_behavior(process_args: list) -> bool:\n"
                "    joined = ' '.join(process_args).lower()\n"
                "    signatures = ['delete shadows', 'recoveryenabled no', 'wevtutil.exe cl']\n"
                "    for sig in signatures:\n"
                "        if sig in joined:\n"
                "            return True\n"
                "    return False\n\n"
                "print(detect_ransomware_behavior(['vssadmin.exe', 'delete', 'shadows', '/all']))\n"
                "print(detect_ransomware_behavior(['notepad.exe', 'my_notes.txt']))"
            ),
            "expected_output": "True\nFalse"
        },
        quizzes=[
            {
                "question": "What is the primary operational objective of Ransomware malware?",
                "options": [
                    "To encrypt the victim's critical files using strong cryptography and demand financial payment (usually cryptocurrency) in exchange for decryption keys",
                    "To clean the computer's temporary folder",
                    "To make the computer monitor display bright colors",
                    "To send holiday greeting cards to company contacts"
                ],
                "correct_answer": "To encrypt the victim's critical files using strong cryptography and demand financial payment (usually cryptocurrency) in exchange for decryption keys",
                "explanation": "Ransomware holds victim data hostage using encryption algorithms like AES and RSA, demanding ransom payments."
            },
            {
                "question": "What does 'Double Extortion' mean in modern ransomware campaigns?",
                "options": [
                    "Attackers steal confidential corporate data before encrypting systems, threatening to publish the leaked data if the ransom is not paid",
                    "Attackers demand double the amount of money if paid in cash",
                    "Two different ransomware gangs infect the same computer at once",
                    "The victim pays ransom twice by accident"
                ],
                "correct_answer": "Attackers steal confidential corporate data before encrypting systems, threatening to publish the leaked data if the ransom is not paid",
                "explanation": "Double extortion bypasses backups: even if a victim can restore files from tapes, attackers extort them by threatening public data leaks."
            },
            {
                "question": "What is a 'Rootkit'?",
                "options": [
                    "A stealthy type of malware designed to hide its presence and other malicious tools deep inside the operating system kernel, intercepting system calls",
                    "A tool used by gardeners to trim tree roots",
                    "A program that updates the CPU fan speed",
                    "A standard Windows password reset utility"
                ],
                "correct_answer": "A stealthy type of malware designed to hide its presence and other malicious tools deep inside the operating system kernel, intercepting system calls",
                "explanation": "Rootkits operate at kernel level (Ring 0) to mask files, network sockets, and processes from the operating system's own diagnostic tools."
            },
            {
                "question": "What type of malware quietly records every keystroke entered by a user on their keyboard to harvest usernames, passwords, and credit card numbers?",
                "options": ["Keylogger (Spyware)", "Adware", "Logic Bomb", "Polymorphic Worm"],
                "correct_answer": "Keylogger (Spyware)",
                "explanation": "Keyloggers capture hardware or software keystrokes, recording passwords and personal data as the victim types."
            },
            {
                "question": "Why is paying the ransom to ransomware criminals discouraged by law enforcement agencies like the FBI?",
                "options": [
                    "There is zero guarantee the criminals will provide working keys, and payments fund future criminal operations and incentivize further attacks",
                    "Bitcoin is illegal in all 50 US states",
                    "Ransomware files automatically decrypt after 30 days anyway",
                    "Criminals are legally required to refund money within 14 business days"
                ],
                "correct_answer": "There is zero guarantee the criminals will provide working keys, and payments fund future criminal operations and incentivize further attacks",
                "explanation": "Paying ransoms does not guarantee decryption, marks the victim as an easy target for re-extortion, and directly funds global organized crime."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 22: Social Engineering Attacks (Phishing, Vishing, Tailgating, Dumpster Diving)
    # ---------------------------------------------------------
    DayBlueprint(
        order=22,
        title="Day 22: Social Engineering Attacks (Phishing, Vishing, Tailgating, Dumpster Diving)",
        concept="Mastering human vulnerability exploitation: Phishing (fraudulent emails), Spear Phishing (targeted attacks), Vishing (voice fraud), Smishing (SMS phishing), Tailgating (piggybacking through doors), and Dumpster Diving (physical waste reconnaissance).",
        analogy="Social engineering is hacking the human brain rather than the computer operating system. It is much easier to trick a receptionist into opening the front door with a fake delivery clipboard than it is to pick a titanium biometric deadbolt with lockpicks.",
        theory_sections=[
            {
                "heading": "The Principles of Social Engineering",
                "content": (
                    "Social engineers manipulate human psychology using core psychological triggers:\n"
                    "- **Urgency**: 'Your account will be suspended within 15 minutes unless you verify credentials!'\n"
                    "- **Authority**: Pretending to be the CEO, legal counsel, or the IT department.\n"
                    "- **Fear**: Threatening tax audits, police arrest, or job termination.\n"
                    "- **Greed / Curiosity**: 'Click here to see the secret employee holiday bonus spreadsheet!'\n\n"
                    "Primary Attack Vectors:\n"
                    "1. **Phishing**: Bulk fraudulent emails luring victims to fake login portals.\n"
                    "2. **Spear Phishing**: Highly tailored phishing targeting a specific individual using customized research (LinkedIn reconnaissance).\n"
                    "3. **Whaling**: Spear phishing targeting C-suite executives (CEOs, CFOs) for Business Email Compromise (BEC) wire transfers.\n"
                    "4. **Vishing & Smishing**: Voice phishing over telephone calls (often with AI voice clones) and SMS text message phishing.\n"
                    "5. **Tailgating (Piggybacking)**: Slipping past secure badge doors behind an authorized employee.\n"
                    "6. **Dumpster Diving**: Searching un-shredded office trash bins for printed passwords, network diagrams, and customer records."
                )
            },
            {
                "heading": "Inspecting Email Headers for Spoofing",
                "content": (
                    "Phishing emails often spoof the display name. Defensive systems verify three DNS records:\n"
                    "- **SPF (Sender Policy Framework)**: Lists authorized mail server IPs.\n"
                    "- **DKIM (DomainKeys Identified Mail)**: Cryptographic signature verifying email integrity.\n"
                    "- **DMARC**: Policy directing mail servers how to treat messages failing SPF/DKIM (quarantine or reject)."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Verifying Email Domain Authenticity via SPF and DMARC Queries",
                "language": "bash",
                "code": (
                    "# Querying DNS TXT records to check SPF authorized sender IPs:\n"
                    "nslookup -type=TXT paypal.com\n"
                    "# Output: v=spf1 include:_spf.paypal.com ~all\n\n"
                    "# Checking DMARC enforcement policy:\n"
                    "nslookup -type=TXT _dmarc.paypal.com\n"
                    "# Output: v=DMARC1; p=reject; rua=mailto:d@rua.agari.com"
                ),
                "explanation": "If an email claiming to be from paypal.com arrives from an unauthorized IP, a strict DMARC 'p=reject' policy instructs receiving servers to discard it."
            },
            {
                "title": "Python: Detecting Phishing Indicators in Email Bodies",
                "language": "python",
                "code": (
                    "def score_phishing_email(subject: str, body: str, sender_domain: str) -> dict:\n"
                    "    score = 0\n"
                    "    flags = []\n"
                    "    urgency_words = ['urgent', 'immediate', 'suspended', 'verify now', 'action required']\n"
                    "    for word in urgency_words:\n"
                    "        if word in subject.lower() or word in body.lower():\n"
                    "            score += 2\n"
                    "            flags.append(f'Urgency keyword: {word}')\n"
                    "    \n"
                    "    if 'bit.ly' in body or 'tinyurl' in body:\n"
                    "        score += 3\n"
                    "        flags.append('Obfuscated link detected')\n"
                    "        \n"
                    "    return {'risk_score': score, 'is_suspected_phishing': score >= 4, 'flags': flags}\n\n"
                    "sample_subj = 'URGENT: Your Corporate Account Will Be Suspended'\n"
                    "sample_body = 'Please verify now via bit.ly/login-verify'\n"
                    "print(score_phishing_email(sample_subj, sample_body, 'attacker-fake.com'))"
                ),
                "explanation": "Demonstrates heuristic scoring rules used by secure email gateways (SEGs) to intercept phishing messages."
            }
        ],
        coding_challenge={
            "description": "Write a Python function `classify_social_engineering(channel: str, is_targeted_executive: bool) -> str` that returns 'WHALING' if channel == 'EMAIL' and is_targeted_executive is True, 'PHISHING' if channel == 'EMAIL', 'VISHING' if channel == 'VOICE', 'SMISHING' if channel == 'SMS', and 'PHYSICAL' if channel == 'IN_PERSON'.",
            "starter_code": (
                "def classify_social_engineering(channel: str, is_targeted_executive: bool) -> str:\n"
                "    # Return attack category string\n"
                "    return ''\n\n"
                "print(classify_social_engineering('EMAIL', True))\n"
                "print(classify_social_engineering('VOICE', False))\n"
                "print(classify_social_engineering('SMS', False))"
            ),
            "solution_code": (
                "def classify_social_engineering(channel: str, is_targeted_executive: bool) -> str:\n"
                "    ch = channel.upper()\n"
                "    if ch == 'EMAIL':\n"
                "        return 'WHALING' if is_targeted_executive else 'PHISHING'\n"
                "    if ch == 'VOICE':\n"
                "        return 'VISHING'\n"
                "    if ch == 'SMS':\n"
                "        return 'SMISHING'\n"
                "    if ch == 'IN_PERSON':\n"
                "        return 'PHYSICAL'\n"
                "    return 'UNKNOWN'\n\n"
                "print(classify_social_engineering('EMAIL', True))\n"
                "print(classify_social_engineering('VOICE', False))\n"
                "print(classify_social_engineering('SMS', False))"
            ),
            "expected_output": "WHALING\nVISHING\nSMISHING"
        },
        quizzes=[
            {
                "question": "What is 'Spear Phishing' compared to standard bulk Phishing?",
                "options": [
                    "A customized, carefully researched phishing attack targeting a specific individual or organization using personalized details",
                    "A phishing attack sent only to fishermen",
                    "A phishing attack with an animated spear icon",
                    "An attack that uses physical paper mail"
                ],
                "correct_answer": "A customized, carefully researched phishing attack targeting a specific individual or organization using personalized details",
                "explanation": "Standard phishing casts a broad net with generic greetings, while spear phishing weaponizes personal intelligence gathered on specific targets."
            },
            {
                "question": "What is 'Whaling' in cybersecurity?",
                "options": [
                    "A spear phishing attack specifically targeting high-profile corporate executives such as CEOs, CFOs, or Board members",
                    "Hacking into submarine sonar systems",
                    "Stealing large hard drives with terabytes of data",
                    "Sending emails with photos of marine mammals"
                ],
                "correct_answer": "A spear phishing attack specifically targeting high-profile corporate executives such as CEOs, CFOs, or Board members",
                "explanation": "Whaling targets the 'big fish' (executives) to authorize fraudulent multimillion-dollar wire transfers or extract trade secrets."
            },
            {
                "question": "What is 'Tailgating' (also known as Piggybacking) in physical security?",
                "options": [
                    "Following closely behind an authorized employee through a secure card-access door before the door closes, without scanning credentials",
                    "Driving a truck behind a server delivery van",
                    "Hacking the brake lights of an employee's car",
                    "Leaving garbage outside the office building"
                ],
                "correct_answer": "Following closely behind an authorized employee through a secure card-access door before the door closes, without scanning credentials",
                "explanation": "Tailgating exploits human politeness (holding doors open) to bypass electronic badge readers and access physical facilities."
            },
            {
                "question": "Which social engineering attack occurs over telephone voice calls, often using spoofed caller IDs or AI voice synthesis?",
                "options": ["Vishing (Voice Phishing)", "Smishing", "Shoulder Surfing", "Watering Hole Attack"],
                "correct_answer": "Vishing (Voice Phishing)",
                "explanation": "Vishing combines 'voice' and 'phishing', where attackers impersonate bank representatives or tech support over telephone lines."
            },
            {
                "question": "Which three DNS security standards protect email domains from being spoofed by unauthorized phishing servers?",
                "options": ["SPF, DKIM, and DMARC", "TCP, UDP, and ICMP", "HTML, CSS, and JavaScript", "BIOS, UEFI, and CMOS"],
                "correct_answer": "SPF, DKIM, and DMARC",
                "explanation": "SPF lists authorized sender IPs, DKIM provides cryptographic digital signatures, and DMARC enforces rejection policies on failure."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 23: Network Attacks (DDoS, MitM, MAC Spoofing, ARP Poisoning)
    # ---------------------------------------------------------
    DayBlueprint(
        order=23,
        title="Day 23: Network Attacks (DDoS, MitM, MAC Spoofing, ARP Poisoning)",
        concept="Dissecting core network-layer attacks: Distributed Denial of Service (DDoS via botnets), Man-in-the-Middle (MitM interception), MAC Spoofing, and ARP Cache Poisoning.",
        analogy="Think of street mail delivery: ARP Poisoning is a rogue neighbor walking up to the mail carrier and whispering 'Hey, the CEO moved into my house—put all their letters into my mailbox.' Once the mail carrier believes this lie, all confidential mail flows through the intruder's hands (Man-in-the-Middle). DDoS is hiring 10,000 people to crowd into the post office lobby at once so no actual customer can reach the counter.",
        theory_sections=[
            {
                "heading": "ARP Poisoning and Man-in-the-Middle (MitM)",
                "content": (
                    "In local Ethernet networks, devices use **ARP (Address Resolution Protocol)** to resolve Layer 3 IP addresses to Layer 2 MAC addresses:\n"
                    "- ARP is completely stateless and lacks authentication. Any device can send an unsolicited **Gratuitous ARP Reply**.\n"
                    "- **ARP Cache Poisoning**: An attacker broadcasts: *'I am the Default Gateway router's IP, and my MAC is attacker_MAC'*. The victim updates their ARP table, routing all outbound internet traffic directly into the attacker's machine.\n"
                    "- **MitM (Man-in-the-Middle)**: The attacker intercepts, inspects, modifies, and re-forwards the victim's packets to the real gateway, eavesdropping on unencrypted traffic without either party noticing."
                )
            },
            {
                "heading": "Denial of Service (DoS) vs Distributed DoS (DDoS)",
                "content": (
                    "- **DoS**: Single attacking machine attempts to overwhelm a target. Easily blocked by firewall IP bans.\n"
                    "- **DDoS**: An attacker commands a global **Botnet** (millions of compromised IoT devices, cameras, home routers) to flood the target simultaneously. Types include Volumetric UDP/NTP Amplification floods, TCP SYN floods, and Layer 7 HTTP floods."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Inspecting Local ARP Tables and Detecting Duplicate MACs",
                "language": "bash",
                "code": (
                    "# Windows / Linux command to inspect current ARP mappings:\n"
                    "arp -a\n\n"
                    "# ARP Poisoning Detection Signature:\n"
                    "# If the Gateway IP (192.168.1.1) and another workstation (192.168.1.50)\n"
                    "# share the EXACT same physical MAC address (e.g., 00-aa-bb-cc-dd-ee),\n"
                    "# an active ARP Poisoning / MitM attack is in progress!"
                ),
                "explanation": "Two different IP addresses resolving to the same hardware MAC address on a local switch indicates ARP spoofing."
            },
            {
                "title": "Python: Detecting Duplicate MACs in an ARP Table (Anti-Spoofing Detector)",
                "language": "python",
                "code": (
                    "def audit_arp_cache(arp_table: dict) -> list:\n"
                    "    # arp_table: {'ip': 'mac'}\n"
                    "    mac_to_ips = {}\n"
                    "    alerts = []\n"
                    "    for ip, mac in arp_table.items():\n"
                    "        if mac not in mac_to_ips:\n"
                    "            mac_to_ips[mac] = []\n"
                    "        mac_to_ips[mac].append(ip)\n"
                    "    \n"
                    "    for mac, ips in mac_to_ips.items():\n"
                    "        if len(ips) > 1:\n"
                    "            alerts.append(f'ALERT: Multiple IPs {ips} mapped to single MAC {mac} (Possible ARP Poisoning!)')\n"
                    "    return alerts\n\n"
                    "sample_arp = {'192.168.1.1': '00:11:22:33:44:55', '192.168.1.20': '00:11:22:33:44:55'}\n"
                    "print(audit_arp_cache(sample_arp))"
                ),
                "explanation": "Algorithmic detection of ARP cache poisoning based on Layer 2 MAC conflict analysis."
            }
        ],
        coding_challenge={
            "description": "Write a Python function `mitigate_arp_spoof(detected_mac: str, expected_gateway_mac: str) -> str` that returns 'ALLOW' if detected_mac matches expected_gateway_mac, and 'DROP_AND_ALERT' if they differ.",
            "starter_code": (
                "def mitigate_arp_spoof(detected_mac: str, expected_gateway_mac: str) -> str:\n"
                "    # Return 'ALLOW' or 'DROP_AND_ALERT'\n"
                "    return ''\n\n"
                "print(mitigate_arp_spoof('00:AA:BB:CC:DD:EE', '00:AA:BB:CC:DD:EE'))\n"
                "print(mitigate_arp_spoof('DE:AD:BE:EF:00:01', '00:AA:BB:CC:DD:EE'))"
            ),
            "solution_code": (
                "def mitigate_arp_spoof(detected_mac: str, expected_gateway_mac: str) -> str:\n"
                "    if detected_mac.strip().lower() == expected_gateway_mac.strip().lower():\n"
                "        return 'ALLOW'\n"
                "    return 'DROP_AND_ALERT'\n\n"
                "print(mitigate_arp_spoof('00:AA:BB:CC:DD:EE', '00:AA:BB:CC:DD:EE'))\n"
                "print(mitigate_arp_spoof('DE:AD:BE:EF:00:01', '00:AA:BB:CC:DD:EE'))"
            ),
            "expected_output": "ALLOW\nDROP_AND_ALERT"
        },
        quizzes=[
            {
                "question": "What architectural weakness allows an attacker on a local network to perform ARP Cache Poisoning?",
                "options": [
                    "The Address Resolution Protocol (ARP) is stateless and accepts unsolicited ARP reply packets without verifying authentication",
                    "Ethernet cables cannot transmit numbers higher than 255",
                    "Routers do not support password protection",
                    "ARP packets only work on Sundays"
                ],
                "correct_answer": "The Address Resolution Protocol (ARP) is stateless and accepts unsolicited ARP reply packets without verifying authentication",
                "explanation": "Because ARP has no authentication, any host on the subnet can broadcast spoofed ARP replies claiming to own any IP address."
            },
            {
                "question": "What is a 'Man-in-the-Middle' (MitM) attack?",
                "options": [
                    "An attack where an adversary secretly intercepts, reads, and potentially alters communication between two parties who believe they are communicating directly",
                    "A virus that crashes the computer screen in the middle of a movie",
                    "A physical fight between two network technicians",
                    "A router that breaks in half"
                ],
                "correct_answer": "An attack where an adversary secretly intercepts, reads, and potentially alters communication between two parties who believe they are communicating directly",
                "explanation": "In a MitM attack, the attacker sits transparently on the communication path, eavesdropping on or altering packets in real time."
            },
            {
                "question": "What is the primary difference between a DoS attack and a DDoS attack?",
                "options": [
                    "A DoS originates from a single attacking machine, whereas a DDoS originates from thousands of distributed machines (a botnet) simultaneously",
                    "A DoS attack deletes files, while a DDoS steals passwords",
                    "DDoS only affects smartphones",
                    "DoS is legal, while DDoS is illegal"
                ],
                "correct_answer": "A DoS originates from a single attacking machine, whereas a DDoS originates from thousands of distributed machines (a botnet) simultaneously",
                "explanation": "DDoS utilizes distributed botnets scattered across multiple countries, making simple IP blocking ineffective."
            },
            {
                "question": "What enterprise switch security feature prevents ARP Poisoning by inspecting ARP packets against a trusted DHCP binding database?",
                "options": ["Dynamic ARP Inspection (DAI)", "Spanning Tree Protocol", "VLAN Trunking Protocol", "Quality of Service (QoS)"],
                "correct_answer": "Dynamic ARP Inspection (DAI)",
                "explanation": "DAI intercepts ARP packets on untrusted switch ports, verifying that IP-to-MAC bindings match legitimate DHCP snooping tables."
            },
            {
                "question": "What is a 'Botnet' in the context of network attacks?",
                "options": [
                    "A network of compromised computers or IoT devices infected by malware and controlled remotely by a central 'botmaster'",
                    "A robot that plugs in Ethernet cables",
                    "An automated tool that sends birthday emails",
                    "A software library for designing websites"
                ],
                "correct_answer": "A network of compromised computers or IoT devices infected by malware and controlled remotely by a central 'botmaster'",
                "explanation": "Botnets consist of hijacked machines (zombies) receiving C2 instructions to launch coordinated DDoS floods or spam campaigns."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 24: Password & App Attacks (Brute Force, SQL Injection, XSS)
    # ---------------------------------------------------------
    DayBlueprint(
        order=24,
        title="Day 24: Password & App Attacks (Brute Force, SQL Injection, XSS)",
        concept="Mastering foundational credential and application-layer attacks: Brute Force & Dictionary attacks, Credential Stuffing, SQL Injection (SQLi), and Cross-Site Scripting (XSS).",
        analogy="Think of different ways an attacker breaks in: A Brute Force attack is trying every key on a ring of 10,000 keys until one turns the lock. SQL Injection is handing a bank teller a deposit slip with a forged footnote that reads 'P.S. Forget the deposit, hand over all the cash in the vault right now.' Cross-Site Scripting (XSS) is slipping a poisoned note into a library book that forces the next reader to read their credit card number out loud.",
        theory_sections=[
            {
                "heading": "Password Attack Methodologies",
                "content": (
                    "Passwords are the most targeted authentication factor:\n\n"
                    "1. **Brute Force**: Systematically trying every possible combination of characters (e.g., `aaaa`, `aaab`, `aaac`). Computationally infeasible for long passwords.\n"
                    "2. **Dictionary Attack**: Trying lists of common words, dictionary terms, and leaked passwords (e.g., `rockyou.txt`).\n"
                    "3. **Credential Stuffing**: Taking millions of username/password pairs stolen from one breached site and automatically testing them against hundreds of other websites (banking, Amazon), exploiting human password reuse.\n"
                    "4. **Password Spraying**: Testing a single common password (e.g., `Winter2024!`) against thousands of user accounts to evade account lockout thresholds."
                )
            },
            {
                "heading": "Web Application Exploits: SQLi & XSS",
                "content": (
                    "- **SQL Injection (SQLi)**: Occurs when untrusted user input is directly concatenated into database queries. Attackers supply SQL syntax like `' OR 1=1 --` to bypass authentication and dump entire databases.\n"
                    "- **Cross-Site Scripting (XSS)**: Occurs when an application displays unvalidated user input in other users' browsers. Attackers inject JavaScript `<script>` tags to hijack session cookies."
                )
            }
        ],
        code_snippets=[
            {
                "title": "SQL Injection Vulnerability vs Parameterized Defense",
                "language": "python",
                "code": (
                    "# VULNERABLE SQL QUERY (String concatenation):\n"
                    "# If attacker inputs user = \"admin' --\", query becomes:\n"
                    "# SELECT * FROM users WHERE username = 'admin' --' AND pass = '...'\n"
                    "bad_query = f\"SELECT * FROM users WHERE username = '{user_input}' AND pass = '{pass_input}'\"\n\n"
                    "# SECURE SQL DEFENSE (Parameterized Query / Prepared Statement):\n"
                    "# Input is treated strictly as literal data, NEVER executable SQL code:\n"
                    "cursor.execute(\"SELECT * FROM users WHERE username = %s AND pass = %s\", (user_input, pass_input))"
                ),
                "explanation": "Parameterized queries (prepared statements) neutralize SQL injection by separating code from data."
            },
            {
                "title": "Simulating Credential Lockout Against Brute-Force Attacks",
                "language": "python",
                "code": (
                    "class LoginController:\n"
                    "    def __init__(self):\n"
                    "        self.failed_attempts = {}\n"
                    "        self.locked_accounts = set()\n"
                    "    \n"
                    "    def attempt_login(self, username: str, is_correct: bool) -> str:\n"
                    "        if username in self.locked_accounts:\n"
                    "            return 'ACCOUNT_LOCKED: Maximum failed attempts exceeded.'\n"
                    "        if is_correct:\n"
                    "            self.failed_attempts[username] = 0\n"
                    "            return 'SUCCESS'\n"
                    "        \n"
                    "        self.failed_attempts[username] = self.failed_attempts.get(username, 0) + 1\n"
                    "        if self.failed_attempts[username] >= 3:\n"
                    "            self.locked_accounts.add(username)\n"
                    "            return 'ACCOUNT_LOCKED'\n"
                    "        return f'FAILED: {3 - self.failed_attempts[username]} attempts remaining'\n\n"
                    "ctl = LoginController()\n"
                    "print(ctl.attempt_login('alice', False))\n"
                    "print(ctl.attempt_login('alice', False))\n"
                    "print(ctl.attempt_login('alice', False))\n"
                    "print(ctl.attempt_login('alice', False))"
                ),
                "explanation": "Account lockout thresholds mitigate simple brute-force attacks by freezing accounts after repeated failures."
            }
        ],
        coding_challenge={
            "description": "Write a Python function `detect_sqli(user_input: str) -> bool` that inspects an input string and returns True if it contains SQL injection patterns like \"' or 1=1\" or \"'--\" or \"union select\" (case-insensitive), otherwise False.",
            "starter_code": (
                "def detect_sqli(user_input: str) -> bool:\n"
                "    # Return True if SQLi indicators are detected\n"
                "    return False\n\n"
                "print(detect_sqli(\"admin' OR 1=1 --\"))\n"
                "print(detect_sqli(\"alice\"))"
            ),
            "solution_code": (
                "def detect_sqli(user_input: str) -> bool:\n"
                "    clean = user_input.lower()\n"
                "    signatures = [\"' or 1=1\", \"'--\", \"union select\", \"' or '1'='1\"]\n"
                "    for sig in signatures:\n"
                "        if sig in clean:\n"
                "            return True\n"
                "    return False\n\n"
                "print(detect_sqli(\"admin' OR 1=1 --\"))\n"
                "print(detect_sqli(\"alice\"))"
            ),
            "expected_output": "True\nFalse"
        },
        quizzes=[
            {
                "question": "What is the primary technical root cause of SQL Injection (SQLi) vulnerabilities in web applications?",
                "options": [
                    "Concatenating untrusted user input directly into executable SQL query strings without parameterization or escaping",
                    "Using a password shorter than 8 characters",
                    "Running a database server on a Linux operating system",
                    "Connecting to a database without an internet cable"
                ],
                "correct_answer": "Concatenating untrusted user input directly into executable SQL query strings without parameterization or escaping",
                "explanation": "SQLi occurs when user input is treated as SQL command syntax. Prepared statements prevent this by strictly separating code from data."
            },
            {
                "question": "What is 'Credential Stuffing'?",
                "options": [
                    "An attack where automated bots test lists of stolen username/password pairs from past data breaches across numerous other websites",
                    "Writing passwords on paper and stuffing them into a desk drawer",
                    "Using more than 50 characters in a single password",
                    "Sending passwords in postal envelopes"
                ],
                "correct_answer": "An attack where automated bots test lists of stolen username/password pairs from past data breaches across numerous other websites",
                "explanation": "Credential stuffing exploits the human habit of password reuse across personal and corporate platforms."
            },
            {
                "question": "What is Cross-Site Scripting (XSS)?",
                "options": [
                    "An attack where malicious executable scripts (such as JavaScript) are injected into trusted websites and executed in the victim's web browser",
                    "Crossing two network cables to double bandwidth",
                    "Drawing a red X across a computer screen",
                    "Deleting an Excel spreadsheet"
                ],
                "correct_answer": "An attack where malicious executable scripts (such as JavaScript) are injected into trusted websites and executed in the victim's web browser",
                "explanation": "XSS allows attackers to execute arbitrary JavaScript in victim browsers, stealing authentication session tokens or redirecting users."
            },
            {
                "question": "How does a 'Password Spraying' attack evade standard account lockout policies?",
                "options": [
                    "By trying a single commonly used password against thousands of different usernames, rather than trying thousands of passwords against a single user",
                    "By typing the password backwards",
                    "By spraying cleaning alcohol onto the keyboard",
                    "By resetting the server clock"
                ],
                "correct_answer": "By trying a single commonly used password against thousands of different usernames, rather than trying thousands of passwords against a single user",
                "explanation": "Account lockouts trigger after multiple failed attempts on one account. Spraying tests one password across all accounts, staying under lockout limits."
            },
            {
                "question": "What is the gold standard defense against SQL Injection across all software development frameworks?",
                "options": [
                    "Parameterized Queries (Prepared Statements)",
                    "Changing the database port number",
                    "Restarting the SQL database every midnight",
                    "Running the web server as root"
                ],
                "correct_answer": "Parameterized Queries (Prepared Statements)",
                "explanation": "Prepared statements ensure that the SQL database parser interprets user inputs purely as literal data parameters, completely preventing code execution."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 25: Authentication Factors (Something you know, have, are, do)
    # ---------------------------------------------------------
    DayBlueprint(
        order=25,
        title="Day 25: Authentication Factors (Something you know, have, are, do)",
        concept="Mastering the foundational categories of human identity authentication factors: Knowledge (know), Possession (have), Inherence (are), and Behavior/Location (do/where).",
        analogy="Think of entering a high-security military vault: Factor 1 (Something you know) is whispering the secret password. Factor 2 (Something you have) is inserting a brass physical key into the lock. Factor 3 (Something you are) is looking into the retinal eye scanner. Factor 4 (Something you do) is signing your handwritten signature on the visitor ledger.",
        theory_sections=[
            {
                "heading": "The Core Authentication Factor Categories",
                "content": (
                    "Security systems verify claims of identity using distinct categories:\n\n"
                    "1. **Something You Know (Knowledge Factor)**: Secrets stored in the human memory. Examples: Passwords, PINs, security questions, passphrase mnemonics. Most vulnerable to phishing and brute-forcing.\n"
                    "2. **Something You Have (Possession Factor)**: Physical or digital items owned by the user. Examples: Hardware security keys (YubiKey), smartphone authenticator apps (TOTP), smart cards, SMS codes.\n"
                    "3. **Something You Are (Inherence Factor)**: Biometric physical characteristics unique to human biology. Examples: Fingerprints, facial geometry (Face ID), iris scans, voice prints.\n"
                    "4. **Something You Do (Behavioral Factor)**: Keystroke typing dynamics, mouse movement cadence, gait recognition.\n"
                    "5. **Somewhere You Are (Location Factor)**: IP geolocation, GPS coordinates, local cellular tower pings."
                )
            },
            {
                "heading": "What Qualifies as Multi-Factor?",
                "content": (
                    "A password and a PIN is **NOT** two-factor authentication (both are 'Something You Know'). True Multi-Factor Authentication (MFA) requires presenting credentials from **two or more DIFFERENT factor categories** (e.g., a password [Know] PLUS a hardware YubiKey [Have])."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Verifying Multiple Authentication Factor Diversity in Code",
                "language": "python",
                "code": (
                    "def is_true_mfa(factors_presented: list) -> bool:\n"
                    "    # factors_presented contains categories: 'KNOW', 'HAVE', 'ARE'\n"
                    "    unique_categories = set(factors_presented)\n"
                    "    # Requires at least 2 distinct factor categories\n"
                    "    return len(unique_categories) >= 2\n\n"
                    "# Case A: Password + PIN (Both KNOW) -> False\n"
                    "print('Password + PIN is MFA:', is_true_mfa(['KNOW', 'KNOW']))\n\n"
                    "# Case B: Password + YubiKey (KNOW + HAVE) -> True\n"
                    "print('Password + YubiKey is MFA:', is_true_mfa(['KNOW', 'HAVE']))"
                ),
                "explanation": "Illustrates the fundamental compliance definition of MFA: diverse factor categories are mandatory."
            },
            {
                "title": "Querying Geolocation Factors via IP (Somewhere You Are)",
                "language": "bash",
                "code": (
                    "# Querying IP geolocation API to enforce impossible travel velocity checks:\n"
                    "curl -s https://ipapi.co/8.8.8.8/json/ | jq '{country_name: .country_name, city: .city}'"
                ),
                "explanation": "Contextual access controls verify physical location to block logins originating from unauthorized foreign countries."
            }
        ],
        coding_challenge={
            "description": "Write a Python function `categorize_factor(item: str) -> str` that maps 'password' -> 'KNOW', 'pin' -> 'KNOW', 'smartcard' -> 'HAVE', 'yubikey' -> 'HAVE', 'fingerprint' -> 'ARE', and 'retina_scan' -> 'ARE'. Return 'UNKNOWN' for anything else.",
            "starter_code": (
                "def categorize_factor(item: str) -> str:\n"
                "    # Return 'KNOW', 'HAVE', 'ARE', or 'UNKNOWN'\n"
                "    return ''\n\n"
                "print(categorize_factor('password'))\n"
                "print(categorize_factor('yubikey'))\n"
                "print(categorize_factor('fingerprint'))"
            ),
            "solution_code": (
                "def categorize_factor(item: str) -> str:\n"
                "    mapping = {\n"
                "        'password': 'KNOW',\n"
                "        'pin': 'KNOW',\n"
                "        'security_question': 'KNOW',\n"
                "        'smartcard': 'HAVE',\n"
                "        'yubikey': 'HAVE',\n"
                "        'totp_token': 'HAVE',\n"
                "        'fingerprint': 'ARE',\n"
                "        'retina_scan': 'ARE',\n"
                "        'face_id': 'ARE'\n"
                "    }\n"
                "    return mapping.get(item.lower(), 'UNKNOWN')\n\n"
                "print(categorize_factor('password'))\n"
                "print(categorize_factor('yubikey'))\n"
                "print(categorize_factor('fingerprint'))"
            ),
            "expected_output": "KNOW\nHAVE\nARE"
        },
        quizzes=[
            {
                "question": "Which of the following represents an authentication factor from the 'Something You Have' (Possession) category?",
                "options": ["A hardware YubiKey USB token", "A 12-character alphanumeric password", "A fingerprint scan", "Your mother's maiden name"],
                "correct_answer": "A hardware YubiKey USB token",
                "explanation": "A YubiKey is a physical possession factor held by the authorized user, generating cryptographic proof of possession."
            },
            {
                "question": "A user enters a standard password, followed immediately by a 4-digit PIN number. Does this qualify as true Multi-Factor Authentication (MFA)?",
                "options": [
                    "No, because both credentials belong to the same category ('Something You Know')",
                    "Yes, because two separate prompts were filled out",
                    "Yes, but only if the PIN is longer than 6 digits",
                    "No, because PIN numbers are illegal in corporate security"
                ],
                "correct_answer": "No, because both credentials belong to the same category ('Something You Know')",
                "explanation": "True MFA requires presenting credentials from two or more DIFFERENT factor categories (e.g., Knowledge + Possession)."
            },
            {
                "question": "Biometric identifiers like fingerprints, facial recognition, and iris patterns belong to which authentication factor category?",
                "options": ["Something You Are (Inherence)", "Something You Know (Knowledge)", "Something You Have (Possession)", "Somewhere You Are (Location)"],
                "correct_answer": "Something You Are (Inherence)",
                "explanation": "Inherence factors are based on unique physical or physiological biological traits of the individual human body."
            },
            {
                "question": "What is an example of an 'Authentication Factor: Something You Do' (Behavioral)?",
                "options": ["Keystroke typing dynamics and mouse movement cadence", "Entering an account username", "Holding an ID badge in your hand", "Memorizing an encryption passphrase"],
                "correct_answer": "Keystroke typing dynamics and mouse movement cadence",
                "explanation": "Behavioral biometrics measure distinct behavioral patterns in how a user types, holds their phone, or moves their cursor."
            },
            {
                "question": "What is 'Impossible Travel' detection in modern identity security systems?",
                "options": [
                    "An anomaly detection alert triggered when a user logs in from New York and then from London 20 minutes later, which is physically impossible",
                    "A rule that bans employees from flying on airplanes",
                    "An internet outage on commercial flights",
                    "A computer running out of battery during transit"
                ],
                "correct_answer": "An anomaly detection alert triggered when a user logs in from New York and then from London 20 minutes later, which is physically impossible",
                "explanation": "Impossible travel evaluates the Location factor: consecutive logins across geographically distant points within impossible transit windows indicate compromised credentials."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 26: Multi-Factor Authentication (MFA) and Two-Factor Authentication (2FA)
    # ---------------------------------------------------------
    DayBlueprint(
        order=26,
        title="Day 26: Multi-Factor Authentication (MFA) and Two-Factor Authentication (2FA)",
        concept="Differentiating MFA implementation tiers: SMS/Email OTP (weak, SIM-swappable), Time-Based One-Time Passwords (TOTP), Push Notifications (MFA Fatigue), and FIDO2/WebAuthn hardware keys (phishing-resistant).",
        analogy="Think of different secondary locks: SMS OTP is the bank mailing you a postcard with a temporary code—anyone who bribes the postman (SIM swap) can read it. TOTP authenticator apps are synchronized digital watches ticking every 30 seconds. FIDO2 hardware keys (YubiKey) are cryptographic passports that will ONLY speak directly to the real bank website, refusing to talk to a fake phishing website.",
        theory_sections=[
            {
                "heading": "The Hierarchy of MFA Security",
                "content": (
                    "Not all MFA methods offer equal security:\n\n"
                    "1. **SMS & Email OTP (Lowest Security)**: Transmits 6-digit codes over cellular networks. Vulnerable to **SIM Swapping** (tricking mobile carriers into porting the victim's phone number to an attacker's SIM) and SS7 cellular interception. Prohibited by NIST for high-security applications.\n"
                    "2. **TOTP (RFC 6238 - Google/Microsoft Authenticator)**: Generates a rotating 6-digit code every 30 seconds using a shared secret seed and the current Unix timestamp. Resistant to SIM swaps, but vulnerable to **Reverse Proxy Phishing** (Evilginx).\n"
                    "3. **Mobile Push Notifications**: Users tap 'Approve' on their phone. Attackers exploit this via **MFA Fatigue / Push Bombing** (sending 100 push alerts at 3 AM until the frustrated victim taps Approve).\n"
                    "4. **FIDO2 / WebAuthn Hardware Tokens (Gold Standard)**: Uses public-key cryptography bound to the website's exact domain origin. **100% immune to phishing and reverse proxies**."
                )
            },
            {
                "heading": "How TOTP Works Under the Hood",
                "content": (
                    "TOTP computes an HMAC-SHA1 hash using a shared base32 secret key and the current 30-second time slice:\n"
                    "`TimeStep = floor(current_unix_time / 30)`\n"
                    "`Code = Truncate(HMAC_SHA1(Secret, TimeStep))`\n"
                    "Both the server and user smartphone calculate this independently without transmitting the code over the internet."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Python: Generating RFC 6238 TOTP Codes",
                "language": "python",
                "code": (
                    "import hmac\n"
                    "import hashlib\n"
                    "import time\n"
                    "import struct\n"
                    "import base64\n\n"
                    "def generate_totp(secret_base32: str) -> str:\n"
                    "    key = base64.b32decode(secret_base32)\n"
                    "    # Current 30-second window\n"
                    "    intervals_no = int(time.time() // 30)\n"
                    "    msg = struct.pack('>Q', intervals_no)\n"
                    "    h = hmac.new(key, msg, hashlib.sha1).digest()\n"
                    "    o = h[19] & 15\n"
                    "    h_code = (struct.unpack('>I', h[o:o+4])[0] & 0x7fffffff) % 1000000\n"
                    "    return f'{h_code:06d}'\n\n"
                    "demo_secret = 'JBSWY3DPEHPK3PXP'\n"
                    "print('Generated 30-second TOTP:', generate_totp(demo_secret))"
                ),
                "explanation": "Underlying mathematics of authenticator apps: calculating cryptographic HMACs against time windows."
            },
            {
                "title": "Hardening Push MFA with Number Matching",
                "language": "bash",
                "code": (
                    "# Microsoft Entra ID / Okta Number Matching policy configuration:\n"
                    "# When a user attempts to log in, the desktop browser displays a 2-digit number (e.g., 42).\n"
                    "# The user MUST physically type '42' into the mobile authenticator app.\n"
                    "# Result: Neutralizes MFA Fatigue attacks, because attackers cannot guess the displayed number."
                ),
                "explanation": "Number matching ensures the person approving the push notification is looking at the active login screen."
            }
        ],
        coding_challenge={
            "description": "Write a Python function `evaluate_mfa_tier(mfa_method: str) -> str` that returns 'HIGH (Phishing Resistant)' if method is 'FIDO2' or 'WEBAUTHN', 'MEDIUM' if 'TOTP', 'LOW (Vulnerable to Push Fatigue)' if 'PUSH', and 'INSECURE (SIM Swap Risk)' if 'SMS'. Return 'NONE' for anything else.",
            "starter_code": (
                "def evaluate_mfa_tier(mfa_method: str) -> str:\n"
                "    # Return security evaluation string\n"
                "    return ''\n\n"
                "print(evaluate_mfa_tier('FIDO2'))\n"
                "print(evaluate_mfa_tier('SMS'))"
            ),
            "solution_code": (
                "def evaluate_mfa_tier(mfa_method: str) -> str:\n"
                "    m = mfa_method.upper()\n"
                "    if m in ['FIDO2', 'WEBAUTHN']:\n"
                "        return 'HIGH (Phishing Resistant)'\n"
                "    if m == 'TOTP':\n"
                "        return 'MEDIUM'\n"
                "    if m == 'PUSH':\n"
                "        return 'LOW (Vulnerable to Push Fatigue)'\n"
                "    if m == 'SMS':\n"
                "        return 'INSECURE (SIM Swap Risk)'\n"
                "    return 'NONE'\n\n"
                "print(evaluate_mfa_tier('FIDO2'))\n"
                "print(evaluate_mfa_tier('SMS'))"
            ),
            "expected_output": "HIGH (Phishing Resistant)\nINSECURE (SIM Swap Risk)"
        },
        quizzes=[
            {
                "question": "Why is SMS-based Two-Factor Authentication discouraged by security organizations like NIST?",
                "options": [
                    "SMS messages can be intercepted via SIM-Swapping social engineering and SS7 cellular network vulnerabilities",
                    "SMS messages cost too much money to send",
                    "Text messages can only be received on landline phones",
                    "SMS codes do not use numbers"
                ],
                "correct_answer": "SMS messages can be intercepted via SIM-Swapping social engineering and SS7 cellular network vulnerabilities",
                "explanation": "Attackers bribe or trick mobile carrier support agents into transferring victim phone numbers to rogue SIM cards, intercepting all SMS OTPs."
            },
            {
                "question": "What is an 'MFA Fatigue' (or Push Bombing) attack?",
                "options": [
                    "An attacker spams a victim's smartphone with dozens of mobile push authorization prompts in rapid succession until the victim approves one to make it stop",
                    "The phone battery running out of power",
                    "An employee falling asleep at their desk",
                    "The authenticator app freezing"
                ],
                "correct_answer": "An attacker spams a victim's smartphone with dozens of mobile push authorization prompts in rapid succession until the victim approves one to make it stop",
                "explanation": "MFA fatigue preys on human exhaustion: repeatedly triggering push notifications at odd hours until the victim clicks 'Approve'."
            },
            {
                "question": "Which MFA standard provides true cryptographic immunity against reverse-proxy phishing attacks?",
                "options": ["FIDO2 / WebAuthn Hardware Security Keys", "SMS text codes", "Voice call PINs", "Security questions about pet names"],
                "correct_answer": "FIDO2 / WebAuthn Hardware Security Keys",
                "explanation": "FIDO2/WebAuthn binds authentication to the browser's cryptographic domain origin. A phishing proxy at `fake-bank.com` cannot elicit keys for `real-bank.com`."
            },
            {
                "question": "How does a standard Time-Based One-Time Password (TOTP) authenticator app generate rotating 6-digit codes without an active internet connection?",
                "options": [
                    "It calculates a cryptographic hash combining a pre-shared secret seed with the current 30-second Unix epoch timestamp",
                    "It guesses numbers randomly",
                    "It connects to satellite radio signals",
                    "It reads data from the phone's camera"
                ],
                "correct_answer": "It calculates a cryptographic hash combining a pre-shared secret seed with the current 30-second Unix epoch timestamp",
                "explanation": "Both the authenticator app and server independently calculate HMACs based on shared secret keys and synchronized clock timestamps."
            },
            {
                "question": "What security feature effectively neutralizes MFA Fatigue attacks in mobile push authenticator apps?",
                "options": [
                    "Number Matching (requiring the user to enter a number shown on the login screen into their phone app)",
                    "Changing the color of the notification banner",
                    "Deleting all email messages",
                    "Turning the phone volume down"
                ],
                "correct_answer": "Number Matching (requiring the user to enter a number shown on the login screen into their phone app)",
                "explanation": "Number matching forces the user to see the two-digit code displayed on the real browser session, preventing accidental approvals of attacker-initiated logins."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 27: Access Control Models (MAC, DAC, RBAC)
    # ---------------------------------------------------------
    DayBlueprint(
        order=27,
        title="Day 27: Access Control Models (MAC, DAC, RBAC)",
        concept="Comparing enterprise access governance models: Discretionary Access Control (DAC), Mandatory Access Control (MAC), Role-Based Access Control (RBAC), and Attribute-Based Access Control (ABAC).",
        analogy="Think of different property rules: DAC is your personal home: you own it, so you have complete discretion to lend your house key to anyone you choose. MAC is a military base: top-secret documents are stamped with classifications, and regardless of who created the file, only soldiers with Top Secret clearance can read it. RBAC is a corporate hospital: doctors get doctor permissions, and nurses get nurse permissions automatically based on job title.",
        theory_sections=[
            {
                "heading": "The Core Access Control Models",
                "content": (
                    "Access control models define how subjects (users) are granted rights over objects (files/databases):\n\n"
                    "1. **DAC (Discretionary Access Control)**: The data owner has complete discretion over who can access their files. Standard in desktop operating systems (Windows NTFS, Linux `chmod`). Weakness: Users can inadvertently grant write permissions to unauthorized guests.\n"
                    "2. **MAC (Mandatory Access Control)**: Centralized, strict security labels determine access. The operating system enforces access rules based on security clearances (e.g., Top Secret, Secret, Unclassified). Users cannot share or alter permissions. Examples: SELinux, military systems.\n"
                    "3. **RBAC (Role-Based Access Control)**: Permissions are assigned to specific job **Roles** (e.g., 'Billing Analyst', 'Network Admin'), and users are assigned to roles. Solves permission bloat in large organizations.\n"
                    "4. **ABAC (Attribute-Based Access Control)**: Evaluates real-time contextual attributes: user role, time of day, location, and device health (e.g., 'Allow access IF role=Doctor AND location=EmergencyRoom AND time=ShiftHours')."
                )
            },
            {
                "heading": "The Principle of Separation of Duties (SoD)",
                "content": (
                    "In enterprise RBAC, high-risk operations require two distinct roles to complete (e.g., the employee who requests an invoice payment cannot be the same role that approves and disburses the funds), preventing fraud."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Linux Mandatory Access Control: Auditing SELinux Contexts",
                "language": "bash",
                "code": (
                    "# Viewing SELinux security context labels (User:Role:Type:Level):\n"
                    "ls -Z /var/www/html/index.html\n"
                    "# Output: system_u:object_r:httpd_sys_content_t:s0\n\n"
                    "# Under MAC, even if root runs a process, if the process lacks\n"
                    "# the proper SELinux type context, the OS kernel forbids access!"
                ),
                "explanation": "Mandatory Access Control enforces kernel-level policy boundaries that even superusers cannot bypass without changing policies."
            },
            {
                "title": "Python: Implementing Role-Based Access Control (RBAC)",
                "language": "python",
                "code": (
                    "class RBACController:\n"
                    "    def __init__(self):\n"
                    "        # Roles -> Permissions\n"
                    "        self.role_permissions = {\n"
                    "            'ADMIN': {'read', 'write', 'delete', 'manage_users'},\n"
                    "            'EDITOR': {'read', 'write'},\n"
                    "            'VIEWER': {'read'}\n"
                    "        }\n"
                    "        # Users -> Roles\n"
                    "        self.user_roles = {'alice': 'ADMIN', 'bob': 'VIEWER'}\n"
                    "    \n"
                    "    def check_permission(self, username: str, action: str) -> bool:\n"
                    "        role = self.user_roles.get(username)\n"
                    "        if not role:\n"
                    "            return False\n"
                    "        return action in self.role_permissions.get(role, set())\n\n"
                    "rbac = RBACController()\n"
                    "print('Alice delete:', rbac.check_permission('alice', 'delete'))\n"
                    "print('Bob delete:', rbac.check_permission('bob', 'delete'))"
                ),
                "explanation": "Standard RBAC engine decouples users from raw permissions via intermediate organizational roles."
            }
        ],
        coding_challenge={
            "description": "Write a Python function `check_abac_access(user_role: str, location: str, hour_24: int) -> bool` that allows access only if user_role == 'SURGEON', location == 'HOSPITAL_NETWORK', and hour_24 is between 6 and 20 inclusive.",
            "starter_code": (
                "def check_abac_access(user_role: str, location: str, hour_24: int) -> bool:\n"
                "    # Return True if all ABAC criteria pass, False otherwise\n"
                "    return False\n\n"
                "print(check_abac_access('SURGEON', 'HOSPITAL_NETWORK', 14))\n"
                "print(check_abac_access('SURGEON', 'EXTERNAL_CAFE', 14))\n"
                "print(check_abac_access('NURSE', 'HOSPITAL_NETWORK', 14))"
            ),
            "solution_code": (
                "def check_abac_access(user_role: str, location: str, hour_24: int) -> bool:\n"
                "    is_role_ok = user_role.upper() == 'SURGEON'\n"
                "    is_loc_ok = location.upper() == 'HOSPITAL_NETWORK'\n"
                "    is_time_ok = 6 <= hour_24 <= 20\n"
                "    return is_role_ok and is_loc_ok and is_time_ok\n\n"
                "print(check_abac_access('SURGEON', 'HOSPITAL_NETWORK', 14))\n"
                "print(check_abac_access('SURGEON', 'EXTERNAL_CAFE', 14))\n"
                "print(check_abac_access('NURSE', 'HOSPITAL_NETWORK', 14))"
            ),
            "expected_output": "True\nFalse\nFalse"
        },
        quizzes=[
            {
                "question": "Which access control model relies on centralized security clearance labels (e.g., Top Secret vs Confidential) where individual file creators cannot grant access to others?",
                "options": ["Mandatory Access Control (MAC)", "Discretionary Access Control (DAC)", "Role-Based Access Control (RBAC)", "Open Source Access"],
                "correct_answer": "Mandatory Access Control (MAC)",
                "explanation": "In MAC, security labels are enforced centrally by the operating system kernel; individual users have zero discretion to share files."
            },
            {
                "question": "In standard desktop operating systems where the user who creates a folder has the power to modify permissions and share it with colleagues, which model is being used?",
                "options": ["Discretionary Access Control (DAC)", "Mandatory Access Control (MAC)", "Attribute-Based Access Control (ABAC)", "Zero-Trust Enforcement"],
                "correct_answer": "Discretionary Access Control (DAC)",
                "explanation": "DAC leaves access decisions to the discretion of the object owner, standard in NTFS and Linux file permissions."
            },
            {
                "question": "What is the primary operational advantage of Role-Based Access Control (RBAC) in large corporate enterprises?",
                "options": [
                    "Permissions are tied to job functions (Roles) rather than individual users, simplifying onboarding, offboarding, and preventing permission creep",
                    "It makes internet connections run faster",
                    "It eliminates the need for passwords",
                    "It works without computer servers"
                ],
                "correct_answer": "Permissions are tied to job functions (Roles) rather than individual users, simplifying onboarding, offboarding, and preventing permission creep",
                "explanation": "When an employee changes departments, administrators simply reassign their role, automatically provisioning appropriate permissions."
            },
            {
                "question": "Which dynamic access control model makes access decisions based on real-time contextual attributes such as user location, time of day, and device health?",
                "options": ["Attribute-Based Access Control (ABAC)", "Discretionary Access Control (DAC)", "Static Access Control (SAC)", "First-In First-Out (FIFO)"],
                "correct_answer": "Attribute-Based Access Control (ABAC)",
                "explanation": "ABAC evaluates granular policy rules combining subject attributes, resource attributes, environmental context, and action types."
            },
            {
                "question": "What is the purpose of the 'Separation of Duties' (SoD) principle in enterprise access governance?",
                "options": [
                    "To prevent internal fraud by requiring high-risk tasks to be divided between two or more distinct individuals with different roles",
                    "To ensure employees work in separate rooms",
                    "To separate mouse cables from keyboard cables",
                    "To divide hard drives into two partitions"
                ],
                "correct_answer": "To prevent internal fraud by requiring high-risk tasks to be divided between two or more distinct individuals with different roles",
                "explanation": "Separation of Duties prevents any single rogue employee from having unchecked power to execute and approve fraudulent transactions."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 28: Single Sign-On (SSO) & Federation
    # ---------------------------------------------------------
    DayBlueprint(
        order=28,
        title="Day 28: Single Sign-On (SSO) & Federation",
        concept="Mastering centralized enterprise identity authentication: Single Sign-On (SSO), Identity Providers (IdP) vs Service Providers (SP), and modern federation protocols (SAML 2.0, OAuth 2.0, OpenID Connect).",
        analogy="Think of visiting a sprawling amusement park with 40 rollercoasters: Without SSO, every single ride requires stopping at an individual ticket booth, filling out an application, showing your ID, and paying cash. With SSO and federation, you show your ID once at the main entrance gate (Identity Provider), receive a validated waterproof wristband (Token), and every rollercoaster ride (Service Provider) lets you right in by scanning the wristband.",
        theory_sections=[
            {
                "heading": "The Mechanics of SSO & Federation",
                "content": (
                    "Single Sign-On allows a user to authenticate once and access multiple independent software applications without re-entering credentials:\n\n"
                    "1. **Identity Provider (IdP)**: The central authoritative authentication server that holds user accounts and validates credentials (e.g., Okta, Microsoft Entra ID, Google Workspace).\n"
                    "2. **Service Provider (SP)**: The target SaaS application where the user wants to work (e.g., Salesforce, Slack, Zoom, AWS Management Console).\n"
                    "3. **Federation**: Trust relationship extending SSO across organizational boundaries and different domains."
                )
            },
            {
                "heading": "Federation Standards: SAML 2.0 vs OIDC",
                "content": (
                    "- **SAML 2.0 (Security Assertion Markup Language)**: Enterprise XML-based standard. The IdP issues a signed XML **SAML Assertion** that the browser posts to the Service Provider.\n"
                    "- **OAuth 2.0**: Authorization framework for delegating API access using Scopes and Access Tokens.\n"
                    "- **OIDC (OpenID Connect)**: An identity layer built directly on top of OAuth 2.0, using lightweight JSON Web Tokens (**JWTs**) to provide authentication."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Decoded JWT ID Token Structure (Header, Payload, Signature)",
                "language": "json",
                "code": (
                    "// OIDC JSON Web Token (JWT) Decoded Payload:\n"
                    "{\n"
                    "  \"iss\": \"https://accounts.google.com\",\n"
                    "  \"sub\": \"1098234871928374\",\n"
                    "  \"aud\": \"my-saas-application.com\",\n"
                    "  \"email\": \"alice@company.com\",\n"
                    "  \"roles\": [\"developer\", \"cloud_operator\"],\n"
                    "  \"exp\": 1735689600,\n"
                    "  \"iat\": 1735686000\n"
                    "}"
                ),
                "explanation": "Service providers inspect cryptographic JWT claims to verify user email, roles, and token expiration."
            },
            {
                "title": "Python: Verifying SSO Token Expiration Timestamp",
                "language": "python",
                "code": (
                    "import time\n\n"
                    "def validate_sso_token(claims: dict) -> dict:\n"
                    "    now = int(time.time())\n"
                    "    if claims.get('exp', 0) < now:\n"
                    "        return {'valid': False, 'error': 'TOKEN_EXPIRED'}\n"
                    "    if claims.get('iss') != 'https://idp.company.com':\n"
                    "        return {'valid': False, 'error': 'UNTRUSTED_ISSUER'}\n"
                    "    return {'valid': True, 'user': claims.get('email')}\n\n"
                    "token = {'iss': 'https://idp.company.com', 'email': 'john@corp.com', 'exp': int(time.time()) + 3600}\n"
                    "print(validate_sso_token(token))"
                ),
                "explanation": "Validates essential claims required for secure Single Sign-On federation processing."
            }
        ],
        coding_challenge={
            "description": "Write a Python function `check_sso_trust(token_issuer: str, trusted_idps: list, token_expired: bool) -> str` that returns 'AUTHORIZED' if issuer is in trusted_idps and token is not expired, 'EXPIRED' if token_expired is True, and 'UNTRUSTED_IDP' otherwise.",
            "starter_code": (
                "def check_sso_trust(token_issuer: str, trusted_idps: list, token_expired: bool) -> str:\n"
                "    # Return 'AUTHORIZED', 'EXPIRED', or 'UNTRUSTED_IDP'\n"
                "    return ''\n\n"
                "trusted = ['https://okta.corp.com', 'https://entra.microsoft.com']\n"
                "print(check_sso_trust('https://okta.corp.com', trusted, False))\n"
                "print(check_sso_trust('https://okta.corp.com', trusted, True))\n"
                "print(check_sso_trust('https://evil-idp.com', trusted, False))"
            ),
            "solution_code": (
                "def check_sso_trust(token_issuer: str, trusted_idps: list, token_expired: bool) -> str:\n"
                "    if token_expired:\n"
                "        return 'EXPIRED'\n"
                "    if token_issuer in trusted_idps:\n"
                "        return 'AUTHORIZED'\n"
                "    return 'UNTRUSTED_IDP'\n\n"
                "trusted = ['https://okta.corp.com', 'https://entra.microsoft.com']\n"
                "print(check_sso_trust('https://okta.corp.com', trusted, False))\n"
                "print(check_sso_trust('https://okta.corp.com', trusted, True))\n"
                "print(check_sso_trust('https://evil-idp.com', trusted, False))"
            ),
            "expected_output": "AUTHORIZED\nEXPIRED\nUNTRUSTED_IDP"
        },
        quizzes=[
            {
                "question": "What is the primary role of the 'Identity Provider' (IdP) in an enterprise Single Sign-On architecture?",
                "options": [
                    "To authenticate user credentials and issue cryptographically signed assertion tokens to service providers",
                    "To print physical photo ID badges",
                    "To manufacture computer memory chips",
                    "To monitor internet download speeds"
                ],
                "correct_answer": "To authenticate user credentials and issue cryptographically signed assertion tokens to service providers",
                "explanation": "The IdP (e.g., Okta, Entra ID) authenticates the user once and generates signed identity tokens that other apps trust."
            },
            {
                "question": "Which modern federation standard is built on top of OAuth 2.0 and utilizes lightweight JSON Web Tokens (JWT) for authentication?",
                "options": ["OpenID Connect (OIDC)", "SAML 1.0", "Telnet", "FTP"],
                "correct_answer": "OpenID Connect (OIDC)",
                "explanation": "OIDC is the modern REST/JSON identity layer built over OAuth 2.0, providing user authentication via signed JWT ID tokens."
            },
            {
                "question": "What is the primary security benefit of deploying Single Sign-On (SSO) across an organization?",
                "options": [
                    "Eliminates password fatigue and reuse across apps, and allows instant global revocation of an employee's access in one central location upon termination",
                    "Allows employees to share passwords with friends",
                    "Automatically disables the company firewall",
                    "Reduces electricity bills"
                ],
                "correct_answer": "Eliminates password fatigue and reuse across apps, and allows instant global revocation of an employee's access in one central location upon termination",
                "explanation": "SSO prevents users from creating dozens of weak passwords and allows HR/IT to revoke access to all company apps with a single click."
            },
            {
                "question": "What is an enterprise 'Service Provider' (SP) in a SAML SSO environment?",
                "options": [
                    "The business application (such as Salesforce, Slack, or Google Workspace) that relies on the IdP for authentication assertions",
                    "The company providing internet fiber optic cables",
                    "The cleaning staff in the building",
                    "The computer repair technician"
                ],
                "correct_answer": "The business application (such as Salesforce, Slack, or Google Workspace) that relies on the IdP for authentication assertions",
                "explanation": "The Service Provider provides the business service, offloading user authentication to the trusted Identity Provider."
            },
            {
                "question": "What is the primary risk associated with Single Sign-On that requires compensating controls like robust MFA?",
                "options": [
                    "If an attacker compromises a user's single SSO password, they gain keys to every connected corporate application simultaneously",
                    "SSO causes monitors to overheat",
                    "SSO makes web browsers crash",
                    "SSO requires replacing all keyboards"
                ],
                "correct_answer": "If an attacker compromises a user's single SSO password, they gain keys to every connected corporate application simultaneously",
                "explanation": "SSO creates a high-value single point of failure: compromising the central account opens the entire application portfolio unless shielded by MFA."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 29: Biometrics and Smart Cards
    # ---------------------------------------------------------
    DayBlueprint(
        order=29,
        title="Day 29: Biometrics and Smart Cards",
        concept="Mastering hardware authentication tokens: Smart Cards (PIV/CAC chip cards), physical cryptography, and Biometric authentication systems (FAR, FRR, CER error rates, and liveness detection).",
        analogy="Think of a bank ATM card vs your face: A smart card is a tamper-resistant mini-computer chip embedded in plastic that performs math inside its own silicon without revealing the secret key. A biometric scanner is a portrait artist who measures the distance between your eyes—if they are too lenient, an imposter gets in (False Accept); if they are too strict, you get locked out with glasses on (False Reject).",
        theory_sections=[
            {
                "heading": "Smart Cards & Hardware Cryptographic Modules",
                "content": (
                    "Smart cards (such as US Department of Defense CAC or federal PIV cards) contain an embedded secure microcontroller:\n"
                    "- The card's private cryptographic key is generated inside the chip and **CAN NEVER BE EXTRACTED**.\n"
                    "- When authenticating, the computer sends a cryptographic challenge to the smart card chip. The chip signs the challenge internally and returns only the digital signature.\n"
                    "- Physical security: Tamper-resistant shielding protects against microscopic laser etching and voltage glitching attacks."
                )
            },
            {
                "heading": "Biometric Accuracy Metrics: FAR, FRR, and CER",
                "content": (
                    "Biometric systems are probabilistic, evaluated by three core error metrics:\n"
                    "1. **FAR (False Acceptance Rate)**: Type II error. The likelihood that an unauthorized imposter is incorrectly authenticated. (Catastrophic for security).\n"
                    "2. **FRR (False Rejection Rate)**: Type I error. The likelihood that an authorized legitimate user is incorrectly rejected. (Frustrating for users).\n"
                    "3. **CER (Crossover Error Rate) / ERR**: The point where FAR and FRR are exactly equal. **The lower the CER, the more accurate the biometric system**.\n"
                    "4. **Liveness Detection**: Prevents spoofing using 3D masks, gelatin fingerprints, or photos by measuring pulse, thermal heat, and involuntary pupil dilation."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Smart Card Service Status and Certificate Propagation (Windows)",
                "language": "bash",
                "code": (
                    "# Windows Smart Card service daemon verification:\n"
                    "Get-Service -Name SCardSvr | Select-Object Name, Status, StartType\n\n"
                    "# Checking smart card certificate storage in personal store:\n"
                    "certutil -scinfo"
                ),
                "explanation": "Sysadmins verify that the Windows Smart Card subsystem is running and reading hardware certificate containers."
            },
            {
                "title": "Python: Calculating Biometric Crossover Error Rate (CER)",
                "language": "python",
                "code": (
                    "def find_crossover_error_rate(threshold_tests: list) -> float:\n"
                    "    # threshold_tests: list of dicts {'threshold': float, 'far': float, 'frr': float}\n"
                    "    best_cer = 100.0\n"
                    "    min_diff = 100.0\n"
                    "    for test in threshold_tests:\n"
                    "        diff = abs(test['far'] - test['frr'])\n"
                    "        if diff < min_diff:\n"
                    "            min_diff = diff\n"
                    "            best_cer = (test['far'] + test['frr']) / 2.0\n"
                    "    return best_cer\n\n"
                    "data = [\n"
                    "    {'threshold': 0.3, 'far': 5.0, 'frr': 0.5},\n"
                    "    {'threshold': 0.5, 'far': 1.8, 'frr': 1.9},\n"
                    "    {'threshold': 0.7, 'far': 0.2, 'frr': 6.0}\n"
                    "]\n"
                    "print(f'Calculated CER: {find_crossover_error_rate(data):.2f}%')"
                ),
                "explanation": "Demonstrates statistical balancing of False Acceptance vs False Rejection rates to benchmark biometric accuracy."
            }
        ],
        coding_challenge={
            "description": "Write a Python function `evaluate_biometric_quality(system_a_cer: float, system_b_cer: float) -> str` that compares two biometric systems by their Crossover Error Rate (CER) and returns 'SYSTEM_A' if A has a lower CER, 'SYSTEM_B' if B has a lower CER, and 'EQUAL' if identical.",
            "starter_code": (
                "def evaluate_biometric_quality(system_a_cer: float, system_b_cer: float) -> str:\n"
                "    # Return 'SYSTEM_A', 'SYSTEM_B', or 'EQUAL'\n"
                "    return ''\n\n"
                "print(evaluate_biometric_quality(1.2, 2.5))\n"
                "print(evaluate_biometric_quality(3.8, 1.1))"
            ),
            "solution_code": (
                "def evaluate_biometric_quality(system_a_cer: float, system_b_cer: float) -> str:\n"
                "    if system_a_cer < system_b_cer:\n"
                "        return 'SYSTEM_A'\n"
                "    elif system_b_cer < system_a_cer:\n"
                "        return 'SYSTEM_B'\n"
                "    return 'EQUAL'\n\n"
                "print(evaluate_biometric_quality(1.2, 2.5))\n"
                "print(evaluate_biometric_quality(3.8, 1.1))"
            ),
            "expected_output": "SYSTEM_A\nSYSTEM_B"
        },
        quizzes=[
            {
                "question": "What is the 'Crossover Error Rate' (CER) in biometric authentication systems?",
                "options": [
                    "The point at which the False Acceptance Rate (FAR) and False Rejection Rate (FRR) are exactly equal, used as the primary benchmark for biometric accuracy",
                    "The rate at which the fingerprint glass gets dirty",
                    "The time it takes to scan a person's retina",
                    "The percentage of employees who forget their passwords"
                ],
                "correct_answer": "The point at which the False Acceptance Rate (FAR) and False Rejection Rate (FRR) are exactly equal, used as the primary benchmark for biometric accuracy",
                "explanation": "CER is the industry gold standard metric: the lower the CER percentage, the higher the overall accuracy and reliability of the biometric device."
            },
            {
                "question": "What is a 'Type II Error' (False Acceptance Rate / FAR) in biometrics?",
                "options": [
                    "An unauthorized imposter is mistakenly recognized by the system and granted access",
                    "A legitimate user is mistakenly denied access",
                    "The biometric scanner turns off unexpectedly",
                    "The software fails to update"
                ],
                "correct_answer": "An unauthorized imposter is mistakenly recognized by the system and granted access",
                "explanation": "FAR represents a dangerous security failure: an unauthorized individual is falsely accepted as a legitimate user."
            },
            {
                "question": "Why is 'Liveness Detection' a critical feature on modern facial recognition and fingerprint biometric scanners?",
                "options": [
                    "To prevent spoofing attacks using 2D printed photographs, recorded videos, or silicone fake fingers",
                    "To verify the user has eaten breakfast",
                    "To ensure the user is smiling",
                    "To measure how fast the user can run"
                ],
                "correct_answer": "To prevent spoofing attacks using 2D printed photographs, recorded videos, or silicone fake fingers",
                "explanation": "Liveness detection verifies real human vitality (blinking, micro-movements, blood flow, 3D depth) to thwart artificial spoof replicas."
            },
            {
                "question": "How does a cryptographic Smart Card protect its private encryption keys from being copied by an attacker?",
                "options": [
                    "Private keys are permanently burned into secure microcontroller hardware memory and cannot be extracted; cryptographic operations occur entirely inside the chip",
                    "The card is coated in bulletproof paint",
                    "Smart cards delete their keys every 10 seconds",
                    "Smart cards do not store keys"
                ],
                "correct_answer": "Private keys are permanently burned into secure microcontroller hardware memory and cannot be extracted; cryptographic operations occur entirely inside the chip",
                "explanation": "Secure cryptoprocessors sign challenge hashes internally without exposing private keys over the physical gold contact pads."
            },
            {
                "question": "If a biometric system's sensitivity threshold is set extremely high, what impact does this have on user experience?",
                "options": [
                    "False Rejection Rate (FRR) increases dramatically, causing legitimate employees to be rejected frequently for minor imperfections",
                    "The system accepts anyone who walks past",
                    "Passwords are automatically deleted",
                    "The camera resolution degrades"
                ],
                "correct_answer": "False Rejection Rate (FRR) increases dramatically, causing legitimate employees to be rejected frequently for minor imperfections",
                "explanation": "Extreme sensitivity minimizes false accepts (high security) at the cost of high false rejections (poor usability and user frustration)."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 30: Principle of Least Privilege (PoLP)
    # ---------------------------------------------------------
    DayBlueprint(
        order=30,
        title="Day 30: Principle of Least Privilege (PoLP)",
        concept="Mastering fundamental security architecture: Principle of Least Privilege (PoLP), Need-to-Know, Just-In-Time (JIT) access, and Privileged Access Management (PAM) to minimize blast radius.",
        analogy="Think of giving keys to a valet parking attendant: You give the valet a special valet key that ONLY starts the engine and locks the glove box. You do NOT give the valet your house key, your master safe combination, and your home security alarm code. If the valet is reckless or robbed, the damage is strictly confined to driving your car.",
        theory_sections=[
            {
                "heading": "Defining the Principle of Least Privilege",
                "content": (
                    "**The Principle of Least Privilege (PoLP)** dictates that users, processes, and service accounts must be granted **ONLY the bare minimum permissions necessary to complete their legitimate job tasks, and for no longer than needed**.\n\n"
                    "Key Operational Benefits:\n"
                    "1. **Minimizes Blast Radius**: If an employee workstation running as a standard unprivileged user downloads ransomware, the malware cannot write to `C:\\Windows\\System32` or infect other domain machines.\n"
                    "2. **Eliminates Privilege Creep**: Employees accumulate extra permissions over years of changing teams. Regular access reviews revoke unnecessary permissions.\n"
                    "3. **Zero Trust Integration**: Trust is never assumed; every request is explicitly verified."
                )
            },
            {
                "heading": "Privileged Access Management (PAM) & JIT Access",
                "content": (
                    "Enterprises manage domain administrator accounts using **PAM solutions** (CyberArk, HashiCorp Vault):\n"
                    "- **Just-In-Time (JIT) Elevation**: Admins work as standard users 99% of the day. When maintenance is required, they request elevated access for a 60-minute window with manager approval.\n"
                    "- **Credential Vaulting**: Passwords for root/admin are stored in encrypted vaults and automatically rotated after every single checkout session."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Auditing Local Administrator Group Memberships (PowerShell & Linux)",
                "language": "bash",
                "code": (
                    "# Windows PowerShell: Auditing members of the sensitive Administrators group:\n"
                    "Get-LocalGroupMember -Group \"Administrators\"\n\n"
                    "# Linux: Auditing users with sudo root privileges in /etc/sudoers:\n"
                    "sudo grep -Po '^sudo.+:\\K.*$' /etc/group\n"
                    "cat /etc/sudoers.d/*"
                ),
                "explanation": "PoLP auditing ensures that standard daily employee accounts are NOT members of local administrative groups."
            },
            {
                "title": "Python: Demonstrating Just-In-Time (JIT) Temporary Privilege Elevation",
                "language": "python",
                "code": (
                    "import time\n\n"
                    "class JITAccessManager:\n"
                    "    def __init__(self):\n"
                    "        self.active_grants = {}  # user -> expiration_timestamp\n"
                    "    \n"
                    "    def grant_temporary_admin(self, user: str, duration_seconds: int = 3600):\n"
                    "        self.active_grants[user] = time.time() + duration_seconds\n"
                    "        print(f'[GRANTED] {user} elevated for {duration_seconds}s.')\n"
                    "    \n"
                    "    def is_admin(self, user: str) -> bool:\n"
                    "        if user in self.active_grants:\n"
                    "            if time.time() < self.active_grants[user]:\n"
                    "                return True\n"
                    "            del self.active_grants[user]  # Expired\n"
                    "        return False\n\n"
                    "jit = JITAccessManager()\n"
                    "jit.grant_temporary_admin('alice', duration_seconds=2)\n"
                    "print('Immediate check:', jit.is_admin('alice'))\n"
                    "time.sleep(2.1)\n"
                    "print('After expiration:', jit.is_admin('alice'))"
                ),
                "explanation": "Demonstrates temporal access boundaries eliminating permanent standing privileges."
            }
        ],
        coding_challenge={
            "description": "Write a Python function `enforce_least_privilege(user_role: str, requested_action: str) -> str` that permits 'BILLING_READ' and 'BILLING_WRITE' only for 'ACCOUNTANT', 'SYSTEM_REBOOT' only for 'SYSADMIN', and allows any role to execute 'PROFILE_VIEW'. Return 'DENIED' for all unauthorized requests.",
            "starter_code": (
                "def enforce_least_privilege(user_role: str, requested_action: str) -> str:\n"
                "    # Return 'ALLOWED' or 'DENIED'\n"
                "    return ''\n\n"
                "print(enforce_least_privilege('ACCOUNTANT', 'BILLING_READ'))\n"
                "print(enforce_least_privilege('ACCOUNTANT', 'SYSTEM_REBOOT'))\n"
                "print(enforce_least_privilege('INTERN', 'PROFILE_VIEW'))"
            ),
            "solution_code": (
                "def enforce_least_privilege(user_role: str, requested_action: str) -> str:\n"
                "    role = user_role.upper()\n"
                "    action = requested_action.upper()\n"
                "    if action == 'PROFILE_VIEW':\n"
                "        return 'ALLOWED'\n"
                "    if role == 'ACCOUNTANT' and action in ['BILLING_READ', 'BILLING_WRITE']:\n"
                "        return 'ALLOWED'\n"
                "    if role == 'SYSADMIN' and action == 'SYSTEM_REBOOT':\n"
                "        return 'ALLOWED'\n"
                "    return 'DENIED'\n\n"
                "print(enforce_least_privilege('ACCOUNTANT', 'BILLING_READ'))\n"
                "print(enforce_least_privilege('ACCOUNTANT', 'SYSTEM_REBOOT'))\n"
                "print(enforce_least_privilege('INTERN', 'PROFILE_VIEW'))"
            ),
            "expected_output": "ALLOWED\nDENIED\nALLOWED"
        },
        quizzes=[
            {
                "question": "What is the core directive of the Principle of Least Privilege (PoLP)?",
                "options": [
                    "Users, applications, and accounts must be granted only the minimum permissions necessary to perform their authorized duties, and no more",
                    "Users should only be allowed to use computers for 1 hour per day",
                    "All employees must share a single guest account",
                    "Printers should be unplugged when not in use"
                ],
                "correct_answer": "Users, applications, and accounts must be granted only the minimum permissions necessary to perform their authorized duties, and no more",
                "explanation": "PoLP limits rights to the bare minimum required to conduct approved tasks, mitigating the impact of compromises or errors."
            },
            {
                "question": "Why is operating as a full Administrator on a daily workstation a severe cybersecurity hazard?",
                "options": [
                    "Any malware, trojan, or ransomware executed by the user runs with full root/administrator privileges, granting it unrestricted ability to modify the OS",
                    "Administrators cannot browse the internet",
                    "It causes the computer screen to flicker",
                    "Administrator accounts expire after 10 minutes"
                ],
                "correct_answer": "Any malware, trojan, or ransomware executed by the user runs with full root/administrator privileges, granting it unrestricted ability to modify the OS",
                "explanation": "Malware inherits the security context of the user executing it. If an admin clicks malware, the malware obtains full administrative control."
            },
            {
                "question": "What is 'Privilege Creep' in enterprise identity governance?",
                "options": [
                    "The gradual accumulation of unnecessary access rights over time as an employee changes roles, projects, and departments without previous rights being revoked",
                    "An unauthorized person crawling into the server room",
                    "A virus that makes the mouse cursor move slowly",
                    "A hacker listening to phone calls"
                ],
                "correct_answer": "The gradual accumulation of unnecessary access rights over time as an employee changes roles, projects, and departments without previous rights being revoked",
                "explanation": "Privilege creep occurs when access permissions are added for new assignments but legacy access rights are never cleaned up."
            },
            {
                "question": "What is 'Just-In-Time' (JIT) privileged access?",
                "options": [
                    "Granting elevated administrative permissions dynamically for a temporary, monitored time window only when required, then automatically revoking them",
                    "Arriving at the office exactly when your shift starts",
                    "Purchasing software at the end of the fiscal year",
                    "Rebooting a server immediately before a crash"
                ],
                "correct_answer": "Granting elevated administrative permissions dynamically for a temporary, monitored time window only when required, then automatically revoking them",
                "explanation": "JIT eliminates standing administrator rights by provisioning elevated privileges on-demand for specific tasks and revoking them upon completion."
            },
            {
                "question": "What is the concept of 'Blast Radius' in security architecture?",
                "options": [
                    "The maximum extent of damage, system compromise, or data exposure that can occur if a specific account or system is breached",
                    "The physical shockwave of an exploding battery",
                    "The distance Wi-Fi waves travel from an access point",
                    "The area covered by security surveillance cameras"
                ],
                "correct_answer": "The maximum extent of damage, system compromise, or data exposure that can occur if a specific account or system is breached",
                "explanation": "PoLP and network segmentation constrain the blast radius, ensuring that compromising a single endpoint does not compromise the entire enterprise."
            }
        ]
    )
]
