from vendor.misc import *

async def scrap_members_group():
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

    print(gr+f'[+] {lang["choose_the_group"]} :'+re)
    i=0
    for g in groups:
        print(gr+'['+cy+str(i)+gr+']'+cy+' - '+ g.title + wh)
        i+=1
    g_index = input("\ntelesploit("+re+"scrapMembers/group"+wh+") > ")
    target_group=groups[int(g_index)]

    print(gr+f'[+] {lang["fetching_messages"]}')
    time.sleep(1)
    all_participants = []
    all_participants = await client.get_participants(target_group, aggressive=True)
        
    print(gr+f'[+] {lang["saving_in_file"]}')
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
    print(gr+f'[+] {lang["scrap_members"]}' + wh)