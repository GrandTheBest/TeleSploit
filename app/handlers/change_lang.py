from vendor.misc import *
import time

def change_lang():
    with open("config.json") as f:
        c = json.loads(f.read())
    with open("config.json", "w") as f:
        a = lang['lang_changed']
        b = lang['reload_script']
        x = ""

        if cfg['app']['config']['language'] == "en-US":
            c['app']['config']['language'] = "ru-RU"
        else:
            c['app']['config']['language'] = "en-US"
        json.dump(c, f, ensure_ascii=False, indent=4)

    print("\n" + gr + a + wh)

    print(gr+ b + wh)

    time.sleep(3)
    client.disconnect()
    sys.exit(0)