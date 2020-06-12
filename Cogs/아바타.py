import discord
from discord.ext import commands

class 아바타(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Commands
    @commands.command()
    async def 아바타(self, ctx):
        if (ctx.message.mentions.__len__() > 0):
            for user in ctx.message.mentions:
                pfp = str(user.avatar_url)
                embed = discord.Embed(title="**" +user.name + "**님의 아바타", description="[Link]" + "(" + pfp + ")",
                                      color=0xff00)
                embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/704619025258512444/6b4cf3a72bb22ad2726a46f6a508c5ad.webp?size=1024")
                embed.set_image(url=pfp)
                embed.set_footer(text=str(self.client.get_user(444363545635848193)) + "가 만들었습니다!", icon_url=self.client.get_user(444363545635848193).avatar_url)
                await ctx.trigger_typing()
                await ctx.send(embed=embed)
        else:
            pfp = ctx.author.avatar_url
            embed = discord.Embed(title="**" + ctx.author.name + "**님의 아바타", description="[Link]" + "(" + str(pfp) + ")",
                                color=0xff00)
            embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/704619025258512444/6b4cf3a72bb22ad2726a46f6a508c5ad.webp?size=1024")
            embed.set_image(url=pfp)
            embed.set_footer(text=str(self.client.get_user(444363545635848193)) + "가 만들었습니다!", icon_url=self.client.get_user(444363545635848193).avatar_url)
            await ctx.trigger_typing()
            await ctx.send(embed=embed)

    @commands.command()
    async def avatart(self, ctx):
        if (ctx.message.mentions.__len__() > 0):
            for user in ctx.message.mentions:
                pfp = str(user.avatar_url)
                embed = discord.Embed(title="**" +user.name + "**님의 아바타", description="[Link]" + "(" + pfp + ")",
                                      color=0xff00)
                embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/704619025258512444/6b4cf3a72bb22ad2726a46f6a508c5ad.webp?size=1024")
                embed.set_image(url=pfp)
                embed.set_footer(text=str(self.client.get_user(444363545635848193)) + "가 만들었습니다!", icon_url=self.client.get_user(444363545635848193).avatar_url)
                await ctx.trigger_typing()
                await ctx.send(embed=embed)
        else:
            pfp = ctx.author.avatar_url
            embed = discord.Embed(title="**" + ctx.author.name + "**님의 아바타", description="[Link]" + "(" + str(pfp) + ")",
                                color=0xff00)
            embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/704619025258512444/6b4cf3a72bb22ad2726a46f6a508c5ad.webp?size=1024")
            embed.set_image(url=pfp)
            embed.set_footer(text=str(self.client.get_user(444363545635848193)) + "가 만들었습니다!", icon_url=self.client.get_user(444363545635848193).avatar_url)
            await ctx.trigger_typing()
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(아바타(client))