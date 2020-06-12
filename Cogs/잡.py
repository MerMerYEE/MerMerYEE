import discord 
from discord.ext import commands
import asyncio
import random
import os
import requests
import youtube_dl
from bs4 import BeautifulSoup
import qrcode
from discord.utils import get
import urllib


user = 444363545635848193


class chat(commands.Cog): 

    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def 사랑해(self, ctx):
        await ctx.send("저두용~ :heart:")
        
        
    @commands.command()
    async def guild(self, ctx):
        await ctx.send([f'{len(client.guilds)}개의 서버 | {len(client.users)}명의 유저', (f"{int(client.latency *1000)}ms")])

    
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
    async def 제작(self, ctx):
        embed=discord.Embed(color=0xff00, title="제작자:오타쿠#5251", description="도움주신분:한곰#6567\nLLOOOOTT#0817\n승현#1702")
        embed.add_field(name = "제작 시작일", value = "5월 1일")
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/704619025258512444/6b4cf3a72bb22ad2726a46f6a508c5ad.webp?size=1024")
        await ctx.send(embed=embed)

    @commands.command()
    async def invite(self, ctx):
        embed=discord.Embed(color=0xff00, title="[초대](https://bit.ly/2Z8fA2C)")
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/704619025258512444/6b4cf3a72bb22ad2726a46f6a508c5ad.webp?size=1024")
        await ctx.send(embed=embed)

    @commands.command()
    async def 초대(self, ctx):
        embed=discord.Embed(color=0xff00, title="[초대](https://bit.ly/2Z8fA2C)")
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/704619025258512444/6b4cf3a72bb22ad2726a46f6a508c5ad.webp?size=1024")
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
            if num == 1:
                embed=discord.Embed(color=0xff00, description = "[미도리야가 마음에 드신다면 :heart:를 눌러주세요!](http://koreanbots.dev/bots/704619025258512444)")
                await ctx.send(embed=embed)
            else:
                return
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
            if num == 1:
                embed=discord.Embed(color=0xff00, description = "[미도리야가 마음에 드신다면 :heart:를 눌러주세요!](http://koreanbots.dev/bots/704619025258512444)")
                await ctx.send(embed=embed)
            else:
                return
        else:
            await ctx.channel.purge(limit=1)
            msg = await ctx.send(word)
            await asyncio.sleep(1)
            await msg.edit(content=word + "\n" + ctx.author.mention + "님이 시키셨어요!")
        
    

def setup(client): 
    client.add_cog(chat(client))
