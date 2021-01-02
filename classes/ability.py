class Ability:
    def __init__(self, name: str, type_: str, power: int, accuracy: int, effect: str = None):
        self.name = name
        self.type = type_
        self.power = power
        self.accuracy = accuracy
        self.effect = effect



