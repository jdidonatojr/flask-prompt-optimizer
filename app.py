import os
import openai
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/optimize-prompt', methods=['POST'])
def optimize_prompt():
    try:
        data = request.json
        user_prompt = data.get("prompt", "")
        
        # Use the new API method to create a completion
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Optimize the user's prompt for clarity and effectiveness."},
                {"role": "user", "content": user_prompt}
            ],
            temperature=1,
            max_tokens=2048
        )
        optimized_prompt = response['choices'][0]['message']['content']
        return jsonify({"optimized_prompt": optimized_prompt})

    except Exception as e:
        print(f"Error occurred: {e}")
        return jsonify({"error": "An internal error occurred"}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
