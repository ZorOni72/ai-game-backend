import os
import traceback
from flask import Flask, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Configure Gemini API key from Render environment variables
api_key = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=api_key)

@app.route("/", methods=["GET"])
def home():
    return "AI Backend is Online!"

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json() or {}
        user_prompt = data.get("prompt", "Hello")
        
        # Use the standard generative model
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(user_prompt)
        
        return jsonify({"reply": response.text})
    except Exception as e:
        # Print full error details to Render logs if something fails
        print("ERROR IN CHAT:", traceback.format_exc())
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
