import discord

from discord_analysis.models import MessageExtract, ThreadExtract


async def get_thread_messages(
    client: "discord.Client", *, guild_id: int, channel_id: int, thread_id: int
) -> ThreadExtract:
    guild = client.get_guild(guild_id)
    if guild is None:
        msg = "Guild not found"
        raise ValueError(msg)

    channel = guild.get_channel(channel_id)
    match channel:
        case None:
            msg = "Channel not found"
            raise ValueError(msg)
        case discord.VoiceChannel | discord.StageChannel | discord.CategoryChannel:
            msg = "Channel is not a text channel"
            raise TypeError(msg)
        case _:
            thread = channel.get_thread(thread_id)

    if thread is None:
        msg = "Thread not found"
        raise ValueError(msg)

    messages = [message async for message in thread.history(oldest_first=True)]
    messages_extract = [MessageExtract.from_message(message) for message in messages]
    return ThreadExtract(name=thread.name, messages=messages_extract)
