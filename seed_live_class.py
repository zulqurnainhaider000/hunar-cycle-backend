import os
import sys
from datetime import datetime, timedelta

backend_root = os.path.abspath(os.path.dirname(__file__))
if backend_root not in sys.path:
    sys.path.insert(0, backend_root)

from dotenv import load_dotenv
load_dotenv(os.path.join(backend_root, '.env'))

from app import create_app
from app.db import db

def seed_events():
    app = create_app()
    if not db.is_connected():
        db.connect()

    print("Checking and seeding rich Live Classes and Events...")

    # Find or create mentor/creator
    creator = db.user.find_first(where={"username": "Marcus Aurelius"})
    if not creator:
        creator = db.user.create({
            "username": "Marcus Aurelius",
            "email": "marcus.aurelius@hunarcircle.com",
            "passwordHash": "live_mentor_secret_hash_2026",
            "headline": "Lead UI/UX & Design Systems Architect",
            "location": "Rome, IT & Global Remote",
            "avatarUrl": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=300&q=80",
            "level": 15,
            "xp": 9500,
            "coins": 450
        })
        print(f"Created mentor user: {creator.username}")
    else:
        print(f"Using existing mentor: {creator.username}")

    now = datetime.utcnow()

    # 1. Featured UI/UX Design Live Class
    existing_hero = db.event.find_first(where={"title": {"contains": "Ui/Ux Design"}})
    if not existing_hero:
        e1 = db.event.create({
            "title": "Ui/Ux Design\nLive Class",
            "description": "Interactive workshop on design tokens, mobile typography, and auto-layout system architecture with live Q&A.",
            "location": "Virtual Live Classroom #1",
            "date": now,
            "color": "#144FE6",
            "creatorId": creator.id
        })
        print(f"[SEEDED] Hero Live Class: {e1.title} (ID: {e1.id})")
    else:
        print(f"[EXISTS] Hero Live Class: {existing_hero.title}")

    # 2. Python Backend Masterclass
    existing_py = db.event.find_first(where={"title": {"contains": "Full-Stack API"}})
    if not existing_py:
        e2 = db.event.create({
            "title": "Full-Stack API Engineering Live",
            "description": "Deep dive into building high-concurrency microservices with Flask, PostgreSQL, and Socket.IO.",
            "location": "Dev Dojo Virtual Stage",
            "date": now + timedelta(days=1, hours=4),
            "color": "#10B981",
            "creatorId": creator.id
        })
        print(f"[SEEDED] Event: {e2.title} (ID: {e2.id})")

    # 3. Algorithms & University Dojo
    existing_dsa = db.event.find_first(where={"title": {"contains": "Algorithms"}})
    if not existing_dsa:
        e3 = db.event.create({
            "title": "Data Structures & Algorithms Live Dojo",
            "description": "Live problem solving session on trees, graphs, and dynamic programming with competitive programmers.",
            "location": "Algorithms Lab Studio",
            "date": now + timedelta(days=3),
            "color": "#8B5CF6",
            "creatorId": creator.id
        })
        print(f"[SEEDED] Event: {e3.title} (ID: {e3.id})")

    total_events = db.event.count()
    print(f"Total Events currently in Database: {total_events}")

if __name__ == '__main__':
    seed_events()
