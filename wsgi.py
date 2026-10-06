import os
import sys
from dotenv import load_dotenv

# Ensure backend root is in Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
load_dotenv()

# Import the actual main app from app.py
import importlib.util
_spec = importlib.util.spec_from_file_location("hunar_app", os.path.join(os.path.dirname(os.path.abspath(__file__)), "app.py"))
_hunar_app = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_hunar_app)

app = _hunar_app.app
socketio = _hunar_app.socketio

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_DEBUG', 'False').lower() in ('true', '1')
    if hasattr(_hunar_app, 'free_port_if_in_use'):
        _hunar_app.free_port_if_in_use(port)
    try:
        socketio.run(app, host='0.0.0.0', port=port, debug=debug)
    except OSError as e:
        if "10048" in str(e) and hasattr(_hunar_app, 'free_port_if_in_use'):
            _hunar_app.free_port_if_in_use(port)
            socketio.run(app, host='0.0.0.0', port=port, debug=debug)
        else:
            raise

