from pyrogram import Client
from pyrogram import filters
import re

app = Client("my_bot", bot_token="5005315425:AAGc9fI1PumWim7YehHlh5xaMjJ2W2g5DN4")


@app.on_message(filters.private & (
        filters.user("inoki1852") | filters.user("ClayzDart") | filters.user("MrBuxlo") | filters.user("Nne_li")))
def media(client, message):
    chat = message.chat
    reply = message.reply_to_message
    if reply is None:
        pass
    else:
        if reply.media != "":
            reply.copy("gifs_and_pics",
                       caption="{}  <code>by {}</code>".format(message.text, message.from_user.username))
            message.reply("Успешно скопировано!")


app.run()
