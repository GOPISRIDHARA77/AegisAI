from fastapi import Request

from app.core.logging import logger


async def log_requests(request: Request, call_next):
    logger.info(f"Request started: {request.method} {request.url.path}")

    response = await call_next(request)

    logger.info(
        f"Request completed: {request.method} "
        f"{request.url.path} - {response.status_code}"
    )

    return response