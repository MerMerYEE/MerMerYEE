import discord 
from discord.ext import commands
import asyncio
import random
import os
import requests
from bs4 import BeautifulSoup

client = commands.AutoShardedBot(command_prefix = "데쿠야 ")
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

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(color=0xff00, title="__**오류!**__", description = "`알 수 없는 명령어야!`")
        await ctx.send(embed=embed)



@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def 삭제(ctx, amount : int):
    await ctx.send("메세지 삭제중~")
    await asyncio.sleep(1)
    await ctx.channel.purge(limit=amount + 2)

@client.command()
async def 채널저장(ctx, channel: discord.TextChannel):
    await ctx.send(channel.id)

@client.command(name="추방", pass_context=True)
@commands.has_permissions(administrator=True)
async def _kick(ctx, *, user_name: discord.Member, reason=None):
    await user_name.kick(reason=reason)
    await ctx.send(str(user_name)+"을(를) 킥했어!")

@client.command(name="밴", pass_context=True)
@commands.has_any_role("Commander")
async def _ban(ctx, *, user_name: discord.Member):
    await user_name.ban()
    await ctx.send(str(user_name)+"을(를) 영원히 보냈어!")

@_ban.error
async def _ban_error(ctx, error):
    if isinstance(error, commands.MissingAnyRole):
        await ctx.send("{} 너 Commander이라는 역할이 필요해!".format(ctx.message.author))

@client.command(name="언밴", pass_context=True)
@commands.has_permissions(administrator=True)
async def _unban(ctx, *, user_name):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = user_name.split('#')
    for ban_entry in banned_users:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"{user.mention}이(가) 갑자기 움직여!! 나 무서워 ㅠㅠ")
            return

@_kick.error
async def _kick_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("{} 너 권한이 없는데?.".format(ctx.message.author))
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("{}님, 유저를 넣지 않았어요!.".format(ctx.message.author))
    if isinstance(error, commands.BadArgument):
        await ctx.send("{}님, 유저를 넣어 주세요!!".format(ctx.message.author))
'''
@client.command(name="뮤트", pass_context=True)
@commands.has_permissions(administrator=True)
@commands.has_any_role("뮤트")
async def _mute(ctx, member : discord.Member):
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
'''
@client.command(name="뮤트", pass_context=True)
@commands.has_permissions(administrator=True)
@commands.has_any_role("뮤트")
async def _Hmute(ctx, member: discord.Member=None):
    member = member or ctx.message.author
    await member.add_roles(get(ctx.guild.roles, name="뮤트"))
    await ctx.channel.send(str(member)+"에게 역할이 적용되었습니다.")

@_Hmute.error
async def _Hmute_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("{} 너 권한이 없는데?.".format(ctx.message.author))
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("{}님, 유저를 넣지 않았어요!.".format(ctx.message.author))
    if isinstance(error, commands.BadArgument):
        await ctx.send("{}님, 유저를 넣어 주세요!!".format(ctx.message.author))
    if isinstance(error, commands.MissingAnyRole):
        await ctx.send("{} 뮤트라는 역할이 존재하지 않는데??".format(ctx.message.author))

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
async def 핑(ctx):
    await ctx.send(f"{int(client.latency *1000)}ms이야!")

@client.command()
async def ping(ctx):
    await ctx.send(f"{int(client.latency *1000)}ms이야!")

@client.command()
async def 봇정보(ctx):
    await ctx.send(f"{int(client.latency *1000)}ms이야!")

@client.command()
async def help(ctx):
    embed=discord.Embed(color=0xff00, title="명령어")
    embed.set_footer(text=client.get_user(444363545635848193).name, icon_url=client.get_user(444363545635848193).avatar_url)
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/704619025258512444.png?size=1024")
    embed.add_field(name = '관리 명령어', value = '밴, 언밴, 뮤트, unmute (뮤트기능은 뮤트 라는 역할이 있어야 실행됨, 밴 명령어는 Commander이라는 역할을 착용하고 있어야 가능함)')
    embed.add_field(name = '잡 명령어', value = '핑(ping), 주인, help, 명령어, 도움말, command, 타이머, 제작, 거꾸로, 사랑해')
    embed.add_field(name = '링크 명령어', value = '메이플(전적), maple, 롤(전적), lol(전적), 트위치(찾기), 오버워치(전적), overwatch(전적)')
    embed.add_field(name = '띵크', value = "띵크")
    await ctx.send(embed=embed)

