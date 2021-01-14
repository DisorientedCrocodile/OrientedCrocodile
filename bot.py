import discord
from discord.ext import commands
import sys

# link to bot: https://discord.com/api/oauth2/authorize?client_id=799235690314465341&permissions=3072&scope=bot


def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()


token = read_token()

client = commands.Bot(command_prefix="croc-")


@client.event
async def on_ready():
    print("poggers")
    return await client.change_presence(status=discord.Status.online, activity=discord.Game("with not breaking"))


initial_extensions = [
    'cogs.cube_counter'
]


if __name__ == "__main__":
    for extension in initial_extensions:
        try:
            client.load_extension(extension)
        except Exception as e:
            print("Failed to load extension", extension, e)


client.run(token)
