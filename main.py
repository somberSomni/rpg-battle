from classes.game import Person, bcolors
from classes.magic import Spell
from classes.item import Item

# Create Black Magic
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thnder", 10, 200, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
meteor = Spell("Meteor", 40, 500, "black")
quake = Spell("Quake", 44, 440, "black")

# Create White Magic
cure = Spell("Cure", 12, 120, "white")
restore = Spell("Restore", 18, 200, "white")

# Create some Items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hi_potion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
super_potion = Item("Super Potion", "potion", "Heals 500 HP", 500)
elixer = Item("Elixer", "elixer", "Fully restores HP/MP of one parter member", 9999)
mega_elixer = Item("MegaElixer", "elixer", "Fully restores HP/MP", 9999)

grenade = Item("Grenade", "attack", "Deals 50 damage", 50)

player_spells = [fire, thunder, blizzard, meteor, cure, restore]
player_items = [{ 'item': potion, 'quantity': 4 },
                { 'item': hi_potion, 'quantity': 2 }, 
                { 'item': elixer, 'quantity': 2 },
                { 'item': mega_elixer, 'quantity': 2 },
                { 'item': grenade, 'quantity': 10 }]

enemy_spells = [meteor, blizzard, cure]
#instantiate player and enemy
player1 = Person("Virt", 8290, 200, 60, 34, player_spells, player_items)
player2 = Person("Artemis", 1460, 100, 60, 34, player_spells, player_items)
players = [player1, player2]
enemy1 = Person('Slime', 1200, 130, 560, 325, enemy_spells, [])
enemy2 = Person('Blazer', 20000, 600, 525, 25, enemy_spells, [])
enemies = [enemy1, enemy2]
running = True
while running:
    print("===============")
    print("\n\n")
    for player in players:
        player.show_stats()
    for enemy in enemies:
        enemy.show_stats()
    for player in players:
        print(player.name)
        player.choose_action()
        choice = int(input("Choose action: ")) - 1
        if choice == 0:
            dmg = player.generate_damage()
            target_choice = player.choose_target(enemies)
            enemy = enemies[target_choice]
            enemy.take_damage(dmg)
            print("You attacked " + enemy.name + " for", dmg, "points of damage. Enemy HP:", enemy.get_hp())
        elif choice == 1:
            player.choose_magic()
            magic_choice = int(input("Choose magic: ")) - 1
            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_damage()
            cost = spell.get_cost()
            spell_type = spell.get_type()
            current_mp = player.get_mp()

            if cost > current_mp:
                print("\nNot enough MP\n")
                continue
            else:
                player.reduce_mp(cost)
                current_mp = player.get_mp()
                if spell_type == "white":
                    player.heal(magic_dmg)
                    print("\n", player.name + " " + spell.name + " heals for", str(magic_dmg), "HP")
                elif spell_type == "black":
                    target_choice = player.choose_target(enemies)
                    enemy = enemies[target_choice]
                    enemy.take_damage(magic_dmg)
                    print("\n", player.name + " " + spell.name + " deals", str(magic_dmg), "points of damage")
                    
                print("\n", "Current MP: ", current_mp)
        elif choice == 2:
            player.choose_item()
            item_choice = int(input("Choose item: ")) - 1

            if item_choice == -1:
                continue
                
            new_item = player.items[item_choice]
            item = new_item['item']
            quantity = new_item['quantity']
            if quantity > 0 :
                if item.type == "potion":
                    player.heal(item.prop)
                    print("\n",player.name + " " + item.name + " heals for", str(item.prop), "HP")
                elif item.type == "elixer":
                    if item.name == "MegaElixer":
                        for each in players:
                            each.hp = each.maxhp
                            each.mp = each.maxmp
                    else: 
                        player.hp = player.maxhp
                        player.mp = player.mp
                    print("\n", item.name, item.description)
                elif item.type == "attack":
                    target_choice = player.choose_target(enemies)
                    enemy = enemies[target_choice]
                    enemy.take_damage(item.prop)
                    print("\n", player.name + " " + item.name + " deals", str(item.prop), "points of damage")

                player.reduce_item_quantity(item_choice)
            else: 
                continue             
        else:
            continue
        i = 0
        for enemy in enemies:
            if enemy.get_hp() == 0:
                print(enemy.name + " has been defeated")
                del enemies[i]
            else :
                enemy_choice = enemy.choose_random_target(2)
                enemy_target_choice = enemy.choose_random_target(len(players))
                enemy_target = players[enemy_target_choice]
                if enemy_choice == 0:
                    enemy_dmg = enemy.generate_damage()
                    enemy_target.take_damage(enemy_dmg)
                elif enemy_choice == 1:
                    enemy_spell, enemy_dmg = enemy.choose_spell()
                    enemy.reduce_mp(enemy_spell.cost)
                    spell_type = enemy_spell.get_type()
                    if spell_type == "white":
                        enemy.heal(enemy_dmg)
                        print("\n", enemy.name + " " + enemy_spell.name + " heals for", str(enemy_dmg), "HP")
                    elif spell_type == "black":
                        enemy_target.take_damage(enemy_dmg)
                        print("\n", enemy.name + " " + enemy_spell.name + " deals", str(enemy_dmg), "points of damage")
                        
                print("---------------------------")
                print(enemy.name + " HP:", str(enemy.get_hp()) + "/" + str(enemy.get_maxhp()))
                if enemy_target.get_hp() == 0:
                    print(enemy_target.name + " has been defeated")
                    del players[enemy_target_choice]
                else:
                    print("Player HP:", str(player.get_hp()) + "/" + str(player.get_maxhp()))
                    print("Player MP:", str(player.get_mp()) + "/" + str(player.get_maxmp()))
            i += 1
        if len(enemies) == 0:
            print("You Win")
            running = False
        elif len(players) == 0:
            print("Your Enemy had defeated you")
            running = False