from backend.models.clip import ClipModel
from backend.models.timeline import TimelineModel
from backend.models.track import TrackModel


def test_timeline_models():
    clip = ClipModel(asset_id="video1")

    track = TrackModel(name="Video Track", track_type="video", clips=[clip])

    timeline = TimelineModel(name="Main Timeline", tracks=[track])

    assert timeline.tracks[0].clips[0].asset_id == "video1"
