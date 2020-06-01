import discord 
from discord.ext import commands
import asyncio
import random
import os
import pymysql

client = commands.AutoShardedBot(command_prefix = '데쿠야 ')
client.remove_command('help')


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

@client.enent
async def on_member_join(member):
    role = "킹반인"
    for i in member.server.roles:
        if i.name == "킹반인"
            role = i
            break
    await client.add_roles(member, role)
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(color=0xff00, title="__**오류!**__", description = "`Invalid command used`")
        await ctx.send(embed=embed)

@client.command(pass_context = True)
async def clear(ctx, number):
       mgs = [] #Empty list to put all the messages in the log
       number = int(number) #Converting the amount of messages to delete to an integer
       async for x in client.logs_from(ctx.message.channel, limit = number):
           mgs.append(x)
       await client.delete_messages(mgs)

@client.command()
async def 채널저장(ctx, channel: discord.TextChannel):
    await ctx.send(channel.id)


@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'Kicked {member.mention}')

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f' banned {member.mention}')

@client.command()
async def mute(ctx, member : discord.Member):
    guild = ctx.guild

    for role in guild.roles:
        if role.name == "뮤트":
            await member.add_roles(role)
            await ctx.send("{} 얘를 {} 얘가 뮤트 시켰어" .format(member.mention, ctx.author.mention))
            return

            overwrite = discord.permissionsOverwrite(send_messages=False)
            newRole = await guild.create_role(name="뮤트")

            for channel in guild.text_channels:
                await channel.set_permissions(newRole, overwrite=overwrite)

            await member.add_roles(newRole)
            await ctx.send("{} 얘를 {} 얘가 뮤트 시켰어" .format(member.mention, ctx.author.mention))

@client.command()
@commands.has_permissions(ban_members = True)
@commands.bot_has_permissions(ban_members = True)
async def unban(ctx, member):
    await ctx.guild.unban(member)
    await ctx.send(f' 언벤 {user.mention}')

@client.command(aliases=["echo"])
async def say(ctx, *, words):
    await ctx.send(words)

@client.command()
async def 사진(ctx):
    embed = discord.Embed()
    file = discord.File("미도리야.jpg")
    embed.set_image(file=file)
    await ctx.send(embed=embed)

@client.command()
async def 타이머(ctx):
    timer = int(ctx.message.content.split(' ')[2])
    msg = await ctx.send("3초후 " + str(timer) + "초 타이머를 시작합니다!")
    await asyncio.sleep(3)
    for i in range(timer):
        await msg.edit(content = str(i))
        await asyncio.sleep(1)
    await msg.edit(content = "시간 끝")

@client.command()
async def 클래식(ctx):
    await ctx.send(":thinking:")

@client.command()
async def 눈(ctx):
    await ctx.send(client.get_emoji(703129203847200829))

@client.command()
async def 빵(ctx):
    await ctx.send(client.get_emoji(708537624012390518))

@client.command()
async def 버거(ctx):
    await ctx.send(client.get_emoji(708537623836098600))

@client.command()
async def 박수(ctx):
    await ctx.send(client.get_emoji(708537624154996808))

@client.command()
async def 가지(ctx):
    await ctx.send(client.get_emoji(708537623622451213))

@client.command()
async def 피젯(ctx):
    await ctx.send(client.get_emoji(708537623983161435))

@client.command()
async def 물고기(ctx):
    await ctx.send(client.get_emoji(708537623446290493))

@client.command()
async def 하드(ctx):
    await ctx.send(client.get_emoji(708537623794155560))

@client.command()
async def 인터넷(ctx):
    await ctx.send(client.get_emoji(708537623723114517))

@client.command()
async def 레몬(ctx):
    await ctx.send(client.get_emoji(708537623425318944))

@client.command()
async def 비정상(ctx):
    ctx.send(client.get_emoji(708537623706075286))

@client.command()
async def 제작(ctx):
    embed=discord.Embed(color=0xff00, title="제작자:오타쿠#5251", description="도움주신분:한곰#6567\nLLOOOOTT#0817\n승현#1702")
    await ctx.send(embed=embed)

@client.command()
async def 메이플(ctx, Name):
    await ctx.send("https://maple.gg/u/"+Name)

@client.command()
async def invite(ctx):
    await ctx.send("https://bit.ly/2Z8fA2C 여기있어")

@client.command()
async def 초대(ctx):
    await ctx.send("https://bit.ly/2Z8fA2C 여기있어")

@client.command()
async def 띵킹(ctx):
    await ctx.send("띵킹띵킹")

@client.command()
async def 띵크(ctx):
    await ctx.send("띵킹띵킹")

@client.command()
async def lol(ctx, lol):
    await ctx.send("https://www.op.gg/summoner/userName="+lol)

