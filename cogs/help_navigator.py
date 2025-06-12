from discord.ext import commands
import discord

class HelpNavigator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help", help="Shows all available commands.")
    async def show_help(self, ctx):
        embed = discord.Embed(
            title="🧭 Command Center: MNDRiN Bot",
            description="Your command index. Sharp. Clean. Brutal.",
            color=discord.Color.from_str("#1abc9c")
        )

        embed.set_thumbnail(url=self.bot.user.display_avatar.url)

        embed.add_field(name="⚙️ `!ping`", value="Check bot latency.", inline=True)
        embed.add_field(name="💬 `!hi`", value="Simple greeting.", inline=True)
        embed.add_field(name="📡 `!status`", value="Bot system and operational status.", inline=True)
        embed.add_field(name="📘 `!help`", value="You're already here.", inline=True)

        embed.set_footer(text="MNDRiN Bot – Run with steel and silence.")
        view = discord.ui.View()
        view.add_item(discord.ui.Button(label="🎬 Main Channel", url="https://www.youtube.com/@MNDRiN", style=discord.ButtonStyle.link))
        view.add_item(discord.ui.Button(label="🎨 New Channel", url="https://www.youtube.com/@MNDRiN.", style=discord.ButtonStyle.link))

        await ctx.send(embed=embed, view=view)

async def setup(bot):
    await bot.add_cog(HelpNavigator(bot))
