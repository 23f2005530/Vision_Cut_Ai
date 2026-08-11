from backend.editor.caption_builder import CaptionBuilder
from backend.speech.models import (
    TranscriptModel,
    TranscriptSegmentModel,
)
from backend.timeline.clip import ClipModel
from backend.timeline.models import TimelineModel


def main():
    timeline = TimelineModel()

    timeline.clips.append(
        ClipModel(
            asset_id="main_video",
            start=5.79,
            end=8.33,
            timeline_start=0.0,
            source_start=5.79,
            duration=2.54,
        )
    )

    transcript = TranscriptModel(
        language="en",
        segments=[
            TranscriptSegmentModel(
                start=5.84,
                end=10.56,
                text="I'm not flat.",
                words=[
                    {
                        "start": 5.84,
                        "end": 6.20,
                        "word": "I'm",
                    },
                    {
                        "start": 6.20,
                        "end": 6.60,
                        "word": "not",
                    },
                    {
                        "start": 6.60,
                        "end": 7.10,
                        "word": "flat.",
                    },
                ],
            ),
        ],
    )

    timeline = CaptionBuilder.build(
        timeline,
        transcript,
    )

    print("Timeline clips:", len(timeline.clips))

    for clip in timeline.clips:
        print(
            "CLIP:",
            clip.source_start,
            "->",
            clip.source_start + clip.duration,
            "timeline:",
            clip.timeline_start,
        )

    print("Transcript segments:", len(transcript.segments))

    for segment in transcript.segments:
        print(
            "SEGMENT:",
            segment.start,
            "->",
            segment.end,
            "words:",
            len(segment.words),
        )

        for word in segment.words[:5]:
            print(
                " WORD:",
                word.start,
                "->",
                word.end,
                repr(word.word),
            )

    print("=" * 60)
    print("CAPTIONS")
    print("=" * 60)

    print("Total captions:", len(timeline.captions))

    for caption in timeline.captions:
        print()
        print("Start :", round(caption.start, 2))
        print("End   :", round(caption.end, 2))
        print("Text  :", caption.text)


if __name__ == "__main__":
    main()
