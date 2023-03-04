import json
import requests
from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request

app = Flask(__name__)

def generate_text(prompt):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer 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'
    }
    data = {
        "model": "text-davinci-003",
        "prompt": prompt,
        "max_tokens": 4000,
        "temperature": 1.0
    }
    response = requests.post('https://api.openai.com/v1/completions', headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        response_data = response.json()
        return response_data["choices"][0]["text"]
    else:
        return None

@app.route("/whatsapp", methods=['POST'])
def incoming_message():
    # Get incoming message
    incoming_msg = request.values.get('Body', '').lower()
    response = MessagingResponse()
    
    # Generate response from OpenAI API
    ai_response = generate_text(incoming_msg)
    
    # Send response to WhatsApp group
    response.message(ai_response)
    return str(response)

if __name__ == "__main__":
    app.run(debug=True)
