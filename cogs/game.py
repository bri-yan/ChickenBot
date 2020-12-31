import random
import asyncio
from discord.ext import commands
from library.functions import *
from classes.player import Player
from classes.chicken import Chicken


class Game(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.players = {}

    # On-Ready Message
    @commands.Cog.listener()
    async def on_ready(self):
        print("Ready!")

    async def assign_chicken(self, ctx, player: Player):
        # await ctx.send(file=discord.File(f"players\\{ctx.author}\\eggs.png"))
        await ctx.send(":egg: :egg: :egg:")
        # Await a response. Timeout 30s
        choice = ""
        while not choice.lower() == "left" and not choice.lower() == "middle" and not choice.lower() == "right":
            try:
                await ctx.send(f"{ctx.author.mention} choose an egg: [Left] [Middle] [Right]")
                response = await self.client.wait_for('message',
                                                      check=lambda message: message.author == ctx.author,
                                                      timeout=30)
                choice = response.content
            except asyncio.TimeoutError:
                # TODO: figure out what to do when no chicken selected
                choice = 'left'
        # Ask player to assign a name to chicken, otherwise a random name will be assigned. Timeout 30s
        try:
            await ctx.send(f"{ctx.author.mention} Enter a name for your egg.")
            response = await self.client.wait_for('message', check=lambda message: message.author == ctx.author,
                                                  timeout=30)
            name = response.content
        except asyncio.TimeoutError:
            name = random.choice(chicken_names)
        chicken = Chicken(name)
        chicken.initialize()
        player.party.add_chicken(chicken)

        await ctx.send(f"Say hello to {name}!")
        return chicken

    @commands.command()
    async def chicken(self, ctx):
        player_key = str(ctx.author)
        if player_key not in self.players:
            player = Player(ctx.author)
            self.players[player_key] = player
            await self.assign_chicken(ctx, player)
        else:
            player = self.players[player_key]
            if player.limit > len(player.party):
                await self.assign_chicken(ctx, player)
            else:
                await ctx.send(player.party_display())

    @commands.command()
    async def encounter(self, ctx):
        pass

    @commands.command()
    async def test(self, ctx):
        player = self.players.get(str(ctx.author))
        if player is None:
            return
        else:
            await ctx.send(player.party[0].health_display())
            player.party[0].lose_health(3)


def setup(client):
    client.add_cog(Game(client))
