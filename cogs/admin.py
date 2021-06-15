from typing import Optional

from discord import AllowedMentions, Embed, TextChannel
from discord.ext import commands

from utils import checks


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @checks.is_admin()
    @commands.command()
    async def echo(self, ctx, channel: Optional[TextChannel], *, content: str):
        channel = channel or ctx.channel
        await ctx.message.delete()
        await channel.send(content, allowed_mentions=AllowedMentions(everyone=False))

    @checks.is_admin()
    @commands.command()
    async def embed(self, ctx, channel: Optional[TextChannel], *, content: str):
        channel = channel or ctx.channel
        await ctx.message.delete()
        await channel.send(
            embed=Embed(description=content, colour=self.bot.primary_colour),
            allowed_mentions=AllowedMentions(everyone=False),
        )
