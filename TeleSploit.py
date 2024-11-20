from telethon import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerUser
from telethon.errors.rpcerrorlist import ChatAdminRequiredError
from art import tprint
import os, sys
import csv
import time

re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"
wh="\033[1;37m"
ye="\033[1;33m"

toolname = "TeleSploit"
version = "v1.6 Beta 2"
inpt = "telesploit > "

options = ["Test connection", "Scrap members(Group)", "Scrap members(Channel)", "Send message", "Scrap dialogs", "Scrap messsages", "Scrap photos", "Scrap videos", "RealTime Messenger", "Delete chat"]

for_replace = ["\\", "/", ":", "*", "?", "\"", "<", ">", "|"]

api_id = 21414125
api_hash = "7862c8301079da0b47934635785de0e5"

client = TelegramClient('cache', api_id, api_hash)

chats = []
last_date = None
chunk_size = 200
groups = []
channels = []
_chats = []
_messages = []
_dialogs = []

def banner():
    os.system('cls' if os.name == 'nt' else 'clear')

    print(re)
    tprint(toolname)
    print(wh)
    print("TeleSploit - a utility for advanced interaction with Telegram")
    print(f"{cy}Version: {version}{wh}\n")
    print("Select option \n")

    i = 0

    for option in options:
        print(gr+'['+cy+str(i)+gr+'] ' + option)
        i+=1
    print(wh)

banner()

