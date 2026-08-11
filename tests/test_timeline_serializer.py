from pathlib import Path

from backend.models.timeline import TimelineModel
from backend.timeline.manager import TimelineManager
from backend.timeline.serializer import TimelineSerializer


def test_timeline_serializer(tmp_path: Path):
    timeline = TimelineModel(name="Timeline")

    manager = TimelineManager(timeline)

    track = manager.add_track("Video", "video")

    manager.add_clip(
        track,
        asset_id="asset1",
        timeline_start=0,
        duration=10,
    )

    TimelineSerializer.save(timeline, str(tmp_path))

    loaded = TimelineSerializer.load(str(tmp_path))

    assert loaded.name == "Timeline"
    assert len(loaded.tracks) == 1
    assert len(loaded.tracks[0].clips) == 1
