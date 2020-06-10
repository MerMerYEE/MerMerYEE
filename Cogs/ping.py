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

num = random.randint(1, 5)

class ping(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def 봇정보(self, ctx):
        await ctx.send(f"{int(self.client.latency *1000)}ms이야!")
        if num == 1:
            embed=discord.Embed(color=0xff00, description = "[미도리야가 마음에 드신다면 :heart:를 눌러주세요!](http://koreanbots.dev/bots/704619025258512444)")
            await ctx.send(embed=embed)
        else:
            return

    @commands.command()
    async def 핑(self, ctx):
        await ctx.send(f"{int(self.client.latency *1000)}ms이야!")
        if num == 1:
            embed=discord.Embed(color=0xff00, description = "[미도리야가 마음에 드신다면 :heart:를 눌러주세요!](http://koreanbots.dev/bots/704619025258512444)")
            await ctx.send(embed=embed)
        else:
            return

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"{int(self.client.latency *1000)}ms이야!")
        if num == 1:
            embed=discord.Embed(color=0xff00, description = "[미도리야가 마음에 드신다면 :heart:를 눌러주세요!](http://koreanbots.dev/bots/704619025258512444)")
            await ctx.send(embed=embed)
        else:
            return

    




def setup(client): 
    client.add_cog(ping(client))
