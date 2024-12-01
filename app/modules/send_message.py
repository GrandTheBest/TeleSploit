from vendor.misc import *

async def send_message():
    a = ""

    print(wh+f'{lang["select_mode"]}\n\n'+gr+'['+cy+'0'+gr+'] ' + f"{lang['by_username']}\n"+gr+'['+cy+'1'+gr+'] '+f'{lang["by_id"]}\n'+gr+'['+cy+'2'+gr+'] '+lang['by_number']+wh)
    mode = input(wh+"\ntelesploit("+re+"sendMessage"+wh+") > ")

    if int(mode) == 0:
        a = "username"
        target = "@" + input(wh+"\ntelesploit("+re+"sendMessage/"+a+wh+") > @")
    elif int(mode) == 1:
        a = "id"
        target = input(wh+"\ntelesploit("+re+"sendMessage/"+a+wh+") > ")
    elif int(mode) == 2:
        a = "number"
        target = "+" + input(wh+"\ntelesploit("+re+"sendMessage/"+a+wh+") > +")
    else:
        a = "username"
        print("Invalid option. Selected by username")
        target = "@" + input(wh+"\ntelesploit("+re+"sendMessage/"+a+wh+") > @")

    if "@" not in target and "+" not in target:
        target = int(target)

    print(gr+f"\n{lang['enter_message']}"+wh)
    message = input(wh+"\ntelesploit("+re+"sendMessage/"+str(target)+wh+") > ")

    try:
        await client.send_message(target, message)
        print(gr+f"\n{lang['message_sended']} "+str(target)+wh+"\n")
    except ValueError:
        print(re+f"\n{lang['cannot_find_entity']} "+str(target)+wh+"\n")