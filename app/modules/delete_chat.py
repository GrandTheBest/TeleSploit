from vendor.misc import *

async def delete_chat():
    chats.clear()

    async for chat in client.iter_dialogs():
        chats.append(chat)

    i = 0
    for chat in chats:
        print(f"{gr}[{cy}{i}{gr}] {chat.title}{wh}")
        i += 1
    
    print(f"\n{wh}Choose the dialog.")
    dialog = input(wh+"\ntelesploit("+re+"deleteChat/"+wh+") > ")
    print("\nRemove for everyone? Yes or No. Default: No")
    isRevoke = input(wh+"\ntelesploit("+re+"deleteChat/removeForEveryone"+wh+") > ")

    if isRevoke.lower() == "yes":
        await client.delete_dialog(chats[int(dialog)].id, revoke=True)
    else:
        await client.delete_dialog(chats[int(dialog)].id, revoke=False)

    print(f"\n{gr}Dialog successfuly removed!{wh}\n")