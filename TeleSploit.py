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

toolname = "TeleSploit"
inpt = "telesploit > "

options = ["Test connection", "Scrap members(Group)", "Scrap members(Channel)", "Send message", "Scrap dialogs", "Scrap messsages", "Scrap Photos"]

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
    print("TeleSploit - a utility for advanced interaction with Telegram\n")
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
            with open("groupMem.csv","w",encoding='UTF-8') as f:
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
            with open("channelMem.csv","w",encoding='UTF-8') as f:
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
                target = "@" + input(wh+"\ntelesploit("+re+"sendMessage/"+a+wh+") > @")
            elif int(mode) == 1:
                a = "id"
                target = input(wh+"\ntelesploit("+re+"sendMessage/"+a+wh+") > ")
            else:
                a = "username"
                print("Invalid option. Selected by username")
                target = "@" + input(wh+"\ntelesploit("+re+"sendMessage/"+a+wh+") > @")

            print(gr+'\n[+] Fetching Messages...'+wh)
            time.sleep(1)
            with open(f"{target}.csv","w",encoding='UTF-8') as f:
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

            mode = input(wh+"\ntelesploit("+re+"scrapMessages"+wh+") > ")

            if int(mode) == 0:
                a = "username"
                target = "@" + input(wh+"\ntelesploit("+re+"sendMessage/"+a+wh+") > @")
            elif int(mode) == 1:
                a = "id"
                target = input(wh+"\ntelesploit("+re+"sendMessage/"+a+wh+") > ")
            else:
                a = "username"
                print("Invalid option. Selected by username")
                target = "@" + input(wh+"\ntelesploit("+re+"sendMessage/"+a+wh+") > @")

            print(gr+'\n[+] Fetching Messages...'+wh)
            time.sleep(1)
            print(gr+'[+] Saving In file...'+wh)

            if "@" in target:
                async for message in client.iter_messages(target, reverse=True):
                    if message.photo:
                        await message.download_media('./' + str(target) + '/')
            else:
                async for message in client.iter_messages(int(target), reverse=True):
                    if message.photo:
                        await message.download_media('./' + str(target) + '/')

        else:
            banner()
            print("\nInvalid option\n")

with client:
    client.loop.run_until_complete(main())