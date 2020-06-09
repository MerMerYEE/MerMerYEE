import discord 
from discord.ext import commands
import asyncio
import random
import os
import requests
from bs4 import BeautifulSoup
import pymysql
import json
import qrcode
from discord.utils import get
from Dtime import Uptime
import time

class 관리(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name="추방", pass_context=True)
    @commands.has_permissions(administrator=True)
    async def _kick(self, ctx, *, user_name: discord.Member, reason=None):
        await user_name.kick(reason=reason)
        await ctx.send(str(user_name)+"님을 추방했어요!!")

    @_kick.error
    async def _kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("{} 권한이 없는데요??".format(ctx.message.author))
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("{}님, 유저를 넣지 않았어요!.".format(ctx.message.author))
        if isinstance(error, commands.BadArgument):
            await ctx.send("{}님, 유저를 넣어 주세요!!".format(ctx.message.author))

    @commands.command(name="킥", pass_context=True)
    @commands.has_permissions(administrator=True)
    async def _추방(self, ctx, *, user_name: discord.Member, reason=None):
        await user_name.kick(reason=reason)
        await ctx.send(str(user_name)+"님을 킥했어요!!")

    @_추방.error
    async def _ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("{} 너 권한이 없는데?.".format(ctx.message.author))
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("{}님, 유저를 넣지 않았어요!.".format(ctx.message.author))
        if isinstance(error, commands.BadArgument):
            await ctx.send("{}님, 유저를 넣어 주세요!!".format(ctx.message.author))

    @commands.command(name="밴", pass_context=True)
    @commands.has_permissions(administrator=True)
    async def _ban(self, ctx, *, user_name: discord.Member):
        await user_name.ban()
        await ctx.send(str(user_name)+"님을 영원히 보냈어요!!")

    @_ban.error
    async def _ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("{} 너 권한이 없는데?.".format(ctx.message.author))
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("{}님, 유저를 넣지 않았어요!.".format(ctx.message.author))
        if isinstance(error, commands.BadArgument):
            await ctx.send("{}님, 유저를 넣어 주세요!!".format(ctx.message.author))

    @commands.command(name="언밴", pass_context=True)
    @commands.has_permissions(administrator=True)
    async def _unban(self, ctx, *, user_name):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = user_name.split('#')
        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f"{user.mention} 그...그가 돌아왔어!!")
                return

    @_unban.error
    async def _unban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("{} 권한이 없는데요???".format(ctx.message.author))
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("{}님, 유저를 넣지 않았어요!.".format(ctx.message.author))
        if isinstance(error, commands.BadArgument):
            await ctx.send("{}님, 유저를 넣어 주세요!!".format(ctx.message.author))

    @commands.command(name="뮤트", pass_context=True)
    @commands.has_permissions(administrator=True)
    async def _mute(self, ctx, member: discord.Member=None):
        member = member or ctx.message.author
        await member.add_roles(get(ctx.guild.roles, name="뮤트"))
        await ctx.channel.send(str(member)+"님이 뮤트가 되었어요!!!")

    @_mute.error
    async def _mute_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("{} 권한이 없는데요??".format(ctx.message.author))
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("{}님, 유저를 넣지 않았어요!.".format(ctx.message.author))
        if isinstance(error, commands.BadArgument):
            await ctx.send("{}님, 유저를 넣어 주세요!!".format(ctx.message.author))
        if isinstance(error, commands.MissingAnyRole):
            await ctx.send("{} 뮤트라는 역할이 존재하지 않는데요??".format(ctx.message.author))

    @commands.command(name="언뮤트", pass_context=True)
    async def _unmute(self, ctx, member: discord.Member=None):
        member = member or ctx.message.author
        await member.remove_roles(get(ctx.guild.roles, name='뮤트'))
        await ctx.send(str(member)+"이젠 말 할 수 있을거에요...")

    @_unmute.error
    async def _unmute_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("{} 권한이 없는데요??".format(ctx.message.author))
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("{}님, 유저를 넣지 않았어요!.".format(ctx.message.author))
        if isinstance(error, commands.BadArgument):
            await ctx.send("{}님, 유저를 넣어 주세요!!".format(ctx.message.author))

    @commands.command(name="삭제", pass_context = True)
    @commands.has_permissions(administrator=True)
    async def _삭제(self, ctx, amount : int):
        await asyncio.sleep(0.5)
        if amount == 0:
            await ctx.send("숫자를 제대로 입력해주세요!!")
            return
        else:
            await ctx.send(":white_check_mark: 메세지 삭제 중 이에요!")
            await asyncio.sleep(0.5)
            await ctx.channel.purge(limit=amount + 2)

    @_삭제.error
    async def _삭제_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("{} 권한이 없는데요??".format(ctx.message.author))


def setup(client): 
    client.add_cog(관리(client))
