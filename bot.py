import discord
import secrets
import math
import re

client = discord.Client()

bidentifier = re.compile(r"\b(bee)\b", re.I)
file = open("beemovie.txt", "r")
beemovie = file.read()


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if bidentifier.match(message.content.lower()):
        rem = len(beemovie) % 2000
        reps = len(beemovie) / 2000
        reps = math.floor(reps)

        chunk = beemovie[reps*2000:]

        for i in range(reps):
            start = i*2000
            end = i + 1
            end = end * 2000
            end = end - 1
            await message.channel.send(beemovie[start:end])

        await message.channel.send(chunk)

client.run(secrets.get_key())
