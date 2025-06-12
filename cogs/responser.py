import discord

class Responder:
    @staticmethod
    def embed(title: str, description: str, color=discord.Color.blurple()):
        return discord.Embed(
            title=title,
            description=description,
            color=color
        ).set_footer(text="Powered by MNDRiN")

    @staticmethod
    def greet(user: discord.User):
        embed = Responder.embed("👋 Greetings!", f"Hello {user.mention}, welcome!")
        embed.set_thumbnail(url=user.avatar)
        return embed

    @staticmethod
    def pong():
        return Responder.embed("🏓 Pong!", "The bot is alive.")

    @staticmethod
    def error(message: str):
        return Responder.embed("❌ Error", message, color=discord.Color.red())
