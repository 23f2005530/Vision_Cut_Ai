from pathlib import Path


class ASSGenerator:
    """
    Generates an ASS subtitle file from timeline captions
    with a pop-in animation for each caption.
    """

    @staticmethod
    def _timestamp(seconds: float) -> str:
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = int(seconds % 60)
        centiseconds = int(round((seconds - int(seconds)) * 100))

        if centiseconds >= 100:
            secs += 1
            centiseconds = 0

        if secs >= 60:
            minutes += 1
            secs = 0

        if minutes >= 60:
            hours += 1
            minutes = 0

        return f"{hours}:{minutes:02d}:{secs:02d}.{centiseconds:02d}"

    @classmethod
    def generate(
        cls,
        timeline,
        output_path: str,
    ) -> str:
        path = Path(output_path)
        path.parent.mkdir(parents=True, exist_ok=True)

        lines = [
            "[Script Info]",
            "ScriptType: v4.00+",
            "PlayResX: 1080",
            "PlayResY: 1920",
            "ScaledBorderAndShadow: yes",
            "",
            "[V4+ Styles]",
            (
                "Format: Name, Fontname, Fontsize, PrimaryColour, "
                "SecondaryColour, OutlineColour, BackColour, Bold, "
                "Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, "
                "Angle, BorderStyle, Outline, Shadow, Alignment, "
                "MarginL, MarginR, MarginV, Encoding"
            ),
            (
                "Style: Default,Arial,64,"
                "&H00FFFFFF,"
                "&H00FFFFFF,"
                "&H00000000,"
                "&H80000000,"
                "-1,0,0,0,"
                "100,100,0,0,1,4,2,2,"
                "40,40,160,1"
            ),
            "",
            "[Events]",
            ("Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text"),
        ]

        for caption in timeline.captions:
            start = cls._timestamp(caption.start)
            end = cls._timestamp(caption.end)

            text = caption.text.replace("\n", "\\N")

            # Pop-in animation:
            # Start at 75% size and grow to 100% over 120ms.
            animated_text = (
                r"{\fscx75\fscy75"
                r"\t(0,120,\fscx100\fscy100)}" + text
            )

            lines.append(f"Dialogue: 0,{start},{end},Default,,0,0,0,,{animated_text}")

        path.write_text(
            "\n".join(lines),
            encoding="utf-8",
        )

        return str(path)
