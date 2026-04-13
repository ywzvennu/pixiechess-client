from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Any

from ..models.misc import EthUsdPrice, PublicConfig

if TYPE_CHECKING:
    from .._http import HttpClient


class MiscResource:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def config(self) -> PublicConfig:
        data = self._http.get("/config/public")
        return PublicConfig.model_validate(data)

    async def aconfig(self) -> PublicConfig:
        data = await self._http.aget("/config/public")
        return PublicConfig.model_validate(data)

    def eth_usd_price(self) -> EthUsdPrice:
        data = self._http.get("/eth-usd-price")
        return EthUsdPrice.model_validate(data)

    async def aeth_usd_price(self) -> EthUsdPrice:
        data = await self._http.aget("/eth-usd-price")
        return EthUsdPrice.model_validate(data)

    def vault_balance(self) -> str:
        data = self._http.get("/vault-balance")
        return data["balance"]

    async def avault_balance(self) -> str:
        data = await self._http.aget("/vault-balance")
        return data["balance"]

    def live_feed(
        self,
        *,
        since: datetime | str | None = None,
        type: str | None = None,
        limit: int | None = None,
    ) -> list[dict[str, Any]]:
        params: dict[str, Any] = {}
        if since is not None:
            params["since"] = (
                since.isoformat() if isinstance(since, datetime) else since
            )
        if type is not None:
            params["type"] = type
        if limit is not None:
            params["limit"] = limit
        return self._http.get("/live-feed", params=params)

    async def alive_feed(
        self,
        *,
        since: datetime | str | None = None,
        type: str | None = None,
        limit: int | None = None,
    ) -> list[dict[str, Any]]:
        params: dict[str, Any] = {}
        if since is not None:
            params["since"] = (
                since.isoformat() if isinstance(since, datetime) else since
            )
        if type is not None:
            params["type"] = type
        if limit is not None:
            params["limit"] = limit
        return await self._http.aget("/live-feed", params=params)
