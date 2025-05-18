import argparse
from chat_summarizer.parser import parse_chat_log
from chat_summarizer.analyzer import (
    get_message_counts,
    extract_keywords_freq,
    extract_keywords_tfidf
)
from chat_summarizer.summarizer import generate_summary
from chat_summarizer.utils import setup_logger

logger = setup_logger()

def main():
    parser = argparse.ArgumentParser(description="AI Chat Log Summarizer")
    parser.add_argument("--file", type=str, required=True, help="Path to chat log .txt file")
    parser.add_argument("--method", choices=["freq", "tfidf"], default="freq", help="Keyword extraction method")
    args = parser.parse_args()

    user_msgs, ai_msgs = parse_chat_log(args.file)

    # Combine for natural prompt
    chat_text = ""
    for u, a in zip(user_msgs, ai_msgs):
        chat_text += f"User: {u}\nAI: {a}\n"

    stats = get_message_counts(user_msgs, ai_msgs)

    if args.method == "freq":
        keywords = extract_keywords_freq(user_msgs + ai_msgs)
    else:
        keywords = extract_keywords_tfidf(user_msgs + ai_msgs)

    summary = generate_summary(chat_text, stats, keywords)
    logger.info("\n" + summary)

if __name__ == "__main__":
    main()
