from backend.vision.manager import VisionManager

video = "storage/samples/test.mp4"


def main():
    vision = VisionManager.analyze(video)

    print("=" * 60)
    print("VISION")
    print("=" * 60)

    print("Frames:", len(vision.frames))

    for frame in vision.frames:
        print(f"{frame.timestamp:.2f}s Objects: {len(frame.objects)}")

        for obj in frame.objects:
            print(f"    {obj.label} confidence={obj.confidence:.2f}")


if __name__ == "__main__":
    main()
