wizard = "Wizard"
elf = "Elf"
human = "Human"
orc = "Orc"
wizard_hp = 70
elf_hp = 100
human_hp = 150
orc_hp = 80
wizard_damage = 150
elf_damage = 100
human_damage = 20
orc_damage = 40
dragon_hp = 300
dragon_damage = 50
while True:
    print("1) Wizard")
    print("2) Elf")
    print("3. Human")
    print("4. Orc")
    character = input("Choose your character:")
    if character == "1" or character == "Wizard":
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        break
    if character == "2" or character == "Elf":
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        break
    if character == "3" or character == "Human":
        character = human
        my_hp = human_hp
        my_damage = human_damage
        break
    if character == "4" or character == "Orc":
        character = orc
        my_hp = orc_hp
        my_damage = orc_damage
        break
    print("Unknown character")
print(character)
print("Health:", my_hp)
print("Damage:", my_damage)
while True:
    dragon_hp = dragon_hp - my_damage
    print("The", character, "damaged the Dragon!")
    print("The dragon has", dragon_hp, "hit points left")
    print()
    if dragon_hp <= 0:
        print("The Dragon has lost the battle!")
        print()
        break
    my_hp = my_hp - dragon_damage
    print("The Dragon has damaged the", character)
    print("The", character, "currently has", my_hp, "hit points")
    print()
    if my_hp <= 0:
        print("The", character, "has lost the battle!")
        break
