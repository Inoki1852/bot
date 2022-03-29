import os
import os.path
import re
import subprocess
import sys

from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler
from pyrogram.raw import functions

app = Client("my_account")

global process1
global process2
global if_check
if_check = False

try:
    os.chdir('../app')
except:
    os.chdir('../../app')

try:
    process1 = subprocess.Popen("python3 func/func.py")
    process2 = subprocess.Popen("python3 gp_bot/gp_bot.py")
except:
    process1 = subprocess.Popen("python3 func/func.py", shell=True)
    process2 = subprocess.Popen("python3 gp_bot/gp_bot.py", shell=True)


def cr(app, message):
    chat = message.chat
    reply = message.reply_to_message
    return chat, reply


@app.on_message(filters.regex(r'^\.bot$'))
def bot(app, message):
    chat, reply = cr(app, message)
    app.send_message(chat.id, "<i>Бот жив, здоров!</i>", reply_to_message_id=message.message_id)


@app.on_message(filters.regex(r'^\.rel$'))
def rel(app, message):
    chat, reply = cr(app, message)
    app.send_message(chat.id, "<i>Бот перезагрузится через 3 секунды!</i>", reply_to_message_id=message.message_id)
    process1.terminate()
    process2.terminate()
    os.execv(sys.executable, ['python3'] + sys.argv)


@app.on_message(filters.regex(r'^\.stop$'))
def stop(app, message):
    chat, reply = cr(app, message)
    app.send_audio(chat.id, "media/shutdown.mp3", file_name="Windows XP", reply_to_message_id=message.message_id)
    process1.terminate()
    process2.terminate()
    sys.exit()


@app.on_message(filters.me & filters.regex(r'^\.edit'))
def edit(app, message):
    chat, reply = cr(app, message)
    rgx = re.compile(r"\.edit(.+)")
    text = rgx.findall(message.text)
    rgx = re.compile(r"(\\S+)")
    text = rgx.findall(text[0])
    edit_handler = app.add_handler(MessageHandler(editing, filters.me & filters.text))
    if text == "n":
        app.remove_handler(*edit_handler)


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


@app.on_message(filters.me & filters.regex(r'^\.idm$'))
def idm(app, message):
    chat, reply = cr(app, message)
    app.send_message(chat.id, reply, reply_to_message_id=reply.message_id)


@app.on_message(filters.me & filters.regex(r'^\.idc$'))
def idc(app, message):
    chat, reply = cr(app, message)
    app.send_message(chat.id, reply, reply_to_message_id=reply.message_id)


@app.on_message(filters.me & ((filters.regex(r'^хорош$', 2) | filters.regex(r'^харош$', 2))))
def dude_is_good(app, message):
    chat, reply = cr(app, message)
    app.delete_messages(chat.id, message.message_id)
    if reply is None:
        app.send_animation(chat.id, "media/dude_is_good.mp4", unsave=True)
    else:
        app.send_animation(chat.id, "media/dude_is_good.mp4", reply_to_message_id=reply.message_id, unsave=True)


@app.on_message(filters.me & filters.regex(r'^\.copy'))
def copy(app, message):
    chat, reply = cr(app, message)
    global if_check
    rgx = re.compile("\.copy @(.+)")
    text = rgx.findall(message.text)
    rgx = re.compile("(\\S+)")
    text = rgx.findall(text[0])
    user_full = app.send(
        functions.users.GetFullUser(
            id=app.resolve_peer(text[0])
        )
    )
    user = app.get_users(text[0])
    photo = app.get_profile_photos(text[0], limit=1)
    photo_me = app.get_profile_photos("inoki1852", limit=1)
    if os.path.exists("handler/downloads/me.png"):
        pass
    else:
        app.download_media(photo_me[0], "me.png")
    app.download_media(photo[0], "photo.png")
    if if_check:
        photos = app.get_profile_photos("me")
        app.delete_profile_photos(photos[0].file_id)
    app.set_profile_photo(photo="handler/downloads/photo.png")
    user_first_name = user.first_name
    user_last_name = user.last_name
    user_about = user_full.full_user.about
    if user_full.full_user.about is None:
        user_about = ""
    elif user.first_name is None:
        user_first_name = ""
    elif user.last_name is None:
        user_last_name = ""
    app.update_profile(
        first_name=user_first_name,
        last_name=user_last_name,
        bio=user_about
    )
    if_check = True
    app.send_message(chat.id, "<i>Копирование завершено!</i>", reply_to_message_id=message.message_id)


@app.on_message(filters.me & filters.regex(r'^\.revert'))
def revert(app, message):
    chat, reply = cr(app, message)
    first_name = "Inoki"
    last_name = "🇺🇦"
    bio = "Русский военный корабль, иди нахуй."
    global if_check
    if if_check:
        photos = app.get_profile_photos("me")
        app.delete_profile_photos(photos[0].file_id)
    app.update_profile(
        first_name=first_name,
        last_name=last_name,
        bio=bio
    )
    if_check = False
    app.send_message(chat.id, "<i>Возврат к истокам!</i>", reply_to_message_id=message.message_id)


app.run()
