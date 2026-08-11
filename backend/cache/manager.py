import json
from pathlib import Path


class CacheManager:
    """
    Handles JSON-based caching of expensive AI results.
    """

    BASE_DIR = Path("storage/cache")

    @classmethod
    def _path(cls, category: str, key: str) -> Path:
        directory = cls.BASE_DIR / category
        directory.mkdir(parents=True, exist_ok=True)

        return directory / f"{key}.json"

    @classmethod
    def save(cls, category: str, key: str, data):
        path = cls._path(category, key)

        with open(path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    @classmethod
    def load(cls, category: str, key: str):
        path = cls._path(category, key)

        if not path.exists():
            return None

        with open(path, encoding="utf-8") as file:
            return json.load(file)

    @classmethod
    def exists(cls, category: str, key: str) -> bool:
        return cls._path(category, key).exists()
