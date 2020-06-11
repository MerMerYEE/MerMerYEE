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
import typing
import youtube_dl
import re
import koreanbots

client = commands.AutoShardedBot(command_prefix = "데쿠야 ")
Bot = koreanbots.Client(client, 'https://koreanbots.dev/manage/704619025258512444')
Uptime.uptimeset()
client.remove_command('help')

num = random.randint(1, 5)

for filename in os.listdir("Cogs"): #2
    if filename.endswith(".py"): #3
        client.load_extension(f"Cogs.{filename[:-3]}") #4

@client.event
async def on_ready():
    print("다음으로 로그인합니다")
    print(client.user.name)
    print(client.user.id)
    print("================")

    messages = [f'{len(client.guilds)}개의 서버 | {len(client.users)}명의 유저', (f"{int(client.latency *1000)}ms")]
    while True:
       await client.change_presence(status=discord.Status.online, activity=discord.Game(name=messages[0]))
       messages.append(messages.pop(0))
       await asyncio.sleep(3)
    Data = await Bot.getBot('704619025258512444')
       

@client.command(name="로드")
async def load_commands(ctx, extension=None):
    if ctx.author.id == user:
        if extension is None: # extension이 None이면 (그냥 !리로드 라고 썼을 때)
            for filename in os.listdir("Cogs"):
                if filename.endswith(".py"):
                    client.unload_extension(f"Cogs.{filename[:-3]}")
                    client.load_extension(f"Cogs.{filename[:-3]}")
            await ctx.send(":white_check_mark: 모든 명령어를 로드했어요!!")
        else:
            client.load_extension(f"Cogs.{extension}")
            await ctx.send(f":white_check_mark: {extension}을(를) 로드했어요!!")
    else:
        return

@client.command(name="언로드")
async def unload_commands(ctx, extension=None):
    if ctx.author.id == user:
        if extension is None: # extension이 None이면 (그냥 !리로드 라고 썼을 때)
            for filename in os.listdir("Cogs"):
                if filename.endswith(".py"):
                    client.unload_extension(f"Cogs.{filename[:-3]}")
                    client.load_extension(f"Cogs.{filename[:-3]}")
            await ctx.send(":white_check_mark: 모든 명령어를 언로드했어요!!")
        else:
            client.unload_extension(f"Cogs.{extension}")
            await ctx.send(f":white_check_mark: {extension}을(를) 언로드했어요!!")
    else:
        return

@client.command(name="리로드")
async def reload_commands(ctx, extension=None):
    if ctx.author.id == user:
        if extension is None: # extension이 None이면 (그냥 !리로드 라고 썼을 때)
            for filename in os.listdir("Cogs"):
                if filename.endswith(".py"):
                    client.unload_extension(f"Cogs.{filename[:-3]}")
                    client.load_extension(f"Cogs.{filename[:-3]}")
            await ctx.send(":white_check_mark: 모든 명령어를 다시 가져왔어요!!")
        else:
            client.unload_extension(f"Cogs.{extension}")
            client.load_extension(f"Cogs.{extension}")
            await ctx.send(f":white_check_mark: {extension}을(를) 다시 가져왔어요!!")
    else:
        return

'''
@reload_commands.error
async def reload_commands_error(ctx, error):
    if isinstance(error, no)
'''
user = 444363545635848193

@client.command()
async def 때려(ctx, user_ : discord.Member):
    if ctx.author.id == user:
        await ctx.send(str(user_) + " 죽어 퍽퍽")
    if num == 1:
        embed=discord.Embed(color=0xff00, description = "[미도리야가 마음에 드신다면 :heart:를 눌러주세요!](http://koreanbots.dev/bots/704619025258512444)")
        await ctx.send(embed=embed)
    else:
        return

@client.command()
async def 길드(ctx):
    if ctx.author.id == user:
        await ctx.send(client.guilds)
    else:
        return

@client.command()
async def 채널저장(ctx, channel: discord.TextChannel):
    await ctx.send(channel.id)
    if num == 1:
        embed=discord.Embed(color=0xff00, description = "[미도리야가 마음에 드신다면 :heart:를 눌러주세요!](http://koreanbots.dev/bots/704619025258512444)")
        await ctx.send(embed=embed)
    else:
        return

