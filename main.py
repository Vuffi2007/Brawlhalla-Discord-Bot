import discord
import asyncio
import os
import dotenv
dotenv.load_dotenv()

intents = discord.Intents.default()
intents.members = True
intents.presences = True
intents.message_content = True
intents.guilds = True

bot = discord.Bot(intents=intents)

active_users = []

@bot.event
async def on_ready():
    print("Bot is ready")
    channel = bot.get_channel(1138762407649493047)
    while True:
        # Pings everyone when a user plays Brawlhalla
        await asyncio.sleep(5)
        for member in bot.get_all_members():
            if member.activity is not None and member.activity.name == "Brawlhalla" and member.id not in active_users:
                active_users.append(member.id)
                print(member.name, member.activity.name)
                await channel.send(f"{member.name} is playing Brawlhalla " + "<@&1159085509201645588>")
            elif (member.activity is None and member.id in active_users):
                active_users.remove(member.id)
                    

bot.run(os.getenv("BOT_TOKEN"))