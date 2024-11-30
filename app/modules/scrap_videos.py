from vendor.misc import *

async def scrap_videos():
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