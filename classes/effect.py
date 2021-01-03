import random
from classes.chicken import Chicken


def paralyze(chicken: Chicken) -> bool:
    if random.random() <= 0.25:  # chance that chicken is paralyzed this turn
        return True
    return False


def sleep(chicken: Chicken) -> bool:
    return True


def freeze(chicken: Chicken) -> bool:
    return True


def burn(chicken: Chicken) -> bool:
    if random.random() <= 0.3:
        return True
    return False


def confuse(chicken: Chicken) -> bool:
    if random.random() <= 0.3:
        return True
    return False


effects = {"paralyze": paralyze, "sleep": sleep}


class Effect:
    def __init__(self, name: str, infliction: int, effectiveness: int, persistence: int,
                 negates: bool, damages: bool, precedes: bool):
        self.name = name
        self.infliction = infliction  # chance for ability to inflict a status effect
        self.effectiveness = effectiveness  # chance for ability to impose a status effect
        self.persistence = persistence  # chance to keep status effect
        self.negates = negates
        self.damages = damages
        self.precedes = precedes

    def does_inflict(self) -> bool:
        return True if random.random() <= self.infliction else False

    def does_affect(self) -> bool:
        return True if random.random() <= self.effectiveness else False

    def does_persist(self) -> bool:
        return True if random.random() <= self.persistence else False
