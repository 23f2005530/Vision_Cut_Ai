from backend.cache.manager import CacheManager


def main():
    category = "analysis"
    key = "test_video"

    data = {
        "duration": 34.333,
        "fps": 60.0,
        "scenes": 9,
    }

    print("Saving cache...")

    CacheManager.save(
        category,
        key,
        data,
    )

    print("Checking cache...")

    print(
        "Exists:",
        CacheManager.exists(
            category,
            key,
        ),
    )

    print("Loading cache...")

    result = CacheManager.load(
        category,
        key,
    )

    print("Result:")
    print(result)


if __name__ == "__main__":
    main()
