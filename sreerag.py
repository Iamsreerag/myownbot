from pyrogram import Client,filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import random
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
]



@sreerag.on_message(filters.command("start")) 
async def start_message(bot, message):
    await message.reply_photo(
        photo=random.choice(SREERAG), 
        caption=f"""Hello {message.from_user.mention}🤠
<b>മലയാളം സിനിമാ ചാനൽ ലിസ്റ്റ് ബോട്ടിലേക്ക് സ്വാഗതം,

⭕Creator:</b> <a href='https://t.me/Mccontact_bot'>👤This Person</a>

⭕Channel:</b> <a href='https://t.me/joinchat/slPWoPDfoJc3NTVl'>Click Here</a>

⭕How To Download Movies? :</b> <a href='https://t.me/minnal_murali77/993'>Click Me</a>

            𝗢𝘂𝗿 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 𝗔𝗻𝗱 𝗚𝗿𝗼𝘂𝗽𝘀👇👇
""", 
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("[🅜🅒]New Movies", url="https://t.me/joinchat/slPWoPDfoJc3NTVl"), 
            InlineKeyboardButton("[🅜🅒]GROUP", url="https://t.me/malayayalies")
            ],[
            InlineKeyboardButton("[🅜🅒]𝐒𝐞𝐫𝐢𝐞𝐬 𝐖𝐨𝐫𝐥𝐝", url="https://t.me/mc_serie"), 
            InlineKeyboardButton("𝗠𝗢𝗩𝗜𝗘 𝗖𝗢𝗟𝗟𝗘𝗖𝗧𝗜𝗢𝗡", url="https://t.me/minnal_murali77")
            ],[
            InlineKeyboardButton("[🅜🅒]𝗡𝗲𝘁𝗳𝗹𝗶𝘅", url="https://t.me/netflix_originals_pdisk"), 
            InlineKeyboardButton("[🅜🅒]𝗡𝗲𝘁𝗳𝗹𝗶𝘅 𝟮", url="https://t.me/netflixorgi")
            ],[
            InlineKeyboardButton("[🅜🅒]𝗡𝗲𝘄 𝗢𝘁𝘁 𝗠𝗼𝘃𝗶𝗲𝘀", url="https://t.me/+3bakJjQahSw5MDdl"), 
            InlineKeyboardButton("[🅜🅒]𝗠𝗢𝗩𝗜𝗘𝗦 𝗨𝗣𝗗𝗔𝗧𝗘𝗦", url="https://t.me/malayalam2")
            ]]
            ) 
        ) 

sreerag.run() 

