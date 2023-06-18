import discord
import random
import os
import requests
from discord.ext import commands
""" 
w - verileri bir dosyaya kaydeder, ancak daha önce orada depolanan tüm verileri silmeden önce değil;
r - bir dosyayi salt okunur modda açar;
a - dosyadan hiçbir şey çikarmadan dosyanin sonuna veri kaydeder;
rb - okumak için metin olmayan bir dosya açar;
wb - kayit için metin olmayan bir dosya açar.

"""
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="$", intents=intents)
intents.members = True

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')
    
@bot.event
async def on_member_join(member):
    guild = member.guild
    if guild.system_channel is not None:
        to_send = f'Welcome {member.mention} to {guild.name}!'
        await guild.system_channel.send(to_send)

@bot.command()
async def merhaba(ctx):
    await ctx.send(f'Bro {bot.user}! ben seninim!')
    
@bot.command()
async def mem(ctx):
    with open("images\TR1a7e888c7a1d59220c4a7e866c083ae8.jpg","rb")as f:
            picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def memr(ctx):
    img_name = random.choice(os.listdir("images"))
    with open(f'images/{img_name}','rb')as f:
        picture = discord.File(f)
    await ctx.send(file = picture)
    
def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)
    


    
    

bot.run("TOKEN BURADA :D")
    
