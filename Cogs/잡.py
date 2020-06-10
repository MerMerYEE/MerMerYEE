import discord 
from discord.ext import commands
import asyncio
import random
import os
import requests
from bs4 import BeautifulSoup
import qrcode
from discord.utils import get

user = 444363545635848193

class chat(commands.Cog): 

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def 사랑해(self, ctx):
        await ctx.send("저두용~ :heart:")
    
    @commands.command()
    async def 주인(self, ctx):
        user = ctx.author.id
        if user == 444363545635848193:
            await ctx.send("와!! 주인님!!")
        else:
            await ctx.send("누...누구세요..?")

    @commands.command()
    async def 죽어(self, ctx):
        await ctx.send("?")

    @commands.command()
    async def 띵킹(self, ctx):
        await ctx.send(":think:")

    @commands.command()
    async def 띵크(self, ctx):
        await ctx.send(":think:")
    
    @commands.command()
    async def 제작(self, ctx):
       embed=discord.Embed(color=0xff00, title="제작자:오타쿠#5251", description="도움주신분:한곰#6567\nLLOOOOTT#0817\n승현#1702")
        embed.add_field(name = "제작 시작일", value = "5월 1일")
        await ctx.send(embed=embed)

    @commands.command()
    async def invite(self, ctx):
        await ctx.send("https://bit.ly/2Z8fA2C 여기있어")

    @commands.command()
    async def 초대(self, ctx):
        embed=discord.Embed(color=0xff00, title="여기있어!)
        embed.add_field(name = "링크", value = "[초대](https://bit.ly/2Z8fA2C"))
        await ctx.send(embed=embed)

    @commands.command()
    async def 띵킹(self, ctx):
        await ctx.send(":thinking:")

    @commands.command()
    async def 띵크(self, ctx):
        await ctx.send(":thinking:")

    @commands.command()
    async def 관짝(self, ctx):
        number = random.randint(1, 3)
        pic = str(number) + ".gif"
        await ctx.send(file=discord.File(pic))

    @commands.command()
    async def 관짝춤(self, ctx):
        number = random.randint(1, 3)
        pic = str(number) + ".gif"
        await ctx.send(file=discord.File(pic))

    @commands.command()
    async def say(self, ctx, *, word):
        if ctx.author.id == user:
            await ctx.channel.purge(limit=1)
            msg = await ctx.send(word)
        else:
            await ctx.channel.purge(limit=1)
            msg = await ctx.send(word)
            await asyncio.sleep(1)
            await msg.edit(content=word + "\n" + ctx.author.mention + "님이 시키셨어요!")

    @commands.command()
    async def 말해(self, ctx, *, word):
        if ctx.author.id == user:
            await ctx.channel.purge(limit=1)
            msg = await ctx.send(word)
        else:
            await ctx.channel.purge(limit=1)
            msg = await ctx.send(word)
            await asyncio.sleep(1)
            await msg.edit(content=word + "\n" + ctx.author.mention + "님이 시키셨어요!")

        
    

def setup(client): 
    client.add_cog(chat(client))
