from msilib.schema import File
import discord
from discord.ext import commands
import json
import random

intents = discord.Intents.default()
intents.members = True

with open('setting.json' , mode='r' , encoding='utf8') as jfile:
    jdate = json.load(jfile)

bot = commands.Bot(command_prefix=',' , intents = intents)

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(int(jdate['joinchannel']))
    await channel.send(f'恭迎{member}降臨 渡世靈顯四方 ')

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(int(jdate['removechannel']))
    await channel.send(f'{member} 默默的離開伺服器QQ')

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)}(ms)')
    
@bot.command()
async def hi(ctx):
    hi = discord.File(jdate['hibot'])
    await ctx.send(file= hi)

@bot.command()
async def give(ctx):
    random_pic = random.choice(jdate['give'])
    give = discord.File(random_pic)
    await ctx.send(file= give)

bot.run(jdate['TOKEN'])



