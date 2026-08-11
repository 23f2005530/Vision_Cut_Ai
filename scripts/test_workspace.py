from pathlib import Path

from backend.project.workspace import Workspace


def main():
    workspace = Workspace(Path("storage/projects/My First Project"))
    workspace.create()

    print(workspace.root)


if __name__ == "__main__":
    main()
