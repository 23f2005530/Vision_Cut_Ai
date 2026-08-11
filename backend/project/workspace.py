from pathlib import Path


class Workspace:
    PROJECT_FOLDERS = [
        "assets",
        "analysis",
        "timeline",
        "exports",
        "cache",
        "logs",
        "thumbnails",
        "proxies",
        "autosave",
    ]

    def __init__(self, root: Path):
        self.root = root

    def create(self) -> None:
        self.root.mkdir(parents=True, exist_ok=True)

        for folder in self.PROJECT_FOLDERS:
            (self.root / folder).mkdir(exist_ok=True)
