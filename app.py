import os
import traceback
from flask import Flask, request, jsonify
from google import genai

app = Flask(__name__)

# Initialize the modern Gemini client
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

@app.route("/", methods=["GET"])
def home():
    return "AI Backend is Online!"

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json() or {}
        user_prompt = data.get("prompt", "Hello")
        
        # Use the modern client model call
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=user_prompt,
        )
        return jsonify({"reply": response.text})
    except Exception as e:
        print("ERROR IN CHAT:", traceback.format_exc())
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
