from discord.ext import commands
import discord

class T_Stats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        import psutil
        
    @commands.command()
    async def stats(self, ctx):
        bot = self.bot
        if ctx.author != bot.user:
            embed = discord.Embed(description="🖥️ | Machine resources information", color=0x00bbff)
            embed.add_field(name=f"Processor", value=f"Core Count: ``{psutil.cpu_count(logical=True)}``\nUsage: ``{psutil.cpu_percent()}%``", inline=True)
            embed.add_field(name=f"Memory", value=f"Total: ``{int(psutil.virtual_memory().total / 1024.0 ** 2)} MB``\nFree: ``{int(psutil.virtual_memory().free / 1024.0 ** 2)}MB ``\nPercent: ``{int(psutil.virtual_memory().percent)}%``", inline=True)
            embed.add_field(name=f"Swap", value=f"Total: ``{int(psutil.swap_memory().total / 1024.0 ** 2)} MB``\nFree: ``{int(psutil.swap_memory().free / 1024.0 ** 2)} MB``\nPercent: ``{int(psutil.swap_memory().percent)}%``", inline=True)
            embed.add_field(name=f"Network", value=f"Sent: ``{int(psutil.net_io_counters().bytes_sent / 1024.0 ** 2)} MB``\nReceived: ``{int(psutil.net_io_counters().bytes_recv / 1024.0 ** 2)} MB``", inline=True)
            embed.set_footer(text="Bot Machine Status", icon_url=ctx.guild.icon.url)
            await ctx.reply(embed=embed, mention_author=False)


async def setup(bot):
    await bot.add_cog(T_Stats(bot))

modules = {
  "psutil"
}
