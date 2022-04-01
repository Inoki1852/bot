from pyrogram import Client, filters

import re
from chat_reply import cr


@Client.on_message(filters.me & filters.regex(r'^\.mt'))
def mention(app, message):
    chat, reply = cr(app, message)
    text = re.findall(r'@?(\w+) (\w+)', message.text)
    user = app.get_users(text[0][0])
    print(text[0][1])
    print(user.id)
    print(user)
    app.edit_message_text(chat.id, message.message_id, "[" + text[0][1] + "](tg://user?id=" + str(user.id) + ")")
