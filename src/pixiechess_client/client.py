from __future__ import annotations

from typing import TYPE_CHECKING

from ._http import DEFAULT_BASE_URL, HttpClient

if TYPE_CHECKING:
    import httpx
from .resources.auctions import AuctionsResource
from .resources.games import GamesResource
from .resources.leaderboard import LeaderboardResource
from .resources.misc import MiscResource
from .resources.pieces import PiecesResource
from .resources.tournaments import TournamentsResource
from .resources.users import UsersResource


class PixieChessClient:
    """Synchronous client for the PixieChess API.

    Usage::

        with PixieChessClient() as client:
            user = client.users.get("username")
            lb = client.leaderboard.get()
    """

    def __init__(
        self,
        base_url: str = DEFAULT_BASE_URL,
        timeout: float = 30.0,
        http_client: httpx.Client | None = None,
    ) -> None:
        self._http = HttpClient(
            base_url=base_url, timeout=timeout, sync_client=http_client
        )
        self.users = UsersResource(self._http)
        self.games = GamesResource(self._http)
        self.leaderboard = LeaderboardResource(self._http)
        self.pieces = PiecesResource(self._http)
        self.auctions = AuctionsResource(self._http)
        self.tournaments = TournamentsResource(self._http)
        self.misc = MiscResource(self._http)

    def close(self) -> None:
        self._http.close()

    def __enter__(self) -> PixieChessClient:
        return self

    def __exit__(self, *args: object) -> None:
        self.close()


class AsyncPixieChessClient:
    """Async client for the PixieChess API.

    Usage::

        async with AsyncPixieChessClient() as client:
            user = await client.users.aget("username")
            lb = await client.leaderboard.aget()
    """

    def __init__(
        self,
        base_url: str = DEFAULT_BASE_URL,
        timeout: float = 30.0,
        http_client: httpx.AsyncClient | None = None,
    ) -> None:
        self._http = HttpClient(
            base_url=base_url, timeout=timeout, async_client=http_client
        )
        self.users = UsersResource(self._http)
        self.games = GamesResource(self._http)
        self.leaderboard = LeaderboardResource(self._http)
        self.pieces = PiecesResource(self._http)
        self.auctions = AuctionsResource(self._http)
        self.tournaments = TournamentsResource(self._http)
        self.misc = MiscResource(self._http)

    async def close(self) -> None:
        await self._http.aclose()

    async def __aenter__(self) -> AsyncPixieChessClient:
        return self

    async def __aexit__(self, *args: object) -> None:
        await self.close()
