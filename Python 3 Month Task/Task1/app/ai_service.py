import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

API_URL = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}


def get_ai_response(message):

    payload = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
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
            timeout=20
        )

        response.raise_for_status()

        data = response.json()

        return data["choices"][0]["message"]["content"]

    except Exception as e:

        return f"Error: {str(e)}"