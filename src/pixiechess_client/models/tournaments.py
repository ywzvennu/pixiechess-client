from __future__ import annotations

from datetime import datetime  # noqa: TCH003 — Pydantic needs this at runtime
from typing import Any

from pydantic import Field

from .common import CamelModel, Helmet

__all__ = [
    "TournamentImages",
    "TournamentColors",
    "TournamentUserInfo",
    "TournamentRuleset",
    "NotificationStatus",
    "PayoutSplit",
    "Tournament",
    "TournamentList",
    "WaitlistEntry",
]


class TournamentImages(CamelModel):
    trophy: str | None = None
    title_card: str | None = None
    title_card_centered: str | None = None
    artwork: str | None = None
    artwork_cropped: str | None = None
    artwork_mobile: str | None = None


class TournamentColors(CamelModel):
    primary: str
    secondary: str
    gradient: str
    gradient_button: bool = False


class TournamentUserInfo(CamelModel):
    user_id: str | None = Field(None, alias="userId")
    username: str | None = None
    username_display: str | None = None
    helmet: Helmet | None = None
    expires: int | None = None
    chosen_pieces: list[str] = []
    free_piece_keys: list[str] = []
    confirmed_entry_tx_hash: str | None = None
    pending_burn_asset_ids: list[Any] = []


class TournamentRuleset(CamelModel):
    burn: dict[str, Any] | None = None
    gameplay: dict[str, Any] | None = None


class NotificationStatus(CamelModel):
    registration_soon: bool = False
    registration_open: bool = False
    starting_soon_for: list[str] = []
    starting_now: bool = False


class PayoutSplit(CamelModel):
    placement: int
    percentage: float


class Tournament(CamelModel):
    id: str = Field(alias="_id")
    tournament_id: str
    registration_opens: int
    start_time: int
    preset: str
    prize_amount: float
    prize_currency: str
    name: str
    description: str | None = None
    images: TournamentImages
    colors: TournamentColors
    slots: int
    pinned: bool = False
    test: bool = False
    test_pieces: list[str] = []
    enable_free_pieces: bool = False
    free_piece_keys: list[str] = []
    game_duration_ms: int | None = None
    piece_selection_timeout_ms: int | None = None
    rematch_duration_ms: int | None = None
    additional_rematch_duration_ms: int | None = None
    schedule_id: str | None = None
    schedule_position: int | None = None
    user_infos: list[TournamentUserInfo] = []
    matchups_by_round: list[Any] = []
    status: str | None = None
    ruleset: TournamentRuleset | None = None
    notification_status: NotificationStatus | None = None
    payout_mode: str | None = None
    payout_splits: list[PayoutSplit] = []
    payout_skipped_players: list[str] = []
    created_at: datetime | None = None
    updated_at: datetime | None = None

    model_config = {**CamelModel.model_config, "extra": "allow"}


class TournamentList(CamelModel):
    total_count: int
    tournaments: list[Tournament]


class WaitlistEntry(CamelModel):
    id: str = Field(alias="_id")
    tournament_id: str
    address: str
    has_been_attempted: bool = False
    created_at: datetime
    updated_at: datetime | None = None
