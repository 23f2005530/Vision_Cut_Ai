from pathlib import Path

from backend.ai.scorer import ClipScorer
from backend.analysis.manager import AnalysisManager
from backend.analysis.mapper import AnalysisMapper
from backend.editor.builder import ClipBuilder
from backend.editor.ranker import ClipRanker
from backend.editor.timeline_builder import TimelineBuilder
from backend.services.render_service import RenderService
from backend.speech.manager import SpeechManager
from backend.vision.manager import VisionManager


def main():
    video = "storage/samples/test.mp4"
    output = "storage/outputs/test_render_vertical.mp4"

    print("Loading analysis...")
    analysis = AnalysisManager.analyze(video)

    print("Loading transcript...")
    transcript = SpeechManager.transcribe(video)

    print("Attaching transcript...")
    analysis = AnalysisMapper.attach_transcript(
        analysis,
        transcript,
    )

    print("Loading vision...")
    vision = VisionManager.analyze(video)

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
    print("=" * 60)
    print("TIMELINE")
    print("=" * 60)
    print("Clips    :", len(timeline.clips))
    print("Duration :", round(timeline.duration, 2), "seconds")

    for i, clip in enumerate(timeline.clips, 1):
        print()
        print(f"[{i}]")
        print("Source   :", f"{clip.source_start:.2f}s")
        print("Duration :", f"{clip.duration:.2f}s")
        print("Score    :", clip.score)

    print()
    print("Rendering...")

    RenderService.render(
        timeline,
        video,
        output,
        transcript,
    )

    print()
    print("=" * 60)
    print("RENDER COMPLETE")
    print("=" * 60)
    print("Output:", output)

    if Path(output).exists():
        size = Path(output).stat().st_size
        print("Size  :", round(size / (1024 * 1024), 2), "MB")


if __name__ == "__main__":
    main()
