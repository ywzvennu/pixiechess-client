from __future__ import annotations

from typing import TYPE_CHECKING

from ..models.leaderboard import LeaderboardEntry, LeaderboardPage
from ..pagination import AsyncPageIterator, PageIterator

if TYPE_CHECKING:
    from .._http import HttpClient


class LeaderboardResource:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def get(self, page: int = 1) -> LeaderboardPage:
        data = self._http.get("/leaderboard", params={"page": page})
        return LeaderboardPage.model_validate(data)

    async def aget(self, page: int = 1) -> LeaderboardPage:
        data = await self._http.aget("/leaderboard", params={"page": page})
        return LeaderboardPage.model_validate(data)

    def iter(self) -> PageIterator[LeaderboardEntry]:
        def fetch(page: int):
            return self._http.get("/leaderboard", params={"page": page})

        def parse(data):
            return [LeaderboardEntry.model_validate(e) for e in data.get("entries", [])]

        return PageIterator(fetch, parse, total_pages_key="totalPages")

    def aiter(self) -> AsyncPageIterator[LeaderboardEntry]:
        async def fetch(page: int):
            return await self._http.aget("/leaderboard", params={"page": page})

        def parse(data):
            return [LeaderboardEntry.model_validate(e) for e in data.get("entries", [])]

        return AsyncPageIterator(fetch, parse, total_pages_key="totalPages")
