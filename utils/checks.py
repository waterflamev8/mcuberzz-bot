from discord.ext import commands


def is_owner():
    def predicate(ctx):
        if ctx.author.id not in ctx.bot.config.owners:
            raise commands.NotOwner()

        return True

    return commands.check(predicate)


def is_admin():
    def predicate(ctx):
        if ctx.author.id not in ctx.bot.config.owners + ctx.bot.config.admins:
            raise commands.NotOwner()

        return True

    return commands.check(predicate)
