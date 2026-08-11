from backend.analysis.manager import AnalysisManager
from backend.analysis.serializer import AnalysisSerializer


def main():
    workspace = "storage/projects/Demo Project"

    analysis = AnalysisManager.analyze("storage/samples/test.mp4")

    AnalysisSerializer.save(
        analysis,
        workspace,
    )

    loaded = AnalysisSerializer.load(workspace)

    print(loaded.model_dump_json(indent=4))


if __name__ == "__main__":
    main()
