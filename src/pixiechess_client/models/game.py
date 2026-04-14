from __future__ import annotations

from datetime import datetime  # noqa: TCH003 — Pydantic needs this at runtime
from typing import Any

from pydantic import Field

from .common import CamelModel

__all__ = ["GameResult", "Game", "RatingChange"]


class GameResult(CamelModel):
    code: str
    winner: int
    piece_key: str | None = None
    winner_id: str


class Game(CamelModel):
    id: str = Field(alias="_id")
    game_id: str
    board: dict[str, Any]
    players: list[dict[str, Any]] | None = None
    player_ids: dict[str, str] = {}
    player_statuses: dict[str, bool] = {}
    tournament_id: str | None = None
    status: str | None = None
    result: GameResult | None = None
    rated: bool = False
    spectator_limit: int | None = None
    game_duration_ms: int | None = None
    piece_selection_timeout_ms: int | None = None
    piece_selection_start_time: int | None = None
    finished_at: datetime | None = None
    rematch_declined: bool = False
    created_at: datetime | None = None
    updated_at: datetime | None = None


class RatingChange(CamelModel):
    rated: bool
    rating_before: float | None = None
    rating_after: float | None = None
    change: float | None = None
