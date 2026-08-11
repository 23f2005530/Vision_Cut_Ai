"""
Render Service

Responsible for converting the AI-generated timeline
into a real video file using FFmpeg.
"""

import subprocess
from pathlib import Path

from backend.editor.caption.ass_generator import ASSGenerator
from backend.editor.caption_builder import CaptionBuilder


class RenderService:
    """Renders a TimelineModel into an MP4 video."""

    @staticmethod
    def render(
        timeline,
        source_video: str,
        output_path: str,
        transcript,
    ) -> str:
        source_path = Path(source_video)
        output_file = Path(output_path)

        output_file.parent.mkdir(parents=True, exist_ok=True)

        if not source_path.exists():
            raise FileNotFoundError(f"Source video not found: {source_path}")

        if not timeline.clips:
            raise ValueError("Timeline contains no clips.")

        # ---------------------------------------------------------
        # BUILD CAPTIONS
        # ---------------------------------------------------------

        print("Building captions...")

        timeline = CaptionBuilder.build(
            timeline,
            transcript,
        )

        print("Captions:", len(timeline.captions))

        # ---------------------------------------------------------
        # GENERATE ASS
        # ---------------------------------------------------------

        ass_path = output_file.with_suffix(".ass")

        print("Generating ASS subtitles...")

        ASSGenerator.generate(
            timeline,
            str(ass_path),
        )

        # ---------------------------------------------------------
        # BUILD FFMPEG INPUTS
        # ---------------------------------------------------------

        inputs = []
        filters = []

        for index, clip in enumerate(timeline.clips):
            inputs.extend(
                [
                    "-ss",
                    str(clip.source_start),
                    "-t",
                    str(clip.duration),
                    "-i",
                    str(source_path),
                ]
            )

            filters.append(
                f"[{index}:v:0]"
                f"setpts=PTS-STARTPTS,"
                f"scale=1080:1920:"
                f"force_original_aspect_ratio=increase,"
                f"crop=1080:1920"
                f"[v{index}]"
            )

            filters.append(f"[{index}:a:0]asetpts=PTS-STARTPTS[a{index}]")

        # ---------------------------------------------------------
        # CONCATENATE SELECTED CLIPS
        # ---------------------------------------------------------

        video_inputs = "".join(f"[v{i}][a{i}]" for i in range(len(timeline.clips)))

        filters.append(f"{video_inputs}concat=n={len(timeline.clips)}:v=1:a=1[vout][aout]")

        # ---------------------------------------------------------
        # BURN ASS CAPTIONS
        # ---------------------------------------------------------

        # Escape Windows path for FFmpeg filter syntax.
        ass_filter_path = str(ass_path.resolve())
        ass_filter_path = ass_filter_path.replace("\\", "/")
        ass_filter_path = ass_filter_path.replace(":", "\\:")

        filters.append(f"[vout]ass='{ass_filter_path}'[vcaption]")

        # ---------------------------------------------------------
        # FFMPEG COMMAND
        # ---------------------------------------------------------

        command = [
            "ffmpeg",
            "-y",
            *inputs,
            "-filter_complex",
            ";".join(filters),
            "-map",
            "[vcaption]",
            "-map",
            "[aout]",
            "-c:v",
            "libx264",
            "-preset",
            "medium",
            "-crf",
            "23",
            "-c:a",
            "aac",
            "-movflags",
            "+faststart",
            str(output_file),
        ]

        print("Rendering video with captions...")

        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
        )

        if result.returncode != 0:
            print(result.stderr)
            raise RuntimeError("FFmpeg rendering failed.")

        print(f"Render complete: {output_file}")

        return str(output_file)
