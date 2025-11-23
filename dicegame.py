import random
from random import choice

# print("\u25CF\u250C\u2500\u2510\u2502\u2514\u2518")
#● ┌ ─ ┐│└ ┘

# "┌─────────┐"
# "│         │"
# "│         │"
# "│         │"
# "└─────────┘"

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│ ●       │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│ ●       │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│ ●     ● │",
        "│         │",
        "│ ●     ● │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│ ●     ● │",
        "│    ●    │",
        "│ ●     ● │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│ ●     ● │",
        "│ ●     ● │",
        "│ ●     ● │",
        "└─────────┘"),
}

while True:
    dice = []
    total = 0
    numbers_of_dice = int(input("How many dice do you want? "))

    for die in range(numbers_of_dice):
        dice.append(random.randint(1, 6))

    # for die in range(numbers_of_dice):
    #     for line in dice_art.get(dice[die]):
    #         print(line)

    for line in range(5):
        for die in dice:
            print(dice_art.get(die)[line], end="")
        print()

    for dice in dice:
        total += dice
    print(f"total {total}")
    choice = input("Press any key to continue...(y/n): ").lower().strip()
    if choice != "y": break


