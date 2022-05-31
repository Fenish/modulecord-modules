import psutil
import discord
from discord.ext import commands


class PsutilStats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def botstats(self, ctx):
        lang = self.bot.locale["PsutilStats"]
        embed = discord.Embed(title="🖥️ " + lang["title"], color=0x00bbff)
        embed.add_field(name=lang["processor"],
                        value=f"{lang['corecount']}: `{psutil.cpu_count(logical=True)}`\n"
                              f"{lang['usage']}: `{psutil.cpu_percent()}`",
                        inline=True)

        embed.add_field(name=lang["memory"],
                        value=f"{lang['total']}: `{int(psutil.virtual_memory().total / 1024.0 ** 2)}`\n"
                              f"{lang['free']}: `{int(psutil.virtual_memory().free / 1024.0 ** 2)}`\n"
                              f"{lang['percent']}: `{int(psutil.virtual_memory().percent)}`",
                        inline=True)

        embed.add_field(name=lang['swap'],
                        value=f"{lang['total']}: `{int(psutil.swap_memory().total / 1024.0 ** 2)}`\n"
                              f"{lang['free']}: `{int(psutil.swap_memory().free / 1024.0 ** 2)}`\n"
                              f"{lang['percent']}: `{int(psutil.swap_memory().percent)}`",
                        inline=True)

        embed.add_field(name=lang["network"],
                        value=f"{lang['sent']}: `{int(psutil.net_io_counters().bytes_sent / 1024.0 ** 2)}`\n"
                              f"{lang['received']}: `{int(psutil.net_io_counters().bytes_recv / 1024.0 ** 2)}`",
                        inline=True)
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(PsutilStats(bot))
