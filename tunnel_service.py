import os
import re
import sys
import subprocess
import time

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

BACKEND_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BACKEND_DIR)
FRONTEND_DIR = os.path.join(ROOT_DIR, 'frontend')
CLOUDFLARED_BIN = os.path.join(BACKEND_DIR, 'bin', 'cloudflared.exe')

def update_frontend_configs(public_url: str):
    print("\n" + "=" * 65)
    print(f"[TUNNEL] PUBLIC HTTPS TUNNEL LIVE: {public_url}")
    print("=" * 65 + "\n")

    # 1. Update frontend/.env
    env_file = os.path.join(FRONTEND_DIR, '.env')
    try:
        with open(env_file, 'w', encoding='utf-8') as f:
            f.write(f"EXPO_PUBLIC_API_URL={public_url}\n")
        print(f"[SUCCESS] Updated {env_file} -> {public_url}")
    except Exception as e:
        print(f"[ERROR] Failed to update {env_file}: {e}")

    # 2. Update frontend/eas.json
    eas_file = os.path.join(FRONTEND_DIR, 'eas.json')
    try:
        if os.path.exists(eas_file):
            with open(eas_file, 'r', encoding='utf-8') as f:
                content = f.read()
            new_content = re.sub(
                r'"EXPO_PUBLIC_API_URL":\s*"[^"]+"',
                f'"EXPO_PUBLIC_API_URL": "{public_url}"',
                content
            )
            with open(eas_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"[SUCCESS] Updated {eas_file} -> {public_url}")
    except Exception as e:
        print(f"[ERROR] Failed to update {eas_file}: {e}")

    # 3. Update frontend/app.json
    app_json = os.path.join(FRONTEND_DIR, 'app.json')
    try:
        if os.path.exists(app_json):
            with open(app_json, 'r', encoding='utf-8') as f:
                content = f.read()
            new_content = re.sub(
                r'"apiUrl":\s*"[^"]+"',
                f'"apiUrl": "{public_url}"',
                content
            )
            with open(app_json, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"[SUCCESS] Updated {app_json} extra.apiUrl -> {public_url}")
    except Exception as e:
        print(f"[ERROR] Failed to update {app_json}: {e}")

    # 4. Update frontend/src/config/api.ts fallback
    api_ts = os.path.join(FRONTEND_DIR, 'src', 'config', 'api.ts')
    try:
        if os.path.exists(api_ts):
            with open(api_ts, 'r', encoding='utf-8') as f:
                content = f.read()
            new_content = re.sub(
                r"return '(http|https)://[^']+';",
                f"return '{public_url}';",
                content
            )
            with open(api_ts, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"[SUCCESS] Updated fallback in {api_ts} -> {public_url}")
    except Exception as e:
        print(f"[ERROR] Failed to update {api_ts}: {e}")

    print("\n[READY] All frontend files configured to point to public tunnel!")


def run_ngrok(port=5000):
    try:
        from pyngrok import ngrok
        token = os.environ.get("NGROK_AUTHTOKEN")
        if token:
            ngrok.set_auth_token(token)
        tunnel = ngrok.connect(port)
        public_url = tunnel.public_url
        update_frontend_configs(public_url)
        print("Press Ctrl+C to terminate ngrok tunnel...")
        ngrok_process = ngrok.get_ngrok_process()
        ngrok_process.proc.wait()
    except KeyboardInterrupt:
        print("\nStopping ngrok...")
    except Exception as e:
        print(f"Error starting ngrok: {e}")


def run_tunnel(port=5000, provider='cloudflare'):
    if provider == 'ngrok':
        return run_ngrok(port)

    if not os.path.exists(CLOUDFLARED_BIN):
        print(f"Error: {CLOUDFLARED_BIN} not found.")
        sys.exit(1)

    print(f"Starting Cloudflare Quick Tunnel forwarding to http://127.0.0.1:{port}...")
    cmd = [CLOUDFLARED_BIN, 'tunnel', '--url', f'http://127.0.0.1:{port}']

    process = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1,
        encoding='utf-8',
        errors='replace'
    )

    tunnel_url_found = False
    url_pattern = re.compile(r'https://[a-zA-Z0-9-]+\.trycloudflare\.com')

    try:
        for line in process.stdout:
            sys.stdout.write(line)
            sys.stdout.flush()

            if not tunnel_url_found:
                match = url_pattern.search(line)
                if match:
                    public_url = match.group(0)
                    tunnel_url_found = True
                    update_frontend_configs(public_url)
    except KeyboardInterrupt:
        print("\nStopping tunnel...")
        process.terminate()
        process.wait()

if __name__ == '__main__':
    port = 5000
    provider = 'cloudflare'
    for arg in sys.argv[1:]:
        if arg.isdigit():
            port = int(arg)
        elif arg in ('--ngrok', 'ngrok'):
            provider = 'ngrok'
        elif arg in ('--cloudflare', 'cloudflare'):
            provider = 'cloudflare'
    run_tunnel(port, provider)
