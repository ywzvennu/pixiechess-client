from __future__ import annotations

from datetime import datetime  # noqa: TCH003 — Pydantic needs this at runtime

from pydantic import Field

from .common import CamelModel, Helmet, PlayerInfo

__all__ = [
    "User",
    "ColorRecord",
    "MatchHistoryEntry",
    "MatchHistoryPage",
    "MatchTiming",
]


class ColorRecord(CamelModel):
    wins: int
    losses: int
    draws: int
    total: int


class User(CamelModel):
    id: str = Field(alias="_id")
    address: str
    username: str | None = None
    username_display: str | None = None
    wallet_client_type: str | None = None
    helmet: Helmet | None = None
    last_login: datetime | None = None
    win_rate: int = 0
    match_count: int = 0
    wins: int = 0
    losses: int = 0
    draws: int = 0
    casual_games: int | None = None
    streak: int = 0
    color_record: dict[str, ColorRecord] = {}
    trophies: int = 0
    rating: float = 0.0
    rd: float | None = None
    is_provisional: bool = False
    peak_rating: float | None = None
    rated_games_played: int | None = None
    points: int | None = None


class MatchTiming(CamelModel):
    white_elapsed_ms: int
    black_elapsed_ms: int
    clock_ms: int


class MatchHistoryEntry(CamelModel):
    game_id: str
    created_at: datetime
    white: PlayerInfo
    black: PlayerInfo
    winner: str | None = None
    result_for_user: str
    outcome: str
    rated: bool = False
    rating_change: float | None = None
    timing: MatchTiming


class MatchHistoryPage(CamelModel):
    matches: list[MatchHistoryEntry]
