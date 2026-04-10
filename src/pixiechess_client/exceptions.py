from __future__ import annotations


class PixieChessError(Exception):
    pass


class NotFoundError(PixieChessError):
    pass


class ApiError(PixieChessError):
    def __init__(self, status_code: int, detail: str = ""):
        self.status_code = status_code
        self.detail = detail
        super().__init__(f"HTTP {status_code}: {detail}")
