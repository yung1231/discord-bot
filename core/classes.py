import discord
from discord.ext import commands

# 之後只要其他 class 要使用，就先來繼承此 class
class Cog_Extension(commands.Cog):
  def __init__(self, bot):
    self.bot = bot