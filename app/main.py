from fastapi import FastAPI

from app.api.error_handlers import invalid_request_handler
from app.api.health import router as health_router
from app.api.middleware import log_requests
from app.core.config import settings
from app.core.exceptions import InvalidRequestError
from app.core.logging import logger


app = FastAPI(
    title=settings.app_name,
    description="Enterprise Autonomous Intelligence & Operations Platform",
    version=settings.app_version,
)


app.add_exception_handler(
    InvalidRequestError,
    invalid_request_handler,
)

app.include_router(health_router)

app.middleware("http")(log_requests)

logger.info("AegisAI application initialized")

