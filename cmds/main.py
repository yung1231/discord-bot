import discord
from discord.ext import commands
from core.classes import Cog_Extension

class Main(Cog_Extension):
  @commands.command()
  async def ping(self, ctx):
    await ctx.send(f'{round(self.bot.latency*1000)} (ms)')

  @commands.command()
  async def hi(self, ctx):
    await ctx.send('Hi')

# 運行 bot.py 就會執行 setup
# 讓 bot 註冊我們所寫的類別
async def setup(bot):
  await bot.add_cog(Main(bot))