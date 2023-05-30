import discord
from discord.ext import commands
import requests
import datetime


client = commands.Bot(command_prefix="-", intents =  discord.Intents.all())



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







client.run('MTAzMzYwOTYyOTQzNzAxODE0NA.GY8l8E.TOgDOsObUmUkyJwqP63mvn9BVrUBroJ0eDMO_8')
