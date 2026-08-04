from backend.config.manager import ConfigManager


def test_config_creation():
    manager = ConfigManager()

    config = manager.load()

    assert config["project"]["autosave"] is True
