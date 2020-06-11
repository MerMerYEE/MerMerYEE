import discord
from discord.ext import commands

import asyncio
import itertools
import sys
import traceback
from async_timeout import timeout
from functools import partial
from youtube_dl import YoutubeDL


ytdlopts = {
    'format': 'bestaudio/best',
    'outtmpl': 'downloads/%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0'  # ipv6 addresses cause issues sometimes
}

ffmpegopts = {
    'before_options': '-nostdin',
    'options': '-vn'
}

ytdl = YoutubeDL(ytdlopts)


class VoiceConnectionError(commands.CommandError):
    """Custom Exception class for connection errors."""


class InvalidVoiceChannel(VoiceConnectionError):
    """Exception for cases of invalid Voice Channels."""


class YTDLSource(discord.PCMVolumeTransformer):

    def __init__(self, source, *, data, requester):
        super().__init__(source)
        self.requester = requester

        self.title = data.get('title')
        self.web_url = data.get('webpage_url')

        # YTDL info dicts (data) have other useful information you might want
        # https://github.com/rg3/youtube-dl/blob/master/README.md

    def __getitem__(self, item: str):
        return self.__getattribute__(item)

    @classmethod
    async def create_source(cls, ctx, search: str, *, loop, download=False):
        loop = loop or asyncio.get_event_loop()

        to_run = partial(ytdl.extract_info, url=search, download=download)
        data = await loop.run_in_executor(None, to_run)

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        await ctx.send(f'```ini\n[Added {data["title"]} to the Queue.]\n```', delete_after=15)

        if download:
            source = ytdl.prepare_filename(data)
        else:
            return {'webpage_url': data['webpage_url'], 'requester': ctx.author, 'title': data['title']}

        return cls(discord.FFmpegPCMAudio(source), data=data, requester=ctx.author)

    @classmethod
    async def regather_stream(cls, data, *, loop):
        loop = loop or asyncio.get_event_loop()
        requester = data['requester']

        to_run = partial(ytdl.extract_info, url=data['webpage_url'], download=False)
        data = await loop.run_in_executor(None, to_run)

        return cls(discord.FFmpegPCMAudio(data['url']), data=data, requester=requester)


class MusicPlayer:
    __slots__ = ('bot', '_guild', '_channel', '_cog', 'queue', 'next', 'current', 'np', 'volume')

    def __init__(self, ctx):
        self.bot = ctx.bot
        self._guild = ctx.guild
        self._channel = ctx.channel
        self._cog = ctx.cog

        self.queue = asyncio.Queue()
        self.next = asyncio.Event()

        self.np = None  # Now playing message
        self.volume = .5
        self.current = None

        ctx.bot.loop.create_task(self.player_loop())

    async def player_loop(self):
        await self.bot.wait_until_ready()

        while not self.bot.is_closed():
            self.next.clear()

            try:
                # Wait for the next song. If we timeout cancel the player and disconnect...
                async with timeout(300):  # 5 minutes...
                    source = await self.queue.get()
            except asyncio.TimeoutError:
                return self.destroy(self._guild)

            if not isinstance(source, YTDLSource):
                # Source was probably a stream (not downloaded)
                # So we should regather to prevent stream expiration
                try:
                    source = await YTDLSource.regather_stream(source, loop=self.bot.loop)
                except Exception as e:
                    await self._channel.send(f'There was an error processing your song.\n'
                                             f'```css\n[{e}]\n```')
                    continue

            source.volume = self.volume
            self.current = source

            self._guild.voice_client.play(source, after=lambda _: self.bot.loop.call_soon_threadsafe(self.next.set))
            self.np = await self._channel.send(f'**Now Playing:** `{source.title}` requested by '
                                               f'`{source.requester}`')
            await self.next.wait()

            # Make sure the FFmpeg process is cleaned up.
            source.cleanup()
            self.current = None

            try:
                # We are no longer playing this song...
                await self.np.delete()
            except discord.HTTPException:
                pass

    def destroy(self, guild):
        return self.bot.loop.create_task(self._cog.cleanup(guild))


