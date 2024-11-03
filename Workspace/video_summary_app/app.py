from flask import Flask, render_template, request, jsonify
import requests
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

app = Flask(__name__)

# Define your AI model API URL and key
AI_API_URL = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro-latest:generateContent?key=Api-key'

@app.route('/')
def index():
    return render_template('index.html')

def get_video_transcript(video_id, languages=None):
    if languages is None:
        languages = ['en', 'ar', 'zh', 'fr', 'es', 'de', 'nl', 'it', 'pt', 'ru', 'ja', 'ko', 'hi', 'tr', 'pl', 'sv', 'da', 'fi', 'no', 'el', 'he', 'th', 'hu', 'cs', 'ro', 'sk', 'bg', 'vi', 'id', 'ms', 'sl', 'lv', 'lt', 'et', 'is', 'mt', 'tl', 'sw']

    try:
        # Get the transcript
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=languages)
        formatter = TextFormatter()
        formatted_transcript = formatter.format_transcript(transcript)
        return formatted_transcript
    except Exception as e:
        return f"Could not retrieve transcript: {e}"

def summarize_transcript(transcript):
    payload = {
        "contents": [
            {
                "parts": [{"text": f"Summarize this transcript: \"{transcript}\""}]
            }
        ]
    }
    response = requests.post(url=AI_API_URL, json=payload)
    
    if response.ok:
        return response.json()["candidates"][0]["content"]["parts"][0]["text"]
    else:
        return "Error summarizing the transcript."

@app.route('/summary', methods=['POST'])
def summary():
    video_id = request.json.get('videoId')
    transcript = get_video_transcript(video_id)
    
    if "Could not retrieve transcript" not in transcript:
        summary = summarize_transcript(transcript)
        return jsonify(summary=summary)
    else:
        return jsonify(summary=None)

if __name__ == '__main__':
    app.run(port=1111)
