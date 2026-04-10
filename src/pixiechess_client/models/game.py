from __future__ import annotations

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
    created_at: str | None = Field(None, alias="createdAt")
    updated_at: str | None = Field(None, alias="updatedAt")

    model_config = {**CamelModel.model_config, "extra": "allow"}


class RatingChange(CamelModel):
    rated: bool
    rating_before: float | None = None
    rating_after: float | None = None
    change: float | None = None
