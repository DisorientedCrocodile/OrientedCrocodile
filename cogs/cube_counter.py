import discord
from discord.ext import commands


class CubeCounter(commands.Cog, name="CubeCounter"):
    def __init__(self, client):
        self.client = client
        with open("cogs/cube.txt", "r") as f:
            l = f.readlines()
            self.cubenum = int(l[0].strip())

    @commands.command(aliases=["cube++"])
    async def cubeplusplus(self, ctx):
        self.cubenum += 1
        with open("cogs/cube.txt", "w") as f:
            f.write(str(self.cubenum))
        await ctx.send(f"Portal can be very evil sometimes. The total is {self.cubenum}")

    @commands.command()
    async def cubeset(self, ctx, cubenum_new:int):
        with open("cogs/cube.txt", "w") as f:
            f.write(str(self.cubenum))
        self.cubenum = cubenum_new
        await ctx.send(f"Set the total to {self.cubenum}")

    @commands.command()
    async def cubetotal(self, ctx):
        await ctx.send(f"Total is {self.cubenum}")


def setup(client):
    client.add_cog(CubeCounter(client))
    print("CubeCounter is loaded")
