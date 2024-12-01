from vendor.misc import *

async def about_user():
    a = ""

    print(wh+f"{lang['select_mode']}:\n\n"+gr+'['+cy+'0'+gr+'] ' + f"{lang['by_username']}\n"+gr+'['+cy+'1'+gr+'] '+lang['by_id']+wh)
    mode = input(wh+"\ntelesploit("+re+"aboutUser"+wh+") > ")

    if int(mode) == 0:
        a = "username"
        target = "@" + input(wh+"\ntelesploit("+re+"aboutUser/"+a+wh+") > @")
    elif int(mode) == 1:
        a = "number"
        target = input(wh+"\ntelesploit("+re+"aboutUser/"+a+wh+") > ")
    else:
        a = "username"
        print(lang['invalid_option_selected_by_username'])
        target = "@" + input(wh+"\ntelesploit("+re+"aboutUser/"+a+wh+") > @")

    if "@" not in target:
        target = int(target)

    try:
        entity = await client.get_entity(target)
        a = "@"

        Yes = lang['yes']
        No = lang['no']
        Empty = lang['empty']

        print(f"{gr}[{cy}{lang['about']['first_name']}{gr}]{gr} {entity.first_name}{wh}")
        print(f"{gr}[{cy}{lang['about']['last_name']}{gr}]{gr if entity.last_name != None else re} {entity.last_name if entity.last_name != None else Empty}{wh}")
        print(f"{gr}[{cy}{lang['about']['username']}{gr}]{gr if entity.username != None else re} {a + entity.username if entity.username != None else Empty}{wh}")
        print(f"{gr}[{cy}{lang['about']['id']}{gr}]{gr} {entity.id}{wh}")
        print(f"{gr}[{cy}{lang['about']['access_hash']}{gr}]{gr} {entity.access_hash}{wh}")
        print(f"{gr}[{cy}{lang['about']['premium']}{gr}]{gr if entity.premium else re} {Yes if entity.premium else No}{wh}")
        print(f"{gr}[{cy}{lang['about']['verified']}{gr}]{gr if entity.verified else re} {Yes if entity.verified else No}{wh}")
        print(f"{gr}[{cy}{lang['about']['scam']}{gr}]{gr if entity.scam else re} {Yes if entity.scam else No}{wh}")
        print(f"{gr}[{cy}{lang['about']['color']}{gr}]{gr if entity.color != None else re} {entity.color}{wh}")
        print(f"{gr}[{cy}{lang['about']['profile_color']}{gr}]{gr if entity.profile_color != None else re} {entity.profile_color}{wh}\n")
    except ValueError:
        print(re+"\nCannot find any entity corresponding to "+target+wh+"\n")