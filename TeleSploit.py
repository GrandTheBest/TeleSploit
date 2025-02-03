from vendor.misc import *
from vendor.init import *

def banner():
    os.system('cls' if os.name == 'nt' else 'clear')

    print(re)
    tprint(toolname)
    print(wh)
    print(lang['subscription'])
    print(f"{cy}{version}{wh}\n")
    print(f"{re}By @GrandTheBest{wh}")
    print(f"{lang['change_language']}{wh}\n")
    print(lang['select_option'] + "\n")

    i = 0

    for option in lang['options']:
        print(gr+'['+cy+str(i)+gr+'] ' + option)
        i+=1
    print(wh)

banner()

async def main():
    global groups
    global channels
    global chats
    global _messages

    while True:
        chats = []
        s = input(prompt)

        if s != "":
            if s == "/lang":
                change_lang()
            if int(s) == 0:
                banner()
                await test_connection()
            elif int(s) == 1:
                banner()
                await scrap_members_group()
            elif int(s) == 2:
                banner()
                await scrap_members_channel()
            elif int(s) == 3:
                banner()
                await send_message()
            elif int(s) == 4:
                banner()
                await scrap_dialogs()
            elif int(s) == 5:
                banner()
                await scrap_messages()
            elif int(s) == 6:
                banner()
                await scrap_images()
            elif int(s) == 7:
                banner()
                await scrap_videos()
            elif int(s) == 8:
                banner()
                await realtime_messenger()
            elif int(s) == 9:
                banner()
                await delete_chat()
            elif int(s) == 10:
                banner()
                await delete_message()
            elif int(s) == 11:
                banner()
                await about_me()
            elif int(s) == 12:
                banner()
                await about_user()
            elif int(s) == 13:
                banner()
                await download_profile_photo()
            elif int(s) == 14:
                await spammer()
            else:
                banner()
                print("Invalid option\n")
                

with client:
    client.loop.run_until_complete(main())