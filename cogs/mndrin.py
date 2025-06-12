from discord.ext import commands
import random

class MNDRiNResponder(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.responses = [
            "MNDRiN is in the lab. He’ll return when the fire cools.",
            "He's not gone. He’s building something bigger.",
            "MNDRiN is silent when the world is too loud. But he’s listening.",
            "He said he’d finish the mod. Nothing else matters.",
            "Behind every line of code... there's intent.",
            "He’ll be back. The build isn’t complete yet.",
            "MNDRiN left notes in the source. All of them end in truth.",
            "Working on the mod. Not for fame, just to prove a point.",
            "MNDRiN doesn’t rest. Not until the game reflects the vision.",
            "They think he vanished. No. He’s rewriting reality.",
            "You don’t summon MNDRiN. You wait.",
            "Rebuilding the world, one bugfix at a time.",
            "Version control is under control. MNDRiN knows.",
            "The terminal glows green. He’s alive in the lines.",
            "Silence isn’t absence. It’s development mode.",
            "He logs off, but the server still runs.",
            "There’s no changelog. MNDRiN changes everything.",
            "Every crash report is a message. He reads them all."
        ]

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        content_lower = message.content.lower()
        MNDRIN_ID = 492199252106280981  # replace with your actual user ID
        mentioned = any(user.id == MNDRIN_ID for user in message.mentions)


        if 'mndrin' in content_lower or mentioned:
            await message.channel.send(random.choice(self.responses))

async def setup(bot):
    await bot.add_cog(MNDRiNResponder(bot))
