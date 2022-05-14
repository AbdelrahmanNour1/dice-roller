import random


def roll_dice(rolls):
    for i in range(0, rolls):
        dice = str(random.randint(1, 6))
        print(dice)
    menu()


def menu():
    print("1. Roll One Die         ")
    print("2. Roll Multiple  Dice ")
    print(".......................")
    print("3. Exit Program")
    choice = int(input("Enter here: "))
    print()

    if choice == 1:
        roll_dice(1)
    if choice == 2:
        rolls = int(input("How many rolls: "))
        roll_dice(rolls)
    if choice == 3:
        exit()


menu()

