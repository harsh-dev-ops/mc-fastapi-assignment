from fastapi import status, HTTPException
from typing import Any, Dict


class AccountNotFound(HTTPException):
    def __init__(
        self, 
        status_code: int = status.HTTP_404_NOT_FOUND, 
        detail: Any = "Account Not Found", 
        headers: Dict[str, str] | None = None
        ) -> None:
        super().__init__(
            status_code,
            detail,
            headers
        )


class AccountExist(HTTPException):
    def __init__(
        self, 
        status_code: int = status.HTTP_409_CONFLICT, 
        detail: Any = "Account exists", 
        headers: Dict[str, str] | None = None
        ) -> None:
        super().__init__(
            status_code,
            detail,
            headers
        )