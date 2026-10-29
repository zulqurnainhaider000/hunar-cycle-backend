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

    print("Running migration to add role column to User table...")
    try:
        db.execute_raw('ALTER TABLE "User" ADD COLUMN IF NOT EXISTS "role" TEXT DEFAULT \'student\';')
        db.execute_raw('UPDATE "User" SET "role" = \'student\' WHERE "role" IS NULL;')
        print("[SUCCESS] role column added to User table and default values populated!")
    except Exception as e:
        print(f"[ERROR] Migration failed: {e}")
    finally:
        db.disconnect()

if __name__ == '__main__':
    run_migration()
