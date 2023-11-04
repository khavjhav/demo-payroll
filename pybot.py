import discord
from discord.ext import commands
import pymongo
from pymongo import MongoClient

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['attendance_db']
collection = db['attendance_data']

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def test(ctx):
    await ctx.send("Bot is working!")

bot.run('YOUR_DISCORD_TOKEN')
