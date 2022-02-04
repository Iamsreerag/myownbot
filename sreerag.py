from pyrogram import Client,filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import random
sreerag=Client(
    "myownbot", 
    bot_token="5237284811:AAEgN7gPmfPFR4vNsPhAWT6jpZ7DX4-kJ_I", 
    api_id="7099124", 
    api_hash="a158cc12519db541370c91c5561f782f" 
) 

SREERAG = [
 "https://telegra.ph/file/77b6521c4ce497c66134a.jpg", 
 "https://telegra.ph/file/cea847dd1a0aa10d2bc30.jpg", 
 "https://telegra.ph/file/0725237f37f86d3481810.jpg", 
 "https://telegra.ph/file/7005ecc0ee9eb926a7195.jpg", 
 "https://telegra.ph/file/5a65ebe278430efc384ec.jpg"
]



@sreerag.on_message(filters.command("start")) 
async def start_message(bot, message):
    await message.reply_photo(
        photo=random.choice(SREERAG), 
        caption="hello sugam annoo", 
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("[🔰🅜🅒]New Movies🔰", url="https://t.me/joinchat/slPWoPDfoJc3NTVl"), 
            InlineKeyboardButton("[⭕🅜🅒]GROUP⭕", url="https://t.me/malayayalies")
            ],[
            InlineKeyboardButton("⚜️[🅜🅒]𝐒𝐞𝐫𝐢𝐞𝐬 𝐖𝐨𝐫𝐥𝐝⚜️", url="https://t.me/mc_serie"), 
            InlineKeyboardButton("[✳️🅜🅒]Movie Collection✳️", url="https://t.me/minnal_murali77")
            ],[
            InlineKeyboardButton("[🅜🅒]𝗡𝗲𝘁𝗳𝗹𝗶𝘅", url="https://t.me/netflix_originals_pdisk"), 
            InlineKeyboardButton("[🅜🅒]𝗡𝗲𝘁𝗳𝗹𝗶𝘅 𝟮", url="https://t.me/netflixorgi")
            ],[
            InlineKeyboardButton("[🅜🅒]𝗡𝗲𝘄 𝗢𝘁𝘁 𝗠𝗼𝘃𝗶𝗲𝘀", url="https://t.me/+3bakJjQahSw5MDdl")
            ]]
            ) 
        ) 

sreerag.run() 

