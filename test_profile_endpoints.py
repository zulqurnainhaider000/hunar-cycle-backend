import os
import sys

backend_root = os.path.abspath(os.path.dirname(__file__))
if backend_root not in sys.path:
    sys.path.insert(0, backend_root)

from dotenv import load_dotenv
load_dotenv(os.path.join(backend_root, '.env'))

from app import create_app
from app.db import db
import jwt
from datetime import timedelta

def run_test():
    app = create_app()
    if not db.is_connected():
        try:
            db.connect(timeout=timedelta(seconds=45))
        except TypeError:
            db.connect()

    client = app.test_client()

    print("=" * 60)
    print("TESTING USER PROFILE ENDPOINTS (LIVE DB)")
    print("=" * 60)

    # Find a test user or first user in DB
    user = db.user.find_first()
    if not user:
        print("[SKIP] No users in database to test with.")
        return

    print(f"Testing with user: {user.username} (ID: {user.id})")

    # Generate token
    secret = os.getenv('JWT_SECRET', 'your_jwt_secret_key_here')
    token = jwt.encode({'user_id': user.id}, secret, algorithm='HS256')
    if isinstance(token, bytes):
        token = token.decode('utf-8')
    headers = {'Authorization': f'Bearer {token}'}

    # 1. Test GET /api/users/me
    res_me = client.get('/api/users/me', headers=headers)
    assert res_me.status_code == 200, f"Expected 200, got {res_me.status_code}: {res_me.get_data(as_text=True)}"
    me_data = res_me.get_json()
    print("[PASS] 1. GET /api/users/me succeeded:")
    print(f"  - Username: {me_data.get('username')}")
    print(f"  - Location: {me_data.get('location')}")
    print(f"  - Headline: {me_data.get('headline')}")
    print(f"  - Avatar: {me_data.get('avatarUrl')}")
    assert 'location' in me_data
    assert 'headline' in me_data

    # 2. Test PUT /api/users/profile
    new_loc = "Lahore, PK"
    new_head = "Full Stack AI Engineer"
    res_update = client.put('/api/users/profile', json={
        "location": new_loc,
        "headline": new_head
    }, headers=headers)
    assert res_update.status_code == 200, f"Expected 200, got {res_update.status_code}: {res_update.get_data(as_text=True)}"
    update_data = res_update.get_json()
    print("[PASS] 2. PUT /api/users/profile succeeded:")
    print(f"  - Message: {update_data.get('message')}")
    print(f"  - Updated Location: {update_data.get('user', {}).get('location')}")
    print(f"  - Updated Headline: {update_data.get('user', {}).get('headline')}")
    assert update_data.get('user', {}).get('location') == new_loc
    assert update_data.get('user', {}).get('headline') == new_head

    # 3. Verify changes persisted in DB via GET /api/users/me
    res_verify = client.get('/api/users/me', headers=headers)
    verify_data = res_verify.get_json()
    assert verify_data.get('location') == new_loc
    assert verify_data.get('headline') == new_head
    print("[PASS] 3. Changes verified in database via GET /api/users/me!")

    print("=" * 60)
    print("ALL USER PROFILE TESTS PASSED (100%)!")
    print("=" * 60)

if __name__ == '__main__':
    run_test()
