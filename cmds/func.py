import discord
from discord.ext import commands
from core.classes import Cog_Extension
import requests

class Func(Cog_Extension):
  @commands.command()
  async def cat(self, ctx):
    # fi = discord.File('./1.jpg')
    # await ctx.send(file=fi)
    
    # response = requests.get('https://some-random-api.ml/img/cat')
    response = requests.get('https://aws.random.cat/meow')
    data = response.json()
    embed = discord.Embed(
      title = 'Cat 🐈',
      description = ':star_struck: :star_struck: :star_struck:',
      colour = discord.Colour.purple())
    embed.set_image(url=data['file'])            
    embed.set_footer(text="")
    await ctx.send(embed=embed)

# 運行 bot.py 就會執行 setup
# 讓 bot 註冊我們所寫的類別
async def setup(bot):
  await bot.add_cog(Func(bot))