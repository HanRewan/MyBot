import discord
from discord.ext import commands
import youtube_dl
import random
import requests
client = commands.Bot(command_prefix='$')
@client.event

async def on_ready():
    print('Logged on')


def Dice(d):
    if(d==""): return 0
    else:
        num=str()
        d_type=str()
        p=0
        try:
            while d[p]!="d":
                num+=d[p]
                p+=1
            p+=1
            while p < len(d):
                d_type += d[p]
                p += 1
            num = int(num)
            d_type = int(d_type)
            part_res = 0
            for i in range(num):
                part_res += random.randint(1, d_type)
            return part_res
        except IndexError:
            return int(num)

def count(text):
    pointer=11
    part=str()
    res=0
    while pointer<len(text):
        if(text[pointer]!='+'):
            part+=text[pointer]
        else:
            res+=Dice(part)
            part=""
        pointer+=1
    return res+Dice(part)

@client.command(pass_context=True)
async def DnD_count(ctx):
    await ctx.send(count(ctx.message.content))

@client.command(pass_context=True)
async def join(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if ctx.author.voice is None:
        await ctx.send("Ти не в войсі")
    voice_channel=ctx.author.voice.channel
    if voice is None:
        await voice_channel.connect()
    else:
        await voice.disconnect()
        await voice_channel.connect()

@client.command(pass_context=True)
async def disconnect(ctx):
    await ctx.voice_client.disconnect()

@client.command(pass_context=True)
async def play(ctx, url):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if ctx.author.voice is None:
        await ctx.send("Ти не в войсі")
    voice_channel = ctx.author.voice.channel
    if voice is None:
        await voice_channel.connect()
    else:
        await voice.disconnect()
        await voice_channel.connect()
    ctx.voice_client.stop()
    YDL_OPTIONS = {'format': "bestaudio"}

    with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
        info = ydl.extract_info(url, download=False)
        """
        print(info['entries'][0]['formats'][0]['url'])
        """
        try:
            if info['_type'] == 'playlist':
                for i in range(len(info['entries'])):
                    url2=[]
                    url2.append(info['entries'][i]['formats'][0]['url'])
                ctx.message.guild.voice_client.play(discord.FFmpegPCMAudio(url2[0], executable="D:/PyCharm Community Edition 2020.2.2/DiscordBot/ffmpeg/ffmpeg-master-latest-win64-gpl-shared/bin/ffmpeg.exe"))
                await ctx.send("Плей листи поламані. (можу грати лише останній трек з плей листа)")
        except KeyError:
            url2 = info['formats'][0]['url']
            ctx.message.guild.voice_client.play(discord.FFmpegPCMAudio(url2, executable="D:/PyCharm Community Edition 2020.2.2/DiscordBot/ffmpeg/ffmpeg-master-latest-win64-gpl-shared/bin/ffmpeg.exe"))


@client.command(pass_context=True)
async def pause(ctx):
    await ctx.voice_client.pause()
    await ctx.send("Пауза")

@client.command(pass_context=True)
async def resume(ctx):
    await ctx.voice_client.resume()
    await ctx.send("Запуск")

@client.command(pass_context=True)
async def find(ctx, item_type, item_name):
    items={
        "spell": "https://dnd5.club/spells/",
        "weapon": "https://dnd5.club/weapons/",
        "armor": "https://dnd5.club/armors/"
    }

    try:
        url = items[item_type]
    except KeyError:
        await ctx.send("Предметів такого типу не існує.")
        return

    page = requests.Session()
    datas = {'html body#body div#container.container div#list_page_two_block.table_list_block.block_information div#left_block.spells div.header_block.filters div.search_block div.input_block input#search.search_int': item_name}
    enter_data = requests.post(url, data=datas)
    print(enter_data.content)

@client.command(pass_context=True)
async def fight_music(ctx):
    url="https://www.youtube.com/watch?v=htCcgpisgtk"
    await play(ctx, url)

@client.command(pass_context=True)
async def normal_music(ctx):
    url=["https://www.youtube.com/watch?v=wLlovxa3VJ0&t=896s", "https://www.youtube.com/watch?v=pgLjYsVP4H0", "https://www.youtube.com/watch?v=M0pOMVCUY50"]
    i=random.randint(0,len(url)-1)
    await play(ctx, url[i])

@client.command(pass_context=True)
async def dark_music(ctx):
    url=["https://www.youtube.com/watch?v=415-xHoSwwA", "https://www.youtube.com/watch?v=0Fl9-359oeg&t=17s"]
    i=random.randint(0,len(url)-1)
    await play(ctx, url[i])

async def add_song(ctx):
    pass


client.run('ODQ1NjUzNDk3MzU3MTM5OTY4.YKkGMQ.6RbZ3k0bbG1mk0lW9PRRDJe9ioA')