@client.command()
async def 사진(ctx):
    embed = discord.Embed()
    file = discord.File("미도리야.jpg")
    embed.set_image(file=file)
    await ctx.send(embed=embed)
    if num == 1:
        embed=discord.Embed(color=0xff00, description = "[미도리야가 마음에 드신다면 :heart:를 눌러주세요!](http://koreanbots.dev/bots/704619025258512444)")
        await ctx.send(embed=embed)
    else:
        return

@client.command()
async def 클래식(ctx):
    await ctx.send(":thinking:")
    if num == 1:
        embed=discord.Embed(color=0xff00, description = "[미도리야가 마음에 드신다면 :heart:를 눌러주세요!](http://koreanbots.dev/bots/704619025258512444)")
        await ctx.send(embed=embed)
    else:
        return

@client.command()
async def 눈(ctx):
    await ctx.send(client.get_emoji(703129203847200829))
    if num == 1:
        embed=discord.Embed(color=0xff00, description = "[미도리야가 마음에 드신다면 :heart:를 눌러주세요!](http://koreanbots.dev/bots/704619025258512444)")
        await ctx.send(embed=embed)
    else:
        return

@client.command()
async def 빵(ctx):
    await ctx.send(client.get_emoji(708537624012390518))
    if num == 1:
        embed=discord.Embed(color=0xff00, description = "[미도리야가 마음에 드신다면 :heart:를 눌러주세요!](http://koreanbots.dev/bots/704619025258512444)")
        await ctx.send(embed=embed)
    else:
        return

@client.command()
async def 버거(ctx):
    await ctx.send(client.get_emoji(708537623836098600))
    if num == 1:
        embed=discord.Embed(color=0xff00, description = "[미도리야가 마음에 드신다면 :heart:를 눌러주세요!](http://koreanbots.dev/bots/704619025258512444)")
        await ctx.send(embed=embed)
    else:
        return

@client.command()
async def 박수(ctx):
    await ctx.send(client.get_emoji(708537624154996808))
    if num == 1:
        embed=discord.Embed(color=0xff00, description = "[미도리야가 마음에 드신다면 :heart:를 눌러주세요!](http://koreanbots.dev/bots/704619025258512444)")
        await ctx.send(embed=embed)
    else:
        return

@client.command()
async def 가지(ctx):
    await ctx.send(client.get_emoji(708537623622451213))
    if num == 1:
        embed=discord.Embed(color=0xff00, description = "[미도리야가 마음에 드신다면 :heart:를 눌러주세요!](http://koreanbots.dev/bots/704619025258512444)")
        await ctx.send(embed=embed)
    else:
        return

@client.command()
async def 피젯(ctx):
    await ctx.send(client.get_emoji(708537623983161435))
    if num == 1:
        embed=discord.Embed(color=0xff00, description = "[미도리야가 마음에 드신다면 :heart:를 눌러주세요!](http://koreanbots.dev/bots/704619025258512444)")
        await ctx.send(embed=embed)
    else:
        return

@client.command()
async def 물고기(ctx):
    await ctx.send(client.get_emoji(708537623446290493))
    if num == 1:
        embed=discord.Embed(color=0xff00, description = "[미도리야가 마음에 드신다면 :heart:를 눌러주세요!](http://koreanbots.dev/bots/704619025258512444)")
        await ctx.send(embed=embed)
    else:
        return

@client.command()
async def 하드(ctx):
    await ctx.send(client.get_emoji(708537623794155560))
    if num == 1:
        embed=discord.Embed(color=0xff00, description = "[미도리야가 마음에 드신다면 :heart:를 눌러주세요!](http://koreanbots.dev/bots/704619025258512444)")
        await ctx.send(embed=embed)
    else:
        return

@client.command()
async def 인터넷(ctx):
    await ctx.send(client.get_emoji(708537623723114517))
    if num == 1:
        embed=discord.Embed(color=0xff00, description = "[미도리야가 마음에 드신다면 :heart:를 눌러주세요!](http://koreanbots.dev/bots/704619025258512444)")
        await ctx.send(embed=embed)
    else:
        return

