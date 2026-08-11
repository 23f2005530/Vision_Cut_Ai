from backend.analysis.manager import AnalysisManager


def main():
    scenes = AnalysisManager.detect_scenes("storage/samples/test.mp4")

    print()

    print("Detected Scenes")

    for i, scene in enumerate(scenes, start=1):
        print(f"{i}. {scene['start']:.2f}s -> {scene['end']:.2f}s")


if __name__ == "__main__":
    main()
