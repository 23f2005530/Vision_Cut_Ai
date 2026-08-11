from backend.editor.caption.ass_generator import ASSGenerator
from backend.editor.caption_builder import CaptionBuilder
from backend.speech.models import (
    TranscriptModel,
    TranscriptSegmentModel,
    TranscriptWordModel,
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
                end=10.50,
                text="And by the way, all those rumors on the internet are fake, I'm not flat.",
                words=[
                    TranscriptWordModel(
                        start=5.84,
                        end=6.20,
                        word="I'm",
                    ),
                    TranscriptWordModel(
                        start=6.20,
                        end=6.60,
                        word="not",
                    ),
                    TranscriptWordModel(
                        start=6.60,
                        end=7.10,
                        word="flat.",
                    ),
                ],
            )
        ],
    )

    timeline = CaptionBuilder.build(
        timeline,
        transcript,
    )

    print("Captions before ASS:", len(timeline.captions))

    output = ASSGenerator.generate(
        timeline,
        "storage/outputs/test.ass",
    )

    print("=" * 60)
    print("ASS GENERATED")
    print("=" * 60)
    print("Output:", output)
    print("Captions:", len(timeline.captions))


if __name__ == "__main__":
    main()
