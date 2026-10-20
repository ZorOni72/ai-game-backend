import os
from flask import Flask, request, jsonify
from google import genai

app = Flask(__name__)

# Initialize the Gemini client using the Render environment variable
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

@app.route("/", methods=["GET"])
def home():
    return "AI Backend is Online!"

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_prompt = data.get("prompt", "Hello")
        
        # Generate content using the new client syntax
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=user_prompt,
        )
        return jsonify({"reply": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
