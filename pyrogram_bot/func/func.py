# from pyrogram import Client
# from pyrogram.raw import base, functions
# import datetime
# import time
# import asyncio
# from pyrogram.errors import RPCError

# app = Client("my_account")

# async def cur_time(app):
#  async with app:
#    while True:
#        fullUser = await app.send(functions.users.GetFullUser(id = await app.resolve_peer("inoki1852")))
#        now = time.strftime("My time is: %H:%M", time.localtime())
#       if fullUser.full_user.about == now:
#            await asyncio.sleep(5)
#        else:
#            await app.update_profile(bio = now)

# app.run(cur_time(app))