@client.command()
async def 도움말(ctx):
    embed=discord.Embed(color=0xff00, title="명령어")
    embed.set_footer(text=client.get_user(444363545635848193).name, icon_url=client.get_user(444363545635848193).avatar_url)
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/704619025258512444.png?size=1024")
    embed.add_field(name = '관리 명령어', value = '밴, 언밴, 뮤트, unmute (뮤트기능은 뮤트 라는 역할이 있어야 실행됨, 밴 명령어는 Commander이라는 역할을 착용하고 있어야 가능함)'
    embed.add_field(name = '잡 명령어', value = '핑(ping), 주인, help, 명령어, 도움말, command, 타이머, 제작, 거꾸로, 사랑해')
    embed.add_field(name = '링크 명령어', value = '메이플(전적), maple, 롤(전적), lol(전적), 트위치(찾기), 오버워치(전적), overwatch(전적)')
    embed.add_field(name = '띵크', value = "띵크")
    await ctx.send(embed=embed)

@client.command()
async def 명령어(ctx):
    embed=discord.Embed(color=0xff00, title="명령어")
    embed.set_footer(text=client.get_user(444363545635848193).name, icon_url=client.get_user(444363545635848193).avatar_url)
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/704619025258512444.png?size=1024")
    embed.add_field(name = '관리 명령어', value = '밴, 언밴, 뮤트, unmute (뮤트기능은 뮤트 라는 역할이 있어야 실행됨, 밴 명령어는 Commander이라는 역할을 착용하고 있어야 가능함)'
    embed.add_field(name = '잡 명령어', value = '핑(ping), 주인, help, 명령어, 도움말, command, 타이머, 제작, 거꾸로, 사랑해')
    embed.add_field(name = '링크 명령어', value = '메이플(전적), maple, 롤(전적), lol(전적), 트위치(찾기), 오버워치(전적), overwatch(전적)')
    embed.add_field(name = '띵크', value = "띵크")
    await ctx.send(embed=embed)

@client.command()
async def command(ctx):
    embed=discord.Embed(color=0xff00, title="명령어")
    embed.set_footer(text=client.get_user(444363545635848193).name, icon_url=client.get_user(444363545635848193).avatar_url)
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/704619025258512444.png?size=1024")
    embed.add_field(name = '관리 명령어', value = 'ban, unban, mute, unmute (뮤트기능은 뮤트 라는 역할이 있어야 실행됨)')
    embed.add_field(name = '잡 명령어', value = '핑(ping), 주인, help, 명령어, 도움말, command, 타이머, 제작, 거꾸로, 사랑해')
    embed.add_field(name = '링크 명령어', value = '메이플(전적), maple, 롤(전적), lol(전적), 트위치(찾기), 오버워치(전적), overwatch(전적)')
    embed.add_field(name = '띵크', value = "띵크")
    await ctx.send(embed=embed)



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
    await msg.edit(content=number)
    
    

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

@client.command()
async def 오버워치(ctx, over):
    await ctx.send("https://overwatch.op.gg/search?playerName=" + over)

@client.command()
async def overwatch(ctx, over2):
    await ctx.send("https://overwatch.op.gg/search?playerName=" + over2)

@client.command()
async def 트위치(ctx, twitch):
    await ctx.send("https://m.twitch.tv/"+twitch)

@client.command()
async def twitch(ctx, twitch2):
    await ctx.send("https://m.twitch.tv/"+twitch2)

@client.command()
async def 메이플(ctx, maple1):
    await ctx.send("https://maple.gg/u/"+maple1)

@client.command()
async def maple(ctx, maple2):
    await ctx.send("https://maple.gg/u/"+maple2)

@client.command()
async def lol(ctx, lol):
    await ctx.send("https://www.op.gg/summoner/userName="+lol)

@client.command()
async def 롤(ctx, lol2):
    await ctx.send("https://www.op.gg/summoner/userName="+lol2)

@client.command()
async def 롤테스트(ctx, Name):
    req = requests.get("https://www.op.gg/summoner/userName="+Name)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    #랭크
    Rank1 = soup.find_all("span", {'class': 'tierRank'})
    Rank2 = str(Rank1[0])[str(Rank1[0]).find('nk">') + 4:str(Rank1[0]).find("</span>")]

    #점수
    LP1 = soup.find_all("span", {"class": "LeaguePoints"})
    LP2 = str(LP1[0])[str(LP1[0]).find('">')+2 :str(LP1[0]).find("</sp")]
    LP3 = LP2.strip()

    #승 패 승률 부분
    win1 = soup.find_all("span", {"class": "win"})
    win2 = str(win1[0])[str(win1[0]).find('ns">') + 4:str(win1[0]).find("</sp")]

    lose1 = soup.find_all("span", {"class": "lose"})
    lose2 = str(lose1[0])[str(lose1[0]).find('es">') + 4:str(lose1[0]).find("</sp")]

    ratio1 = soup.find_all("span", {"class": "total"})
    ratio2 = str(ratio1[0])[str(ratio1[0]).find('io">') + 4:str(ratio1[0]).find("</sp")]

    win3 = win2.replace('W', '승')
    lose3 = lose2.replace('L', '패')
    ratio3 = ratio2.replace('Win Ratio', '승률')

    lool = '티어: ' + Rank2 +' / 점수: ' + LP3 +' / '+ratio3+' / '+win3+' / '+lose3
    await ctx.send(lool)

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

@client.command()
async def 생성(ctx, qrr):
    qr.add_data(qrr)
    qr.make(fit=True)

    img = qr.make_image()
    img.save("파일명.png")
    qr.clear()






client.run(os.environ['TOKEN'])
