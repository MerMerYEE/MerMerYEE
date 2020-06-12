import discord
from discord.ext import commands



class help(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx)
        msg = await ctx.author.create_dm()
        embed = discord.Embed(title="*명령어!*", color=0xff00)
        embed.set_footer(text=str(self.client.get_user(444363545635848193)) + "가 만들었습니다!", icon_url=self.client.get_user(444363545635848193).avatar_url)
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/704619025258512444/6b4cf3a72bb22ad2726a46f6a508c5ad.webp?size=1024")
        embed.add_field(name="잡 명령어", value="사랑해, 주인, 죽어, 제작, 띵크, 띵킹, 초대, invite say, 말해, 때려, 생성(qr코드 생성입니다!)")
        embed.add_field(name="밈", value="관짝, 관짝춤")
        embed.add_field(name="유틸", value="타이머, 주사위, roll, 아바타, avatar, 유저정보, userinfo, 홀짝(미완이라 숫자만 되요!), 업타임, ping, 핑, 봇정보")
        embed.add_field(name="밈", value="관짝, 관짝춤")
        embed.add_field(name="관리", value="밴, 언밴, 킥, 추방, 뮤트(뮤트라는 역할이 있어야 해요!), 언뮤트(뮤트라는 역할이 있어야 해요!)")
        embed.add_field(name="띵킹눈, 띵킹빵, 띵킹버거, 띵킹박수, 띵킹가지, 띵킹피젯, 띵킹물고기, 띵킹하드, 띵킹인터넷, 띵킹레몬, 띵킹비정상")
        embed.add_field(name="음악", value="play(p, ㅔ), connect(join)<--비상용, pause(일시중지), skip(s, ㄴ), queue(q, playlist),  now_playing(np, current, playing),volume(vol), stop")
        await ctx.send(ctx.author.mention + "DM으로 도움말을 보냈어요!")
        await msg.send(embed=embed)

    @commands.command()
    async def 도움말(self, ctx)
        msg = await ctx.author.create_dm()
        embed = discord.Embed(title="*도움말!*", color=0xff00)
        embed.set_footer(text=str(self.client.get_user(444363545635848193)) + "가 만들었습니다!", icon_url=self.client.get_user(444363545635848193).avatar_url)
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/704619025258512444/6b4cf3a72bb22ad2726a46f6a508c5ad.webp?size=1024")
        embed.add_field(name="잡 명령어", value="사랑해, 주인, 죽어, 제작, 띵크, 띵킹, 초대, invite say, 말해, 때려")
        embed.add_field(name="밈", value="관짝, 관짝춤")
        embed.add_field(name="유틸", value="타이머, 주사위, roll, 아바타, avatar, 유저정보, userinfo, 홀짝(미완이라 숫자만 되요!), 업타임, ping, 핑, 봇정보")
        embed.add_field(name="밈", value="관짝, 관짝춤")
        embed.add_field(name="관리", value="밴, 언밴, 킥, 추방, 뮤트(뮤트라는 역할이 있어야 해요!), 언뮤트(뮤트라는 역할이 있어야 해요!)")
        embed.add_field(name="띵킹눈, 띵킹빵, 띵킹버거, 띵킹박수, 띵킹가지, 띵킹피젯, 띵킹물고기, 띵킹하드, 띵킹인터넷, 띵킹레몬, 띵킹비정상")
        embed.add_field(name="음악", value="play(p, ㅔ), connect(join)<--비상용, pause(일시중지), skip(s, ㄴ), queue(q, playlist),  now_playing(np, current, playing),volume(vol), stop")
        await ctx.send(ctx.author.mention + "DM으로 도움말을 보냈어요!")
        await msg.send(embed=embed)

    @commands.command()
    async def 도움(self, ctx)
        msg = await ctx.author.create_dm()
        embed = discord.Embed(title="*도움말!*", color=0xff00)
        embed.set_footer(text=str(self.client.get_user(444363545635848193)) + "가 만들었습니다!", icon_url=self.client.get_user(444363545635848193).avatar_url)
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/704619025258512444/6b4cf3a72bb22ad2726a46f6a508c5ad.webp?size=1024")
        embed.add_field(name="잡 명령어", value="사랑해, 주인, 죽어, 제작, 띵크, 띵킹, 초대, invite say, 말해, 때려")
        embed.add_field(name="밈", value="관짝, 관짝춤")
        embed.add_field(name="유틸", value="타이머, 주사위, roll, 아바타, avatar, 유저정보, userinfo, 홀짝(미완이라 숫자만 되요!), 업타임, ping, 핑, 봇정보")
        embed.add_field(name="밈", value="관짝, 관짝춤")
        embed.add_field(name="관리", value="밴, 언밴, 킥, 추방, 뮤트(뮤트라는 역할이 있어야 해요!), 언뮤트(뮤트라는 역할이 있어야 해요!)")
        embed.add_field(name="띵킹눈, 띵킹빵, 띵킹버거, 띵킹박수, 띵킹가지, 띵킹피젯, 띵킹물고기, 띵킹하드, 띵킹인터넷, 띵킹레몬, 띵킹비정상")
        embed.add_field(name="음악", value="play(p, ㅔ), connect(join)<--비상용, pause(일시중지), skip(s, ㄴ), queue(q, playlist),  now_playing(np, current, playing),volume(vol), stop")
        await ctx.send(ctx.author.mention + "DM으로 도움말을 보냈어요!")
        await msg.send(embed=embed)

    @commands.command()
    async def cmds(self, ctx)
        msg = await ctx.author.create_dm()
        embed.set_footer(text=str(self.client.get_user(444363545635848193)) + "가 만들었습니다!", icon_url=self.client.get_user(444363545635848193).avatar_url)
        embed = discord.Embed(title="*커맨드!!*", color=0xff00)
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/704619025258512444/6b4cf3a72bb22ad2726a46f6a508c5ad.webp?size=1024")
        embed.add_field(name="잡 명령어", value="사랑해, 주인, 죽어, 제작, 띵크, 띵킹, 초대, invite say, 말해, 때려")
        embed.add_field(name="밈", value="관짝, 관짝춤")
        embed.add_field(name="유틸", value="타이머, 주사위, roll, 아바타, avatar, 유저정보, userinfo, 홀짝(미완이라 숫자만 되요!), 업타임, ping, 핑, 봇정보")
        embed.add_field(name="밈", value="관짝, 관짝춤")
        embed.add_field(name="관리", value="밴, 언밴, 킥, 추방, 뮤트(뮤트라는 역할이 있어야 해요!), 언뮤트(뮤트라는 역할이 있어야 해요!)")
        embed.add_field(name="띵킹눈, 띵킹빵, 띵킹버거, 띵킹박수, 띵킹가지, 띵킹피젯, 띵킹물고기, 띵킹하드, 띵킹인터넷, 띵킹레몬, 띵킹비정상")
        embed.add_field(name="음악", value="play(p, ㅔ), connect(join)<--비상용, pause(일시중지), skip(s, ㄴ), queue(q, playlist),  now_playing(np, current, playing),volume(vol), stop")
        await ctx.send(ctx.author.mention + "DM으로 도움말을 보냈어요!")
        await msg.send(embed=embed)
        
        
        
def setup(client): 
    client.add_cog(help(client))
