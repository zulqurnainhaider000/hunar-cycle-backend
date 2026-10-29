import os
import sys

backend_root = os.path.abspath(os.path.dirname(__file__))
if backend_root not in sys.path:
    sys.path.insert(0, backend_root)

from dotenv import load_dotenv
load_dotenv(os.path.join(backend_root, '.env'))

from app.db import db

def run_migration():
    print("Running migration for LiveClass and Event models...")
    try:
        if not db.is_connected():
            db.connect()

        # 1. Update Event table if exists
        try:
            db.execute_raw('ALTER TABLE "Event" ADD COLUMN IF NOT EXISTS "accessCode" TEXT DEFAULT \'FREE\';')
            db.execute_raw('ALTER TABLE "Event" ADD COLUMN IF NOT EXISTS "isLocked" BOOLEAN DEFAULT false;')
            db.execute_raw('ALTER TABLE "Event" ADD COLUMN IF NOT EXISTS "youtubeVideoId" TEXT;')
            db.execute_raw('ALTER TABLE "Event" ADD COLUMN IF NOT EXISTS "status" TEXT DEFAULT \'active\';')
            print("[SUCCESS] Event table columns updated!")
        except Exception as e:
            print(f"[NOTICE] Event table migration notice: {e}")

        # 2. Create LiveClass table if not exists
        try:
            db.execute_raw('''
            CREATE TABLE IF NOT EXISTS "LiveClass" (
                "id" TEXT PRIMARY KEY,
                "courseTitle" TEXT NOT NULL,
                "title" TEXT NOT NULL,
                "instructorName" TEXT NOT NULL,
                "instructorTitle" TEXT,
                "instructorAvatar" TEXT,
                "instructorId" TEXT,
                "liveRoomUrl" TEXT,
                "youtubeVideoId" TEXT,
                "accessCode" TEXT DEFAULT 'FREE',
                "isLocked" BOOLEAN DEFAULT false,
                "status" TEXT DEFAULT 'active',
                "enrolledCount" TEXT DEFAULT '+60',
                "duration" TEXT DEFAULT '2h+ Hours',
                "tag" TEXT DEFAULT 'Live Class',
                "badgeText" TEXT DEFAULT 'Live Class',
                "interactiveBadgeTitle" TEXT DEFAULT 'Live Interactive',
                "interactiveBadgeSub" TEXT DEFAULT 'Q&A+ Feedback',
                "currentTopic" TEXT,
                "description" TEXT,
                "scheduledTime" TEXT,
                "createdAt" TIMESTAMP(3) DEFAULT CURRENT_TIMESTAMP,
                "updatedAt" TIMESTAMP(3) DEFAULT CURRENT_TIMESTAMP
            );
            ''')
            print("[SUCCESS] LiveClass table verified/created!")
        except Exception as e:
            print(f"[NOTICE] LiveClass table creation notice: {e}")

    except Exception as e:
        print(f"[ERROR] Database connection failed during migration: {e}")
    finally:
        try:
            if db.is_connected():
                db.disconnect()
        except Exception:
            pass

if __name__ == '__main__':
    run_migration()
