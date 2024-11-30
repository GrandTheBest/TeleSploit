from vendor.misc import *

async def about_me():
    entity = await client.get_me()

    a = "@"

    Yes = "Yes"
    No = "No"
    Empty = "Empty"

    print(f"{gr}[{cy}First Name{gr}]{gr} {entity.first_name}{wh}")
    print(f"{gr}[{cy}Last Name{gr}]{gr if entity.last_name != None else re} {entity.last_name if entity.last_name != None else Empty}{wh}")
    print(f"{gr}[{cy}Username{gr}]{gr if entity.username != None else re} {a + entity.username if entity.username != None else Empty}{wh}")
    print(f"{gr}[{cy}ID{gr}]{gr} {entity.id}{wh}")
    print(f"{gr}[{cy}Premium{gr}]{gr if entity.premium else re} {Yes if entity.premium else No}{wh}")
    print(f"{gr}[{cy}Verified{gr}]{gr if entity.verified else re} {Yes if entity.verified else No}{wh}")
    print(f"{gr}[{cy}Scam{gr}]{gr if entity.scam else re} {Yes if entity.scam else No}{wh}")
    print(f"{gr}[{cy}Color{gr}]{gr if entity.color != None else re} {entity.color}{wh}")
    print(f"{gr}[{cy}Profile Color{gr}]{gr if entity.profile_color != None else re} {entity.profile_color}{wh}\n")