@client.command()
async def 롤(ctx, lol2):
    await ctx.send("https://www.op.gg/summoner/userName="+lol2)

@client.command()
async def 핑(ctx):
    await ctx.send(f"{int(client.latency *1000)}ms이야!")

@client.command()
async def ping(ctx):
    await ctx.send(f"{int(client.latency *1000)}ms이야!")

@client.command()
async def 봇정보(ctx):
    await ctx.send(f"{int(client.latency *1000)}ms이야!")

@client.command()
async def 명령어(ctx):
    embed=discord.Embed(color=0xff00, title="명령어")
    embed.set_footer(text=client.get_user(444363545635848193).name, icon_url=client.get_user(444363545635848193).avatar_url)
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/704619025258512444.png?size=1024")
    embed.add_field(name = '관리 명령어', value = 'ban, unban, mute, unmute (뮤트기능은 뮤트 라는 역할이 있어야 실행됨)')
    embed.add_field(name = '잡 명령어', value = '핑(ping), 주인, help, 명령어, 타이머, 제작, 거꾸로')
    embed.add_field(name = '링크 명령어', value = '메이플(전적), 롤(전적), lol(전적), 트위치(찾기)')
    embed.add_field(name = '띵크', value = '클래식, 빵, 버거, 박수, 가지, 피젯, 물고기, 하드, 인터넷, 레몬, 비정상')
    await ctx.send(embed=embed)

@client.command()
async def help(ctx):
    embed=discord.Embed(color=0xff00, title="명령어")
    embed.set_footer(text=client.get_user(444363545635848193).name, icon_url=client.get_user(444363545635848193).avatar_url)
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/704619025258512444.png?size=1024")
    embed.add_field(name = '관리 명령어', value = 'ban, unban, mute, unmute (뮤트기능은 뮤트 라는 역할이 있어야 실행됨)')
    embed.add_field(name = '잡 명령어', value = '핑(ping), 주인, help, 명령어, 타이머, 제작, 거꾸로')
    embed.add_field(name = '링크 명령어', value = '메이플(전적), 롤(전적), lol(전적), 트위치(찾기)')
    embed.add_field(name = '띵크', value = '클래식, 빵, 버거, 박수, 가지, 피젯, 물고기, 하드, 인터넷, 레몬, 비정상')
    await ctx.send(embed=embed)

@client.command()
async def 도움말(ctx):
    embed=discord.Embed(color=0xff00, title="명령어")
    embed.set_footer(text=client.get_user(444363545635848193).name, icon_url=client.get_user(444363545635848193).avatar_url)
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/704619025258512444.png?size=1024")
    embed.add_field(name = '관리 명령어', value = 'ban, unban, mute, unmute (뮤트기능은 뮤트 라는 역할이 있어야 실행됨)')
    embed.add_field(name = '잡 명령어', value = '핑(ping), 주인, help, 명령어, 타이머, 제작, 거꾸로')
    embed.add_field(name = '링크 명령어', value = '메이플(전적), 롤(전적), lol(전적), 트위치(찾기)')
    embed.add_field(name = '띵크', value = '클래식, 빵, 버거, 박수, 가지, 피젯, 물고기, 하드, 인터넷, 레몬, 비정상')
    await ctx.send(embed=embed)

@client.command()
async def 메이플(ctx, maple):
    await ctx.send("https://maple.gg/u/"+maple)

@client.command()
async def 트위치(ctx, twitch):
    await ctx.send("https://maple.gg/u/"+twitch)

@client.command()
async def maple(ctx, maple2):
    await ctx.send("https://maple.gg/u/"+maple2)

@client.command()
async def 거꾸로(ctx, rv):
    rv = ' '.join(ctx.split(' ')[2:])
    if rv == "enoyreve@":
        return
    if rv == "ereh@":
        return
    await ctx.send(rv[::-1])

number = random.randint(1, 6)
@client.command()
async def 주사위(ctx):
    msg = await ctx.send("3초후 주사위를 돌립니다! (1~6)")
    await asyncio.sleep(3)
    await msg.edit(content="두")
    await msg.edit(content="구")
    await msg.edit(content="두")
    await msg.edit(content="구")
    await msg.edit(content=number + "이 나왔습니다!")
    
    

@client.command()
async def 주인(ctx):
    user = ctx.author.id
    if user == 444363545635848193:
        await ctx.send("와!! 주인님!!")
    else:
        await ctx.send("누...누구세요..?")

@client.command()
async def 사랑해(ctx):
    await ctx.send("저두용~ :heart:")


    






        

    

    


    





client.run("NzA0NjE5MDI1MjU4NTEyNDQ0.XsMwFw.YPfHVhGa2kDfNgUrOfuuYFgeviM")