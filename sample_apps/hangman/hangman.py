import random
from hangman_words import words

hangman_draw = {0: ("   ",
                    "   ",
                    "   "),
                1: (" o ",
                    "   ",
                    "   "),
                2: (" o ",
                    " | ",
                    "   "),
                3: (" o ",
                    "/| ",
                    "   "),
                4: (" o ",
                    "/|\\",
                    "   "),
                5: (" o ",
                    "/|\\",
                    "/  "),
                6: (" o ",
                    "/|\\",
                    "/ \\")}

# for i in hangman_draw:
#   for line in hangman_draw[i]:
#     print(line)

def display_man(wrong_answer):
  for line in hangman_draw[wrong_answer]:
    print(line)
  pass

def display_hint(hint):
  print(" ".join(hint))

def display_answer(answer):
  print(" ".join(answer))

def main():
  guessed_letters = set()
  is_run = True
  answer = random.choice(words)
  print(answer)
  hint = ["_"] * len(answer)
  wrong_answer = 0
  display_hint(hint)

  while is_run:
    guess = input("알파벳을 입력하여 주세요: ").lower()
    if (len(guess) != 1) or not(guess.isalpha()):
      print("알파벳 한글자 또는 알파벳만 입력하여 주세요")
      continue
    if guess in guessed_letters:
      print("이미 입력한 알파벳 입니다.")
      continue
    guessed_letters.add(guess)
    print(guessed_letters)

    if guess in answer:
      for i in range(len(answer)):
        if guess == answer[i]:
          hint[i] = guess
          print(hint)
    else:
      wrong_answer += 1
      display_man(wrong_answer)
    
    

    if "_" not in hint:
      print("정답입니다.")
      display_man(wrong_answer)
      display_answer(answer)
      is_run = False
    elif wrong_answer >= len(hangman_draw) - 1:
      print("죽었습니다.")
      display_man(wrong_answer)
      display_answer(answer)
      is_run = False

if __name__ == "__main__":
  main()