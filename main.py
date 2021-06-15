import asyncio
import logging

from discord import Intents
from discord_slash import SlashCommand

from classes.bot import Bot

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
handler.setFormatter(logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s"))
logger.addHandler(handler)

log = logging.getLogger(__name__)

bot = Bot(command_prefix="]", intents=Intents(guilds=True, messages=True))
slash = SlashCommand(bot, sync_commands=True, sync_on_cog_reload=True, override_type=True)

loop = asyncio.get_event_loop()
loop.run_until_complete(bot.start_bot())
