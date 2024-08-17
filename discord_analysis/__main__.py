import logging
import os
from pathlib import Path

import discord
import dotenv

from discord_analysis.extractor import get_thread_messages

log = logging.getLogger(__name__)
log.setLevel(20)

log.info("loading from .env")
dotenv.load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready() -> None:
    thread_extract = await get_thread_messages(
        client,
        guild_id=int(os.environ["GUILD_ID"]),
        channel_id=int(os.environ["CHANNEL_ID"]),
        thread_id=int(os.environ["THREAD_ID"]),
    )
    Path(os.environ["OUTPUT_PATH"]).write_text(thread_extract.model_dump_json(indent=2))
    log.info("Saved output")
    await client.close()


log.info("Starting")
client.run(os.environ["DISCORD_TOKEN"])
