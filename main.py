import os
from typing import final 
import discord
from dotenv import load_dotenv
import asyncio
load_dotenv()
token = os.environ["TOKEN"]
print(token)
client = discord.Client(intents=discord.Intents.all())
import requests
import json
import random 



sad_words = ["sad","depressed","unhappy","angry","miserable","depressing"]
starter_encouragements = ["Cheer UP !","Hang in There ","You are a great person"]


@client.event
async def on_ready():
    print("we have logged in as {0.user}".format(client))

# @client.event
# async def on_message(message):
#     print("Enteted here ", message)

#     print("Enteted here ", message.content)
#     if message.author == client.user:
#         return 
#     if message.content.startswith("&hello"):
#         await message.channel.send("Hello!")

# @client.event
# async def on_message(message):
#     if message.content.startswith('$greet'):
#         channel = message.channel
#         await channel.send('Say hello!')

#         def check(m):
#             return m.content == 'hello' and m.channel == channel

#         msg = await client.wait_for('message', check=check)
#         await channel.send(f'Hello {msg.author}!')



def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q']
    author = json_data[0]['a']
    final_quote = quote + " -"+author
    return final_quote


@client.event
async def on_message(message):
    if message.content.startswith('$hello'):
        channel = message.channel
        await channel.send('Send me that 👍 reaction, mate')

        def check(reaction, user):
            return user == message.author and str(reaction.emoji) == '👍'

        try:
            reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
        except asyncio.TimeoutError:
            await channel.send('👎')
        else:
            await channel.send('👍')
    if message.content.startswith('$inspire'):
        channel = message.channel
        value = get_quote()
        await channel.send(value)
    msg = message.content
    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(starter_encouragements))




client.run(token)
