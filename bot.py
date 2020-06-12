import discord 
from discord.ext import commands
import asyncio
import random
import os
import requests
from bs4 import BeautifulSoup
import qrcode
from discord.utils import get
from Dtime import Uptime
import time
import typing
import youtube_dl
import re
import koreanbots

client = commands.AutoShardedBot(command_prefix = "데쿠야 ")
Bot = koreanbots.Client(client, os.environ['TOKEN2'])
Uptime.uptimeset()
client.remove_command('help')


@client.event
async def on_ready():
    print("다음으로 로그인합니다")
    print(client.user.name)
    print(client.user.id)
    print("================")

    messages = [f'{len(client.guilds)}개의 서버 | {len(client.users)}명의 유저', (f"{int(client.latency *1000)}ms")]
    while True:
       await client.change_presence(status=discord.Status.online, activity=discord.Game(name=messages[0]))
       messages.append(messages.pop(0))
       await asyncio.sleep(3)
       

@client.command(name="로드")
async def load_commands(ctx, extension=None):
    if ctx.author.id == user:
        if extension is None: # extension이 None이면 (그냥 !리로드 라고 썼을 때)
            for filename in os.listdir("Cogs"):
                if filename.endswith(".py"):
                    client.unload_extension(f"Cogs.{filename[:-3]}")
                    client.load_extension(f"Cogs.{filename[:-3]}")
            await ctx.send(":white_check_mark: 모든 명령어를 로드했어요!!")
        else:
            client.load_extension(f"Cogs.{extension}")
            await ctx.send(f":white_check_mark: {extension}을(를) 로드했어요!!")
    else:
        return

@client.command(name="언로드")
async def unload_commands(ctx, extension=None):
    if ctx.author.id == user:
        if extension is None: # extension이 None이면 (그냥 !리로드 라고 썼을 때)
            for filename in os.listdir("Cogs"):
                if filename.endswith(".py"):
                    client.unload_extension(f"Cogs.{filename[:-3]}")
                    client.load_extension(f"Cogs.{filename[:-3]}")
            await ctx.send(":white_check_mark: 모든 명령어를 언로드했어요!!")
        else:
            client.unload_extension(f"Cogs.{extension}")
            await ctx.send(f":white_check_mark: {extension}을(를) 언로드했어요!!")
    else:
        return

@client.command(name="리로드")
async def reload_commands(ctx, extension=None):
    if ctx.author.id == user:
        if extension is None: # extension이 None이면 (그냥 !리로드 라고 썼을 때)
            for filename in os.listdir("Cogs"):
                if filename.endswith(".py"):
                    client.unload_extension(f"Cogs.{filename[:-3]}")
                    client.load_extension(f"Cogs.{filename[:-3]}")
            await ctx.send(":white_check_mark: 모든 명령어를 다시 가져왔어요!!")
        else:
            client.unload_extension(f"Cogs.{extension}")
            client.load_extension(f"Cogs.{extension}")
            await ctx.send(f":white_check_mark: {extension}을(를) 다시 가져왔어요!!")
    else:
        return
        
'''
@reload_commands.error
async def reload_commands_error(ctx, error):
    if isinstance(error, no)
'''
user = 444363545635848193

@client.command()
async def 때려(ctx, user_ : discord.Member):
    if ctx.author.id == user:
        await ctx.send(str(user_) + " 죽어 퍽퍽")

@client.command()
async def 길드(ctx):
    if ctx.author.id == user:
        await ctx.send(client.guilds)
    else:
        return

@client.command()
async def 채널저장(ctx, channel: discord.TextChannel):
    await ctx.send(channel.id)

@client.command()
async def 거꾸로(ctx, rv):
    if rv == "enoyreve@":
        return
    if rv == "ereh@":
        return
    await ctx.send(reversed(rv))

@client.command()
async def 생성(ctx, qrr):
    img = qrcode.make(qrr)
    img.save("asdf.png")
    qrc = "asdf.png"

    await ctx.send(file=discord.File(qrc))

@client.command()
async def eval(ctx, evall):
    embed=discord.Embed(color=0xff00, title="eval 결과", description = "결과 =" + eval(evall))
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/704619025258512444/6b4cf3a72bb22ad2726a46f6a508c5ad.webp?size=1024")
    await ctx.send(embed=embed)

@client.command()
async def eval2(ctx, eeval):
    if ctx.author.id == user:
        embed=discord.Embed(title="Eval 결과", description=f"""input :inbox_tray:
            
        {ctx.message.content[8:]}
            

        output :outbox_tray:
            
        {eval(ctx.message.content[8:])}
            

        """)
        await ctx.send(embed=embed)
    else:
        embed=discord.Embed(title="오류!", description="봇 제작자가 아닙니다!")
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/704619025258512444/6b4cf3a72bb22ad2726a46f6a508c5ad.webp?size=1024")
        await ctx.send(embed=embed)







client.run(os.environ['TOKEN'])
