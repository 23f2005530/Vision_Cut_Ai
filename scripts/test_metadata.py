from backend.assets.manager import AssetManager


def main():
    manager = AssetManager()

    asset = manager.import_asset("storage/samples/test.mp4")

    print(asset.model_dump_json(indent=4))


if __name__ == "__main__":
    main()
