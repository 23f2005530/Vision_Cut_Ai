from backend.project.manager import ProjectManager


def test_create_project():
    project = ProjectManager.create("Demo Project")

    assert project.name == "Demo Project"
