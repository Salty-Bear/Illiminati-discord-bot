# This example requires the 'message_content' intent.
import discord
import os
import requests
from discord.ext import commands
from discord import activity

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix="-", intents =  discord.Intents.all())

chk=False;
chk1=False;

@client.event
async def on_ready():
    print(f'Logged on as {client.user}!')
    # async with aiosqlite.connect("main.db") as db:
    #     async with db.cursor() as cursor:
    #         await cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER , guild INTEGER)')
    #     await db.commit();


# @client.event
# async def on_message(message):
#     print(f'{message.author} : {message.content}')
#     if(message.author==client.user):
#         return

@client.command()
async def say(ctx,arg):
    await ctx.send(arg)

@client.command()
async def purge(ctx,arg):
    await ctx.channel.purge(limit=int(arg))

############## MEMES #####################################


@client.command()
async def memes(ctx,arg):
    if (int(arg)>5):
        await ctx.send("too many memes, can spam the channel boi");
        return
    for i in range(0,int(arg)):
        r=requests.get('https://meme-api.com/gimme')
        json_data=r.json();
        img=list(json_data["preview"])[-1]
        embed=discord.Embed(
        description="**"+json_data["title"]+"**"+"              "+"_"+"Bot made by Salty Bear"+"_",
        colour=discord.Colour.random()
        )
        embed.set_image(url=img)
        await ctx.send(embed=embed)

@client.command()
async def meme(ctx):
        r=requests.get('https://meme-api.com/gimme')
        json_data=r.json();
        img=list(json_data["preview"])[-1]
        embed=discord.Embed(
        description="**"+json_data["title"]+"**"+"              "+"_"+"Bot made by Salty Bear"+"_",
        colour=discord.Colour.random()
        )
        embed.set_image(url=img)
        await ctx.send(embed=embed)

@client.command(brief="Drops memes autimatically in that channel ",description="-automemetrue {arg (integer)}")
async def automemetrue(ctx,arg):
    await ctx.send(f"`Auto MEME : TRUE  ||   Delay Time: {int(arg)} minutes`")
    chk=True;
    while(chk):
        await meme(ctx)
        await asyncio.sleep(int(arg)*60)
        if(chk1): break;

@client.command(brief="Stops the automeme feat. " , description="simply type the command duh, is it that hard?")
async def automemefalse(ctx):
    await ctx.send("`Auto MEME : FALSE`")
    chk1=False;
############## MEMES #####################################

@client.command()
async def codeforces(ctx):
    r=requests.get('https://kontests.net/api/v1/codeforces')
    json_data=r.json();
    print(json_data)
    for i in json_data:
        name=i["name"]
        start_time=i["start_time"]
        end_time=i["end_time"]
        duration=i["duration"]
        url=i["url"]
        embed=discord.Embed(
        title=name,
        description=(f'`Start time : {start_time[11:20]} || {start_time[0:10]}` \n  \n `End-Time : {end_time[11:20]} || {end_time[0:10]} `'),
        url=url
        )
        embed.set_thumbnail(url='https://cdn.iconscout.com/icon/free/png-256/code-forces-3628695-3029920.png')
        await ctx.send(embed=embed)

@client.command()
async def codechef(ctx):
    r=requests.get('https://kontests.net/api/v1/code_chef')
    json_data=r.json();
    print(json_data)
    for i in json_data:
        name=i["name"]
        start_time=i["start_time"]
        end_time=i["end_time"]
        duration=i["duration"]
        url=i["url"]
        embed=discord.Embed(
        title=name,
        description=(f'`Start time : {start_time[10:20]} || {start_time[0:10]}` \n  \n `End-Time : {end_time[12:20]} || {end_time[0:10]} `'),
        url=url
        )
        embed.set_thumbnail(url='https://i.pinimg.com/originals/c5/d9/fc/c5d9fc1e18bcf039f464c2ab6cfb3eb6.jpg')
        await ctx.send(embed=embed)


@client.command()
async def leetcode(ctx):
    r=requests.get('https://kontests.net/api/v1/leet_code')
    json_data=r.json();
    print(json_data)
    for i in json_data:
        name=i["name"]
        start_time=i["start_time"]
        end_time=i["end_time"]
        duration=i["duration"]
        url=i["url"]
        embed=discord.Embed(
        title=name,
        description=(f'`Start time : {start_time[12:20]} || {start_time[0:10]}` \n  \n `End-Time : {end_time[12:20]} || {end_time[0:10]} `'),
        url=url
        )
        embed.set_thumbnail(url='https://leetcode.com/static/images/LeetCode_logo_rvs.png')
        await ctx.send(embed=embed)

@client.command()
async def kickstart(ctx):
    r=requests.get('https://kontests.net/api/v1/kick_start')
    json_data=r.json();
    print(json_data)
    for i in json_data:
        name=i["name"]
        start_time=i["start_time"]
        end_time=i["end_time"]
        duration=i["duration"]
        url=i["url"]
        embed=discord.Embed(
        title=name,
        description=(f'`Start time : {start_time[12:20]} || {start_time[0:10]}` \n  \n `End-Time : {end_time[12:20]} || {end_time[0:10]} `'),
        url=url
        )
        embed.set_thumbnail(url='https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Google_%22G%22_Logo.svg/2048px-Google_%22G%22_Logo.svg.png')
        await ctx.send(embed=embed)

@client.command()
async def atcoder(ctx):
    r=requests.get('https://kontests.net/api/v1/at_coder')
    json_data=r.json();
    print(json_data)
    for i in json_data:
        name=i["name"]
        start_time=i["start_time"]
        end_time=i["end_time"]
        duration=i["duration"]
        url=i["url"]
        embed=discord.Embed(
        title=name,
        description=(f'`Start time : {start_time[12:20]} || {start_time[0:10]}` \n  \n `End-Time : {end_time[12:20]} || {end_time[0:10]} `'),
        url=url
        )
        embed.set_thumbnail(url='https://img.atcoder.jp/assets/atcoder.png')
        await ctx.send(embed=embed)

################################################    TIC TAC TOE  #############################
# winning=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
# player1=""
# player2=""
# turn=""
# gameOver=True

# @client.command()
# async def ttt(ctx,p1: discord.Member,p2: discord.Member):
#     global player1
#     global player2
#     global turn
#     global gameOver
#     global count
#
#     if gameOver:
#         global bloard
#         board = ["white_large_square","white_large_square","white_large_square"
#                  "white_large_square","white_large_square","white_large_square"
#                  "white_large_square","white_large_square","white_large_square"]
#         turn =""
#         gameOver=False
#         count=0
#
#         player1 = p1
#         player2 = p2


@client.command()
async def spam(ctx,arg1,arg2):
    cv=int(arg2);
    if(cv>10):
        await ctx.send("Cannot spam more than 10 times")
        await asyncio.sleep(5)
        await ctx.channel.purge(limit=1)
    else:
        while(cv):
            await ctx.send(arg1)
            cv=cv-1;


@client.command()
async def kick(ctx,user:discord.Member, *,reason="no reason"):
    try:
        await user.kick(reason=reason)
        embed=discord.Embed(
                description=(f'This user has been kicked successfully **{user}**'),
                )
        await ctx.send(embed=embed);
    except:
        await ctx.send("*_Permission not granted_*")



client.run('**your tokken**')
