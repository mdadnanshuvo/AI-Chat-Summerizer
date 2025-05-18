import logging
from chat_summarizer.parser import parse_chat_log

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def main():
    file_path = "data/sample_chat.txt"
    user_msgs, ai_msgs = parse_chat_log(file_path)

    logging.info("User Messages:")
    for msg in user_msgs:
        logging.info(f"- {msg}")

    logging.info("AI Messages:")
    for msg in ai_msgs:
        logging.info(f"- {msg}")


if __name__ == "__main__":
    main()
