"""
Root Runner for Seeding Complete APIs & Web Services Architecture (60 Days)
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from seeder.courses.seed_api_60_days import main

if __name__ == "__main__":
    main()
