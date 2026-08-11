from backend.analysis.manager import AnalysisManager
from backend.analysis.mapper import AnalysisMapper
from backend.editor.builder import ClipBuilder
from backend.speech.manager import SpeechManager
from backend.vision.manager import VisionManager

VIDEO = "storage/samples/test.mp4"


def main():
    print("Loading analysis...")
    analysis = AnalysisManager.analyze(VIDEO)

    print("Loading transcript...")
    transcript = SpeechManager.transcribe(VIDEO)

    print("Attaching transcript...")
    analysis = AnalysisMapper.attach_transcript(
        analysis,
        transcript,
    )

    print("Loading vision...")
    vision = VisionManager.analyze(VIDEO)

    print("Building clips...")

    clips = ClipBuilder.build(
        analysis,
        vision,
    )

    print()
    print("=" * 60)
    print("SOURCE CLIPS")
    print("=" * 60)

    print("Total clips:", len(clips))

    for index, clip in enumerate(clips, start=1):
        print()
        print(f"[{index}]")
        print(f"Start      : {clip.start:.2f}")
        print(f"End        : {clip.end:.2f}")
        print(f"Duration   : {clip.duration:.2f}")
        print(f"Transcript : {clip.transcript}")
        print(f"Labels     : {clip.labels}")
        print(f"Score      : {clip.score}")
        print(f"Reason     : {clip.reason}")


if __name__ == "__main__":
    main()
