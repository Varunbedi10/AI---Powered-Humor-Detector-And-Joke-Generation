from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

# Configure Gemini API
genai.configure(api_key=)

@app.route('/generate-joke', methods=['POST'])
def generate_joke():
    input_text = request.json.get('theme', '')
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(f"Tell me a joke about {input_text}")
    joke = response.text if response.text else "Couldn't generate a joke."
    return jsonify({"joke": joke})

@app.route('/detect-humor', methods=['POST'])
def detect_humor():
    input_text = request.json.get('text', '')
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(f"Is this text funny? '{input_text}' Answer with just Yes or No.")
    is_humor = "yes" in response.text.lower()
    return jsonify({"is_humor": is_humor})

if __name__ == '__main__':
    app.run(debug=True)
