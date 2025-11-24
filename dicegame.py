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

def PaytoWin(money) :
    tiennap = int(input("ban muon nap bao nhieu: $"))
    print(f"so du moi cua ban la: {tiennap + money}")
    return tiennap + money

money = 0
print("pay your money to me")
money = PaytoWin(money)

while True:
    T = False # false neu la xiu
    tien_cuoc = float(input("Tien dat cuoc: $"))
    while(tien_cuoc < 0 or tien_cuoc > money):
        print("Tien dat cuoc khong hop le")
        tien_cuoc = float(input("Tien dat cuoc: $"))
    dice = []
    total = 0
    #numbers_of_dice = int(input("How many dice do you want? "))
    choose_tai_xiu = input("choose tai xiu: ").lower().strip()
    for die in range(3):
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

    print(f"total {total} -> {"Tai" if total > 10 else "Xiu"}")
    if (choose_tai_xiu == "tai" and total > 10) or (choose_tai_xiu == "xiu" and total <= 10):
        print(f"Chuc mung ban! -> ban nhan duoc {tien_cuoc}$ vao tai khoan")
        money += tien_cuoc
        print(f"tien cua ban hien tai la {money}")
    else:
        print(f"xin chia buon cung ban! tai khoan cua ban -{tien_cuoc}$")
        money -= tien_cuoc
        print(f"tien cua ban hien tai la {money}")


    choice = input("Press any key to continue...(y/n): ").lower().strip()
    if choice != "y": break


