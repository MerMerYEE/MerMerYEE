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

num = random.randint(1, 5)


class help(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def 도움말(self, ctx):
        channel = await ctx.author.create_dm()
        embed=discord.Embed(color=0xff00, title="명령어")
        embed.set_footer(text=str(self.client.get_user(444363545635848193)) + "가 만들었습니다!", icon_url=self.client.get_user(444363545635848193).avatar_url)
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/704619025258512444/6b4cf3a72bb22ad2726a46f6a508c5ad.webp?size=1024")
        embed.add_field(name = '관리 명령어', value = '밴, 언밴, 뮤트, 언뮤트, 킥, 추방, 삭제, clear (뮤트기능은 뮤트 라는 역할이 있어야 실행됨)')
        embed.add_field(name = '잡 명령어', value = '핑(ping), 주인, help, 명령어, 도움말, 타이머, 제작, 거꾸로, 사랑해')
        embed.add_field(name = '링크 명령어', value = '메이플(전적), maple, 롤(전적), lol(전적), 트위치(찾기), 오버워치(전적), overwatch(전적)')
        embed.add_field(name = '띵크', value = "띵크")
        await ctx.send(ctx.author.mention + "님 DM으로 도움말을 보냈어요!")
        await channel.send(embed=embed)
        if num == 1:
            embed=discord.Embed(color=0xff00, description = "[미도리야가 마음에 드신다면 :heart:를 눌러주세요!](http://koreanbots.dev/bots/704619025258512444)")
            await ctx.send(embed=embed)
        else:
            return

    @commands.command()
    async def help(self, ctx):
        channel = await ctx.author.create_dm()
        embed=discord.Embed(color=0xff00, title="명령어")
        embed.set_footer(text=str(self.client.get_user(444363545635848193)) + "가 만들었습니다!", icon_url=self.client.get_user(444363545635848193).avatar_url)
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/704619025258512444/6b4cf3a72bb22ad2726a46f6a508c5ad.webp?size=1024")
        embed.add_field(name = '관리 명령어', value = '밴, 언밴, 뮤트, 언뮤트, 킥, 추방, 삭제, clear (뮤트기능은 뮤트 라는 역할이 있어야 실행됨)')
        embed.add_field(name = '잡 명령어', value = '핑(ping), 주인, help, 명령어, 도움말, 타이머, 제작, 거꾸로, 사랑해')
        embed.add_field(name = '링크 명령어', value = '메이플(전적), maple, 롤(전적), lol(전적), 트위치(찾기), 오버워치(전적), overwatch(전적)')
        embed.add_field(name = '띵크', value = "띵크")
        await ctx.send(ctx.author.mention + "님 DM으로 도움말을 보냈어요!")
        await channel.send(embed=embed)
        if num == 1:
            embed=discord.Embed(color=0xff00, description = "[미도리야가 마음에 드신다면 :heart:를 눌러주세요!](http://koreanbots.dev/bots/704619025258512444)")
            await ctx.send(embed=embed)
        else:
            return

    @commands.command()
    async def 명령어(self, ctx):
        channel = await ctx.author.create_dm()
        embed=discord.Embed(color=0xff00, title="명령어")
        embed.set_footer(text=str(self.client.get_user(444363545635848193)) + "가 만들었습니다!", icon_url=self.client.get_user(444363545635848193).avatar_url)
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/704619025258512444/6b4cf3a72bb22ad2726a46f6a508c5ad.webp?size=1024")
        embed.add_field(name = '관리 명령어', value = '밴, 언밴, 뮤트, 언뮤트, 킥, 추방, 삭제, clear (뮤트기능은 뮤트 라는 역할이 있어야 실행됨)')
        embed.add_field(name = '잡 명령어', value = '핑(ping), 주인, help, 명령어, 도움말, 타이머, 제작, 거꾸로, 사랑해')
        embed.add_field(name = '링크 명령어', value = '메이플(전적), maple, 롤(전적), lol(전적), 트위치(찾기), 오버워치(전적), overwatch(전적)')
        embed.add_field(name = '띵크', value = "띵크")
        await ctx.send(ctx.author.mention + "님 DM으로 도움말을 보냈어요!")
        await channel.send(embed=embed)
        if num == 1:
            embed=discord.Embed(color=0xff00, description = "[미도리야가 마음에 드신다면 :heart:를 눌러주세요!](http://koreanbots.dev/bots/704619025258512444)")
            await ctx.send(embed=embed)
        else:
            return

    @commands.command()
    async def cmds(self, ctx):
        channel = await ctx.author.create_dm()
        embed=discord.Embed(color=0xff00, title="명령어")
        embed.set_footer(text=str(self.client.get_user(444363545635848193)) + "가 만들었습니다!", icon_url=self.client.get_user(444363545635848193).avatar_url)
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/704619025258512444/6b4cf3a72bb22ad2726a46f6a508c5ad.webp?size=1024")
        embed.add_field(name = '관리 명령어', value = '밴, 언밴, 뮤트, 언뮤트, 킥, 추방, 삭제, clear (뮤트기능은 뮤트 라는 역할이 있어야 실행됨)')
        embed.add_field(name = '잡 명령어', value = '핑(ping), 주인, help, 명령어, 도움말, 타이머, 제작, 거꾸로, 사랑해')
        embed.add_field(name = '링크 명령어', value = '메이플(전적), maple, 롤(전적), lol(전적), 트위치(찾기), 오버워치(전적), overwatch(전적)')
        embed.add_field(name = '띵크', value = "띵크")
        await ctx.send(ctx.author.mention + "님 DM으로 도움말을 보냈어요!")
        await channel.send(embed=embed)
        if num == 1:
            embed=discord.Embed(color=0xff00, description = "[미도리야가 마음에 드신다면 :heart:를 눌러주세요!](http://koreanbots.dev/bots/704619025258512444)")
            await ctx.send(embed=embed)
        else:
            return


def setup(client): 
    client.add_cog(help(client))
