from flask import Flask, jsonify, request
import openai
import os

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/')
def home():
    return "Welcome to the Prompt Optimizer API!"

@app.route('/optimize-prompt', methods=['POST'])
def optimize_prompt():
    data = request.json
    user_prompt = data.get("prompt", "")
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

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

