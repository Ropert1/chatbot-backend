from flask import Flask, request, jsonify, session
from flask_cors import CORS
import os

app = Flask(__name__)
app.secret_key = 'super-secret-key'
CORS(app, supports_credentials=True)

# -------------------------------
# Root-Route für Browser-Test
# -------------------------------
@app.route("/", methods=["GET"])
def index():
    return "✅ Chatbot läuft – schicke eine POST-Anfrage an /chat"

# -------------------------------
# Chat-Route
# -------------------------------
@app.route("/chat", methods=["POST"])
def chat():
    message = request.json.get("message", "").strip().lower()

    if message == "hallo":
        response = "Hallo!"
    else:
        response = "Er versteht mich nicht."

    return jsonify({"response": response})

# -------------------------------
# Lokaler Start (Render nutzt gunicorn)
# -------------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
