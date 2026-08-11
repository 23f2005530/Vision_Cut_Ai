from backend.assets.manager import AssetManager
from backend.database.repository import AssetRepository
from backend.database.schema import DatabaseSchema


def main():
    DatabaseSchema.initialize()

    manager = AssetManager()

    asset = manager.import_asset("storage/samples/test.mp4")

    AssetRepository.save(asset)

    print("\n=== Import Completed ===")
    print(asset.model_dump_json(indent=4))


if __name__ == "__main__":
    main()
