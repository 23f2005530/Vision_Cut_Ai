from pydantic import Field

from backend.models.base import VCCBaseModel


class TranscriptWordModel(VCCBaseModel):
    start: float
    end: float
    word: str


class TranscriptSegmentModel(VCCBaseModel):
    start: float
    end: float
    text: str
    words: list[TranscriptWordModel] = Field(default_factory=list)


class TranscriptModel(VCCBaseModel):
    language: str = "unknown"

    text: str = ""

    segments: list[TranscriptSegmentModel] = Field(default_factory=list)
