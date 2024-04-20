# bot.py
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from jerome import do_chat_jerome, set_up_jerome

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
print(TOKEN)

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

client = discord.Client(intents=intents)
@bot.command(name="Jerome")
async def say(ctx, *args):
    print(args)
    result = do_chat_jerome(" ".join(args))
    await ctx.send(result)


def start_bot():
    global TOKEN
    bot.run(TOKEN)


if __name__ == "__main__":
    set_up_jerome()
    start_bot()
