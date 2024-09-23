import random

top_n = input("자연수를 입력하세요: ")

while not(top_n.isdigit()) or "0" == top_n:
  top_n = input("입력값이 자연수여야 합니다. 다시 입력해주세요: ")
top_n = int(top_n)

random_n = random.randint(1, top_n)
cnt = 0

while True:
  cnt += 1
  guess_n = input(f"1~{top_n}중 숫자를 입력하세요: ")
  while not(guess_n.isdigit()) or "0" == guess_n:
    guess_n = input("입력값이 자연수여야 합니다. 다시 입력해주세요: ")
  guess_n = int(guess_n)

  if guess_n > random_n:
    print("입력값이 큽니다.")
  elif guess_n < random_n:
    print("입력값이 작습니다.")
  else:
    print(f"{cnt}번째 만에 정답을 맞춰었습니다.")
    break