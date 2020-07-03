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
        await ctx.send(discord.Embed(title="봇 정보!", description = f"{int(self.client.latency *1000)}ms이야!"))

    @commands.command()
    async def 핑(self, ctx):
        await ctx.send(discord.Embed(title="핑!", description = f"{int(self.client.latency *1000)}ms이야!"))

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(discord.Embed(title="ping!", description = f"{int(self.client.latency *1000)}ms이야!"))

    




def setup(client): 
    client.add_cog(ping(client))
