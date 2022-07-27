# roblox-game-update-checker
A Discord bot, which will update you about roblox game updates you choose.

How to use:
  - insert the bot's token into token.txt file located in data folder
  - if you want, you can insert the game id's you want to check for update into games.txt folder, but you can add them later.
  - run it
 
Commands:
  - .setchannel - Sets the channel where the annoucements about game updates will show, it won't let you to start checking if you won't set it
  - .addgame <game-id> - Adds the game into memory.
  - .removegame <game-id> - Removes the game from memory.
  - .start - Starts the checking.
  - .stop - Stops the checking (can take longer to respond)
  - .getgamesfromfile - Loads the games from file into memory.
  - .erasegames - Delete all the games from memory (it won't delete them from the file though)

TODO (in this order):
  - .info command
  - optimalisation (it sucks now in my opinion, could be better)
  - replace global vars with bot vars
  - and some more things i will find...
