# Discord-Activity-Kicker-Bot
Kicks Discord Users the second they open a game.  
Uses discord.py as a framework.

## Requirements:
- `Python 3.5.3` and up - https://www.python.org/downloads/
- `discord.py` - Using `pip install discord.py` will install the latest version. Read the Docs [here](https://discordpy.readthedocs.io/en/latest/).
- The Python code for the Bot itself - Download the latest [release](https://github.com/Nighthater/Discord-Activity-Kicker-Bot/releases)


## Steps to use the bot yourself

### Configure settings.json

#### Get the API tokens:
- Create discord Bot token: https://discord.com/developers/applications

#### Replace `token` with your Bot Token
#### Replace `bannable game` with the Game you dont want your users to play (Name is case sensitive)
#### Replace `kick or ban` with either an K for Kick or a B for Ban
#### Replace `invite link` with your server Invite Link for kicked users

## Invite the bot to your server and set Intents
- Go to the [Discord Developer Portal](https://discord.com/developers/applications)
- Select your Application
- Select `Bot` then under Privileged Gateway Intents, tick `Presence Intent` and `Server Member Intent`
- Select `OAuth2` then `URL Generator`
- Under `Scopes`, tick `bot`
- For `Permissions` you only need to tick `Kick Users` and `Ban Users` or `Administrator`
- Open the generated URL at the bottom
- Select your server and confirm

## All done

Now you have finished setting up your bot.\
Run bot.py with `python3 bot.py` from the directory.
After a few seconds the bot should come online on your Server.
