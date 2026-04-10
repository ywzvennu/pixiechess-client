from __future__ import annotations

from typing import Any

from pydantic import Field

from .common import CamelModel

__all__ = ["PieceAttribute", "PieceMetadata", "Piece", "PiecesPage"]


class PieceAttribute(CamelModel):
    trait_type: str
    value: str | int | float


class PieceMetadata(CamelModel):
    name: str | None = None
    image: str | None = None
    animation_url: str | None = None
    description: str | None = None
    attributes: list[PieceAttribute] = []


class Piece(CamelModel):
    id: str = Field(alias="_id")
    collection_address: str | None = None
    token_id: int | None = None
    owner: str | None = None
    metadata: PieceMetadata | None = None
    created_at: str | None = Field(None, alias="createdAt")
    count: int | None = None

    model_config = {**CamelModel.model_config, "extra": "allow"}


class PiecesPage(CamelModel):
    pieces: list[Piece]
    total_pages: int
    current_page: int
    total_count: int
