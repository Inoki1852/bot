from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler

import re
from chat_reply import cr


@Client.on_message(filters.me & filters.regex(r'^\.m'))
def mention(app, message):
    chat, reply = cr(app, message)


