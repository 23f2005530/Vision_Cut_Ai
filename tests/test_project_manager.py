from pathlib import Path

from backend.project.manager import ProjectManager


def test_create_project(tmp_path: Path):
    manager = ProjectManager()

    project = manager.create_project(
        "Demo",
        str(tmp_path),
    )

    assert project.name == "Demo"

    assert (tmp_path / "Demo.vca").exists()

    assert (tmp_path / "Demo.vca" / "assets").exists()

    assert (tmp_path / "Demo.vca" / "analysis").exists()
