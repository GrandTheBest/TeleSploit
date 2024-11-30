from vendor.misc import *

async def scrap_members_channel():
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