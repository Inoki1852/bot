from pyrogram import Client

plugins = dict(root="plugins")

app = Client("my_account", 1474699, "5427b333bbe9380419f6fdf2ccdd37a2", plugins=plugins)

app.run()