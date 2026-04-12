from __future__ import annotations

from typing import Any

import httpx

from .exceptions import ApiError, NotFoundError

DEFAULT_BASE_URL = "https://api.pixiechess.xyz"

_DEFAULT_HEADERS = {
    "Origin": "https://www.pixiechess.xyz",
    "Referer": "https://www.pixiechess.xyz/",
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36"
    ),
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.8",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
}


def _handle_response(resp: httpx.Response) -> Any:
    if resp.status_code == 404:
        raise NotFoundError(resp.text)
    if resp.status_code >= 400:
        raise ApiError(resp.status_code, resp.text)
    if not resp.content:
        return None
    return resp.json()


class HttpClient:
    def __init__(
        self,
        base_url: str = DEFAULT_BASE_URL,
        timeout: float = 30.0,
        sync_client: httpx.Client | None = None,
        async_client: httpx.AsyncClient | None = None,
    ) -> None:
        self._base_url = base_url
        self._timeout = timeout
        self._sync = sync_client
        self._async = async_client

    @property
    def sync(self) -> httpx.Client:
        if self._sync is None:
            self._sync = httpx.Client(
                base_url=self._base_url,
                timeout=self._timeout,
                headers=_DEFAULT_HEADERS,
            )
        return self._sync

    @property
    def async_client(self) -> httpx.AsyncClient:
        if self._async is None:
            self._async = httpx.AsyncClient(
                base_url=self._base_url,
                timeout=self._timeout,
                headers=_DEFAULT_HEADERS,
            )
        return self._async

    def get(self, path: str, params: dict[str, Any] | None = None) -> Any:
        resp = self.sync.get(path, params=params)
        return _handle_response(resp)

    async def aget(self, path: str, params: dict[str, Any] | None = None) -> Any:
        resp = await self.async_client.get(path, params=params)
        return _handle_response(resp)

    def close(self) -> None:
        if self._sync is not None:
            self._sync.close()
            self._sync = None

    async def aclose(self) -> None:
        if self._async is not None:
            await self._async.aclose()
            self._async = None
