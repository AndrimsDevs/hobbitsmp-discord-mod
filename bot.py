# base example code taken from discord.py docs

import discord

forbidden_words = ["fuck", "shit", "bitch", "whore", "nigga", "nigger", "cunt", "pussy", "fag"]

class MyClient(discord.Client):
    async def on_ready(self):
        await client.change_presence(status=discord.Status.dnd, activity=discord.Game('Watching Ault and Bowswa\'s msgs'))
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        for bannedWord in forbidden_words:
            if (str(message.content)).find(bannedWord) != -1:
                print(f'Message from {message.author}: {message.content}')
                break

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('TOKEN')