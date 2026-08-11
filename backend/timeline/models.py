from pydantic import Field

from backend.models.base import VCCBaseModel
from backend.models.caption import CaptionModel
from backend.timeline.clip import ClipModel


class TimelineModel(VCCBaseModel):
    clips: list[ClipModel] = Field(default_factory=list)

    captions: list[CaptionModel] = Field(default_factory=list)

    duration: float = 0.0
