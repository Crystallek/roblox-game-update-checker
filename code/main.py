from discord.ext import tasks
import requests
import discord
import json
import time
import os

os.chdir(os.path.dirname(__file__))

with open("data/data.txt", "r") as f:
    a = f.readlines()[0].removeprefix("token=")
    f.close()

b = discord.Client()
c = 0 
d = {}
e = []
f = False

@tasks.loop()
async def timer():
    if f:
        await b.wait_until_ready()
        channel = b.get_channel(c)
        try:
            for games in d:
                t = json.loads(requests.get(f'https://games.roblox.com/v1/games?universeIds={games}').text)
                if d[games] != t['data'][0]['updated']:
                    await channel.send(embed=discord.Embed(title=t['data'][0]['name'], url=f"https://www.roblox.com/games/{t['data'][0]['rootPlaceId']}", description=f"**Update detected!**\n\nLast update: **{d[games].replace('-', '.').split('T')[0]} at {d[games].split('T')[1].split('.')[0]}**\nLatest update: **{t['data'][0]['updated'].replace('-', '.').split('T')[0]} at {t['data'][0]['updated'].split('T')[1].split('.')[0]}**", color=discord.Color.red()).set_footer(text="Game update checker - Made by Crystallek#3348"))
                    d[games] = t['data'][0]['updated']
        except Exception as e:
            return f"Error: {e}"
    
    if not f: time.sleep(0.1)
    else: time.sleep(1)

@b.event
async def on_ready():
    print(f"Logged as {b.user}")
    timer.start()

@b.event
async def on_message(message):
    global c
    global d
    global e
    global f 

    if message.content.startswith(".setchannel"):

        c = int(message.content.split(".setchannel ")[1])
        await message.channel.send(f"Changed main channel to \"{json.loads(requests.get(f'https://discord.com/api/v6/channels/{c}', headers={'Authorization': f'Bot {a}'}).text)['name']}\"\nID: {c}")

    if message.content.startswith(".addgame"):
        try:
            r = json.loads(requests.get(f'https://api.roblox.com/universes/get-universe-containing-place?placeid={message.content.split(".addgame ")[1]}').text)
            time.sleep(0.2)
            r2 = json.loads(requests.get(f'https://games.roblox.com/v1/games?universeIds={r["UniverseId"]}').text)
            d[r["UniverseId"]] = str(r2['data'][0]['updated'])
            await message.channel.send(f"Succesfully added {r2['data'][0]['name']} to the list!")
        except KeyError:
            await message.channel.send(f"Please enter valid place ID, {message.content.split('.addgame ')[1]} isn\'t.")
        except BaseException:
            await message.channel.send("Unknown error, try again.")
    
    if message.content.startswith(".removegame"):
        try:
            r = json.loads(requests.get(f'https://api.roblox.com/universes/get-universe-containing-place?placeid={message.content.split(".removegame ")[1]}').text)
        except BaseException:
            await message.channel.send("Couldn't delete the game, because of an Roblox API error.")
        try:
            del d[r["UniverseId"]]
        except BaseException:
            await message.channel.send("Couldn't delete the game, because it doesn't exist.")
        else:
            await message.channel.send("Successfully removed.")

    if message.content.startswith(".start"):
        if c == 0:
            await message.channel.send("Error: No main channel for annoucements selected. Select it via command .setchannel <channel_id>")
        elif d == {}:
            await message.channel.send("Error: No games to check. Select them via command .addgame <game_id> or .getdatafromfile if you have them in txt file.")
        else:
            f = True
            await message.channel.send("Checking has started!")

    if message.content.startswith(".stop"):
        f = False
        await message.channel.send("Checking has stopped!")

    if message.content.startswith(".getgamesfromfile"):
        with open("data/data.txt", "r") as i:
            e = i.readlines()[1].removeprefix("games=").split(",")
            for game in e:
                try:
                    r = json.loads(requests.get(f'https://api.roblox.com/universes/get-universe-containing-place?placeid={game}').text)
                    time.sleep(0.2)
                    r2 = json.loads(requests.get(f'https://games.roblox.com/v1/games?universeIds={r["UniverseId"]}').text)
                    if r["UniverseId"] not in d:
                        d[r["UniverseId"]] = str(r2['data'][0]['updated'])
                        await message.channel.send(f"Succesfully added {r2['data'][0]['name']} to the list!")
                except BaseException:
                    await message.channel.send(f"Invalid game ID (\"{game}\"). Skipping...")
                time.sleep(0.2)
    
    if message.content.startswith(".erasegamesfrommemory"):
        d = {}
        await message.channel.send("Erased.")
    if message.content.startswith(".erasegamesfromfile"):
        with open("data/data.txt", "r") as f:
            lines = f.readlines()
        with open("data/data.txt", "w") as f:
            for line in lines:
                if str(line.strip("\n")).startswith("token="):
                    f.write(line)
            f.write("games=")
        await message.channel.send("Erased.")

b.run(a)
