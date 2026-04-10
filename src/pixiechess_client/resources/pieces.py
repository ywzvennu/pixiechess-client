from __future__ import annotations

from typing import TYPE_CHECKING, Any

from ..models.pieces import Piece, PiecesPage
from ..pagination import AsyncPageIterator, PageIterator

if TYPE_CHECKING:
    from .._http import HttpClient


def _pieces_params(
    page: int, limit: int | None = None, grouped: bool = False
) -> dict[str, Any]:
    params: dict[str, Any] = {"page": page}
    if limit is not None:
        params["limit"] = limit
    if grouped:
        params["grouped"] = "true"
    return params


def _burned_params(page: int, limit: int | None = None) -> dict[str, Any]:
    params: dict[str, Any] = {"page": page}
    if limit is not None:
        params["limit"] = limit
    return params


class PiecesResource:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def get(
        self,
        address: str,
        *,
        page: int = 1,
        limit: int | None = None,
        grouped: bool = False,
    ) -> PiecesPage:
        data = self._http.get(
            f"/pieces/{address}", params=_pieces_params(page, limit, grouped)
        )
        return PiecesPage.model_validate(data)

    async def aget(
        self,
        address: str,
        *,
        page: int = 1,
        limit: int | None = None,
        grouped: bool = False,
    ) -> PiecesPage:
        data = await self._http.aget(
            f"/pieces/{address}", params=_pieces_params(page, limit, grouped)
        )
        return PiecesPage.model_validate(data)

    def burned(
        self, address: str, *, page: int = 1, limit: int | None = None
    ) -> PiecesPage:
        data = self._http.get(
            f"/burned-pieces/{address}", params=_burned_params(page, limit)
        )
        return PiecesPage.model_validate(data)

    async def aburned(
        self, address: str, *, page: int = 1, limit: int | None = None
    ) -> PiecesPage:
        data = await self._http.aget(
            f"/burned-pieces/{address}", params=_burned_params(page, limit)
        )
        return PiecesPage.model_validate(data)

    def iter(
        self, address: str, *, limit: int | None = None, grouped: bool = False
    ) -> PageIterator[Piece]:
        def fetch(page: int):
            return self._http.get(
                f"/pieces/{address}", params=_pieces_params(page, limit, grouped)
            )

        def parse(data):
            return [Piece.model_validate(p) for p in data.get("pieces", [])]

        return PageIterator(fetch, parse, total_pages_key="totalPages")

    def aiter(
        self, address: str, *, limit: int | None = None, grouped: bool = False
    ) -> AsyncPageIterator[Piece]:
        async def fetch(page: int):
            return await self._http.aget(
                f"/pieces/{address}", params=_pieces_params(page, limit, grouped)
            )

        def parse(data):
            return [Piece.model_validate(p) for p in data.get("pieces", [])]

        return AsyncPageIterator(fetch, parse, total_pages_key="totalPages")

    def burned_iter(
        self, address: str, *, limit: int | None = None
    ) -> PageIterator[Piece]:
        def fetch(page: int):
            return self._http.get(
                f"/burned-pieces/{address}", params=_burned_params(page, limit)
            )

        def parse(data):
            return [Piece.model_validate(p) for p in data.get("pieces", [])]

        return PageIterator(fetch, parse, total_pages_key="totalPages")

    def aburned_iter(
        self, address: str, *, limit: int | None = None
    ) -> AsyncPageIterator[Piece]:
        async def fetch(page: int):
            return await self._http.aget(
                f"/burned-pieces/{address}", params=_burned_params(page, limit)
            )

        def parse(data):
            return [Piece.model_validate(p) for p in data.get("pieces", [])]

        return AsyncPageIterator(fetch, parse, total_pages_key="totalPages")
