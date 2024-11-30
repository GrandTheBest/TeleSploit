from vendor.misc import *

async def scrap_messages():
    _messages = []
    _dialogs = []

    print(wh+'Select mode:\n\n'+gr+'['+cy+'0'+gr+'] ' + "By username\n"+gr+'['+cy+'1'+gr+'] '+'By ID'+wh)

    mode = input(wh+"\ntelesploit("+re+"scrapMessages"+wh+") > ")

    if int(mode) == 0:
        a = "username"
        target = "@" + input(wh+"\ntelesploit("+re+"scrapMessages/"+a+wh+") > @")
    elif int(mode) == 1:
        a = "id"
        target = input(wh+"\ntelesploit("+re+"scrapMessages/"+a+wh+") > ")
    else:
        a = "username"
        print("Invalid option. Selected by username")
        target = "@" + input(wh+"\ntelesploit("+re+"scrapMessages/"+a+wh+") > @")

    print(gr+'\n[+] Fetching Messages...'+wh)
    time.sleep(1)

    _target = ""
    title = ""

    if "@" in target:
        _target = await client.get_entity(target)
    else:
        _target = await client.get_entity(int(target))

    try:
        title = _target.title
        for symbol in for_replace:
            if symbol in title:
                title = title.replace(symbol, ".")
    except AttributeError:
        if _target.last_name is not None:
            title = _target.first_name + " " + _target.last_name
            for symbol in for_replace:
                if symbol in title:
                    title = title.replace(symbol, ".")
        else:
            title = _target.first_name
            for symbol in for_replace:
                if symbol in title:
                    title = title.replace(symbol, ".")

    with open(f"{title}.csv","w",encoding='UTF-8') as f:
        print(gr+'[+] Saving In file...'+wh)
        time.sleep(1)
        writer = csv.writer(f,delimiter=",",lineterminator="\n")
        writer.writerow(['text', 'is_reply', 'from_id', 'from_username', 'date'])

        if "@" in target:
            async for message in client.iter_messages(target, reverse=True):
                date = message.date.strftime("%Y-%m-%d %H:%M:%S")
                try:
                    from_user = await client.get_entity(message.from_id.user_id)
                    ID = message.from_id.user_id
                    writer.writerow([message.text, message.is_reply, ID, from_user.username, date])
                except AttributeError:
                    try:
                        from_user = await client.get_entity(message.peer_id.user_id)
                        ID = message.peer_id.user_id
                        writer.writerow([message.text, message.is_reply, ID, from_user.username, date])
                    except AttributeError:
                        writer.writerow([message.text, message.is_reply, 0, None, date])
        else:
            async for message in client.iter_messages(int(target), reverse=True):
                date = message.date.strftime("%Y-%m-%d %H:%M:%S")
                try:
                    from_user = await client.get_entity(message.from_id.user_id)
                    ID = message.from_id.user_id
                    writer.writerow([message.text, message.is_reply, ID, from_user.username, date])
                except AttributeError:
                    try:
                        from_user = await client.get_entity(message.peer_id.user_id)
                        ID = message.peer_id.user_id
                        writer.writerow([message.text, message.is_reply, ID, from_user.username, date])
                    except AttributeError:
                        writer.writerow([message.text, message.is_reply, 0, None, date])
    print(gr+'[+] Members scraped successfully.\n' + wh)