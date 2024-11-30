from vendor.misc import *

async def download_profile_photo():
    a = ""

    print(wh+'Select mode:\n\n'+gr+'['+cy+'0'+gr+'] ' + "By username\n"+gr+'['+cy+'1'+gr+'] '+'By ID'+wh)
    mode = input(wh+"\ntelesploit("+re+"downloadProfilePhoto"+wh+") > ")

    if int(mode) == 0:
        a = "username"
        target = "@" + input(wh+"\ntelesploit("+re+"downloadProfilePhoto/"+a+wh+") > @")
    elif int(mode) == 1:
        a = "id"
        target = input(wh+"\ntelesploit("+re+"downloadProfilePhoto/"+a+wh+") > ")
    else:
        a = "username"
        print("Invalid option. Selected by username")
        target = "@" + input(wh+"\ntelesploit("+re+"downloadProfilePhoto/"+a+wh+") > @")

    if "@" not in target:
        target = int(target)

    try:
        entity = await client.get_entity(target)
        await client.download_profile_photo(target, file=f"{entity.first_name}")
        print(f"\n{gr}[+] Profile photo successfully downloaded!{wh}\n")
    except ValueError:
        print(re+"\nCannot find any entity corresponding to "+target+wh+"\n")