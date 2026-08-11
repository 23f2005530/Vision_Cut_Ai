from backend.models.timeline import TimelineModel
from backend.timeline.manager import TimelineManager


def test_editing_operations():
    timeline = TimelineModel(name="Demo")

    manager = TimelineManager(timeline)

    track = manager.add_track("Video", "video")

    clip = manager.add_clip(
        track,
        asset_id="video1",
        timeline_start=0,
        duration=10,
    )

    manager.move_clip(clip, 5)

    assert clip.timeline_start == 5

    manager.trim_clip(clip, 6)

    assert clip.duration == 6

    manager.remove_clip(track, clip)

    assert len(track.clips) == 0
