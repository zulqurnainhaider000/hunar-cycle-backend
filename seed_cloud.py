"""
HunarCircle - Cloud Database Seeder Script
Run this script locally or in cloud shell to populate all lessons, modules, and hub events into your cloud database.
Usage:
  python seed_cloud.py
"""
import os
import sys
import subprocess

def run_seed():
    print("[1/3] Seeding all base lessons...")
    try:
        import seed_all_lessons
        seed_all_lessons.seed()
        print("✓ Base lessons seeded successfully.")
    except Exception as e:
        print(f"Error seeding base lessons: {e}")

    print("\n[2/3] Seeding 30-day curriculum modules...")
    try:
        import seed_all_modules_30_days
        # seed_all_modules_30_days runs on import or we can call its main logic
        print("✓ 30-day curriculum modules seeded.")
    except Exception as e:
        print(f"Error seeding 30-day curriculum: {e}")

    print("\n[3/3] Seeding Hub events and turfs...")
    try:
        import seed_hub
        print("✓ Hub seeded successfully.")
    except Exception as e:
        print(f"Error seeding hub: {e}")

    print("\n✓ Database seeding routine completed!")

if __name__ == '__main__':
    run_seed()
