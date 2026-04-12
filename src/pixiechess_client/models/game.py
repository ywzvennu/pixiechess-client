from __future__ import annotations

from datetime import datetime  # noqa: TCH003 — Pydantic needs this at runtime
from typing import Any

from pydantic import Field

from .common import CamelModel

__all__ = ["Game", "RatingChange"]


class Game(CamelModel):
    id: str = Field(alias="_id")
    board: dict[str, Any]
    players: list[dict[str, Any]] | None = None
    status: str | None = None
    winner: int | None = None
    outcome: str | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None

    model_config = {**CamelModel.model_config, "extra": "allow"}


class RatingChange(CamelModel):
    rated: bool
    rating_before: float | None = None
    rating_after: float | None = None
    change: float | None = None
