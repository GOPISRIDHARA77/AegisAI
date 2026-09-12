from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(
    title = settings.app_name,
    description = "Enterprise Autonomous Intelligence AND Operational platform",
    version=settings.app_version
)

@app.get("/health")
def health_check():
    return {
        "status":"healthy",
        "environment": settings.environment,
        }