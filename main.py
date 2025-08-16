from flask import Flask, request, jsonify, session
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = 'super-secret-key'
CORS(app, supports_credentials=True)

@app.route('/chat', methods=['POST'])
def chat():
    message = request.json.get('message', '').strip().lower()

    if message == "hallo":
        response = "Hallo!"
    else:
        response = "Er versteht mich nicht."

    return jsonify({'response': response})

if __name__ == "__main__":
    app.run()