import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

API_URL = "https://openrouter.ai/api/v1/chat/completions"

def get_ai_response(message):

    if not API_KEY:
        return "OpenRouter API key not configured."

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are a Career Guidance Assistant. "
                    "Help users with careers, internships, learning paths, "
                    "skills, projects and job preparation."
                )
            },
            {
                "role": "user",
                "content": message
            }
        ]
    }

    try:

        response = requests.post(
            API_URL,
            headers=headers,
            json=payload,
            timeout=30
        )

        data = response.json()

        return data["choices"][0]["message"]["content"]

    except Exception as e:

        return f"AI Error: {str(e)}"