from vendor.misc import *

async def spammer():
    a = ""

    print(wh+f"\n{lang['select_mode']}\n\n"+gr+'['+cy+'0'+gr+'] ' + f"{lang['by_username']}\n"+gr+'['+cy+'1'+gr+'] '+lang['by_id']+wh)
    mode = input(wh+"\nOpenTSP("+re+""+wh+") > ")

    if int(mode) == 0:
        a = "username"
        target = "@" + input(wh+"\nOpenTSP("+re+"spammer/"+a+wh+") > @")
    elif int(mode) == 1:
        a = "number"
        target = input(wh+"\nOpenTSP("+re+"spammer/"+a+wh+") > ")
    else:
        a = "username"
        print(lang['invalid_option_selected_by_username'])
        target = "@" + input(wh+"\nOpenTSP("+re+"spammer/"+a+wh+") > @")

    if "@" not in target:
        target = int(target)

    print(wh+f"{lang['enter_message']}:")
    message = input(wh+f"\nOpenTSP({re}spammer/{target}/message{wh}) > ")

    print(wh+f"{lang['enter_count_iterations']}:")
    iter_count = input(wh+f"\nOpenTSP({re}spammer/{target}/count{wh}) > ")

    print(wh+f"{lang['enter_delay']}(ms):")
    delay = input(wh+f"\nOpenTSP({re}spammer/{target}/delay{wh}) > ")

    print(gr+f'[+] {lang["spammer_started"]}'+wh)

    for i in range(1, int(iter_count)):
        try:
            await client.send_message(target, message)
            print(gr+f"{lang['message_sended']} {target}"+wh+"")
        except ValueError:
            print(re+f"{lang['cannot_find_entity']} "+str(target)+wh+"\n")
            break
        except Exception:
            print(f"{re}[*]{lang['except']}{wh}")
        
        time.sleep(int(delay) / 1000)
    
    print(f"{gr}[+] {lang['done']}{wh}\n")