import discord
from discord.ext import commands
import youtube_dl
client = commands.Bot(command_prefix='$', pass_context=True)
@client.event


class music(commands.Cog):
    def __init__(self, client):
        self.client=client

    @commands.command()
    async def join(self, ctx):
        if ctx.author.voice is None:
             await ctx.send("Ти не в войсі")
        voice_channel=ctx.author.voice.channel
        if ctx.author.voice is None:
            await voice_channel.connect()
        else:
            await ctx.voice_clinet.move_to(voice_channel)

    @commands.command()
    async def disconnect(self, ctx):
        await ctx.voice_clinet.disconnect()

    @commands.command()
    async def play(self, ctx, url):
        ctx.voice_client.stop()
        FFMPEG_OPTIONS={'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        YDL_OPTIONS={'format': "bestaudio"}
        vc=ctx.voice_client

        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
            vc.play(source)

    @commands.command()
    async def pause(self, ctx):
        await ctx.voice_clinet.pause()
        await ctx.send("Paused")

    @commands.command()
    async def resume(self, ctx):
        await ctx.voice_clinet.resume()
        await ctx.send("Resumed")
client.run('ODQ1NjUzNDk3MzU3MTM5OTY4.YKkGMQ.6RbZ3k0bbG1mk0lW9PRRDJe9ioA')

