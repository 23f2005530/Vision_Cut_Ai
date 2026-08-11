from pydantic import Field

from backend.models.base import VCCBaseModel


class ClipModel(VCCBaseModel):
    """
    Represents a single clip on the timeline.
    """

    # Source media
    asset_id: str = ""

    # Source video timing
    start: float
    end: float

    # Timeline placement
    timeline_start: float = 0.0
    source_start: float = 0.0
    duration: float = 0.0

    # Playback settings
    speed: float = 1.0
    muted: bool = False
    enabled: bool = True

    # AI metadata
    transcript: str = ""
    labels: list[str] = Field(default_factory=list)
    score: float = 0.0

    # LLM explanation (useful later)
    reason: str = ""
