from fastapi import Request
from fastapi.responses import JSONResponse

class ExceptionHandler(Exception):
    def __init__(self, status_code: int, message: str):
        self.status_code = status_code
        self.message = message


async def exception_handler(request: Request, exc: ExceptionHandler) -> JSONResponse:
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.message},
    )
