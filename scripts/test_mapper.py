from backend.analysis.manager import AnalysisManager
from backend.analysis.mapper import AnalysisMapper
from backend.speech.manager import SpeechManager


def main():
    video = "storage/samples/test.mp4"

    analysis = AnalysisManager.analyze(video)

    transcription = SpeechManager.transcribe(video)

    analysis = AnalysisMapper.attach_transcript(
        analysis,
        transcription,
    )

    for i, scene in enumerate(analysis.scenes, start=1):
        print("-" * 60)
        print(f"Scene {i}")
        print(scene.start)
        print(scene.end)
        print(scene.transcript)


if __name__ == "__main__":
    main()
