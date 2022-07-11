import os
import re

from pyrogram import Client, filters
from pyrogram.raw import functions

from chat_reply import cr

global if_check
if_check = False


@Client.on_message(filters.me & filters.regex(r'^\.copy'))
def copy(app, message):
    chat, reply = cr(app, message)
    global if_check
    if reply is None:
        text_id = re.findall(r'\.copy @?(.+)', message.text)
        print(text_id)
        user_full = app.send(
            functions.users.GetFullUser(
                id=app.resolve_peer(text_id[0])
            )
        )
        user = app.get_users(text_id[0])
        photo = app.get_profile_photos(text_id[0], limit=1)
        photo_me = app.get_profile_photos("inoki1852", limit=1)
        if os.path.exists("downloads/me.png"):
            pass
        else:
            app.download_media(photo_me[0], "me.png")
        app.download_media(photo[0], "photo.png")
        if if_check:
            photos = app.get_profile_photos("me")
            app.delete_profile_photos(photos[0].file_id)
        app.set_profile_photo(photo="downloads/photo.png")
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
    else:
        user_id = reply.from_user.id
        user_full = app.send(
            functions.users.GetFullUser(
                id=app.resolve_peer(user_id)
            )
        )
        user = app.get_users(user_id)
        photo = app.get_profile_photos(user_id, limit=1)
        photo_me = app.get_profile_photos("inoki1852", limit=1)
        if os.path.exists("downloads/me.png"):
            pass
        else:
            app.download_media(photo_me[0], "me.png")
        app.download_media(photo[0], "photo.png")
        if if_check:
            photos = app.get_profile_photos("me")
            app.delete_profile_photos(photos[0].file_id)
        app.set_profile_photo(photo="downloads/photo.png")
        user_first_name = user.first_name
        user_last_name = user.last_name
        user_about = user_full.full_user.about
        if user_full.full_user.about is None:
            user_about = ""
        if user.first_name is None:
            user_first_name = ""
        if user.last_name is None:
            user_last_name = ""
        app.update_profile(
            first_name=user_first_name,
            last_name=user_last_name,
            bio=user_about
        )
    if_check = True
    app.send_message(chat.id, "<i>Копирование завершено!</i>", reply_to_message_id=message.id)


@Client.on_message(filters.me & filters.regex(r'^\. ?revert$'))
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
    app.send_message(chat.id, "<i>Возврат к истокам!</i>", reply_to_message_id=message.id)
