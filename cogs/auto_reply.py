from discord.ext import commands
import time

from cogs.responser import Responder

class AutoReply(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.user_last_message = {}  # {user_id: (last_content, timestamp)}

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        content = message.content.lower()
        user_id = message.author.id
        now = time.time()

        last = self.user_last_message.get(user_id, ("", 0))

        # Cooldown: 3 seconds for same content
        if last[0] == content and now - last[1] < 10:
            return

        self.user_last_message[user_id] = (content, now)

        if 'hi' in content or 'hello' in content:
            await message.channel.send("Hey. What's up?")
        elif 'aanand' in content:
            await message.channel.send("shut up.")
        elif 'mod' in content:
            await message.channel.send("Mod is being worked on. Stay brutal.")
        elif 'update' in content:
            if any(role.name == "Admin" for role in message.author.roles):
                await message.channel.send("You're an Admin. You *know* we're working on it.")
            elif message.author.id == 492199252106280981:
                await message.channel.send("You're MNDRiN. No updates for you. You write them.")
            else:
                await message.channel.send("Update is being worked on. Stay brutal.")
        elif 'bye' in content:
            await message.channel.send(embed=Responder.error("Fuck"))

async def setup(bot):
    await bot.add_cog(AutoReply(bot))
