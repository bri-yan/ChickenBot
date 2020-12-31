import discord


class Player:
    def __init__(self, member: discord.Member):
        self.member = member
        self.balance = 0
        self.limit = 1
        self.party = []

    def add_balance(self, amount):
        self.balance += amount

    def subtract_balance(self, amount):
        self.balance = max(self.balance - amount, 0)
