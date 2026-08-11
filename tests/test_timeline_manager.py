from backend.models.timeline import TimelineModel
from backend.timeline.manager import TimelineManager


def test_add_clip():
    timeline = TimelineModel(name="Demo")

    manager = TimelineManager(timeline)

    track = manager.add_track(
        "Video 1",
        "video",
    )

    manager.add_clip(
        track,
        asset_id="video123",
        timeline_start=0,
        duration=10,
    )

    assert len(track.clips) == 1
    assert timeline.duration == 10
