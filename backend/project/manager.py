from pathlib import Path

from backend.models.project import ProjectModel
from backend.project.workspace import Workspace


class ProjectManager:
    """
    Creates and manages Vision Cut AI projects.
    """

    def create_project(
        self,
        name: str,
        location: str,
    ) -> ProjectModel:
        root = Path(location) / f"{name}.vca"

        workspace = Workspace(root)
        workspace.create()

        project = ProjectModel(
            name=name,
            project_path=str(root),
        )

        return project
