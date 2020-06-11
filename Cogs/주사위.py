import discord
from discord.ext import commands
import time
import random

class en_Dice(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Commands
    @commands.command()
    async def 주사위(self, ctx):
        await ctx.trigger_typing()

        randomNum = random.randrange(1, 7) # 1~6까지 랜덤수
        if randomNum == 1:
            embed = discord.Embed(title= "**주사위!**", description = ':one:', color= 0xff00)
            embed.set_footer(text=str(self.client.get_user(444363545635848193)) + "가 만들었습니다!", icon_url=self.client.get_user(444363545635848193).avatar_url)
            await ctx.send(embed=embed)
        if randomNum == 2:
            embed = discord.Embed(title= "**주사위!**", description = ':two:', color= 0xff00)
            embed.set_footer(text=str(self.client.get_user(444363545635848193)) + "가 만들었습니다!", icon_url=self.client.get_user(444363545635848193).avatar_url)
            await ctx.send(embed=embed)
        if randomNum ==3:
            embed = discord.Embed(title= "**주사위!**", description = ':three:', color= 0xff00)
            embed.set_footer(text=str(self.client.get_user(444363545635848193)) + "가 만들었습니다!", icon_url=self.client.get_user(444363545635848193).avatar_url)
            await ctx.send(embed=embed)
        if randomNum ==4:
            embed = discord.Embed(title= "**주사위!**", description = ':four:', color= 0xff00)
            embed.set_footer(text=str(self.client.get_user(444363545635848193)) + "가 만들었습니다!", icon_url=self.client.get_user(444363545635848193).avatar_url)
            await ctx.send(embed=embed)
        if randomNum ==5:
            embed = discord.Embed(title= "**주사위!**", description = ':five:', color= 0xff00)
            embed.set_footer(text=str(self.client.get_user(444363545635848193)) + "가 만들었습니다!", icon_url=self.client.get_user(444363545635848193).avatar_url)
            await ctx.send(embed=embed)
        if randomNum ==6:
            embed = discord.Embed(title= "**주사위!**", description = ':six:', color= 0xff00)
            embed.set_footer(text=str(self.client.get_user(444363545635848193)) + "가 만들었습니다!", icon_url=self.client.get_user(444363545635848193).avatar_url)
            await ctx.send(embed=embed)

    @commands.command()
    async def roll(self, ctx):
        await ctx.trigger_typing()

        randomNum = random.randrange(1, 7) # 1~6까지 랜덤수
        if randomNum == 1:
            embed = discord.Embed(title= "**Dice!**", description =  ':one:', color= 0xff00)
            embed.set_footer(text=str(self.client.get_user(444363545635848193)) + "가 만들었습니다!", icon_url=self.client.get_user(444363545635848193).avatar_url)
            await ctx.send(embed=embed)
        if randomNum == 2:
            embed = discord.Embed(title= "**Dice!**", description = ':two:', color= 0xff00)
            embed.set_footer(text=str(self.client.get_user(444363545635848193)) + "가 만들었습니다!", icon_url=self.client.get_user(444363545635848193).avatar_url)
            await ctx.send(embed=embed)
        if randomNum ==3:
            embed = discord.Embed(title= "**Dice!**", description = ':three:', color= 0xff00)
            embed.set_footer(text=str(self.client.get_user(444363545635848193)) + "가 만들었습니다!", icon_url=self.client.get_user(444363545635848193).avatar_url)
            await ctx.send(embed=embed)
        if randomNum ==4:
            embed = discord.Embed(title= "**Dice!**", description = ':four:', color= 0xff00)
            embed.set_footer(text=str(self.client.get_user(444363545635848193)) + "가 만들었습니다!", icon_url=self.client.get_user(444363545635848193).avatar_url)
            await ctx.send(embed=embed)
        if randomNum ==5:
            embed = discord.Embed(title= "**Dice!**", description = ':five:', color= 0xff00)
            embed.set_footer(text=str(self.client.get_user(444363545635848193)) + "가 만들었습니다!", icon_url=self.client.get_user(444363545635848193).avatar_url)
            await ctx.send(embed=embed)
        if randomNum ==6:
            embed = discord.Embed(title= "**Dice!**", description = ':six:', color= 0xff00)
            embed.set_footer(text=str(self.client.get_user(444363545635848193)) + "가 만들었습니다!", icon_url=self.client.get_user(444363545635848193).avatar_url)
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(en_Dice(client))