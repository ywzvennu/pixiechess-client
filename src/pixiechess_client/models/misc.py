from __future__ import annotations

from .common import CamelModel

__all__ = ["EthUsdPrice"]


class EthUsdPrice(CamelModel):
    usd: float
