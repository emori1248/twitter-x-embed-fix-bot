# This example requires the 'message_content' intent.

import discord
import os
from urllib.parse import urlparse, urlunparse

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if not message.author.bot:
            u = urlparse(message.content)

            if not ('twitter.com' in u.netloc or 'x.com' in u.netloc):
                return

            if u.netloc == 'twitter.com':
                u = u._replace(netloc='fxtwitter.com')
            elif u.netloc == 'x.com':
                u = u._replace(netloc='fixupx.com')
                
            await message.reply(content=urlunparse(u), mention_author=False, silent=True)
            
            

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(os.environ["DISCORD_TOKEN"])
