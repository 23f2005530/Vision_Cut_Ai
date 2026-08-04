from backend.logging import get_logger


def test_logger_creation():
    logger = get_logger("tests")

    logger.info("Logger test successful")

    assert logger is not None
