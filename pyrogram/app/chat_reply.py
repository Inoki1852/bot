def cr(app, message):
    chat = message.chat
    reply = message.reply_to_message
    return chat, reply
