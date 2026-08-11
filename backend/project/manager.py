from pathlib import Path

from backend.models.project import ProjectModel
from backend.project.serializer import ProjectSerializer
from backend.project.workspace import Workspace


class ProjectManager:
    """
    Creates and loads Vision Cut AI projects.
    """

    ROOT = Path("storage/projects")

    @classmethod
    def create(cls, name: str) -> ProjectModel:
        workspace_path = cls.ROOT / name

        workspace = Workspace(workspace_path)
        workspace.create()

        project = ProjectModel(
            name=name,
            workspace=str(workspace_path),
        )

        ProjectSerializer.save(project)

        return project

    @classmethod
    def open(cls, name: str) -> ProjectModel:
        workspace = cls.ROOT / name

        return ProjectSerializer.load(str(workspace))
