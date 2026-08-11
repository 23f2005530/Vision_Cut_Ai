from backend.assets.thumbnail_generator import ThumbnailGenerator


def main():
    thumbnail = ThumbnailGenerator.generate("storage/samples/test.mp4")

    print(thumbnail)


if __name__ == "__main__":
    main()
