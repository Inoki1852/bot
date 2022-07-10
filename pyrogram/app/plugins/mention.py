from pyrogram import Client, filters

import re
from chat_reply import cr


@Client.on_message(filters.me & filters.regex(r'^\.mt'))
def mention(app, message):
    chat, reply = cr(app, message)
    text = re.findall(r'\.mt @?(\w+) ((\w+|\W+ ?)+)', message.text)
    user = app.get_users(text[0][0])
    app.edit_message_text(chat.id, message.id, "[" + text[0][1] + "](tg://user?id=" + str(user.id) + ")")
