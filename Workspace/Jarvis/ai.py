from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Define the URL and API key for the AI model
API_URL = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro-latest:generateContent?key=AIzaSyC4QESyWZwQ-XPBwr2KXC5iwO5l0rP40pU'

# Initialize chat history with a system prompt
chat_history = [
    {
        "role": "system",
        "text": "You are Jarvis, an advanced AI assistant specializing in engineering, home automation, cybersecurity, and task management. Your goal is to assist users with complex tasks, providing real-time solutions in any language. Maintain a calm, articulate, and professional demeanor throughout the conversation."
    }
]

# Function to add a user query to chat history
def add_user_query(query):
    chat_history.append({"role": "user", "text": query})

# Function to add the assistant's response to chat history
def add_assistant_response(response):
    chat_history.append({"role": "assistant", "text": response})

# Function to generate a response from the assistant
def generate_response(user_query):
    # Update chat history with the user query
    add_user_query(user_query)

    # Prepare the payload for the API request
    payload = {
        "contents": [
            {
                "parts": [{"text": message["text"]} for message in chat_history]
            }
        ]
    }

    # Send a POST request to the AI model
    response = requests.post(url=API_URL, json=payload)

    # Handle the response from the assistant
    if response.status_code == 200:
        assistant_response = response.json()["candidates"][0]["content"]["parts"][0]["text"]
        add_assistant_response(assistant_response)
        return assistant_response
    else:
        return f"Error {response.status_code}: {response.text}"

# Flask routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_query = request.json.get("query")
    assistant_response = generate_response(user_query)
    return jsonify({"response": assistant_response})

# Run the Flask app
if __name__ == '__main__':
    app.run(port=2222)
