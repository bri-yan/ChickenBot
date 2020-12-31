from discord.ext import commands
import os


client = commands.Bot(command_prefix='!')


@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')


@client.command()
async def reload(ctx, extenstion):
    client.load_extension(f'cogs.{extenstion}')
    client.unload_extension(f'cogs.{extenstion}')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


try:
    token_file = open('token.txt', 'r')
    token = token_file.readline()
    token_file.close()
except (FileNotFoundError, FileExistsError):
    token = 'INSERT TOKEN HERE'

client.run(token)
