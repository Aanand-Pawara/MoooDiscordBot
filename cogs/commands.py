from discord.ext import commands
import discord
import asyncio

class CoreCommands(commands.Cog):
            def __init__(self, bot):
                self.bot = bot

            @commands.hybrid_command(name="ping", description="Check if the bot is alive")
            async def ping(self, ctx: commands.Context):
                """Responds with 'Pong!' to check bot's availability."""
                try:
                    await ctx.defer(ephemeral=True)
                    await ctx.reply("Pong!", ephemeral=True)
                except Exception as e:
                    print(f"[ping] Error: {e}")
                    await ctx.reply("An error occurred.", ephemeral=True)

            @commands.hybrid_command(name="greet", description="A warm greeting!")
            async def greet(self, ctx: commands.Context):
                """Sends a formatted greeting message to the user."""
                try:
                    await ctx.defer(ephemeral=True)

                    author_avatar = ctx.author.avatar.url if ctx.author.avatar else ctx.author.default_avatar.url
                    bot_avatar = self.bot.user.avatar.url if self.bot.user.avatar else self.bot.user.default_avatar.url

                    embed = discord.Embed(
                        title="👋 Greetings!",
                        description=f"Hello {ctx.author.mention}! Welcome to the server!",
                        color=discord.Color.gold()
                    )
                    embed.set_author(name=self.bot.user.name, icon_url=bot_avatar)
                    embed.add_field(name="Enjoy your stay!", value="Feel free to explore and have fun!", inline=False)
                    embed.set_thumbnail(url=author_avatar)
                    embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=author_avatar)

                    await ctx.reply(embed=embed, ephemeral=True)
                except Exception as e:
                    print(f"[greet] Error: {e}")
                    await ctx.reply("Something went wrong while greeting you.", ephemeral=True)

            @commands.hybrid_command(name="hi", description="Say hello")
            async def hi(self, ctx: commands.Context):
                """Says hello to the user with a short delay."""
                try:
                    await ctx.defer(ephemeral=True)
                    await asyncio.sleep(1)
                    await ctx.reply("Hello there!", ephemeral=True)
                except Exception as e:
                    print(f"[hi] Error: {e}")
                    await ctx.reply("Couldn't say hi. Try again.", ephemeral=True)

            @commands.command()
            async def love(self, ctx: commands.Context):
                """Sends a quote about love."""
                try:
                    await ctx.send("Love never dies. Only people do.")
                except Exception as e:
                    print(f"[love] Error: {e}")
                    await ctx.send("Couldn't express love. Something's wrong.")

            @commands.command()
            async def status(self, ctx: commands.Context):
                """Sends the bot's status in an embed."""
                try:
                    embed = discord.Embed(
                        title="🧠 MNDRiN System",
                        description="All systems green.",
                        color=0x1abc9c
                    )
                    embed.set_footer(text="Powered by brutal honesty.")
                    await ctx.send(embed=embed)
                except Exception as e:
                    print(f"[status] Error: {e}")
                    await ctx.send("Status failed. Check logs.")
                    
                    
async def setup(bot):
            try:
                await bot.add_cog(CoreCommands(bot))
            except Exception as e:
                print(f"[setup] Failed to add CoreCommands cog: {e}")
