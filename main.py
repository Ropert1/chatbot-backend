from flask import Flask, request, jsonify, session
from flask_cors import CORS
import os
import random

app = Flask(__name__)
app.secret_key = 'super-secret-key'
CORS(app, supports_credentials=True)

# ------------------------------------
# Englische Challenges & Übungen 🎉
# ------------------------------------
english_challenges = [
    "Translate this into English: 'Ich habe einen hungrigen Hamster.' 🐹",
    "Fill in the blank: 'I _____ to learn English every day!' 💪",
    "What's the English word for 'Kühlschrank'? Hint: It's cool 😎",
    "Unscramble this word: 'gnelish' 🧠",
    "Say this tongue twister three times fast: 'She sells sea shells by the sea shore.' 🌊",
    "What does 'awesome' mean in German? And how would you use it in a sentence?",
    "Can you name 3 animals in English that start with the letter 'C'? 🐱🦀🐄",
    "What's the past tense of 'go'? And can you use it in a sentence?",
    "Which of these is NOT an English word: 'banana', 'computer', 'schmetterling'? 🧐",
    "Try to say this in English: 'Ich lerne Englisch, weil es Spaß macht!' 🎯"
]

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
        response = "Hallo! Bereit für eine lustige Englisch-Übung? 😄"
        challenge = random.choice(english_challenges)
        response += f"\n\n👉 {challenge}"
    elif message == "mehr":
        challenge = random.choice(english_challenges)
        response = f"Hier kommt noch eine Übung für dich:\n\n👉 {challenge}"
    elif "hilfe" in message:
        response = (
            "Keine Sorge! Du kannst einfach 'mehr' schreiben, um eine neue Übung zu bekommen. "
            "Oder frag mich etwas auf Englisch – ich helfe dir gerne! 💬"
        )
    else:
        response = (
            "Ich verstehe dich nicht ganz. Sag 'hallo' für den Start oder 'mehr' für eine neue Englisch-Challenge! 🎓"
        )

    return jsonify({"response": response})

# -------------------------------
# Lokaler Start (Render nutzt gunicorn)
# -------------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


