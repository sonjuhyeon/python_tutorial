# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")
# ● ┌ ─ ┐ │ └ ┘
import random

dice_block = {
  1: ("┌───────┐",
      "│       │",
      "│   ●   │",
      "│       │",
      "└───────┘"),
  2: ("┌───────┐",
      "│ ●     │",
      "│       │",
      "│     ● │",
      "└───────┘"),
  3: ("┌───────┐",
      "│ ●     │",
      "│   ●   │",
      "│     ● │",
      "└───────┘"),
  4: ("┌───────┐",
      "│ ●   ● │",
      "│       │",
      "│ ●   ● │",
      "└───────┘"),
  5: ("┌───────┐",
      "│ ●   ● │",
      "│   ●   │",
      "│ ●   ● │",
      "└───────┘"),
  6: ("┌───────┐",
      "│ ●   ● │",
      "│ ●   ● │",
      "│ ●   ● │",
      "└───────┘"),
}

dice = []
total = 0

num_of_dice = input("주사위 던질 횟수를 입력하세요: ")
while not(num_of_dice.isdigit()):
  num_of_dice = input("입력값이 잘못 되었습니다. 주사위 던질 횟수를 입력하세요: ")
num_of_dice = int(num_of_dice)

for i in range(num_of_dice):
  dice.append(random.randint(1, 6))

print(dice)

for i in dice:
  total += i
  for line in dice_block[i]:
    print(line)

print(f"주사위의 합읜 {total}입니다.")