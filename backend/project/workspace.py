from pathlib import Path


class Workspace:
    """
    Handles Vision Cut AI workspace directories.
    """

    def __init__(self, root: Path):
        self.root = root

    def create(self) -> None:
        folders = [
            "assets",
            "analysis",
            "timeline",
            "exports",
            "cache",
            "logs",
        ]

        self.root.mkdir(parents=True, exist_ok=True)

        for folder in folders:
            (self.root / folder).mkdir(exist_ok=True)
