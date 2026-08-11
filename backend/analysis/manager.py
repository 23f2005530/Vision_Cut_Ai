from pathlib import Path

from scenedetect import ContentDetector, SceneManager, open_video

from backend.analysis.models import AnalysisModel, SceneModel
from backend.analysis.scene_merger import SceneMerger
from backend.assets.extractor import MetadataExtractor
from backend.cache.keys import CacheKey
from backend.cache.manager import CacheManager


class AnalysisManager:
    """
    Performs complete AI analysis on a video.
    Uses cached analysis when available.
    """

    @staticmethod
    def analyze(video_path: str) -> AnalysisModel:
        cache_key = CacheKey.video_key(video_path)

        cached = CacheManager.load(
            "analysis",
            cache_key,
        )

        if cached is not None:
            print("Loading analysis from cache...")

            analysis: AnalysisModel = AnalysisModel.model_validate(cached)

            return analysis

        print("Running video analysis...")

        analysis = AnalysisModel()

        # Extract metadata
        metadata = MetadataExtractor.extract(Path(video_path))

        analysis.duration = metadata["duration"]
        analysis.fps = metadata["fps"]
        analysis.width = metadata["width"]
        analysis.height = metadata["height"]

        # Detect scenes
        video = open_video(video_path)

        scene_manager = SceneManager()

        scene_manager.add_detector(ContentDetector(threshold=35))

        scene_manager.detect_scenes(video)

        raw_scenes = []

        for start, end in scene_manager.get_scene_list():
            raw_scenes.append(
                SceneModel(
                    start=start.get_seconds(),
                    end=end.get_seconds(),
                )
            )

        # Merge short scenes
        analysis.scenes = SceneMerger.merge(raw_scenes)

        # Save result
        CacheManager.save(
            "analysis",
            cache_key,
            analysis.model_dump(mode="json"),
        )

        print("Analysis saved to cache.")

        return analysis
