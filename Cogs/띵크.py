import discord
from discord.ext import commands

class 띵크(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def 띵킹눈(ctx):
        await ctx.send(self.client.get_emoji(703129203847200829))
        if num == 1:
            embed=discord.Embed(color=0xff00, description = "[미도리야가 마음에 드신다면 :heart:를 눌러주세요!](http://koreanbots.dev/bots/704619025258512444)")
            await ctx.send(embed=embed)
        else:
            return

    @commands.command()
    async def 띵킹빵(ctx):
        await ctx.send(self.client.get_emoji(708537624012390518))
        if num == 1:
            embed=discord.Embed(color=0xff00, description = "[미도리야가 마음에 드신다면 :heart:를 눌러주세요!](http://koreanbots.dev/bots/704619025258512444)")
            await ctx.send(embed=embed)
        else:
            return

    @commands.command()
    async def 띵킹버거(ctx):
        await ctx.send(self.client.get_emoji(708537623836098600))
        if num == 1:
            embed=discord.Embed(color=0xff00, description = "[미도리야가 마음에 드신다면 :heart:를 눌러주세요!](http://koreanbots.dev/bots/704619025258512444)")
            await ctx.send(embed=embed)
        else:
            return

    @commands.command()
    async def 띵킹박수(ctx):
        await ctx.send(self.client.get_emoji(708537624154996808))
        if num == 1:
            embed=discord.Embed(color=0xff00, description = "[미도리야가 마음에 드신다면 :heart:를 눌러주세요!](http://koreanbots.dev/bots/704619025258512444)")
            await ctx.send(embed=embed)
        else:
            return

    @commands.command()
    async def 띵킹가지(ctx):
        await ctx.send(self.client.get_emoji(708537623622451213))
        if num == 1:
            embed=discord.Embed(color=0xff00, description = "[미도리야가 마음에 드신다면 :heart:를 눌러주세요!](http://koreanbots.dev/bots/704619025258512444)")
            await ctx.send(embed=embed)
        else:
            return

    @commands.command()
    async def 띵킹피젯(ctx):
        await ctx.send(self.client.get_emoji(708537623983161435))
        if num == 1:
            embed=discord.Embed(color=0xff00, description = "[미도리야가 마음에 드신다면 :heart:를 눌러주세요!](http://koreanbots.dev/bots/704619025258512444)")
            await ctx.send(embed=embed)
        else:
            return

    @commands.command()
    async def 띵킹물고기(ctx):
        await ctx.send(self.client.get_emoji(708537623446290493))
        if num == 1:
            embed=discord.Embed(color=0xff00, description = "[미도리야가 마음에 드신다면 :heart:를 눌러주세요!](http://koreanbots.dev/bots/704619025258512444)")
            await ctx.send(embed=embed)
        else:
            return

    @commands.command()
    async def 띵킹하드(ctx):
        await ctx.send(self.client.get_emoji(708537623794155560))
        if num == 1:
            embed=discord.Embed(color=0xff00, description = "[미도리야가 마음에 드신다면 :heart:를 눌러주세요!](http://koreanbots.dev/bots/704619025258512444)")
            await ctx.send(embed=embed)
        else:
            return

    @commands.command()
    async def 띵킹인터넷(ctx):
        await ctx.send(self.client.get_emoji(708537623723114517))
        if num == 1:
            embed=discord.Embed(color=0xff00, description = "[미도리야가 마음에 드신다면 :heart:를 눌러주세요!](http://koreanbots.dev/bots/704619025258512444)")
            await ctx.send(embed=embed)
        else:
            return

    @commands.command()
    async def 띵킹레몬(ctx):
        await ctx.send(self.client.get_emoji(708537623425318944))
        if num == 1:
            embed=discord.Embed(color=0xff00, description = "[미도리야가 마음에 드신다면 :heart:를 눌러주세요!](http://koreanbots.dev/bots/704619025258512444)")
            await ctx.send(embed=embed)
        else:
            return

    @commands.command()
    async def 띵킹비정상(ctx):
        ctx.send(self.client.get_emoji(708537623706075286))
        if num == 1:
            embed=discord.Embed(color=0xff00, description = "[미도리야가 마음에 드신다면 :heart:를 눌러주세요!](http://koreanbots.dev/bots/704619025258512444)")
            await ctx.send(embed=embed)
        else:
            return

def setup(client): 
    client.add_cog(띵크(client))    