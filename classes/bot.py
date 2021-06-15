import logging
import sys
import traceback

from discord.ext.commands import AutoShardedBot

import config

log = logging.getLogger(__name__)


class Bot(AutoShardedBot):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.config = config
        self.redis = None

        self._cogs = ["admin", "algorithms", "events", "owner", "scrambles"]

    @property
    def primary_colour(self):
        return self.config.bot_primary_colour

    @property
    def success_colour(self):
        return self.config.bot_success_colour

    @property
    def error_colour(self):
        return self.config.bot_error_colour

    async def send_embed(self, channel_id, embed):
        await self.http.send_message(channel_id, None, embed=embed.to_dict())

    async def start_bot(self):
        for cog in self._cogs:
            try:
                self.load_extension(f"cogs.{cog}")
            except Exception:
                log.error(f"Failed to load extension {cog}.", file=sys.stderr)
                log.error(traceback.print_exc())

        log.info("Starting...")

        await self.start(self.config.bot_token)
