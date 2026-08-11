import sqlite3
from pathlib import Path

DATABASE_DIR = Path("storage/database")
DATABASE_DIR.mkdir(parents=True, exist_ok=True)

DATABASE_PATH = DATABASE_DIR / "vision_cut.db"


class DatabaseConnection:
    """
    Handles the SQLite database connection.
    """

    @staticmethod
    def connect() -> sqlite3.Connection:
        connection = sqlite3.connect(DATABASE_PATH)
        connection.row_factory = sqlite3.Row
        return connection
