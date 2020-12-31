from library.classes import *

chicken_names = ['Albert Eggstein', 'Attila the Hen', 'Big Bird', 'Chicken Little', 'Cluck Norris', 'Hen Solo',
                 'Henneth Paltrow', 'Nugget', 'Eggspreso', 'Mother Clucker', 'Princess Lay-a',
                 'Chickira', 'Hennifer Lopez', 'Lil Peep', 'Clarence']


async def get_player(self, ctx) -> Player:
    player_key = str(ctx.author)
    if player_key not in self.players:
        await ctx.send("Enter [!chicken] to get a chicken")
    return self.players.get(player_key)


