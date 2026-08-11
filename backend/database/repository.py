from backend.database.connection import DatabaseConnection
from backend.models.asset import AssetModel


class AssetRepository:
    """
    Handles asset persistence.
    """

    @staticmethod
    def save(asset: AssetModel) -> None:
        connection = DatabaseConnection.connect()

        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO assets (
                id,
                filename,
                filepath,
                media_type,
                file_size,
                duration,
                width,
                height,
                fps,
                thumbnail_path,
                created_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                str(asset.id),
                asset.filename,
                asset.filepath,
                asset.media_type,
                asset.file_size,
                asset.duration,
                asset.width,
                asset.height,
                asset.fps,
                asset.thumbnail_path,
                asset.created_at.isoformat(),
            ),
        )

        connection.commit()
        connection.close()

    @staticmethod
    def get_all() -> list[AssetModel]:
        connection = DatabaseConnection.connect()

        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT *
            FROM assets
            ORDER BY created_at DESC
            """
        )

        rows = cursor.fetchall()

        connection.close()

        return [AssetModel.model_validate(dict(row)) for row in rows]

    @staticmethod
    def get_by_id(asset_id: str) -> AssetModel | None:
        connection = DatabaseConnection.connect()

        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM assets WHERE id=?",
            (asset_id,),
        )

        row = cursor.fetchone()

        connection.close()

        if row is None:
            return None

        asset: AssetModel = AssetModel.model_validate(dict(row))
        return asset

    @staticmethod
    def delete(asset_id: str) -> None:
        connection = DatabaseConnection.connect()

        cursor = connection.cursor()

        cursor.execute(
            "DELETE FROM assets WHERE id=?",
            (asset_id,),
        )

        connection.commit()
        connection.close()
