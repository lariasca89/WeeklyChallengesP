
# Weekly Challenge 6
# CX Programming Club
# lariasca
# Name Game

sample = ['Goblin', 'Creature', 'Troll', 'King/Queen', 'Witch/Warlock',
          'Vampire', 'Guardian', 'Fairy', 'Knight', 'Elf', 'Assasin',
          'Sorcerer/Sorceress', 'Giant', 'Warewolf', 'Wizard', 'Ogre',
          'Goblin', 'Beast', 'Dragon', 'Ghost', 'Dwarf', 'Giant', 'Unicorn',
          'Warrior', 'Spirit', 'Thief', 'Cyclops', 'Troll', 'Orc', 'Vampire']

villains = list(set(sample))
alpha = dict()
villain = 0
letter = 97

while letter <= 122:
    alpha[chr(letter)] = villains[villain]
    villain += 1
    letter += 1

string = "The Black,The Vengeful,The Dark,The Red,The Cursed,The Savage,The White,The Ugly,The Treacherous,The Blue,The Wicked,The Green"
descrip = list(string.split(","))

months = {'Jan': '', 'Feb': '', 'Mar': '', 'Apr': '', 'May': '', 'Jun': '',
          'Jul': '', 'Aug': '', 'Sep': '', 'Oct': '', 'Nov': '', 'Dec': ''}

month_list = list(months.keys())
months_numbers = dict()
value = 0

for key in months:
    months[key] = descrip[value]
    months_numbers[value+1] = month_list[value]
    value += 1

print('''Hola!... que bueno que estes de vuelta en Python.

Esta vez nos vamos a divertir mucho!!
Disculpa que te pregunte de nuevo, no tengo mucha memoria...:(''')

name = list(input("Me podrias repetir tu nombre?\n").lower())

print('''Oh...! pero claro ya recordé esa cara...
Te voy a ser muy honesto, tampoco recuerdo tu mes de nacimiento,
estar encerrado en casa me ha afectado la memoria.
Te juro que no vuelve a pasar, de hecho recuerdo mejor los números que los meses!''')

month = int(input("En que número de mes naciste?\n"))

# Map month and name received with dictionaries to build the villain name.

print(f'''Como haz sido muy paciente conmigo, te voy a dar algo único!
Te ves emocionado, ya no puedo soportarlo, te lo diré!
Quiero decirte tu nombre de VILLANO...!
Que es.....

¡¡¡{months[months_numbers[month]]} {alpha[name[0]]}!!!

Ahora que ya estas mas tranquilo puedes continuar con lo que hacias, hasta luego!!!\n''')

