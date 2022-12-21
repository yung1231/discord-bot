import discord
from discord.ext import commands
from core.classes import Cog_Extension
import requests

class Func(Cog_Extension):
  pass

# 運行 bot.py 就會執行 setup
# 讓 bot 註冊我們所寫的類別
async def setup(bot):
  await bot.add_cog(Func(bot))