class ko_Music(commands.Cog):

    __slots__ = ('bot', 'players')

    def __init__(self, bot):
        self.bot = bot
        self.players = {}

    async def cleanup(self, guild):
        try:
            await guild.voice_client.disconnect()
        except AttributeError:
            pass

        try:
            del self.players[guild.id]
        except KeyError:
            pass

    async def __local_check(self, ctx):
        if not ctx.guild:
            raise commands.NoPrivateMessage
        return True

    async def __error(self, ctx, error):
        if isinstance(error, commands.NoPrivateMessage):
            try:
                return await ctx.send('This command can not be used in Private Messages.')
            except discord.HTTPException:
                pass
        elif isinstance(error, InvalidVoiceChannel):
            await ctx.send('Error connecting to Voice Channel. '
                           'Please make sure you are in a valid channel or provide me with one')

        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

    def get_player(self, ctx):
        try:
            player = self.players[ctx.guild.id]
        except KeyError:
            player = MusicPlayer(ctx)
            self.players[ctx.guild.id] = player

        return player

    @commands.command(name='connect', aliases=['join'])
    async def connect_(self, ctx, *, channel: discord.VoiceChannel=None):
        
        if not channel:
            try:
                channel = ctx.author.voice.channel
            except AttributeError:
                raise InvalidVoiceChannel('알 수 없는 채널이거나 이미 접속해 있는 채널이에요!')

        vc = ctx.voice_client

        if vc:
            if vc.channel.id == channel.id:
                return
            try:
                await vc.move_to(channel)
            except asyncio.TimeoutError:
                raise VoiceConnectionError(f'채널을 바꿨어요!: <{channel}> 타임 아웃!')
        else:
            try:
                await channel.connect()
            except asyncio.TimeoutError:
                raise VoiceConnectionError(f'채널에 접속했어요!: <{channel}> 타임 아웃!')

        await ctx.trigger_typing()
        embed = discord.Embed(title="Music", description= f'채널에 점속했어요!: **{channel}**', color=0x8680df)
        embed.set_footer(text=str(client.get_user(444363545635848193)) + "가 만들었습니다!", icon_url=client.get_user(444363545635848193).avatar_url)
        await ctx.send(embed=embed)

    @commands.command(name='play', aliases=['sing', 'p', 'ㅔ'])
    async def play_(self, ctx, *, search: str):
        await ctx.trigger_typing()

        vc = ctx.voice_client

        if not vc:
            await ctx.invoke(self.connect_)

        player = self.get_player(ctx)

        # If download is False, source will be a dict which will be used later to regather the stream.
        # If download is True, source will be a discord.FFmpegPCMAudio with a VolumeTransformer.
        source = await YTDLSource.create_source(ctx, search, loop=self.bot.loop, download=False)

        await player.queue.put(source)

    @commands.command(name='pause')
    async def pause_(self, ctx):
        
        vc = ctx.voice_client

        if not vc or not vc.is_playing():
            await ctx.trigger_typing()
            embed = discord.Embed(title="Music", description= '저는 지금 아무 트랙도 플레이하고 있지 않아요!', color=0x8680df)
            embed.set_footer(text=str(client.get_user(444363545635848193)) + "가 만들었습니다!", icon_url=client.get_user(444363545635848193).avatar_url)
            await ctx.send(embed=embed)
        elif vc.is_paused():
            return

        vc.pause()
        await ctx.send(f'**`{ctx.author}`**: 노래를 일시 중지했어!!')

    @commands.command(name='resume')
    async def resume_(self, ctx):
        
        vc = ctx.voice_client

        if not vc or not vc.is_connected():
            await ctx.trigger_typing()
            embed = discord.Embed(title="MUSIC", description= '저는 지금 음성채널에 들어가 있지 않아요!', color=0x8680df)
            embed.set_footer(text=str(client.get_user(444363545635848193)) + "가 만들었습니다!", icon_url=client.get_user(444363545635848193).avatar_url)
            await ctx.send(embed=embed)
        elif not vc.is_paused():
            return

        vc.resume()
        await ctx.send(f'**`{ctx.author}`**: 노래를 다시 시작했어요!!')

    @commands.command(name='skip', aliases=['s', 'ㄴ'])
    async def skip_(self, ctx):
        
        vc = ctx.voice_client

        if not vc or not vc.is_connected():
            await ctx.trigger_typing()
            await ctx.trigger_typing()
            embed = discord.Embed(title="Music", description= '저는 지금 음성채널에 들어가 있지 않아요!', color=0x8680df)
            embed.set_footer(text=str(client.get_user(444363545635848193)) + "가 만들었습니다!", icon_url=client.get_user(444363545635848193).avatar_url)
            await ctx.send(embed=embed)

        if vc.is_paused():
            pass
        elif not vc.is_playing():
            return

        vc.stop()
        await ctx.send(f'**`{ctx.author}`**: 노래를 스킵했어!!')

    @commands.command(name='queue', aliases=['q', 'playlist'])
    async def queue_info(self, ctx):
        
        vc = ctx.voice_client

        if not vc or not vc.is_connected():
            await ctx.trigger_typing()
            await ctx.trigger_typing()
            embed = discord.Embed(title="Music", description= '저는 지금 음성채널에 들어가 있지 않아요!', color=0x8680df)
            embed.set_footer(text=str(client.get_user(444363545635848193)) + "가 만들었습니다!", icon_url=client.get_user(444363545635848193).avatar_url)
            await ctx.send(embed=embed)

        player = self.get_player(ctx)
        if player.queue.empty():
            await ctx.trigger_typing()
            embed = discord.Embed(title="Music", description= '더 이상 대기중인 곡이 없어요!', color=0x8680df)
            embed.set_footer(text=str(client.get_user(444363545635848193)) + "가 만들었습니다!", icon_url=client.get_user(444363545635848193).avatar_url)
            await ctx.send(embed=embed)

        # Grab up to 5 entries from the queue...
        upcoming = list(itertools.islice(player.queue._queue, 0, 5))

        fmt = '\n'.join(f'**`{_["title"]}`**' for _ in upcoming)
        embed = discord.Embed(title=f'Upcoming - Next {len(upcoming)}', description=fmt)

        await ctx.send(embed=embed)

    @commands.command(name='now_playing', aliases=['np', 'current', 'currentsong', 'playing'])
    async def now_playing_(self, ctx):
        
        vc = ctx.voice_client

        if not vc or not vc.is_connected():
            await ctx.trigger_typing()
            embed = discord.Embed(title="Music", description= '저는 지금 음성채널에 들어가 있지 않아요!', color=0x8680df)
            embed.set_footer(text=str(client.get_user(444363545635848193)) + "가 만들었습니다!", icon_url=client.get_user(444363545635848193).avatar_url)
            await ctx.send(embed=embed)

        player = self.get_player(ctx)
        if not player.current:
            await ctx.trigger_typing()
            embed = discord.Embed(title="Music", description= '저는 지금 아무 트랙도 플레이하고 있지 않아요!', color=0x8680df)
            embed.set_footer(text=str(client.get_user(444363545635848193)) + "가 만들었습니다!", icon_url=client.get_user(444363545635848193).avatar_url)
            await ctx.send(embed=embed)

        try:
            # Remove our previous now_playing message.
            await player.np.delete()
        except discord.HTTPException:
            pass

        player.np = await ctx.send(f'**현재 이 노래를 틀고 있어요!:** `{vc.source.title}` '
                                   f'requested by `{vc.source.requester}`')

    @commands.command(name='volume', aliases=['vol'])
    async def change_volume(self, ctx, *, vol: float):
        
        vc = ctx.voice_client

        if not vc or not vc.is_connected():
            await ctx.trigger_typing()
            embed = discord.Embed(title="Music", description= '저는 지금 음성채널에 들어가 있지 않아요!', color=0x8680df)
            embed.set_footer(text=str(client.get_user(444363545635848193)) + "가 만들었습니다!", icon_url=client.get_user(444363545635848193).avatar_url)
            await ctx.send(embed=embed)

        if not 0 < vol < 501:
            return await ctx.send('볼륨은 1부터 500까지만 가능해요!')

        player = self.get_player(ctx)

        if vc.source:
            vc.source.volume = vol / 500

        player.volume = vol / 500
        await ctx.send(f'**`{ctx.author}`**: 볼륨을 설정했어! **{vol}%**')

    @commands.command(name='stop')
    async def stop_(self, ctx):
        
        vc = ctx.voice_client

        if not vc or not vc.is_connected():
            return await ctx.send('채널에 접속해 있지 않아!!', delete_after=20)

        await self.cleanup(ctx.guild)

    @play_.error
    async def play_error(self, ctx, error):
        if isinstance(error, InvalidVoiceChannel):
            await ctx.send("음성 채널에 접속해 있어야 해!")


def setup(bot):
    bot.add_cog(ko_Music(bot))
