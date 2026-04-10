from __future__ import annotations

from typing import TYPE_CHECKING, Any

from ..models.tournaments import Tournament, TournamentList, WaitlistEntry

if TYPE_CHECKING:
    from .._http import HttpClient


class TournamentsResource:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def list(
        self,
        *,
        limit: int = 10,
        offset: int = 0,
        pinned: bool = False,
        sort: str = "date",
        date_filter: str | None = None,
        tz_offset: int | None = None,
        active: bool | None = None,
    ) -> TournamentList:
        params: dict[str, Any] = {
            "limit": limit,
            "offset": offset,
            "pinned": str(pinned).lower(),
            "sort": sort,
        }
        if date_filter is not None:
            params["dateFilter"] = date_filter
        if tz_offset is not None:
            params["tzOffset"] = tz_offset
        if active is not None:
            params["active"] = str(active).lower()
        data = self._http.get("/tournament/list", params=params)
        return TournamentList.model_validate(data)

    async def alist(
        self,
        *,
        limit: int = 10,
        offset: int = 0,
        pinned: bool = False,
        sort: str = "date",
        date_filter: str | None = None,
        tz_offset: int | None = None,
        active: bool | None = None,
    ) -> TournamentList:
        params: dict[str, Any] = {
            "limit": limit,
            "offset": offset,
            "pinned": str(pinned).lower(),
            "sort": sort,
        }
        if date_filter is not None:
            params["dateFilter"] = date_filter
        if tz_offset is not None:
            params["tzOffset"] = tz_offset
        if active is not None:
            params["active"] = str(active).lower()
        data = await self._http.aget("/tournament/list", params=params)
        return TournamentList.model_validate(data)

    def details(self, tournament_id: str) -> Tournament:
        data = self._http.get(f"/tournament/details/{tournament_id}")
        return Tournament.model_validate(data["data"])

    async def adetails(self, tournament_id: str) -> Tournament:
        data = await self._http.aget(f"/tournament/details/{tournament_id}")
        return Tournament.model_validate(data["data"])

    def waitlist(self, tournament_id: str) -> list[WaitlistEntry]:
        data = self._http.get(f"/tournament/waitlist/{tournament_id}")
        return [WaitlistEntry.model_validate(e) for e in data]

    async def awaitlist(self, tournament_id: str) -> list[WaitlistEntry]:
        data = await self._http.aget(f"/tournament/waitlist/{tournament_id}")
        return [WaitlistEntry.model_validate(e) for e in data]
