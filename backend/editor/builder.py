from backend.models.source_clip import (
    SourceClipModel,
    SourceClipObjectModel,
)


class ClipBuilder:
    """
    Converts analysis + vision into AI-ready source clips.
    """

    @staticmethod
    def build(analysis, vision):
        clips = []

        for scene in analysis.scenes:
            labels = set()
            objects = []

            for frame in vision.frames:
                if scene.start <= frame.timestamp <= scene.end:
                    for obj in frame.objects:
                        labels.add(obj.label)

                        objects.append(
                            SourceClipObjectModel(
                                label=obj.label,
                                confidence=obj.confidence,
                                x=obj.x,
                                y=obj.y,
                                width=obj.width,
                                height=obj.height,
                            )
                        )

            clips.append(
                SourceClipModel(
                    start=scene.start,
                    end=scene.end,
                    transcript=scene.transcript,
                    labels=sorted(labels),
                    objects=objects,
                )
            )

        return clips
