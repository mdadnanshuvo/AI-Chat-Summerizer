import os
from typing import List, Dict
import google.generativeai as genai
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def generate_summary(chat_text: str, message_stats: Dict[str, int], keywords: List[str]) -> str:
    model = genai.GenerativeModel('gemini')

    prompt = (
        "Analyze the following chat between a user and an AI. "
        "Write one descriptive sentence summarizing what the user was mainly asking about, "
        "in natural English (e.g., 'The user asked mainly about Python and its uses.').\n\n"
        f"{chat_text}"
    )

    try:
        response = model.generate_content(prompt)
        nature_summary = response.text.strip()
    except Exception as e:
        nature_summary = "The user asked about various topics."  # fallback

    summary_lines = [
        "Summary:",
        f"- The conversation had {message_stats.get('total_messages', 0)} exchanges.",
        f"- {nature_summary}",
        f"- Most common keywords: {', '.join(keywords)}."
    ]
    return "\n".join(summary_lines)
