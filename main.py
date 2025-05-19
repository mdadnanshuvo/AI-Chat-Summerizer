import argparse
import os

from chat_summarizer.analyzer import (
    extract_keywords_freq,
    extract_keywords_tfidf,
    get_message_counts,
)
from chat_summarizer.parser import parse_chat_log
from chat_summarizer.summarizer import generate_summary
from chat_summarizer.utils import setup_logger

logger = setup_logger()


def summarize_file(file_path: str, method: str):
    """Summarize a single chat log file."""
    user_msgs, ai_msgs = parse_chat_log(file_path)

    # Combine messages for prompt
    chat_text = "\n".join([f"User: {u}\nAI: {a}" for u, a in zip(user_msgs, ai_msgs)])
    stats = get_message_counts(user_msgs, ai_msgs)

    if method == "freq":
        keywords = extract_keywords_freq(user_msgs + ai_msgs)
    else:
        keywords = extract_keywords_tfidf(user_msgs + ai_msgs)

    logger.info(f"\n📄 Summarizing: {file_path}")
    summary = generate_summary(chat_text, stats, keywords)
    logger.info(summary + "\n")


def main():
    parser = argparse.ArgumentParser(description="AI Chat Log Summarizer")
    parser.add_argument("--file", type=str, help="Path to a single chat log .txt file")
    parser.add_argument("--folder", type=str, help="Path to a folder containing multiple .txt files")
    parser.add_argument("--method", choices=["freq", "tfidf"], default="freq", help="Keyword extraction method")
    args = parser.parse_args()

    if args.file:
        summarize_file(args.file, args.method)
    elif args.folder:
        for filename in os.listdir(args.folder):
            if filename.endswith(".txt"):
                file_path = os.path.join(args.folder, filename)
                summarize_file(file_path, args.method)
    else:
        parser.error("You must specify either --file or --folder")


if __name__ == "__main__":
    main()
