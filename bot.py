import os
import random
import discord
from names import names
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    content = message.content 

    if content == '!bunot':
        num = random.randint(0, len(names))
        print(num)
        nabunot = names[num]
        await message.author.send(nabunot)
        print(message.author)
        names.pop(num)
    
        print(names)

client.run(TOKEN)