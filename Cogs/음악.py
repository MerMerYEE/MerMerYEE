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
import youtube_dl
import re



class music(commands.Cog): 

    def __init__(self, client):
        self.client = client



    @commands.command(name="참가", pass_context=True)
    async def _join(self, ctx):
        if ctx.author.voice and ctx.author.voice.channel: # 채널에 들어가 있는지 파악
            channel = ctx.author.voice.channel # 채널 구하기
            await channel.connect() # 채널 연결
        else: # 유저가 채널에 없으면
            await ctx.send("채널에 연결되지 않았습니다.") # 출력

    @commands.command(name="나가")
    async def _leave(ctx):
        await self.client.voice_clients[0].disconnect()

    



    

def setup(client): 
    client.add_cog(music(client))
