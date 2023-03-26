# base example code taken from discord.py docs

import discord
from discord.ext import commands
from discord import Permissions

description = ""

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="TBD", description=description, intents=intents)

forbidden_words = ["fuck", "shit", "bitch", "whore", "nigga", "nigger", "cunt", "pussy", "fag"]

def notifDiscord(wordToRaise, messageAuthor, messageLink):
    import requests

    # Define the webhook URL and payload data
    webhook_url = "https://discord.com/api/webhooks/1089343268782882956/k7FwrQirM_BP_WSAxwStVMnGGa44LHgnJUV3uBj92nfHJq0xCLoNXCy0yBdbxDUUqAyt"
    payload = {
        "content": "Flag Inbound",
        "username": "Owner Word Flagging",
        "avatar_url": "https://my-bot-avatar-image-url.com/avatar.png",
        "embeds": [
            {
                "title": "flag ig",
                "description": "test",
                "color": 16711680, # RGB color code (decimal) - red in this example
            }
        ]
    }

    # Send the webhook using the requests library
    response = requests.post(webhook_url, json=payload)

    # Check the response status code to see if the webhook was successful
    if response.status_code == 200:
        print("Webhook sent successfully!")
    else:
        print("Error sending webhook:", response.status_code)


class MyClient(discord.Client):
    async def on_ready(self):
        await client.change_presence(status=discord.Status.dnd, activity=discord.Game('Watching Ault and Bowswa\'s msgs'))
        print(f'Logged on as {self.user}!')

    @bot.event
    async def on_message(self, message):
        # to make sure bot does not reply to itself
        if message.author.id == self.user.id or message.author.id == "1089343268782882956":
            return
        
        if message.channel.id == "1089046162956370040":
            return
        
        for bannedWord in forbidden_words:
            if (str(message.content)).find(bannedWord) != -1:
                print(f'Message from {message.author}: {message.content}')
                # await ctx.send(f"{message.author} watch your language.")
                notifDiscord(bannedWord, message.author, message.content)
                await message.reply(f"{message.author} watch your language.", mention_author=True)
                break

client = MyClient(intents=intents)
client.run('TOKEN')