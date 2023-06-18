import random
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='$', intents=intents)

text1 = "Plastik bardak ve şişe gibi tek kullanımlık ürünleri kullanmaktan kaçının"
text2 = "Kağıt tüketimini azaltmak için e-okuyuculara geçiş yapın"
text3 = "Mümkün olduğunca az ambalajlı market ürünlerini ve atıştırmalıkları tercih edin, yiyecekleri ağırlıklarına göre (ambalajsız) satın alın ve yeniden kullanılabilir poşetlere geçmeye çalışın"
text4 = "Geri dönüştürmeye çalışın. Geri dönüştürülebilir ürünler için bir çöp kutusu ayırın ve dolduğunda geri dönüşüm istasyonuna taşıyın"
liste = [text1,text2,text3,text4]
@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def yardim(ctx):
    text_name = random.choice(liste)
    await ctx.send(text_name)


bot.run("TOKEN BURADA :D")
