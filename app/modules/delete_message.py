from vendor.misc import *

async def delete_message():
    messages.clear()
    chats.clear()

    async for chat in client.iter_dialogs():
        chats.append(chat)

    i = 0
    for chat in chats:
        print(f"{gr}[{cy}{i}{gr}] {chat.title}{wh}")
        i += 1
    
    print(f"\n{wh}Choose the dialog.")
    dialog = input(wh+"\ntelesploit("+re+"deleteMessage/"+wh+") > ")
    
    async for message in client.iter_messages(chats[int(dialog)], reverse=True):
        messages.append(message)

    i = 0
    for message in messages:
        date = message.date.strftime("%Y-%m-%d %H:%M:%S")
        is_reply = ""

        if message.is_reply:
            is_reply = f"{gr}Is reply!{wh}"
        else:
            is_reply = f"{re}Not reply!{wh}"
        try:
            from_user = await client.get_entity(message.from_id.user_id)
            ID = message.from_id.user_id
            print(f"{gr}[{cy}{i}{gr}] {cy}@{from_user.username}({ye}{ID}{cy}): {gr}{message.text}{wh}. {date}. {is_reply}")
        except AttributeError:
            try:
                from_user = await client.get_entity(message.peer_id.user_id)
                ID = message.peer_id.user_id
                print(f"{gr}[{cy}{i}{gr}] {cy}@{from_user.username}({ye}{ID}{cy}): {gr}{message.text}{wh}. {date}. {is_reply}")
            except AttributeError:
                print(f"{gr}[{cy}{i}{gr}] {cy}@{re}None{cy}({re}None{cy}): {gr}{message.text}{wh}. {date}. {is_reply}")
        i += 1
    
    print(f"\n{wh}Choose the message.")

    message = input(wh+"\ntelesploit("+re+"deleteMessage/"+wh+") > ")

    print("\nRemove for everyone? Yes or No. Default: No")
    isRevoke = input(wh+"\ntelesploit("+re+"deleteMessage/removeForEveryone"+wh+") > ")

    if isRevoke.lower() == "yes":
        await client.delete_messages(chats[int(dialog)].id, messages[int(message)].id, revoke=True)
    else:
        await client.delete_messages(chats[int(dialog)].id, messages[int(message)].id, revoke=False)

    print(f"\n{gr}Message successfuly removed!{wh}\n")