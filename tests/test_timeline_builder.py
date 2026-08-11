from backend.ai.scorer import ClipScorer
from backend.analysis.manager import AnalysisManager
from backend.analysis.mapper import AnalysisMapper
from backend.editor.builder import ClipBuilder
from backend.editor.ranker import ClipRanker
from backend.editor.timeline_builder import TimelineBuilder
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

    print("Building source clips...")
    clips = ClipBuilder.build(
        analysis,
        vision,
    )

    print("Scoring clips...")
    clips = ClipScorer.score(clips)

    print("Ranking clips...")
    ranked = ClipRanker.rank(
        clips,
        minimum_score=6.5,
    )

    print("Building timeline...")

    timeline = TimelineBuilder.build(ranked)

    print()
    print("=" * 70)
    print("TIMELINE")
    print("=" * 70)

    print(f"Total clips : {len(timeline.clips)}")
    print(f"Duration    : {timeline.duration:.2f}s")

    for index, clip in enumerate(timeline.clips, start=1):
        print()
        print(f"[{index}]")
        print(f"Timeline start : {clip.timeline_start:.2f}")
        print(f"Source start   : {clip.source_start:.2f}")
        print(f"Duration       : {clip.duration:.2f}")
        print(f"Score          : {clip.score}")
        print(f"Reason         : {clip.reason}")
        print(f"Transcript     : {clip.transcript}")


if __name__ == "__main__":
    main()
