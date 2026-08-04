import logging
from pathlib import Path

from backend.logging.formatter import VisionFormatter

LOG_DIR = Path("storage/logs")
LOG_DIR.mkdir(parents=True, exist_ok=True)

LOG_FILE = LOG_DIR / "vision_cut.log"


def get_logger(name: str):
    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    formatter = VisionFormatter()

    file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")

    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
