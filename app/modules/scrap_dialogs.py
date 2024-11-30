from vendor.misc import *

async def scrap_dialogs():
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