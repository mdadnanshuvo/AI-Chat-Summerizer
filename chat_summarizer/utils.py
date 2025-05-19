import logging
import os

from dotenv import load_dotenv


def setup_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    if logger.hasHandlers():
        logger.handlers.clear()

    console_handler = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger


def load_api_config():
    """Loads environment variables and returns API key, URL, and headers."""
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY not found in .env file")

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}"
    headers = {"Content-Type": "application/json"}
    return api_key, url, headers


def build_prompt(chat_text: str, stats: dict, keywords: list) -> str:
    """Builds a prompt string for the summarization request."""
    return (
        "You are a helpful summarizer AI.\n\n"
        f"Chat conversation:\n{chat_text}\n\n"
        f"Stats:\n- Total Exchanges: {stats.get('total_exchanges')}\n"
        f"- User Messages: {stats.get('user_messages')}\n"
        f"- AI Messages: {stats.get('ai_messages')}\n\n"
        f"Keywords: {', '.join(keywords)}\n\n"
        "Please return a clear summary in this format:\n"
        "Summary:\n"
        "- The conversation had <X> exchanges.\n"
        "- The user mainly asked about <topics>.\n"
        "- Most common keywords: <list of keywords>."
    )