@client.command()
async def 레몬(ctx):
    await ctx.send(client.get_emoji(708537623425318944))
    if num == 1:
        embed=discord.Embed(color=0xff00, description = "[미도리야가 마음에 드신다면 :heart:를 눌러주세요!](http://koreanbots.dev/bots/704619025258512444)")
        await ctx.send(embed=embed)
    else:
        return

@client.command()
async def 비정상(ctx):
    ctx.send(client.get_emoji(708537623706075286))
    if num == 1:
        embed=discord.Embed(color=0xff00, description = "[미도리야가 마음에 드신다면 :heart:를 눌러주세요!](http://koreanbots.dev/bots/704619025258512444)")
        await ctx.send(embed=embed)
    else:
        return

@client.command()
async def 거꾸로(ctx, rv):
    if rv == "enoyreve@":
        return
    if rv == "ereh@":
        return
    await ctx.send(reversed(rv))

@client.command()
async def 생성(ctx, qrr):
    img = qrcode.make(qrr)
    img.save("asdf.png")
    qrc = "asdf.png"

    await ctx.send(file=discord.File(qrc))
    if num == 1:
        embed=discord.Embed(color=0xff00, description = "[미도리야가 마음에 드신다면 :heart:를 눌러주세요!](http://koreanbots.dev/bots/704619025258512444)")
        await ctx.send(embed=embed)
    else:
        return

@client.command()
async def eval(ctx, evall):
    embed=discord.Embed(color=0xff00, title="eval 결과", description = "결과 =" + eval(evall))
    await ctx.send(embed=embed)

@client.command()
async def eval2(ctx, eeval):
    if ctx.author.id == user:
        embed=discord.Embed(title="Eval 결과", description=f"""input :inbox_tray:
            
        {ctx.message.content[8:]}
            

        output :outbox_tray:
            
        {eval(ctx.message.content[8:])}
            

        """)
        await ctx.send(embed=embed)
    else:
        embed=discord.Embed(title="오류!", description="봇 제작자가 아닙니다!")
        await ctx.send(embed=embed)



def find(filename, directory):
    if os.path.exists(directory+filename): # 파일이 존재한다면
        return True # True 반환
    else: # 아니면
        return False # False 반환

def returnAddData(filename, directory, num):
    try: # 에러 처리
        f = open(directory+filename, "r") # 읽기 전용으로 파일 열기
        data = f.read() # 읽고 data에 저장
        f.close() # 파일 닫기
        f = open(directory+filename, "w") # 쓰기 전용으로 파일 열기
        f.write(str(int(data)+int(num))) # 더하기
        f.close() # 파일 닫기
    except FileNotFoundError: # 에러가 날 경우 
        print("Error : File not found") # 출력

@client.command(name="경고", pass_context=True)
@commands.has_permissions(administrator=True)
async def _warn(ctx, counts, user_name : typing.Optional[discord.Member]=None, reason="없음"):
    if user_name == None or user_name == ctx.message.author:
        await ctx.send("자신에겐 경고를 줄 수 없어요!")
    else:
        foundfile = find(str(user_name)+".txt", "warnings/")
        if foundfile:
            warnings = returnAddData(str(user_name)+".txt", "warnings/", counts)
            if warnings >= 10:
                await user_name.ban()
                await ctx.send(str(user_name)+"이(가) 경고 때문에 밴 되었어요 ㅠㅠ")
            else:
                await ctx.send(str(user_name)+"에게 경고를 줬어요!!")
        else:
            f = open("warnings/"+str(user_name)+".txt", "w+")
            f.write(str(int(counts)))
            f.close()
            await ctx.send(str(user_name)+"에게 경고를 부여했어요!")

@_warn.error
async def _warn_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("{}님! 권한이 없는데요?!".format(ctx.message.author))

if os.path.exists("warnings"):
    print("Warnings Dir found, passing")
else:
    os.mkdir("warnings")







client.run(os.environ['TOKEN'])
