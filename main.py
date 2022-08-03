import discord
from discord.ext import commands
import youtube_dl
import random
import requests
import time
import _thread
client = commands.Bot(command_prefix='$')
url2=[]
last=0
@client.event
async def on_ready(): #Ця команда виконуєтся при запуску бота
    print('Logged on')

def stream(ctx):
    p = 0
    while True:
        if(ctx.voice_client.is_playing()):
            pass
        else:
            if(p<last):
                p+=1
                ctx.message.guild.voice_client.play(discord.FFmpegPCMAudio(url2[p], executable="D:/PyCharm Community Edition 2020.2.2/DiscordBot/ffmpeg/ffmpeg-master-latest-win64-gpl-shared/bin/ffmpeg.exe"))


def Dice(d): #рахує конкретний кубик
    if(d==""): return 0
    else:
        num=str() #кількість кубиків
        d_type=str() #кількість граней
        p=0 #pointer
        try:
            while d[p]!="d":#йде вздовж тексту кубика поки не потрапить на d
                num+=d[p]
                p+=1
            p+=1
            while p < len(d):#йде по тексту після d
                d_type += d[p]
                p += 1
            num = int(num) #робить з стрінгів числа
            d_type = int(d_type)
            part_res = 0
            for i in range(num):
                part_res += random.randint(1, d_type)#рандомно кидає куби
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
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild) #отримує айді войсу в яку сидить бот
    if ctx.author.voice is None:
        await ctx.send("Ти не в войсі")
    voice_channel=ctx.author.voice.channel #отримує айді войсу в яку сидить юзер
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
    #усе вище код команди join()
    ctx.voice_client.stop() #зупиняє пісню що зараз грає бот. (якщо грає)
    YDL_OPTIONS = {'format': "bestaudio"} #налаштування аудіо

    with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
        info = ydl.extract_info(url, download=False) #качає відео в webp
        """
        print(info['entries'][0]['formats'][0]['url'])
        """
        try:
            if info['_type'] == 'playlist':
                url2 = []
                for i in range(len(info['entries'])):
                    url2.append(info['entries'][i]['formats'][0]['url'])
                for i in range(len(info['entries'])):
                    ctx.message.guild.voice_client.play(discord.FFmpegPCMAudio(url2[i], executable="D:/PyCharm Community Edition 2020.2.2/DiscordBot/ffmpeg/ffmpeg-master-latest-win64-gpl-shared/bin/ffmpeg.exe"))
                #await ctx.send("Плей листи поламані. (можу грати лише останній трек з плей листа)")
        except KeyError:
            url2=info['formats'][0]['url']#дістає посилання
            ctx.message.guild.voice_client.play(discord.FFmpegPCMAudio(url2, executable="D:/PyCharm Community Edition 2020.2.2/DiscordBot/ffmpeg/ffmpeg-master-latest-win64-gpl-shared/bin/ffmpeg.exe")) #запускає пісню через FFmpeg


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
async def boss_fight_music(ctx):
    url="https://www.youtube.com/watch?v=jxzX3OHaGw8"
    await play(ctx, url)

@client.command(pass_context=True)
async def DOOM_music(ctx):
    url="https://www.youtube.com/watch?v=2XI7YwUMHEs"
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
