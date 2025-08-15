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
    print(f"We are good to go, {bot.user.name}")

@bot.command(name='brand_name')
async def find(ctx, *,brand_name: str):
    result = CarInfoSearch.get_brand_info(brand_name)
    await ctx.reply(CarInfoSearch.result)

#This is what will allow the bot to run
bot.run(token, log_handler=handler,log_level=logging.DEBUG)
