"""
Cybersecurity & IT Fundamentals Curriculum - Days 46 to 60
Module 8 (Cont.): Endpoint & Physical Security (Days 46-50)
Module 9: Security Operations & Incident Response (Days 51-54)
Module 10: Risk Management & Compliance (Days 55-60)

Universal Standard Compliant:
- ELI5 markdown theory with beginner analogies
- Shell / Python / configuration snippets
- Daily hands-on coding or practical challenge
- Exactly 5 MCQs per day (75 total for Days 46-60)
"""

from seeder.course_blueprint import DayBlueprint

DAYS_46_TO_60 = [
    # ---------------------------------------------------------
    # Day 46: Patch Management (OS and Software Updates)
    # ---------------------------------------------------------
    DayBlueprint(
        order=46,
        title="Day 46: Patch Management (OS and Software Updates)",
        concept="Mastering vulnerability remediation lifecycles: Patch Management (testing, staging, deploying), Microsoft Patch Tuesday, Zero-Day out-of-band hotfixes, and automated patch orchestration.",
        analogy="Think of patching a roof: A software flaw is a hole in your roof tiles discovered during a storm. Patch Management is the roofing repair team that doesn't just slap tape on it while it rains; they test the replacement tiles in a warehouse first to ensure they won't crack (Staging), apply the sealant carefully on Saturday morning (Maintenance Window), and inspect the attic to verify no leaks remain.",
        theory_sections=[
            {
                "heading": "The Strategic Role of Patch Management",
                "content": (
                    "Over 80% of successful enterprise breaches exploit vulnerabilities for which **a vendor patch had already been available for months**:\n\n"
                    "1. **The Vulnerability Window**: The dangerous time interval between when a vendor announces a CVE vulnerability and when an enterprise actually applies the patch. Threat actors reverse-engineer vendor patches to create working exploits within 48 hours.\n"
                    "2. **Patch Tuesday**: Microsoft releases monthly security updates on the second Tuesday of each month. Critical out-of-band patches are pushed immediately for active zero-days.\n"
                    "3. **The 4-Stage Patch Lifecycle**:\n"
                    "   - *Discovery*: Automated scanning identifies unpatched servers and third-party software (Chrome, Zoom, Adobe).\n"
                    "   - *Testing / Staging*: Applying patches in a non-production lab environment to ensure updates do not break critical line-of-business applications.\n"
                    "   - *Deployment*: Pushing patches during scheduled maintenance windows via WSUS, Intune, or Ansible.\n"
                    "   - *Verification*: Auditing compliance reports to ensure 100% endpoint coverage."
                )
            },
            {
                "heading": "Case Study: Equifax Breach (2017)",
                "content": (
                    "The massive Equifax breach (147 million sensitive records leaked) was caused by a single unpatched Apache Struts vulnerability (CVE-2017-5638). A patch had been available for two full months, but Equifax's internal patch management team failed to apply it."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Querying and Applying System Patches via CLI",
                "language": "bash",
                "code": (
                    "# Linux (Debian/Ubuntu) automated security update check:\n"
                    "sudo apt update\n"
                    "sudo apt list --upgradable\n"
                    "sudo apt-get --just-print upgrade | grep -i security\n\n"
                    "# Windows PowerShell: Querying installed hotfixes:\n"
                    "Get-HotFix | Sort-Object InstalledOn -Descending | Select-Object -First 5"
                ),
                "explanation": "Essential sysadmin commands to audit patch installation dates and identify pending security updates."
            },
            {
                "title": "Python: Auditing Server Patch SLA Compliance",
                "language": "python",
                "code": (
                    "import datetime\n\n"
                    "def audit_patch_sla(cve_release_date: str, patch_installed: bool, severity: str) -> dict:\n"
                    "    release = datetime.datetime.strptime(cve_release_date, '%Y-%m-%d').date()\n"
                    "    days_open = (datetime.date.today() - release).days\n"
                    "    sla_days = {'CRITICAL': 7, 'HIGH': 30, 'MEDIUM': 90}.get(severity.upper(), 90)\n"
                    "    \n"
                    "    if not patch_installed and days_open > sla_days:\n"
                    "        return {'compliant': False, 'status': f'VIOLATION: {severity} patch missing for {days_open} days (SLA: {sla_days}d)'}\n"
                    "    return {'compliant': True, 'status': 'WITHIN_SLA'}\n\n"
                    "print(audit_patch_sla('2024-01-01', False, 'CRITICAL'))\n"
                    "print(audit_patch_sla('2024-09-25', False, 'CRITICAL'))"
                ),
                "explanation": "Calculates organizational compliance against corporate patch remediation Service Level Agreements (SLAs)."
            }
        ],
        coding_challenge={
            "description": "Write a Python function `patch_priority_sla(cvss_score: float) -> int` that returns maximum allowed remediation days: 7 days for CVSS >= 9.0 (Critical), 30 days for CVSS >= 7.0 (High), 60 days for CVSS >= 4.0 (Medium), and 90 days for Low.",
            "starter_code": (
                "def patch_priority_sla(cvss_score: float) -> int:\n"
                "    # Return maximum allowed days to patch\n"
                "    return 0\n\n"
                "print(patch_priority_sla(9.8))\n"
                "print(patch_priority_sla(7.5))\n"
                "print(patch_priority_sla(5.0))"
            ),
            "solution_code": (
                "def patch_priority_sla(cvss_score: float) -> int:\n"
                "    if cvss_score >= 9.0:\n"
                "        return 7\n"
                "    elif cvss_score >= 7.0:\n"
                "        return 30\n"
                "    elif cvss_score >= 4.0:\n"
                "        return 60\n"
                "    return 90\n\n"
                "print(patch_priority_sla(9.8))\n"
                "print(patch_priority_sla(7.5))\n"
                "print(patch_priority_sla(5.0))"
            ),
            "expected_output": "7\n30\n60"
        },
        quizzes=[
            {
                "question": "Why is testing security patches in a staging environment essential before deploying them across production enterprise servers?",
                "options": [
                    "Patches can occasionally conflict with custom line-of-business applications, corrupt databases, or cause unexpected server crashes and outages",
                    "To allow cybercriminals to test the patch first",
                    "Because software patches are illegal to install without government testing",
                    "To drain residual electricity from the servers"
                ],
                "correct_answer": "Patches can occasionally conflict with custom line-of-business applications, corrupt databases, or cause unexpected server crashes and outages",
                "explanation": "Staging verifies operational stability: ensuring security fixes do not inadvertently break core business services."
            },
            {
                "question": "What is 'Patch Tuesday' in the technology industry?",
                "options": [
                    "The second Tuesday of each month when Microsoft regularly releases scheduled security patches and updates for Windows systems",
                    "A holiday celebrating computer repair technicians",
                    "A day when all office computers are turned off",
                    "A discount day for purchasing laptop computers"
                ],
                "correct_answer": "The second Tuesday of each month when Microsoft regularly releases scheduled security patches and updates for Windows systems",
                "explanation": "Microsoft standardizes regular non-emergency security patch distribution on the second Tuesday of each month."
            },
            {
                "question": "What is an 'Out-of-Band' security patch?",
                "options": [
                    "An emergency patch released immediately outside the normal monthly update schedule to remediate an active, critical zero-day exploit",
                    "A patch delivered via musical radio waves",
                    "An update applied only to disconnected tape drives",
                    "A patch that does not require restarting the computer"
                ],
                "correct_answer": "An emergency patch released immediately outside the normal monthly update schedule to remediate an active, critical zero-day exploit",
                "explanation": "When zero-day exploits actively threaten systems in the wild, vendors release out-of-band emergency fixes immediately."
            },
            {
                "question": "What historic mega-breach exposed 147 million consumers' sensitive records because the organization failed to patch an Apache Struts flaw two months after the patch was released?",
                "options": ["The Equifax Data Breach (2017)", "The Apollo 11 moon landing", "The creation of Bitcoin", "The invention of the iPhone"],
                "correct_answer": "The Equifax Data Breach (2017)",
                "explanation": "Equifax suffered one of history's largest breaches because an internal patch management failure left known CVE-2017-5638 unpatched."
            },
            {
                "question": "Why do threat actors aggressively reverse-engineer software patches the moment a vendor publishes them?",
                "options": [
                    "To identify the exact underlying vulnerability being fixed and create automated exploits targeting organizations that have not yet deployed the patch",
                    "To help the vendor write cleaner code",
                    "To translate the patch into foreign languages",
                    "To improve the graphics of the operating system"
                ],
                "correct_answer": "To identify the exact underlying vulnerability being fixed and create automated exploits targeting organizations that have not yet deployed the patch",
                "explanation": "Comparing unpatched and patched binaries (binary diffing) reveals the vulnerability blueprint, weaponizing exploits before companies patch."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 47: Hardening (System security steps)
    # ---------------------------------------------------------
    DayBlueprint(
        order=47,
        title="Day 47: Hardening (System security steps)",
        concept="Mastering system defense-in-depth: Operating system hardening, disabling unnecessary services, closing unused ports, removing default accounts, CIS (Center for Internet Security) Benchmarks, and automated baselining.",
        analogy="Think of preparing a fortress for battle: An out-of-the-box computer is like a castle with 10 open gates, 50 decorative side windows, and the default master gate password set to 'admin'. System Hardening is bricking up all unnecessary side windows, locking 9 of the gates permanently, replacing standard wooden doors with reinforced steel, and firing anyone who uses default keys.",
        theory_sections=[
            {
                "heading": "Principles of System Hardening",
                "content": (
                    "Default out-of-the-box operating systems prioritize usability over security. **System Hardening** reduces the attack surface by stripping away every non-essential feature:\n\n"
                    "1. **Disable Unnecessary Services & Protocols**: Shut down Telnet, FTP, SMBv1, and unused web daemons. If a service isn't running, it cannot be exploited.\n"
                    "2. **Disable or Rename Default Accounts**: Disable the built-in `Guest` account and rename `Administrator` to complicate automated brute-force attacks.\n"
                    "3. **Enforce Strong Password & Lockout Policies**: Minimum length (14+ characters), complexity, and account lockout thresholds.\n"
                    "4. **Remove Unused Software & Bloatware**: Uninstall Xbox services, games, and trial software from corporate server images.\n"
                    "5. **Principle of Least Functionality**: A database server should do NOTHING except run database queries—no web browser, no email client, no office suite."
                )
            },
            {
                "heading": "CIS Benchmarks & DISA STIGs",
                "content": (
                    "Enterprise engineers don't guess hardening settings; they adhere to **CIS (Center for Internet Security) Benchmarks** and DoD **STIGs (Security Technical Implementation Guides)**. Automated compliance scanners audit systems against these exact hardening checklists."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Hardening Scripts (Disabling Insecure SMBv1 and Remote Services)",
                "language": "bash",
                "code": (
                    "# Windows PowerShell: Disabling vulnerable legacy SMBv1 (WannaCry vector):\n"
                    "Disable-WindowsOptionalFeature -Online -FeatureName \"SMB1Protocol\" -NoRestart\n\n"
                    "# Disabling the insecure built-in Guest account:\n"
                    "Disable-LocalUser -Name \"Guest\"\n\n"
                    "# Linux: Hardening SSH daemon (/etc/ssh/sshd_config):\n"
                    "# PermitRootLogin no\n"
                    "# PasswordAuthentication no  (Mandate SSH keys only)\n"
                    "sudo systemctl restart sshd"
                ),
                "explanation": "Essential baseline configuration changes removing primary initial compromise vectors."
            },
            {
                "title": "Python: Auditing Server Hardening Score Against Baseline",
                "language": "python",
                "code": (
                    "def audit_system_hardening(checks: dict) -> dict:\n"
                    "    # checks: {'check_name': bool_passed}\n"
                    "    total = len(checks)\n"
                    "    passed = sum(1 for v in checks.values() if v is True)\n"
                    "    score = (passed / total) * 100\n"
                    "    failed = [k for k, v in checks.items() if v is False]\n"
                    "    return {'score_percent': score, 'status': 'PASS' if score >= 80 else 'FAIL', 'remediations_needed': failed}\n\n"
                    "server_audit = {\n"
                    "    'smbv1_disabled': True,\n"
                    "    'guest_account_disabled': True,\n"
                    "    'root_ssh_disabled': False,\n"
                    "    'firewall_active': True\n"
                    "}\n"
                    "print(audit_system_hardening(server_audit))"
                ),
                "explanation": "Automated security configuration baseline assessment scoring."
            }
        ],
        coding_challenge={
            "description": "Write a Python function `is_service_allowed(service_name: str, server_role: str) -> bool` that enforces least functionality. If server_role == 'DATABASE', only 'POSTGRESQL' and 'SSH' are allowed. If server_role == 'WEB', only 'NGINX', 'HTTPS', and 'SSH' are allowed. Return False for any other service.",
            "starter_code": (
                "def is_service_allowed(service_name: str, server_role: str) -> bool:\n"
                "    # Return True if allowed by hardening policy, False otherwise\n"
                "    return False\n\n"
                "print(is_service_allowed('POSTGRESQL', 'DATABASE'))\n"
                "print(is_service_allowed('PRINT_SPOOLER', 'DATABASE'))\n"
                "print(is_service_allowed('NGINX', 'WEB'))"
            ),
            "solution_code": (
                "def is_service_allowed(service_name: str, server_role: str) -> bool:\n"
                "    s = service_name.upper()\n"
                "    r = server_role.upper()\n"
                "    allowed = {\n"
                "        'DATABASE': {'POSTGRESQL', 'SSH'},\n"
                "        'WEB': {'NGINX', 'HTTPS', 'SSH'}\n"
                "    }\n"
                "    return s in allowed.get(r, set())\n\n"
                "print(is_service_allowed('POSTGRESQL', 'DATABASE'))\n"
                "print(is_service_allowed('PRINT_SPOOLER', 'DATABASE'))\n"
                "print(is_service_allowed('NGINX', 'WEB'))"
            ),
            "expected_output": "True\nFalse\nTrue"
        },
        quizzes=[
            {
                "question": "What is the primary objective of System Hardening in cybersecurity?",
                "options": [
                    "To reduce the system's attack surface by eliminating non-essential services, closing unused ports, and enforcing strict security configurations",
                    "To install physical metal armor around the server rack",
                    "To make computers heavy so they cannot be carried away",
                    "To delete all files from the operating system"
                ],
                "correct_answer": "To reduce the system's attack surface by eliminating non-essential services, closing unused ports, and enforcing strict security configurations",
                "explanation": "Hardening strips away unnecessary services, default credentials, and insecure protocols to minimize potential exploit vectors."
            },
            {
                "question": "What are CIS (Center for Internet Security) Benchmarks?",
                "options": [
                    "Globally recognized, consensus-based best-practice configuration guidelines for hardening operating systems, databases, and network devices",
                    "Speed tests measuring computer monitor refresh rates",
                    "A ranking of the fastest internet service providers",
                    "A list of the world's most expensive computers"
                ],
                "correct_answer": "Globally recognized, consensus-based best-practice configuration guidelines for hardening operating systems, databases, and network devices",
                "explanation": "CIS Benchmarks provide prescriptive, step-by-step checklists used by enterprises worldwide to harden infrastructure."
            },
            {
                "question": "Why is disabling the legacy SMBv1 file-sharing protocol considered a mandatory hardening step across Windows networks?",
                "options": [
                    "SMBv1 contains severe architectural vulnerabilities (such as EternalBlue) that allow unauthenticated remote code execution and ransomware propagation",
                    "SMBv1 only works on black and white monitors",
                    "Microsoft charges a daily fee to use SMBv1",
                    "SMBv1 causes keyboards to disconnect"
                ],
                "correct_answer": "SMBv1 contains severe architectural vulnerabilities (such as EternalBlue) that allow unauthenticated remote code execution and ransomware propagation",
                "explanation": "WannaCry and NotPetya leveraged EternalBlue flaws in SMBv1 to infect hundreds of thousands of computers globally within hours."
            },
            {
                "question": "What does the 'Principle of Least Functionality' dictate for a dedicated enterprise production server?",
                "options": [
                    "A system should be configured to provide only essential capabilities and services specifically required for its intended business role, and nothing else",
                    "Servers should only be powered on 4 hours per day",
                    "Computers should have only one user account",
                    "Servers should never have hard drives"
                ],
                "correct_answer": "A system should be configured to provide only essential capabilities and services specifically required for its intended business role, and nothing else",
                "explanation": "A production database server should only run database services—no games, web browsers, media players, or extra compilers."
            },
            {
                "question": "In Linux server hardening, why is setting `PermitRootLogin no` in the SSH configuration file (`/etc/ssh/sshd_config`) strongly recommended?",
                "options": [
                    "It forces administrators to log in using individual named unprivileged user accounts with SSH keys, preventing direct brute-force attacks on the all-powerful root account",
                    "It deletes the root account permanently",
                    "It makes Linux run as Windows",
                    "It disables internet access on the server"
                ],
                "correct_answer": "It forces administrators to log in using individual named unprivileged user accounts with SSH keys, preventing direct brute-force attacks on the all-powerful root account",
                "explanation": "Disabling direct root logins enforces individual accountability (via `sudo`) and neutralizes automated dictionary bots attacking the `root` username."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 48: Mobile Device Management (MDM) & BYOD policies
    # ---------------------------------------------------------
    DayBlueprint(
        order=48,
        title="Day 48: Mobile Device Management (MDM) & BYOD policies",
        concept="Mastering enterprise mobility security: MDM (Mobile Device Management), MAM (Mobile Application Management), BYOD (Bring Your Own Device) challenges, containerization, and remote wipe capabilities.",
        analogy="Think of using your personal car for company delivery deliveries: In a pure BYOD free-for-all, your personal groceries, kids' toys, and company confidential packages are thrown together in the trunk. MDM/MAM is installing a locked, fireproof steel company safe inside your trunk (Containerization). If you resign from the company, the company doesn't tow your entire car away; they just send a signal that locks and wipes the contents of that steel safe (Selective Remote Wipe).",
        theory_sections=[
            {
                "heading": "Mobile Deployment Frameworks",
                "content": (
                    "Enterprises manage smartphones, tablets, and laptops across different ownership models:\n\n"
                    "1. **BYOD (Bring Your Own Device)**: Employees use personal smartphones for corporate email. High employee privacy concerns; significant corporate data leak risk.\n"
                    "2. **COPE (Corporate-Owned, Personally-Enabled)**: Company buys the device, but allows personal apps and photos.\n"
                    "3. **COBO (Corporate-Owned, Business-Only)**: Strict business-only usage. No personal accounts permitted.\n"
                    "4. **CYOD (Choose Your Own Device)**: Employees select from a pre-approved list of company-purchased smartphones."
                )
            },
            {
                "heading": "MDM vs MAM & Remote Wipe",
                "content": (
                    "- **MDM (Mobile Device Management - Microsoft Intune, Jamf)**: Manages the entire physical hardware device: enforcing lock-screen PINs, mandating OS encryption, blocking jailbroken/rooted devices, and executing full device wipes.\n"
                    "- **MAM (Mobile Application Management)**: Manages only the specific corporate applications (Outlook, Teams). Enforces copy/paste restrictions (preventing users from copying confidential financial data from corporate Outlook into personal WhatsApp).\n"
                    "- **Selective Wipe vs Full Wipe**: Selective Wipe deletes corporate emails, files, and tokens while leaving personal family photos and contacts completely untouched."
                )
            }
        ],
        code_snippets=[
            {
                "title": "MDM Policy Configuration Elements (Intune & Jamf Profile XML)",
                "language": "json",
                "code": (
                    "// Sample MDM Mobile Security Policy Payload:\n"
                    "{\n"
                    "  \"policyName\": \"Corporate_Android_Security_Baseline\",\n"
                    "  \"passwordMinimumLength\": 8,\n"
                    "  \"passwordComplexity\": \"alphanumeric\",\n"
                    "  \"maxFailedAttemptsBeforeWipe\": 10,\n"
                    "  \"storageEncryptionMandatory\": true,\n"
                    "  \"blockJailbrokenRootedDevices\": true,\n"
                    "  \"allowCamera\": false,\n"
                    "  \"allowUntrustedAppSideloading\": false\n"
                    "}"
                ),
                "explanation": "MDM server profiles push configuration baselines over-the-air to enforce lockouts and encryption."
            },
            {
                "title": "Python: Simulating BYOD Root / Jailbreak Detection Triage",
                "language": "python",
                "code": (
                    "def audit_mobile_compliance(device: dict) -> dict:\n"
                    "    violations = []\n"
                    "    if device.get('is_rooted_or_jailbroken'):\n"
                    "        violations.append('DEVICE_INTEGRITY_COMPROMISED (Rooted/Jailbroken)')\n"
                    "    if not device.get('storage_encrypted'):\n"
                    "        violations.append('STORAGE_NOT_ENCRYPTED')\n"
                    "    if device.get('pin_length', 0) < 6:\n"
                    "        violations.append('PIN_TOO_SHORT')\n"
                    "        \n"
                    "    is_compliant = len(violations) == 0\n"
                    "    return {'compliant': is_compliant, 'violations': violations, 'action': 'ALLOW' if is_compliant else 'BLOCK_ACCESS'}\n\n"
                    "print(audit_mobile_compliance({'is_rooted_or_jailbroken': False, 'storage_encrypted': True, 'pin_length': 6}))\n"
                    "print(audit_mobile_compliance({'is_rooted_or_jailbroken': True, 'storage_encrypted': True, 'pin_length': 4}))"
                ),
                "explanation": "Mobile gateway access logic blocking corporate email access on jailbroken devices."
            }
        ],
        coding_challenge={
            "description": "Write a Python function `select_wipe_type(is_byod_personal: bool, device_stolen: bool) -> str` that returns 'SELECTIVE_WIPE' if device is personal BYOD and not stolen (employee resigned), 'FULL_FACTORY_WIPE' if device is corporate-owned or stolen, and 'NO_ACTION' otherwise.",
            "starter_code": (
                "def select_wipe_type(is_byod_personal: bool, device_stolen: bool) -> str:\n"
                "    # Return 'SELECTIVE_WIPE', 'FULL_FACTORY_WIPE', or 'NO_ACTION'\n"
                "    return ''\n\n"
                "print(select_wipe_type(True, False))   # BYOD resignation\n"
                "print(select_wipe_type(True, True))    # BYOD stolen\n"
                "print(select_wipe_type(False, False))  # Corporate device"
            ),
            "solution_code": (
                "def select_wipe_type(is_byod_personal: bool, device_stolen: bool) -> str:\n"
                "    if device_stolen:\n"
                "        return 'FULL_FACTORY_WIPE'\n"
                "    if is_byod_personal:\n"
                "        return 'SELECTIVE_WIPE'\n"
                "    return 'FULL_FACTORY_WIPE'\n\n"
                "print(select_wipe_type(True, False))\n"
                "print(select_wipe_type(True, True))\n"
                "print(select_wipe_type(False, False))"
            ),
            "expected_output": "SELECTIVE_WIPE\nFULL_FACTORY_WIPE\nFULL_FACTORY_WIPE"
        },
        quizzes=[
            {
                "question": "What is the primary difference between a 'Full Device Wipe' and a 'Selective Wipe' in Mobile Device Management (MDM)?",
                "options": [
                    "A Full Wipe restores the entire phone to factory default erasing everything; a Selective Wipe erases ONLY corporate data and apps, leaving personal photos intact",
                    "A Selective Wipe changes the wallpaper",
                    "A Full Wipe only deletes music files",
                    "There is no difference"
                ],
                "correct_answer": "A Full Wipe restores the entire phone to factory default erasing everything; a Selective Wipe erases ONLY corporate data and apps, leaving personal photos intact",
                "explanation": "Selective wipe is critical for BYOD: removing corporate emails when an employee departs without destroying their personal personal memories."
            },
            {
                "question": "Why do enterprise MDM policies strictly forbid rooted (Android) or jailbroken (iOS) devices from accessing corporate networks?",
                "options": [
                    "Rooting and jailbreaking bypass core operating system sandboxing and permission controls, exposing corporate apps to spyware and malware",
                    "Rooted phones cannot connect to 5G networks",
                    "Jailbroken phones use too much battery power",
                    "Apple and Google sue companies that allow rooted phones"
                ],
                "correct_answer": "Rooting and jailbreaking bypass core operating system sandboxing and permission controls, exposing corporate apps to spyware and malware",
                "explanation": "Jailbreaking breaks application isolation boundaries, allowing untrusted apps to hook memory and steal corporate tokens."
            },
            {
                "question": "What is the focus of Mobile Application Management (MAM) compared to Mobile Device Management (MDM)?",
                "options": [
                    "MAM focuses specifically on controlling and securing corporate applications and data containers rather than managing the entire physical device",
                    "MAM manages battery manufacturing",
                    "MAM tracks the phone's physical weight",
                    "MAM designs mobile games"
                ],
                "correct_answer": "MAM focuses specifically on controlling and securing corporate applications and data containers rather than managing the entire physical device",
                "explanation": "MAM secures specific apps (e.g., preventing copy/paste from work Outlook into personal apps) without needing full hardware control."
            },
            {
                "question": "Under a 'BYOD' (Bring Your Own Device) policy, who legally owns the physical smartphone hardware?",
                "options": ["The individual employee", "The company employer", "The mobile cellular carrier", "The phone manufacturer"],
                "correct_answer": "The individual employee",
                "explanation": "BYOD means the employee owns the hardware and data plan, requiring balanced policies that protect corporate data while respecting personal privacy."
            },
            {
                "question": "What is 'Containerization' on mobile endpoints?",
                "options": [
                    "Creating an isolated, encrypted partition on the mobile device that separates corporate applications and data from personal applications",
                    "Placing the phone inside a waterproof plastic container",
                    "Shipping phones overseas in freight containers",
                    "Installing all apps on a microSD card"
                ],
                "correct_answer": "Creating an isolated, encrypted partition on the mobile device that separates corporate applications and data from personal applications",
                "explanation": "Containerization creates a cryptographic wall between personal space and work space, stopping cross-app contamination."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 49: Physical Security Controls (Locks, Badges, Mantraps, CCTV)
    # ---------------------------------------------------------
    DayBlueprint(
        order=49,
        title="Day 49: Physical Security Controls (Locks, Badges, Mantraps, CCTV)",
        concept="Mastering physical cybersecurity perimeters: Defense-in-depth physical barriers, Access control vestibules (Mantraps), Smart badge readers (RFID/NFC), Biometric locks, CCTV surveillance, and Faraday cages.",
        analogy="Think of medieval castles: Even with the best computer passwords in the world, if a thief can physically walk into your server room with a screwdriver and unplug the hard drive, your software security is useless. Physical security is the moat, drawbridge, portcullis, outer wall, guard dogs, and watchtowers that stop physical intruders before they touch silicon.",
        theory_sections=[
            {
                "heading": "Physical Defense-in-Depth Perimeters",
                "content": (
                    "Physical security operates in concentric layers:\n\n"
                    "1. **Perimeter Layer (Property Boundary)**: Chain-link fences, razor wire, bollards (preventing vehicle ramming), security gates, guard shacks.\n"
                    "2. **Building Exterior**: High-intensity lighting, security CCTV cameras with PTZ, motion sensors, visitor sign-in desks.\n"
                    "3. **Internal Corridors**: Electronic RFID badge readers, visitor badges with physical escorts.\n"
                    "4. **Access Control Vestibules (Mantraps)**: A small room with two interlocking doors where Door B cannot open until Door A closes and locks. Prevents tailgating and unauthorized entry into datacenters.\n"
                    "5. **Server Room / Secure Enclave**: Biometric retinal/fingerprint scanners, locked server rack cages, raised floors with under-floor fire suppression.\n"
                    "6. **Faraday Cages**: Metal mesh shielding preventing electromagnetic radiation (TEMPEST) and RF radio waves from leaking outward."
                )
            },
            {
                "heading": "Physical Environmental Controls",
                "content": (
                    "- **HVAC & Humidity**: Data centers maintain ~68-72°F and 40-50% humidity. Too dry causes Electrostatic Discharge (ESD); too humid causes corrosion.\n"
                    "- **Fire Suppression**: Clean agent systems (FM-200, Novec 1230, Inergen) starve fires of heat/oxygen without spraying water on active electronic servers."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Simulating Electronic Access Control Door Lock Controller",
                "language": "python",
                "code": (
                    "class MantrapController:\n"
                    "    def __init__(self):\n"
                    "        self.outer_door_locked = True\n"
                    "        self.inner_door_locked = True\n"
                    "        self.occupant_badge_scanned = False\n"
                    "    \n"
                    "    def step_1_open_outer(self, badge_id: str) -> str:\n"
                    "        if badge_id == 'VALID_DATACENTER_BADGE':\n"
                    "            self.outer_door_locked = False\n"
                    "            return 'OUTER_DOOR_UNLOCKED (Step inside airlock)'\n"
                    "        return 'ACCESS_DENIED'\n"
                    "    \n"
                    "    def step_2_open_inner(self, outer_closed: bool, biometric_passed: bool) -> str:\n"
                    "        # Security rule: Inner door CANNOT unlock unless outer door is fully closed!\n"
                    "        if not outer_closed:\n"
                    "            return 'INTERLOCK_ENGAGED: Cannot unlock inner door while outer door is open!'\n"
                    "        if biometric_passed:\n"
                    "            self.inner_door_locked = False\n"
                    "            return 'INNER_DOOR_UNLOCKED: Access granted to Server Room.'\n"
                    "        return 'BIOMETRIC_FAILED'\n\n"
                    "mantrap = MantrapController()\n"
                    "print(mantrap.step_1_open_outer('VALID_DATACENTER_BADGE'))\n"
                    "print(mantrap.step_2_open_inner(outer_closed=True, biometric_passed=True))"
                ),
                "explanation": "Logic governing access control vestibules preventing multiple individuals from entering high-security server rooms."
            },
            {
                "title": "Verifying Server Room Environmental Sensor Telemetry via CLI",
                "language": "bash",
                "code": (
                    "# Querying environmental monitor sensor (SNMP protocol):\n"
                    "snmpget -v2c -c public 10.10.50.25 .1.3.6.1.4.1.318.1.1.10.2.3.2.1.4.1\n"
                    "# Output: INTEGER: 68 (Temperature: 68 degrees Fahrenheit)\n"
                    "snmpget -v2c -c public 10.10.50.25 .1.3.6.1.4.1.318.1.1.10.2.3.2.1.6.1\n"
                    "# Output: INTEGER: 45 (Relative Humidity: 45%)"
                ),
                "explanation": "Datacenter infrastructure management tools monitor temperature and humidity to prevent hardware burnout."
            }
        ],
        coding_challenge={
            "description": "Write a Python function `check_mantrap_interlock(outer_door_open: bool, inner_door_open: bool) -> bool` that returns True if the state is SAFE (at least one door is closed, or both closed), and False if it is a SECURITY_VIOLATION (both doors are open simultaneously).",
            "starter_code": (
                "def check_mantrap_interlock(outer_door_open: bool, inner_door_open: bool) -> bool:\n"
                "    # Return True if safe, False if security violation\n"
                "    return False\n\n"
                "print(check_mantrap_interlock(False, False))  # Both closed\n"
                "print(check_mantrap_interlock(True, False))   # Outer open, inner closed\n"
                "print(check_mantrap_interlock(True, True))    # Both open!"
            ),
            "solution_code": (
                "def check_mantrap_interlock(outer_door_open: bool, inner_door_open: bool) -> bool:\n"
                "    # If both doors are open simultaneously, it's a violation\n"
                "    if outer_door_open and inner_door_open:\n"
                "        return False\n"
                "    return True\n\n"
                "print(check_mantrap_interlock(False, False))\n"
                "print(check_mantrap_interlock(True, False))\n"
                "print(check_mantrap_interlock(True, True))"
            ),
            "expected_output": "True\nTrue\nFalse"
        },
        quizzes=[
            {
                "question": "What is an 'Access Control Vestibule' (commonly known as a Mantrap) in physical security?",
                "options": [
                    "A double-door airlock system where the first door must fully close and lock before the second door will unlock, preventing tailgating into secure areas",
                    "A bear trap placed on the office lawn",
                    "A revolving door at a shopping mall",
                    "A security camera with night vision"
                ],
                "correct_answer": "A double-door airlock system where the first door must fully close and lock before the second door will unlock, preventing tailgating into secure areas",
                "explanation": "Mantraps enforce one-person-at-a-time physical authentication, physically blocking tailgating into datacenters."
            },
            {
                "question": "What is the purpose of physical 'Bollards' installed outside corporate headquarters and datacenter buildings?",
                "options": [
                    "Heavy concrete or steel vertical posts engineered to prevent vehicular ramming attacks against building entrances",
                    "Antennas that provide free public Wi-Fi",
                    "Pipes that collect rainwater for server cooling",
                    "Decorative light posts for evening workers"
                ],
                "correct_answer": "Heavy concrete or steel vertical posts engineered to prevent vehicular ramming attacks against building entrances",
                "explanation": "Security bollards physically stop vehicles from crashing through glass lobbies or perimeter fences into facilities."
            },
            {
                "question": "Why are 'Clean Agent' fire suppression systems (like FM-200 or Novec 1230) used in server rooms instead of standard water sprinkler systems?",
                "options": [
                    "They extinguish fires by chemical cooling and oxygen reduction without leaving conductive water residue that destroys active electrical computer circuitry",
                    "They smell like flowers",
                    "Water is too expensive to install in datacenters",
                    "Water causes computer hard drives to spin backwards"
                ],
                "correct_answer": "They extinguish fires by chemical cooling and oxygen reduction without leaving conductive water residue that destroys active electrical computer circuitry",
                "explanation": "Clean agents suppress fire in seconds without conducting electricity or damaging sensitive electronic computing equipment."
            },
            {
                "question": "What is a 'Faraday Cage'?",
                "options": [
                    "An enclosure formed by conductive mesh shielding that blocks electromagnetic radiation and radio frequency signals from entering or escaping",
                    "A metal rack used to store laptop computers",
                    "A cage used to secure server backup tapes",
                    "A plastic cover placed over office keyboards"
                ],
                "correct_answer": "An enclosure formed by conductive mesh shielding that blocks electromagnetic radiation and radio frequency signals from entering or escaping",
                "explanation": "Faraday cages prevent RF signal eavesdropping (TEMPEST) and block wireless communication with seized forensic devices."
            },
            {
                "question": "What environmental hazard occurs in a server room if the humidity levels drop significantly below 30-40%?",
                "options": [
                    "Severe risk of Electrostatic Discharge (ESD) buildup, which can instantly fry sensitive silicon microchips upon human touch",
                    "Computers begin to freeze into ice",
                    "The internet cable loses connectivity",
                    "The servers catch fire spontaneously"
                ],
                "correct_answer": "Severe risk of Electrostatic Discharge (ESD) buildup, which can instantly fry sensitive silicon microchips upon human touch",
                "explanation": "Low humidity creates dry air that generates high static electrical charges, leading to ESD damage to exposed circuits."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 50: Secure Data Destruction (Shredding, Degaussing, Wiping)
    # ---------------------------------------------------------
    DayBlueprint(
        order=50,
        title="Day 50: Secure Data Destruction (Shredding, Degaussing, Wiping)",
        concept="Mastering sanitization and media disposal standards: Clearing, Purging, Destroying (NIST SP 800-88), Cryptographic Erase (Crypto-shredding), Degaussing, and physical shredding.",
        analogy="Think of erasing an ink secret from a notebook: Simply clicking 'Delete' in Windows is like tearing out the Table of Contents page—the secret chapters are still completely readable on the pages behind it. Secure Wiping (Purging) is using heavy black ink to overwrite every single line 7 times. Degaussing is running a massive industrial magnet over magnetic tape. Physical Destruction is throwing the entire notebook into an industrial steel woodchipper that grinds it into dust.",
        theory_sections=[
            {
                "heading": "Why Standard File Deletion Leaves Data Intact",
                "content": (
                    "When a user presses 'Delete' and empties the Recycle Bin on a traditional operating system:\n"
                    "- The OS does **NOT** erase the underlying physical sectors on disk!\n"
                    "- It simply marks the file's index pointer as 'free space available for future overwriting'.\n"
                    "- Anyone with free forensic software (Recuva, TestDisk) can recover 100% of the deleted files in seconds."
                )
            },
            {
                "heading": "NIST SP 800-88 Media Sanitization Guidelines",
                "content": (
                    "NIST standardizes three distinct sanitization tiers:\n\n"
                    "1. **Clear**: Overwriting storage space with logical techniques (e.g., writing all zeros or random data over sectors using tools like `shred` or DBAN). Protects against simple keyboard recovery.\n"
                    "2. **Purge**: Executing firmware-level sanitization (**Cryptographic Erase - CE** on SEDs/SSDs) or **Degaussing** (exposing magnetic HDDs/tapes to a powerful electromagnetic pulse that scrambles magnetic domains permanently). Protects against laboratory forensic recovery.\n"
                    "3. **Destroy**: Physical destruction making media completely unusable:\n"
                    "   - **Shredding / Disintegrating**: Grinding drives into 2mm particulate fragments.\n"
                    "   - **Incineration**: Melting drives in a high-temperature industrial furnace.\n"
                    "   - Certificate of Destruction: A legal document issued by certified disposal vendors recording drive serial numbers."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Secure Disk Overwriting Tools (Linux Shred & Windows Cipher)",
                "language": "bash",
                "code": (
                    "# Linux shred utility: Overwriting drive with 3 random passes plus zeroes:\n"
                    "sudo shred -v -n 3 -z /dev/sdb\n\n"
                    "# Windows native cipher utility: Overwriting unused free space with zeroes:\n"
                    "cipher /w:C:\\\n\n"
                    "# ATA Secure Erase command via hdparm on Linux:\n"
                    "sudo hdparm --user-master u --security-erase p /dev/sdb"
                ),
                "explanation": "Overwriting sectors ensures residual file data cannot be carved from unallocated storage blocks."
            },
            {
                "title": "Python: Simulating Cryptographic Erase (Crypto-Shredding)",
                "language": "python",
                "code": (
                    "class CryptoShreddingStorage:\n"
                    "    def __init__(self):\n"
                    "        self.master_encryption_key = 'SUPER_SECRET_AES_KEY_888'\n"
                    "        self.encrypted_payload = 'CIPHERTEXT_CONTAINS_10000_PATIENT_RECORDS'\n"
                    "    \n"
                    "    def cryptographic_erase(self) -> str:\n"
                    "        # Destroy the single decryption key instantly!\n"
                    "        self.master_encryption_key = None\n"
                    "        # The ciphertext remains, but is mathematically unrecoverable forever\n"
                    "        return 'CRYPTO_SHRED_COMPLETE: Master key permanently purged.'\n\n"
                    "drive = CryptoShreddingStorage()\n"
                    "print(drive.cryptographic_erase())\n"
                    "print('Key status:', drive.master_encryption_key)"
                ),
                "explanation": "Crypto-shredding sanitizes terabytes of cloud or SSD storage instantly by securely discarding the encryption key."
            }
        ],
        coding_challenge={
            "description": "Write a Python function `select_sanitization_tier(data_classification: str, drive_is_ssd: bool) -> str` that returns 'PHYSICAL_SHRED' if classification is 'TOP_SECRET', 'CRYPTO_ERASE' if drive_is_ssd is True and classification is 'CONFIDENTIAL', 'DEGAUSS' if not SSD and 'CONFIDENTIAL', and 'OVERWRITE_ZEROES' for 'PUBLIC'.",
            "starter_code": (
                "def select_sanitization_tier(data_classification: str, drive_is_ssd: bool) -> str:\n"
                "    # Return sanitization method string\n"
                "    return ''\n\n"
                "print(select_sanitization_tier('TOP_SECRET', True))\n"
                "print(select_sanitization_tier('CONFIDENTIAL', True))\n"
                "print(select_sanitization_tier('CONFIDENTIAL', False))\n"
                "print(select_sanitization_tier('PUBLIC', False))"
            ),
            "solution_code": (
                "def select_sanitization_tier(data_classification: str, drive_is_ssd: bool) -> str:\n"
                "    c = data_classification.upper()\n"
                "    if c == 'TOP_SECRET':\n"
                "        return 'PHYSICAL_SHRED'\n"
                "    if c == 'CONFIDENTIAL':\n"
                "        return 'CRYPTO_ERASE' if drive_is_ssd else 'DEGAUSS'\n"
                "    return 'OVERWRITE_ZEROES'\n\n"
                "print(select_sanitization_tier('TOP_SECRET', True))\n"
                "print(select_sanitization_tier('CONFIDENTIAL', True))\n"
                "print(select_sanitization_tier('CONFIDENTIAL', False))\n"
                "print(select_sanitization_tier('PUBLIC', False))"
            ),
            "expected_output": "PHYSICAL_SHRED\nCRYPTO_ERASE\nDEGAUSS\nOVERWRITE_ZEROES"
        },
        quizzes=[
            {
                "question": "What happens when you delete a file in Windows and empty the Recycle Bin without using secure wiping tools?",
                "options": [
                    "The operating system only marks the file's directory index pointer as free space; the actual data remains intact on disk sectors until overwritten",
                    "The hard drive physically melts the sectors",
                    "The data is beamed to a government satellite",
                    "The bits are converted into blank spaces immediately"
                ],
                "correct_answer": "The operating system only marks the file's directory index pointer as free space; the actual data remains intact on disk sectors until overwritten",
                "explanation": "Standard deletion does not sanitize data. Forensic carving tools easily extract deleted files from unallocated clusters."
            },
            {
                "question": "What is 'Degaussing' in media sanitization?",
                "options": [
                    "Exposing magnetic storage media (like HDDs and backup tapes) to a powerful electromagnetic pulse that permanently scrambles magnetic domains",
                    "Washing hard drives with soapy water",
                    "Drilling a small hole through the plastic drive cover",
                    "Deleting temporary internet cache files"
                ],
                "correct_answer": "Exposing magnetic storage media (like HDDs and backup tapes) to a powerful electromagnetic pulse that permanently scrambles magnetic domains",
                "explanation": "Degaussing neutralizes magnetic fields on platters, rendering magnetic drives unreadable and permanently destroying their servo tracks."
            },
            {
                "question": "Why is Degaussing completely ineffective on Solid-State Drives (SSDs) and USB flash drives?",
                "options": [
                    "SSDs store data electronically in flash NAND semiconductor memory cells, not magnetic domains",
                    "SSDs are made of pure gold",
                    "SSDs are immune to magnets because they run on batteries",
                    "Degaussers can only fit 3.5-inch drives"
                ],
                "correct_answer": "SSDs store data electronically in flash NAND semiconductor memory cells, not magnetic domains",
                "explanation": "Flash memory is electronic, not magnetic. SSDs require cryptographic erasure, specialized ATA Secure Erase commands, or physical shredding."
            },
            {
                "question": "What is 'Cryptographic Erase' (Crypto-shredding)?",
                "options": [
                    "Permanently deleting or purging the encryption key used to encrypt a storage volume, rendering the remaining ciphertext mathematically unrecoverable",
                    "A ransomware attack that deletes files",
                    "Mining cryptocurrency on decommissioned servers",
                    "Encrypting a file twice with different passwords"
                ],
                "correct_answer": "Permanently deleting or purging the encryption key used to encrypt a storage volume, rendering the remaining ciphertext mathematically unrecoverable",
                "explanation": "Crypto-shredding purges the encryption key in milliseconds. Without the key, the ciphertext cannot be deciphered by any known supercomputer."
            },
            {
                "question": "What legal document must be provided by third-party electronic recycling companies to certify that decommissioned storage media was destroyed according to NIST standards?",
                "options": ["A Certificate of Destruction", "A receipt of shipping", "A clean bill of health", "A tax exemption voucher"],
                "correct_answer": "A Certificate of Destruction",
                "explanation": "Certificates of Destruction provide legal and regulatory proof (with serial numbers and destruction methods) for compliance audits."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 51: Security Operations Center (SOC) Basics
    # ---------------------------------------------------------
    DayBlueprint(
        order=51,
        title="Day 51: Security Operations Center (SOC) Basics",
        concept="Mastering the organizational heartbeat of cyber defense: SOC roles (Tier 1 Triage Analyst, Tier 2 Incident Responder, Tier 3 Threat Hunter/SME), 24/7/365 monitoring, alert queues, and alert fatigue.",
        analogy="Think of a hospital Emergency Room (ER): Tier 1 SOC analysts are the triage nurses at the front desk checking vital signs and sorting headaches from heart attacks. Tier 2 analysts are the emergency room doctors stitching wounds, administering medicine, and stabilizing patients. Tier 3 analysts are the specialized surgeons and disease researchers performing deep post-mortems and investigating rare virus strains.",
        theory_sections=[
            {
                "heading": "The Structure of a Modern SOC",
                "content": (
                    "A **Security Operations Center (SOC)** is the centralized command facility responsible for monitoring, detecting, analyzing, and responding to cybersecurity incidents:\n\n"
                    "1. **Tier 1 (Triage Analyst)**: Monitors SIEM alert queues 24/7. Reviews incoming alerts, filters false positives, gathers initial contextual data, and escalates genuine threats within 15 minutes.\n"
                    "2. **Tier 2 (Incident Responder)**: Deep-dive investigation. Gathers endpoint telemetry, isolates infected hosts, performs root-cause remediation, and recovers systems.\n"
                    "3. **Tier 3 (Senior Threat Hunter / Forensic SME)**: Proactively searches internal networks for stealthy adversaries that bypassed automated detection. Conducts reverse engineering of malware and digital forensics.\n"
                    "4. **SOC Manager**: Manages shift coverage, budgets, compliance reporting, and executive communication."
                )
            },
            {
                "heading": "The Challenge of Alert Fatigue",
                "content": (
                    "Enterprise SIEMs ingest millions of log events daily, generating thousands of automated alerts. **Alert Fatigue** occurs when analysts are overwhelmed by high volumes of low-fidelity false positives, causing them to accidentally miss the one critical breach alert hidden in the noise. Modern SOCs combat this with SOAR (Security Orchestration, Automation, and Response)."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Simulating a SOC Alert Triage Ticket Queue",
                "language": "python",
                "code": (
                    "class SOCTriageQueue:\n"
                    "    def __init__(self):\n"
                    "        self.queue = []\n"
                    "    \n"
                    "    def ingest_alert(self, title: str, severity: str, host: str):\n"
                    "        # Priority mapping: P1 (Critical), P2 (High), P3 (Medium)\n"
                    "        priority = {'CRITICAL': 1, 'HIGH': 2, 'MEDIUM': 3}.get(severity.upper(), 4)\n"
                    "        self.queue.append({'priority': priority, 'title': title, 'host': host, 'severity': severity})\n"
                    "        # Sort queue by priority\n"
                    "        self.queue.sort(key=lambda x: x['priority'])\n"
                    "    \n"
                    "    def get_next_ticket(self) -> dict:\n"
                    "        return self.queue.pop(0) if self.queue else None\n\n"
                    "soc = SOCTriageQueue()\n"
                    "soc.ingest_alert('Unusual Port Scan', 'MEDIUM', 'web-01')\n"
                    "soc.ingest_alert('Ransomware Canary Triggered', 'CRITICAL', 'fs-finance')\n"
                    "print('First ticket for Tier 1 Analyst to triage:', soc.get_next_ticket())"
                ),
                "explanation": "Illustrates priority queue dispatching where critical incidents jump ahead of low-severity events."
            },
            {
                "title": "Querying Security Ticket Status via Command Line",
                "language": "bash",
                "code": (
                    "# Querying SOC ticket SLA metrics via ticketing API (e.g. Jira / ServiceNow):\n"
                    "curl -s -H \"Authorization: Bearer SOC_API_KEY\" \\\n"
                    "  \"https://soc.company.com/api/v1/incidents?status=open&severity=critical\" | jq '.total_open_p1'"
                ),
                "explanation": "SOC leads track mean time to detect (MTTD) and mean time to respond (MTTR) across analyst shifts."
            }
        ],
        coding_challenge={
            "description": "Write a Python function `escalate_soc_ticket(severity: str, confidence_score: float) -> str` that returns 'ESCALATE_TIER_2' if severity is 'CRITICAL' or (severity == 'HIGH' and confidence_score >= 0.8), 'CLOSE_FALSE_POSITIVE' if confidence_score < 0.3, and 'TIER_1_MONITOR' otherwise.",
            "starter_code": (
                "def escalate_soc_ticket(severity: str, confidence_score: float) -> str:\n"
                "    # Return triage escalation decision string\n"
                "    return ''\n\n"
                "print(escalate_soc_ticket('CRITICAL', 0.9))\n"
                "print(escalate_soc_ticket('HIGH', 0.85))\n"
                "print(escalate_soc_ticket('LOW', 0.1))"
            ),
            "solution_code": (
                "def escalate_soc_ticket(severity: str, confidence_score: float) -> str:\n"
                "    s = severity.upper()\n"
                "    if s == 'CRITICAL' or (s == 'HIGH' and confidence_score >= 0.8):\n"
                "        return 'ESCALATE_TIER_2'\n"
                "    if confidence_score < 0.3:\n"
                "        return 'CLOSE_FALSE_POSITIVE'\n"
                "    return 'TIER_1_MONITOR'\n\n"
                "print(escalate_soc_ticket('CRITICAL', 0.9))\n"
                "print(escalate_soc_ticket('HIGH', 0.85))\n"
                "print(escalate_soc_ticket('LOW', 0.1))"
            ),
            "expected_output": "ESCALATE_TIER_2\nESCALATE_TIER_2\nCLOSE_FALSE_POSITIVE"
        },
        quizzes=[
            {
                "question": "What is the primary role of a Tier 1 Triage Analyst in a Security Operations Center (SOC)?",
                "options": [
                    "To monitor incoming SIEM security alert queues 24/7, perform initial triage, filter false positives, and escalate confirmed threats to Tier 2",
                    "To write marketing press releases",
                    "To manufacture computer memory chips",
                    "To physically repair broken office chairs"
                ],
                "correct_answer": "To monitor incoming SIEM security alert queues 24/7, perform initial triage, filter false positives, and escalate confirmed threats to Tier 2",
                "explanation": "Tier 1 analysts act as the first line of defense, validating incoming alarms and quickly escalating high-priority incidents."
            },
            {
                "question": "What is 'Alert Fatigue' and why is it dangerous in security operations?",
                "options": [
                    "When security analysts become desensitized and exhausted by overwhelming volumes of false positive alarms, causing them to overlook genuine breach notifications",
                    "When the computer alarm buzzer runs out of sound",
                    "When a server shuts down from lack of sleep",
                    "When an employee forgets to set their morning alarm clock"
                ],
                "correct_answer": "When security analysts become desensitized and exhausted by overwhelming volumes of false positive alarms, causing them to overlook genuine breach notifications",
                "explanation": "High volumes of low-value alerts overwhelm human analysts, leading to missed detections and delayed response times."
            },
            {
                "question": "What is 'Threat Hunting' performed by Tier 3 SOC analysts?",
                "options": [
                    "Proactively and iteratively searching through networks and datasets to detect stealthy advanced adversaries that have evaded automated security tools",
                    "Hunting wild animals in the forest",
                    "Buying new antivirus licenses online",
                    "Resetting lost email passwords for employees"
                ],
                "correct_answer": "Proactively and iteratively searching through networks and datasets to detect stealthy advanced adversaries that have evaded automated security tools",
                "explanation": "Threat hunting assumes the network is already breached, actively investigating anomalies and telemetry to root out persistent threats."
            },
            {
                "question": "What does MTTD (Mean Time to Detect) measure in SOC performance benchmarking?",
                "options": [
                    "The average time that elapses from when a security incident or intrusion begins until the security team successfully discovers it",
                    "The time it takes to download a software update",
                    "The average lifespan of a computer monitor",
                    "The speed of an employee's typing cadence"
                ],
                "correct_answer": "The average time that elapses from when a security incident or intrusion begins until the security team successfully discovers it",
                "explanation": "MTTD measures detection agility: reducing MTTD from months to minutes prevents adversaries from executing lateral movement."
            },
            {
                "question": "What technology platform helps modern SOCs combat alert fatigue by automating repetitive triage workflows and incident response playbooks?",
                "options": ["SOAR (Security Orchestration, Automation, and Response)", "VLAN", "POP3", "FAT32"],
                "correct_answer": "SOAR (Security Orchestration, Automation, and Response)",
                "explanation": "SOAR automates routine tasks (e.g., querying VirusTotal, blocking firewall IPs, isolating hosts), freeing analysts to focus on complex triage."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 52: SIEM Tools (Security Information and Event Management)
    # ---------------------------------------------------------
    DayBlueprint(
        order=52,
        title="Day 52: SIEM Tools (Security Information and Event Management)",
        concept="Mastering enterprise log aggregation: SIEM architecture (Splunk, Microsoft Sentinel, Elastic), log normalization, correlation rules, and user/entity behavioral analytics (UEBA).",
        analogy="Think of detective evidence gathering: A single clue in isolation means nothing—a door opened at 2:00 AM, a computer logged in at 2:01 AM, an outbound file transfer at 2:05 AM. The building door system doesn't know about the computer, and the computer doesn't know about the firewall. A SIEM is the master detective who collects all three diaries, stitches them onto a single timeline, and screams 'The janitor badge opened the vault, logged into payroll, and exfiltrated 5 GB of data!'",
        theory_sections=[
            {
                "heading": "The Core Functions of a SIEM",
                "content": (
                    "A **SIEM (Security Information and Event Management)** platform provides centralized visibility across the entire enterprise:\n\n"
                    "1. **Log Ingestion & Aggregation**: Ingests gigabytes/terabytes of logs daily from Windows Event Logs, Linux syslog, firewalls, cloud audit trails (AWS CloudTrail), and proxies.\n"
                    "2. **Normalization & Parsing**: Converts disparate vendor log formats into a common schema (e.g., mapping `src_ip`, `client_ip`, and `sourceAddress` to a standardized `source.ip` field).\n"
                    "3. **Correlation Rules**: Detects attack patterns across separate systems (e.g., 'Firewall detects 50 port scan hits' + 'Domain Controller registers 10 failed logins' + 'Local EDR sees mimikatz.exe execution' = High Priority Incident).\n"
                    "4. **Compliance & Retention**: Securely archives immutable audit logs for 1 to 7 years to meet PCI-DSS, HIPAA, and SOC 2 regulatory mandates."
                )
            },
            {
                "heading": "UEBA (User and Entity Behavior Analytics)",
                "content": (
                    "Next-Gen SIEMs incorporate machine learning algorithms to establish individual baseline behavioral models for every user and computer (e.g., alerting when a marketing manager who typically logs in 9-5 from Chicago suddenly downloads the entire customer database at 3:00 AM from an IP in Russia)."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Writing a Splunk SPL Search Query for Brute-Force Attacks",
                "language": "bash",
                "code": (
                    "# Splunk Search Processing Language (SPL) to detect brute-force:\n"
                    "index=windows EventCode=4625\n"
                    "| stats count by Account_Name, Source_Network_Address\n"
                    "| where count > 10\n"
                    "| sort - count"
                ),
                "explanation": "Queries Windows failed logon events, aggregating by username and source IP to flag brute-force intrusion attempts."
            },
            {
                "title": "Python: Simulating a SIEM Event Correlation Engine",
                "language": "python",
                "code": (
                    "def correlate_security_events(events: list) -> list:\n"
                    "    # Detecting Account Takeover: Failed logins followed by rapid data download\n"
                    "    user_failures = {}\n"
                    "    alerts = []\n"
                    "    for e in events:\n"
                    "        user = e.get('user')\n"
                    "        if e.get('event') == 'FAILED_LOGIN':\n"
                    "            user_failures[user] = user_failures.get(user, 0) + 1\n"
                    "        elif e.get('event') == 'BULK_DOWNLOAD' and user_failures.get(user, 0) >= 3:\n"
                    "            alerts.append(f'CRITICAL SIEM CORRELATION: Account Takeover on {user} ({user_failures[user]} failed logins followed by download)!')\n"
                    "    return alerts\n\n"
                    "log_stream = [\n"
                    "    {'user': 'alice', 'event': 'FAILED_LOGIN'},\n"
                    "    {'user': 'alice', 'event': 'FAILED_LOGIN'},\n"
                    "    {'user': 'alice', 'event': 'FAILED_LOGIN'},\n"
                    "    {'user': 'alice', 'event': 'BULK_DOWNLOAD'}\n"
                    "]\n"
                    "print(correlate_security_events(log_stream))"
                ),
                "explanation": "Illustrates how SIEM correlation rules connect disparate event logs to reveal multi-stage attacks."
            }
        ],
        coding_challenge={
            "description": "Write a Python function `detect_brute_force_siem(events: list, threshold: int = 5) -> list` that inspects a list of log dicts `[{'ip': str, 'status': 'FAIL'/'SUCCESS'}]` and returns a list of unique IP addresses that exceeded the failure threshold.",
            "starter_code": (
                "def detect_brute_force_siem(events: list, threshold: int = 5) -> list:\n"
                "    # Return list of attacking IPs\n"
                "    return []\n\n"
                "logs = [\n"
                "    {'ip': '1.2.3.4', 'status': 'FAIL'},\n"
                "    {'ip': '1.2.3.4', 'status': 'FAIL'},\n"
                "    {'ip': '1.2.3.4', 'status': 'FAIL'},\n"
                "    {'ip': '1.2.3.4', 'status': 'FAIL'},\n"
                "    {'ip': '1.2.3.4', 'status': 'FAIL'},\n"
                "    {'ip': '1.2.3.4', 'status': 'FAIL'},\n"
                "    {'ip': '5.6.7.8', 'status': 'SUCCESS'}\n"
                "]\n"
                "print(detect_brute_force_siem(logs, threshold=5))"
            ),
            "solution_code": (
                "def detect_brute_force_siem(events: list, threshold: int = 5) -> list:\n"
                "    fail_counts = {}\n"
                "    for event in events:\n"
                "        if event.get('status') == 'FAIL':\n"
                "            ip = event.get('ip')\n"
                "            fail_counts[ip] = fail_counts.get(ip, 0) + 1\n"
                "    flagged = [ip for ip, count in fail_counts.items() if count > threshold]\n"
                "    return sorted(flagged)\n\n"
                "logs = [\n"
                "    {'ip': '1.2.3.4', 'status': 'FAIL'},\n"
                "    {'ip': '1.2.3.4', 'status': 'FAIL'},\n"
                "    {'ip': '1.2.3.4', 'status': 'FAIL'},\n"
                "    {'ip': '1.2.3.4', 'status': 'FAIL'},\n"
                "    {'ip': '1.2.3.4', 'status': 'FAIL'},\n"
                "    {'ip': '1.2.3.4', 'status': 'FAIL'},\n"
                "    {'ip': '5.6.7.8', 'status': 'SUCCESS'}\n"
                "]\n"
                "print(detect_brute_force_siem(logs, threshold=5))"
            ),
            "expected_output": "['1.2.3.4']"
        },
        quizzes=[
            {
                "question": "What is the primary operational function of a SIEM (Security Information and Event Management) platform?",
                "options": [
                    "To aggregate, parse, normalize, and correlate security event logs from across the entire enterprise to detect cyber threats in real time",
                    "To replace human software developers",
                    "To host the company's public marketing website",
                    "To speed up computer 3D graphics rendering"
                ],
                "correct_answer": "To aggregate, parse, normalize, and correlate security event logs from across the entire enterprise to detect cyber threats in real time",
                "explanation": "A SIEM serves as the central brain of a SOC, ingesting and correlating logs from firewalls, servers, endpoints, and cloud systems."
            },
            {
                "question": "What is 'Log Normalization' in a SIEM environment?",
                "options": [
                    "Translating diverse log formats from different vendors into a standardized, unified schema with consistent field names (like `source.ip`)",
                    "Deleting all log files every morning",
                    "Converting logs into audio recordings",
                    "Translating logs into Spanish"
                ],
                "correct_answer": "Translating diverse log formats from different vendors into a standardized, unified schema with consistent field names (like `source.ip`)",
                "explanation": "Normalization ensures analysts can search and correlate across Cisco, Windows, and Linux logs using standardized field queries."
            },
            {
                "question": "What is a 'Correlation Rule' in a SIEM?",
                "options": [
                    "A programmed logic statement that connects multiple related events across different log sources to trigger a composite security alert",
                    "A rule stating that all employees must take lunch at noon",
                    "A mathematical rule for calculating computer memory",
                    "A guideline for purchasing office chairs"
                ],
                "correct_answer": "A programmed logic statement that connects multiple related events across different log sources to trigger a composite security alert",
                "explanation": "Correlation rules tie together disparate clues (e.g., 5 failed logins on a domain controller followed by an outbound spike on a firewall)."
            },
            {
                "question": "Which of the following is a leading commercial enterprise SIEM platform widely deployed in global SOCs?",
                "options": ["Splunk", "Microsoft Word", "Adobe Photoshop", "VLC Media Player"],
                "correct_answer": "Splunk",
                "explanation": "Splunk (along with Microsoft Sentinel, QRadar, and Elastic) is one of the world's most widely utilized SIEM platforms."
            },
            {
                "question": "What is the role of UEBA (User and Entity Behavior Analytics) within a modern Next-Gen SIEM?",
                "options": [
                    "Using machine learning algorithms to establish normal behavioral baselines for users and assets, detecting anomalous activity indicative of insider threats or hijacked accounts",
                    "Recording audio of employee office conversations",
                    "Measuring how fast employees type on their keyboards",
                    "Deleting old emails automatically"
                ],
                "correct_answer": "Using machine learning algorithms to establish normal behavioral baselines for users and assets, detecting anomalous activity indicative of insider threats or hijacked accounts",
                "explanation": "UEBA spots subtle compromises (like a user downloading gigabytes of sensitive files at 2 AM from an unusual IP) by identifying deviations from normal baselines."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 53: Incident Response Lifecycle (Prep, Ident, Contain, Erad, Rec, Lessons)
    # ---------------------------------------------------------
    DayBlueprint(
        order=53,
        title="Day 53: Incident Response Lifecycle (Prep, Ident, Contain, Erad, Rec, Lessons)",
        concept="Mastering the NIST SP 800-61 Incident Response framework: Preparation, Detection & Analysis, Containment (short-term & long-term), Eradication, Recovery, and Post-Incident Activity (Lessons Learned).",
        analogy="Think of responding to a structural building fire: 1. Preparation: Installing smoke detectors, training firefighters, maintaining fire hydrants. 2. Identification: The fire alarm sounds and firefighters identify the kitchen blaze. 3. Containment: Shutting fire doors to stop flames from spreading to the bedrooms. 4. Eradication: Hosing down the flames and clearing flammable debris. 5. Recovery: Restoring power, ventilating smoke, and clearing residents to re-enter. 6. Lessons Learned: Meeting to ask 'Why did the toaster catch fire, and how do we prevent it next time?'",
        theory_sections=[
            {
                "heading": "The 6 Phases of NIST SP 800-61 Incident Handling",
                "content": (
                    "When a cyber breach occurs, chaos ensues without a practiced Incident Response (IR) plan:\n\n"
                    "1. **Preparation**: Establishing IR policies, training the Computer Security Incident Response Team (CSIRT), deploying monitoring tools, and conducting tabletop simulation exercises.\n"
                    "2. **Detection & Analysis (Identification)**: Identifying genuine security incidents from triage alerts, scoping the intrusion blast radius, and determining compromised systems.\n"
                    "3. **Containment**: Preventing the attack from spreading further:\n"
                    "   - *Short-Term*: Isolating endpoints from the network, disabling compromised user credentials, blocking attacker C2 IPs on perimeter firewalls.\n"
                    "   - *Long-Term*: Applying temporary firewall micro-segmentation while business operations continue.\n"
                    "4. **Eradication**: Completely purging malware, deleting attacker backdoors, resetting passwords across the enterprise, and patching the exploited vulnerability.\n"
                    "5. **Recovery**: Restoring clean systems from verified offline backups, re-enabling services, and closely monitoring for recurrence.\n"
                    "6. **Post-Incident Activity (Lessons Learned)**: Conducting a mandatory retrospective within 14 days. Answering: *What happened? How quickly did we respond? How do we improve documentation and automated defenses?*"
                )
            },
            {
                "heading": "Preserving Evidence Before Containment",
                "content": (
                    "Never immediately reboot or format an infected computer! Volatile evidence stored in physical RAM (unencrypted encryption keys, active network sockets, injected DLLs) will be permanently lost."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Incident Responder Host Isolation & Evidence Capture Steps",
                "language": "bash",
                "code": (
                    "# Step 1: Capture volatile memory BEFORE powering off or rebooting:\n"
                    "# (Using winpmem or LiME memory dumper tool)\n"
                    "winpmem.exe -o memdump.raw\n\n"
                    "# Step 2: Immediate network containment (quarantine):\n"
                    "netsh interface set interface name=\"Ethernet\" admin=DISABLED\n\n"
                    "# Step 3: Disable compromised active directory user account:\n"
                    "Disable-ADAccount -Identity \"compromised_employee\""
                ),
                "explanation": "Standard forensic triage preserves evidence in memory before severing connectivity to contain an outbreak."
            },
            {
                "title": "Python: Tracking Incident Response Lifecycle State Transitions",
                "language": "python",
                "code": (
                    "class IncidentResponseWorkflow:\n"
                    "    STAGES = ['PREPARATION', 'IDENTIFICATION', 'CONTAINMENT', 'ERADICATION', 'RECOVERY', 'LESSONS_LEARNED']\n"
                    "    \n"
                    "    def __init__(self, incident_id: str):\n"
                    "        self.incident_id = incident_id\n"
                    "        self.current_stage_idx = 1 # Starts at Identification\n"
                    "    \n"
                    "    def advance_stage(self) -> str:\n"
                    "        if self.current_stage_idx < len(self.STAGES) - 1:\n"
                    "            self.current_stage_idx += 1\n"
                    "            return f'Incident {self.incident_id} advanced to: {self.STAGES[self.current_stage_idx]}'\n"
                    "        return 'Incident is CLOSED (Lessons Learned completed).'\n\n"
                    "ir = IncidentResponseWorkflow('INC-2024-001')\n"
                    "print(ir.advance_stage()) # Containment\n"
                    "print(ir.advance_stage()) # Eradication"
                ),
                "explanation": "Formalizing the sequential stages of the NIST incident response framework."
            }
        ],
        coding_challenge={
            "description": "Write a Python function `get_ir_phase_order(phase_name: str) -> int` that maps the 6 NIST phases: 'PREPARATION' -> 1, 'IDENTIFICATION' -> 2, 'CONTAINMENT' -> 3, 'ERADICATION' -> 4, 'RECOVERY' -> 5, 'LESSONS_LEARNED' -> 6. Return 0 for unknown phases.",
            "starter_code": (
                "def get_ir_phase_order(phase_name: str) -> int:\n"
                "    # Return integer order 1 to 6\n"
                "    return 0\n\n"
                "print(get_ir_phase_order('CONTAINMENT'))\n"
                "print(get_ir_phase_order('LESSONS_LEARNED'))"
            ),
            "solution_code": (
                "def get_ir_phase_order(phase_name: str) -> int:\n"
                "    phases = {\n"
                "        'PREPARATION': 1,\n"
                "        'IDENTIFICATION': 2,\n"
                "        'CONTAINMENT': 3,\n"
                "        'ERADICATION': 4,\n"
                "        'RECOVERY': 5,\n"
                "        'LESSONS_LEARNED': 6\n"
                "    }\n"
                "    return phases.get(phase_name.upper(), 0)\n\n"
                "print(get_ir_phase_order('CONTAINMENT'))\n"
                "print(get_ir_phase_order('LESSONS_LEARNED'))"
            ),
            "expected_output": "3\n6"
        },
        quizzes=[
            {
                "question": "Which phase of the NIST Incident Response lifecycle focuses on isolating infected endpoints to prevent malware from spreading laterally across the network?",
                "options": ["Containment", "Preparation", "Lessons Learned", "Eradication"],
                "correct_answer": "Containment",
                "explanation": "Containment stops bleeding: isolating hosts, blocking C2 communications, and disabling compromised accounts to halt lateral movement."
            },
            {
                "question": "Why should an incident responder NEVER immediately reboot or power off a computer suspected of being infected by advanced malware?",
                "options": [
                    "Powering off the machine destroys volatile data stored in RAM (like running processes, memory-injected malware, and unencrypted keys) required for forensic investigation",
                    "The computer will catch fire",
                    "Rebooting permanently deletes the operating system",
                    "The monitor will display an error message"
                ],
                "correct_answer": "Powering off the machine destroys volatile data stored in RAM (like running processes, memory-injected malware, and unencrypted keys) required for forensic investigation",
                "explanation": "Volatile memory (RAM) holds crucial evidence (keys, active sockets, injected code) that vaporizes the moment power is cut."
            },
            {
                "question": "What is the purpose of the 'Lessons Learned' (Post-Incident Activity) phase in the incident response lifecycle?",
                "options": [
                    "To conduct a blameless retrospective analyzing what happened, how the response performed, and what security controls must be improved to prevent recurrence",
                    "To assign personal blame to individual employees and fire them",
                    "To calculate how much money was spent on coffee during the incident",
                    "To delete all incident logs from the company servers"
                ],
                "correct_answer": "To conduct a blameless retrospective analyzing what happened, how the response performed, and what security controls must be improved to prevent recurrence",
                "explanation": "Lessons Learned ensures continuous improvement: strengthening detection rules and closing policy loopholes exposed during the incident."
            },
            {
                "question": "What actions occur during the 'Eradication' phase of incident handling?",
                "options": [
                    "Removing all malware, eliminating adversary backdoors, closing compromised accounts, and patching the vulnerabilities exploited to gain entry",
                    "Buying new laptops for all employees",
                    "Changing the company name",
                    "Taking out insurance policies"
                ],
                "correct_answer": "Removing all malware, eliminating adversary backdoors, closing compromised accounts, and patching the vulnerabilities exploited to gain entry",
                "explanation": "Eradication completely purges all adversary traces and root vulnerabilities from the environment before systems are restored."
            },
            {
                "question": "What is a 'Tabletop Exercise' conducted during the Preparation phase?",
                "options": [
                    "A simulated, discussion-based walkthrough where the incident response team practices responding to a hypothetical cyberattack scenario without impacting live production systems",
                    "Exercising on a physical table in the office gym",
                    "Assembling office furniture",
                    "A meeting to purchase server hardware"
                ],
                "correct_answer": "A simulated, discussion-based walkthrough where the incident response team practices responding to a hypothetical cyberattack scenario without impacting live production systems",
                "explanation": "Tabletop exercises rehearse roles, communication channels, and technical procedures to ensure readiness when real incidents strike."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 54: Digital Forensics Basics (Chain of Custody, Data Preservation)
    # ---------------------------------------------------------
    DayBlueprint(
        order=54,
        title="Day 54: Digital Forensics Basics (Chain of Custody, Data Preservation)",
        concept="Mastering legal digital forensics: Chain of Custody, Order of Volatility, bit-stream disk imaging (dd/E01), hardware write blockers, and forensic hash integrity verification.",
        analogy="Think of homicide crime scene investigation: If a police detective picks up a murder weapon with bare hands, drops it in their pocket, and takes it home over the weekend, the judge throws the evidence out of court. Digital Forensics is wearing sterile gloves (Write Blockers), creating an exact microscopic photographic twin of the hard drive (Bit-Stream Image), computing its digital DNA (SHA-256 Hash), and documenting every single human who touched it in an unbroken legal log (Chain of Custody).",
        theory_sections=[
            {
                "heading": "The Order of Volatility (RFC 3227)",
                "content": (
                    "When collecting digital evidence, forensic investigators must preserve data in order from **most volatile** (disappears first) to **least volatile** (persists longest):\n\n"
                    "1. CPU Registers and CPU Cache (nanoseconds)\n"
                    "2. Routing Tables, ARP Cache, Process Tables, Kernel Memory\n"
                    "3. Physical System Memory (**RAM**)\n"
                    "4. Temporary File Systems / Swap space\n"
                    "5. Disk Drives (HDDs, SSDs, Flash Storage)\n"
                    "6. Remote Logging Data and Network Backups\n"
                    "7. Physical Configuration and Network Topology\n"
                    "8. Archival Tapes and Optical Media"
                )
            },
            {
                "heading": "Chain of Custody & Forensic Imaging Rules",
                "content": (
                    "- **Hardware Write Blocker**: Physical device placed between the evidence hard drive and the forensic workstation. Permits read commands while electrically blocking all write commands, guaranteeing the original evidence is never altered.\n"
                    "- **Bit-Stream Forensic Image**: An exact bit-for-bit, sector-for-sector physical clone of the drive (including unallocated slack space and deleted files) saved as raw (`.dd`) or Expert Witness (`.E01`) format.\n"
                    "- **Chain of Custody**: A chronological legal document tracking: *Who collected the evidence? When? Where was it stored? Who accessed it? Why?* Breaking the chain makes evidence inadmissible in court."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Creating a Bit-Stream Image and Verifying Hashes via Linux dd",
                "language": "bash",
                "code": (
                    "# Creating bit-for-bit forensic clone of evidence drive /dev/sdb:\n"
                    "sudo dd if=/dev/sdb of=/evidence/case_001_sdb.dd bs=4096 status=progress conv=noerror,sync\n\n"
                    "# Computing matching hashes before and after imaging:\n"
                    "sha256sum /dev/sdb\n"
                    "sha256sum /evidence/case_001_sdb.dd\n"
                    "# If both SHA-256 hashes are 100% identical, the image is legally certified!"
                ),
                "explanation": "Forensic examiners always perform investigations on certified bit-stream copies, never on the original physical evidence."
            },
            {
                "title": "Python: Maintaining a Digital Chain of Custody Record",
                "language": "python",
                "code": (
                    "import time\n\n"
                    "class ChainOfCustody:\n"
                    "    def __init__(self, evidence_id: str, sha256_hash: str):\n"
                    "        self.evidence_id = evidence_id\n"
                    "        self.sha256_hash = sha256_hash\n"
                    "        self.custody_log = []\n"
                    "        self.log_transfer('Detective Smith', 'Seized from suspect residence', 'Evidence Locker A')\n"
                    "    \n"
                    "    def log_transfer(self, handler: str, purpose: str, destination: str):\n"
                    "        entry = {\n"
                    "            'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),\n"
                    "            'handler': handler,\n"
                    "            'purpose': purpose,\n"
                    "            'destination': destination,\n"
                    "            'hash_verified': self.sha256_hash\n"
                    "        }\n"
                    "        self.custody_log.append(entry)\n\n"
                    "coc = ChainOfCustody('ITEM-001', 'a1b2c3d4e5f6...')\n"
                    "coc.log_transfer('Analyst Jones', 'Forensic memory extraction', 'Secure Forensics Lab')\n"
                    "print(coc.custody_log)"
                ),
                "explanation": "Illustrates continuous legal documentation verifying evidence integrity across custodians."
            }
        ],
        coding_challenge={
            "description": "Write a Python function `order_of_volatility_rank(data_type: str) -> int` that returns the RFC 3227 volatility rank (1 = most volatile, 5 = least volatile): 'CPU_REGISTERS' -> 1, 'RAM' -> 2, 'TEMPORARY_SWAP' -> 3, 'HARD_DRIVE' -> 4, 'BACKUP_TAPE' -> 5. Return 0 for unknown.",
            "starter_code": (
                "def order_of_volatility_rank(data_type: str) -> int:\n"
                "    # Return integer rank 1 to 5\n"
                "    return 0\n\n"
                "print(order_of_volatility_rank('CPU_REGISTERS'))\n"
                "print(order_of_volatility_rank('RAM'))\n"
                "print(order_of_volatility_rank('HARD_DRIVE'))"
            ),
            "solution_code": (
                "def order_of_volatility_rank(data_type: str) -> int:\n"
                "    mapping = {\n"
                "        'CPU_REGISTERS': 1,\n"
                "        'RAM': 2,\n"
                "        'TEMPORARY_SWAP': 3,\n"
                "        'HARD_DRIVE': 4,\n"
                "        'BACKUP_TAPE': 5\n"
                "    }\n"
                "    return mapping.get(data_type.upper(), 0)\n\n"
                "print(order_of_volatility_rank('CPU_REGISTERS'))\n"
                "print(order_of_volatility_rank('RAM'))\n"
                "print(order_of_volatility_rank('HARD_DRIVE'))"
            ),
            "expected_output": "1\n2\n4"
        },
        quizzes=[
            {
                "question": "According to the Order of Volatility (RFC 3227), which source of digital evidence must be captured FIRST because it is lost the fastest?",
                "options": ["CPU Registers and Cache Memory", "Hard Disk Drive sectors", "Backup magnetic tapes", "Printed paper documents"],
                "correct_answer": "CPU Registers and Cache Memory",
                "explanation": "Registers and cache change within nanoseconds; memory (RAM) is next. Disk drives and tapes persist indefinitely without power."
            },
            {
                "question": "What is the primary function of a Hardware Write Blocker in digital forensics?",
                "options": [
                    "To physically and electrically intercept disk commands, permitting read access while blocking any data from being written to the original evidence drive",
                    "To format the drive with zeroes",
                    "To make the hard drive spin twice as fast",
                    "To encrypt the suspect's computer monitor"
                ],
                "correct_answer": "To physically and electrically intercept disk commands, permitting read access while blocking any data from being written to the original evidence drive",
                "explanation": "Write blockers guarantee that plugging an evidence drive into a forensic workstation does not alter metadata or timestamps."
            },
            {
                "question": "What is a 'Chain of Custody' document in digital forensics and court proceedings?",
                "options": [
                    "A legal document chronologically recording who collected, handled, transferred, analyzed, and stored digital evidence",
                    "A receipt for purchasing handcuffs",
                    "A list of websites visited by employees",
                    "A diagram of network router cables"
                ],
                "correct_answer": "A legal document chronologically recording who collected, handled, transferred, analyzed, and stored digital evidence",
                "explanation": "Chain of custody proves evidence was not altered, tampered with, or swapped from the moment of seizure to trial."
            },
            {
                "question": "Why do digital forensic examiners create and work on 'Bit-Stream Disk Images' rather than analyzing the suspect's original physical hard drive?",
                "options": [
                    "To preserve the pristine original physical evidence intact while allowing destructive or deep analysis on an exact bit-for-bit cloned copy",
                    "Because original hard drives cannot connect to computers",
                    "Because copies run faster than real drives",
                    "Because original drives are destroyed after 24 hours"
                ],
                "correct_answer": "To preserve the pristine original physical evidence intact while allowing destructive or deep analysis on an exact bit-for-bit cloned copy",
                "explanation": "Working on bit-stream copies protects the original media from accidental corruption and preserves legal admissibility."
            },
            {
                "question": "How does a forensic examiner prove in court that a forensic image file is an exact, unaltered duplicate of the suspect's original hard drive?",
                "options": [
                    "By calculating cryptographic hashes (like SHA-256) of both the original drive and the forensic image, demonstrating the hashes match identically",
                    "By printing both files onto paper and weighing them",
                    "By swearing under oath that they tried their best",
                    "By taking a photograph of the computer screen"
                ],
                "correct_answer": "By calculating cryptographic hashes (like SHA-256) of both the original drive and the forensic image, demonstrating the hashes match identically",
                "explanation": "Matching cryptographic hashes mathematically proves that not a single bit was modified during imaging or transport."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 55: Risk Management Basics (Assessment, Mitigation, Acceptance, Transfer)
    # ---------------------------------------------------------
    DayBlueprint(
        order=55,
        title="Day 55: Risk Management Basics (Assessment, Mitigation, Acceptance, Transfer)",
        concept="Mastering enterprise risk governance: Risk Assessment (Qualitative vs Quantitative), SLE, ARO, ALE formulas, and the four Risk Treatment strategies (Mitigation, Transfer, Acceptance, Avoidance).",
        analogy="Think of living in an area prone to severe earthquakes: Risk Mitigation is bolting your bookcases to the wall studs and reinforcing your foundations. Risk Transfer is buying homeowner earthquake insurance so the insurance company pays for the damage. Risk Acceptance is saying 'A minor crack in the drywall will cost $200, which I can afford out of pocket.' Risk Avoidance is moving to a state with zero earthquakes.",
        theory_sections=[
            {
                "heading": "Quantitative Risk Calculation Formulas",
                "content": (
                    "Security leadership uses quantitative mathematics to justify cybersecurity tool budgets:\n\n"
                    "1. **Asset Value (AV)**: Total monetary value of the asset (e.g., E-commerce database = $1,000,000).\n"
                    "2. **Exposure Factor (EF)**: Percentage of asset value lost if a threat strikes (e.g., 40% = 0.40).\n"
                    "3. **Single Loss Expectancy (SLE)**: Financial loss from a single security incident:\n"
                    "   `SLE = AV x EF` (e.g., $1,000,000 x 0.40 = $400,000).\n"
                    "4. **Annualized Rate of Occurrence (ARO)**: Estimated number of times the event occurs per year (e.g., once every 2 years = 0.5).\n"
                    "5. **Annualized Loss Expectancy (ALE)**: Total annual expected financial loss:\n"
                    "   `ALE = SLE x ARO` (e.g., $400,000 x 0.5 = $200,000/year).\n\n"
                    "*Rule of Thumb*: You should never spend more on a security control than the ALE of the risk it prevents!"
                )
            },
            {
                "heading": "The 4 Strategies of Risk Treatment",
                "content": (
                    "When a security risk is identified, leadership must select one of four paths:\n"
                    "- **Mitigation (Reduction)**: Deploying technical/administrative controls (firewalls, patching, training) to lower likelihood or impact.\n"
                    "- **Transfer (Transference)**: Shifting financial impact to a third party (purchasing **Cyber Insurance** or outsourcing to a cloud provider).\n"
                    "- **Acceptance**: Acknowledging the risk and choosing to absorb potential losses because the cost of fixing it exceeds the potential damage.\n"
                    "- **Avoidance**: Completely terminating the risky business activity (e.g., canceling a high-risk software project)."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Python: Quantitative Risk Assessment Calculator (ALE)",
                "language": "python",
                "code": (
                    "def calculate_ale(asset_value: float, exposure_factor: float, aro: float) -> dict:\n"
                    "    sle = asset_value * exposure_factor\n"
                    "    ale = sle * aro\n"
                    "    return {\n"
                    "        'asset_value': asset_value,\n"
                    "        'sle': sle,\n"
                    "        'aro': aro,\n"
                    "        'ale': ale,\n"
                    "        'max_justified_countermeasure_budget_annual': ale\n"
                    "    }\n\n"
                    "# Example: Web store worth $500,000, outage causes 30% loss, occurs twice a year\n"
                    "result = calculate_ale(asset_value=500000.0, exposure_factor=0.30, aro=2.0)\n"
                    "for k, v in result.items():\n"
                    "    print(f'{k}: ${v:,.2f}' if 'value' in k or 'le' in k or 'budget' in k else f'{k}: {v}')"
                ),
                "explanation": "Quantitative risk calculations provide financial justification for executive security budgets."
            },
            {
                "title": "Mapping Risk Strategy to Scenarios",
                "language": "bash",
                "code": (
                    "# Scenario 1: Deploying EDR and MFA -> RISK MITIGATION\n"
                    "# Scenario 2: Purchasing a $5M Cyber Insurance Policy -> RISK TRANSFER\n"
                    "# Scenario 3: Deciding not to expand e-commerce into a hostile nation -> RISK AVOIDANCE\n"
                    "# Scenario 4: Choosing not to patch an isolated legacy test lab machine -> RISK ACCEPTANCE"
                ),
                "explanation": "Executive risk governance requires deliberate categorization of risk handling decisions."
            }
        ],
        coding_challenge={
            "description": "Write a Python function `recommend_risk_strategy(action_type: str) -> str` that maps 'BUY_CYBER_INSURANCE' -> 'TRANSFER', 'DEPLOY_FIREWALL' -> 'MITIGATE', 'CANCEL_PROJECT' -> 'AVOID', and 'SIGN_WAIVER' -> 'ACCEPT'. Return 'UNKNOWN' for any other string.",
            "starter_code": (
                "def recommend_risk_strategy(action_type: str) -> str:\n"
                "    # Return 'TRANSFER', 'MITIGATE', 'AVOID', 'ACCEPT', or 'UNKNOWN'\n"
                "    return ''\n\n"
                "print(recommend_risk_strategy('BUY_CYBER_INSURANCE'))\n"
                "print(recommend_risk_strategy('DEPLOY_FIREWALL'))\n"
                "print(recommend_risk_strategy('CANCEL_PROJECT'))"
            ),
            "solution_code": (
                "def recommend_risk_strategy(action_type: str) -> str:\n"
                "    mapping = {\n"
                "        'BUY_CYBER_INSURANCE': 'TRANSFER',\n"
                "        'DEPLOY_FIREWALL': 'MITIGATE',\n"
                "        'CANCEL_PROJECT': 'AVOID',\n"
                "        'SIGN_WAIVER': 'ACCEPT'\n"
                "    }\n"
                "    return mapping.get(action_type.upper(), 'UNKNOWN')\n\n"
                "print(recommend_risk_strategy('BUY_CYBER_INSURANCE'))\n"
                "print(recommend_risk_strategy('DEPLOY_FIREWALL'))\n"
                "print(recommend_risk_strategy('CANCEL_PROJECT'))"
            ),
            "expected_output": "TRANSFER\nMITIGATE\nAVOID"
        },
        quizzes=[
            {
                "question": "In quantitative risk management, what is the formula to calculate Annualized Loss Expectancy (ALE)?",
                "options": [
                    "ALE = Single Loss Expectancy (SLE) x Annualized Rate of Occurrence (ARO)",
                    "ALE = Asset Value / Number of Firewalls",
                    "ALE = CPU Speed x Hard Drive Size",
                    "ALE = Total Passwords + Employees"
                ],
                "correct_answer": "ALE = Single Loss Expectancy (SLE) x Annualized Rate of Occurrence (ARO)",
                "explanation": "ALE represents the total annual expected loss, calculated by multiplying the loss per incident (SLE) by annual frequency (ARO)."
            },
            {
                "question": "Purchasing a comprehensive Cyber Insurance policy to cover financial losses from potential ransomware attacks is an example of which risk management strategy?",
                "options": ["Risk Transfer (Transference)", "Risk Mitigation", "Risk Avoidance", "Risk Acceptance"],
                "correct_answer": "Risk Transfer (Transference)",
                "explanation": "Risk Transfer shifts the financial burden of an incident to a third party, such as an insurance company or cloud provider."
            },
            {
                "question": "Deploying a Next-Generation Firewall and implementing Multi-Factor Authentication are examples of which risk response strategy?",
                "options": ["Risk Mitigation (Reduction)", "Risk Acceptance", "Risk Avoidance", "Risk Elimination"],
                "correct_answer": "Risk Mitigation (Reduction)",
                "explanation": "Mitigation deploys technical or administrative controls to reduce the likelihood or impact of potential vulnerabilities."
            },
            {
                "question": "What is 'Risk Acceptance'?",
                "options": [
                    "An informed executive decision to acknowledge an identified risk and absorb potential losses without applying additional costly controls",
                    "Pretending that hackers do not exist",
                    "Surrendering to a ransomware demand",
                    "Refusing to run antivirus software"
                ],
                "correct_answer": "An informed executive decision to acknowledge an identified risk and absorb potential losses without applying additional costly controls",
                "explanation": "Acceptance is chosen when the cost of countermeasure controls exceeds the total potential loss of the risk itself."
            },
            {
                "question": "What is the difference between Qualitative and Quantitative risk assessments?",
                "options": [
                    "Quantitative uses specific numerical dollar figures and percentages; Qualitative uses subjective severity rankings (e.g., High, Medium, Low)",
                    "Quantitative is for Linux; Qualitative is for Windows",
                    "Quantitative does not use math",
                    "Qualitative only assesses physical door locks"
                ],
                "correct_answer": "Quantitative uses specific numerical dollar figures and percentages; Qualitative uses subjective severity rankings (e.g., High, Medium, Low)",
                "explanation": "Quantitative assessment calculates financial values (SLE, ALE); qualitative assessment uses expert judgment matrices (High/Medium/Low)."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 56: Vulnerability Scanning vs Penetration Testing (Pen Test)
    # ---------------------------------------------------------
    DayBlueprint(
        order=56,
        title="Day 56: Vulnerability Scanning vs Penetration Testing (Pen Test)",
        concept="Differentiating between passive vulnerability scanning (automated, broad, high false positives) and active penetration testing (human-led, exploitation, proof of concept, black/white/gray box).",
        analogy="Think of building security testing: A Vulnerability Scan is a security guard walking around the outside of your building with a clipboard, shining a flashlight at all 20 windows, and noting 'Window #4 looks like it might be unlocked.' A Penetration Test is a professional ethical burglar who physically climbs through Window #4, walks into the CEO's office, takes a selfie at their desk, and hands you the photograph in the morning as proof of breach.",
        theory_sections=[
            {
                "heading": "Vulnerability Scanning vs Penetration Testing",
                "content": (
                    "Organizations use both assessments for comprehensive posture validation:\n\n"
                    "1. **Vulnerability Scanning (Automated)**:\n"
                    "   - *Tools*: Nessus, Qualys, OpenVAS, Rapid7 InsightVM.\n"
                    "   - *Methodology*: Automated scanners probe networks, matching banners and open ports against known CVE vulnerability databases.\n"
                    "   - *Attributes*: Fast, cost-effective, can run weekly. High false-positive rate. **Does NOT exploit flaws**.\n\n"
                    "2. **Penetration Testing (Active Exploitation)**:\n"
                    "   - *Methodology*: Skilled ethical hackers attempt to actively exploit vulnerabilities to simulate real-world adversary breaches.\n"
                    "   - *Attributes*: Demonstrates actual business impact, chains multiple minor flaws together to gain domain admin, eliminates false positives. Conducted annually or after major changes."
                )
            },
            {
                "heading": "Penetration Testing Knowledge Methodologies",
                "content": (
                    "- **Black Box**: The tester has **Zero Prior Knowledge** of internal systems, simulating an external unauthenticated attacker.\n"
                    "- **White Box**: The tester has **Full Knowledge** (source code access, network diagrams, architectural documentation, credentials).\n"
                    "- **Gray Box**: The tester has **Partial Knowledge** (e.g., standard employee login credentials to test internal privilege escalation)."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Running an Automated Vulnerability Scan via OpenVAS / Nmap Scripts",
                "language": "bash",
                "code": (
                    "# Using Nmap Scripting Engine (NSE) to scan for critical known vulnerabilities:\n"
                    "nmap -sV --script vuln 192.168.1.100\n\n"
                    "# Output identifies matching CVEs without actively weaponizing them:\n"
                    "# | ssl-heartbleed: \n"
                    "# |   VULNERABLE:\n"
                    "# |   The Heartbleed Bug is a serious vulnerability in OpenSSL (CVE-2014-0160)"
                ),
                "explanation": "Automated vulnerability scans identify potential exposure signatures across host networks."
            },
            {
                "title": "Python: Classifying Assessment Findings by Exploit Confirmation",
                "language": "python",
                "code": (
                    "def classify_assessment_finding(finding: dict) -> str:\n"
                    "    if finding.get('exploit_executed_successfully'):\n"
                    "        return 'PEN_TEST_VERIFIED: Exploit successfully demonstrated Proof-of-Concept!'\n"
                    "    elif finding.get('cve_signature_matched'):\n"
                    "        return 'VULN_SCAN_DETECTED: Potential vulnerability identified based on version banner.'\n"
                    "    return 'INFO: Normal finding'\n\n"
                    "scan_item = {'cve_signature_matched': True, 'exploit_executed_successfully': False}\n"
                    "pentest_item = {'cve_signature_matched': True, 'exploit_executed_successfully': True}\n"
                    "print(classify_assessment_finding(scan_item))\n"
                    "print(classify_assessment_finding(pentest_item))"
                ),
                "explanation": "Penetration testing moves beyond signature detection by proving exploitability."
            }
        ],
        coding_challenge={
            "description": "Write a Python function `classify_box_testing(has_source_code: bool, has_credentials: bool) -> str` that returns 'WHITE_BOX' if both are True, 'BLACK_BOX' if both are False, and 'GRAY_BOX' if one is True and the other is False.",
            "starter_code": (
                "def classify_box_testing(has_source_code: bool, has_credentials: bool) -> str:\n"
                "    # Return 'WHITE_BOX', 'BLACK_BOX', or 'GRAY_BOX'\n"
                "    return ''\n\n"
                "print(classify_box_testing(False, False))\n"
                "print(classify_box_testing(True, True))\n"
                "print(classify_box_testing(False, True))"
            ),
            "solution_code": (
                "def classify_box_testing(has_source_code: bool, has_credentials: bool) -> str:\n"
                "    if has_source_code and has_credentials:\n"
                "        return 'WHITE_BOX'\n"
                "    if not has_source_code and not has_credentials:\n"
                "        return 'BLACK_BOX'\n"
                "    return 'GRAY_BOX'\n\n"
                "print(classify_box_testing(False, False))\n"
                "print(classify_box_testing(True, True))\n"
                "print(classify_box_testing(False, True))"
            ),
            "expected_output": "BLACK_BOX\nWHITE_BOX\nGRAY_BOX"
        },
        quizzes=[
            {
                "question": "What is the primary difference between an automated Vulnerability Scan and an ethical Penetration Test?",
                "options": [
                    "A vulnerability scan identifies potential flaws using automated tools without exploiting them; a penetration test actively exploits vulnerabilities to prove real-world impact",
                    "A vulnerability scan is illegal, while a penetration test is legal",
                    "Penetration tests only check printer ink levels",
                    "Vulnerability scans are only conducted on weekends"
                ],
                "correct_answer": "A vulnerability scan identifies potential flaws using automated tools without exploiting them; a penetration test actively exploits vulnerabilities to prove real-world impact",
                "explanation": "Scanners passively flag potential CVEs based on banners; pen testers actively chain and exploit flaws to prove security impact."
            },
            {
                "question": "What characterizes a 'Black Box' penetration test?",
                "options": [
                    "The penetration tester has zero prior internal knowledge, documentation, or credentials regarding the target network, simulating an external adversary",
                    "The tester works in a room with the lights turned off",
                    "The tester only uses computers painted black",
                    "The test is performed on an airplane flight recorder"
                ],
                "correct_answer": "The penetration tester has zero prior internal knowledge, documentation, or credentials regarding the target network, simulating an external adversary",
                "explanation": "Black Box simulates an unprivileged external attacker attempting blind reconnaissance and intrusion."
            },
            {
                "question": "In which penetration testing methodology does the security auditor receive full architectural diagrams, network topologies, and complete source code access?",
                "options": ["White Box Testing", "Black Box Testing", "Red Box Testing", "Blind Testing"],
                "correct_answer": "White Box Testing",
                "explanation": "White Box (crystal box) provides full transparency, allowing deep source-code auditing and comprehensive internal assessment."
            },
            {
                "question": "What is a 'False Positive' produced by an automated vulnerability scanner?",
                "options": [
                    "The scanner reports that a system is vulnerable when it is actually secure or patched",
                    "The scanner catches on fire",
                    "The computer crashes during the scan",
                    "The scanner finds a brand new zero-day"
                ],
                "correct_answer": "The scanner reports that a system is vulnerable when it is actually secure or patched",
                "explanation": "Automated scanners often flag false positives based purely on version banners, even if the vendor has backported security patches."
            },
            {
                "question": "What legal document must be formally signed by corporate executives before a third-party penetration testing firm begins offensive testing?",
                "options": ["Rules of Engagement (RoE) / Authorization Letter (Get Out of Jail Free Card)", "A nondisclosure agreement only", "A copyright registration form", "A building lease contract"],
                "correct_answer": "Rules of Engagement (RoE) / Authorization Letter (Get Out of Jail Free Card)",
                "explanation": "Penetration testing without signed Rules of Engagement and explicit legal authorization is illegal computer intrusion."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 57: Business Continuity Plan (BCP) & Disaster Recovery (DR)
    # ---------------------------------------------------------
    DayBlueprint(
        order=57,
        title="Day 57: Business Continuity Plan (BCP) & Disaster Recovery (DR)",
        concept="Mastering operational resilience: Business Continuity Planning (BCP), Disaster Recovery (DR), Recovery Time Objective (RTO), Recovery Point Objective (RPO), and recovery sites (Hot, Warm, Cold).",
        analogy="Think of a power outage at a major hospital: The Disaster Recovery (DR) plan is the technical maintenance crew rushing to the basement to crank on the diesel electrical backup generators. The Business Continuity Plan (BCP) is the medical leadership ensuring that ICU patients remain on battery ventilators, doctors use flashlights, and paper medical charts are distributed so patient care continues without interruption.",
        theory_sections=[
            {
                "heading": "BCP vs Disaster Recovery",
                "content": (
                    "Disasters (hurricanes, fiber cuts, ransomware wipes) threaten organizational survival:\n\n"
                    "1. **BCP (Business Continuity Plan)**: Strategic, holistic business operations plan. Focuses on keeping critical business operations running during and immediately after a disaster (relocating staff, alternate supply chains, crisis communications).\n"
                    "2. **Disaster Recovery (DR)**: Technical IT plan. Focuses specifically on restoring IT infrastructure, servers, databases, and network connectivity after an outage."
                )
            },
            {
                "heading": "The Golden Metrics: RTO vs RPO",
                "content": (
                    "- **RTO (Recovery Time Objective)**: The maximum tolerable duration of system downtime (*How long can the system be down before business suffers catastrophic damage?* E.g., RTO = 2 hours).\n"
                    "- **RPO (Recovery Point Objective)**: The maximum tolerable amount of data loss measured in time (*How far back do backups go?* E.g., if you back up once every 24 hours at midnight and a disaster strikes at 11:00 PM, you lose 23 hours of transactional data. If RPO = 15 minutes, you must replicate databases every 15 minutes)."
                )
            },
            {
                "heading": "DR Recovery Site Types",
                "content": (
                    "- **Hot Site**: Fully duplicated, near-instant mirror datacenter with live synchronized data and active servers. RTO = Minutes. Most expensive.\n"
                    "- **Warm Site**: Hardware and networking pre-installed, but data backups must be restored and loaded before taking over. RTO = Hours to days.\n"
                    "- **Cold Site**: An empty physical room with power, raised floors, and HVAC, but zero computers or data. RTO = Weeks. Cheapest."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Automating Offsite Backup Synchronization via rsync CLI",
                "language": "bash",
                "code": (
                    "# Synchronizing critical database snapshots to an offsite DR backup vault:\n"
                    "rsync -avz --delete -e \"ssh -i /root/.ssh/dr_key\" \\\n"
                    "  /var/backups/postgresql/ \\\n"
                    "  dr-backup-vault.company.com:/mnt/dr_backups/postgresql/"
                ),
                "explanation": "Automated offsite backup replication fulfills tight Recovery Point Objectives (RPO)."
            },
            {
                "title": "Python: Evaluating RTO and RPO SLA Compliance",
                "language": "python",
                "code": (
                    "def evaluate_dr_metrics(actual_downtime_hours: float, max_rto_hours: float,\n"
                    "                        data_loss_hours: float, max_rpo_hours: float) -> dict:\n"
                    "    rto_met = actual_downtime_hours <= max_rto_hours\n"
                    "    rpo_met = data_loss_hours <= max_rpo_hours\n"
                    "    \n"
                    "    return {\n"
                    "        'rto_status': 'PASS' if rto_met else f'FAIL: Downtime {actual_downtime_hours}h exceeded {max_rto_hours}h',\n"
                    "        'rpo_status': 'PASS' if rpo_met else f'FAIL: Data loss {data_loss_hours}h exceeded {max_rpo_hours}h',\n"
                    "        'dr_success': rto_met and rpo_met\n"
                    "    }\n\n"
                    "print(evaluate_dr_metrics(1.5, 4.0, 0.25, 1.0))\n"
                    "print(evaluate_dr_metrics(6.0, 4.0, 2.5, 1.0))"
                ),
                "explanation": "Calculates post-disaster recovery compliance against target RTO and RPO metrics."
            }
        ],
        coding_challenge={
            "description": "Write a Python function `select_recovery_site(budget_tier: str, rto_requirement: str) -> str` that returns 'HOT_SITE' if rto_requirement == 'MINUTES', 'WARM_SITE' if rto_requirement == 'HOURS', and 'COLD_SITE' if rto_requirement == 'DAYS'.",
            "starter_code": (
                "def select_recovery_site(budget_tier: str, rto_requirement: str) -> str:\n"
                "    # Return 'HOT_SITE', 'WARM_SITE', or 'COLD_SITE'\n"
                "    return ''\n\n"
                "print(select_recovery_site('HIGH', 'MINUTES'))\n"
                "print(select_recovery_site('MEDIUM', 'HOURS'))\n"
                "print(select_recovery_site('LOW', 'DAYS'))"
            ),
            "solution_code": (
                "def select_recovery_site(budget_tier: str, rto_requirement: str) -> str:\n"
                "    rto = rto_requirement.upper()\n"
                "    if rto == 'MINUTES':\n"
                "        return 'HOT_SITE'\n"
                "    if rto == 'HOURS':\n"
                "        return 'WARM_SITE'\n"
                "    return 'COLD_SITE'\n\n"
                "print(select_recovery_site('HIGH', 'MINUTES'))\n"
                "print(select_recovery_site('MEDIUM', 'HOURS'))\n"
                "print(select_recovery_site('LOW', 'DAYS'))"
            ),
            "expected_output": "HOT_SITE\nWARM_SITE\nCOLD_SITE"
        },
        quizzes=[
            {
                "question": "What is the critical distinction between a Business Continuity Plan (BCP) and a Disaster Recovery (DR) plan?",
                "options": [
                    "BCP focuses on maintaining overall business operations during a crisis; DR focuses specifically on restoring technical IT systems and data",
                    "BCP is for small businesses, while DR is for large corporations",
                    "DR is about human resources, while BCP is about computers",
                    "There is no difference"
                ],
                "correct_answer": "BCP focuses on maintaining overall business operations during a crisis; DR focuses specifically on restoring technical IT systems and data",
                "explanation": "BCP ensures operational survival across the entire business; DR is the IT-centric technical subset focused on data and server recovery."
            },
            {
                "question": "What does Recovery Time Objective (RTO) define?",
                "options": [
                    "The maximum acceptable duration of system downtime that an organization can tolerate before suffering catastrophic business harm",
                    "The time it takes to reboot a computer",
                    "The speed at which emails are delivered",
                    "The amount of time employees take for lunch"
                ],
                "correct_answer": "The maximum acceptable duration of system downtime that an organization can tolerate before suffering catastrophic business harm",
                "explanation": "RTO measures downtime duration: how quickly systems must be brought back online to avoid unacceptable loss."
            },
            {
                "question": "What does Recovery Point Objective (RPO) define?",
                "options": [
                    "The maximum tolerable amount of data loss measured in time, dictating how frequently data backups must be performed",
                    "The number of servers in a datacenter",
                    "The price of backup tape drives",
                    "The geographic distance between branch offices"
                ],
                "correct_answer": "The maximum tolerable amount of data loss measured in time, dictating how frequently data backups must be performed",
                "explanation": "RPO dictates backup frequency: an RPO of 1 hour means the business can afford to lose at most 1 hour of newly entered transactional data."
            },
            {
                "question": "Which disaster recovery site provides a fully equipped, near-instant mirror datacenter with synchronized real-time data ready to take over within minutes?",
                "options": ["Hot Site", "Warm Site", "Cold Site", "Mobile Trailer"],
                "correct_answer": "Hot Site",
                "explanation": "A Hot Site is a live, synchronized redundant facility providing near-zero RTO failover capabilities at high operational cost."
            },
            {
                "question": "What is a 'Cold Site' in disaster recovery planning?",
                "options": [
                    "An empty facility with power, HVAC, and network connections, but zero computer hardware or data installed, taking weeks to become operational",
                    "A server room located in Antarctica",
                    "A server cooled with liquid nitrogen",
                    "A datacenter that only operates during winter"
                ],
                "correct_answer": "An empty facility with power, HVAC, and network connections, but zero computer hardware or data installed, taking weeks to become operational",
                "explanation": "A Cold Site provides physical space, power, and cooling, but requires purchasing and shipping equipment before operations can resume."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 58: Security Policies (AUP, Password Policies)
    # ---------------------------------------------------------
    DayBlueprint(
        order=58,
        title="Day 58: Security Policies (AUP, Password Policies)",
        concept="Mastering administrative governance controls: Acceptable Use Policy (AUP), Information Security Policies, Modern Password Policies (NIST SP 800-63B length vs complexity), and data classification schemes.",
        analogy="Think of traffic laws and road signs: Technical controls (firewalls) are concrete highway guardrails that physically stop your car from going over a cliff. Administrative Security Policies are the speed limit signs and driver license rules: they define clear boundaries of acceptable behavior, establish legal accountability, and give the police authority to revoke your license if you drive recklessly.",
        theory_sections=[
            {
                "heading": "Core Organizational Security Policies",
                "content": (
                    "Security tools are ineffective without enforceable administrative policies:\n\n"
                    "1. **AUP (Acceptable Use Policy)**: Explicit agreement defining approved employee computer behavior (e.g., prohibition of personal torrenting, unauthorized software installation, or viewing inappropriate materials on company laptops).\n"
                    "2. **Information Security Policy**: High-level governance document outlining executive security commitments, risk management, and regulatory compliance.\n"
                    "3. **Data Classification Policy**: Categorizing records into tiered sensitivity levels:\n"
                    "   - *Public*: Press releases, public marketing.\n"
                    "   - *Internal*: Intranet phone directories, employee handbooks.\n"
                    "   - *Confidential*: Source code, customer records, accounting files.\n"
                    "   - *Restricted / Secret*: Executive mergers, trade secrets, encryption keys."
                )
            },
            {
                "heading": "Modern Password Policies: The NIST Revolution (SP 800-63B)",
                "content": (
                    "For years, companies forced complex, 8-character passwords with mandatory 90-day expiration. **NIST completely debunked this legacy guidance**:\n"
                    "- Mandatory 90-day changes led to users writing `Winter2024!` -> `Spring2024!` on sticky notes.\n"
                    "- **Modern Standard**: Favor **Password Length (Passphrases of 15+ characters)** over confusing character complexity.\n"
                    "- Screen passwords against known breached password lists (HaveIBeenPwned).\n"
                    "- **Never expire passwords arbitrarily** unless there is evidence of an actual compromise."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Active Directory Group Policy Password Policy Configuration",
                "language": "bash",
                "code": (
                    "# Windows PowerShell Active Directory Fine-Grained Password Policy:\n"
                    "New-ADFineGrainedPasswordPolicy -Name \"HighSecurityStaff\" \\\n"
                    "  -Precedence 10 \\\n"
                    "  -MinPasswordLength 15 \\\n"
                    "  -PasswordHistoryCount 24 \\\n"
                    "  -LockoutThreshold 5 \\\n"
                    "  -LockoutDuration (New-TimeSpan -Minutes 30) \\\n"
                    "  -ComplexityEnabled $True"
                ),
                "explanation": "Sysadmins configure domain policies enforcing passphrases and account lockout limits across all corporate workstations."
            },
            {
                "title": "Python: Auditing Password Strength Against NIST SP 800-63B",
                "language": "python",
                "code": (
                    "def audit_password_nist(password: str, common_blacklist: set) -> dict:\n"
                    "    if len(password) < 15:\n"
                    "        return {'compliant': False, 'reason': f'Length {len(password)} < 15 characters required (Use a passphrase!)'}\n"
                    "    if password.lower() in common_blacklist:\n"
                    "        return {'compliant': False, 'reason': 'Password matches common breached password list!'}\n"
                    "    return {'compliant': True, 'reason': 'Meets modern NIST passphrase standard'}\n\n"
                    "blacklist = {'correcthorsebatterystaple', 'password12345678'}\n"
                    "print(audit_password_nist('P@ss1!', blacklist))\n"
                    "print(audit_password_nist('purple-dinosaur-coffee-jump-2024', blacklist))"
                ),
                "explanation": "Validates password compliance focusing on length and breach dictionary screening."
            }
        ],
        coding_challenge={
            "description": "Write a Python function `classify_data_label(is_public_marketing: bool, contains_customer_pii: bool, is_merger_secret: bool) -> str` that returns 'RESTRICTED' if is_merger_secret is True, 'CONFIDENTIAL' if contains_customer_pii is True, 'PUBLIC' if is_public_marketing is True, and 'INTERNAL' otherwise.",
            "starter_code": (
                "def classify_data_label(is_public_marketing: bool, contains_customer_pii: bool, is_merger_secret: bool) -> str:\n"
                "    # Return data classification label\n"
                "    return ''\n\n"
                "print(classify_data_label(False, False, True))\n"
                "print(classify_data_label(False, True, False))\n"
                "print(classify_data_label(True, False, False))"
            ),
            "solution_code": (
                "def classify_data_label(is_public_marketing: bool, contains_customer_pii: bool, is_merger_secret: bool) -> str:\n"
                "    if is_merger_secret:\n"
                "        return 'RESTRICTED'\n"
                "    if contains_customer_pii:\n"
                "        return 'CONFIDENTIAL'\n"
                "    if is_public_marketing:\n"
                "        return 'PUBLIC'\n"
                "    return 'INTERNAL'\n\n"
                "print(classify_data_label(False, False, True))\n"
                "print(classify_data_label(False, True, False))\n"
                "print(classify_data_label(True, False, False))"
            ),
            "expected_output": "RESTRICTED\nCONFIDENTIAL\nPUBLIC"
        },
        quizzes=[
            {
                "question": "What is an Acceptable Use Policy (AUP) in an enterprise organization?",
                "options": [
                    "A policy agreement signed by employees detailing approved vs prohibited uses of corporate computers, network hardware, and internet access",
                    "A warranty for purchasing new keyboards",
                    "A recipe book for office lunches",
                    "A contract with the power company"
                ],
                "correct_answer": "A policy agreement signed by employees detailing approved vs prohibited uses of corporate computers, network hardware, and internet access",
                "explanation": "AUP defines acceptable employee computer behavior, providing legal grounds for discipline or termination if violated."
            },
            {
                "question": "According to modern NIST Special Publication 800-63B password guidance, which factor provides the greatest security improvement?",
                "options": [
                    "Password Length (e.g., 15+ character passphrases) screened against known breached password lists",
                    "Forcing users to change passwords every 30 days",
                    "Requiring exclamation marks and hashtags in 8-character passwords",
                    "Making passwords expire every 24 hours"
                ],
                "correct_answer": "Password Length (e.g., 15+ character passphrases) screened against known breached password lists",
                "explanation": "NIST emphasizes length (passphrases) and breach screening over periodic arbitrary expiration, which only creates weak predictable variations."
            },
            {
                "question": "Why does NIST recommend AGAINST forcing users to change their passwords every 60 to 90 days if no compromise has occurred?",
                "options": [
                    "Frequent forced changes cause users to create predictable pattern variations (e.g., Winter2023! -> Winter2024!) or write them on sticky notes",
                    "Password changes damage computer hard drives",
                    "Changing passwords consumes all network bandwidth",
                    "It causes domain controllers to overheat"
                ],
                "correct_answer": "Frequent forced changes cause users to create predictable pattern variations (e.g., Winter2023! -> Winter2024!) or write them on sticky notes",
                "explanation": "Empirical studies prove that arbitrary 90-day expirations degrade password security as frustrated users resort to predictable patterns."
            },
            {
                "question": "Under a standard corporate Data Classification policy, what classification tier applies to customer credit cards, employee Social Security Numbers, and medical records?",
                "options": ["Confidential (or Restricted)", "Public", "Unclassified", "Informational"],
                "correct_answer": "Confidential (or Restricted)",
                "explanation": "PII, PHI, and financial records are classified as Confidential or Restricted, requiring mandatory encryption and strict access controls."
            },
            {
                "question": "What type of security control is a written corporate policy document classified as?",
                "options": ["Administrative (Managerial) Control", "Technical Control", "Physical Control", "Cryptographic Control"],
                "correct_answer": "Administrative (Managerial) Control",
                "explanation": "Policies, procedures, employee training, and background checks are classified as Administrative/Managerial controls."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 59: Security Awareness Training for Employees
    # ---------------------------------------------------------
    DayBlueprint(
        order=59,
        title="Day 59: Security Awareness Training for Employees",
        concept="Mastering human layer defense: Security awareness training, simulated phishing campaigns, Clean Desk policies, recognizing social engineering, and building a proactive security culture.",
        analogy="Think of a modern submarine: You can build titanium hull walls, install advanced sonar, and configure automated fire doors, but if a single crew member forgets to close an airlock valve while diving, the entire submarine floods. Security awareness training ensures every crew member understands how their daily actions protect the vessel.",
        theory_sections=[
            {
                "heading": "The Human Element: The Strongest or Weakest Link",
                "content": (
                    "Technical defenses (firewalls, EDR, spam filters) can stop 99% of commodity attacks, but threat actors bypass technology by targeting human psychology:\n\n"
                    "1. **Continuous vs Annual Training**: Annual 30-minute slide shows fail completely. Modern security cultures use **Continuous Micro-Learning** (short 2-minute monthly interactive modules).\n"
                    "2. **Simulated Phishing Campaigns**: Automated platforms (KnowBe4, Infosec IQ) send realistic, benign test phishing emails. Employees who click are immediately provided with non-punitive, just-in-time training.\n"
                    "3. **Clean Desk & Clear Screen Policy**: Mandates locking computer screens (`Win + L`) when walking away and securing sensitive paper documents, badges, and keys in locked drawers overnight.\n"
                    "4. **No-Blame Reporting Culture**: If an employee accidentally clicks a suspicious link, they must feel safe reporting it to IT immediately without fear of termination, allowing the SOC to contain the incident before encryption begins."
                )
            },
            {
                "heading": "Recognizing Red Flags in Communications",
                "content": (
                    "Employees are trained to pause whenever communications exhibit:\n"
                    "- Artificial urgency or emotional pressure.\n"
                    "- Mismatched sender domains (e.g., `payroll@company-support-desk.com` instead of `@company.com`).\n"
                    "- Requests to bypass standard payment authorization procedures."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Windows Keyboard Shortcut to Lock Screen Immediately",
                "language": "bash",
                "code": (
                    "# Windows Lock Screen command (Clean Screen Policy):\n"
                    "# Keyboard: Windows Key + L\n"
                    "rundll32.exe user32.dll,LockWorkStation\n\n"
                    "# Linux Screen Lock shortcut (GNOME):\n"
                    "# Keyboard: Super Key + L"
                ),
                "explanation": "Employees must instinctively lock their workstations whenever stepping away from their desk."
            },
            {
                "title": "Python: Tracking Simulated Phishing Click-Through Rates",
                "language": "python",
                "code": (
                    "def evaluate_phishing_campaign(total_sent: int, clicked: int, reported_to_soc: int) -> dict:\n"
                    "    click_rate = (clicked / total_sent) * 100\n"
                    "    report_rate = (reported_to_soc / total_sent) * 100\n"
                    "    culture_rating = 'STRONG'\n"
                    "    if click_rate > 15.0 or report_rate < 50.0:\n"
                    "        culture_rating = 'NEEDS_IMPROVEMENT'\n"
                    "    return {\n"
                    "        'click_rate_percent': click_rate,\n"
                    "        'report_rate_percent': report_rate,\n"
                    "        'culture_rating': culture_rating\n"
                    "    }\n\n"
                    "print(evaluate_phishing_campaign(total_sent=1000, clicked=40, reported_to_soc=650))\n"
                    "print(evaluate_phishing_campaign(total_sent=1000, clicked=220, reported_to_soc=100))"
                ),
                "explanation": "Security teams benchmark organizational resilience through simulated phishing metrics."
            }
        ],
        coding_challenge={
            "description": "Write a Python function `screen_clean_desk_violation(items_on_desk: list) -> list` that inspects a list of strings on a desk and returns a list of items that violate a Clean Desk policy ('PASSWORDS_STICKY_NOTE', 'UNENCRYPTED_USB', 'PRINTED_SALARY_REPORT').",
            "starter_code": (
                "def screen_clean_desk_violation(items_on_desk: list) -> list:\n"
                "    # Return list of policy violating items\n"
                "    return []\n\n"
                "desk = ['COFFEE_MUG', 'PASSWORDS_STICKY_NOTE', 'PEN', 'PRINTED_SALARY_REPORT']\n"
                "print(screen_clean_desk_violation(desk))"
            ),
            "solution_code": (
                "def screen_clean_desk_violation(items_on_desk: list) -> list:\n"
                "    prohibited = {'PASSWORDS_STICKY_NOTE', 'UNENCRYPTED_USB', 'PRINTED_SALARY_REPORT', 'CUSTOMER_LIST'}\n"
                "    violations = [item for item in items_on_desk if item.upper() in prohibited]\n"
                "    return violations\n\n"
                "desk = ['COFFEE_MUG', 'PASSWORDS_STICKY_NOTE', 'PEN', 'PRINTED_SALARY_REPORT']\n"
                "print(screen_clean_desk_violation(desk))"
            ),
            "expected_output": "['PASSWORDS_STICKY_NOTE', 'PRINTED_SALARY_REPORT']"
        },
        quizzes=[
            {
                "question": "What is the primary goal of conducting simulated phishing campaigns against corporate employees?",
                "options": [
                    "To assess organizational vulnerability to social engineering and provide immediate, practical training to employees who fall for simulated lures",
                    "To fire employees who make mistakes",
                    "To collect employee passwords for management",
                    "To reduce company email server storage space"
                ],
                "correct_answer": "To assess organizational vulnerability to social engineering and provide immediate, practical training to employees who fall for simulated lures",
                "explanation": "Simulated phishing builds muscle memory, transforming employees from passive targets into active security sensors."
            },
            {
                "question": "What does a 'Clean Desk Policy' mandate for office employees?",
                "options": [
                    "Employees must lock away all sensitive documents, papers, sticky notes with passwords, and storage media when leaving their workspace",
                    "Desks must be wiped with sanitizing spray daily",
                    "Employees are not allowed to drink coffee at their desks",
                    "Computer monitors must be turned upside down"
                ],
                "correct_answer": "Employees must lock away all sensitive documents, papers, sticky notes with passwords, and storage media when leaving their workspace",
                "explanation": "Clean Desk policies prevent visual snooping, shoulder surfing, and physical theft by visitors, contractors, or cleaners."
            },
            {
                "question": "What keyboard shortcut should every Windows employee use instinctively whenever stepping away from their desk for lunch or coffee?",
                "options": ["Windows Key + L", "Ctrl + Alt + Delete", "Alt + F4", "Windows Key + D"],
                "correct_answer": "Windows Key + L",
                "explanation": "Pressing Windows + L instantly locks the workstation, requiring password/biometric authentication to re-enter."
            },
            {
                "question": "Why is a 'No-Blame' security reporting culture critical to effective enterprise defense?",
                "options": [
                    "Employees who fear termination will conceal their mistakes, allowing active ransomware or backdoors to spread undetected for weeks",
                    "Because managers do not like reading incident reports",
                    "Because hackers will apologize if you are friendly",
                    "Because security software works better without human reports"
                ],
                "correct_answer": "Employees who fear termination will conceal their mistakes, allowing active ransomware or backdoors to spread undetected for weeks",
                "explanation": "Fear of punishment delays reporting. Fast reporting allows the SOC to isolate the host and contain intrusions in minutes."
            },
            {
                "question": "Which psychological trigger is most frequently manipulated in phishing emails claiming 'Your account will be terminated in 15 minutes unless you verify credentials'?",
                "options": ["Artificial Urgency and Fear", "Curiosity and Humor", "Greed and Excitement", "Sadness and Pity"],
                "correct_answer": "Artificial Urgency and Fear",
                "explanation": "Urgency forces victims to react emotionally without pausing to verify sender headers, URLs, or legitimacy."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 60: Capstone: Compliance & Privacy Laws (GDPR, HIPAA, PCI-DSS, ISO 27001)
    # ---------------------------------------------------------
    DayBlueprint(
        order=60,
        title="Day 60 (Capstone): Compliance & Privacy Laws (GDPR, HIPAA, PCI-DSS, ISO 27001)",
        concept="Synthesizing enterprise cybersecurity governance: Global compliance frameworks and privacy legislation—GDPR (EU data privacy & right to be forgotten), HIPAA (healthcare PHI), PCI-DSS (credit card data), and ISO/IEC 27001 (information security management systems).",
        analogy="Think of building safety codes: A homeowner might build a rickety wooden staircase with no handrails because it was cheap. But the municipal building safety inspector arrives with a legal codebook: 'The steps must support 500 lbs, the handrail must be 36 inches high, and you must install an emergency fire exit.' Compliance frameworks are the legal, certified engineering blueprints that mandate minimum security standards across finance, healthcare, and technology.",
        theory_sections=[
            {
                "heading": "Major Global Cybersecurity & Privacy Frameworks",
                "content": (
                    "Cybersecurity is not just an IT concern—it is a strict legal and regulatory obligation:\n\n"
                    "1. **GDPR (General Data Protection Regulation - European Union)**:\n"
                    "   - Protects personal data of EU residents globally.\n"
                    "   - Key Rights: **Right to be Forgotten (Data Erasure)**, Data Portability, Explicit Consent.\n"
                    "   - Mandatory **72-Hour Breach Notification** to regulators.\n"
                    "   - Fines: Up to **€20 million or 4% of annual global turnover**, whichever is higher.\n\n"
                    "2. **HIPAA (Health Insurance Portability and Accountability Act - United States)**:\n"
                    "   - Protects **PHI (Protected Health Information)** across healthcare providers, insurers, and business associates.\n"
                    "   - Mandates technical safeguards (encryption, audit logging, access controls) and administrative training.\n\n"
                    "3. **PCI-DSS (Payment Card Industry Data Security Standard)**:\n"
                    "   - Global standard created by Visa, Mastercard, and Amex for any entity storing, processing, or transmitting cardholder data.\n"
                    "   - Strict rules: Never store CVV codes after authorization, encrypt cardholder data across public networks, maintain a firewall, and conduct regular penetration testing.\n\n"
                    "4. **ISO/IEC 27001**:\n"
                    "   - The international benchmark for establishing, implementing, maintaining, and continually improving an **ISMS (Information Security Management System)**. Audited by accredited third-party registrars."
                )
            },
            {
                "heading": "Capstone Reflection: The Complete Cybersecurity Mindset",
                "content": (
                    "Over 60 days, you have journeyed from physical computer hardware, networking protocols, malware analysis, and IAM, up through cryptographic primitives, perimeter firewalls, SOC operations, forensics, and regulatory governance. True cybersecurity is **Defense-in-Depth**: layering technology, processes, and people so that when any single layer fails, the next layer stands impenetrable."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Mapping Regulatory Frameworks to Business Sectors",
                "language": "bash",
                "code": (
                    "# Regulatory Mapping Matrix:\n"
                    "# Retail & Payments: PCI-DSS (Payment Card Industry)\n"
                    "# Healthcare & Hospitals: HIPAA (Protected Health Information)\n"
                    "# European Union Consumer Data: GDPR (General Data Protection Regulation)\n"
                    "# US Federal Government Systems: FISMA / NIST SP 800-53\n"
                    "# Global Enterprise Information Security: ISO/IEC 27001"
                ),
                "explanation": "Compliance officers map technical security controls directly to specific regulatory requirements."
            },
            {
                "title": "Python: Capstone Compliance Verification Engine",
                "language": "python",
                "code": (
                    "class EnterpriseComplianceAuditor:\n"
                    "    def __init__(self, controls: dict):\n"
                    "        self.controls = controls\n"
                    "    \n"
                    "    def audit_gdpr(self) -> bool:\n"
                    "        # Requires 72-hr breach SLA, encryption, user consent, right to delete\n"
                    "        return all([self.controls.get('encryption_at_rest'), self.controls.get('breach_notification_72h'), self.controls.get('data_erasure_supported')])\n"
                    "    \n"
                    "    def audit_pci_dss(self) -> bool:\n"
                    "        # Requires card data encryption, no CVV storage, network segmentation\n"
                    "        return all([self.controls.get('encryption_in_transit'), not self.controls.get('stores_cvv_codes'), self.controls.get('network_segmentation')])\n\n"
                    "current_controls = {\n"
                    "    'encryption_at_rest': True,\n"
                    "    'encryption_in_transit': True,\n"
                    "    'breach_notification_72h': True,\n"
                    "    'data_erasure_supported': True,\n"
                    "    'stores_cvv_codes': False,\n"
                    "    'network_segmentation': True\n"
                    "}\n"
                    "auditor = EnterpriseComplianceAuditor(current_controls)\n"
                    "print('GDPR Compliant:   ', auditor.audit_gdpr())\n"
                    "print('PCI-DSS Compliant:', auditor.audit_pci_dss())"
                ),
                "explanation": "Validates enterprise technical architecture against multi-regulatory compliance controls."
            }
        ],
        coding_challenge={
            "description": "Write a Python function `check_regulatory_requirement(data_type: str) -> str` that returns 'PCI_DSS' if data_type is 'CREDIT_CARDS', 'HIPAA' if 'PATIENT_HEALTH_RECORDS', 'GDPR' if 'EU_CITIZEN_PII', and 'GENERAL_SECURITY' for any other data type.",
            "starter_code": (
                "def check_regulatory_requirement(data_type: str) -> str:\n"
                "    # Return governing compliance framework string\n"
                "    return ''\n\n"
                "print(check_regulatory_requirement('CREDIT_CARDS'))\n"
                "print(check_regulatory_requirement('PATIENT_HEALTH_RECORDS'))\n"
                "print(check_regulatory_requirement('EU_CITIZEN_PII'))"
            ),
            "solution_code": (
                "def check_regulatory_requirement(data_type: str) -> str:\n"
                "    mapping = {\n"
                "        'CREDIT_CARDS': 'PCI_DSS',\n"
                "        'PATIENT_HEALTH_RECORDS': 'HIPAA',\n"
                "        'EU_CITIZEN_PII': 'GDPR'\n"
                "    }\n"
                "    return mapping.get(data_type.upper(), 'GENERAL_SECURITY')\n\n"
                "print(check_regulatory_requirement('CREDIT_CARDS'))\n"
                "print(check_regulatory_requirement('PATIENT_HEALTH_RECORDS'))\n"
                "print(check_regulatory_requirement('EU_CITIZEN_PII'))"
            ),
            "expected_output": "PCI_DSS\nHIPAA\nGDPR"
        },
        quizzes=[
            {
                "question": "Under the European Union General Data Protection Regulation (GDPR), within how many hours must an organization notify data protection authorities after becoming aware of a personal data breach?",
                "options": ["Within 72 hours", "Within 30 days", "Within 6 months", "Within 1 year"],
                "correct_answer": "Within 72 hours",
                "explanation": "GDPR Article 33 mandates reporting breaches of personal data to relevant supervisory authorities without undue delay and within 72 hours."
            },
            {
                "question": "What is the primary focus of the HIPAA (Health Insurance Portability and Accountability Act) Security Rule?",
                "options": [
                    "Protecting the confidentiality, integrity, and availability of electronic Protected Health Information (ePHI)",
                    "Regulating the prices of prescription medicines",
                    "Providing health insurance to college students",
                    "Designing medical equipment"
                ],
                "correct_answer": "Protecting the confidentiality, integrity, and availability of electronic Protected Health Information (ePHI)",
                "explanation": "HIPAA enforces administrative, physical, and technical safeguards for patient medical records and healthcare data."
            },
            {
                "question": "Which data element is STRICTLY FORBIDDEN from ever being stored by a merchant after payment card authorization under PCI-DSS rules?",
                "options": [
                    "The CVV / CVC (Card Verification Value 3-4 digit security code) and full magnetic stripe track data",
                    "The customer's email address",
                    "The merchant's store address",
                    "The transaction dollar total"
                ],
                "correct_answer": "The CVV / CVC (Card Verification Value 3-4 digit security code) and full magnetic stripe track data",
                "explanation": "PCI-DSS prohibits storing sensitive authentication data (CVV/CVC, full magnetic stripe data, PIN blocks) after authorization."
            },
            {
                "question": "What is ISO/IEC 27001?",
                "options": [
                    "The leading international standard providing requirements for establishing, implementing, maintaining, and continually improving an Information Security Management System (ISMS)",
                    "A type of fiber optic internet cable",
                    "A law passed by the United States Congress",
                    "A brand of computer processor"
                ],
                "correct_answer": "The leading international standard providing requirements for establishing, implementing, maintaining, and continually improving an Information Security Management System (ISMS)",
                "explanation": "ISO 27001 is the global gold standard for information security management systems, audited and certified by independent registrars."
            },
            {
                "question": "What is the core philosophical takeaway of the 'Defense-in-Depth' cybersecurity strategy?",
                "options": [
                    "Layering multiple diverse security controls (physical, technical, administrative) so that if any single protective layer is compromised, subsequent layers prevent total breach",
                    "Digging deep moats around the office building",
                    "Using only one very expensive firewall",
                    "Relying entirely on employee common sense"
                ],
                "correct_answer": "Layering multiple diverse security controls (physical, technical, administrative) so that if any single protective layer is compromised, subsequent layers prevent total breach",
                "explanation": "Defense-in-depth recognizes that no single security control is foolproof, providing layered barriers to protect organizational assets."
            }
        ]
    )
]
