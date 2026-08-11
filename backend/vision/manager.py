import cv2

from backend.ai.manager import AIModelManager
from backend.cache.keys import CacheKey
from backend.cache.manager import CacheManager
from backend.vision.models import (
    DetectedObjectModel,
    VisionFrameModel,
    VisionModel,
)


class VisionManager:
    """
    Runs object detection on video frames.
    Uses cached vision results when available.
    """

    @classmethod
    def analyze(cls, video_path: str) -> VisionModel:
        cache_key = CacheKey.video_key(video_path)

        cached = CacheManager.load(
            "vision",
            cache_key,
        )

        if cached is not None:
            print("Loading vision from cache...")

            vision: VisionModel = VisionModel.model_validate(cached)

            return vision

        print("Running YOLO vision analysis...")

        model = AIModelManager.get_yolo()

        cap = cv2.VideoCapture(video_path)

        fps = cap.get(cv2.CAP_PROP_FPS)

        frame_number = 0

        vision = VisionModel()

        while True:
            success, frame = cap.read()

            if not success:
                break

            # Analyze one frame every second
            if frame_number % int(fps) != 0:
                frame_number += 1
                continue

            timestamp = frame_number / fps

            results = model(
                frame,
                verbose=False,
            )

            frame_result = VisionFrameModel(timestamp=timestamp)

            for box in results[0].boxes:
                cls_id = int(box.cls[0])

                label = model.names[cls_id]

                confidence = float(box.conf[0])

                if confidence < 0.50:
                    continue

                x1, y1, x2, y2 = box.xyxy[0].tolist()

                frame_result.objects.append(
                    DetectedObjectModel(
                        label=label,
                        confidence=confidence,
                        x=x1,
                        y=y1,
                        width=x2 - x1,
                        height=y2 - y1,
                    )
                )

            vision.frames.append(frame_result)

            frame_number += 1

        cap.release()

        CacheManager.save(
            "vision",
            cache_key,
            vision.model_dump(mode="json"),
        )

        print("Vision saved to cache.")

        return vision
