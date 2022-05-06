from pyrogram import Client, filters
import os
import sys
import subprocess
from chat_reply import cr

try:
    os.chdir('../app')
except:
    os.chdir('../..')

try:
    process1 = subprocess.Popen("python3 func/func.py")
    process2 = subprocess.Popen("python3 gp_bot/gp_bot.py")
except:
    process1 = subprocess.Popen("python3 func/func.py", shell=True)
    process2 = subprocess.Popen("python3 gp_bot/gp_bot.py", shell=True)


@Client.on_message(filters.regex(r'^\.bot$'))
def bot(app, message):
    chat, reply = cr(app, message)
    app.send_message(chat.id, "<i>Ah, ha, ha, ha, stayin' alive, stayin' alive!</i>",
                     reply_to_message_id=message.message_id)


@Client.on_message(filters.me & filters.regex(r'^\.rel$'))
def rel(app, message):
    chat, reply = cr(app, message)
    app.send_audio(chat.id, "media/shutdown.mp3", file_name="Windows XP", reply_to_message_id=message.message_id)
    process1.terminate()
    process2.terminate()
    os.execv(sys.executable, ['python3'] + sys.argv)


@Client.on_message(filters.me & filters.regex(r'^\.stop$'))
def stop(app, message):
    chat, reply = cr(app, message)
    app.send_audio(chat.id, "media/shutdown.mp3", file_name="Windows XP", reply_to_message_id=message.message_id)
    process1.terminate()
    process2.terminate()
    sys.exit()
