import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")
URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"

headers = {
    "Content-Type": "application/json"
}

data = {
    "contents": [
        {
            "parts": [
                {"text": "Explain how AI works"}
            ]
        }
    ]
}


def test_gemini_api():
    response = requests.post(URL, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        print("API Response:")
        print(json.dumps(response.json(), indent=2))
    else:
        print(f"Failed with status code {response.status_code}")
        print(response.text)


if __name__ == "__main__":
    test_gemini_api()
