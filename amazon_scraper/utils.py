import logging


def setup_logging(log_file="scraper.log", console_output=False):
    handlers = [logging.FileHandler(log_file)]
    if console_output:
        handlers.append(logging.StreamHandler())  # Add console output if enabled

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=handlers,
    )
