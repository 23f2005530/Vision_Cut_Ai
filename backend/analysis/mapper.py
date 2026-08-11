from backend.analysis.models import AnalysisModel
from backend.speech.models import TranscriptModel


class AnalysisMapper:
    """
    Maps transcript segments into scenes.
    """

    @staticmethod
    def attach_transcript(
        analysis: AnalysisModel,
        transcription: TranscriptModel,
    ) -> AnalysisModel:
        for scene in analysis.scenes:
            texts = []

            for segment in transcription.segments:
                if segment.start < scene.end and segment.end > scene.start:
                    texts.append(segment.text)

            scene.transcript = " ".join(texts)

        return analysis
