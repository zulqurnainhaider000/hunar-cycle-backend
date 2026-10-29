import os
import sys

backend_root = os.path.abspath(os.path.dirname(__file__))
if backend_root not in sys.path:
    sys.path.insert(0, backend_root)

from dotenv import load_dotenv
load_dotenv(os.path.join(backend_root, '.env'))

from app.db import db

def run_migration():
    if not db.is_connected():
        db.connect()

    print("Running migration to add avatarUrl, location, headline to User table...")
    try:
        db.execute_raw('ALTER TABLE "User" ADD COLUMN IF NOT EXISTS "avatarUrl" TEXT;')
        db.execute_raw('ALTER TABLE "User" ADD COLUMN IF NOT EXISTS "location" TEXT DEFAULT \'Islamabad, PK\';')
        db.execute_raw('ALTER TABLE "User" ADD COLUMN IF NOT EXISTS "headline" TEXT DEFAULT \'Creative Technologist & Learner\';')
        db.execute_raw('UPDATE "User" SET "location" = \'Islamabad, PK\' WHERE "location" IS NULL;')
        db.execute_raw('UPDATE "User" SET "headline" = \'Creative Technologist & Learner\' WHERE "headline" IS NULL;')
        print("[SUCCESS] Columns added and default values populated!")
    except Exception as e:
        print(f"[ERROR] Migration failed: {e}")
    finally:
        db.disconnect()

if __name__ == '__main__':
    run_migration()
