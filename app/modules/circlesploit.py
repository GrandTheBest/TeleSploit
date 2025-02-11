from vendor.misc import *
from vendor.utils import crop_video_opencv, add_audio_to_video

import os
import tqdm
import random
import colorama
import tempfile

colorama.init(autoreset=True)

pbar = None

# Функция прогресса
def progress_callback(current, total):
    if pbar:  # Проверяем, что pbar не None
        pbar.update(current - pbar.n)  # Обновление прогресса в прогресс-баре

async def circlesploit():
    temp_dir = tempfile.gettempdir()

    if sys.platform.startswith("win"):
        temp_dir += "\\"
    else:
        temp_dir += "/"

    a = ""

    print(wh+f"\n{lang['select_mode']}\n\n"+gr+'['+cy+'0'+gr+'] ' + f"{lang['by_username']}\n"+gr+'['+cy+'1'+gr+'] '+lang['by_id']+wh)
    mode = input(wh+"\nOpenTSP("+re+""+wh+") > ")

    if int(mode) == 0: 
        a = "username"
        target = "@" + input(wh+"\nOpenTSP("+re+"circlesploit/"+a+wh+") > @")
    elif int(mode) == 1:
        a = "number"
        target = input(wh+"\nOpenTSP("+re+"circlesploit/"+a+wh+") > ")
    else:
        a = "username"
        print(lang['invalid_option_selected_by_username'])
        target = "@" + input(wh+"\nOpenTSP("+re+"circlesploit/"+a+wh+") > @") 

    if "@" not in target:
        target = int(target)

    print(wh+f"{lang['enter_full_path']}:")
    path = input(wh+f"\nOpenTSP({re}circlesploit/{target}/path{wh}) > ")

    o_path = temp_dir + str(random.randint(100000, 999999)) + ".mp4"

    crop_video_opencv(path, o_path)

    final_output = temp_dir + str(random.randint(100000, 999999)) + ".mp4"
    add_audio_to_video(path, o_path, final_output)
    o_path = final_output  # Меняем путь на итоговый файл с аудио

    file_size = os.path.getsize(o_path)

    print(colorama.Fore.YELLOW + "[$] Starting file upload...")

    global pbar
    pbar = tqdm.tqdm(total=file_size, unit='B', unit_scale=True, desc="Sending circle", position=0, dynamic_ncols=True)

    try:
        # Проверка, если target это @username, иначе это ID
        if "@" not in target:
            target = int(target)


        # Отправка файла
        await client.send_file(entity=target, file=o_path, progress_callback=progress_callback, video_note=True)
        pbar.close()
        print(colorama.Fore.GREEN + "[+] Success!")
    except Exception as e:
        print(colorama.Fore.RED + f"[*] Except! {e}")
    finally:
        if os.path.exists(o_path):
            os.remove(o_path)
        if os.path.exists(final_output):
            os.remove(final_output)

    # Закрытие прогресс-бара
    pbar.close()

