from backend.models.caption import CaptionModel


class CaptionBuilder:
    """
    Converts transcript words into timeline captions.
    Creates one caption per word.
    """

    @staticmethod
    def build(timeline, transcript):
        captions = []

        for clip in timeline.clips:
            clip_source_start = clip.source_start
            clip_source_end = clip.source_start + clip.duration

            for segment in transcript.segments:
                # Skip segments outside this clip
                if segment.end <= clip_source_start:
                    continue

                if segment.start >= clip_source_end:
                    continue

                # Use word-level timestamps
                for word in segment.words:
                    word_start = word.start
                    word_end = word.end

                    # Word is outside the selected clip
                    if word_end <= clip_source_start:
                        continue

                    if word_start >= clip_source_end:
                        continue

                    # Limit word to clip boundaries
                    source_start = max(
                        word_start,
                        clip_source_start,
                    )

                    source_end = min(
                        word_end,
                        clip_source_end,
                    )

                    # Convert source time -> timeline time
                    timeline_start = clip.timeline_start + source_start - clip_source_start

                    timeline_end = clip.timeline_start + source_end - clip_source_start

                    text = word.word.strip()

                    if not text:
                        continue

                    captions.append(
                        CaptionModel(
                            text=text,
                            start=timeline_start,
                            end=timeline_end,
                        )
                    )

        timeline.captions = captions

        return timeline
