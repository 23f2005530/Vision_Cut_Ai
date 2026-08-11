from pydantic import Field

from backend.models.base import VCCBaseModel


class DetectedObjectModel(VCCBaseModel):
    label: str

    confidence: float

    x: float

    y: float

    width: float

    height: float


class VisionFrameModel(VCCBaseModel):
    timestamp: float

    objects: list[DetectedObjectModel] = Field(default_factory=list)


class VisionModel(VCCBaseModel):
    frames: list[VisionFrameModel] = Field(default_factory=list)
