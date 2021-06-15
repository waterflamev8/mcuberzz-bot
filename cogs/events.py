import logging

from datetime import datetime

from discord import Embed, Game
from discord.ext import commands

log = logging.getLogger(__name__)


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        log.info(f"{self.bot.user} is online!")
        log.info("--------")

        embed = Embed(
            title="Bot Ready",
            colour=self.bot.success_colour,
            timestamp=datetime.utcnow(),
        )
        await self.bot.send_embed(self.bot.config.event_channel, embed)
        await self.bot.change_presence(activity=Game(name=self.bot.config.bot_activity))

    @commands.Cog.listener()
    async def on_shard_ready(self, shard):
        embed = Embed(
            title=f"Shard {shard} Ready",
            colour=self.bot.success_colour,
            timestamp=datetime.utcnow(),
        )
        await self.bot.send_embed(self.bot.config.event_channel, embed)

    @commands.Cog.listener()
    async def on_shard_connect(self, shard):
        embed = Embed(
            title=f"Shard {shard} Connected",
            colour=self.bot.success_colour,
            timestamp=datetime.utcnow(),
        )
        await self.bot.send_embed(self.bot.config.event_channel, embed)

    @commands.Cog.listener()
    async def on_shard_disconnect(self, shard):
        embed = Embed(
            title=f"Shard {shard} Disconnected",
            colour=self.bot.error_colour,
            timestamp=datetime.utcnow(),
        )
        await self.bot.send_embed(self.bot.config.event_channel, embed)

    @commands.Cog.listener()
    async def on_shard_resumed(self, shard):
        embed = Embed(
            title=f"Shard {shard} Resumed",
            colour=self.bot.primary_colour,
            timestamp=datetime.utcnow(),
        )
        await self.bot.send_embed(self.bot.config.event_channel, embed)


def setup(bot):
    bot.add_cog(Events(bot))
