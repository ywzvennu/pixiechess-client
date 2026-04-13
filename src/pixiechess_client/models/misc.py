from __future__ import annotations

from .common import CamelModel

__all__ = ["EthUsdPrice", "PublicConfig"]


class EthUsdPrice(CamelModel):
    usd: float


class PublicConfig(CamelModel):
    open_to_all: bool
