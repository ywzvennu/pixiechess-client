from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel

__all__ = ["CamelModel", "Helmet", "PlayerInfo"]


class CamelModel(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
    )


class Helmet(CamelModel):
    key: str
    color: str


class PlayerInfo(CamelModel):
    address: str
    username: str
    username_display: str
    helmet: Helmet
