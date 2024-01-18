#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>\n○  ᴄʀᴇᴀᴛᴏʀ : <a href='https://t.me/Sensei_Rimuru'>Noir </a>\n○  ʟᴀɴɢᴜᴀɢᴇ : <code>Python</code>\n○  Main Channel : <a href=https://t.me/Anime_Sensei_Network>Anime Sensei</a>\n○  Support Group : <a href=https://t.me/Ani_Bots_Update>Anime Chats</a>\n</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒ᴄʟᴏsᴇ", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
