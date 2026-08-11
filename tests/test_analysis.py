from backend.analysis.manager import AnalysisManager

video = "storage/samples/test.mp4"

analysis = AnalysisManager.analyze(video)

print("=" * 60)
print("VIDEO ANALYSIS")
print("=" * 60)

print("Duration:", analysis.duration)
print("FPS     :", analysis.fps)
print("Scenes  :", len(analysis.scenes))

print("\nSCENES")

for i, scene in enumerate(analysis.scenes, start=1):
    duration = scene.end - scene.start

    print(f"[{i:02d}] {scene.start:.2f} -> {scene.end:.2f} ({duration:.2f}s)")
