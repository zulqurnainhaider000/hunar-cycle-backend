"""
Root Runner for Seeding Basics of Cybersecurity & IT Fundamentals (60 Days)
Imports the orchestration logic from seeder/courses/seed_cybersecurity_60_days.py
"""
import sys
import os

backend_root = os.path.dirname(os.path.abspath(__file__))
if backend_root not in sys.path:
    sys.path.insert(0, backend_root)

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

from seeder.courses.seed_cybersecurity_60_days import run_seeder_and_verify

def main():
    try:
        run_seeder_and_verify(verbose=True)
    except Exception as e:
        sys.exit(1)

if __name__ == "__main__":
    main()
