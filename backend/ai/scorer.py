from backend.ai.llm import LLMManager


class ClipScorer:
    """
    Uses the local LLM to score every clip.
    """

    HOOK_WEIGHT = 0.35
    TRANSCRIPT_WEIGHT = 0.25
    VISUAL_WEIGHT = 0.25
    CONTEXT_WEIGHT = 0.10
    DURATION_WEIGHT = 0.05

    @staticmethod
    def score(clips):
        total = len(clips)

        for index, clip in enumerate(clips, start=1):
            print(f"[{index}/{total}] Scoring clip...")

            try:
                result = LLMManager.analyze(clip)

                hook = float(result.get("hook", 0))
                transcript = float(result.get("transcript", 0))
                visual = float(result.get("visual_relevance", 0))
                context = float(result.get("context", 0))
                duration = float(result.get("duration", 0))

                clip.score = round(
                    hook * ClipScorer.HOOK_WEIGHT
                    + transcript * ClipScorer.TRANSCRIPT_WEIGHT
                    + visual * ClipScorer.VISUAL_WEIGHT
                    + context * ClipScorer.CONTEXT_WEIGHT
                    + duration * ClipScorer.DURATION_WEIGHT,
                    2,
                )

                clip.reason = result.get("reason", "")

            except Exception as e:
                print(f"Error: {e}")

                clip.score = 0
                clip.reason = ""

        return clips
