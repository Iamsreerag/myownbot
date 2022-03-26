from pyrogram import Client,filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import random
import pymongo
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
    if not await present_in_userbase(update.from_user.id):
    	await add_to_userbase(update.from_user.id)
    	await message.reply_photo(
        photo=random.choice(SREERAG), 
        caption=f"""Hello {message.from_user.mention}🤠
<b>മലയാളം സിനിമാ ചാനൽ ലിസ്റ്റ് ബോട്ടിലേക്ക് സ്വാഗതം,

⭕Creator:</b> <a href='https://t.me/Mccontact_bot'>👤This Person</a>

⭕Channel:</b> <a href='https://t.me/joinchat/slPWoPDfoJc3NTVl'>Click Here</a>

⭕How To Download Movies? :</b> <a href='https://t.me/malyalamcinemass/23'>Click Me</a>

            𝗢𝘂𝗿 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 𝗔𝗻𝗱 𝗚𝗿𝗼𝘂𝗽𝘀👇👇
""", 
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("[🅜🅒]New Movies", url="https://t.me/joinchat/slPWoPDfoJc3NTVl"), 
            InlineKeyboardButton("[🅜🅒]GROUP", url="https://t.me/mc_cinema")
            ],[
            InlineKeyboardButton("[🅜🅒]𝐒𝐞𝐫𝐢𝐞𝐬 𝐖𝐨𝐫𝐥𝐝", url="https://t.me/mc_serie"), 
            InlineKeyboardButton("[🅜🅒]𝐒𝐞𝐫𝐢𝐞𝐬 𝐂𝐡𝐚𝐧𝐧𝐞𝐥", url="https://t.me/mc_series_c")
            ],[
            InlineKeyboardButton("𝗠𝗼𝘃𝗶𝗲 𝗖𝗼𝗹𝗹𝗲𝗰𝘁𝗶𝗼𝗻", url="https://t.me/minnal_murali77"), 
            InlineKeyboardButton("[🅜🅒]𝗡𝗲𝘁𝗳𝗹𝗶𝘅 𝟮", url="https://t.me/netflixorgi")
            ],[
            InlineKeyboardButton("[🅜🅒]𝗡𝗲𝘄 𝗢𝘁𝘁 𝗠𝗼𝘃𝗶𝗲𝘀", url="https://t.me/+3bakJjQahSw5MDdl"), 
            InlineKeyboardButton("[🅜🅒]𝗠𝗢𝗩𝗜𝗘𝗦 𝗨𝗣𝗗𝗔𝗧𝗘𝗦", url="https://t.me/malayalam2")
            ],[
            InlineKeyboardButton("🎖ᴄʟɪᴄᴋ ʜᴇʀᴇ & sʜᴀʀᴇ ᴄʜᴀɴɴᴇʟ🎖", url="http://t.me/share/url?url=Hai%20Bro%2FSis%20%E2%9D%A4%EF%B8%8F%2C%20Today%20I%20Just%20Found%20Out%20A%20Movies%20And%20Series%20Group%20Which%20Uploads%20Requested%20Movies%20and%20Series%20In%20Second%27s%F0%9F%A5%B0.J%CF%83%CE%B9%D0%B8%20N%CF%83%CF%89%20%20%3A%20%40mc_cinema%20%F0%9F%91%8C%F0%9F%94%A5%20and%20Series%20In%20Second%27s%F0%9F%A5%B0.J%CF%83%CE%B9%D0%B8%20N%CF%83%CF%89%20%20%3A%20%40malayayalies%20%F0%9F%91%8C%F0%9F%94%A5") 
            ]]
            ) 
        ) 

sreerag.run() 
