import json
import requests
from chat_summarizer.utils import setup_logger, load_api_config, build_prompt

# Setup
logger = setup_logger()
_, API_URL, HEADERS = load_api_config()


def call_gemini_api(prompt: str) -> str:
    """Sends a request to the Gemini API and returns the response text."""
    payload = {
        "contents": [
            {
                "parts": [{"text": prompt}]
            }
        ]
    }

    try:
        response = requests.post(API_URL, headers=HEADERS, data=json.dumps(payload))
        response.raise_for_status()

        data = response.json()
        summary = data.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "")
        return summary.strip()

    except requests.exceptions.RequestException as e:
        logger.error(f"Request to Gemini API failed: {e}")
        raise

    except (KeyError, IndexError, TypeError) as e:
        logger.error(f"Unexpected response structure: {e}")
        logger.debug("Full response: %s", json.dumps(response.json(), indent=2))
        raise


def generate_summary(chat_text: str, message_stats: dict, keywords: list) -> str:
    """Generates a summary using Gemini based on chat, stats, and keywords."""
    logger.info("Generating prompt for Gemini API...")
    prompt = build_prompt(chat_text, message_stats, keywords)
    logger.info("Sending prompt to Gemini API...")
    return call_gemini_api(prompt)
