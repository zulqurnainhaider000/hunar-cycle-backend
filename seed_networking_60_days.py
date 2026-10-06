"""
Root Runner for Seeding Computer Networking Basics (60 Days)
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from seeder.courses.seed_networking_60_days import main

if __name__ == "__main__":
    main()
