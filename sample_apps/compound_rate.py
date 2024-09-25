# compound interest calculator : Compound interest calculator는 원금(principal)과 이자가 누적되어 이자에 이자가 붙는 방식으로 계산되는 복리(Compound Interest)를 계산하는 도구입니다. 복리 계산은 다음과 같은 수식을 사용합니다:

# [ A = P * (1 + r / n)^t ]

# ( A )는 최종 금액 (원금 + 이자)
# ( P )는 초기 원금 (Principal)
# ( r )는 연이율 (Annual interest rate, 소수로 표현)
# ( n )는 연간 복리 계산 횟수 (Compounding frequency per year)
# ( t )는 시간 (연 단위, Time in years)

# 1. 변수 초기화
principal = 0 # 원금
rate = 0 # 연이율
time = 0 # 시간

# 2 원금 입력
# while True:
#   principal = input("원금을 입력해 주세요: ")

#   try:
#     principal = float(principal)
#   except ValueError:
#     print(f"{principal}은 문자 입니다. 숫자로 입력해 주세요")
#     continue

#   if principal <= 0:
#     print("원금은 0보다 커야 합니다.")
#   else:
#     break

# # 3. 연이율 입력
# while True:
#   rate = input("연이율을 입력해 주세요: ")

#   try:
#     rate = float(rate) / 100
#   except ValueError:
#     print(f"{rate}은 문자 입니다. 숫자로 입력해 주세요")
#     continue

#   if rate <= 0:
#     print("연이율은 0보다 커야 합니다.")
#   else:
#     break

# # 4. 시간 입력
# while True:
#   time = input("시간을 입력해 주세요: ")

#   try:
#     time = float(time)
#   except ValueError:
#     print(f"{time}은 문자 입니다. 숫자로 입력해 주세요")
#     continue

#   if time <= 0:
#     print("시간은 0보다 큰 값이어야 합니다.")
#   else:
#     break


# 2 원금 입력
def get_compound_rate(message):
  while True:
    value = input(f"{message}: ")

    try:
      value = float(value)
    except ValueError:
      print(f"{value}은 문자 입니다. 숫자로 입력해 주세요")
      continue

    if value <= 0:
      print("원금은 0보다 커야 합니다.")
    else:
      # if "이자율" in message:
      #   value = value / 100
      break
  return value

principal = get_compound_rate("원금을 입력해 주세요")
rate = get_compound_rate("이자율을 입력해 주세요")
time = get_compound_rate("예금 기간을 입력해 주세요")

# 5. 복리 계산
# [ A = P * (1 + r / n)**t ]
# pow() : pow(x, y) - x의 y제곱
total = principal * pow((1 + rate / 100), time)
print(f"당신이 예금한 원금은 {principal}원이며, {time}년 후에 받게 될 금액은 {total}원 입니다.")
# print(principal)
# print(rate)
# print(time)
# print(total)