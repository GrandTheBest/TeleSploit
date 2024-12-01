from vendor.misc import *

async def about_me():
    entity = await client.get_me()

    a = "@"

    Yes = lang['yes']
    No = lang['no']
    Empty = lang['empty']

    print(f"{gr}[{cy}{lang['about']['first_name']}{gr}]{gr} {entity.first_name}{wh}")
    print(f"{gr}[{cy}{lang['about']['last_name']}{gr}]{gr if entity.last_name != None else re} {entity.last_name if entity.last_name != None else Empty}{wh}")
    print(f"{gr}[{cy}{lang['about']['username']}{gr}]{gr if entity.username != None else re} {a + entity.username if entity.username != None else Empty}{wh}")
    print(f"{gr}[{cy}{lang['about']['id']}{gr}]{gr} {entity.id}{wh}")
    print(f"{gr}[{cy}{lang['about']['premium']}{gr}]{gr if entity.premium else re} {Yes if entity.premium else No}{wh}")
    print(f"{gr}[{cy}{lang['about']['verified']}{gr}]{gr if entity.verified else re} {Yes if entity.verified else No}{wh}")
    print(f"{gr}[{cy}{lang['about']['scam']}{gr}]{gr if entity.scam else re} {Yes if entity.scam else No}{wh}")
    print(f"{gr}[{cy}{lang['about']['color']}{gr}]{gr if entity.color != None else re} {entity.color}{wh}")
    print(f"{gr}[{cy}{lang['about']['profile_color']}{gr}]{gr if entity.profile_color != None else re} {entity.profile_color}{wh}\n")