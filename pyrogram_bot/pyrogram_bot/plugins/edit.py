from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler

import re
from chat_reply import cr

global text


@Client.on_message(filters.me & filters.regex(r'^\.edit'))
def edit(app, message):
    chat, reply = cr(app, message)
    global text
    text = re.findall(r'\.edit(.+)', message.text)
    text = re.findall(r'(\S+)', text[0])
    print(text)
    edit_handler = app.add_handler(MessageHandler(editing, filters.me & filters.text))
    if text == "n":
        app.remove_handler(*edit_handler)


def editing(app, message):
    chat, reply = cr(app, message)
    global text
    len_text = len(text)
    if len_text == 1:
        app.edit_message_text(chat.id, message.message_id, "<{0}>{1}</{2}>".format(text[0], message.text, text[0]))
    elif len_text == 2:
        app.edit_message_text(chat.id, message.message_id,
                              "<{0}><{1}>{2}</{3}></{4}>".format(text[0], text[1], message.text, text[1], text[0]))
    elif len_text == 3:
        app.edit_message_text(chat.id, message.message_id,
                              "<{0}><{1}><{2}>{3}</{4}></{5}></{6}>".format(text[0], text[1], text[2], message.text,
                                                                            text[2], text[1], text[0]))
