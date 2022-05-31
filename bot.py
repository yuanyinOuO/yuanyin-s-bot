from msilib.schema import File
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=',' , intents = intents)

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(981018005817421904)
    await channel.send(f'{member} 他進來了!')

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(981018774478151720)
    await channel.send(f'{member} 他離開了!')

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)}(ms)')
    
@bot.command()
async def pic(ctx):
    pic = discord.File('C:\\Users\\ACER\\OneDrive\\文件\\GitHub\\yuanyin-s-bot\\pic\\miku.jpg')
    await ctx.send(file= pic)

bot.run("OTgxMDI3MzYzMDM2OTg3NDYy.Gcr6Vu.UHJ528RCCxmPPwNiyGGYgp4vMKSrYo3JVsofsM")



