import discord
from discord.ext import commands
from core.classes import Cog_Extension
import requests
import datetime

class Func(Cog_Extension):
  @commands.command()
  async def cat(self, ctx):
    # fi = discord.File('./1.jpg')
    # await ctx.send(file=fi)
    
    # response = requests.get('https://some-random-api.ml/img/cat')
    response = requests.get('https://aws.random.cat/meow')
    data = response.json()
    embed = discord.Embed(
      title = 'Cat :star_struck:',
      description = data['file'],
      color = 0xbf47ff,
      timestamp = datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))))
      # colour = discord.Colour.purple())
    embed.set_thumbnail(url='https://i.imgur.com/LJ2mVtV.png')
    embed.set_image(url=data['file'])   
    await ctx.send(embed=embed)

# 運行 bot.py 就會執行 setup
# 讓 bot 註冊我們所寫的類別
async def setup(bot):
  await bot.add_cog(Func(bot))