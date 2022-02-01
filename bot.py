from discord.ext import commands
from discord.utils import get
import discord
import subprocess
import asyncio
import os
import sys
import json

intents = discord.Intents().all()

if not os.path.isfile("settings.json"):
    sys.exit("'settings.json' not found!")
else:
    with open("settings.json") as file:
        settings = json.load(file)
        print('\n' * 150)
        print("Discord Bot API Token: " + settings["token"])
        print("Game to lookout for: " + settings["bannable_Game"])

bot = discord.Client(intents=intents)

if __name__ == "__main__":
    print("Initialized!")

@bot.event
async def on_ready():
    print('\n')
    print("BanBot is online!, Beep Boop")
    activity = discord.Activity(name="with your Server privilege :)", type=discord.ActivityType.playing)
    await bot.change_presence(activity=activity)
    
@bot.event
async def on_member_update(before, after):
    name = settings["bannable_Game"] 
    if name in str(after.activity):
        print("Offense Detected!")
        print(after)
        if settings["kick_or_ban"] == "B":
            await after.ban(reason = "User is playing a prohibited game")
            channel = await after.create_dm()
            await channel.send("You have been Banned from the Server for commiting a serious offense: \nPlaying "+ settings["bannable_Game"] + ". Don't Play that Game.")
            print("User Banned from the Server!\n")
        
        if settings["kick_or_ban"] == "K":
            channel = await after.create_dm()
            await channel.send("You have been Kicked from the Server for commiting a serious offense: \nPlaying "+ settings["bannable_Game"] + ". Don't Play that Game.\n\nRejoin at: " + settings["invite_link"])
            await after.kick(reason = "User is playing a prohibited game")
            print("User Kicked from the Server!\n")

bot.run(settings["token"])

