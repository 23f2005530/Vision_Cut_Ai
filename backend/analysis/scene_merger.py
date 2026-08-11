from backend.analysis.models import SceneModel


class SceneMerger:
    """
    Merges very short consecutive scenes into larger, usable scenes.
    """

    @staticmethod
    def merge(
        scenes: list[SceneModel],
        min_duration: float = 2.0,
    ) -> list[SceneModel]:
        if not scenes:
            return []

        merged = []

        current = scenes[0]

        for next_scene in scenes[1:]:
            current_duration = current.end - current.start

            if current_duration < min_duration:
                current.end = next_scene.end

                if current.transcript and next_scene.transcript:
                    current.transcript += " " + next_scene.transcript
                elif next_scene.transcript:
                    current.transcript = next_scene.transcript

            else:
                merged.append(current)
                current = next_scene

        merged.append(current)

        return merged
