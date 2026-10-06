"""
Root Runner for Seeding Web Development with Flask (40 Days)
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from seeder.courses.seed_flask_40_days import main

if __name__ == "__main__":
    main()
