import discord
from discord.ext import commands
Bot = commands.Bot(command_prefix="!mm ")


@Bot.event
async def on_ready():
    print("Ben hazırım")

@Bot.command()
async def Animot(msg):
    await msg.send("Bu bir bottur, yapımcısı Graiden'dır.")
Bot.run("ODg3NzQ0NTIyNTkzOTE4OTc4.YUImgw.tuFeGkNCrA1M0sYeS8KUnfKtZUI")
