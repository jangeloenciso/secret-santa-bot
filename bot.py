import os
import random
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

names = []

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    name = message.author.name
    nabunot = name
    content = message.content 

    if content == '!bunot':
        if names:
            while nabunot == name:
                num = random.randint(0, len(names)-1)
                nabunot = names[num]
                if nabunot != name:
                    await message.author.send(nabunot)
                    names.pop(num)
        else:
            await message.channel.send("Ubos na")

    if content == "!join":
        if name in names:
            await message.channel.send("Kasali ka na tabi")
        else:
            names.append(name)
            print(names)
client.run(TOKEN)