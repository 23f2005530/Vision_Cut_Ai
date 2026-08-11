import json
import subprocess
from pathlib import Path


class MetadataExtractor:
    """
    Extracts metadata from media files using FFprobe.
    """

    @staticmethod
    def extract(file_path: Path) -> dict:
        """
        Extract metadata from a media file.

        Returns:
            dict containing duration, width, height, fps and bitrate.
        """

        if not file_path.exists():
            raise FileNotFoundError(file_path)

        command = [
            "ffprobe",
            "-v",
            "quiet",
            "-print_format",
            "json",
            "-show_format",
            "-show_streams",
            str(file_path),
        ]

        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True,
        )

        metadata = json.loads(result.stdout)

        video_stream = next(
            (stream for stream in metadata["streams"] if stream["codec_type"] == "video"),
            None,
        )

        if video_stream is None:
            raise ValueError("No video stream found.")

        fps_num, fps_den = map(
            float,
            video_stream["r_frame_rate"].split("/"),
        )

        fps = fps_num / fps_den if fps_den else 0.0

        return {
            "duration": float(metadata["format"].get("duration", 0)),
            "width": int(video_stream.get("width", 0)),
            "height": int(video_stream.get("height", 0)),
            "fps": fps,
            "bitrate": int(metadata["format"].get("bit_rate", 0)),
        }
