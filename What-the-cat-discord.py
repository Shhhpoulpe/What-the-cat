import discord
from discord.ext import tasks
from discord.ext import commands
from discord_param import discord_token
from discord.ext import commands

client = discord.Client()

@tasks.loop(seconds = 1)
async def myLoop():
    # Attends que le bot soit connecté
    await client.wait_until_ready()
    channel = client.get_channel(741298761569009826)
    # Envoie un message si la dernière vidéo est différente de la dernière vidéo envoyée
    message = (await channel.history(limit=1).flatten())[0]
    print(message.attachments)
    if message.attachments:
        await channel.send(f"<@{message.author.id}> nice cat")
        

myLoop.start()
client.run(discord_token)