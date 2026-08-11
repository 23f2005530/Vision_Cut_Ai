from backend.ai.scorer import ClipScorer
from backend.analysis.manager import AnalysisManager
from backend.analysis.mapper import AnalysisMapper
from backend.editor.builder import ClipBuilder
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

for clip in clips:
    print("-" * 60)

    print("Start :", clip.start)

    print("End   :", clip.end)

    print("Score :", clip.score)

    print("Reason:", clip.reason)
