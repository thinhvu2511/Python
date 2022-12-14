# Write a Discord bot that
# Send a cat image every 5 minus
# Search cat image with inline command

import discord
from discord.ext import commands, tasks
import requests

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="$", intents=intents) #use bot command when we start with $
bot_Token = "Token of catBot" #Token of catBot

@tasks.loop(seconds=5) # Send messsage each 5 seconds
async def auto_send():
    response = requests.get('https://api.thecatapi.com/v1/images/search')
    data = response.json()
    channel = await bot.fetch_channel('ID of channel') # ID of channel
    await channel.send(data[0]['url'])

@bot.event
async def on_ready():
    print('Bot is ready!')
    auto_send.start()
bot.run(bot_Token)
