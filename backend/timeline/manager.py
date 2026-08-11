from copy import deepcopy

from backend.models.clip import ClipModel
from backend.models.timeline import TimelineModel
from backend.models.track import TrackModel


class TimelineManager:
    """
    Handles timeline operations.
    """

    def __init__(self, timeline: TimelineModel):
        self.timeline = timeline

    def add_track(self, name: str, track_type: str) -> TrackModel:
        track = TrackModel(
            name=name,
            track_type=track_type,
        )

        self.timeline.tracks.append(track)

        return track

    def add_clip(
        self,
        track: TrackModel,
        asset_id: str,
        timeline_start: float,
        duration: float,
    ) -> ClipModel:
        clip = ClipModel(
            asset_id=asset_id,
            timeline_start=timeline_start,
            duration=duration,
        )

        track.clips.append(clip)

        self.timeline.duration = max(
            self.timeline.duration,
            timeline_start + duration,
        )

        return clip

    def remove_clip(self, track, clip):
        """
        Removes a clip from a track.
        """
        track.clips.remove(clip)

        if track.clips:
            self.timeline.duration = max(
                c.timeline_start + c.duration for t in self.timeline.tracks for c in t.clips
            )
        else:
            self.timeline.duration = 0

    def move_clip(self, clip, new_start: float):
        """
        Moves a clip on the timeline.
        """
        clip.timeline_start = new_start

        self.timeline.duration = max(
            (c.timeline_start + c.duration for t in self.timeline.tracks for c in t.clips),
            default=0,
        )

    def trim_clip(self, clip, new_duration: float):
        """
        Changes clip duration.
        """
        if new_duration <= 0:
            raise ValueError("Duration must be positive.")

        clip.duration = new_duration

        self.timeline.duration = max(
            (c.timeline_start + c.duration for t in self.timeline.tracks for c in t.clips),
            default=0,
        )

    def split_clip(self, track, clip, split_time: float):
        """
        Split a clip into two clips.
        """

        if split_time <= clip.timeline_start:
            raise ValueError("Split before clip.")

        if split_time >= clip.timeline_start + clip.duration:
            raise ValueError("Split after clip.")

        left_duration = split_time - clip.timeline_start

        right = deepcopy(clip)

        right.source_start += left_duration
        right.timeline_start = split_time
        right.duration = clip.duration - left_duration

        clip.duration = left_duration

        index = track.clips.index(clip)

        track.clips.insert(index + 1, right)

        return right
