import os
from flask import Flask, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Load Gemini API Key from Render environment variables
api_key = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

@app.route("/", methods=["GET"])
def home():
    return "AI Backend is Online!"

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_prompt = data.get("prompt", "Hello")
        
        # Generate response from Gemini AI
        response = model.generate_content(user_prompt)
        return jsonify({"reply": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
