class Item:
    def __init__(self, name, rank):
        self.name = name
        self.rank = rank


class Gun(Item):
    def __repr__(self):
        return f"{self.rank}* Gun: {self.name}"


class Weapon(Item):
    def __repr__(self):
        return f"{self.rank}* Weapon: {self.name}"
