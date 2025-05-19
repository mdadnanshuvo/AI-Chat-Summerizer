import re
from typing import Dict, List, Tuple


def parse_chat_log(file_path: str) -> Tuple[List[str], List[str]]:
    """
    Parses a chat log file and separates messages from User and AI.

    Returns:
        user_messages: List of messages from the user.
        ai_messages: List of messages from the AI.
    """
    user_messages = []
    ai_messages = []

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line.startswith("User:"):
                user_messages.append(line.replace("User:", "").strip())
            elif line.startswith("AI:"):
                ai_messages.append(line.replace("AI:", "").strip())

    return user_messages, ai_messages
