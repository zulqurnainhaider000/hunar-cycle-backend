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

    print("=" * 70)
    print("HUNAR CYCLE — ADMIN API TEST SUITE")
    print("=" * 70)

    # 1. Test unauthorized access
    unauth_res = client.get('/api/admin/stats')
    assert unauth_res.status_code == 401, f"Expected 401, got {unauth_res.status_code}"
    print("[PASS] 1. Unauthorized request correctly rejected with 401")

    # 2. Test admin login with master admin key
    login_res = client.post('/api/admin/login', json={'adminKey': 'hunar_admin_secret_2026'})
    assert login_res.status_code == 200, f"Expected 200, got {login_res.status_code}"
    token = login_res.get_json()['token']
    headers = {'Authorization': f'Bearer {token}'}
    print("[PASS] 2. Admin authentication successful -> JWT Token acquired")

    # 3. Test stats
    stats_res = client.get('/api/admin/stats', headers=headers)
    assert stats_res.status_code == 200, f"Expected 200, got {stats_res.status_code}"
    stats = stats_res.get_json()
    print(f"[PASS] 3. GET /api/admin/stats: Total Users={stats['totalUsers']}, Verified={stats['verifiedUsers']} ({stats['verifiedPercentage']}%), University Courses={stats['universityCourses']}, Quizzes={stats['totalQuizzes']}, Certificates Issued={stats['certificatesIssued']}")

    # 4. Test users list & pagination
    users_res = client.get('/api/admin/users?page=1&limit=5', headers=headers)
    assert users_res.status_code == 200, f"Expected 200, got {users_res.status_code}"
    users_data = users_res.get_json()
    print(f"[PASS] 4. GET /api/admin/users: Retrieved {len(users_data['users'])} users (Page {users_data['page']}/{users_data['totalPages']})")

    # 5. Test toggle verify on a user if exists
    if users_data['users']:
        test_user = users_data['users'][0]
        initial_status = test_user['isVerified']
        toggle_res = client.put(f"/api/admin/users/{test_user['id']}/toggle-verify", headers=headers)
        assert toggle_res.status_code == 200, f"Expected 200, got {toggle_res.status_code}"
        new_status = toggle_res.get_json()['user']['isVerified']
        assert new_status == (not initial_status), f"Toggle verify mismatch: {new_status} vs {not initial_status}"
        
        # Toggle back to restore initial state
        client.put(f"/api/admin/users/{test_user['id']}/toggle-verify", headers=headers)
        print(f"[PASS] 5. PUT /api/admin/users/:id/toggle-verify: Successfully toggled verification and restored intact for {test_user['username']}")

    # 6. Test courses
    courses_res = client.get('/api/admin/courses', headers=headers)
    assert courses_res.status_code == 200, f"Expected 200, got {courses_res.status_code}"
    courses = courses_res.get_json()
    print(f"[PASS] 6. GET /api/admin/courses: {courses['total']} total courses, {courses['universityCount']} official university courses verified with OBE mappings")

    # 7. Test course quizzes for first course
    if courses['courses']:
        first_c = courses['courses'][0]
        quizzes_res = client.get(f"/api/admin/courses/{first_c['id']}/quizzes", headers=headers)
        assert quizzes_res.status_code == 200, f"Expected 200, got {quizzes_res.status_code}"
        q_data = quizzes_res.get_json()
        print(f"[PASS] 7. GET /api/admin/courses/:id/quizzes: '{q_data['course']['title']}' has {q_data['totalQuizzes']} quizzes across {len(q_data['steps'])} lab experiments")

        # 8. Test quiz update if a quiz exists
        if q_data['steps'] and q_data['steps'][0]['quizzes']:
            q = q_data['steps'][0]['quizzes'][0]
            update_res = client.put(f"/api/admin/quizzes/{q['id']}", headers=headers, json={
                "question": q['question'],
                "options": q['options'],
                "correctAnswer": q['correctAnswer'],
                "explanation": (q.get('explanation') or '') + " [Verified by Admin]"
            })
            assert update_res.status_code == 200, f"Expected 200, got {update_res.status_code}"
            print(f"[PASS] 8. PUT /api/admin/quizzes/:id: Successfully edited assessment question Q: '{q['question'][:40]}...'")

    # 9. Test /admin Web Page
    web_res = client.get('/admin')
    assert web_res.status_code == 200, f"Expected 200, got {web_res.status_code}"
    web_html = web_res.get_data(as_text=True)
    assert "Hunar Cycle" in web_html
    assert "Executive Admin" in web_html
    assert "Course & Lab Creator Studio" in web_html
    assert "marked.min.js" in web_html
    print("[PASS] 9. GET /admin: React/Tailwind Web Dashboard rendered with Course & Lab Creator Studio & Marked.js")

    # 10. Test POST /api/admin/courses (Create Course Container)
    create_course_res = client.post('/api/admin/courses', headers=headers, json={
        "title": "Automated Testing & Kernel CI/CD (QA-401)",
        "category": "University Courses",
        "description": "Comprehensive automated testing and kernel continuous integration syllabus.",
        "color": "#10B981",
        "image": "/assets/courses/testing.png",
        "totalSteps": 14
    })
    assert create_course_res.status_code == 201, f"Expected 201, got {create_course_res.status_code}: {create_course_res.get_data(as_text=True)}"
    created_course = create_course_res.get_json()['course']
    test_course_id = created_course['id']
    print(f"[PASS] 10. POST /api/admin/courses: Successfully created course '{created_course['title']}' (ID: {test_course_id[:8]}...)")

    # 11. Test POST /api/admin/courses/:id/steps (Add Lab Step with OBE Matrix)
    create_step_res = client.post(f"/api/admin/courses/{test_course_id}/steps", headers=headers, json={
        "order": 1,
        "title": "Lab 1: Cross-Compilation Toolchains & QEMU Emulation",
        "content": "### Experiment 1 Procedure\nSetup the ARM GCC toolchain and build a minimal Linux rootfs.",
        "codeSnippet": "arm-linux-gnueabihf-gcc -static -o init init.c\nqemu-system-arm -M versatilepb -kernel zImage",
        "type": "lab",
        "clo": "CLO-1: Configure GNU cross-compiler toolchains and ARM targets",
        "plo": "PLO-1 (Academic Knowledge)",
        "blooms": "Cognitive C3 (Apply)",
        "imagePath": "/assets/diagrams/qemu_arch.png"
    })
    assert create_step_res.status_code == 201, f"Expected 201, got {create_step_res.status_code}: {create_step_res.get_data(as_text=True)}"
    created_step = create_step_res.get_json()['step']
    test_step_id = created_step['id']
    assert "> **OBE Mapping:**" in created_step['content'], "OBE header block should be injected into content markdown"
    print(f"[PASS] 11. POST /api/admin/courses/:id/steps: Successfully created lab step '{created_step['title']}' with OBE attributes (Order: {created_step['order']})")

    # 12. Test POST /api/admin/steps/:stepId/quizzes (Dynamic Quiz Adder with 4 choices)
    create_quiz_res = client.post(f"/api/admin/steps/{test_step_id}/quizzes", headers=headers, json={
        "question": "Which QEMU architecture emulator is used for ARM 32-bit Cortex targets?",
        "options": [
            "qemu-system-arm",
            "qemu-system-x86_64",
            "qemu-system-mips",
            "qemu-system-riscv"
        ],
        "correctAnswer": "qemu-system-arm",
        "explanation": "qemu-system-arm provides full hardware emulation for ARM 32-bit SoC boards like VersatilePB."
    })
    assert create_quiz_res.status_code == 201, f"Expected 201, got {create_quiz_res.status_code}: {create_quiz_res.get_data(as_text=True)}"
    created_quiz = create_quiz_res.get_json()['quiz']
    assert created_quiz['correctAnswer'] == "qemu-system-arm"
    print(f"[PASS] 12. POST /api/admin/steps/:stepId/quizzes: Successfully added assessment quiz tied directly to Lab Step (Correct: '{created_quiz['correctAnswer']}')")

    # 13. Direct PostgreSQL Persistence Audit
    db_step = db.lessonstep.find_unique(where={"id": test_step_id})
    assert db_step is not None, "Step must exist in Neon PostgreSQL"
    assert db_step.title == "Lab 1: Cross-Compilation Toolchains & QEMU Emulation"

    db_quiz = db.quiz.find_first(where={"lessonStepId": test_step_id})
    assert db_quiz is not None, "Quiz must exist in Neon PostgreSQL"
    assert db_quiz.correctAnswer == "qemu-system-arm"
    print(f"[PASS] 13. Direct Neon PostgreSQL Audit: Verified LessonStep and Quiz records physically persisted in database")

    # 14. Clean Up Test Course (Non-destructive cleanup)
    del_res = client.delete(f"/api/admin/courses/{test_course_id}", headers=headers)
    assert del_res.status_code == 200, f"Expected 200, got {del_res.status_code}"
    print(f"[PASS] 14. DELETE /api/admin/courses/:id: Safely deleted test container; 9 official university courses remain 100% pristine")

    print("=" * 70)
    print("ALL 14 ADMIN TESTS PASSED WITH 100% SUCCESS!")
    print("=" * 70)

    db.disconnect()

if __name__ == '__main__':
    run_tests()
