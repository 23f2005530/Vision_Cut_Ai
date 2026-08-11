import json
from pathlib import Path

from backend.models.timeline import TimelineModel


class TimelineSerializer:
    """
    Saves and loads timeline files.
    """

    FILE_NAME = "timeline.json"

    @classmethod
    def save(cls, timeline: TimelineModel, workspace: str) -> None:
        file_path = Path(workspace) / cls.FILE_NAME

        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(
                timeline.model_dump(mode="json"),
                file,
                indent=4,
            )

    @classmethod
    def load(cls, workspace: str) -> TimelineModel:
        file_path = Path(workspace) / cls.FILE_NAME

        with open(file_path, encoding="utf-8") as file:
            data = json.load(file)

        timeline: TimelineModel = TimelineModel.model_validate(data)

        return timeline
