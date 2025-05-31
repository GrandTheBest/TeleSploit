from vendor.misc import *
from telethon import functions

async def sessions():
    result = await client(functions.account.GetAuthorizationsRequest())
    for i, auth in enumerate(result.authorizations, start=1):
        print(f"\n--- Session #{i} ---")
        for attr in auth.__dict__:
            value = getattr(auth, attr)
            print(f"{gr}[{cy}{attr}{gr}]{wh} {value}")
    print("")