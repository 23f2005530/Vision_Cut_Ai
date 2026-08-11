from backend.ai.llm import LLMManager
from backend.timeline.clip import ClipModel

clip = ClipModel(
    asset_id="test-video",
    start=0,
    end=6,
    duration=6,
    transcript="IShowSpeed reacts to himself in Minecraft.",
    labels=["person", "minecraft"],
)

result = LLMManager.analyze(clip)

print(result)
