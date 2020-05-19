import discord
import asyncio
import tasks
import requests
from bs4 import BeautifulSoup
import os


client = discord.AutoShardedClient()


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
async def on_message(message):

    if message.author.bot:
        return

    

    if message.content == "데쿠야 미도리야":
        embed = discord.Embed()
        file = discord.File("미도리야.jpg")
        embed.set_image(url="attachment://미도리야.jpg")
        await message.channel.send(file=file, embed=embed)
    

    if message.content == '데쿠야 제작':
        embed=discord.Embed(color=0xff00, title="제작자:오타쿠#5251", description="도움주신분:한곰#6567\nLLOOOOTT#0817\n승현#1702", timestamp=message.created_at)
        embed.set_footer(text=message.author, icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)

    if message.content == '데쿠야 명령어':
        embed=discord.Embed(color=0xff00, title="명령어", description="데쿠야 help\n데쿠야 명령어\n데쿠야 제작\n데쿠야 메이플(미완)\n데쿠야 초대\n데쿠야 제작자트위치\n데쿠야 롤", timestamp=message.created_at)
        embed.set_footer(text=message.author, icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)


    if message.content == "데쿠야 ping":
        await message.channel.send(f"{int(client.latency *1000)}ms이야!")


    if message.content == "데쿠야 핑":
        await message.channel.send(f"{int(client.latency *1000)}ms이야!")



    if message.content == '데쿠야 help':
        embed=discord.Embed(color=0xff00, title="명령어", description="데쿠야 help\n데쿠야 명령어\n데쿠야 제작\n데쿠야 메이플(미완)\n데쿠야 초대\n데쿠야 제작자트위치\n데쿠야 노래\n데쿠야 롤", timestamp=message.created_at)
        embed.set_footer(text=client.get_user(444363545635848193).name, icon_url=client.get_user(444363545635848193).avatar_url)
        await message.channel.send(embed=embed)


    async def on_message(self, message):
        if message.auathor.id == self.user.id:
            return

    if message.content == "데쿠야 주인":
        user = message.author.id
        if user == 444363545635848193:
            await message.channel.send("와!! 주인님!!")
        else:
            await message.channel.send("누...누구세요..?")

        




    if message.content.startswith('데쿠야 거꾸로'):
        rv = ' '.join(message.content.split(' ')[1:])
        await message.channel.send(rv[::-1])

    if message.content.startswith("데쿠야 메이플"):
        Name = message.content[8:len(message.content)]

        await message.channel.send("https://maple.gg/u/"+Name)

    if message.content == "데쿠야 사용중인 길드 목록":
        if message.author.id == 444363545635848193:
            await message.channel.send(','.join([a.name for a in client.guilds]))

        else:
            await message.channel.send("너가 이거 보면 나 영정이야 안대")



    if message.content == "데쿠야 초대":
        await message.channel.send("https://bit.ly/2Z8fA2C 여기있어")

    if message.content == "데쿠야 invite":
        await message.channel.send("https://bit.ly/2Z8fA2C 여기있어")


    if message.content == "데쿠야 트위치":
        await message.channel.send("트위치는 뭘뭘이이지! https://m.twitch.tv/MerMerYEE")


    if message.content.startswith("데쿠야 입력"):
        if message.author.id == 444363545635848193:
            embed=discord.Embed(color=0xff00, title="입력 결과", description=f"""input📥
            ```py
            {message.content[6:]}
            ```
            output📤
            ```py
            {eval(message.content[6:])}
            ```
            """)
            await message.channel.send(embed=embed)
        else:
            embed=discord.Embed(color=0xff00, title="오류!", description=f"너 이 권한이 없는데? : {owner_per}")
            await message.channel.send(embed=embed)

    if message.content == '데쿠야 노래':
        embed=discord.Embed(color=0xff00, title="노래 명령어", description="데쿠야 재생\n데쿠야 들어와\n데쿠야 나가", timestamp=message.created_at)
        embed.set_footer(text=message.author, icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)


    if message.content.startswith("데쿠야 롤"):
        lol = message.content[6:].replace("+",  "%2B").replace(" ", "+")
        await message.channel.send("https://www.op.gg/summoner/userName="+lol)












    
client.run(os.environ['TOKEN'])
