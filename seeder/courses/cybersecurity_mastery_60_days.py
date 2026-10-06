"""
Basics of Cybersecurity & IT Fundamentals 60-Day Curriculum Blueprint
Assembles all 60 days of topic-per-day lessons, deep ELI5 analogies,
progressive code/CLI snippets, daily challenges, and 5 MCQs per day.
"""

from seeder.course_blueprint import CourseBlueprint
from seeder.courses.cybersecurity_curriculum_days_1_15 import DAYS_1_TO_15
from seeder.courses.cybersecurity_curriculum_days_16_30 import DAYS_16_TO_30
from seeder.courses.cybersecurity_curriculum_days_31_45 import DAYS_31_TO_45
from seeder.courses.cybersecurity_curriculum_days_46_60 import DAYS_46_TO_60

# Consolidate all 60 days in strict sequential order
ALL_60_DAYS = DAYS_1_TO_15 + DAYS_16_TO_30 + DAYS_31_TO_45 + DAYS_46_TO_60

CYBERSECURITY_MASTERY_COURSE_BLUEPRINT = CourseBlueprint(
    title="Basics of Cybersecurity & IT Fundamentals",
    category="TECH",
    description=(
        "The definitive 60-Day foundational journey into Cybersecurity and Information Technology. "
        "Enforced universal topic-per-day architecture across 10 comprehensive modules: "
        "Module 1: IT Fundamentals (CPU, RAM, Storage, Motherboards, Peripherals, System vs Application Software, OS Architecture, File Systems, Virtualization, and Cloud Computing); "
        "Module 2: Networking Fundamentals (LAN/WAN/PAN/WLAN, 7-Layer OSI & 4-Layer TCP/IP models, IPv4/IPv6, MAC Addresses, Common Ports & Protocols, Network Hardware, and Hands-on CLI Lab); "
        "Module 3: Cyber Security Foundations (Cyber Security definitions, The CIA Triad, The AAA Framework, Vulnerability/Threat/Risk/Exploit taxonomy, Hacker Types, and Nation-State APTs); "
        "Module 4: Threats, Attacks & Malware (Viruses, Worms, Trojans, Logic Bombs, Ransomware & Rootkits, Social Engineering & Phishing, Network Attacks & MitM, and SQL Injection/XSS); "
        "Module 5: Identity & Access Management (Authentication Factors, MFA/2FA, MAC/DAC/RBAC/ABAC models, SSO & Federation, Biometrics, and Principle of Least Privilege); "
        "Module 6: Network & Infrastructure Security (Firewalls & WAFs, IDS vs IPS, VPNs & IPsec, Wi-Fi WEP/WPA/WPA2/WPA3, Network Segmentation & DMZ, Honeypots, and Proxies); "
        "Module 7: Cryptography & Data Protection (Plaintext vs Ciphertext, Symmetric AES, Asymmetric RSA/ECC, Hashing MD5/SHA-256, Digital Signatures, PKI & TLS, and Data States); "
        "Module 8: Endpoint & Physical Security (Antivirus & EDR, Patch Management, System Hardening, MDM & BYOD, Physical Security & Mantraps, and NIST SP 800-88 Data Sanitization); "
        "Module 9: Security Operations & Incident Response (SOC Tier Operations, SIEM Log Correlation, NIST SP 800-61 Incident Handling, and Digital Forensics Chain of Custody); "
        "Module 10: Risk Management & Compliance (Quantitative Risk Assessment, Vulnerability Scanning vs Pen Testing, BCP & Disaster Recovery, Security Policies, Awareness Training, and Day 60 Capstone: Compliance Laws GDPR, HIPAA, PCI-DSS, ISO 27001). "
        "Features 60 practical security coding challenges and 300 knowledge verification quizzes."
    ),
    color="#06B6D4",
    days=ALL_60_DAYS
)
