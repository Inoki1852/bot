from pyrogram import Client, filters

from chat_reply import cr


@Client.on_message(filters.me & filters.regex(r'^\.idm$'))
def idm(app, message):
    chat, reply = cr(app, message)
    if reply is None:
        app.send_message(chat.id, message, reply_to_message_id=message.id)
    else:
        app.send_message(chat.id, reply, reply_to_message_id=message.id)


@Client.on_message(filters.me & filters.regex(r'^\.user$'))
def copy(app, message):
    chat, reply = cr(app, message)
    if reply is None:
        user_id = message.from_user.id
    else:
        user_id = reply.from_user.id
    user = app.get_users(user_id)
    app.send_message(chat.id, user, reply_to_message_id=message.id)