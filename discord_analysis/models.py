import typing as t
from datetime import datetime

from pydantic import BaseModel

if t.TYPE_CHECKING:
    import discord


class MessageExtract(BaseModel):
    author: str
    created_at: datetime
    content: str
    reaction_count: int

    @classmethod
    def from_message(cls, message: "discord.message.Message") -> t.Self:
        return cls(
            author=message.author.name,
            created_at=message.created_at,
            content=message.content,
            reaction_count=len(message.reactions),
        )


class ThreadExtract(BaseModel):
    name: str
    messages: list[MessageExtract]
