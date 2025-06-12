# MNDRiN Discord Bot

A modular, well-structured Discord bot developed specifically for the **MNDRiN Server**.  
This bot provides hybrid command support, styled interactions, and real-time responsiveness. It is deployed on **Render** and maintained using **UptimeRobot** for continuous uptime.

---

## Features

- ✅ **Hybrid Command System**  
  Supports both prefix and slash (`/`) commands using `discord.ext.commands` and application command trees.

- 🧠 **Custom Responses with Personality**  
  The bot replies with styled embeds and messages tailored to the tone of the MNDRiN server — raw, direct, and honest.

- 🎨 **Embedded Messaging**  
  Interactive, formatted messages using Discord's embed system for cleaner presentation.

- 🕵️ **Ephemeral Support**  
  Optional ephemeral replies to ensure clean channels and private interactions.

- ⚙️ **Modular Architecture**  
  Built using a cog-based structure, making it easy to extend or modify individual functionalities.

- 🔄 **Typing Simulation**  
  Realistic `ctx.typing()` effects to simulate thought before sending replies.

---

## Deployment

### Hosting Platform: [Render](https://render.com/)

- The bot is deployed as a **background worker** service or a **web service** with a lightweight Flask server to allow pings.
- Code is automatically pulled from GitHub and deployed via Render’s CI/CD system.
- Environment variables are managed securely within the Render dashboard.

### Keep-Alive Strategy: [UptimeRobot](https://uptimerobot.com/)

- A minimal Flask web server runs alongside the bot, exposing a root (`/`) endpoint.
- UptimeRobot pings this endpoint every 5 minutes to prevent Render from idling, ensuring near 24/7 availability.

---

## Getting Started (Local Development)

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/mndrin-discord-bot.git
cd mndrin-discord-bot
