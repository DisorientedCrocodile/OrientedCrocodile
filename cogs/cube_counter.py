import discord
from discord.ext import commands


class CubeCounter(commands.Cog, name="CubeCounter"):
    def __init__(self, client):
        self.client = client
        self.cubenum = 0

    @commands.command(aliases=["cube++"])
    async def cubeplusplus(self, ctx):
        self.cubenum += 1
        await ctx.send(f"Portal can be very evil sometimes. The total is {self.cubenum}")

    @commands.command()
    async def cubeset(self, ctx, cubenum_new:int):
        self.cubenum = cubenum_new
        await ctx.send(f"Set the total to {self.cubenum}")

    @commands.command()
    async def cubetotal(self, ctx):
        await ctx.send(f"Total is {self.cubenum}")


def setup(client):
    client.add_cog(CubeCounter(client))
    print("CubeCounter is loaded")
