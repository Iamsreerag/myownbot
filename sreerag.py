from pyrogram import Client,filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import random
from userbase import present_in_userbase, add_to_userbase
sreerag=Client(
    "myownbot", 
    bot_token="5158569357:AAEvZRy0t9h6OotO2n6o-ksZV6CeNEp9Ujo", 
    api_id="7099124", 
    api_hash="a158cc12519db541370c91c5561f782f" 
) 

SREERAG = [
 "https://telegra.ph/file/77b6521c4ce497c66134a.jpg", 
 "https://telegra.ph/file/cea847dd1a0aa10d2bc30.jpg", 
 "https://telegra.ph/file/0725237f37f86d3481810.jpg", 
 "https://telegra.ph/file/7005ecc0ee9eb926a7195.jpg", 
 "https://telegra.ph/file/5a65ebe278430efc384ec.jpg", 
 "https://telegra.ph/file/96bd3f6e96e7b1ce5422b.jpg",
 "https://telegra.ph/file/daeaa96908b8053948cb2.jpg",
 "https://telegra.ph/file/70d2da745d72f8ecdf141.jpg"
]



@sreerag.on_message(filters.command("start")) 
async def start_message(bot, message):
    if not await present_in_userbase(message.from_user.id):
    	await add_to_userbase(message.from_user.id)
    	await message.reply_photo(
        photo=random.choice(SREERAG), 
        caption=f"""Hello {message.from_user.mention}ð¤ 
<b>à´®à´²à´¯à´¾à´³à´ à´¸à´¿à´¨à´¿à´®à´¾ à´à´¾à´¨àµ½ à´²à´¿à´¸àµà´±àµà´±àµ à´¬àµà´àµà´à´¿à´²àµà´àµà´àµ à´¸àµà´µà´¾à´à´¤à´,

â­Creator:</b> <a href='https://t.me/Mccontact_bot'>ð¤This Person</a>

â­Channel:</b> <a href='https://t.me/joinchat/slPWoPDfoJc3NTVl'>Click Here</a>

â­How To Download Movies? :</b> <a href='https://t.me/malyalamcinemass/23'>Click Me</a>

            ð¢ðð¿ ððµð®ð»ð»ð²ð¹ ðð»ð± ðð¿ð¼ðð½ððð
""", 
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("[ðð]New Movies", url="https://t.me/joinchat/slPWoPDfoJc3NTVl"), 
            InlineKeyboardButton("[ðð]GROUP", url="https://t.me/mc_cinema")
            ],[
            InlineKeyboardButton("[ðð]ððð«ð¢ðð¬ ðð¨ð«ð¥ð", url="https://t.me/mc_serie"), 
            InlineKeyboardButton("[ðð]ððð«ð¢ðð¬ ðð¡ðð§ð§ðð¥", url="https://t.me/mc_series_c")
            ],[
            InlineKeyboardButton("ð ð¼ðð¶ð² ðð¼ð¹ð¹ð²ð°ðð¶ð¼ð»", url="https://t.me/minnal_murali77"), 
            InlineKeyboardButton("[ðð]ð¡ð²ðð³ð¹ð¶ð ð®", url="https://t.me/netflixorgi")
            ],[
            InlineKeyboardButton("[ðð]ð¡ð²ð ð¢ðð ð ð¼ðð¶ð²ð", url="https://t.me/+3bakJjQahSw5MDdl"), 
            InlineKeyboardButton("[ðð]ð ð¢ð©ððð¦ ð¨ð£ððð§ðð¦", url="https://t.me/malayalam2")
            ],[
            InlineKeyboardButton("ðá´ÊÉªá´á´ Êá´Êá´ & sÊá´Êá´ á´Êá´É´É´á´Êð", url="http://t.me/share/url?url=Hai%20Bro%2FSis%20%E2%9D%A4%EF%B8%8F%2C%20Today%20I%20Just%20Found%20Out%20A%20Movies%20And%20Series%20Group%20Which%20Uploads%20Requested%20Movies%20and%20Series%20In%20Second%27s%F0%9F%A5%B0.J%CF%83%CE%B9%D0%B8%20N%CF%83%CF%89%20%20%3A%20%40mc_cinema%20%F0%9F%91%8C%F0%9F%94%A5%20and%20Series%20In%20Second%27s%F0%9F%A5%B0.J%CF%83%CE%B9%D0%B8%20N%CF%83%CF%89%20%20%3A%20%40malayayalies%20%F0%9F%91%8C%F0%9F%94%A5") 
            ]]
            ) 
        ) 

sreerag.run() 
