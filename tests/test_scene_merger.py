from backend.analysis.manager import AnalysisManager
from backend.analysis.scene_merger import SceneMerger

video = "storage/samples/test.mp4"

analysis = AnalysisManager.analyze(video)

print("=" * 70)
print("BEFORE MERGING")
print("=" * 70)

for scene in analysis.scenes:
    print(f"{scene.start:.2f} -> {scene.end:.2f} ({scene.end - scene.start:.2f}s)")

merged = SceneMerger.merge(analysis.scenes)

print("\n" + "=" * 70)
print("AFTER MERGING")
print("=" * 70)

for scene in merged:
    print(f"{scene.start:.2f} -> {scene.end:.2f} ({scene.end - scene.start:.2f}s)")

print("\n" + "=" * 70)
print(f"Scenes before : {len(analysis.scenes)}")
print(f"Scenes after  : {len(merged)}")
print("=" * 70)
