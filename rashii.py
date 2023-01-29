from pyrogram import Client,filters
import requests
from bs4 import BeautifulSoup
def rashi(name):
    r = requests.get(f"https://www.hamropatro.com/rashifal/daily/{name}")
    r_content = r.content
    soup = BeautifulSoup(r_content,"html.parser")
    rashi_content = soup.find_all("div",{"class":"desc"})
    rashifal= (rashi_content[0].find_all("p")[0].text.replace("\n",""))
    return rashifal
bot = Client(
    "rashifalBot",
    api_id = APIID,
    api_hash = "APIHASH",
    bot_token = "BOTTOKEN",
    
)

@bot.on_message(filters.command('start'))
def start_message(bot, message):
     message.reply_text("I am a rashifal robot.\nEvery day, I can be your rashifal provider.\n/usage for the available options.")

@bot.on_message(filters.command('help'))
def help_message(bot, message):
    message.reply_text("Kindly DM @hylov")

@bot.on_message(filters.command('usage'))
def helpmessage(bot,message):
    message.reply_text("/Mesh for मेष\n/Brish for वृष\n/Mithun for मिथुन\n/Karkat for कर्कट\n/Singha for सिंह\n/Kanya for कन्या\n/Tula for तुला\n/Brischik for वृश्चिक\n/Dhanu for धनु\n/Makar for मकर\n/Kumbha for कुम्भ\n/Meen for मीन")
@bot.on_message(filters.command('Mesh'))
def helpmessage(bot,message):
    message.reply_text(rashi('Mesh'))
@bot.on_message(filters.command('Brish'))
def helpmessage(bot,message):
    message.reply_text(rashi('Brish'))
@bot.on_message(filters.command('Mithun'))
def helpmessage(bot,message):
    message.reply_text(rashi('Mithun'))

@bot.on_message(filters.command('Karkat'))
def helpmessage(bot,message):
    message.reply_text(rashi('Karkat'))
    
@bot.on_message(filters.command('Singha'))
def helpmessage(bot,message):
    message.reply_text(rashi('Singha'))
    
@bot.on_message(filters.command('Kanya'))
def helpmessage(bot,message):
    message.reply_text(rashi('Kanya'))
    
@bot.on_message(filters.command('Tula'))
def helpmessage(bot,message):
    message.reply_text(rashi('Tula'))
    
@bot.on_message(filters.command('Brischik'))
def helpmessage(bot,message):
    message.reply_text(rashi('Brischik'))

@bot.on_message(filters.command('Dhanu'))
def helpmessage(bot,message):
    message.reply_text(rashi('Dhanu'))
    
@bot.on_message(filters.command('Makar'))
def helpmessage(bot,message):
    message.reply_text(rashi('Makar'))
    
@bot.on_message(filters.command('Kumbha'))
def helpmessage(bot,message):
    message.reply_text(rashi('Kumbha'))
    
@bot.on_message(filters.command('Meen'))
def helpmessage(bot,message):
    message.reply_text(rashi('Meen'))  
print("i'm alive")
bot.run()
