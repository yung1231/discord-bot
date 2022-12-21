import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv()

intents = discord.Intents.default()
# intents.messages = True
intents.message_content = True
# client = discord.Client(intents=intents)
client=commands.Bot(command_prefix=".", intents=intents)

@client.event
async def on_ready():
    print('>> Bot is online')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    print('message.content: ', len(message.content))
    if message.content == '$hello':
        await message.channel.send('Hello')

@client.command
async def hi(ctx):
    await ctx.send('Hi')

TOKEN = os.getenv("TOKEN")
client.run(TOKEN)
