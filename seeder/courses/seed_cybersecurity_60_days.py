"""
Executable Runner for Seeding Basics of Cybersecurity & IT Fundamentals (60 Days)
Using the Universal Course Seeder Engine and the 3 curriculum modules:
- cybersecurity_curriculum_days_1_20.py (Days 1 to 20)
- cybersecurity_curriculum_days_21_40.py (Days 21 to 40)
- cybersecurity_curriculum_days_41_60.py (Days 41 to 60)
"""

import sys
import os

# Ensure backend root is on sys.path
backend_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if backend_root not in sys.path:
    sys.path.insert(0, backend_root)

# Ensure Windows terminal doesn't crash on UTF-8 / emojis
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

from seeder.course_blueprint import CourseBlueprint
from seeder.universal_seeder import UniversalCourseSeeder
from seeder.courses.cybersecurity_curriculum_days_1_20 import DAYS_1_TO_20
from seeder.courses.cybersecurity_curriculum_days_21_40 import DAYS_21_TO_40
from seeder.courses.cybersecurity_curriculum_days_41_60 import DAYS_41_TO_60

# Consolidate all 60 days strictly in sequence
ALL_60_DAYS = DAYS_1_TO_20 + DAYS_21_TO_40 + DAYS_41_TO_60

CYBERSECURITY_60_DAYS_BLUEPRINT = CourseBlueprint(
    title="Basics of Cybersecurity & IT Fundamentals",
    category="Tech",
    description=(
        "The complete 60-Day foundational curriculum in Cybersecurity and IT Fundamentals. "
        "Covers 10 core modules: "
        "Module 1: IT Fundamentals (Hardware & Systems, Days 1-7); "
        "Module 2: Networking Fundamentals (OSI, TCP/IP, IP/MAC, Ports, Devices, CLI Tools, Days 8-13); "
        "Module 3: Cyber Security Foundations (Definitions, CIA Triad, AAA Framework, Terminologies, Hacker Types, Days 14-19); "
        "Module 4: Threats, Attacks & Malware (Viruses, Ransomware, Social Engineering, DDoS/MitM, Web Attacks, Days 20-24); "
        "Module 5: Identity & Access Management (Authentication Factors, MFA/2FA, MAC/DAC/RBAC, SSO, Biometrics, PoLP, Days 25-30); "
        "Module 6: Network & Infrastructure Security (Firewalls, IDS/IPS, VPNs, Wi-Fi, DMZ, Honeypots, Proxies, Days 31-37); "
        "Module 7: Cryptography & Data Protection (Symmetric AES, Asymmetric RSA, Hashing SHA-256, Digital Signatures, PKI/TLS, Data States, Days 38-44); "
        "Module 8: Endpoint & Physical Security (Antivirus/EDR, Patching, Hardening, MDM/BYOD, Physical Controls, Data Sanitization, Days 45-50); "
        "Module 9: Security Operations & Incident Response (SOC Basics, SIEM, Incident Response Lifecycle, Digital Forensics, Days 51-54); "
        "Module 10: Risk Management & Compliance (Risk Assessment, Vuln Scanning vs Pen Testing, BCP/DR, Security Policies, Awareness Training, Compliance Laws GDPR/HIPAA/PCI-DSS/ISO 27001, Days 55-60). "
        "Includes 60 practical security challenges and 300 multiple choice questions."
    ),
    color="#06B6D4",
    days=ALL_60_DAYS
)


def run_seeder_and_verify(verbose: bool = True):
    seeder = UniversalCourseSeeder()
    try:
        seeder.connect()
        results = seeder.seed_course(CYBERSECURITY_60_DAYS_BLUEPRINT, verbose=verbose)

        # Database Verification
        db = seeder.db
        lesson_id = results['lesson_id']
        lesson = db.lesson.find_unique(where={"id": lesson_id})
        steps_count = db.lessonstep.count(where={"lessonId": lesson_id})
        quizzes_count = db.quiz.count(where={"lessonId": lesson_id})
        flashcards_count = db.flashcard.count(where={"lessonId": lesson_id})

        print("\n" + "=" * 60)
        print("[DATABASE VERIFICATION REPORT]")
        print(f"  Lesson ID:         {lesson_id}")
        print(f"  Lesson Title:      {lesson.title}")
        print(f"  Lesson Category:   {lesson.category}")
        print(f"  Lesson Steps:      {steps_count} (Expected: 60)")
        print(f"  Quizzes:           {quizzes_count} (Expected: 300)")
        print(f"  Flashcards:        {flashcards_count} (Expected: 300)")
        print("=" * 60)

        assert steps_count == 60, f"Expected 60 LessonSteps, found {steps_count}"
        assert quizzes_count == 300, f"Expected 300 Quizzes, found {quizzes_count}"
        assert lesson is not None, "Lesson not found in database"

        # Verify steps and quiz foreign keys
        steps = db.lessonstep.find_many(
            where={"lessonId": lesson_id},
            order={"order": "asc"},
            include={"quizzes": True}
        )
        assert len(steps) == 60, f"Expected 60 steps retrieved, got {len(steps)}"
        for s in steps:
            assert len(s.quizzes) == 5, f"Step {s.order} ({s.title}) has {len(s.quizzes)} quizzes, expected 5"

        print("[OK] ALL VERIFICATION CHECKS PASSED: 1 Lesson, 60 LessonSteps, 300 Quizzes successfully seeded!")
        return results
    except Exception as e:
        print(f"[ERROR] Error during seeding or verification: {e}")
        import traceback
        traceback.print_exc()
        raise
    finally:
        seeder.disconnect()


def main():
    run_seeder_and_verify(verbose=True)


if __name__ == "__main__":
    main()
