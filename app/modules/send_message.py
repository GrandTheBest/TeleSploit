from vendor.misc import *

async def send_message():
    a = ""

    print(wh+'Select mode:\n\n'+gr+'['+cy+'0'+gr+'] ' + "By username\n"+gr+'['+cy+'1'+gr+'] '+'By number'+wh)
    mode = input(wh+"\ntelesploit("+re+"sendMessage"+wh+") > ")

    if int(mode) == 0:
        a = "username"
        target = "@" + input(wh+"\ntelesploit("+re+"sendMessage/"+a+wh+") > @")
    elif int(mode) == 1:
        a = "number"
        target = "+" + input(wh+"\ntelesploit("+re+"sendMessage/"+a+wh+") > +")
    else:
        a = "username"
        print("Invalid option. Selected by username")
        target = "@" + input(wh+"\ntelesploit("+re+"sendMessage/"+a+wh+") > @")

    print(gr+"\nEnter message"+wh)
    message = input(wh+"\ntelesploit("+re+"sendMessage/"+target+wh+") > ")

    try:
        await client.send_message(target, message)
        print(gr+"\nMessage sended successfully to "+target+wh+"\n")
    except ValueError:
        print(re+"\nCannot find any entity corresponding to "+target+wh+"\n")