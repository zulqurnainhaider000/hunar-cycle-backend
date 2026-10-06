import importlib.util
spec = importlib.util.spec_from_file_location("main_app", "app.py")
main_app = importlib.util.module_from_spec(spec)
spec.loader.exec_module(main_app)

from app.db import db
import jwt, datetime

client = main_app.app.test_client()

user = db.user.find_first()
token = jwt.encode({'user_id': user.id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(days=30)}, 'hunarcircle_super_secret_jwt_key_2026', algorithm='HS256')

res = client.get('/api/lessons/e937d93d-5471-4610-8a8e-34d3ecfbe89a', headers={'Authorization': 'Bearer ' + token})
print(res.status_code)
print(res.get_json())
