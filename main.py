from keep_alive import keep_alive
import discord
from discord.ext import commands
import os
import traceback
import asyncio

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)


cogs = ["cogs.commands", "cogs.auto_reply", "cogs.aditi", "cogs.mndrin", "cogs.help_navigator"]

async def load_extensions():
    for cog in cogs:
        try:
            await bot.load_extension(cog)
            print(f"[✔] Loaded cog: {cog}")
        except Exception:
            print(f"[✘] Failed to load cog: {cog}")
            traceback.print_exc()

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user} (ID: {bot.user.id})")
    try:
        synced = await bot.tree.sync()
        print(f"✅ Synced {len(synced)} slash commands.")
    except Exception:
        print("❌ Failed to sync slash commands:")
        traceback.print_exc()



keep_alive()

async def main():
    await load_extensions()
    try:
        await bot.start(os.environ['TOKEN'])
    except Exception:
        print("[✘] Bot failed to start:")
        traceback.print_exc()

asyncio.run(main())
