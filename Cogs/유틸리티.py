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
    async def 타이머(self, ctx):
        timer = int(ctx.message.content.split(' ')[2])
        msg = await ctx.send("3초후 " + str(timer) + "초 타이머를 시작합니다!")
        await asyncio.sleep(3)
        for i in range(timer):
            await msg.edit(content = str(i))
            await asyncio.sleep(1)
        await msg.edit(content = "시간 끝")

    @commands.command()
    async def 업타임(self, ctx):
        uptime = str(Uptime.uptime()).split(":")
        hours = uptime[0]
        minitues = uptime[1]
        seconds = uptime[2].split(".")[0]
        await ctx.send(f"{hours}시간 {minitues}분 {seconds}초 동안 살아있었어!!")

    @commands.command()
    async def 홀짝(ctx):
        a = "홀", "짝"
	c = random.choice(a)
        if b == c:
            print("정답입니다!!")
	    c = random.choice(a)
        else:
	    print("틀렸습니다!!")
            c = random.choice(a)


def setup(client): 
    client.add_cog(util(client))
