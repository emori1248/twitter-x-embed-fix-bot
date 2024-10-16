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

            elif u.netloc == 'instagram.com':
                u = u._replace(netloc='ddinstagram.com')

            elif u.netloc == 'tiktok.com':
                u = u._replace(netloc='tnktok.com')
                
            # Delete the old user message in case a partially functioning embed is present
            await message.delete()

            # Append the redirected link to a formatted message to indicate the original author after their message is deleted
            content = message.author.mention + ": " + urlunparse(u)
            await message.channel.send(content, silent=True)
            
            

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(os.environ["DISCORD_TOKEN"])
