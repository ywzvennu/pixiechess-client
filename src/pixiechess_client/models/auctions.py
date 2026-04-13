from __future__ import annotations

from datetime import date, datetime  # noqa: TCH003 — Pydantic needs this at runtime
from typing import cast

from pydantic import Field, field_validator

from .common import CamelModel

__all__ = [
    "AuctionMetadata",
    "Auction",
    "PastAuction",
    "AuctionPieceInfo",
    "VrgdaPrice",
    "InstantMintPrice",
    "AuctionDaySummary",
    "CompletedDaySummary",
    "DailyVolume",
    "Prices",
]


class AuctionMetadata(CamelModel):
    piece_key: str
    sub_key: str


class Auction(CamelModel):
    id: str = Field(alias="_id")
    address: str
    created_at: datetime
    end_time: int
    start_time: int
    metadata: AuctionMetadata
    type: str
    updated_at: datetime | None = None
    last_mint_price_in_wei: str | None = None


class PastAuction(Auction):
    end_date: date | None = None
    final_price: str | None = None

    @field_validator("end_date", mode="before")
    @classmethod
    def _parse_end_date(cls, v: object) -> object:
        if isinstance(v, str):
            month, day = v.split("/")
            return date(date.today().year, int(month), int(day))
        return v


class AuctionPieceInfo(CamelModel):
    piece_key: str
    has_auction_history: bool
    total_units_sold: int
    most_recent_past_auction: PastAuction | None = None


class VrgdaPrice(CamelModel):
    address: str
    price: str
    total_sold: int
    max_mints: int
    price_trend: str | None = None


class InstantMintPrice(CamelModel):
    address: str
    price: str
    total_sold: int
    max_mints: int
    price_trend: str | None = None


def _parse_date_dict(v: object) -> object:
    if isinstance(v, dict):
        d = cast("dict[str, int]", v)
        return date(d["year"], d["month"], d["day"])
    return v


class AuctionDaySummary(CamelModel):
    pieces_sold: int
    total_sales_eth: float


class CompletedDaySummary(CamelModel):
    date: date
    total_eth: float
    pieces_sold: int
    eth_change_percent: float

    _parse_date = field_validator("date", mode="before")(_parse_date_dict)


class DailyVolume(CamelModel):
    date: date
    pieces_sold: int
    total_eth: float

    _parse_date = field_validator("date", mode="before")(_parse_date_dict)


class Prices(CamelModel):
    vrgda: list[VrgdaPrice]
    instant_mint: InstantMintPrice
    poll_interval_ms: int
