from backend.models.project import ProjectModel


def test_project_creation():
    project = ProjectModel(
        name="Demo Project",
        workspace="storage/projects/Demo Project",
    )

    assert project.name == "Demo Project"
    assert project.workspace == "storage/projects/Demo Project"
