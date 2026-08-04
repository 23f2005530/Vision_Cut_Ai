import logging


class VisionFormatter(logging.Formatter):
    """Custom formatter for Vision Cut AI."""

    FORMAT = "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"

    def __init__(self):
        super().__init__(
            fmt=self.FORMAT,
            datefmt="%Y-%m-%d %H:%M:%S",
        )
