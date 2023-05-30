import discord
from discord.ext import commands
import requests


intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix="-", intents =  discord.Intents.all())

@client.command()
async def say(ctx,arg):
    await ctx.send(arg)

@client.command()
async def purge(ctx,arg):
    await ctx.channel.purge(limit=int(arg))


@client.command()
async def memes(ctx):
    r=requests.get('https://meme-api.herokuapp.com/gimme')
    json_data=r.json();
    print(json_data)
    img=list(json_data["preview"])[-1]
    embed=discord.Embed(
    description="**"+json_data["title"]+"**"+"              "+"_"+"Bot made by Salty Bear"+"_",
    colour=discord.Colour.random()
    )
    embed.set_image(url=img)
    await ctx.send(embed=embed)

# client.run('MTAzMzYwOTYyOTQzNzAxODE0NA.GY8l8E.TOgDOsObUmUkyJwqP63mvn9BVrUBroJ0eDMO_8')
