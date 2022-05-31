from discord.ext import commands


# Name: Autorole
# Author: fenish#1703
# Description: Gives specified role automatically to newcomers on your server


class AutoRole(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


async def setup(bot):
    await bot.add_cog(AutoRole(bot))
