from backend.models.timeline import TimelineModel
from backend.timeline.manager import TimelineManager
from backend.timeline.serializer import TimelineSerializer


def main():
    workspace = "storage/projects/Demo Project"

    timeline = TimelineModel(name="Main Timeline")

    manager = TimelineManager(timeline)

    track = manager.add_track("Video 1", "video")

    manager.add_clip(
        track,
        asset_id="video123",
        timeline_start=0,
        duration=5,
    )

    TimelineSerializer.save(timeline, workspace)

    loaded = TimelineSerializer.load(workspace)

    print(loaded.model_dump_json(indent=4))


if __name__ == "__main__":
    main()
