import discord
from discord.ext import commands


class Help(commands.Cog, name="Help"):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def crochelp(self, ctx):
        emb = discord.Embed(title="My commands",
                            description="Commands for OrientedCrocodile",
                            color=discord.Color.green())
        emb.add_field(name="croc-cube++", value="Adds 1 to the cube number")
        emb.add_field(name="croc-cubeset [number]", value="Sets cube number to [number]")
        emb.add_field(name="croc-cubetotal", value="Prints out the cube number")
        emb.add_field(name="croc-portal++", value="Adds 1 to the portalboost number")
        emb.add_field(name="croc-portalset [number]", value="Sets portalboost number to [number]")
        emb.add_field(name="croc-portaltotal", value="Prints out the portalboost number")
        emb.add_field(name="croc-crochelp", value="What do you think?")

        await ctx.send(embed=emb)


def setup(client):
    client.add_cog(Help(client))
    print("Help is loaded")
