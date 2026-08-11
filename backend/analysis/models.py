from pydantic import Field

from backend.models.base import VCCBaseModel


class SceneModel(VCCBaseModel):
    start: float
    end: float
    transcript: str = ""


class AnalysisModel(VCCBaseModel):
    duration: float = 0.0

    fps: float = 0.0

    width: int = 0

    height: int = 0

    scenes: list[SceneModel] = Field(default_factory=list)
