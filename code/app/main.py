import os
import json
import time
import requests
import colorama
import webbrowser
import win10toast_click

os.chdir(os.path.dirname(__file__))

d = {}
toaster = win10toast_click.ToastNotifier()

print(f"""{colorama.Fore.BLUE}   _____          __  __ ______   _    _ _____  _____       _______ ______    _____ _    _ ______ _____ _  ________ _____  
  / ____|   /\   |  \/  |  ____| | |  | |  __ \|  __ \   /\|__   __|  ____|  / ____| |  | |  ____/ ____| |/ /  ____|  __ \ 
 | |  __   /  \  | \  / | |__    | |  | | |__) | |  | | /  \  | |  | |__    | |    | |__| | |__ | |    | ' /| |__  | |__) |
 | | |_ | / /\ \ | |\/| |  __|   | |  | |  ___/| |  | |/ /\ \ | |  |  __|   | |    |  __  |  __|| |    |  < |  __| |  _  / 
 | |__| |/ ____ \| |  | | |____  | |__| | |    | |__| / ____ \| |  | |____  | |____| |  | | |___| |____| . \| |____| | \ \ 
  \_____/_/    \_\_|  |_|______|  \____/|_|    |_____/_/    \_\_|  |______|  \_____|_|  |_|______\_____|_|\_\______|_|  \_|
\n{colorama.Fore.RESET}Made by Crystallek#3348""")

with open("data/data.txt", "r") as i:
    e = i.readlines()
    for game in e:
        try:
            r = json.loads(requests.get(f'https://api.roblox.com/universes/get-universe-containing-place?placeid={game}').text)
            time.sleep(0.2)
            r2 = json.loads(requests.get(f'https://games.roblox.com/v1/games?universeIds={r["UniverseId"]}').text)
            if r["UniverseId"] not in d:
                d[r["UniverseId"]] = str(r2['data'][0]['updated'])
                print(r2)
                print(f"{colorama.Fore.GREEN}[SUCCESS]{colorama.Fore.RESET} Succesfully added \"{r2['data'][0]['name']}\" to the list!")
        except BaseException:
            print(f"{colorama.Fore.RED}[ERROR]{colorama.Fore.RESET} Invalid game ID (\"{game}\"). Skipping...")
        time.sleep(0.2)

print(f"{colorama.Fore.GREEN}[SUCCESS]{colorama.Fore.RESET} Games successfully loaded, checking has started.")
while True:
    try:
        for games in d:
            t = json.loads(requests.get(f'https://games.roblox.com/v1/games?universeIds={games}').text)
            if d[games] != t['data'][0]['updated']:
                print(f"{colorama.Fore.YELLOW}[UPDATE DETECTED]{colorama.Fore.RESET}\n" + "="*50 + f"\n{t['data'][0]['name']}\nhttps://www.roblox.com/games/{t['data'][0]['rootPlaceId']}\n\nLast update: {d[games].replace('-', '.').split('T')[0]} at {d[games].split('T')[1].split('.')[0]}\nLatest update: {t['data'][0]['updated'].replace('-', '.').split('T')[0]} at {t['data'][0]['updated'].split('T')[1].split('.')[0]}\n" + "="*50)
                toaster.show_toast(
                "[UPDATE DETECTED]",
                f"{t['data'][0]['name']}",
                icon_path=None,  
                duration=5, 
                threaded=True, 
                callback_on_click=lambda: webbrowser.open_new(f"https://www.roblox.com/games/{t['data'][0]['rootPlaceId']}")
                )
                d[games] = t['data'][0]['updated']
    except Exception as e:
        print(f"{colorama.Fore.RED}[ERROR]{colorama.Fore.RESET} {e}")
    time.sleep(5)