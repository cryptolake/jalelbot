#!/usr/bin/env python3
import discord
import random
from random import randint
from os import listdir

jalel = open('./jalel').readlines()
ball = open('./ball').readlines()
st = listdir('./voices/')
key = open('key').readline()
allahu = listdir('./allahu/')
client = discord.Client()
global jaleli
jaleli = "jalel"
global tkalem
tkalem = "tkalem"
global allah
allah = "rab"

def quote():
    return random.choice(jalel)

def magicball():
    return random.choice(ball)

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        global counter
        counter = 0
        if message.author == self.user:
            return
        if "?" in message.content and jaleli in message.content.lower() and counter <= 5:
            if "kadeh" in message.content:
                await message.channel.send("ahawa kadeh: " + str(randint(0, 10)))
            else:
                await message.channel.send(magicball())
            counter = counter + 1
        elif jaleli in message.content.lower():
            global voice
            global channel
            if tkalem in message.content.lower():
                try:
                    channel = message.author.voice.channel
                    voice = await channel.connect()
                    voice.play(source=discord.FFmpegPCMAudio(
                        './st/' + random.choice(st)))
                    await message.channel.send('hani jeyek')
                except:
                    voice.stop()
                    voice.play(source=discord.FFmpegPCMAudio(
                        './st/' + random.choice(st)))
                    await message.channel.send('hani jeyek')
            elif allah in message.content.lower():
                try:
                    voice.stop()
                    voice.play(source=discord.FFmpegPCMAudio(
                        './allahu/'+random.choice(allahu)))
                except:
                    channel = message.author.voice.channel
                    voice = await channel.connect()
                    voice.stop()
                    voice.play(source=discord.FFmpegPCMAudio(
                        './allahu/'+random.choice(allahu)))
                    await message.channel.send('haw jayek rabek')

            else:
                await message.channel.send(quote())
                await voice.disconnect()
                counter = 0


bot = MyClient()
bot.run(key)
