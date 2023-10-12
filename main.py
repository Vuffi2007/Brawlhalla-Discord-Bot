import discord
import asyncio
import os
import dotenv
dotenv.load_dotenv()

intents = discord.Intents.default()
intents.members = True
intents.presences = True

bot = discord.Bot(intents=intents)

@bot.event
async def on_ready():
    print("Bot is ready")
    while True:
        await asyncio.sleep(5)
        for member in bot.get_all_members():
            if not member.activity:
                continue
            print(member.name, member.activity.name)





bot.run(os.getenv("BOT_TOKEN"))