async def main():
    global groups
    global channels
    global chats

    while True:
        chats = []
        s = input(inpt)

        if s != "":
            if int(s) == 0:
                banner()
                me = await client.get_me()
                print(me.stringify())
            elif int(s) == 1:
                banner()
                groups = []
                result = await client(GetDialogsRequest(
                    offset_date=last_date,
                    offset_id=0,
                    offset_peer=InputPeerEmpty(),
                    limit=chunk_size,
                    hash = 0
                ))
                chats.extend(result.chats)
                
                for chat in chats:
                    try:
                        if chat.megagroup== True:
                            groups.append(chat)
                    except:
                        continue

                print(gr+'[+] Choose a group to scrape members :'+re)
                i=0
                for g in groups:
                    print(gr+'['+cy+str(i)+gr+']'+cy+' - '+ g.title + wh)
                    i+=1
                g_index = input("\ntelesploit("+re+"scrapMembers/group"+wh+") > ")
                target_group=groups[int(g_index)]
     
                print(gr+'[+] Fetching Members...')
                time.sleep(1)
                all_participants = []
                all_participants = await client.get_participants(target_group, aggressive=True)
                 
                print(gr+'[+] Saving In file...')
                time.sleep(1)
                with open(f"{target_group.title}.csv","w",encoding='UTF-8') as f:
                    writer = csv.writer(f,delimiter=",",lineterminator="\n")
                    writer.writerow(['username','user id', 'access hash','name','group', 'group id'])
                    for user in all_participants:
                        if user.username:
                            username= user.username
                        else:
                            username= ""
                        if user.first_name:
                            first_name= user.first_name
                        else:
                            first_name= ""
                        if user.last_name:
                            last_name= user.last_name
                        else:
                            last_name= ""
                        name= (first_name + ' ' + last_name).strip()
                        writer.writerow([username,user.id,user.access_hash,name,target_group.title, target_group.id])      
                print(gr+'[+] Members scraped successfully.' + wh)
            elif int(s) == 2:
                banner()
                channels = []
                result = await client(GetDialogsRequest(
                    offset_date=last_date,
                    offset_id=0,
                    offset_peer=InputPeerEmpty(),
                    limit=chunk_size,
                    hash = 0
                ))
                chats.extend(result.chats)
                
                for chat in chats:
                    try:
                        if chat.broadcast == True:
                            channels.append(chat)
                    except:
                        continue

                print(gr+'[+] Choose a channel to scrape members :'+re)
                i=0
                for c in channels:
                    print(gr+'['+cy+str(i)+gr+']'+cy+' - '+ c.title + wh)
                    i+=1
                c_index = input(wh+"\ntelesploit("+re+"scrapMembers/channel"+wh+") > ")
                target_channel=channels[int(c_index)]

                try:
                    print(gr+'[+] Fetching Members...'+wh)
                    time.sleep(1)
                    all_participants = []
                    all_participants = await client.get_participants(target_channel, aggressive=True)
                except ChatAdminRequiredError:
                    print(re+"Error: you're not admin!"+wh)
                    client.disconnect()
                    sys.exit()
                 
                print(gr+'[+] Saving In file...'+wh)
                time.sleep(1)
                with open(f"{target_channel.title}.csv","w",encoding='UTF-8') as f:
                    writer = csv.writer(f,delimiter=",",lineterminator="\n")
                    writer.writerow(['username','user id', 'access hash','name','channel', 'channel id'])
                    for user in all_participants:
                        if user.username:
                            username= user.username
                        else:
                            username= ""
                        if user.first_name:
                            first_name= user.first_name
                        else:
                            first_name= ""
                        if user.last_name:
                            last_name= user.last_name
                        else:
                            last_name= ""
                        name= (first_name + ' ' + last_name).strip()
                        writer.writerow([username,user.id,user.access_hash,name,target_channel.title, target_channel.id])      
                print(gr+'[+] Members scraped successfully.' + wh)
            elif int(s) == 3:
                a = ""

                banner()
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
            elif int(s) == 4:
                banner()
                _chats = []
                print(gr+'[+] Fetching Dialogs...'+wh)
                time.sleep(1)
                with open("dialogs.csv","w",encoding='UTF-8') as f:
                    print(gr+'[+] Saving In file...'+wh)
                    time.sleep(1)
                    writer = csv.writer(f,delimiter=",",lineterminator="\n")
                    writer.writerow(['id','title', 'last_message','last_msg_date','unread_count', 'is_user', 'is_group', 'is_channel'])
                    async for dialog in client.iter_dialogs():
                        # name= (first_name + ' ' + last_name).strip()
                        date = '{:.19}'.format(str(dialog.date))
                        writer.writerow([dialog.id,dialog.title,dialog.message.message,date,dialog.unread_count, dialog.is_user, dialog.is_group, dialog.is_channel])
                print(gr+'[+] Dialogs scraped successfully.\n' + wh)
            elif int(s) == 5:
                banner()
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
            elif int(s) == 6:
                banner()
                _messages = []
                _dialogs = []

                print(wh+'Select mode:\n\n'+gr+'['+cy+'0'+gr+'] ' + "By username\n"+gr+'['+cy+'1'+gr+'] '+'By ID'+wh)

                mode = input(wh+"\ntelesploit("+re+"scrapPhotos"+wh+") > ")

                if int(mode) == 0:
                    a = "username"
                    target = "@" + input(wh+"\ntelesploit("+re+"scrapPhotos/"+a+wh+") > @")
                elif int(mode) == 1:
                    a = "id"
                    target = input(wh+"\ntelesploit("+re+"scrapPhotos/"+a+wh+") > ")
                else:
                    a = "username"
                    print("Invalid option. Selected by username")
                    target = "@" + input(wh+"\ntelesploit("+re+"scrapPhotos/"+a+wh+") > @")

                print(gr+'\n[+] Fetching Photos...'+wh)
                time.sleep(1)
                print(gr+'[+] Saving In file...'+wh)


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

                if "@" in target:
                    async for message in client.iter_messages(target, reverse=True):
                        if message.photo:
                            await message.download_media('./' + title + '/')
                else:
                    async for message in client.iter_messages(int(target), reverse=True):
                        if message.photo:
                            await message.download_media('./' + title + '/')
            elif int(s) == 7:
                banner()
                _messages = []
                _dialogs = []

                print(wh+'Select mode:\n\n'+gr+'['+cy+'0'+gr+'] ' + "By username\n"+gr+'['+cy+'1'+gr+'] '+'By ID'+wh)

                mode = input(wh+"\ntelesploit("+re+"scrapVideos"+wh+") > ")

                if int(mode) == 0:
                    a = "username"
                    target = "@" + input(wh+"\ntelesploit("+re+"scrapVideos/"+a+wh+") > @")
                elif int(mode) == 1:
                    a = "id"
                    target = input(wh+"\ntelesploit("+re+"scrapVideos/"+a+wh+") > ")
                else:
                    a = "username"
                    print("Invalid option. Selected by username")
                    target = "@" + input(wh+"\ntelesploit("+re+"scrapVideos/"+a+wh+") > @")

                print(gr+'\n[+] Fetching Videos...'+wh)
                time.sleep(1)
                print(gr+'[+] Saving In file...'+wh)

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

                if "@" in target:
                    async for message in client.iter_messages(target, reverse=True):
                        if message.video:
                            await message.download_media('./' + title + '/')
                else:
                    async for message in client.iter_messages(int(target), reverse=True):
                        if message.video:
                            await message.download_media('./' + title + '/')
            elif int(s) == 8:
                banner()
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
            elif int(s) == 9:
                banner()

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
            else:
                banner()
                print("\nInvalid option\n")

with client:
    client.loop.run_until_complete(main())