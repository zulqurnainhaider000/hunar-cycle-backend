"""
Root Runner for Seeding Mobile App Development (40 Days)
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from seeder.courses.seed_mobile_40_days import main

if __name__ == "__main__":
    main()
