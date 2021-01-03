import random


def paralyze() -> bool:
    if random.random() <= 0.25:  # chance that chicken is paralyzed this turn
        return True
    return False


def sleep() -> bool:
    return True


def frozen() -> bool:
    return True


def burn() -> bool:
    if random.random() <= 0.3:
        return True
    return False


def confuse() -> bool:
    if random.random() <= 0.3:
        return True
    return False


class Effect:
    def __init__(self, name: str, likelihood: int, remove: int):
        self.name = name
        self.likelihood = likelihood  # chance for ability (fire, ice, or electric type) to apply a status effect (burn, frozen, or paralyze)
        self.remove = remove  # chance to remove status effect
