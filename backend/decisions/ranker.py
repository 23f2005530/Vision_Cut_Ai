from backend.timeline.models import TimelineModel


class ClipRanker:
    @classmethod
    def rank(cls, timeline: TimelineModel) -> TimelineModel:
        timeline.clips.sort(
            key=lambda clip: clip.score,
            reverse=True,
        )

        return timeline
