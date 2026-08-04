from backend.models.project import ProjectModel


def test_project_creation():
    project = ProjectModel(name="Demo Project")

    assert project.name == "Demo Project"

    assert project.version == "0.1.0"
