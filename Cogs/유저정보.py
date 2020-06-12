import discord
from discord.ext import commands

class Userinfo(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Commands
    @commands.command()
    async def 유저정보(self, ctx):
        if (ctx.message.mentions.__len__() > 0):
            for user in ctx.message.mentions:
                embed = discord.Embed(title="**" + user.name + "**님의 정보", description="",
                                      color=0xff00)
                embed.add_field(name="**ID**",
                                value=user.id,
                                inline=True)
                embed.add_field(name="**Nickname**",
                                value=user.display_name,
                                inline=True)
                embed.add_field(name="**Status**",
                                value=user.status,
                                inline=True)
                embed.add_field(name="**Mention**",
                                value="<@" + str(user.id) + ">",
                                inline=True)
                embed.set_thumbnail(url=user.avatar_url)
                embed.set_footer(text=str(self.client.get_user(444363545635848193)) + "가 만들었습니다!", icon_url=self.client.get_user(444363545635848193).avatar_url)
                await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title=ctx.author.name + "님의 정보", description="",
                                  color=0xff00)
            embed.add_field(name="**ID**",
                            value=ctx.author.id,
                            inline=True)
            embed.add_field(name="**Nickname**",
                            value=ctx.author.display_name,
                            inline=True)
            embed.add_field(name="**Status**",
                            value=ctx.author.status,
                            inline=True)
            embed.add_field(name="**Mention**",
                            value="<@" + str(ctx.author.id) + ">",
                            inline=True)
            embed.set_thumbnail(url=ctx.author.avatar_url)
            embed.set_footer(text=str(self.client.get_user(444363545635848193)) + "가 만들었습니다!", icon_url=self.client.get_user(444363545635848193).avatar_url)
            await ctx.send(embed=embed)

    @commands.command()
    async def userinfo(self, ctx):
        if (ctx.message.mentions.__len__() > 0):
            for user in ctx.message.mentions:
                embed = discord.Embed(title="**" + user.name + "**님의 정보", description="",
                                      color=0xff00)
                embed.add_field(name="**ID**",
                                value=user.id,
                                inline=True)
                embed.add_field(name="**Nickname**",
                                value=user.display_name,
                                inline=True)
                embed.add_field(name="**Status**",
                                value=user.status,
                                inline=True)
                embed.add_field(name="**Mention**",
                                value="<@" + str(user.id) + ">",
                                inline=True)
                embed.set_thumbnail(url=user.avatar_url)
                embed.set_footer(text=str(self.client.get_user(444363545635848193)) + "가 만들었습니다!", icon_url=self.client.get_user(444363545635848193).avatar_url)
                await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title=ctx.author.name + "님의 정보", description="",
                                  color=0xff00)
            embed.add_field(name="**ID**",
                            value=ctx.author.id,
                            inline=True)
            embed.add_field(name="**Nickname**",
                            value=ctx.author.display_name,
                            inline=True)
            embed.add_field(name="**Status**",
                            value=ctx.author.status,
                            inline=True)
            embed.add_field(name="**Mention**",
                            value="<@" + str(ctx.author.id) + ">",
                            inline=True)
            embed.set_thumbnail(url=ctx.author.avatar_url)
            embed.set_footer(text=str(self.client.get_user(444363545635848193)) + "가 만들었습니다!", icon_url=self.client.get_user(444363545635848193).avatar_url)
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Userinfo(client))