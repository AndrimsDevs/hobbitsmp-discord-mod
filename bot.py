
import discord
from discord.ext import commands
from discord import Permissions

description = ""

# declare intents to discord api
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="TBD", description=description, intents=intents)

# forbidden words list
forbidden_words = ["fuck", "shit", "bitch", "whore", "nigga", "nigger", "cunt", "pussy", "fag"]

# function to send discord a flag
def raiseFlag(wordToRaise, messageAuthor, messageLink):
    import requests

    # Define the webhook URL and payload data
    webhook_url = "https://discord.com/api/webhooks/1089343268782882956/k7FwrQirM_BP_WSAxwStVMnGGa44LHgnJUV3uBj92nfHJq0xCLoNXCy0yBdbxDUUqAyt"
    payload = {
        "content": "Flag Inbound",
        "username": "Owner Banned Word Flagging",
        "avatar_url": "https://cdn.discordapp.com/attachments/982416332685471764/1089394190166794372/hobbits2_logo.png",
        "embeds": [
            {
                "title": "flag ig",
                "description": "%s sent flag key: ||`%s`|| in <#%s>"%(messageAuthor, wordToRaise, messageLink),
                "color": 16711680, # RGB color code (decimal) - red in this example
            }
        ]
    }

    # Send the webhook using the requests library
    response = requests.post(webhook_url, json=payload)

    # Check the response status code to see if the webhook was successful
    if response.status_code == 204:
        print("Webhook sent successfully!")
    else:
        print("Error sending webhook:", response.status_code)

class MyClient(discord.Client):
    # sets discord prescense on script boot
    async def on_ready(self): 
        await client.change_presence(status=discord.Status.dnd, activity=discord.Game('Watching Ault and Bowswa\'s msgs'))
        print(f'Logged on as {self.user}!')

    @bot.event # executes code below when message detected by bot in guild
    async def on_message(self, message):
        # to make sure bot does not reply to itself
        if message.author.id == self.user.id:
            return
        
        for bannedWord in forbidden_words:
            if (str(message.content)).find(bannedWord) != -1:
                # log into console
                print(f'Message from {message.author}: {message.content}')
                # send notification embed to discord
                raiseFlag(bannedWord, message.author, message.channel.id)
                # reply to message sender
                await message.reply(f"{message.author} watch your language.", mention_author=True)
                # break out of loop to avoid multiple flags for multiple flags within one msg
                break

# run bot with declared intents
client = MyClient(intents=intents)
client.run('YOUR TOKEN HERE')