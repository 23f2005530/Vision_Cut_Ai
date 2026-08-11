import json
from pathlib import Path

from backend.analysis.models import AnalysisModel


class AnalysisSerializer:
    FILE_NAME = "analysis.json"

    @classmethod
    def save(
        cls,
        analysis: AnalysisModel,
        workspace: str,
    ):
        file = Path(workspace) / cls.FILE_NAME

        with open(file, "w", encoding="utf-8") as f:
            json.dump(
                analysis.model_dump(mode="json"),
                f,
                indent=4,
            )

    @classmethod
    def load(
        cls,
        workspace: str,
    ):
        file = Path(workspace) / cls.FILE_NAME

        with open(file, encoding="utf-8") as f:
            data = json.load(f)

        return AnalysisModel.model_validate(data)
