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

debt1 = ["vay tien", "nap them tien", "hoan tat"]
debt = 0
count_debt = 0
def PaytoWin(money) :
    tiennap = int(input("ban muon nap bao nhieu: $"))
    print(f"so du moi cua ban la: {tiennap + money}")
    return tiennap + money
def Debt(money, vay) :
    money += vay
    return money

money = 0
print("pay your money to me")
money = PaytoWin(money)

while True:
    T = False # false neu la xiu
    tien_cuoc = float(input("Tien dat cuoc: $"))
    while(tien_cuoc < 0 or tien_cuoc > money):
        print("Tien dat cuoc khong hop le")
        tien_cuoc = float(input("Tien dat cuoc: $"))
    dices = []
    total = 0
    #numbers_of_dice = int(input("How many dice do you want? "))
    choose_tai_xiu = input("choose tai xiu: ").lower().strip()
    for die in range(3):
        dices.append(random.randint(1, 6))

    # for die in range(numbers_of_dice):
    #     for line in dice_art.get(dice[die]):
    #         print(line)

    for line in range(5):
        for dice in dices:
            print(dice_art.get(dice)[line], end="")
        print()

    for dice in dices:
        total += dice
    nha_cai_choose = "xiu"
    if total > 10:
        nha_cai_choose = "tai"

    # xử lý phaafn in tiền và tính tiền
    print(f"total {total} -> {nha_cai_choose}")
    if (choose_tai_xiu == nha_cai_choose):
        print(f"Chuc mung ban! -> ban nhan duoc {tien_cuoc}$ vao tai khoan")
        money += tien_cuoc
        print(f"tien cua ban hien tai la {money}")
    else:
        print(f"xin chia buon cung ban! tai khoan cua ban -{tien_cuoc}$")
        money -= tien_cuoc
        print(f"tien cua ban hien tai la {money}")
    choice = input("Press any key to continue...(y/n): ").lower().strip()
    if choice != "y":
        print("ban co muon thanh toan so tien ma ban da no? ")
        print("1. yes")
        print("2. no")

        pay = int(input("Choose your option: "))
        if pay == 1:

            print(f"so tien con lai cua ban {money}")
            pay_1 = int(input("nhap so tien ma ban muon tra: $"))
            print("thanh toan thanh cong!")
            money -= pay_1
            debt -= pay_1
        break

    # vay de choi
    if money <= 0:
        print("Tai khoan cua ban khong du de tiep tuc choi")
        print("some options: ")
        for i in range(3):
            print(f"{i + 1}. {debt1[i]}")

        while True:
            lc = int(input("Choose your option: "))
            if lc == 1:
                v = int(input("nhap so tien ma ban muon vay: $"))
                money = Debt(money, v)
                debt += v
                count_debt += 1
            elif lc == 2:
                money = PaytoWin(money)
            else:
                break


print("thong tin cua player sau khi choi: ")
print(f"so du con lai cua ban la: ${money}")
print(f"so tien con vay la ${debt}")

