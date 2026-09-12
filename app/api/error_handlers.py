from fastapi import Request
from fastapi.responses import JSONResponse

from app.core.exceptions import InvalidRequestError


async def invalid_request_handler(
    request: Request,
    exc: InvalidRequestError,
):
    return JSONResponse(
        status_code=400,
        content={
            "error": "invalid_request",
            "message": str(exc),
        },
    )