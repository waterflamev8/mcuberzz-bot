import logging

from urllib.parse import quote

from discord import Embed
from discord.ext import commands
from discord_slash import cog_ext
from discord_slash.utils.manage_commands import create_choice, create_option

log = logging.getLogger(__name__)


class Algorithms(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._triggers = {
            "sexy": "R U R' U'",
            "unsexy": "U R U' R'",
            "sledge": "R' F R F'",
            "sledgehammer": "R' F R F'",
            "hedge": "F R' F' R",
            "hedgeslammer": "F R' F' R",
        }

    @cog_ext.cog_slash(
        name="alg",
        description="Visually show an algorithm on a virtual cube",
        options=[
            create_option(
                name="view",
                description="The format you want to view the cube in",
                option_type=3,
                choices=[
                    create_choice(name="plan", value="plan"),
                    create_choice(name="3d", value="3d"),
                ],
                required=True,
            ),
            create_option(
                name="algorithm",
                description="Key in algorithms",
                option_type=3,
                required=True,
            ),
        ],
        guild_ids=[794893985494597712, 844740227074883624],
    )
    async def alg(self, ctx, view, algorithm):
        await ctx.defer()  # visualcube sometimes takes too long

        for name, trigger in self._triggers.items():
            algorithm = algorithm.replace(name, trigger)

        safe_alg = quote(algorithm, safe="")
        embed = Embed(
            title=algorithm,
            url=f"https://alg.cubing.net/?alg={safe_alg}&setup=({safe_alg})-",
            colour=self.bot.primary_colour,
        )
        embed.set_image(
            url=f"http://cube.rider.biz/visualcube.php?fmt=png&size=150&pzl=3&bg=t&case={safe_alg}&view={view}"
        )
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Algorithms(bot))
