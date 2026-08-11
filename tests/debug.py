from backend.analysis.manager import AnalysisManager
from backend.speech.manager import SpeechManager

video = "storage/samples/test.mp4"

analysis = AnalysisManager.analyze(video)
transcript = SpeechManager.transcribe(video)

print("\nSCENES")
for scene in analysis.scenes:
    print(f"{scene.start:.2f} -> {scene.end:.2f}")

print("\nSEGMENTS")
for seg in transcript.segments:
    print(f"{seg.start:.2f} -> {seg.end:.2f} : {seg.text}")
