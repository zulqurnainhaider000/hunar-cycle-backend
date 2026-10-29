import os
import sys

backend_root = os.path.abspath(os.path.dirname(__file__))
if backend_root not in sys.path:
    sys.path.insert(0, backend_root)

from dotenv import load_dotenv
load_dotenv(os.path.join(backend_root, '.env'))

from app import create_app
from app.db import db

def run_tests():
    app = create_app()
    if not db.is_connected():
        db.connect()

    client = app.test_client()

    print("=" * 60)
    print("TESTING UNIVERSITY CATEGORY BACKEND FILTERING")
    print("=" * 60)

    # 1. Test /api/courses?category=University
    res_uni = client.get('/api/courses?category=University')
    assert res_uni.status_code == 200, f"Expected 200, got {res_uni.status_code}"
    uni_courses = res_uni.get_json()
    print(f"[PASS] /api/courses?category=University returned {len(uni_courses)} courses")
    assert len(uni_courses) == 9, f"Expected 9 university courses, got {len(uni_courses)}"
    for idx, c in enumerate(uni_courses, 1):
        print(f"  {idx}. {c['title']} | Category: {c['category']}")
        assert (c['category'] or '').lower() in ['university', 'university courses'], f"Unexpected category: {c['category']}"

    # 2. Test /api/courses?category=All (or no param)
    res_all = client.get('/api/courses')
    assert res_all.status_code == 200
    all_courses = res_all.get_json()
    print(f"\n[PASS] /api/courses (All) returned {len(all_courses)} total courses")
    assert len(all_courses) >= 30, f"Expected at least 30 courses, got {len(all_courses)}"
    # Verify university courses are included in all courses
    uni_in_all = [c for c in all_courses if (c['category'] or '').lower() in ['university', 'university courses']]
    assert len(uni_in_all) == 9, f"Expected 9 university courses in All, got {len(uni_in_all)}"
    print(f"  - Verified all 9 university courses appear in 'All' ({len(uni_in_all)} found)")

    # 3. Test /api/courses?category=AI & Data
    res_ai = client.get('/api/courses?category=AI%20%26%20Data')
    assert res_ai.status_code == 200
    ai_courses = res_ai.get_json()
    print(f"\n[PASS] /api/courses?category=AI & Data returned {len(ai_courses)} courses")
    # Verify NO university courses leaked into AI & Data
    uni_in_ai = [c for c in ai_courses if (c['category'] or '').lower() in ['university', 'university courses']]
    assert len(uni_in_ai) == 0, f"University courses leaked into AI & Data: {uni_in_ai}"
    print("  - Verified 0 university courses in 'AI & Data'")

    # 4. Test /api/lessons?category=University
    res_lessons = client.get('/api/lessons?category=University')
    assert res_lessons.status_code == 200
    assert len(res_lessons.get_json()) == 9
    print(f"\n[PASS] /api/lessons?category=University returned {len(res_lessons.get_json())} courses")

    db.disconnect()
    print("\n" + "=" * 60)
    print("ALL UNIVERSITY CATEGORY TESTS PASSED SUCCESSFULLY (100%)!")
    print("=" * 60)

if __name__ == '__main__':
    run_tests()
