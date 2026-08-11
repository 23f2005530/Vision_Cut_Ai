from backend.timeline.clip import ClipModel
from backend.timeline.models import TimelineModel


class TimelineBuilder:
    """
    Converts ranked source clips into an editable timeline.
    """

    @staticmethod
    def build(clips):
        timeline = TimelineModel()

        current_time = 0.0

        for clip in clips:
            duration = clip.end - clip.start

            timeline.clips.append(
                ClipModel(
                    asset_id="main_video",
                    timeline_start=current_time,
                    source_start=clip.start,
                    duration=duration,
                    start=clip.start,
                    end=clip.end,
                    transcript=clip.transcript,
                    labels=clip.labels,
                    score=clip.score,
                    reason=clip.reason,
                )
            )

            current_time += duration

        timeline.duration = current_time

        return timeline
