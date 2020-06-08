import discord 
from discord.ext import commands
import asyncio
import random
import os
import requests
from bs4 import BeautifulSoup
import qrcode
from discord.utils import get



class 전적(commands.Cog): 

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def 오버워치(self, ctx, over):
        await ctx.send("https://overwatch.op.gg/search?playerName=" + over)

    @commands.command()
    async def overwatch(self, ctx, over2):
        await ctx.send("https://overwatch.op.gg/search?playerName=" + over2)

    @commands.command()
    async def 트위치(self, ctx, twitch):
        await ctx.send("https://m.twitch.tv/"+twitch)

    @commands.command()
    async def twitch(self, ctx, twitch2):
        await ctx.send("https://m.twitch.tv/"+twitch2)

    @commands.command()
    async def 메이플(self, ctx, maple1):
        await ctx.send("https://maple.gg/u/"+maple1)

    @commands.command()
    async def maple(self, ctx, maple2):
        await ctx.send("https://maple.gg/u/"+maple2)

    @commands.command()
    async def lol(self, ctx, lol):
        await ctx.send("https://www.op.gg/summoner/userName="+lol)

    @commands.command()
    async def 롤(self, ctx, lol2):
        await ctx.send("https://www.op.gg/summoner/userName="+lol2)
    

def setup(client): 
    client.add_cog(전적(client))
