"""
Cybersecurity & IT Fundamentals Curriculum - Days 21 to 40
Module 4: Threats, Attacks & Malware (Part 2: Days 21-24)
Module 5: Identity & Access Management (Days 25-30)
Module 6: Network & Infrastructure Security (Days 31-37)
Module 7: Cryptography & Data Protection (Part 1: Days 38-40)

Universal Standard Compliant:
- ELI5 markdown theory with beginner analogies
- Shell / Python / configuration snippets
- Daily hands-on coding or practical challenge
- Exactly 5 MCQs per day (100 total for Days 21-40)
"""

from seeder.course_blueprint import DayBlueprint

DAYS_21_TO_40 = [
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
,

    # ---------------------------------------------------------
    # Day 31: Firewalls (Network-based, Host-based, WAF)
    # ---------------------------------------------------------
    DayBlueprint(
        order=31,
        title="Day 31: Firewalls (Network-based, Host-based, WAF)",
        concept="Mastering network perimeter defense: Packet-filtering firewalls, Stateful inspection firewalls, Next-Generation Firewalls (NGFW), Host-based firewalls, and Layer 7 Web Application Firewalls (WAF).",
        analogy="Think of building security: A Packet-Filtering firewall is a bouncer checking guest list names. A Stateful firewall is a bouncer who remembers which guests were already inside so they can return from the restroom without re-checking. A Next-Gen Firewall (NGFW) is an airport X-ray scanner examining what is inside every suitcase. A Web Application Firewall (WAF) is a translator who reads every spoken sentence to make sure nobody slips in a disguised magic spell.",
        theory_sections=[
            {
                "heading": "Firewall Evolution & Types",
                "content": (
                    "Firewalls isolate and protect networks by inspecting traffic against security rules:\n\n"
                    "1. **Packet-Filtering Firewalls (Stateless)**: Inspects Layer 3 and Layer 4 headers (Source/Destination IP and Port) in isolation. Very fast, but cannot track connection state.\n"
                    "2. **Stateful Inspection Firewalls**: Maintains a **State Table** tracking established TCP handshakes. Outbound requests automatically permit inbound response packets without opening static ports.\n"
                    "3. **Next-Generation Firewalls (NGFW)**: Operates up to Layer 7 with Deep Packet Inspection (DPI), integrated IDS/IPS, TLS/SSL decryption, and application awareness (e.g., blocking Facebook games while allowing corporate Facebook posts).\n"
                    "4. **Host-Based vs Network-Based**: Network firewalls are dedicated hardware appliances protecting the whole subnet; host-based firewalls (Windows Defender Firewall, `iptables`/`ufw`) run as software on individual endpoints.\n"
                    "5. **Web Application Firewall (WAF)**: Sits in front of web servers to inspect HTTP/HTTPS payloads for SQL injection, Cross-Site Scripting, and credential stuffing."
                )
            },
            {
                "heading": "The Golden Rule: Implicit Deny",
                "content": (
                    "Enterprise firewalls are strictly configured with an **Implicit Deny** rule at the very bottom of the rule list: *Any traffic not explicitly permitted by a higher rule is automatically dropped.*"
                )
            }
        ],
        code_snippets=[
            {
                "title": "Configuring Firewall Rules (Linux UFW & Windows PowerShell)",
                "language": "bash",
                "code": (
                    "# Linux UFW (Uncomplicated Firewall):\n"
                    "sudo ufw default deny incoming       # Enforce implicit deny\n"
                    "sudo ufw default allow outgoing\n"
                    "sudo ufw allow 22/tcp                # Allow SSH\n"
                    "sudo ufw allow 443/tcp               # Allow HTTPS\n"
                    "sudo ufw enable\n\n"
                    "# Windows PowerShell Firewall Rule:\n"
                    "New-NetFirewallRule -DisplayName \"Block Port 23 Telnet\" -Direction Inbound -LocalPort 23 -Protocol TCP -Action Block"
                ),
                "explanation": "Sysadmins configure least-privilege firewall rule sets allowing only necessary ports while dropping unauthorized inbound traffic."
            },
            {
                "title": "Python: Simulating a Stateful Firewall Rule Engine",
                "language": "python",
                "code": (
                    "class StatefulFirewall:\n"
                    "    def __init__(self):\n"
                    "        self.state_table = set()  # (src_ip, dst_ip, src_port, dst_port)\n"
                    "        self.inbound_allow_rules = {(443, 'TCP'), (22, 'TCP')}\n"
                    "    \n"
                    "    def inspect_packet(self, direction: str, src: str, dst: str, port: int, proto: str) -> str:\n"
                    "        if direction == 'OUTBOUND':\n"
                    "            # Track outgoing connection in state table\n"
                    "            self.state_table.add((dst, src, port))  # Reverse mapping\n"
                    "            return 'ALLOW_OUTBOUND'\n"
                    "        \n"
                    "        # Inbound check: Is it an established response?\n"
                    "        if (src, dst, port) in self.state_table:\n"
                    "            return 'ALLOW_ESTABLISHED_RESPONSE'\n"
                    "        \n"
                    "        # Is it an approved new inbound service port?\n"
                    "        if (port, proto) in self.inbound_allow_rules:\n"
                    "            return 'ALLOW_NEW_SERVICE'\n"
                    "        return 'DROP (Implicit Deny)'\n\n"
                    "fw = StatefulFirewall()\n"
                    "fw.inspect_packet('OUTBOUND', '192.168.1.10', '93.184.216.34', 80, 'TCP')\n"
                    "print(fw.inspect_packet('INBOUND', '93.184.216.34', '192.168.1.10', 80, 'TCP'))\n"
                    "print(fw.inspect_packet('INBOUND', '1.2.3.4', '192.168.1.10', 23, 'TCP'))"
                ),
                "explanation": "Demonstrates state tracking: incoming response packets are recognized as part of an established conversation."
            }
        ],
        coding_challenge={
            "description": "Write a Python function `evaluate_firewall(direction: str, port: int, rule_list: list) -> str` that iterates through a list of rule dicts `[{'direction': str, 'port': int, 'action': 'ALLOW'/'BLOCK'}]` and returns the action of the first matching rule. If no rule matches, return 'BLOCK (Implicit Deny)'.",
            "starter_code": (
                "def evaluate_firewall(direction: str, port: int, rule_list: list) -> str:\n"
                "    # Return matching action or 'BLOCK (Implicit Deny)'\n"
                "    return ''\n\n"
                "rules = [\n"
                "    {'direction': 'INBOUND', 'port': 443, 'action': 'ALLOW'},\n"
                "    {'direction': 'INBOUND', 'port': 22, 'action': 'BLOCK'}\n"
                "]\n"
                "print(evaluate_firewall('INBOUND', 443, rules))\n"
                "print(evaluate_firewall('INBOUND', 22, rules))\n"
                "print(evaluate_firewall('INBOUND', 8080, rules))"
            ),
            "solution_code": (
                "def evaluate_firewall(direction: str, port: int, rule_list: list) -> str:\n"
                "    d_clean = direction.upper()\n"
                "    for rule in rule_list:\n"
                "        if rule.get('direction', '').upper() == d_clean and rule.get('port') == port:\n"
                "            return rule.get('action', 'BLOCK')\n"
                "    return 'BLOCK (Implicit Deny)'\n\n"
                "rules = [\n"
                "    {'direction': 'INBOUND', 'port': 443, 'action': 'ALLOW'},\n"
                "    {'direction': 'INBOUND', 'port': 22, 'action': 'BLOCK'}\n"
                "]\n"
                "print(evaluate_firewall('INBOUND', 443, rules))\n"
                "print(evaluate_firewall('INBOUND', 22, rules))\n"
                "print(evaluate_firewall('INBOUND', 8080, rules))"
            ),
            "expected_output": "ALLOW\nBLOCK\nBLOCK (Implicit Deny)"
        },
        quizzes=[
            {
                "question": "What is the primary operational advantage of a Stateful Inspection Firewall over a Stateless Packet-Filtering Firewall?",
                "options": [
                    "A stateful firewall tracks active connection sessions in a state table, automatically allowing return traffic for established outbound requests",
                    "A stateful firewall runs without electricity",
                    "A stateless firewall is immune to all DDoS attacks",
                    "A stateful firewall physically deletes bad hard drives"
                ],
                "correct_answer": "A stateful firewall tracks active connection sessions in a state table, automatically allowing return traffic for established outbound requests",
                "explanation": "Stateful firewalls remember outbound conversations, avoiding the need to open static wide-open inbound ports for response data."
            },
            {
                "question": "What does the 'Implicit Deny' rule at the bottom of a firewall access control list enforce?",
                "options": [
                    "Any network traffic that is not explicitly permitted by an earlier rule is automatically blocked and dropped",
                    "The firewall reboots every 10 minutes",
                    "All users must change passwords daily",
                    "Outbound web browsing is permanently disabled"
                ],
                "correct_answer": "Any network traffic that is not explicitly permitted by an earlier rule is automatically blocked and dropped",
                "explanation": "Implicit Deny is the foundational principle of least privilege in networking: silence and block everything unless explicitly whitelisted."
            },
            {
                "question": "Which type of firewall is specifically designed to inspect Layer 7 web traffic for SQL Injection, Cross-Site Scripting (XSS), and CSRF attacks?",
                "options": ["Web Application Firewall (WAF)", "Stateless Layer 3 Packet Filter", "Circuit-Level Gateway", "Ethernet Hub"],
                "correct_answer": "Web Application Firewall (WAF)",
                "explanation": "A WAF inspects HTTP/HTTPS application payloads, headers, cookies, and parameters to block web exploits before reaching the web server."
            },
            {
                "question": "What is the difference between a Host-Based Firewall and a Network-Based Firewall?",
                "options": [
                    "A host-based firewall runs as software directly on an individual computer protecting that single host, while a network firewall protects an entire subnet",
                    "Host-based firewalls only work on Linux",
                    "Network firewalls cannot block IP addresses",
                    "Host firewalls are installed in the cloud only"
                ],
                "correct_answer": "A host-based firewall runs as software directly on an individual computer protecting that single host, while a network firewall protects an entire subnet",
                "explanation": "Network firewalls protect perimeter boundaries, while host-based firewalls (like Windows Defender Firewall) enforce defense-in-depth on endpoints."
            },
            {
                "question": "What advanced capability distinguishes a Next-Generation Firewall (NGFW) from traditional stateful firewalls?",
                "options": [
                    "Deep Packet Inspection (DPI) capable of analyzing application layer data, detecting malware payloads, and decrypting TLS traffic",
                    "The ability to run without computer memory",
                    "Providing free internet to neighboring offices",
                    "Transmitting data faster than the speed of light"
                ],
                "correct_answer": "Deep Packet Inspection (DPI) capable of analyzing application layer data, detecting malware payloads, and decrypting TLS traffic",
                "explanation": "NGFWs integrate traditional firewalling with intrusion prevention (IPS), application-level control, and SSL inspection."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 32: IDS (Intrusion Detection System) vs IPS (Intrusion Prevention)
    # ---------------------------------------------------------
    DayBlueprint(
        order=32,
        title="Day 32: IDS (Intrusion Detection System) vs IPS (Intrusion Prevention)",
        concept="Differentiating between passive detection (IDS) and active inline prevention (IPS), analyzing detection methodologies (Signature-based vs Heuristic/Anomaly-based), and managing false positives vs false negatives.",
        analogy="Think of bank security: An IDS (Intrusion Detection System) is a security camera watching the lobby—if a masked thief enters, it sounds an alarm buzzer and logs the video, but does not stop them from running away. An IPS (Intrusion Prevention System) is an armed guard stationed inside an airlock door—if someone draws a weapon, the guard physically locks the security doors and blocks their path immediately.",
        theory_sections=[
            {
                "heading": "IDS vs IPS: Passive vs Inline",
                "content": (
                    "Both appliances analyze network packets for malicious activity:\n\n"
                    "1. **IDS (Intrusion Detection System)**: Deployed **Out-of-Band (Passive)** via a Switch Port Analyzer (SPAN) or network TAP. It receives a copy of traffic. If malware is spotted, it generates an alert (syslog, email) and sends TCP Reset (RST) packets. Cannot stop the initial malicious packet.\n"
                    "2. **IPS (Intrusion Prevention System)**: Deployed **Inline** directly in the network traffic path (all packets must physically pass through the IPS). If an exploit is detected, the IPS drops the malicious packets in real time before reaching the destination."
                )
            },
            {
                "heading": "Detection Methodologies: Signatures vs Anomalies",
                "content": (
                    "- **Signature-Based**: Matches packets against a database of known exploit byte sequences (Snort/Suricata rules). Ultra-fast, low false positives, but completely blind to brand-new zero-days.\n"
                    "- **Anomaly / Heuristic-Based**: Establishes a baseline of normal traffic behavior (e.g., standard bandwidth, normal port usage). Flags any statistically abnormal deviations (e.g., a workstation suddenly sending 10 GB of data to an IP in Russia at 3:00 AM)."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Writing a Snort / Suricata IDS/IPS Detection Rule",
                "language": "bash",
                "code": (
                    "# Snort Rule format:\n"
                    "# action proto src_ip src_port -> dst_ip dst_port (rule_options)\n"
                    "alert tcp any any -> $HOME_NET 80 (\n"
                    "    msg:\"ATTACK [SQLi] - Classic 'or 1=1' Attempt\";\n"
                    "    content:\"or+1%3D1\"; nocase;\n"
                    "    sid:1000001;\n"
                    "    rev:1;\n"
                    ")"
                ),
                "explanation": "Snort signatures inspect packet payloads for specific hexadecimal or ASCII exploit patterns."
            },
            {
                "title": "Python: Simulating an Inline IPS Packet Dropper",
                "language": "python",
                "code": (
                    "class NetworkIPS:\n"
                    "    def __init__(self):\n"
                    "        # Known exploit signatures\n"
                    "        self.signatures = ['/etc/passwd', 'cmd.exe', 'UNION SELECT']\n"
                    "    \n"
                    "    def process_packet_inline(self, packet_payload: str) -> str:\n"
                    "        for sig in self.signatures:\n"
                    "            if sig.lower() in packet_payload.lower():\n"
                    "                # IPS DROPS packet and terminates connection\n"
                    "                return f'IPS_ACTION: PACKET_DROPPED (Matched Signature: {sig})'\n"
                    "        return 'IPS_ACTION: PACKET_FORWARDED'\n\n"
                    "ips = NetworkIPS()\n"
                    "print(ips.process_packet_inline('GET /index.html HTTP/1.1'))\n"
                    "print(ips.process_packet_inline('GET /view?file=../../etc/passwd HTTP/1.1'))"
                ),
                "explanation": "Inline IPS evaluates packets before forwarding them, dropping malicious traffic before it reaches target servers."
            }
        ],
        coding_challenge={
            "description": "Write a Python function `ips_inspect(payload: str, known_signatures: list) -> dict` that returns a dict `{'status': 'FORWARDED' or 'DROPPED', 'matched_rule': str or None}`. Drop if any signature is found in payload (case-insensitive).",
            "starter_code": (
                "def ips_inspect(payload: str, known_signatures: list) -> dict:\n"
                "    # Return {'status': 'FORWARDED' or 'DROPPED', 'matched_rule': str/None}\n"
                "    return {}\n\n"
                "sigs = ['malicious_payload', 'bash_reverse_shell']\n"
                "print(ips_inspect('GET /home HTTP/1.1', sigs))\n"
                "print(ips_inspect('POST /api data=bash_reverse_shell', sigs))"
            ),
            "solution_code": (
                "def ips_inspect(payload: str, known_signatures: list) -> dict:\n"
                "    clean = payload.lower()\n"
                "    for sig in known_signatures:\n"
                "        if sig.lower() in clean:\n"
                "            return {'status': 'DROPPED', 'matched_rule': sig}\n"
                "    return {'status': 'FORWARDED', 'matched_rule': None}\n\n"
                "sigs = ['malicious_payload', 'bash_reverse_shell']\n"
                "print(ips_inspect('GET /home HTTP/1.1', sigs))\n"
                "print(ips_inspect('POST /api data=bash_reverse_shell', sigs))"
            ),
            "expected_output": "{'status': 'FORWARDED', 'matched_rule': None}\n{'status': 'DROPPED', 'matched_rule': 'bash_reverse_shell'}"
        },
        quizzes=[
            {
                "question": "What is the critical deployment difference between an IDS and an IPS?",
                "options": [
                    "An IDS is deployed passively out-of-band to monitor and alert, while an IPS is deployed inline directly in the traffic flow to actively block attacks",
                    "An IDS is for Windows, while an IPS is for macOS",
                    "An IDS runs without computer hardware",
                    "An IPS can only inspect Wi-Fi networks"
                ],
                "correct_answer": "An IDS is deployed passively out-of-band to monitor and alert, while an IPS is deployed inline directly in the traffic flow to actively block attacks",
                "explanation": "IDS detects and alerts on traffic copies (passive); IPS sits inline on the physical wire and drops malicious packets in real time."
            },
            {
                "question": "What is the main limitation of Signature-Based detection systems in modern cybersecurity?",
                "options": [
                    "They cannot detect zero-day exploits or newly modified malware whose signatures are not yet in the database",
                    "They produce too many false alarms on known viruses",
                    "They take days to inspect a single network packet",
                    "They require dial-up internet connections"
                ],
                "correct_answer": "They cannot detect zero-day exploits or newly modified malware whose signatures are not yet in the database",
                "explanation": "Signature detection requires prior knowledge of the attack pattern. An attacker with a novel zero-day will bypass signature filters."
            },
            {
                "question": "What is a 'False Positive' in the context of an Intrusion Detection System?",
                "options": [
                    "The system generates a security alert on legitimate, harmless user traffic",
                    "An actual attack occurred but the system failed to detect it",
                    "The server crashed due to a power outage",
                    "A user forgot their password"
                ],
                "correct_answer": "The system generates a security alert on legitimate, harmless user traffic",
                "explanation": "A False Positive is a false alarm: benign traffic triggers an alert, wasting analyst triage time."
            },
            {
                "question": "Which detection methodology establishes a statistical baseline of normal network behavior and flags abnormal deviations?",
                "options": ["Anomaly / Heuristic-Based Detection", "Signature-Based Detection", "Static String Matching", "CRC32 Checksumming"],
                "correct_answer": "Anomaly / Heuristic-Based Detection",
                "explanation": "Anomaly detection models normal traffic metrics and generates alerts when unusual spikes or unseen behaviors emerge."
            },
            {
                "question": "What network switch feature is used to send a mirrored copy of all network traffic to a passive IDS sensor?",
                "options": ["SPAN (Port Mirroring)", "Spanning Tree Protocol", "Trunk Port VLAN Tagging", "DHCP Snooping"],
                "correct_answer": "SPAN (Port Mirroring)",
                "explanation": "Switch Port Analyzer (SPAN) mirrors traffic from designated switch ports to a monitoring port connected to the IDS sensor."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 33: VPNs (Virtual Private Networks) and IPsec
    # ---------------------------------------------------------
    DayBlueprint(
        order=33,
        title="Day 33: VPNs (Virtual Private Networks) and IPsec",
        concept="Understanding encrypted network tunnels: Site-to-Site vs Remote Access VPNs, IPsec architecture (AH vs ESP, Tunnel mode vs Transport mode), and modern TLS/SSL VPNs (OpenVPN, WireGuard).",
        analogy="Using the public internet without a VPN is like driving an open-air convertible along a public highway where every bystander can look inside and photograph what you are carrying. A VPN is building a private underground bulletproof tunnel straight from your garage directly into the corporate headquarters vault.",
        theory_sections=[
            {
                "heading": "VPN Topologies: Remote Access vs Site-to-Site",
                "content": (
                    "Virtual Private Networks create encrypted tunnels over untrusted networks (the public internet):\n\n"
                    "1. **Remote Access VPN**: Connects individual remote workers to the corporate network via VPN client software (Cisco AnyConnect, OpenVPN, WireGuard).\n"
                    "2. **Site-to-Site VPN**: Interconnects two entire geographically separated branch office networks across the internet. Handled automatically by routers or firewalls without individual desktop client software."
                )
            },
            {
                "heading": "The IPsec Protocol Suite Architecture",
                "content": (
                    "IPsec operates at Layer 3 (Network Layer) to secure IP communications:\n"
                    "- **AH (Authentication Header - IP Protocol 51)**: Provides integrity and authentication, but **NO ENCRYPTION** (data remains visible in cleartext!). Rarely used alone.\n"
                    "- **ESP (Encapsulating Security Payload - IP Protocol 50)**: Provides **CONFIDENTIALITY (ENCRYPTION)**, integrity, and anti-replay protection.\n"
                    "- **Transport Mode**: Only the payload is encrypted; original IP headers remain exposed. Used for direct host-to-host links.\n"
                    "- **Tunnel Mode**: The ENTIRE original IP packet (header and payload) is encrypted and wrapped inside a brand-new outer IP header. Standard for site-to-site VPNs."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Inspecting Active WireGuard and OpenVPN Tunnel Interfaces",
                "language": "bash",
                "code": (
                    "# Linux WireGuard VPN interface status and cryptographic handshakes:\n"
                    "sudo wg show\n"
                    "# Output: interface: wg0, public key: ..., latest handshake: 1 minute ago, transfer: 50MB\n\n"
                    "# Verifying default routing goes through the VPN tunnel (tun0 / wg0):\n"
                    "ip route show | grep -E 'tun|wg'"
                ),
                "explanation": "Sysadmins verify that all default egress traffic routes across the virtual tunnel adapter rather than the local gateway."
            },
            {
                "title": "Python: Simulating VPN Packet Tunnel Encapsulation",
                "language": "python",
                "code": (
                    "def ipsec_tunnel_encapsulate(original_ip_packet: dict, vpn_gateway_ip: str) -> dict:\n"
                    "    # In Tunnel Mode, the entire original packet is encrypted and nested\n"
                    "    ciphertext_payload = f\"ENCRYPTED_ESP_DATA[{original_ip_packet}]\"\n"
                    "    outer_packet = {\n"
                    "        'src_ip': '198.51.100.1',           # Local VPN Appliance Public IP\n"
                    "        'dst_ip': vpn_gateway_ip,            # Remote Corporate Gateway Public IP\n"
                    "        'protocol': 'ESP (50)',\n"
                    "        'payload': ciphertext_payload\n"
                    "    }\n"
                    "    return outer_packet\n\n"
                    "inner = {'src': '10.0.1.5', 'dst': '10.0.2.80', 'data': 'confidential_finance.xlsx'}\n"
                    "print(ipsec_tunnel_encapsulate(inner, '203.0.113.1'))"
                ),
                "explanation": "Demonstrates IPsec tunnel mode where private internal IP addresses are completely hidden inside an outer routable packet."
            }
        ],
        coding_challenge={
            "description": "Write a Python function `evaluate_ipsec_security(protocol: str, mode: str) -> dict` that evaluates whether confidentiality (encryption) is provided. Protocol 'ESP' provides encryption; 'AH' does NOT provide encryption. Return dict `{'protocol': protocol, 'mode': mode, 'encryption_enabled': bool}`.",
            "starter_code": (
                "def evaluate_ipsec_security(protocol: str, mode: str) -> dict:\n"
                "    # Return {'protocol': protocol, 'mode': mode, 'encryption_enabled': True/False}\n"
                "    return {}\n\n"
                "print(evaluate_ipsec_security('ESP', 'Tunnel'))\n"
                "print(evaluate_ipsec_security('AH', 'Transport'))"
            ),
            "solution_code": (
                "def evaluate_ipsec_security(protocol: str, mode: str) -> dict:\n"
                "    p_clean = protocol.upper()\n"
                "    has_encryption = (p_clean == 'ESP')\n"
                "    return {\n"
                "        'protocol': p_clean,\n"
                "        'mode': mode.capitalize(),\n"
                "        'encryption_enabled': has_encryption\n"
                "    }\n\n"
                "print(evaluate_ipsec_security('ESP', 'Tunnel'))\n"
                "print(evaluate_ipsec_security('AH', 'Transport'))"
            ),
            "expected_output": "{'protocol': 'ESP', 'mode': 'Tunnel', 'encryption_enabled': True}\n{'protocol': 'AH', 'mode': 'Transport', 'encryption_enabled': False}"
        },
        quizzes=[
            {
                "question": "Which protocol within the IPsec suite is responsible for providing data confidentiality through encryption?",
                "options": ["ESP (Encapsulating Security Payload)", "AH (Authentication Header)", "ICMP", "ARP"],
                "correct_answer": "ESP (Encapsulating Security Payload)",
                "explanation": "ESP encrypts the payload to provide confidentiality. AH only provides integrity and authentication without encrypting data."
            },
            {
                "question": "What is the difference between IPsec 'Transport Mode' and 'Tunnel Mode'?",
                "options": [
                    "Transport mode encrypts only the payload, leaving original IP headers visible; Tunnel mode encrypts the ENTIRE original packet inside a brand-new IP header",
                    "Transport mode is for airplanes; Tunnel mode is for trains",
                    "Tunnel mode does not use encryption",
                    "Transport mode is only supported on mobile phones"
                ],
                "correct_answer": "Transport mode encrypts only the payload, leaving original IP headers visible; Tunnel mode encrypts the ENTIRE original packet inside a brand-new IP header",
                "explanation": "Tunnel mode wraps the original packet (including private internal headers) inside an outer header, shielding network topology."
            },
            {
                "question": "What type of VPN connection permanently links two separate branch offices across the public internet without requiring individual software on user laptops?",
                "options": ["Site-to-Site VPN", "Remote Access VPN", "Dial-Up VPN", "Point-to-Point Bluetooth"],
                "correct_answer": "Site-to-Site VPN",
                "explanation": "Site-to-site VPNs connect two network gateways (routers/firewalls), transparently routing traffic between corporate subnets."
            },
            {
                "question": "Why is using a public Wi-Fi network at an airport or coffee shop dangerous without a VPN?",
                "options": [
                    "Attackers on the same unencrypted Wi-Fi network can capture unencrypted packets, perform ARP poisoning, or launch Evil Twin attacks",
                    "Airport Wi-Fi burns out the laptop battery",
                    "Coffee shop routers delete all Word documents",
                    "Laptops automatically download viruses from airplanes"
                ],
                "correct_answer": "Attackers on the same unencrypted Wi-Fi network can capture unencrypted packets, perform ARP poisoning, or launch Evil Twin attacks",
                "explanation": "Open Wi-Fi lacks peer isolation. A VPN wraps all endpoint traffic in an encrypted tunnel, rendering sniffed frames unreadable."
            },
            {
                "question": "Which modern, lightweight open-source VPN protocol has gained massive adoption due to its small codebase (~4,000 lines of code) and state-of-the-art cryptography?",
                "options": ["WireGuard", "PPTP", "Telnet", "FTP"],
                "correct_answer": "WireGuard",
                "explanation": "WireGuard uses modern cryptography (ChaCha20, Curve25519) with a radically smaller codebase than legacy IPsec or OpenVPN, dramatically reducing attack surface."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 34: Wi-Fi Security Protocols (WEP, WPA, WPA2, WPA3)
    # ---------------------------------------------------------
    DayBlueprint(
        order=34,
        title="Day 34: Wi-Fi Security Protocols (WEP, WPA, WPA2, WPA3)",
        concept="Tracing the evolution of wireless encryption: WEP (broken RC4), WPA (TKIP band-aid), WPA2 (AES-CCMP, 4-way handshake, KRACK vulnerability), and WPA3 (SAE Dragonfly handshake, Protected Management Frames).",
        analogy="Think of wireless deadbolts: WEP was a paper padlock that anyone could pick with a paperclip in 60 seconds. WPA was a slightly thicker cardboard lock. WPA2 was a heavy steel padlock, but if someone recorded you locking it (4-way handshake), they could take that recording home and guess combinations offline. WPA3 is a biometric titanium vault with an anti-tamper lock that resists offline guessing.",
        theory_sections=[
            {
                "heading": "The Evolution of Wi-Fi Encryption Standards",
                "content": (
                    "Wireless 802.11 transmissions broadcast across open air, requiring cryptographic shielding:\n\n"
                    "1. **WEP (Wired Equivalent Privacy - 1999)**: Uses RC4 stream cipher with a tiny 24-bit **Initialization Vector (IV)**. IVs collide and repeat after capturing a few thousand packets. Can be cracked in under 2 minutes. Completely obsolete.\n"
                    "2. **WPA (Wi-Fi Protected Access - 2003)**: Interim fix using **TKIP (Temporal Key Integrity Protocol)**. Dynamically rotates keys per packet, but still relies on vulnerable RC4.\n"
                    "3. **WPA2 (802.11i - 2004)**: Mandatory **AES-CCMP** encryption. Standard for two decades. Pre-Shared Key (PSK) mode uses a **4-Way Handshake**; attackers capture the handshake and crack the password offline using dictionary attacks. Vulnerable to **KRACK (Key Reinstallation Attack)**.\n"
                    "4. **WPA3 (2018)**: Replaces PSK with **SAE (Simultaneous Authentication of Equals)** using the Dragonfly handshake. Provides **Forward Secrecy**, rendering offline dictionary attacks mathematically impossible. Mandates 192-bit encryption for Enterprise and Protected Management Frames (PMF) to block deauthentication attacks."
                )
            },
            {
                "heading": "Deauthentication Attacks",
                "content": (
                    "In WPA2, Layer 2 management frames are unencrypted. Attackers spoof the AP's MAC address and broadcast **Deauth packets**, instantly kicking victims off the Wi-Fi network to capture their 4-way handshake when they reconnect. WPA3 mandates **PMF (802.11w)**, preventing rogue deauth frames."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Auditing Wi-Fi Encryption Protocols via Command Line",
                "language": "bash",
                "code": (
                    "# Windows PowerShell command to inspect local Wi-Fi encryption:\n"
                    "netsh wlan show interfaces\n"
                    "# Expected Output: Authentication: WPA3-Personal | Cipher: CCMP\n\n"
                    "# Linux Aircrack-ng suite monitoring wireless frames (Ethical Lab):\n"
                    "sudo airodump-ng wlan0mon\n"
                    "# Shows BSSID, Channel, Encryption (WEP, WPA2, WPA3), and ESSID"
                ),
                "explanation": "Security assessments verify that corporate wireless networks do not support legacy WEP or TKIP fallbacks."
            },
            {
                "title": "Python: Classifying Wi-Fi Protocol Security Strength",
                "language": "python",
                "code": (
                    "def audit_wifi_security(protocol: str) -> dict:\n"
                    "    p = protocol.upper()\n"
                    "    ratings = {\n"
                    "        'WEP': ('BROKEN / INSECURE', 'Cracked in minutes via IV collisions', False),\n"
                    "        'WPA': ('DEPRECATED', 'Uses vulnerable TKIP stream cipher', False),\n"
                    "        'WPA2': ('ACCEPTABLE', 'Vulnerable to 4-way handshake capture & offline cracking', True),\n"
                    "        'WPA3': ('EXCELLENT', 'Uses SAE Dragonfly handshake with Forward Secrecy', True)\n"
                    "    }\n"
                    "    status, desc, is_approved = ratings.get(p, ('UNKNOWN', 'Invalid protocol', False))\n"
                    "    return {'protocol': p, 'status': status, 'analysis': desc, 'approved': is_approved}\n\n"
                    "print(audit_wifi_security('WEP'))\n"
                    "print(audit_wifi_security('WPA3'))"
                ),
                "explanation": "Triage logic used in automated compliance scanners to flag legacy wireless configurations."
            }
        ],
        coding_challenge={
            "description": "Write a Python function `is_wifi_secure(protocol: str, cipher: str) -> bool` that returns True only if protocol is 'WPA3' or ('WPA2' with cipher 'AES'/'CCMP'). Return False for 'WEP', 'TKIP', or any other combination.",
            "starter_code": (
                "def is_wifi_secure(protocol: str, cipher: str) -> bool:\n"
                "    # Return True if secure, False otherwise\n"
                "    return False\n\n"
                "print(is_wifi_secure('WPA3', 'AES'))\n"
                "print(is_wifi_secure('WPA2', 'CCMP'))\n"
                "print(is_wifi_secure('WPA2', 'TKIP'))\n"
                "print(is_wifi_secure('WEP', 'RC4'))"
            ),
            "solution_code": (
                "def is_wifi_secure(protocol: str, cipher: str) -> bool:\n"
                "    p = protocol.upper()\n"
                "    c = cipher.upper()\n"
                "    if p == 'WPA3':\n"
                "        return True\n"
                "    if p == 'WPA2' and c in ['AES', 'CCMP']:\n"
                "        return True\n"
                "    return False\n\n"
                "print(is_wifi_secure('WPA3', 'AES'))\n"
                "print(is_wifi_secure('WPA2', 'CCMP'))\n"
                "print(is_wifi_secure('WPA2', 'TKIP'))\n"
                "print(is_wifi_secure('WEP', 'RC4'))"
            ),
            "expected_output": "True\nTrue\nFalse\nFalse"
        },
        quizzes=[
            {
                "question": "Why is WEP (Wired Equivalent Privacy) considered completely broken and unsafe to use?",
                "options": [
                    "It uses a weak 24-bit Initialization Vector (IV) with the RC4 cipher, causing key reuse that allows attackers to crack the password in minutes",
                    "WEP only works on desktop computers",
                    "WEP was invented by cybercriminals",
                    "WEP shuts down internet access after 100 megabytes"
                ],
                "correct_answer": "It uses a weak 24-bit Initialization Vector (IV) with the RC4 cipher, causing key reuse that allows attackers to crack the password in minutes",
                "explanation": "WEP's short 24-bit IV results in frequent key collisions. Capturing sufficient IV traffic allows instant key derivation."
            },
            {
                "question": "Which robust symmetric encryption algorithm is utilized by the WPA2 wireless standard?",
                "options": ["AES (Advanced Encryption Standard) with CCMP", "RC4", "DES", "MD5"],
                "correct_answer": "AES (Advanced Encryption Standard) with CCMP",
                "explanation": "WPA2 mandated the replacement of legacy RC4 with military-grade AES encryption operating in CCMP mode."
            },
            {
                "question": "What major vulnerability in WPA2-Personal (PSK) networks allows attackers to crack passwords offline without actively connecting to the router?",
                "options": [
                    "Capturing the 4-Way Handshake frames transmitted when a client connects to the AP, then brute-forcing the hash offline using dictionaries",
                    "Unplugging the router power cord",
                    "Looking at the router's plastic antenna",
                    "Changing the computer screen resolution"
                ],
                "correct_answer": "Capturing the 4-Way Handshake frames transmitted when a client connects to the AP, then brute-forcing the hash offline using dictionaries",
                "explanation": "In WPA2-PSK, an attacker sniffs the 4-way handshake exchange and uses GPU clusters to test billions of dictionary passwords offline."
            },
            {
                "question": "What key cryptographic mechanism does WPA3 introduce to eliminate offline dictionary attacks and provide Forward Secrecy?",
                "options": ["SAE (Simultaneous Authentication of Equals) Dragonfly Handshake", "TKIP", "Cleartext HTTP", "Static WEP Keys"],
                "correct_answer": "SAE (Simultaneous Authentication of Equals) Dragonfly Handshake",
                "explanation": "WPA3 uses the SAE Dragonfly handshake: even if an attacker captures the wireless handshake, offline dictionary guessing is mathematically prevented."
            },
            {
                "question": "What is a 'Deauthentication Attack' on an unhardened WPA2 Wi-Fi network?",
                "options": [
                    "Spoofing the router's MAC address and sending fake disconnect frames to forcefully disconnect a victim, capturing their handshake upon reconnection",
                    "Calling the internet service provider to cancel the account",
                    "Physically cutting the Ethernet cables",
                    "Resetting the router to factory settings"
                ],
                "correct_answer": "Spoofing the router's MAC address and sending fake disconnect frames to forcefully disconnect a victim, capturing their handshake upon reconnection",
                "explanation": "Because 802.11 management frames were unencrypted in WPA2, attackers send spoofed deauth frames to force handshakes for cracking."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 35: Network Segmentation & DMZ (Demilitarized Zone)
    # ---------------------------------------------------------
    DayBlueprint(
        order=35,
        title="Day 35: Network Segmentation & DMZ (Demilitarized Zone)",
        concept="Mastering enterprise network architecture: VLANs (Virtual LANs), Subnetting, DMZs (Demilitarized Zones), Micro-segmentation, and Zero-Trust lateral movement prevention.",
        analogy="Think of a cruise ship: If the ship's hull was one single open hollow room, a single rock tear would flood the whole vessel and sink it. Instead, naval engineers build watertight steel bulkheads (VLANs & Firewalls) dividing the hull into 20 sealed compartments. If Compartment 3 floods, the watertight doors seal it off, and the ship stays afloat.",
        theory_sections=[
            {
                "heading": "Network Segmentation & VLANs",
                "content": (
                    "Placing all corporate devices (receptionists, finance, IoT printers, guest smartphones, domain controllers) on a single flat network is disastrous:\n\n"
                    "1. **Flat Network Hazard**: If a guest phone or printer is infected, malware uses ARP scanning to discover and compromise domain servers within seconds.\n"
                    "2. **VLANs (Virtual LANs - 802.1Q)**: Logical Layer 2 boundaries created inside network switches. Traffic between VLANs CANNOT pass without going through a Layer 3 firewall.\n"
                    "3. **Micro-segmentation**: Cloud security model where security policies are applied down to individual workloads/containers (e.g., Database container only accepts traffic from Backend App container on port 5432)."
                )
            },
            {
                "heading": "The DMZ (Demilitarized Zone) Architecture",
                "content": (
                    "A **DMZ** is a physical or logical buffer subnetwork that exposes external-facing public services (Web servers, DNS servers, Email relays) to the untrusted internet:\n"
                    "- Internet clients can talk to the DMZ.\n"
                    "- DMZ servers **CANNOT initiate connections into the private internal corporate network**.\n"
                    "- If an attacker exploits a zero-day on the public web server, they are trapped inside the DMZ and cannot access the internal database holding credit cards."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Cisco Switch VLAN Configuration & Routing Boundary",
                "language": "bash",
                "code": (
                    "# Cisco IOS Switch VLAN Segmentation:\n"
                    "Switch(config)# vlan 10\n"
                    "Switch(config-vlan)# name CORPORATE_WORKSTATIONS\n"
                    "Switch(config)# vlan 20\n"
                    "Switch(config-vlan)# name IOT_CAMERAS_PRINTERS\n"
                    "Switch(config)# vlan 30\n"
                    "Switch(config-vlan)# name PUBLIC_DMZ_SERVERS\n\n"
                    "# Assigning physical switch port 1 to VLAN 20:\n"
                    "Switch(config)# interface gigabitethernet 0/1\n"
                    "Switch(config-if)# switchport mode access\n"
                    "Switch(config-if)# switchport access vlan 20"
                ),
                "explanation": "Isolating untrusted IoT hardware on VLAN 20 prevents infected printers from sniffing corporate workstation frames."
            },
            {
                "title": "Python: Simulating DMZ Firewall Traffic Enforcement",
                "language": "python",
                "code": (
                    "def dmz_firewall_rule(src_zone: str, dst_zone: str, port: int) -> str:\n"
                    "    # INTERNET -> DMZ (Allowed for public web port 443)\n"
                    "    if src_zone == 'INTERNET' and dst_zone == 'DMZ' and port == 443:\n"
                    "        return 'ALLOW_PUBLIC_WEB'\n"
                    "    \n"
                    "    # DMZ -> INTERNAL_LAN (STRICTLY FORBIDDEN to prevent pivot attacks!)\n"
                    "    if src_zone == 'DMZ' and dst_zone == 'INTERNAL_LAN':\n"
                    "        return 'CRITICAL_BLOCK: DMZ cannot initiate connection into Internal LAN!'\n"
                    "        \n"
                    "    # INTERNAL_LAN -> DMZ (Allowed for database updates)\n"
                    "    if src_zone == 'INTERNAL_LAN' and dst_zone == 'DMZ':\n"
                    "        return 'ALLOW_INTERNAL_MANAGEMENT'\n"
                    "    return 'BLOCK_DEFAULT'\n\n"
                    "print(dmz_firewall_rule('INTERNET', 'DMZ', 443))\n"
                    "print(dmz_firewall_rule('DMZ', 'INTERNAL_LAN', 1433))"
                ),
                "explanation": "Illustrates DMZ boundary isolation preventing compromised internet-facing servers from pivoting into internal network assets."
            }
        ],
        coding_challenge={
            "description": "Write a Python function `check_lateral_movement(src_vlan: int, dst_vlan: int, is_firewall_rule_present: bool) -> str` that returns 'PERMITTED' if src_vlan == dst_vlan or is_firewall_rule_present is True, and 'BLOCKED (Isolated VLAN)' otherwise.",
            "starter_code": (
                "def check_lateral_movement(src_vlan: int, dst_vlan: int, is_firewall_rule_present: bool) -> str:\n"
                "    # Return 'PERMITTED' or 'BLOCKED (Isolated VLAN)'\n"
                "    return ''\n\n"
                "print(check_lateral_movement(10, 10, False))\n"
                "print(check_lateral_movement(10, 20, False))\n"
                "print(check_lateral_movement(10, 20, True))"
            ),
            "solution_code": (
                "def check_lateral_movement(src_vlan: int, dst_vlan: int, is_firewall_rule_present: bool) -> str:\n"
                "    if src_vlan == dst_vlan:\n"
                "        return 'PERMITTED'\n"
                "    if is_firewall_rule_present:\n"
                "        return 'PERMITTED'\n"
                "    return 'BLOCKED (Isolated VLAN)'\n\n"
                "print(check_lateral_movement(10, 10, False))\n"
                "print(check_lateral_movement(10, 20, False))\n"
                "print(check_lateral_movement(10, 20, True))"
            ),
            "expected_output": "PERMITTED\nBLOCKED (Isolated VLAN)\nPERMITTED"
        },
        quizzes=[
            {
                "question": "What is the primary security goal of a Demilitarized Zone (DMZ) in enterprise network design?",
                "options": [
                    "To isolate publicly accessible servers (like web and email) in a perimeter buffer network so that if compromised, the attacker cannot easily pivot into the internal network",
                    "To provide free Wi-Fi to military personnel",
                    "To turn off all firewalls on holidays",
                    "To double the download speed of video files"
                ],
                "correct_answer": "To isolate publicly accessible servers (like web and email) in a perimeter buffer network so that if compromised, the attacker cannot easily pivot into the internal network",
                "explanation": "DMZs host public services in an isolated zone. Strict firewall rules prevent DMZ servers from initiating inbound sessions into internal LANs."
            },
            {
                "question": "What is a 'Flat Network' and why is it considered a major cybersecurity risk?",
                "options": [
                    "A network where all devices share a single broadcast domain without segmentation; if any single device is infected, malware can easily spread laterally to all others",
                    "A network running on flat fiber optic cables",
                    "A network that has run out of IP addresses",
                    "A website that has no 3D graphics"
                ],
                "correct_answer": "A network where all devices share a single broadcast domain without segmentation; if any single device is infected, malware can easily spread laterally to all others",
                "explanation": "Flat networks lack internal barriers. A compromised guest laptop or IoT thermostat can freely attack internal payroll servers."
            },
            {
                "question": "What network technology logically divides a physical network switch into separate, isolated broadcast domains at Layer 2?",
                "options": ["VLAN (Virtual Local Area Network - 802.1Q)", "NAT", "DNS", "BGP"],
                "correct_answer": "VLAN (Virtual Local Area Network - 802.1Q)",
                "explanation": "VLANs partition physical switch hardware into distinct logical networks. Traffic cannot jump between VLANs without routing through a firewall."
            },
            {
                "question": "What is 'Lateral Movement' in cyber attack lifecycle terminology?",
                "options": [
                    "The techniques an attacker uses to progressively navigate through a network from an initial compromised endpoint to other high-value target systems",
                    "Typing on a keyboard with your left hand",
                    "Moving servers from one physical rack to another",
                    "A mouse moving sideways across the desk"
                ],
                "correct_answer": "The techniques an attacker uses to progressively navigate through a network from an initial compromised endpoint to other high-value target systems",
                "explanation": "After gaining initial entry, adversaries probe internal networks and pivot laterally toward domain controllers and databases."
            },
            {
                "question": "What is 'Micro-segmentation' in cloud and zero-trust environments?",
                "options": [
                    "Enforcing granular security policies and isolation rules directly at the individual workload, virtual machine, or container level",
                    "Cutting network cables into very short pieces",
                    "Using tiny microchip routers",
                    "Dividing passwords into 2-letter chunks"
                ],
                "correct_answer": "Enforcing granular security policies and isolation rules directly at the individual workload, virtual machine, or container level",
                "explanation": "Micro-segmentation creates individual micro-perimeters around workloads, preventing lateral movement even between servers in the same subnet."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 36: Honeypots and Honeynets
    # ---------------------------------------------------------
    DayBlueprint(
        order=36,
        title="Day 36: Honeypots and Honeynets",
        concept="Mastering active cyber deception: Low-interaction vs High-interaction Honeypots, Honeynets, Honeytokens (canary credentials), and adversary intelligence gathering.",
        analogy="A Honeypot is a counterfeit bank vault with unlocked glass doors placed deliberately in the middle of a city alleyway, filled with fake gold bars. It has no real money and zero legitimate business customers. Therefore, the second anyone opens the door or steps inside, an alarm bells ring—because there is 100% certainty that anyone touching it is an intruder.",
        theory_sections=[
            {
                "heading": "The Purpose of Honeypots & Deception Technology",
                "content": (
                    "A **Honeypot** is a decoy computer system explicitly configured to be attacked, probed, and compromised:\n\n"
                    "1. **Zero Legitimate Traffic**: Because the honeypot has no real business function, **any interaction is inherently malicious**, yielding zero false positives.\n"
                    "2. **Adversary Early Warning**: Alerts the SOC the instant an attacker initiates internal reconnaissance.\n"
                    "3. **Threat Intelligence Gathering**: Researchers study attacker tactics, exploits, and toolkits in a controlled environment.\n"
                    "4. **Low-Interaction Honeypots**: Emulates specific services (e.g., fake SSH banner on port 22). Low risk, low resource usage, but cannot observe full exploit detonation.\n"
                    "5. **High-Interaction Honeypots**: Real operating systems and real databases heavily monitored and sandboxed. High intelligence value, but carries risk if the attacker attempts to pivot."
                )
            },
            {
                "heading": "Honeynets and Honeytokens (Canary Artifacts)",
                "content": (
                    "- **Honeynet**: An entire network of interconnected honeypots simulating a fake enterprise domain.\n"
                    "- **Honeytokens / Canary Tokens**: Fake credentials, fake API keys (e.g., dummy AWS access keys planted in GitHub repos), or bogus database records. If that canary key is ever used, alerts immediately reveal who stole it."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Deploying an Open-Source Cowrie SSH/Telnet Honeypot",
                "language": "bash",
                "code": (
                    "# Cowrie is a medium/high interaction SSH and Telnet honeypot:\n"
                    "# 1. Clone and launch via Docker container:\n"
                    "docker run -p 2222:2222 cowrie/cowrie\n\n"
                    "# 2. Inspecting live attacker login attempts logged as JSON:\n"
                    "tail -f cowrie/var/log/cowrie/cowrie.json | jq '{src_ip: .src_ip, user: .username, pass: .password}'"
                ),
                "explanation": "Honeypots log attacker credentials and downloaded malware samples directly into threat intelligence pipelines."
            },
            {
                "title": "Python: Building a Simple Port Trap Honeypot",
                "language": "python",
                "code": (
                    "import socket\n"
                    "import time\n\n"
                    "def run_honey_listener(trap_port: int):\n"
                    "    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)\n"
                    "    s.bind(('0.0.0.0', trap_port))\n"
                    "    s.listen(1)\n"
                    "    print(f'[*] Honeypot listening on trap port {trap_port}...')\n"
                    "    \n"
                    "    # Simulating connection trigger\n"
                    "    # In production, this runs in a loop logging attacker IPs\n"
                    "    # s.accept() -> Triggers critical SOC alert\n"
                    "    return 'HONEYPOT_ACTIVE'\n\n"
                    "print(run_honey_listener(23)) # Telnet trap"
                ),
                "explanation": "Trap listeners detect reconnaissance port sweeps across corporate subnets."
            }
        ],
        coding_challenge={
            "description": "Write a Python function `inspect_honeytoken(used_token: str, canary_tokens: set) -> dict` that returns `{'is_honeypot_triggered': True, 'alert_level': 'CRITICAL'}` if the token is in canary_tokens, otherwise `{'is_honeypot_triggered': False, 'alert_level': 'NONE'}`.",
            "starter_code": (
                "def inspect_honeytoken(used_token: str, canary_tokens: set) -> dict:\n"
                "    # Return alert dict\n"
                "    return {}\n\n"
                "canaries = {'AKIA_CANARY_FAKE_KEY_123', 'fake_admin_pass'}\n"
                "print(inspect_honeytoken('AKIA_CANARY_FAKE_KEY_123', canaries))\n"
                "print(inspect_honeytoken('LEGIT_PROD_KEY_456', canaries))"
            ),
            "solution_code": (
                "def inspect_honeytoken(used_token: str, canary_tokens: set) -> dict:\n"
                "    is_hit = used_token in canary_tokens\n"
                "    return {\n"
                "        'is_honeypot_triggered': is_hit,\n"
                "        'alert_level': 'CRITICAL' if is_hit else 'NONE'\n"
                "    }\n\n"
                "canaries = {'AKIA_CANARY_FAKE_KEY_123', 'fake_admin_pass'}\n"
                "print(inspect_honeytoken('AKIA_CANARY_FAKE_KEY_123', canaries))\n"
                "print(inspect_honeytoken('LEGIT_PROD_KEY_456', canaries))"
            ),
            "expected_output": "{'is_honeypot_triggered': True, 'alert_level': 'CRITICAL'}\n{'is_honeypot_triggered': False, 'alert_level': 'NONE'}"
        },
        quizzes=[
            {
                "question": "What is the primary purpose of deploying a 'Honeypot' in an enterprise network?",
                "options": [
                    "To serve as a decoy system designed to lure, detect, and study malicious activity without hosting any legitimate business data or traffic",
                    "To produce honey in the office kitchen",
                    "To store company customer backup databases",
                    "To boost wireless internet signals"
                ],
                "correct_answer": "To serve as a decoy system designed to lure, detect, and study malicious activity without hosting any legitimate business data or traffic",
                "explanation": "Honeypots act as traps: because no legitimate employee has a reason to contact them, any connection represents an attacker or malware."
            },
            {
                "question": "Why do alerts generated by honeypots have an exceptionally low False Positive rate?",
                "options": [
                    "Because honeypots have zero legitimate production users, meaning virtually any interaction is inherently unauthorized or malicious",
                    "Because honeypots are written in Python",
                    "Because honeypots cannot connect to routers",
                    "Because honeypots only operate during business hours"
                ],
                "correct_answer": "Because honeypots have zero legitimate production users, meaning virtually any interaction is inherently unauthorized or malicious",
                "explanation": "With no authorized users or scheduled tasks contacting the decoy, almost all alerts represent legitimate adversary activity."
            },
            {
                "question": "What is a 'Honeytoken' (or Canary Token)?",
                "options": [
                    "A bogus piece of data (such as a fake database record, fake password, or fake API key) planted deliberately to detect unauthorized data theft",
                    "A cryptocurrency coin given to employees",
                    "A physical gold medal awarded to programmers",
                    "A discount coupon for antivirus software"
                ],
                "correct_answer": "A bogus piece of data (such as a fake database record, fake password, or fake API key) planted deliberately to detect unauthorized data theft",
                "explanation": "Honeytokens are boobytrapped digital assets. If someone attempts to use a planted fake AWS key, automated alarms fire immediately."
            },
            {
                "question": "What is the main risk associated with deploying a High-Interaction Honeypot (a real, fully functional operating system)?",
                "options": [
                    "If not properly isolated and contained, an attacker could compromise the honeypot and use it as a launchpad to attack real internal production systems",
                    "It consumes too much paper",
                    "It makes coffee machines malfunction",
                    "It changes all computer desktop wallpapers"
                ],
                "correct_answer": "If not properly isolated and contained, an attacker could compromise the honeypot and use it as a launchpad to attack real internal production systems",
                "explanation": "High-interaction honeypots run real OS software; if containment controls fail, the attacker can use the decoy as an internal pivot point."
            },
            {
                "question": "What is a 'Honeynet'?",
                "options": [
                    "A network composed of multiple honeypots designed to simulate an entire corporate network environment",
                    "A fishing net made of fiber optic cables",
                    "A Wi-Fi network that only works on laptops",
                    "An internet connection provided by the city"
                ],
                "correct_answer": "A network composed of multiple honeypots designed to simulate an entire corporate network environment",
                "explanation": "A honeynet scales honeypots into a full decoy network with multiple servers, routers, and simulated workstations to observe complex attack chains."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 37: Proxy Servers
    # ---------------------------------------------------------
    DayBlueprint(
        order=37,
        title="Day 37: Proxy Servers",
        concept="Differentiating between Forward Proxies (client-side privacy, content filtering, caching) and Reverse Proxies (server-side load balancing, SSL termination, DDoS protection).",
        analogy="Think of intermediaries: A Forward Proxy is an attorney you hire to make purchases for you—the seller never knows your identity because your attorney speaks on your behalf. A Reverse Proxy is the grand reception desk of a skyscraper—visitors never wander into the CEO's office directly; the receptionist verifies credentials, balances elevator loads, and delivers packages to the right floor.",
        theory_sections=[
            {
                "heading": "Forward Proxy vs Reverse Proxy",
                "content": (
                    "Proxies act as intermediaries for network requests:\n\n"
                    "1. **Forward Proxy**: Sits in front of internal **clients** reaching out to the internet.\n"
                    "   - *Functions*: Hides client IP addresses, filters objectionable or malicious websites, caches frequently requested web assets to save bandwidth, and performs outbound SSL/TLS decryption inspection.\n"
                    "2. **Reverse Proxy**: Sits in front of internal **servers** receiving inbound traffic from the internet.\n"
                    "   - *Functions*: Conceals backend server IP addresses, provides **Load Balancing** across server pools, handles **SSL/TLS Termination** (decrypting HTTPS so backend servers focus purely on compute), and blocks web application attacks."
                )
            },
            {
                "heading": "Transparent vs Explicit Proxies",
                "content": (
                    "- **Explicit Proxy**: Client web browsers must be configured with the proxy's IP and port (or via a PAC auto-config file).\n"
                    "- **Transparent Proxy**: Operates at the network gateway without requiring any client-side software configuration. All outbound port 80/443 traffic is invisibly redirected into the proxy via router policy."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Reverse Proxy Configuration (NGINX Load Balancing & SSL Termination)",
                "language": "bash",
                "code": (
                    "# NGINX Reverse Proxy configuration block:\n"
                    "server {\n"
                    "    listen 443 ssl;\n"
                    "    server_name api.company.com;\n"
                    "    ssl_certificate /etc/ssl/cert.pem;\n"
                    "    ssl_certificate_key /etc/ssl/privkey.pem;\n\n"
                    "    location / {\n"
                    "        # Forward traffic to internal private server pool:\n"
                    "        proxy_pass http://internal_backend_servers;\n"
                    "        proxy_set_header X-Forwarded-For $remote_addr;\n"
                    "    }\n"
                    "}"
                ),
                "explanation": "The reverse proxy terminates HTTPS publicly and forwards requests to private internal cluster nodes."
            },
            {
                "title": "Python: Querying Web Resources Through a Forward Proxy",
                "language": "python",
                "code": (
                    "import requests\n\n"
                    "def fetch_via_proxy(target_url: str, proxy_url: str) -> dict:\n"
                    "    proxies = {'http': proxy_url, 'https': proxy_url}\n"
                    "    try:\n"
                    "        # Request exits via proxy IP rather than local machine IP\n"
                    "        r = requests.get(target_url, proxies=proxies, timeout=5)\n"
                    "        return {'status_code': r.status_code, 'proxied': True}\n"
                    "    except Exception as e:\n"
                    "        return {'error': str(e), 'proxied': False}\n\n"
                    "print(fetch_via_proxy('https://httpbin.org/ip', 'http://10.10.1.1:8080'))"
                ),
                "explanation": "Demonstrates programmatic routing of client traffic through an outbound enterprise forward proxy."
            }
        ],
        coding_challenge={
            "description": "Write a Python function `classify_proxy_role(protects: str) -> str` that returns 'FORWARD_PROXY' if protects == 'CLIENTS', 'REVERSE_PROXY' if protects == 'SERVERS', and 'UNKNOWN' otherwise.",
            "starter_code": (
                "def classify_proxy_role(protects: str) -> str:\n"
                "    # Return 'FORWARD_PROXY', 'REVERSE_PROXY', or 'UNKNOWN'\n"
                "    return ''\n\n"
                "print(classify_proxy_role('CLIENTS'))\n"
                "print(classify_proxy_role('SERVERS'))"
            ),
            "solution_code": (
                "def classify_proxy_role(protects: str) -> str:\n"
                "    p = protects.strip().upper()\n"
                "    if p == 'CLIENTS':\n"
                "        return 'FORWARD_PROXY'\n"
                "    if p == 'SERVERS':\n"
                "        return 'REVERSE_PROXY'\n"
                "    return 'UNKNOWN'\n\n"
                "print(classify_proxy_role('CLIENTS'))\n"
                "print(classify_proxy_role('SERVERS'))"
            ),
            "expected_output": "FORWARD_PROXY\nREVERSE_PROXY"
        },
        quizzes=[
            {
                "question": "What is the primary difference between a Forward Proxy and a Reverse Proxy?",
                "options": [
                    "A Forward Proxy protects internal clients reaching out to the internet, while a Reverse Proxy protects internal servers receiving traffic from the internet",
                    "A Forward Proxy is for sending emails; a Reverse Proxy is for reading documents",
                    "Reverse proxies only work in reverse alphabetical order",
                    "There is no difference; both are exact synonyms"
                ],
                "correct_answer": "A Forward Proxy protects internal clients reaching out to the internet, while a Reverse Proxy protects internal servers receiving traffic from the internet",
                "explanation": "Forward proxies manage outbound client traffic (anonymity, filtering); reverse proxies manage inbound server traffic (load balancing, SSL termination)."
            },
            {
                "question": "What is 'SSL/TLS Termination' on a Reverse Proxy?",
                "options": [
                    "The reverse proxy decrypts incoming HTTPS traffic at the perimeter, forwarding unencrypted HTTP requests to backend cluster servers to relieve their CPU load",
                    "Deleting all digital certificates from the web server",
                    "Canceling the company's domain name registration",
                    "Shutting down the web browser permanently"
                ],
                "correct_answer": "The reverse proxy decrypts incoming HTTPS traffic at the perimeter, forwarding unencrypted HTTP requests to backend cluster servers to relieve their CPU load",
                "explanation": "Offloading SSL/TLS decryption to the reverse proxy centralizes certificate management and frees backend servers from cryptographic overhead."
            },
            {
                "question": "Why do corporate enterprise networks force employee web browsers to connect through an outbound Forward Proxy?",
                "options": [
                    "To enforce URL filtering (blocking gambling or malware sites), inspect traffic for data loss (DLP), and cache web content to save bandwidth",
                    "To make videos play in slow motion",
                    "To charge employees per megabyte of data",
                    "To prevent keyboards from wearing out"
                ],
                "correct_answer": "To enforce URL filtering (blocking gambling or malware sites), inspect traffic for data loss (DLP), and cache web content to save bandwidth",
                "explanation": "Forward proxies provide visibility and control over outbound enterprise web traffic, stopping malware downloads and data exfiltration."
            },
            {
                "question": "What is a 'Transparent Proxy'?",
                "options": [
                    "A proxy that intercepts network traffic at the gateway without requiring any manual proxy configuration changes on client computers",
                    "A computer monitor made of transparent glass",
                    "A proxy server that publishes all passwords online",
                    "A software program that has no code"
                ],
                "correct_answer": "A proxy that intercepts network traffic at the gateway without requiring any manual proxy configuration changes on client computers",
                "explanation": "Transparent proxies invisibly divert client traffic using router redirect rules without end-user awareness or device configuration."
            },
            {
                "question": "Which HTTP header is typically added by a reverse proxy to inform backend servers of the true original client IP address?",
                "options": ["X-Forwarded-For", "Authorization", "User-Agent", "Set-Cookie"],
                "correct_answer": "X-Forwarded-For",
                "explanation": "Because backend servers see the reverse proxy's IP as the direct source, the proxy inserts the `X-Forwarded-For` header containing the client's original IP."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 38: Basics of Cryptography (Plaintext vs Ciphertext)
    # ---------------------------------------------------------
    DayBlueprint(
        order=38,
        title="Day 38: Basics of Cryptography (Plaintext vs Ciphertext)",
        concept="Mastering foundational cryptography: Plaintext (readable data), Ciphertext (encrypted scrambled data), Ciphers (mathematical algorithms), Keys (secret entropy), Kerckhoffs's Principle, and the Caesar cipher.",
        analogy="Think of locking a handwritten diary: The readable English words are **Plaintext**. The mechanical lock mechanism is the **Cipher** (the mathematical algorithm). The unique physical metal key is the **Key**. The scrambled, completely unreadable mess of ink inside is the **Ciphertext**. Anyone who finds the diary cannot read a word without having the matching metal key.",
        theory_sections=[
            {
                "heading": "Core Cryptographic Terminology",
                "content": (
                    "Cryptography transforms readable information into unreadable formats to ensure confidentiality and integrity:\n\n"
                    "1. **Plaintext (Cleartext)**: Unencrypted, human-readable data (e.g., `'Meet at noon'`, credit card numbers, passwords).\n"
                    "2. **Ciphertext**: Scrambled data produced by an encryption algorithm, appearing completely random and indecipherable without the decryption key.\n"
                    "3. **Cipher (Algorithm)**: The mathematical function or steps used to perform encryption and decryption (e.g., AES, RSA, Caesar substitution).\n"
                    "4. **Key**: A secret value (string of bits) that feeds into the cipher. The security of the ciphertext depends entirely on keeping the key secret.\n"
                    "5. **Cryptanalysis**: The art and science of analyzing and breaking cryptographic systems without knowing the key."
                )
            },
            {
                "heading": "Kerckhoffs's Principle: Security Through Obscurity is Dead",
                "content": (
                    "Formulated in the 19th century by Auguste Kerckhoffs:\n"
                    "*'A cryptosystem should be secure even if everything about the system, except the key, is public knowledge.'*\n"
                    "Never design a secret proprietary algorithm. Modern ciphers like AES-256 are completely open source and mathematically analyzed by the world's top mathematicians. True security rests entirely in the secrecy and entropy of the **Key**, not the algorithm."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Python: Demonstrating the Historic Caesar Substitution Cipher",
                "language": "python",
                "code": (
                    "def caesar_encrypt(plaintext: str, shift: int) -> str:\n"
                    "    ciphertext = []\n"
                    "    for char in plaintext:\n"
                    "        if char.isalpha():\n"
                    "            base = ord('A') if char.isupper() else ord('a')\n"
                    "            shifted = (ord(char) - base + shift) % 26 + base\n"
                    "            ciphertext.append(chr(shifted))\n"
                    "        else:\n"
                    "            ciphertext.append(char)\n"
                    "    return ''.join(ciphertext)\n\n"
                    "secret = 'ATTACK AT DAWN'\n"
                    "cipher = caesar_encrypt(secret, shift=3)\n"
                    "print(f'Plaintext:  {secret}')\n"
                    "print(f'Ciphertext: {cipher}') # 'DZZDFN DW GDZQ'"
                ),
                "explanation": "Illustrates how simple substitution transforms plaintext into ciphertext using a numerical key shift."
            },
            {
                "title": "Generating Cryptographically Secure Random Keys via Python",
                "language": "python",
                "code": (
                    "import secrets\n\n"
                    "# Generating high-entropy 256-bit (32 byte) encryption key:\n"
                    "aes_256_key = secrets.token_bytes(32)\n"
                    "hex_key = aes_256_key.hex()\n"
                    "print('Cryptographic Key (Hex):', hex_key)\n"
                    "print('Key Length in Bits:     ', len(aes_256_key) * 8)"
                ),
                "explanation": "Standard random libraries like `random.randint` are predictable; cryptographic security mandates OS entropy via `secrets`."
            }
        ],
        coding_challenge={
            "description": "Write a Python function `caesar_decrypt(ciphertext: str, shift: int) -> str` that reverses the Caesar cipher shift to recover the original plaintext string.",
            "starter_code": (
                "def caesar_decrypt(ciphertext: str, shift: int) -> str:\n"
                "    # Return original decrypted plaintext\n"
                "    return ''\n\n"
                "print(caesar_decrypt('DZZDFN DW GDZQ', 3))\n"
                "print(caesar_decrypt('KHOOR', 3))"
            ),
            "solution_code": (
                "def caesar_decrypt(ciphertext: str, shift: int) -> str:\n"
                "    plaintext = []\n"
                "    for char in ciphertext:\n"
                "        if char.isalpha():\n"
                "            base = ord('A') if char.isupper() else ord('a')\n"
                "            shifted = (ord(char) - base - shift) % 26 + base\n"
                "            plaintext.append(chr(shifted))\n"
                "        else:\n"
                "            plaintext.append(char)\n"
                "    return ''.join(plaintext)\n\n"
                "print(caesar_decrypt('DZZDFN DW GDZQ', 3))\n"
                "print(caesar_decrypt('KHOOR', 3))"
            ),
            "expected_output": "ATTACK AT DAWN\nHELLO"
        },
        quizzes=[
            {
                "question": "What is the term for original, readable, unencrypted information in cryptography?",
                "options": ["Plaintext (or Cleartext)", "Ciphertext", "Hash Digest", "Entropy"],
                "correct_answer": "Plaintext (or Cleartext)",
                "explanation": "Plaintext is raw, human-readable data before an encryption algorithm converts it into ciphertext."
            },
            {
                "question": "What is 'Ciphertext'?",
                "options": [
                    "The scrambled, unreadable output produced by an encryption algorithm that can only be deciphered with the matching key",
                    "A computer programming language",
                    "A font style in Microsoft Word",
                    "A deleted text file"
                ],
                "correct_answer": "The scrambled, unreadable output produced by an encryption algorithm that can only be deciphered with the matching key",
                "explanation": "Ciphertext is the encrypted result of running plaintext through a cipher with a secret key."
            },
            {
                "question": "What is 'Kerckhoffs's Principle' in cryptographic engineering?",
                "options": [
                    "A cryptographic system should be secure even if everything about the algorithm is publicly known, as long as the key remains secret",
                    "All encryption algorithms must be kept top secret from the public",
                    "Passwords must be changed every 3 days",
                    "Computers should never be connected to the internet"
                ],
                "correct_answer": "A cryptographic system should be secure even if everything about the algorithm is publicly known, as long as the key remains secret",
                "explanation": "Kerckhoffs established that security should rely solely on key secrecy, rejecting 'security through obscurity' of algorithms."
            },
            {
                "question": "Why is 'Security Through Obscurity' (keeping an algorithm secret rather than using tested public algorithms) considered poor security practice?",
                "options": [
                    "Proprietary secret algorithms almost always contain severe hidden mathematical flaws that attackers quickly discover through reverse engineering",
                    "Secret algorithms cost too much money to print",
                    "Secret algorithms are illegal under international copyright law",
                    "Secret algorithms cannot run on Intel CPUs"
                ],
                "correct_answer": "Proprietary secret algorithms almost always contain severe hidden mathematical flaws that attackers quickly discover through reverse engineering",
                "explanation": "Public algorithms like AES have withstood decades of global peer review; homegrown secret algorithms inevitably fail."
            },
            {
                "question": "In modern cryptography, what determines the ultimate strength and resistance of an encrypted message against brute-force attacks?",
                "options": [
                    "The length (entropy) and unpredictability of the secret cryptographic Key",
                    "The physical weight of the computer hard drive",
                    "Whether the computer is connected via Wi-Fi or Ethernet",
                    "The number of monitors on the desk"
                ],
                "correct_answer": "The length (entropy) and unpredictability of the secret cryptographic Key",
                "explanation": "Key size dictates brute-force complexity: an AES-256 key has 2^256 combinations, taking supercomputers billions of years to exhaust."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 39: Symmetric Encryption
    # ---------------------------------------------------------
    DayBlueprint(
        order=39,
        title="Day 39: Symmetric Encryption",
        concept="Mastering symmetric-key cryptography: Shared secret keys, Block ciphers vs Stream ciphers, DES/3DES legacy vulnerabilities, and the modern AES (Advanced Encryption Standard) gold standard.",
        analogy="Think of a locked metal toolbox: Symmetric encryption uses **one single physical key** to both lock AND unlock the toolbox. If Alice wants to send a secret tool to Bob, she locks the box with her key. But Bob can only open it if Alice also gives him a duplicate copy of that EXACT same key. The big challenge: how does Alice get the key to Bob safely without a thief stealing it in transit?",
        theory_sections=[
            {
                "heading": "Symmetric Encryption Mechanics",
                "content": (
                    "In symmetric cryptography, a **single shared secret key** is used for both encryption and decryption:\n"
                    "- **Extreme Speed**: Symmetric algorithms rely on rapid mathematical permutations and substitutions, making them 1,000x faster than asymmetric algorithms. Ideal for bulk data (hard drives, streaming video, database files).\n"
                    "- **Block Ciphers**: Encrypt data in fixed-size blocks (e.g., 128-bit chunks). Examples: AES, DES, Blowfish.\n"
                    "- **Stream Ciphers**: Encrypt data bit-by-bit or byte-by-byte continuously. Examples: RC4 (deprecated), ChaCha20."
                )
            },
            {
                "heading": "Evolution: From DES to AES",
                "content": (
                    "1. **DES (Data Encryption Standard - 1977)**: 56-bit key length. Obsolete; can be brute-forced in under 24 hours.\n"
                    "2. **3DES (Triple DES)**: Encrypts data with DES three times. Secure, but slow and being phased out.\n"
                    "3. **AES (Advanced Encryption Standard - 2001 / Rijndael)**: The global standard. Fixed block size of 128 bits with key lengths of **128, 192, or 256 bits**. Zero practical attacks exist against full AES-256."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Encrypting Files with OpenSSL AES-256-CBC via Terminal",
                "language": "bash",
                "code": (
                    "# Encrypting a confidential text document using AES-256 with a password:\n"
                    "openssl enc -aes-256-cbc -salt -in confidential.txt -out confidential.enc\n\n"
                    "# Decrypting the encrypted file back to plaintext:\n"
                    "openssl enc -d -aes-256-cbc -in confidential.enc -out decrypted.txt"
                ),
                "explanation": "Standard OpenSSL CLI commands used by system administrators to encrypt sensitive archives with AES-256."
            },
            {
                "title": "Python: Demonstrating Symmetric AES-GCM Encryption (Authenticated Encryption)",
                "language": "python",
                "code": (
                    "# Note: In production use the 'cryptography' library (AESGCM)\n"
                    "import secrets\n\n"
                    "def simulate_symmetric_key_exchange():\n"
                    "    # Shared secret key known to both Alice and Bob\n"
                    "    shared_key = secrets.token_bytes(32)  # 256 bits\n"
                    "    print(f'Shared Secret Key: {shared_key.hex()[:16]}... (Must be kept secret!)')\n"
                    "    return shared_key\n\n"
                    "key = simulate_symmetric_key_exchange()\n"
                    "print('Key length in bytes:', len(key))"
                ),
                "explanation": "Demonstrates generation of a 256-bit symmetric key that must be pre-shared between communicating parties."
            }
        ],
        coding_challenge={
            "description": "Write a Python function `symmetric_key_pairs(num_users: int) -> int` that calculates how many unique shared secret keys are required for `num_users` individuals to all communicate securely with each other using symmetric encryption (Formula: `n * (n - 1) / 2`).",
            "starter_code": (
                "def symmetric_key_pairs(num_users: int) -> int:\n"
                "    # Return total unique symmetric keys required\n"
                "    return 0\n\n"
                "print(symmetric_key_pairs(2))\n"
                "print(symmetric_key_pairs(10))\n"
                "print(symmetric_key_pairs(100))"
            ),
            "solution_code": (
                "def symmetric_key_pairs(num_users: int) -> int:\n"
                "    if num_users < 2:\n"
                "        return 0\n"
                "    return (num_users * (num_users - 1)) // 2\n\n"
                "print(symmetric_key_pairs(2))\n"
                "print(symmetric_key_pairs(10))\n"
                "print(symmetric_key_pairs(100))"
            ),
            "expected_output": "1\n45\n4950"
        },
        quizzes=[
            {
                "question": "What is the defining characteristic of Symmetric Encryption?",
                "options": [
                    "A single, identical secret key is used for both encrypting the plaintext and decrypting the ciphertext",
                    "Two different keys are used: one public and one private",
                    "No keys are needed to decrypt data",
                    "It only encrypts numbers, not letters"
                ],
                "correct_answer": "A single, identical secret key is used for both encrypting the plaintext and decrypting the ciphertext",
                "explanation": "In symmetric systems (like AES), both sender and receiver must possess the exact same shared secret key."
            },
            {
                "question": "What is the primary operational advantage of Symmetric Encryption over Asymmetric Encryption?",
                "options": [
                    "Symmetric encryption is computationally lightweight and dramatically faster, making it suitable for bulk data transfers",
                    "Symmetric keys can be published openly on the internet",
                    "Symmetric algorithms do not require electricity",
                    "Symmetric encryption never uses mathematical formulas"
                ],
                "correct_answer": "Symmetric encryption is computationally lightweight and dramatically faster, making it suitable for bulk data transfers",
                "explanation": "Symmetric ciphers use fast hardware-accelerated bitwise operations, encrypting gigabytes of data in seconds."
            },
            {
                "question": "Which symmetric cipher is universally adopted as the modern gold standard by governments, banks, and cybersecurity frameworks?",
                "options": ["AES (Advanced Encryption Standard)", "DES (Data Encryption Standard)", "Caesar Cipher", "RC4"],
                "correct_answer": "AES (Advanced Encryption Standard)",
                "explanation": "AES was selected by NIST in 2001, providing impenetrable security at 128, 192, and 256-bit key sizes."
            },
            {
                "question": "What is the 'Key Distribution Problem' inherent to symmetric cryptography?",
                "options": [
                    "Securely delivering the shared secret key to the recipient over an untrusted network without an eavesdropper intercepting it",
                    "Keys taking up too much hard drive storage",
                    "Key generation wearing out the computer CPU",
                    "Forgetting where the physical key was placed"
                ],
                "correct_answer": "Securely delivering the shared secret key to the recipient over an untrusted network without an eavesdropper intercepting it",
                "explanation": "If Alice and Bob have never met, sending the symmetric key over the internet risks interception, which led to the invention of asymmetric cryptography."
            },
            {
                "question": "Why is the original 56-bit DES (Data Encryption Standard) considered completely insecure today?",
                "options": [
                    "Its 56-bit key size is so small that modern computers can brute-force all possible keys in just a few hours",
                    "DES was deleted from the internet",
                    "DES cannot encrypt vowels",
                    "DES requires an analog dial-up telephone"
                ],
                "correct_answer": "Its 56-bit key size is so small that modern computers can brute-force all possible keys in just a few hours",
                "explanation": "56 bits yields only 72 quadrillion combinations, easily brute-forced by modern cloud compute clusters."
            }
        ]
    ),

    # ---------------------------------------------------------
    # Day 40: Asymmetric Encryption (Public Key & Private Key)
    # ---------------------------------------------------------
    DayBlueprint(
        order=40,
        title="Day 40: Asymmetric Encryption (Public Key & Private Key)",
        concept="Mastering public-key cryptography: Mathematically paired keys (Public Key to encrypt, Private Key to decrypt), Diffie-Hellman key exchange, RSA, and Elliptic Curve Cryptography (ECC).",
        analogy="Think of a public post office drop box: The mail drop slot is the **Public Key**—anyone in the entire world can drop a sealed letter into the box. But once the letter falls inside, only the mail carrier who owns the physical brass key (**Private Key**) can open the door and retrieve the letter. Anyone can deposit (encrypt), but only the owner can unlock (decrypt).",
        theory_sections=[
            {
                "heading": "Asymmetric Cryptography Architecture",
                "content": (
                    "Invented to solve the symmetric key distribution problem, asymmetric encryption uses a **mathematically linked keypair**:\n\n"
                    "1. **Public Key**: Distributed freely and openly to the entire world. Anyone can use your public key to encrypt a secret message addressed to you.\n"
                    "2. **Private Key**: Kept strictly secret by the owner and **NEVER SHARED**. Only your private key can decrypt messages encrypted with your matching public key.\n"
                    "3. **Mathematical Foundations**: Relies on 'one-way trapdoor functions'—math that is easy to compute in one direction, but computationally impossible to reverse without a secret trapdoor:\n"
                    "   - **RSA (Rivest-Shamir-Adleman)**: Relies on the extreme difficulty of factoring the product of two massive prime numbers (2048 to 4096 bits).\n"
                    "   - **ECC (Elliptic Curve Cryptography)**: Relies on the discrete logarithm problem over elliptic curves. Provides equivalent security to RSA at dramatically smaller key sizes (e.g., 256-bit ECC matches 3072-bit RSA), saving CPU and battery on mobile devices."
                )
            },
            {
                "heading": "Hybrid Cryptography: The Best of Both Worlds",
                "content": (
                    "Asymmetric encryption is computationally slow and cannot encrypt large gigabyte files. Real-world protocols (HTTPS, SSH, PGP) use **Hybrid Encryption**:\n"
                    "1. Use Asymmetric crypto (RSA/ECC/Diffie-Hellman) to safely negotiate a temporary random symmetric session key.\n"
                    "2. Use fast Symmetric crypto (AES-256) with that session key to encrypt the actual web traffic or file."
                )
            }
        ],
        code_snippets=[
            {
                "title": "Generating RSA and ECC Keypairs via OpenSSL CLI",
                "language": "bash",
                "code": (
                    "# Generating a 2048-bit RSA private key:\n"
                    "openssl genrsa -out private_key.pem 2048\n\n"
                    "# Extracting the matching public key to share with the world:\n"
                    "openssl rsa -in private_key.pem -pubout -out public_key.pem\n\n"
                    "# Generating modern Elliptic Curve (ECC - prime256v1) private key:\n"
                    "openssl ecparam -name prime256v1 -genkey -noout -out ecc_private.pem"
                ),
                "explanation": "Standard commands used to generate public/private key pairs for SSH servers and SSL certificates."
            },
            {
                "title": "Python: Demonstrating Asymmetric Hybrid Key Exchange Concept",
                "language": "python",
                "code": (
                    "def simulate_hybrid_handshake():\n"
                    "    # Step 1: Server sends Public Key to Client\n"
                    "    server_public_key = 'SERVER_PUB_KEY_RSA_4096'\n"
                    "    \n"
                    "    # Step 2: Client generates high-speed symmetric AES session key\n"
                    "    session_key = 'AES_SESSION_SECRET_987654'\n"
                    "    \n"
                    "    # Step 3: Client encrypts session key with server's public key\n"
                    "    encrypted_session_key = f'RSA_ENCRYPTED({session_key})_BY_{server_public_key}'\n"
                    "    \n"
                    "    # Step 4: Server decrypts using its Private Key\n"
                    "    print('[Client] Transmitting encrypted session key over internet...')\n"
                    "    print(f'[Server] Decrypted session key using Private Key: {session_key}')\n"
                    "    print('[Both] Subsequent gigabytes of data encrypted via fast AES-256!')\n\n"
                    "simulate_hybrid_handshake()"
                ),
                "explanation": "Demonstrates the hybrid encryption model utilized in HTTPS (TLS) handshakes."
            }
        ],
        coding_challenge={
            "description": "Write a Python function `check_asymmetric_rule(encrypt_key_type: str, decrypt_key_type: str) -> bool` that verifies asymmetric confidentiality: data encrypted with 'PUBLIC' must be decrypted with 'PRIVATE' to return True. Any other combination returns False.",
            "starter_code": (
                "def check_asymmetric_rule(encrypt_key_type: str, decrypt_key_type: str) -> bool:\n"
                "    # Return True if valid asymmetric encryption/decryption pair\n"
                "    return False\n\n"
                "print(check_asymmetric_rule('PUBLIC', 'PRIVATE'))\n"
                "print(check_asymmetric_rule('PUBLIC', 'PUBLIC'))\n"
                "print(check_asymmetric_rule('PRIVATE', 'PRIVATE'))"
            ),
            "solution_code": (
                "def check_asymmetric_rule(encrypt_key_type: str, decrypt_key_type: str) -> bool:\n"
                "    e = encrypt_key_type.upper()\n"
                "    d = decrypt_key_type.upper()\n"
                "    return (e == 'PUBLIC' and d == 'PRIVATE')\n\n"
                "print(check_asymmetric_rule('PUBLIC', 'PRIVATE'))\n"
                "print(check_asymmetric_rule('PUBLIC', 'PUBLIC'))\n"
                "print(check_asymmetric_rule('PRIVATE', 'PRIVATE'))"
            ),
            "expected_output": "True\nFalse\nFalse"
        },
        quizzes=[
            {
                "question": "If Alice wants to send a confidential encrypted message to Bob using Asymmetric Cryptography, which key must Alice use to encrypt the message?",
                "options": ["Bob's Public Key", "Bob's Private Key", "Alice's Private Key", "Alice's Public Key"],
                "correct_answer": "Bob's Public Key",
                "explanation": "To send confidential data to Bob, Alice encrypts it using Bob's freely available Public Key. Only Bob's matching Private Key can decrypt it."
            },
            {
                "question": "What is the primary operational advantage of Elliptic Curve Cryptography (ECC) over traditional RSA?",
                "options": [
                    "ECC provides equivalent cryptographic security with significantly smaller key sizes, reducing compute overhead and power consumption",
                    "ECC can only be broken by aliens",
                    "ECC eliminates the need for private keys",
                    "ECC does not use math"
                ],
                "correct_answer": "ECC provides equivalent cryptographic security with significantly smaller key sizes, reducing compute overhead and power consumption",
                "explanation": "A 256-bit ECC key offers comparable security to a 3072-bit RSA key, providing high speed and low memory footprints ideal for mobile and IoT devices."
            },
            {
                "question": "What is 'Hybrid Cryptography' as used in HTTPS (TLS)?",
                "options": [
                    "Using asymmetric cryptography to securely exchange a temporary symmetric session key, then using fast symmetric AES to encrypt the actual data stream",
                    "Using both gasoline and electric batteries to power servers",
                    "Switching between Windows and Linux every hour",
                    "Using two passwords instead of one"
                ],
                "correct_answer": "Using asymmetric cryptography to securely exchange a temporary symmetric session key, then using fast symmetric AES to encrypt the actual data stream",
                "explanation": "Hybrid encryption combines the key-distribution solution of asymmetric crypto with the raw processing speed of symmetric ciphers."
            },
            {
                "question": "What happens if someone accidentally publishes or shares their Asymmetric Private Key online?",
                "options": [
                    "Anyone who obtains the private key can now decrypt all past and future confidential messages addressed to that entity and impersonate their digital signature",
                    "The public key automatically deletes itself",
                    "The internet service provider shuts off power",
                    "Nothing, because public keys protect private keys"
                ],
                "correct_answer": "Anyone who obtains the private key can now decrypt all past and future confidential messages addressed to that entity and impersonate their digital signature",
                "explanation": "The private key is the foundation of identity and decryption. Compromising it completely breaks confidentiality and authenticity."
            },
            {
                "question": "Can an Asymmetric Public Key be used to decrypt a message that was encrypted using that exact same Public Key?",
                "options": [
                    "No, only the mathematically paired Private Key can decrypt messages encrypted by the Public Key",
                    "Yes, public keys work in both directions",
                    "Yes, but only within 5 minutes of encryption",
                    "Only if the computer is connected to the internet"
                ],
                "correct_answer": "No, only the mathematically paired Private Key can decrypt messages encrypted by the Public Key",
                "explanation": "Asymmetric cryptography is asymmetric: one key encrypts, but only the other paired key can reverse the mathematical trapdoor."
            }
        ]
    ),


]
