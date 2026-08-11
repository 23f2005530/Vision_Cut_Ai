from backend.models.timeline import TimelineModel
from backend.timeline.manager import TimelineManager


def test_split_clip():
    timeline = TimelineModel(name="Demo")

    manager = TimelineManager(timeline)

    track = manager.add_track(
        "Video",
        "video",
    )

    clip = manager.add_clip(
        track,
        asset_id="video1",
        timeline_start=0,
        duration=10,
    )

    second = manager.split_clip(
        track,
        clip,
        4,
    )

    assert len(track.clips) == 2

    assert clip.duration == 4

    assert second.timeline_start == 4

    assert second.duration == 6
