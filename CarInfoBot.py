import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import CarInfoSearch

#This contains the secret token our bot needs
load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print("We are good to go, {bot.user.name}")
#This will not allow the bot to reply to its own message, to avoid any potential infinite loops
@bot.event
async def on_message(message):
    if  message.author == bot.user:
        return

@bot.command(brand_name='car_brand')
async def find(ctx, brand_name):
    CarInfoSearch.search(brand_name)
    await ctx.reply(CarInfoSearch.result)

#This is what will allow the bot to run
bot.run(token, log_handler=handler,log_level=logging.DEBUG)
