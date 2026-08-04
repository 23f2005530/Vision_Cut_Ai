from backend.assets.manager import AssetManager


def test_import_asset(tmp_path):
    video = tmp_path / "demo.mp4"

    video.write_bytes(b"123")

    manager = AssetManager()

    asset = manager.import_asset(str(video))

    assert asset.filename == "demo.mp4"

    assert asset.media_type == "video"

    assert asset.file_size == 3
