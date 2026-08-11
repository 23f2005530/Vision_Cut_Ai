import hashlib
from pathlib import Path


class CacheKey:
    @staticmethod
    def video_key(video_path: str) -> str:
        path = Path(video_path)

        if not path.exists():
            raise FileNotFoundError(f"Video not found: {video_path}")

        hasher = hashlib.md5()

        with open(path, "rb") as file:
            while chunk := file.read(1024 * 1024):
                hasher.update(chunk)

        return hasher.hexdigest()
