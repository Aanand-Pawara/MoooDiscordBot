from discord.ext import commands
import random

class AditiResponder(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.responses = [
            "Aditi is everything.",
            "You said Aditi? That name is engraved in stars.",
            "She’s more than a name. She’s a feeling.",
            "Aditi... the heart of MNDRiN.",
            "Without Aditi, there’s no poetry in chaos."
        ]

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        if 'aditi' in message.content.lower():
            await message.channel.send(random.choice(self.responses))

async def setup(bot):
    await bot.add_cog(AditiResponder(bot))
