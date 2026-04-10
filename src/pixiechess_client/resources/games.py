from __future__ import annotations

from typing import TYPE_CHECKING

from ..models.game import Game, RatingChange

if TYPE_CHECKING:
    from .._http import HttpClient


class GamesResource:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def get(self, game_id: str) -> Game:
        data = self._http.get(f"/game/{game_id}")
        return Game.model_validate(data)

    async def aget(self, game_id: str) -> Game:
        data = await self._http.aget(f"/game/{game_id}")
        return Game.model_validate(data)

    def rating_change(self, game_id: str, address: str) -> RatingChange:
        data = self._http.get(f"/game/{game_id}/rating/{address}")
        return RatingChange.model_validate(data)

    async def arating_change(self, game_id: str, address: str) -> RatingChange:
        data = await self._http.aget(f"/game/{game_id}/rating/{address}")
        return RatingChange.model_validate(data)
