class ClipRanker:
    """
    Filters, deduplicates, and sorts clips while preserving
    chronological storytelling.
    """

    @staticmethod
    def _similar_transcript(text_a, text_b):
        words_a = set(text_a.lower().split())
        words_b = set(text_b.lower().split())

        if not words_a or not words_b:
            return False

        intersection = words_a & words_b
        union = words_a | words_b

        similarity = len(intersection) / len(union)

        return similarity >= 0.70

    @staticmethod
    def rank(
        clips,
        minimum_score=6.5,
        max_clips=None,
    ):
        # 1. Remove low-scoring clips.
        candidates = [clip for clip in clips if clip.score >= minimum_score]

        # 2. Process chronologically.
        candidates.sort(key=lambda clip: clip.start)

        selected = []

        for clip in candidates:
            duplicate_index = None

            # Check against already-selected clips.
            for index, selected_clip in enumerate(selected):
                # Reject overlapping clips.
                if clip.start < selected_clip.end and clip.end > selected_clip.start:
                    duplicate_index = index
                    break

                # Reject highly similar transcript.
                if ClipRanker._similar_transcript(
                    clip.transcript,
                    selected_clip.transcript,
                ):
                    duplicate_index = index
                    break

            if duplicate_index is not None:
                existing = selected[duplicate_index]

                # Keep whichever duplicate has the better score.
                if clip.score > existing.score:
                    selected[duplicate_index] = clip

                continue

            selected.append(clip)

        # 3. Restore chronological order after replacements.
        selected.sort(key=lambda clip: clip.start)

        # 4. Limit the number of clips.
        if max_clips is not None:
            selected = selected[:max_clips]

        return selected
