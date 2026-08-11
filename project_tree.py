from pathlib import Path

ROOT = Path("backend")

IGNORE_DIRS = {
    "__pycache__",
    ".git",
    ".venv",
    "storage",
    "models",  # AI weights
    "thumbnails",
    "uploads",
    "samples",
}


def walk(path: Path, indent=""):
    entries = sorted(path.iterdir(), key=lambda p: (p.is_file(), p.name.lower()))

    entries = [e for e in entries if e.name not in IGNORE_DIRS]

    for i, entry in enumerate(entries):
        last = i == len(entries) - 1
        branch = "└── " if last else "├── "

        if entry.is_dir():
            print(indent + branch + entry.name + "/")
            walk(entry, indent + ("    " if last else "│   "))

        elif entry.suffix == ".py":
            print(indent + branch + entry.name)


print("backend/")
walk(ROOT)
