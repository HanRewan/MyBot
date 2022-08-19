import discord
from discord.ext import commands
import youtube_dl
import random
import requests
from threading import Thread
clientM = commands.Bot(command_prefix='!')
url2=[]
last=0
@clientM.event
async def on_ready(): #Ця команда виконуєтся при запуску бота
    print('Logged on Master')

@clientM.command(pass_context=True)
async def join(ctx):
    voice = discord.utils.get(clientM.voice_clients, guild=ctx.guild) #отримує айді войсу в яку сидить бот
    if ctx.author.voice is None:
        await ctx.send("Ти не в войсі")
    voice_channel=ctx.author.voice.channel #отримує айді войсу в яку сидить юзер
    if voice is None:
        await voice_channel.connect()
    else:
        await voice.disconnect()
        await voice_channel.connect()

@clientM.command(pass_context=True)
async def disconnect(ctx):
    await ctx.voice_client.disconnect()

clientM.run('MTAwNDM3Mjc5MzQyMjUyNDQyNg.GAhfhM.pC3SHOeFJHHe6CPL2pLVE9cqyd8EC1idW8-oEM')


