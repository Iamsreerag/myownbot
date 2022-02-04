from pyrogram import Client,filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

sreerag=Client(
    "myownbot", 
    bot_token="5237284811:AAEgN7gPmfPFR4vNsPhAWT6jpZ7DX4-kJ_I", 
    api_id="7099124", 
    api_hash="a158cc12519db541370c91c5561f782f" 
) 

@sreerag.on_message(filters.command("start")) 
async def start_message(bot, message):
    await message.reply_text(
        text="hello sugam annoo", 
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("button name", url="https://t.me/joinchat/slPWoPDfoJc3NTVl") 
            InlineKeyboardButton("button2 name", url="https://t.me/joinchat/slPWoPDfoJc3NTVl")
            ]]
            ) 
        ) 

sreerag.run() 

