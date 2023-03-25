# base example code taken from discord.py docs

import discord
from discord.ext import commands
from discord import Permissions

description = ""

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="TBD", description=description, intents=intents)

forbidden_words = ["fuck", "shit", "bitch", "whore", "nigga", "nigger", "cunt", "pussy", "fag"]

class MyClient(discord.Client):
    async def on_ready(self):
        await client.change_presence(status=discord.Status.dnd, activity=discord.Game('Watching Ault and Bowswa\'s msgs'))
        print(f'Logged on as {self.user}!')

    @bot.event
    async def on_message(self, message):
        # to make sure bot does not reply to itself
        if message.author.id == self.user.id:
            return
        
        for bannedWord in forbidden_words:
            if (str(message.content)).find(bannedWord) != -1:
                print(f'Message from {message.author}: {message.content}')
                await ctx.send(f"{message.author} watch your language.")
                # await message.reply(f"{message.author} watch your language.", mention_author=True)
                break



client = MyClient(intents=intents)
client.run('TOKEN')