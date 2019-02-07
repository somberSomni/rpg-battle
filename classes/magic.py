import random

class Spell:
    def __init__(self, name, cost=10, dmg=50, spell_type="normal"):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.type = spell_type

    def generate_damage(self):
        low = self.dmg - 15
        high = self.dmg + 15
        return random.randrange(low, high)

    def get_name(self):
        return self.name
    def get_cost(self):
        return self.cost
    def get_type(self):
        return self.type