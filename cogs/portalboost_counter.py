import discord
from discord.ext import commands


class PortalboostCounter(commands.Cog, name="PortalboostCounter"):
    def __init__(self, client):
        self.client = client
        with open("cogs/portalboost.txt", "r") as f:
            l = f.readlines()
            self.portalboostnum = int(l[0].strip())

    @commands.command(aliases=["portal++"])
    async def portalplusplus(self, ctx):
        self.portalboostnum += 1
        with open("cogs/portalboost.txt", "w") as f:
            f.write(str(self.portalboostnum))
        await ctx.send(f"Woah. That was weird. It just... launched you out. Total is {self.portalboostnum}")

    @commands.command()
    async def portalset(self, ctx, portalboostnum_new:int):
        self.portalboostnum = portalboostnum_new
        with open("cogs/portalboost.txt", "w") as f:
            f.write(str(self.portalboostnum))
        await ctx.send(f"Total is now {self.portalboostnum}")

    @commands.command()
    async def portaltotal(self, ctx):
        await ctx.send(f"Total of portalboosts is {self.portalboostnum}")


def setup(client):
    client.add_cog(PortalboostCounter(client))
    print("PortalboostCounter is loaded")
