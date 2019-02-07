import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
        
class Person:
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.name = name
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.items = items
        self.actions = ["Attack", "Magic", "Items"]

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp
    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp
    def get_hp(self):
        return self.hp
    def get_maxhp(self):
        return self.maxhp
    def get_mp(self):
        return self.mp
    def get_maxmp(self):
        return self.maxmp
    def reduce_mp(self, cost):
        self.mp -= cost
    def reduce_item_quantity(self, i):
        self.items[i]['quantity'] -= 1
    def choose_action(self):
        i = 1
        for item in self.actions:
            print(str(i) + ":", item)
            i += 1

    def choose_spell(self):
        magic_choice = self.choose_random_target(len(self.magic))
        spell = self.magic[magic_choice]
        dmg = spell.generate_damage()
        cost = spell.cost
        pct = int((self.hp / self.maxhp) * 100)
        if self.mp < cost or spell.type == "white" and pct > 50:
            self.choose_spell()
        else:
            return (spell, dmg)
    def choose_magic(self):
        i = 1
        for spell in self.magic:
            print(str(i) + ":", spell.get_name(), "cost: ", str(spell.get_cost()))
            i += 1
    def choose_item(self):
        i = 1
        for item in self.items:
            print(str(i) + ":", item['item'].name, "description: ", item['item'].description, " [x" + str(item['quantity']) + "]")
            i += 1
    def choose_random_target(self, length):
        return random.randrange(0, length)
    def choose_target(self, enemies):
        i = 1
        for enemy in enemies:
            print(str(i) + ":", enemy.name)
            i += 1
        return int(input("Choose Target: ")) - 1
    def render_bar(self, bar, p, p_max):
        bar_length = len(bar)
        bar_ticks = int((p / p_max) * bar_length)
        new_bar = ""
        new_bar = "█" * bar_ticks
        new_bar += " " * (bar_length - bar_ticks)
        return new_bar
    def show_stats(self):
        hp_bar = self.render_bar("███████████████████", self.hp, self.maxhp)
        mp_bar = self.render_bar("███████", self.mp, self.maxmp)
        print("Name               HP                                MP")
        print(self.name + ":   " + str(self.hp) + "/" + str(self.maxhp) + "  |" + hp_bar + "|    " + str(self.mp) + "/" + str(self.maxmp) + " |" + mp_bar + "|")