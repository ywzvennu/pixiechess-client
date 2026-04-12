from __future__ import annotations

from .common import CamelModel, Helmet

__all__ = [
    "LeaderboardEntry",
    "LeaderboardPage",
    "LeaderboardStats",
    "PointsLeaderboardEntry",
    "PointsLeaderboardPage",
]


class LeaderboardEntry(CamelModel):
    rank: int
    address: str
    username: str
    username_display: str
    helmet: Helmet | None = None
    rating: float
    is_provisional: bool
    games_played: int
    wins: int
    streak: int
    is_online: bool
    is_in_game: bool


class LeaderboardStats(CamelModel):
    total_ranked_players: int
    games_today: int
    active_now: int


class LeaderboardPage(CamelModel):
    entries: list[LeaderboardEntry]
    total_count: int
    page: int
    total_pages: int
    current_user: dict | None = None
    stats: LeaderboardStats | None = None


class PointsLeaderboardEntry(CamelModel):
    rank: int
    address: str
    username: str
    username_display: str
    helmet: Helmet | None = None
    total_points: int
    today: int
    this_week: int
    rank_change: int
    is_online: bool


class PointsLeaderboardPage(CamelModel):
    entries: list[PointsLeaderboardEntry]
    total_count: int
    page: int
    total_pages: int
    current_user: dict | None = None
