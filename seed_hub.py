from prisma import Prisma
from datetime import datetime, timedelta

def seed():
    db = Prisma()
    db.connect()

    print("Seeding Local Hub (Events & Turfs)...")
    
    # Need a dummy user to act as creator
    creator = db.user.find_first()
    if not creator:
        creator = db.user.create({
            "username": "HubAdmin",
            "email": "admin@hunarcircle.com",
            "passwordHash": "dummy"
        })

    # Events
    now = datetime.now()
    
    db.event.create({
        "title": "Weekend Futsal Tournament",
        "description": "5v5 knockout tournament at Haripur Ground.",
        "location": "Haripur Ground",
        "date": now + timedelta(days=2),
        "color": "#10B981",
        "creatorId": creator.id
    })
    
    db.event.create({
        "title": "Tech Talk: Python & Flask architectures",
        "description": "Deep dive into building APIs with Flask and Prisma.",
        "location": "UOBS Campus, Hall B",
        "date": now + timedelta(days=5),
        "color": "#3B82F6",
        "creatorId": creator.id
    })

    # Turfs
    db.turf.create({
        "name": "Football Kit Design Enthusiasts",
        "description": "Share designs, mockups, and find collabs.",
        "color": "#8B5CF6",
        "creatorId": creator.id
    })
    
    db.turf.create({
        "name": "Medical Billing Prep Group",
        "description": "Study group for ICD-10 exams.",
        "color": "#EF4444",
        "creatorId": creator.id
    })

    print("Seeding complete!")
    db.disconnect()

if __name__ == "__main__":
    seed()
