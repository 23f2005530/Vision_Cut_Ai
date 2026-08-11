from pathlib import Path

from backend.assets.extractor import MetadataExtractor
from backend.assets.thumbnail_generator import ThumbnailGenerator
from backend.models.asset import AssetModel


class AssetManager:
    """
    Handles imported assets.
    """

    SUPPORTED_VIDEO = {
        ".mp4",
        ".mov",
        ".mkv",
        ".avi",
        ".webm",
    }

    def import_asset(self, file_path: str):
        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(file_path)

        if path.suffix.lower() not in self.SUPPORTED_VIDEO:
            raise ValueError("Unsupported format")

        metadata = MetadataExtractor.extract(path)

        thumbnail = ThumbnailGenerator.generate(str(path))

        return AssetModel(
            filename=path.name,
            filepath=str(path.resolve()),
            media_type="video",
            file_size=path.stat().st_size,
            duration=metadata["duration"],
            width=metadata["width"],
            height=metadata["height"],
            fps=metadata["fps"],
            thumbnail_path=thumbnail,
        )
