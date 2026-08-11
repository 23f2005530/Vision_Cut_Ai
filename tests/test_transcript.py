from backend.speech.manager import SpeechManager

video = "storage/samples/test.mp4"


def main():
    transcript = SpeechManager.transcribe(video)

    print("=" * 60)
    print("TRANSCRIPT")
    print("=" * 60)

    print("Language:", transcript.language)
    print("Segments:", len(transcript.segments))

    for segment in transcript.segments:
        print()
        print(f"SEGMENT {segment.start:.2f} -> {segment.end:.2f}")

        print("Text:", segment.text)

        print("Words:")

        for word in segment.words:
            print(f"  {word.start:.2f} -> {word.end:.2f} : {word.word}")


if __name__ == "__main__":
    main()
