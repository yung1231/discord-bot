import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import asyncio

load_dotenv()

# bot 是我們與 Discord 連結的橋樑
# intents 是我們要求的權限
intents = discord.Intents.default()
# intents.messages = True
intents.message_content = True
# bot = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='!', intents=intents)
# bot = commands.Bot(command_prefix='!')

# 調用 event 函式庫
# 當機器人完成啟動時
@bot.event
async def on_ready():
	await bot.change_presence(status=discord.Status.online, activity=discord.Game('努力學習中'))
	print('>> Bot is online')
	print('目前登入身份：', bot.user)

# # 當收到訊息時會觸發
# @bot.event
# async def on_message(message):
# 	# 排除自己的訊息，避免陷入無限循環
# 	if message.author == bot.user:
# 		return
	
# 	# 如果包含 ping，機器人回傳 pong
# 	if message.content == 'Hello':
# 		await message.channel.send('Hello')

# @bot.event
# async def on_member_join(member):
#     channel = bot.get_channel(558186833109057548) # 每個 channel 都有各自的 ID
#     await channel.send(f'{member} welcome welcome welcome!')

# @bot.event
# async def on_raw_reaction_add(ctx):
# 	c = bot.get_channel(ctx.channel_id)
# 	await c.send(ctx.emoji.name)

@bot.command()
async def load(ctx, extension):
  await bot.load_extension(f'cmds.{extension}')
  await ctx.send(f'Loaded {extension} done!')

@bot.command()
async def unload(ctx, extension):
  await bot.unload_extension(f'cmds.{extension}')
  await ctx.send(f'Un - Loaded {extension} done!')

@bot.command()
async def reload(ctx, extension):
  await bot.reload_extension(f'cmds.{extension}')
  await ctx.send(f'Re - Loaded {extension} done!')

# 用迴圈導入 cmds
async def load_extensions():
	for filename in os.listdir("./cmds"):
		if filename.endswith(".py"):
			# cut off the .py from the file name
			await bot.load_extension(f"cmds.{filename[:-3]}")

if __name__=='__main__':
	TOKEN = os.getenv("TOKEN")
	# bot.run(TOKEN) #TOKEN 在剛剛 Discord Developer 那邊「BOT」頁面裡面
	async def main():
		async with bot:
			await load_extensions()
			await bot.start(TOKEN)

	asyncio.run(main())