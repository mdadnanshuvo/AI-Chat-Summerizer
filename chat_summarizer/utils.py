import logging

def setup_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    # Clear previous handlers (if rerun in some environments)
    if logger.hasHandlers():
        logger.handlers.clear()

    console_handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)

    return logger
