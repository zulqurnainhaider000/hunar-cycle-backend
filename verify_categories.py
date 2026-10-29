"""
Verifies that /api/lessons endpoint returns courses for every single frontend category tab.
"""
import sys
import os

backend_root = os.path.abspath(os.path.dirname(__file__))
if backend_root not in sys.path:
    sys.path.insert(0, backend_root)

# Load environment
try:
    from dotenv import load_dotenv
    load_dotenv(os.path.join(backend_root, '.env'))
except ImportError:
    pass

from app import create_app
from app.db import db

def main():
    app = create_app()
    if not db.is_connected():
        db.connect()

    client = app.test_client()

    response = client.get('/api/lessons')
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    lessons = response.get_json()

    print("=" * 70)
    print(f"VERIFYING /api/lessons (Total Courses: {len(lessons)})")
    print("=" * 70)

    # 10 Frontend category filter definitions from LearnScreen.tsx
    frontend_tabs = [
        {"name": "Computer Courses", "key": "Computer"},
        {"name": "Business", "key": "Business"},
        {"name": "Language", "key": "Language"},
        {"name": "Design", "key": "Design"},
        {"name": "University Courses", "key": "University"},
        {"name": "Medical Billing", "key": "Medical Billing"},
        {"name": "Freelancing", "key": "Freelancing"},
        {"name": "Mobile Dev", "key": "Mobile Dev"},
        {"name": "Finance & Crypto", "key": "Finance & Crypto"},
        {"name": "Networking & IT", "key": "Networking & IT"}
    ]

    all_passed = True

    for tab in frontend_tabs:
        sel = tab["key"].lower()
        
        # Exact filtering logic from frontend LearnScreen.tsx:
        matched = []
        for l in lessons:
            cat = (l.get("category") or "").lower()
            title = (l.get("title") or "").lower()

            if sel == "computer":
                if cat in ["tech", "computer courses", "computer"]:
                    matched.append(l)
            elif sel == "language":
                if cat == "language":
                    matched.append(l)
            elif sel == "medical billing":
                if cat in ["medical billing", "medical"]:
                    matched.append(l)
            elif sel == "freelancing":
                if "freelancing" in cat:
                    matched.append(l)
            else:
                if cat == sel or sel in title:
                    matched.append(l)

        count = len(matched)
        status = "PASSED" if count > 0 else "FAILED"
        if count == 0:
            all_passed = False

        course_names = ", ".join([m["title"] for m in matched[:2]])
        if count > 2:
            course_names += f" (+{count - 2} more)"

        print(f"[{status}] Tab '{tab['name']:<18}' (key: '{tab['key']:<16}') -> {count:<2} course(s): {course_names}")

    if db.is_connected():
        db.disconnect()

    print("=" * 70)
    if all_passed:
        print("[SUCCESS] ALL 10 FRONTEND CATEGORY TABS HAVE ACTIVE COURSES!")
    else:
        print("[FAIL] Some category tabs are still empty.")
    print("=" * 70)

if __name__ == "__main__":
    main()
