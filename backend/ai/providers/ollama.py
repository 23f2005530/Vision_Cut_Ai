import requests

from backend.ai.providers.base import BaseLLM


class OllamaProvider(BaseLLM):
    def __init__(
        self,
        model="qwen3:8b",
        url="http://localhost:11434/api/generate",
    ):
        self.model = model
        self.url = url

    def generate(self, prompt: str):
        response = requests.post(
            self.url,
            json={
                "model": self.model,
                "prompt": prompt,
                "stream": False,
            },
        )

        response.raise_for_status()

        return response.json()["response"]
