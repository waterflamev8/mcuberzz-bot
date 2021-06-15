import copy
import io
import logging
import subprocess
import textwrap
import traceback

from contextlib import redirect_stdout
from typing import Optional

from discord import AllowedMentions, Embed, Forbidden, Member, TextChannel
from discord.ext import commands

from utils import checks

log = logging.getLogger(__name__)


class Owner(commands.Cog):
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

    @checks.is_owner()
    @commands.command()
    async def _eval(self, ctx, *, body: str):
        env = {
            "bot": self.bot,
            "ctx": ctx,
            "channel": ctx.channel,
            "author": ctx.author,
            "guild": ctx.guild,
            "message": ctx.message,
        }
        env.update(globals())

        if body.startswith("```") and body.endswith("```"):
            body = "\n".join(body.split("\n")[1:-1])
        body = body.strip("` \n")

        try:
            exec(f"async def func():\n{textwrap.indent(body, '  ')}", env)
        except Exception as e:
            await ctx.send(
                embed=Embed(
                    description=f"```py\n{e.__class__.__name__}: {e}\n```",
                    colour=self.bot.error_colour,
                )
            )
            return

        func = env["func"]
        stdout = io.StringIO()

        try:
            with redirect_stdout(stdout):
                ret = await func()
        except Exception:
            await ctx.send(
                embed=Embed(
                    description=f"```py\n{stdout.getvalue()}{traceback.format_exc()}\n```",
                    colour=self.bot.error_colour,
                )
            )
            return

        try:
            await ctx.message.add_reaction("✅")
        except Forbidden:
            pass

        value = stdout.getvalue()

        if ret is not None:
            await ctx.send(
                embed=Embed(
                    description=f"```py\n{value}{ret}\n```",
                    colour=self.bot.primary_colour,
                )
            )
        elif value is not None:
            await ctx.send(
                embed=Embed(description=f"```py\n{value}\n```", colour=self.bot.primary_colour)
            )

    @checks.is_owner()
    @commands.command()
    async def bash(self, ctx, *, command: str):
        try:
            output = subprocess.check_output(command.split(), stderr=subprocess.STDOUT).decode(
                "utf-8"
            )
            await ctx.send(
                embed=Embed(description=f"```py\n{output}\n```", colour=self.bot.primary_colour)
            )
        except Exception as error:
            await ctx.send(
                embed=Embed(
                    description=f"```py\n{error.__class__.__name__}: {error}\n```",
                    colour=self.bot.error_colour,
                )
            )

    @checks.is_owner()
    @commands.command()
    async def invoke(
        self,
        ctx,
        channel: Optional[TextChannel],
        member: Member,
        *,
        command: str,
    ):
        msg = copy.copy(ctx.message)
        channel = channel or ctx.channel
        msg.channel = channel
        msg.author = member
        msg.content = ctx.prefix + command

        await self.bot.invoke(await self.bot.get_context(msg, cls=type(ctx)))


def setup(bot):
    bot.add_cog(Owner(bot))
