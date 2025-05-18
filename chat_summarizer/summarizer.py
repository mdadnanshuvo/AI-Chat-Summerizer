from typing import List, Dict

def generate_summary(message_stats: Dict[str, int], keywords: List[str]) -> str:
    summary_lines = [
        f"Summary:",
        f"- The conversation had {message_stats['total_messages']} exchanges.",
        f"- User sent {message_stats['user_messages']} messages. AI sent {message_stats['ai_messages']} messages.",
        f"- Most common keywords: {', '.join(keywords)}"
    ]
    return "\n".join(summary_lines)
