import discord
from discord.ext import commands
intentsa = discord.Intents(message=True, guilds=True, reactions=True, members=True, presences=True)
Bot = commands.Bot(command_prefix="!mm ", intentsa=intentsa)

Token = open("token.txt", "r").read()


@Bot.event
async def on_ready():
    print("Ben hazırım")


@Bot.command()
async def animot(msg):
    await msg.send("Ben sayın Animot, daha yeni yazılmaya başlanmış bir botum pek özelliğim yok.")


@Bot.event
async def on_member_join(member):
    print(f"{member} aramıza katıldı, kurallara uy lütfen!!")


@Bot.command()
async def bö(msa):
    await msa.send("https://i.pinimg.com/736x/1e/3e/62/1e3e62961cde08c1ee439ea017715583.jpg")


@Bot.event
async def on_member_remove(member):
    print(f"{member} aramızdan ayrıldı, civcivin karizmasına dayanamadı!!")


Bot.run("Token")
