
### Imports ###
import platform
from colorama import Fore
import os
import requests

def clear(): # Clear screen
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def sysm(message:str,id:int): # System message
    if id == 0:
        print( Fore.GREEN + "[+] " + message + Fore.WHITE)
    if id == 1:
        print( Fore.RED + "[-] " + message + Fore.WHITE)
    if id == 2:
        print(Fore.MAGENTA + "[$] " + message + Fore.WHITE)

os.system("pip install discord-py==1.7.3")
clear()
import discord
from discord.ext import commands
sysm("Got right version of discord-py!",0)
sysm("Dizzyspam (by spidermanfromearth69.)",2)
sysm("Put the token in token.txt likethis : TOKEN - NAME",2)
sysm("1. Spam with the token (must be verified with phone)",2)
sysm("2. Quit progam",2)
sysm("Select option",2)
while True:
    option = input(Fore.CYAN + "[#] " + Fore.WHITE)
    if option == "1":
        token = open("token.txt","r").readline(-1)
        token = token.split()
        sysm("Will use the token " + Fore.CYAN + token[2] + Fore.MAGENTA + " for the spam.",2)
        name = token[2]
        token = token[0]
        client = commands.Bot(command_prefix="*", self_bot=True)

        @client.event
        async def on_ready():
            i = 0
            sysm("Bot ready!",0)
            for guild in client.guilds:
                sysm(Fore.CYAN + guild.name + Fore.MAGENTA + " Guild Detected",2)
                i = i+1
            
            sysm("Bot in " + Fore.CYAN + str(i) + Fore.MAGENTA + " guilds",3)
            target_channel_id = int(input(Fore.CYAN + "Select a channel id to spam in (grab it manualy with developer mode enabled): " + Fore.WHITE))
            target_channel_id = int(target_channel_id)

            for guild in client.guilds:
                for channel in guild.channels:
                    if channel.id == target_channel_id:
                        message = input(Fore.CYAN + "What message to spam: " + Fore.WHITE)
                        while True:
                            try:
                                await channel.send(message)
                            except:
                                sysm("Error! Probably ratelimit (don't worry about it too much)",1)

        client.run(token,bot=False)

    elif option == "2":
        break
    else:
        sysm("Not an option!",1)
