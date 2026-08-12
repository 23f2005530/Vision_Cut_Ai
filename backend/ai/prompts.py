import json


class PromptBuilder:
    @staticmethod
    def score_clip(clip):
        clip_data = {
            "start": round(clip.start, 2),
            "end": round(clip.end, 2),
            "duration": round(clip.end - clip.start, 2),
            "transcript": clip.transcript,
            "labels": clip.labels,
        }

        return f"""
You are an expert YouTube Shorts editor.

Evaluate this video clip using FIVE independent scores.

Each score must be an integer from 0 to 10.

Do NOT calculate a final score.
Python will calculate the final score.

========================
1. HOOK
========================

How attention-grabbing is the clip?

10 = extremely strong hook, surprising, funny, dramatic,
     or immediately interesting

5 = somewhat interesting

0 = boring or no meaningful hook

========================
2. TRANSCRIPT
========================

How good is the spoken content?

10 = excellent, clear, complete, entertaining statement
5 = understandable but ordinary
0 = no speech, meaningless, or unusable speech

========================
3. VISUAL RELEVANCE
========================

The labels are objects detected in the video.

Judge whether those objects are relevant to the transcript.

IMPORTANT:

Do NOT assume an object is relevant simply because it exists.

Examples:

"I'm playing football."
labels: ["sports ball"]
→ high visual relevance

"I'm talking about my phone."
labels: ["cell phone"]
→ high visual relevance

"I'm not flat."
labels: ["kite"]
→ very low visual relevance

"I'm not flat."
labels: ["person"]
→ moderate relevance at most

labels: []
→ score based on whether the lack of detected objects
   actually hurts the clip. Do not automatically give 0.

========================
4. CONTEXT
========================

How understandable is the clip by itself?

10 = viewer can understand it immediately
5 = requires some surrounding context
0 = confusing or meaningless without missing information

========================
5. DURATION
========================

How suitable is the duration?

10 = ideal length for the idea being communicated
5 = acceptable
0 = far too short or otherwise unusable

Do not automatically give a high duration score simply
because the clip is long.

========================
IMPORTANT
========================

Judge each criterion independently.

Do not use 7 as a default.

Scores should vary depending on the actual clip.

Do not invent visual events that are not present in the labels.

Return ONLY valid JSON.

Required format:

{{
    "hook": 8,
    "transcript": 9,
    "visual_relevance": 3,
    "context": 8,
    "duration": 8,
    "reason": "Strong spoken hook,
    but the detected visual has little relationship to the statement."
)
}}

Keep the reason to one or two sentences.

========================
CLIP DATA
========================

{json.dumps(clip_data, indent=4)}
"""
