from vendor.misc import *

async def realtime_messenger():
    _messages = []

    print(wh+'Select mode:\n\n'+gr+'['+cy+'0'+gr+'] ' + "By username\n"+gr+'['+cy+'1'+gr+'] '+'By ID'+wh)

    mode = input(wh+"\ntelesploit("+re+"RealTimeMessenger"+wh+") > ")

    if int(mode) == 0:
        a = "username"
        target = "@" + input(wh+"\ntelesploit("+re+"RealTimeMessenger/"+a+wh+") > @")
    elif int(mode) == 1:
        a = "id"
        target = input(wh+"\ntelesploit("+re+"RealTimeMessenger/"+a+wh+") > ")
    else:
        a = "username"
        print("Invalid option. Selected by username")
        target = "@" + input(wh+"\ntelesploit("+re+"RealTimeMessenger/"+a+wh+") > @")

    print(gr+'\n[+] Fetching Messages...'+wh)
    time.sleep(1)

    _target = ""
    title = ""

    if "@" in target:
        _target = await client.get_entity(target)
    else:
        _target = await client.get_entity(int(target))

    if "@" in target:
        async for message in client.iter_messages(target, reverse=True):
            date = message.date.strftime("%Y-%m-%d %H:%M:%S")
            is_reply = ""

            if message.is_reply:
                is_reply = f"{gr}Is reply!{wh}"
            else:
                is_reply = f"{re}Not reply!{wh}"
            try:
                from_user = await client.get_entity(message.from_id.user_id)
                ID = message.from_id.user_id
                print(f"{cy}@{from_user.username}({ye}{ID}{cy}): {gr}{message.text}{wh}. {date}. {is_reply}")
            except AttributeError:
                try:
                    from_user = await client.get_entity(message.peer_id.user_id)
                    ID = message.peer_id.user_id
                    print(f"{cy}@{from_user.username}({ye}{ID}{cy}): {gr}{message.text}{wh}. {date}. {is_reply}")
                except AttributeError:
                    print(f"{cy}@{re}None{cy}({re}None{cy}): {gr}{message.text}{wh}. {date}. {is_reply}")
    else:
        async for message in client.iter_messages(int(target), reverse=True):
            date = message.date.strftime("%Y-%m-%d %H:%M:%S")
            try:
                from_user = await client.get_entity(message.from_id.user_id)
                ID = message.from_id.user_id
                print(f"{cy}@{from_user.username}({ye}{ID}{cy}): {gr}{message.text}{wh}. {date}. {is_reply}")
            except AttributeError:
                try:
                    from_user = await client.get_entity(message.peer_id.user_id)
                    ID = message.peer_id.user_id
                    print(f"{cy}@{from_user.username}({ye}{ID}{cy}): {gr}{message.text}{wh}. {date}. {is_reply}")
                except AttributeError:
                    print(f"{cy}@{re}None{cy}({re}None{cy}): {gr}{message.text}{wh}. {date}. {is_reply}")
    while True:
        msg = input(wh+"\ntelesploit("+re+"RealTimeMessenger/"+target+wh+") > ")
        await client.send_message(_target, msg)