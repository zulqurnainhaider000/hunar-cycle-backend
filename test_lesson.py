import requests

BASE_URL = 'http://192.168.18.62:5000/api'

# 1. Register a test user
print("Registering test user...")
res = requests.post(f"{BASE_URL}/auth/register", json={
    "username": "test_error_user2",
    "email": "test_error2@example.com",
    "password": "password123"
})
if res.status_code == 201:
    token = res.json()['token']
else:
    # Try login
    res = requests.post(f"{BASE_URL}/auth/login", json={
        "email": "test_error2@example.com",
        "password": "password123"
    })
    token = res.json()['token']

print(f"Token: {token[:20]}...")

# 2. Get lessons
print("Fetching lessons...")
res = requests.get(f"{BASE_URL}/lessons", headers={"Authorization": f"Bearer {token}"})
lessons = res.json()
lesson_id = lessons[0]['id']
print(f"Got lesson ID: {lesson_id}")

# 3. Get specific lesson details (THIS FAILS WITH 401 in app!)
print(f"Fetching lesson details for {lesson_id}...")
res = requests.get(f"{BASE_URL}/lessons/{lesson_id}", headers={"Authorization": f"Bearer {token}"})
print(f"Status Code: {res.status_code}")
print(f"Response: {res.text}")
