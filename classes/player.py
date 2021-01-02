import discord
from library.world import world
from classes.graph import Vertex


class Player:
    def __init__(self, member: discord.Member, location: Vertex):
        self.member = member
        self.balance = 0
        self.limit = 1
        self.party = []
        self.world = world
        self.location = location

    def add_balance(self, amount):
        self.balance += amount

    def subtract_balance(self, amount):
        self.balance = max(self.balance - amount, 0)

    def locate(self):
        return self.location.name

    def search(self):
        return [destination.name for destination in self.world.neighbors(self.location)]

    def travel(self, destination: str) -> bool:
        if destination in self.search():
            location = self.world.get(destination)
            if location is not None:
                self.location = location
                return True
        return False
