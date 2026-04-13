from __future__ import annotations

from datetime import datetime  # noqa: TCH003 — Pydantic needs this at runtime

from pydantic import Field

from .common import CamelModel

__all__ = [
    "AuctionMetadata",
    "Auction",
    "AuctionPieceInfo",
    "VrgdaPrice",
    "InstantMintPrice",
    "AuctionDaySummary",
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


class AuctionPieceInfo(CamelModel):
    piece_key: str
    has_auction_history: bool
    total_units_sold: int
    most_recent_past_auction: dict | None = None


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


class AuctionDaySummary(CamelModel):
    pieces_sold: int
    total_sales_eth: float


class Prices(CamelModel):
    vrgda: list[VrgdaPrice]
    instant_mint: InstantMintPrice
    poll_interval_ms: int
