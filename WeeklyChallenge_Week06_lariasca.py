
# Weekly Challenge 6
# CX Programming Club
# lariasca
# Name Game
sample = ['Goblin', 'Creature', 'Troll', 'King/Queen', 'Witch/Warlock',
          'Vampire', 'Guardian', 'Fairy', 'Knight', 'Elf', 'Assasin',
          'Sorcerer/Sorceress', 'Giant', 'Warewolf', 'Wizard', 'Ogre',
          'Goblin', 'Beast', 'Dragon', 'Ghost', 'Dwarf', 'Giant', 'Unicorn',
          'Warrior', 'Spirit', 'Thief', 'Cyclops', 'Troll', 'Orc', 'Vampire']
villains = set(sample)
villains_map = dict()
counter = 0
for let in range(97, 122):
    villains_map[chr(let)] = villains[counter]
    counter += 1
print(villains_map)
