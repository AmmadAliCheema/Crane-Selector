from fastapi import FastAPI

from app.api.routes_cranes import router as cranes_router
from app.api.routes_selection import router as selection_router
from app.core.config import settings
from app.db.database import Base, engine
from app import models  # noqa: F401


Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.app_name, version=settings.app_version)


@app.get("/")
def root():
    return {"message": "Crane Selector API is running successfully."}


@app.get("/health")
def health_check():
    return {"status": "ok"}


app.include_router(selection_router, prefix=settings.api_v1_prefix)
app.include_router(cranes_router, prefix=settings.api_v1_prefix)
