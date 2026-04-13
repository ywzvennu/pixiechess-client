from __future__ import annotations

from datetime import datetime  # noqa: TCH003 — Pydantic needs this at runtime
from typing import Any

from pydantic import Field

from .common import CamelModel

__all__ = ["EthUsdPrice", "PublicConfig", "LiveFeedEvent"]


class EthUsdPrice(CamelModel):
    usd: float


class PublicConfig(CamelModel):
    open_to_all: bool


class LiveFeedEvent(CamelModel):
    id: str = Field(alias="_id")
    type: str
    data: dict[str, Any]
    created_at: datetime
