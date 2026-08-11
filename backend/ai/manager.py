from pathlib import Path

import whisper
from ultralytics import YOLO


class AIModelManager:
    """
    Loads and caches AI models.
    """

    _yolo = None
    _whisper = None

    MODELS_DIR = Path("models")

    @classmethod
    def get_yolo(cls):
        if cls._yolo is None:
            model_path = cls.MODELS_DIR / "vision" / "yolov8n.pt"

            print("Loading YOLO...")

            cls._yolo = YOLO(model_path)

        return cls._yolo

    @classmethod
    def get_whisper(cls):
        if cls._whisper is None:
            print("Loading Whisper...")

            cls._whisper = whisper.load_model("tiny")

        return cls._whisper
