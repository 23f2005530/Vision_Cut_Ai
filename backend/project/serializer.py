import json
from pathlib import Path

from backend.models.project import ProjectModel


class ProjectSerializer:
    """
    Saves and loads project files.
    """

    FILE_NAME = "project.json"

    @classmethod
    def save(cls, project: ProjectModel) -> None:
        project_file = Path(project.workspace) / cls.FILE_NAME

        with open(project_file, "w", encoding="utf-8") as file:
            json.dump(
                project.model_dump(mode="json"),
                file,
                indent=4,
            )

    @classmethod
    def load(cls, workspace: str) -> ProjectModel:
        project_file = Path(workspace) / cls.FILE_NAME

        with open(project_file, encoding="utf-8") as file:
            data = json.load(file)

        project: ProjectModel = ProjectModel.model_validate(data)

        return project
