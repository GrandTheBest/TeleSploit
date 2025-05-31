from vendor.misc import *
from telethon import functions

async def test_connection():
    me = await client.get_me()
    print(me.stringify())