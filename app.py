import asyncio
import os
from dotenv import load_dotenv
load_dotenv()

from flask import Flask, jsonify
from flask_cors import CORS
# Prisma Client setup
from app.db import db
from app.sockets import socketio

# Import the modular blueprints
from app.routes.onboarding import onboarding_bp
from app.routes.gigs import gigs_bp
from app.routes.dojos import dojos_bp
from app.routes.lessons import lessons_bp, courses_bp
from app.routes.users import users_bp, user_bp
from app.routes.zen import zen_bp
from app.routes.auth import auth_bp
from app.routes.hub import hub_bp
# We will assume learn, matches, etc. are still in __init__
from app.routes import learn_bp, matches_bp

def create_app():
    app = Flask(__name__)
    
    # 1. Initialize CORS to allow requests from the React Native app
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    
    # 2. Register API routing blueprints
    app.register_blueprint(onboarding_bp)
    app.register_blueprint(gigs_bp)
    app.register_blueprint(dojos_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(learn_bp)
    app.register_blueprint(matches_bp)
    app.register_blueprint(hub_bp)
    app.register_blueprint(zen_bp)
    app.register_blueprint(lessons_bp)
    app.register_blueprint(courses_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(user_bp)
    
    # Initialize SocketIO with the app
    socketio.init_app(app)
    
    # Root status endpoint
    @app.route('/')
    def root():
        return jsonify({
            "status": "online",
            "service": "HunarCircle API",
            "version": "1.0.0",
            "health": "/api/health"
        }), 200

    # Health Check with live Database diagnosis
    @app.route('/api/health')
    def health_check():
        db_status = "unknown"
        db_err = None
        user_count = 0
        try:
            if not db.is_connected():
                db.connect()
            user_count = db.user.count()
            db_status = f"connected (users: {user_count})"
        except Exception as e:
            db_status = "error"
            db_err = str(e)
            print(f"[Health Check DB Error] {e}", flush=True)

        return jsonify({
            "status": "healthy" if db_status.startswith("connected") else "db_issue", 
            "service": "HunarCircle API",
            "database": db_status,
            "db_error": db_err,
            "user_count": user_count,
            "message": "Ready to serve Gigs and Dojos!"
        }), 200

    # Auto-migration endpoint for remote cloud database setup
    @app.route('/api/admin/push-db', methods=['GET', 'POST'])
    def admin_push_db():
        import subprocess, sys
        try:
            res = subprocess.run([sys.executable, "-m", "prisma", "db", "push", "--accept-data-loss"], capture_output=True, text=True)
            return jsonify({
                "success": True,
                "stdout": res.stdout,
                "stderr": res.stderr
            }), 200
        except Exception as e:
            return jsonify({"success": False, "error": str(e)}), 500

    return app

app = create_app()

_schema_migrated = False

def ensure_db_connected():
    global _schema_migrated
    import subprocess, sys
    try:
        if not db.is_connected():
            db.connect()
            print("[Prisma] Database connected successfully.", flush=True)

        if not _schema_migrated:
            try:
                db.user.count()
                _schema_migrated = True
            except Exception as table_err:
                print(f"[Prisma] Tables not initialized ({table_err}). Running prisma db push...", flush=True)
                push_res = subprocess.run([sys.executable, "-m", "prisma", "db", "push", "--accept-data-loss"], capture_output=True, text=True)
                print(f"[Prisma db push] {push_res.stdout} {push_res.stderr}", flush=True)
                _schema_migrated = True
    except Exception as e:
        print(f"[Prisma] Database connection status: {e}", flush=True)

# Connect Prisma Client synchronously
ensure_db_connected()

@app.before_request
def before_request():
    ensure_db_connected()

def free_port_if_in_use(port_num):
    """
    Checks if the desired port is occupied (e.g. by dangling python or node tasks).
    Gracefully identifies and terminates the blocking process so the server can bind cleanly.
    """
    import socket
    import subprocess
    import time

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        in_use = (s.connect_ex(('127.0.0.1', port_num)) == 0)

    if not in_use:
        return

    print(f"\n[PORT AUTO-RESOLVER] Port {port_num} is currently in use. Clearing conflicting process...")
    try:
        # Use netstat to find owning PID
        cmd = f'netstat -ano | findstr :{port_num}'
        out = subprocess.check_output(cmd, shell=True).decode('utf-8', errors='ignore')
        current_pid = str(os.getpid())
        pids = set()
        for line in out.strip().splitlines():
            parts = line.split()
            if len(parts) >= 5 and "LISTENING" in parts:
                pid = parts[-1]
                if pid != current_pid and pid != "0":
                    pids.add(pid)

        for pid in pids:
            print(f"[PORT AUTO-RESOLVER] Terminating process PID {pid} occupying port {port_num}...")
            subprocess.run(f'taskkill /F /PID {pid}', shell=True, capture_output=True)

        time.sleep(1)
        print(f"[PORT AUTO-RESOLVER] Port {port_num} is now freed and ready!\n")
    except Exception as e:
        print(f"[PORT AUTO-RESOLVER] Could not auto-clear port: {e}")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_DEBUG', 'False').lower() in ('true', '1')
    
    # Auto-resolve port conflict if port is occupied
    free_port_if_in_use(port)

    try:
        # Start the server on dynamic port using socketio to support WebSockets
        socketio.run(app, host='0.0.0.0', port=port, debug=debug)
    except OSError as e:
        if "10048" in str(e):
            print(f"\n[PORT CONFLICT] Port {port} locked by Windows. Force clearing and retrying...")
            free_port_if_in_use(port)
            socketio.run(app, host='0.0.0.0', port=port, debug=debug)
        else:
            raise

