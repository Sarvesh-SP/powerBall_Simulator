import random

print("-" * 10 + "Power-Ball Simulator" + "-" * 10)

white_balls = int(
    input(("How many white-balls to draw from the 5 winning numbers (Normally 69): "))
)


red_balls = int(
    input("How many red-balls to draw from for the Power-Ball (Normally 26)")
)
if red_balls < 1:
    red_balls = 1


odds = 1

for x in range(5):
    odds *= white_balls - x

odds *= red_balls / 120

print(f"You have a 1 in {odds} chance of winning this lottery.")

# Get ticket interval.
ticket = int(input("Purchace tickets in what interval: "))

# Generate the winning lottery number.
win = []

while len(win) < 5:
    num = random.randint(1, white_balls)
    if num not in win:
        win.append(num)
win.sort()


powa = random.randint(1, red_balls)
win.append(powa)

print("\n" + "-" * 10 + "Welcome to the Power Ball" + "-" * 10)
print(f"\nTonight's Winning numbers are: ", end="")

for x in win:
    print(str(x), end=" ")


input("\nPress 'Enter' to begin purchasing tickets!!")

tickPur = 0
active = True
tickSold = []

while win not in tickSold and active == True:
    lottery = []
    while len(lottery) < 5:
        n = random.randint(1, white_balls)
        if n not in lottery:
            lottery.append(n)
    lottery.sort()

    num = random.randint(1, red_balls)

    lottery.append(num)

    if lottery not in tickSold:
        tickPur += 1
        tickSold.append(lottery)
        print(lottery)
    else:
        print("Losing ticket generated, disregard...")

    if tickPur % ticket == 0:
        print(f"{tickPur} tickets purchased so far with no winners...")
        ch = input("\nKeep purchasing tickets(y/n): ").lower()
        if ch != "y":
            active = False


if lottery == win:
    print("\nWinning ticket numbers: ", end="")
    for x in lottery:
        print(f"{x}", end=" ")

    print(f"\nPurchased a total of {tickPur} tickets.")

else:
    print(f"\nYou bought {tickPur} tickets and still lost!")
    print("Better luck next time!")
