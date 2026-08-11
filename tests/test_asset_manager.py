from backend.assets.manager import AssetManager


def test_import_asset():
    manager = AssetManager()

    asset = manager.import_asset("storage/samples/test.mp4")

    assert asset.filename == "test.mp4"
    assert asset.media_type == "video"
    assert asset.duration > 0
    assert asset.width > 0
    assert asset.height > 0
