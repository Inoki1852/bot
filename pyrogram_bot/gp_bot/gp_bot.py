from pyrogram import Client
from pyrogram import filters
import re

api_id = 1474699
api_hash = "5427b333bbe9380419f6fdf2ccdd37a2"
bot_token = "5005315425:AAGc9fI1PumWim7YehHlh5xaMjJ2W2g5DN4"

app = Client("my_bot", bot_token="5005315425:AAGc9fI1PumWim7YehHlh5xaMjJ2W2g5DN4")

users = ["inoki1852", "ClayzDart", "Nne_li"]


@app.on_message(
    (filters.text & filters.regex(r'^[^#].+') | filters.media) & filters.private & ~filters.group)
def suggest(client, message):
    media = message.media
    text = message.text
    if text is None:
        text = ""
    if media is not None:
        for value in users:
            try:
                message.copy(value, caption="{} by <code>{}</code>".format(text, message.from_user.username))
            except:
                pass
    else:
        text = re.findall(r'^\.?(.+)', message.text)
        user_message = "{}:\n— {}".format(message.from_user.username, text[0])
        for value in users:
            app.send_message(value, user_message)
    # message.delete()
    print("delete")


@app.on_message(filters.private & ~filters.group & filters.reply & filters.text & filters.regex(r'^#.+') & (
        filters.user("inoki1852") | filters.user("ClayzDart") | filters.user("MrBuxlo") | filters.user("Nne_li")))
def media(client, message):
    reply = message.reply_to_message
    media = reply.media
    if media is not None:
        reply.copy("gifs_and_pics",
                   caption="{}  <code>by {}</code>".format(message.text, message.from_user.username))
        message.reply("Успешно скопировано!")


@app.on_message(filters.private & ~filters.group & filters.reply & filters.regex(r'^\.') & (
        filters.user("inoki1852") | filters.user("ClayzDart") | filters.user("Nne_li")))
def answer(client, message):
    reply = message.reply_to_message
    media = reply.media
    if media is None:
        user_name = re.findall(r'(.+):', reply.text)
    else:
        user_name = re.findall(r'by (.+)', reply.caption)
    text_answer = re.findall(r'\.(.*)', message.text)
    print(text_answer[0])
    if text_answer[0] == "":
        text_answer[0] = ""
    try:
        app.send_message(user_name[0], "<i>{}</i>:\n— {}".format(text_answer[0], message.from_user.username))
    except:
        pass
    message.delete()


app.run()
