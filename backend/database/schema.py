from backend.database.connection import DatabaseConnection


class DatabaseSchema:
    """
    Creates database tables.
    """

    @staticmethod
    def initialize() -> None:
        connection = DatabaseConnection.connect()

        cursor = connection.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS assets (
                id TEXT PRIMARY KEY,
                filename TEXT NOT NULL,
                filepath TEXT NOT NULL,
                media_type TEXT NOT NULL,
                file_size INTEGER,
                duration REAL,
                width INTEGER,
                height INTEGER,
                fps REAL,
                thumbnail_path TEXT,
                created_at TEXT
            )
            """
        )

        connection.commit()
        connection.close()
