from backend.vision.manager import VisionManager


def main():
    vision = VisionManager.analyze("storage/samples/test.mp4")

    for frame in vision.frames:
        print("-" * 50)

        print(f"Time: {frame.timestamp:.2f}s")

        for obj in frame.objects:
            print(f"{obj.label} ({obj.confidence:.2f})")


if __name__ == "__main__":
    main()
