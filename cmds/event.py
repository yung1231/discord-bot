import discord
from discord.ext import commands
from core.classes import Cog_Extension

class Event(Cog_Extension):
  @commands.Cog.listener()
  async def on_message(self, msg):
    # 排除自己的訊息，避免陷入無限循環
    if msg.content == '?' and msg.author != self.bot.user:
      await msg.channel.send('???')

  @commands.Cog.listener()
  async def on_member_join(self, member):
      channel = self.bot.get_channel(558186833109057548) # 每個 channel 都有各自的 ID
      await channel.send(f'{member} welcome welcome welcome!')

  @commands.Cog.listener()
  async def on_raw_reaction_add(self, ctx):
    c = self.bot.get_channel(ctx.channel_id)
    await c.send(ctx.emoji.name)

async def setup(bot):
  await bot.add_cog(Event(bot))