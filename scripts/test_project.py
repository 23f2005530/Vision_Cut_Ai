from backend.project.manager import ProjectManager


def main():
    project = ProjectManager.create("Demo Project")

    print(project.model_dump_json(indent=4))

    loaded = ProjectManager.open("Demo Project")

    print("\nLoaded Project:\n")
    print(loaded.model_dump_json(indent=4))


if __name__ == "__main__":
    main()
