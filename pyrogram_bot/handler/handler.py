import os
import re
import subprocess
import sys

from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler

app = Client("my_account")

try:
    os.chdir('../pyrogram_bot')
except:
    os.chdir('../../pyrogram_bot')

global process1
global process2

try:
    process1 = subprocess.Popen("python func/func.py")
    process2 = subprocess.Popen("python g_p_bot/g_p_bot.py")
except:
    process1 = subprocess.Popen("python func/func.py", shell=True)
    process2 = subprocess.Popen("python g_p_bot/g_p_bot.py", shell=True)


def cr(app, message):
    chat = message.chat
    reply = message.reply_to_message
    return chat, reply


@app.on_message(filters.regex('^\.rel$'))
def rel(app, message):
    chat, reply = cr(app, message)
    app.send_message(chat.id, "<i>Бот перезагрузится через 3 секунды!</i>", reply_to_message_id=message.message_id)
    process1.terminate()
    process2.terminate()
    os.execv(sys.executable, ['python'] + sys.argv)


@app.on_message(filters.regex('^\.stop$'))
def stop(app, message):
    chat, reply = cr(app, message)
    app.send_message(chat.id, "<i>Останавливаем работу бота...</i>", reply_to_message_id=message.message_id)
    process1.terminate()
    process2.terminate()
    sys.exit()


@app.on_message(filters.me & filters.regex('^\.edit'))
def edit(app, message):
    chat, reply = cr(app, message)
    global text
    rgx = re.compile("\.edit(.+)")
    text = rgx.findall(message.text)
    rgx = re.compile("(\\S+)")
    text = rgx.findall(text[0])
    edit_handl = app.add_handler(MessageHandler(editing, filters.me & filters.text))
    if text == "n":
        app.remove_handler(*edit_handl)


def editing(app, message):
    chat, reply = cr(app, message)
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


@app.on_message((filters.me | filters.user("MrBuxlo") | filters.user("@ClayzDart")) & filters.regex('^\.copy'))
def copy(app, message):
    chat, reply = cr(app, message)
    rgx = re.compile("\.copy(.+)")
    text = rgx.findall(message.text)
    rgx = re.compile("(\\S+)")
    text = rgx.findall(text[0])
    text = " ".join(text)
    app.copy_message("gifs_and_pics", chat.id, reply.message_id, caption=text)


@app.on_message(filters.me & filters.regex('^\.idm$'))
def idm(app, message):
    chat, reply = cr(app, message)
    app.send_message(chat.id, reply, reply_to_message_id=reply.message_id)


@app.on_message(filters.me & ((filters.regex('^хорош$', 2) | filters.regex('^харош$', 2))))
def dude_is_good(app, message):
    chat, reply = cr(app, message)
    app.delete_messages(chat.id, message.message_id)
    if reply is None:
        app.send_animation(chat.id, "media/dude_is_good.mp4", unsave=True)
    else:
        app.send_animation(chat.id, "media/dude_is_good.mp4", reply_to_message_id=reply.message_id, unsave=True)


@app.on_message(filters.regex('^\.bot$'))
def bot(app, message):
    chat, reply = cr(app, message)
    app.send_message(chat.id, "<i>Бот жив, здоров!</i>", reply_to_message_id=message.message_id)


app.run()
