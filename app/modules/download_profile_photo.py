from vendor.misc import *

async def download_profile_photo():
    a = ""

    print(wh+f'{lang["select_mode"]}:\n\n'+gr+'['+cy+'0'+gr+'] ' + f"{lang['by_username']}\n"+gr+'['+cy+'1'+gr+'] '+lang['by_id']+wh)
    mode = input(wh+"\ntelesploit("+re+"downloadProfilePhoto"+wh+") > ")

    if int(mode) == 0:
        a = "username"
        target = "@" + input(wh+"\ntelesploit("+re+"downloadProfilePhoto/"+a+wh+") > @")
    elif int(mode) == 1:
        a = "id"
        target = input(wh+"\ntelesploit("+re+"downloadProfilePhoto/"+a+wh+") > ")
    else:
        a = "username"
        print(lang['invalid_option_selected_by_username'])
        target = "@" + input(wh+"\ntelesploit("+re+"downloadProfilePhoto/"+a+wh+") > @")

    if "@" not in target:
        target = int(target) 

    try:
        entity = await client.get_entity(target)
        await client.download_profile_photo(target, file=f"{entity.first_name}")
        print(f"\n{gr}[+] {lang['profile_photo_downloaded']}{wh}\n")
    except ValueError:
        print(re+f"\n{lang['cannot_find_entity']} "+target+wh+"\n")