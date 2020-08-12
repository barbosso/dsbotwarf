import discord
from discord.ext import commands
import os
from random import choice

client = commands.Bot(command_prefix="!")

client.remove_command("help")

# Events
@client.event()
async def on_ready(self):
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('Warface'))
    print("Bot Online!")


@client.command()
@commands.has_permissions(administrator= True)
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")


@client.command()
@commands.has_permissions(administrator= True)
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")

@client.command()
@commands.has_permissions(administrator= True)
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f"cogs.{filename[:-3]}")


token = os.environ.get('BOT_TOKEN')

client.run(str(token))
