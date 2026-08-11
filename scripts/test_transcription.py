from backend.speech.manager import SpeechManager


def main():
    transcript = SpeechManager.transcribe("storage/samples/test.mp4")

    print(transcript.model_dump_json(indent=4))


if __name__ == "__main__":
    main()
