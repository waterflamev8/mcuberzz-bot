import logging

from discord import Embed
from discord.ext import commands
from discord_slash import cog_ext
from discord_slash.utils.manage_commands import create_choice, create_option
from pyTwistyScrambler import (
    megaminxScrambler,
    scrambler222,
    scrambler333,
    scrambler444,
    scrambler555,
    scrambler666,
    scrambler777,
)

log = logging.getLogger(__name__)


class Scrambles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(
        description="Generate scrambles (Press `enter` for 3x3, press `space` for other events)",
        options=[
            create_option(
                name="type",
                description="Type of scramble",
                option_type=3,
                choices=[
                    create_choice(name="2x2", value="2x2"),
                    create_choice(name="4x4", value="4x4"),
                    create_choice(name="5x5", value="5x5"),
                    create_choice(name="6x6", value="6x6"),
                    create_choice(name="7x7", value="7x7"),
                    create_choice(name="mega", value="mega"),
                ],
                required=False,
            )
        ],
        guild_ids=[794893985494597712, 844740227074883624],
    )
    async def scram(self, ctx, type="3x3"):
        if type == "2x2":
            msg = await ctx.send(
                embed=Embed(
                    title="2x2 Scramble",
                    description=scrambler222.get_WCA_scramble(),
                    colour=self.bot.primary_colour,
                )
            )

        elif type == "3x3":
            msg = await ctx.send(
                embed=Embed(
                    title="3x3 Scramble",
                    description=scrambler333.get_WCA_scramble(),
                    colour=self.bot.primary_colour,
                )
            )

        elif type == "4x4":
            await ctx.defer()  # scrambler444.get_WCA_scramble() is too slow 🙄
            msg = await ctx.send(
                embed=Embed(
                    title="4x4 Scramble",
                    description=scrambler444.get_WCA_scramble(),
                    colour=self.bot.primary_colour,
                )
            )

        elif type == "5x5":
            await ctx.defer()  # same here
            msg = await ctx.send(
                embed=Embed(
                    title="5x5 Scramble",
                    description=scrambler555.get_WCA_scramble(),
                    colour=self.bot.primary_colour,
                )
            )

        elif type == "6x6":
            await ctx.defer()  # same here
            msg = await ctx.send(
                embed=Embed(
                    title="6x6 Scramble",
                    description=scrambler666.get_WCA_scramble(),
                    colour=self.bot.primary_colour,
                )
            )

        elif type == "7x7":
            await ctx.defer()  # same here
            msg = await ctx.send(
                embed=Embed(
                    title="7x7 Scramble",
                    description=scrambler777.get_WCA_scramble(),
                    colour=self.bot.primary_colour,
                )
            )

        elif type == "mega":
            await ctx.defer()  # same here
            msg = await ctx.send(
                embed=Embed(
                    title="Megaminx Scramble",
                    description=megaminxScrambler.get_WCA_scramble(),
                    colour=self.bot.primary_colour,
                )
            )


def setup(bot):
    bot.add_cog(Scrambles(bot))
