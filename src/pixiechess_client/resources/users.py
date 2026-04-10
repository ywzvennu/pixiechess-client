from __future__ import annotations

from typing import TYPE_CHECKING

from ..models.user import MatchHistoryEntry, MatchHistoryPage, User
from ..pagination import AsyncPageIterator, PageIterator

if TYPE_CHECKING:
    from .._http import HttpClient


class UsersResource:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def get(self, identifier: str) -> User:
        data = self._http.get(f"/user/{identifier}")
        return User.model_validate(data["user"])

    async def aget(self, identifier: str) -> User:
        data = await self._http.aget(f"/user/{identifier}")
        return User.model_validate(data["user"])

    def match_history(
        self, address: str, *, limit: int = 15, page: int = 1
    ) -> MatchHistoryPage:
        data = self._http.get(
            f"/user/match-history/{address}", params={"limit": limit, "page": page}
        )
        return MatchHistoryPage.model_validate(data)

    async def amatch_history(
        self, address: str, *, limit: int = 15, page: int = 1
    ) -> MatchHistoryPage:
        data = await self._http.aget(
            f"/user/match-history/{address}", params={"limit": limit, "page": page}
        )
        return MatchHistoryPage.model_validate(data)

    def match_history_iter(
        self, address: str, *, limit: int = 15
    ) -> PageIterator[MatchHistoryEntry]:
        def fetch(page: int):
            return self._http.get(
                f"/user/match-history/{address}",
                params={"limit": limit, "page": page},
            )

        def parse(data):
            return [MatchHistoryEntry.model_validate(m) for m in data.get("matches", [])]

        return PageIterator(fetch, parse, total_pages_key=None)

    def amatch_history_iter(
        self, address: str, *, limit: int = 15
    ) -> AsyncPageIterator[MatchHistoryEntry]:
        async def fetch(page: int):
            return await self._http.aget(
                f"/user/match-history/{address}",
                params={"limit": limit, "page": page},
            )

        def parse(data):
            return [MatchHistoryEntry.model_validate(m) for m in data.get("matches", [])]

        return AsyncPageIterator(fetch, parse, total_pages_key=None)
