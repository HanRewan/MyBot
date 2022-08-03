import discord
from discord.ext import commands
import random

class MyClient(discord.Client, commands.Cog):
    async def join(self, ctx):
        await ctx.author.voice.channel.connect()
    def Dice(self, d):
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
            except IndexError: return int(num)

    def count(self, text):
        pointer=11
        part=str()
        res=0
        while pointer<len(text):
            if(text[pointer]!='+'):
                part+=text[pointer]
            else:
                res+=self.Dice(part)
                part=""
            pointer+=1
        return res+self.Dice(part)

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.author == client.user:
            return

        if message.content.startswith('$hello'):
            await message.channel.send(message.content)

        if message.content.startswith('$D&D_count'):
            await message.channel.send(self.count(message.content))

client = MyClient()
client.run('ODQ1NjUzNDk3MzU3MTM5OTY4.YKkGMQ.6RbZ3k0bbG1mk0lW9PRRDJe9ioA')
