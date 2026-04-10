from __future__ import annotations

from typing import TYPE_CHECKING

from ..models.pieces import Piece, PiecesPage
from ..pagination import AsyncPageIterator, PageIterator

if TYPE_CHECKING:
    from .._http import HttpClient


class PiecesResource:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def get(
        self, address: str, *, page: int = 1, grouped: bool = False
    ) -> PiecesPage:
        params: dict = {"page": page}
        if grouped:
            params["grouped"] = "true"
        data = self._http.get(f"/pieces/{address}", params=params)
        return PiecesPage.model_validate(data)

    async def aget(
        self, address: str, *, page: int = 1, grouped: bool = False
    ) -> PiecesPage:
        params: dict = {"page": page}
        if grouped:
            params["grouped"] = "true"
        data = await self._http.aget(f"/pieces/{address}", params=params)
        return PiecesPage.model_validate(data)

    def burned(self, address: str, *, page: int = 1) -> PiecesPage:
        data = self._http.get(f"/burned-pieces/{address}", params={"page": page})
        return PiecesPage.model_validate(data)

    async def aburned(self, address: str, *, page: int = 1) -> PiecesPage:
        data = await self._http.aget(
            f"/burned-pieces/{address}", params={"page": page}
        )
        return PiecesPage.model_validate(data)

    def iter(
        self, address: str, *, grouped: bool = False
    ) -> PageIterator[Piece]:
        def fetch(page: int):
            params: dict = {"page": page}
            if grouped:
                params["grouped"] = "true"
            return self._http.get(f"/pieces/{address}", params=params)

        def parse(data):
            return [Piece.model_validate(p) for p in data.get("pieces", [])]

        return PageIterator(fetch, parse, total_pages_key="totalPages")

    def aiter(
        self, address: str, *, grouped: bool = False
    ) -> AsyncPageIterator[Piece]:
        async def fetch(page: int):
            params: dict = {"page": page}
            if grouped:
                params["grouped"] = "true"
            return await self._http.aget(f"/pieces/{address}", params=params)

        def parse(data):
            return [Piece.model_validate(p) for p in data.get("pieces", [])]

        return AsyncPageIterator(fetch, parse, total_pages_key="totalPages")

    def burned_iter(self, address: str) -> PageIterator[Piece]:
        def fetch(page: int):
            return self._http.get(f"/burned-pieces/{address}", params={"page": page})

        def parse(data):
            return [Piece.model_validate(p) for p in data.get("pieces", [])]

        return PageIterator(fetch, parse, total_pages_key="totalPages")

    def aburned_iter(self, address: str) -> AsyncPageIterator[Piece]:
        async def fetch(page: int):
            return await self._http.aget(
                f"/burned-pieces/{address}", params={"page": page}
            )

        def parse(data):
            return [Piece.model_validate(p) for p in data.get("pieces", [])]

        return AsyncPageIterator(fetch, parse, total_pages_key="totalPages")
