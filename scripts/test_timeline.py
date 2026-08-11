from backend.ai.scorer import ClipScorer
from backend.analysis.manager import AnalysisManager
from backend.analysis.mapper import AnalysisMapper
from backend.editor.builder import ClipBuilder
from backend.editor.ranker import ClipRanker
from backend.editor.timeline_builder import TimelineBuilder
from backend.speech.manager import SpeechManager
from backend.vision.manager import VisionManager

video = "storage/samples/test.mp4"

analysis = AnalysisManager.analyze(video)

transcript = SpeechManager.transcribe(video)

analysis = AnalysisMapper.attach_transcript(
    analysis,
    transcript,
)

vision = VisionManager.analyze(video)

clips = ClipBuilder.build(
    analysis,
    vision,
)

clips = ClipScorer.score(clips)

clips = ClipRanker.rank(
    clips,
    minimum_score=6.5,
)

timeline = TimelineBuilder.build(clips)

print(f"Timeline duration: {timeline.duration:.2f}s")

for clip in timeline.clips:
    print("-" * 60)

    print(f"Timeline : {clip.timeline_start:.2f}s")

    print(f"Source   : {clip.source_start:.2f}s")

    print(f"Duration : {clip.duration:.2f}s")

    print(f"Score    : {clip.score}")

    print(clip.transcript)
