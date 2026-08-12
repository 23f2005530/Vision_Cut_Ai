import json

import ollama

from backend.ai.prompts import PromptBuilder


class LLMManager:
    """
    Handles communication with Ollama.
    """

    MODEL = "qwen2.5:3b"

    @classmethod
    def analyze(cls, clip):
        prompt = PromptBuilder.score_clip(clip)

        response = ollama.chat(
            model=cls.MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            format="json",
            options={
                "temperature": 0.2,
            },
        )

        content = response["message"]["content"]

        return json.loads(content)
