import random

def roll_dice():
    dice_face = {
        1: "⚀",
        2: "⚁",
        3: "⚂",
        4: "⚃",
        5: "⚄",
        6: "⚅"
    }
    return random.randint(1, 6)

print("\n    🎲 Dice Rolling Simulator 🎲")
while True:
    input("\nPress Enter to roll the dice...")
    value = roll_dice()
    print(f"You rolled a {value} {['','⚀','⚁','⚂','⚃','⚄','⚅'][value]}")

    again = input("Roll again? (y/n): ").strip().lower()
    if again != 'y':
        print("\n Thanks for playing 😇👏!")
        break