import discord
import os
import youtube_dl
client = discord.Client()
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$play'):
        url = message.content.split()[1]
        channel = message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio(url))
        vc.source = discord.PCMVolumeTransformer(vc.source)
        vc.source.volume = 0.07
    if message.content.startswith('$stop'):
        await vc.disconnect()  

client.run(os.getenv("TOKEN"))
