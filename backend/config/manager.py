import json
from pathlib import Path

from backend.config.defaults import DEFAULT_CONFIG


class ConfigManager:
    def __init__(self):
        self.config_path = Path("storage/config.json")

        self.config_path.parent.mkdir(parents=True, exist_ok=True)

        if not self.config_path.exists():
            self.save(DEFAULT_CONFIG)

    def load(self):
        with open(self.config_path) as f:
            return json.load(f)

    def save(self, config):
        with open(self.config_path, "w") as f:
            json.dump(config, f, indent=4)
