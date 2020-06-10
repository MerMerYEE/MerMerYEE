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




class util(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command()
    async def 주사위(self, ctx):
        number = random.randint(1, 6)
        msg = await ctx.send("3초후 주사위를 돌립니다! (1~6)")
        await asyncio.sleep(3)
        await msg.edit(content="두")
        await msg.edit(content="구")
        await msg.edit(content="두")
        await msg.edit(content="구")
        await msg.edit(content="짜잔! {}이 나왔습니다!".format(number))
        if num == 1:
            embed=discord.Embed(color=0xff00, description = "[미도리야가 마음에 드신다면 :heart:를 눌러주세요!](http://koreanbots.dev/bots/704619025258512444)")
            await ctx.send(embed=embed)
        else:
            return

    @commands.command()
    async def 타이머(self, ctx):
        timer = int(ctx.message.content.split(' ')[2])
        msg = await ctx.send("3초후 " + str(timer) + "초 타이머를 시작합니다!")
        await asyncio.sleep(3)
        for i in range(timer):
            await msg.edit(content = str(i))
            await asyncio.sleep(1)
        await msg.edit(content = "시간 끝")
        if num == 1:
            embed=discord.Embed(color=0xff00, description = "[미도리야가 마음에 드신다면 :heart:를 눌러주세요!](http://koreanbots.dev/bots/704619025258512444)")
            await ctx.send(embed=embed)
        else:
            return

    @commands.command()
    async def 업타임(self, ctx):
        uptime = str(Uptime.uptime()).split(":")
        hours = uptime[0]
        minitues = uptime[1]
        seconds = uptime[2].split(".")[0]
        await ctx.send(f"{hours}시간 {minitues}분 {seconds}초 동안 살아있었어!!")
        if num == 1:
            embed=discord.Embed(color=0xff00, description = "[미도리야가 마음에 드신다면 :heart:를 눌러주세요!](http://koreanbots.dev/bots/704619025258512444)")
            await ctx.send(embed=embed)
        else:
            return

    @commands.command()
    async def 시간(self, ctx):
        now = time.localtime()
        await ctx.send("%04d년 %02d월 %02d일 %02d시 %02d분 %02d초네??" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec))
        if num == 1:
            embed=discord.Embed(color=0xff00, description = "[미도리야가 마음에 드신다면 :heart:를 눌러주세요!](http://koreanbots.dev/bots/704619025258512444)")
            await ctx.send(embed=embed)
        else:
            return

    @commands.command()
    async def 홀짝(self, ctx, 홀짝):
        a = random.randint(1, 2)
        홀 = 1
        짝 = 2
        if 홀짝 == str(a):
            await ctx.send("정답입니다!")
        else:
            await ctx.send("땡 틀렸습니다 ㅠㅠ")


def setup(client): 
    client.add_cog(util(client))