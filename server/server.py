from flask import Flask, jsonify, request
from openai import OpenAI
import os

app = Flask(__name__)

openai = OpenAI(os.environ.get('OPENAI_API_KEY'))

@app.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'Hello from Intellichat!'})

@app.route('/', methods=['POST'])
def generate_response():
    prompt = request.json.get('prompt')
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0,
        max_tokens=3000,
        top_p=1,
        frequency_penalty=0.5,
        presence_penalty=0
    )
    return jsonify({'bot': response.choices[0].text})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
