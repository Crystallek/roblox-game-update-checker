[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/Crystallek/discord-chat-logger.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/Crystallek/discord-chat-logger/context:python)

# roblox-game-update-checker
A program, which will update you about roblox game updates you choose.

Should work on replit too (haven't tried it though)

How to use:
  - insert the bot's token into token.txt file located in data folder
  - if you want, you can insert the game ids you want to check for update into games.txt folder, but you can add them later.
  - run it
 
Commands:
  - .setchannel - Sets the channel where the annoucements about game updates will show, it won't let you to start checking if you won't set it
  - .addgame <game-id> - Adds the game into memory.
  - .removegame <game-id> - Removes the game from memory.
  - .start - Starts the checking.
  - .stop - Stops the checking (can take longer to respond)
  - .getgamesfromfile - Loads the games from file into memory.
  - .erasegamesfrommemory - Deletes all games from memory (it won't delete them from the file though)
  - .erasegamesfrofile - Deletes all games from a file

TODO (in this order):
  - optimalisation
