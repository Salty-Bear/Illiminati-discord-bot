import discord
from discord.ext import commands
import requests
import datetime


client = commands.Bot(command_prefix="-", intents =  discord.Intents.all())



@client.command()
async def codeforces(ctx):
