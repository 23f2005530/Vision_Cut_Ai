from fastapi import FastAPI

from backend.core.settings import settings
from backend.database.schema import DatabaseSchema

DatabaseSchema.initialize()


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)


@app.get("/")
def root():
    return {
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "running",
    }
