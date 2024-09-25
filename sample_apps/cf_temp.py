# 1. 입력 문자를 받는다. (c or f) - 대문자든 소문자든 상관없이 받는다
unit = input("변환할 온도 체계를 입력해 주세요 (c 또는 f): ").lower()

# 2. 입력 문자가 c 또는 f가 아니면 둘 중 하나만 입력하라고 출력한다.
if unit != "c" and unit != "f":
  print("c 또는 f만 입력해 주세요.")
  exit()

# 3. 온도를 입력 받는다. (초기화 변수가 필요함)
c_or_f = ""
temp = input("온도를 입력해 주세요: ")

# 4. 입력 받은 온도가 숫자가 아닌지 확인하고, 아니라면 숫자를 입력하라고 주문한다.
try:
  temp = float(temp)
except ValueError:
  print(f"{temp}은 문자 입니다. 숫자로 입력해 주세요")
  exit()

# 5. 입력 받은 문자가 c 이면 화씨로 변환하고, f 이면 섭씨로 변환한다.
if unit == "c":
  c_or_f = "화씨"
  # [°F] = [°C] × 1.8 + 32
  temp = (temp * 1.8) + 32
elif unit == "f":
  c_or_f = "섭씨"
  # [°C] = ([°F] − 32) / 1.8
  temp = (temp - 32) / 1.8

# 6. 변환된 온도를 출력한다.
print(f"입력하신 변환 온도는 {c_or_f} {temp}도 입니다.")