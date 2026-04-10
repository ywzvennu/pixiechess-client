from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import Field

from .common import CamelModel, Helmet, PlayerInfo

__all__ = ["User", "Streak", "ColorRecord", "MatchHistoryEntry", "MatchHistoryPage", "MatchTiming"]


class Streak(CamelModel):
    type: str
    count: int


class ColorRecord(CamelModel):
    wins: int
    losses: int
    draws: int
    total: int


class User(CamelModel):
    id: str = Field(alias="_id")
    username_display: str
    username: str
    address: str
    wallet_client_type: str | None = None
    helmet: Helmet
    last_login: datetime | None = None
    win_rate: int
    match_count: int
    wins: int
    losses: int
    draws: int
    casual_games: int | None = None
    streak: Streak
    color_record: dict[str, ColorRecord] = {}
    trophies: int
    rating: float
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
    rated: bool
    rating_change: float | None = None
    timing: MatchTiming


class MatchHistoryPage(CamelModel):
    matches: list[MatchHistoryEntry]
