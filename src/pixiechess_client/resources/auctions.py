from __future__ import annotations

from typing import TYPE_CHECKING, Any

from ..models.auctions import Auction, AuctionDaySummary, AuctionPieceInfo, Prices

if TYPE_CHECKING:
    from .._http import HttpClient


class AuctionsResource:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def get(self, address: str) -> Auction:
        data = self._http.get(f"/auction/{address}")
        return Auction.model_validate(data["auction"])

    async def aget(self, address: str) -> Auction:
        data = await self._http.aget(f"/auction/{address}")
        return Auction.model_validate(data["auction"])

    def active(self) -> list[Auction]:
        data = self._http.get("/auctions/active")
        return [Auction.model_validate(a) for a in data.get("auctions", [])]

    async def aactive(self) -> list[Auction]:
        data = await self._http.aget("/auctions/active")
        return [Auction.model_validate(a) for a in data.get("auctions", [])]

    def past(self, *, page: int = 1) -> list[Auction]:
        data = self._http.get("/auctions/past", params={"page": page})
        return [Auction.model_validate(a) for a in data.get("auctions", [])]

    async def apast(self, *, page: int = 1) -> list[Auction]:
        data = await self._http.aget("/auctions/past", params={"page": page})
        return [Auction.model_validate(a) for a in data.get("auctions", [])]

    def piece_info(self, piece_key: str) -> AuctionPieceInfo:
        data = self._http.get(f"/auctions/piece/{piece_key}")
        return AuctionPieceInfo.model_validate(data)

    async def apiece_info(self, piece_key: str) -> AuctionPieceInfo:
        data = await self._http.aget(f"/auctions/piece/{piece_key}")
        return AuctionPieceInfo.model_validate(data)

    def piece_daily_volume(
        self, piece_key: str, *, range: str = "30d"
    ) -> list[dict[str, Any]]:
        data = self._http.get(
            f"/auctions/piece/{piece_key}/daily-volume", params={"range": range}
        )
        return data.get("days", [])

    async def apiece_daily_volume(
        self, piece_key: str, *, range: str = "30d"
    ) -> list[dict[str, Any]]:
        data = await self._http.aget(
            f"/auctions/piece/{piece_key}/daily-volume", params={"range": range}
        )
        return data.get("days", [])

    def daily_volume(self, *, range: str = "7d") -> list[dict[str, Any]]:
        data = self._http.get("/auctions/daily-volume", params={"range": range})
        return data.get("days", [])

    async def adaily_volume(self, *, range: str = "7d") -> list[dict[str, Any]]:
        data = await self._http.aget("/auctions/daily-volume", params={"range": range})
        return data.get("days", [])

    def today_summary(self) -> AuctionDaySummary:
        data = self._http.get("/auctions/today-summary")
        return AuctionDaySummary.model_validate(data)

    async def atoday_summary(self) -> AuctionDaySummary:
        data = await self._http.aget("/auctions/today-summary")
        return AuctionDaySummary.model_validate(data)

    def last_completed_day_summary(self) -> dict[str, Any]:
        return self._http.get("/auctions/last-completed-day-summary")

    async def alast_completed_day_summary(self) -> dict[str, Any]:
        return await self._http.aget("/auctions/last-completed-day-summary")

    def prices(self) -> Prices:
        data = self._http.get("/prices")
        return Prices.model_validate(data)

    async def aprices(self) -> Prices:
        data = await self._http.aget("/prices")
        return Prices.model_validate(data)
