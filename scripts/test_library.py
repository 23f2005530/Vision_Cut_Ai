from backend.database.repository import AssetRepository


def main():
    assets = AssetRepository.get_all()

    print(f"\nFound {len(assets)} assets\n")

    for asset in assets:
        print("-------------------------")
        print(asset.filename)
        print(asset.duration)
        print(asset.width, "x", asset.height)
        print(asset.id)


if __name__ == "__main__":
    main()
