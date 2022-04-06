from pyrogram import Client
from pyrogram import filters
import re

app = Client("my_bot", bot_token="5005315425:AAGc9fI1PumWim7YehHlh5xaMjJ2W2g5DN4")

users = ["inoki1852", "ClayzDart", "Nne_li"]

@app.on_message(filters.private & ~(
        filters.user("inoki1852") | filters.user("ClayzDart") | filters.user("MrBuxlo") | filters.user("Nne_li")))
def suggest(client, message):
    media = message.media
    if media is not None:
        for value in users:
            message.copy(value, caption="{}  <code>by {}</code>".format(message.text, message.from_user.username))
    else:
        user_message = "{}  <code>by {}</code>".format(message.text, message.from_user.username)
        for value in users:
            app.send_message(value, user_message)


@app.on_message(filters.private & filters.regex(r'^[^\.].+') & (
        filters.user("inoki1852") | filters.user("ClayzDart") | filters.user("MrBuxlo") | filters.user("Nne_li")))
def media(client, message):
    reply = message.reply_to_message
    if reply is None:
        pass
    else:
        media = reply.media
        if media is not None:
            reply.copy("gifs_and_pics",
                       caption="{}  <code>by {}</code>".format(message.text, message.from_user.username))
            message.reply("Успешно скопировано!")


@app.on_message(filters.private & filters.regex(r'^\.') & (
        filters.user("inoki1852") | filters.user("ClayzDart") | filters.user("MrBuxlo") | filters.user("Nne_li")))
def answer(client, message):
    reply = message.reply_to_message
    if reply is not None:
        media = reply.media
        if media is None:
            user_name = re.findall(r'by (\w+)', reply.text)
        else:
            user_name = re.findall(r'by (\w+)', reply.caption)
        text_answer = re.findall(r'\.(.*)', message.text)
        try:
            app.send_message(user_name[0], text_answer[0])
        except:
            pass

app.run()
