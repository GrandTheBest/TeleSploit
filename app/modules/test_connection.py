from vendor.misc import *

async def test_connection():
    me = await client.get_me()
    print(me.stringify())