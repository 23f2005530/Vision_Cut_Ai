import subprocess
from pathlib import Path


class ThumbnailGenerator:
    """
    Generates thumbnail images from videos.
    """

    OUTPUT_DIR = Path("storage/thumbnails")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    @classmethod
    def generate(cls, video_path: str) -> str:
        video = Path(video_path)

        output = cls.OUTPUT_DIR / f"{video.stem}.jpg"

        command = [
            "ffmpeg",
            "-y",
            "-i",
            str(video),
            "-ss",
            "00:00:01",
            "-vframes",
            "1",
            str(output),
        ]

        subprocess.run(
            command,
            capture_output=True,
            check=True,
        )

        return str(output.resolve())
