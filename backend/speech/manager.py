from backend.ai.manager import AIModelManager
from backend.cache.keys import CacheKey
from backend.cache.manager import CacheManager
from backend.speech.models import (
    TranscriptModel,
    TranscriptSegmentModel,
    TranscriptWordModel,
)


class SpeechManager:
    """
    Handles speech-to-text transcription.
    Uses cached transcripts when available.
    """

    @classmethod
    def transcribe(cls, video_path: str) -> TranscriptModel:
        cache_key = CacheKey.video_key(video_path)

        cached = CacheManager.load(
            "transcripts",
            cache_key,
        )

        if cached is not None:
            print("Loading transcript from cache...")

            transcript: TranscriptModel = TranscriptModel.model_validate(cached)

            return transcript

        print("Running Whisper transcription...")

        model = AIModelManager.get_whisper()

        result = model.transcribe(
            video_path,
            word_timestamps=True,
        )

        transcript = TranscriptModel(
            language=result["language"],
            text=result["text"].strip(),
        )

        for segment_data in result["segments"]:
            words = []

            for word_data in segment_data.get("words", []):
                words.append(
                    TranscriptWordModel(
                        start=word_data["start"],
                        end=word_data["end"],
                        word=word_data["word"].strip(),
                    )
                )

            segment = TranscriptSegmentModel(
                start=segment_data["start"],
                end=segment_data["end"],
                text=segment_data["text"].strip(),
                words=words,
            )

            transcript.segments.append(segment)

        CacheManager.save(
            "transcripts",
            cache_key,
            transcript.model_dump(mode="json"),
        )

        print("Transcript saved to cache.")

        return transcript
