# 잔액확인
# 1번 입력시 잔액 출력

# 입금
# 2번 입력시 입금 금액을 입력 받음
# 입금할 금액이 0보다 작거나 문자일 경우 예외처리

# 출금
# 3번 입력시 출금 금액을 입력 받음
# 출금할 금액이 0보다 작거나 문자일 경우 예외처리
# 출금할 금액이 잔액보다 클 경우 예외처리

# 종료
# 4번 입력시 프로그램 종료


# 메인 로직이 들어가는 함수
def main(balance):
  # 숫자 선택 로직
  select_num = input("잔액확인: 1, 입금: 2, 출금: 3, 종료: 4 -> ")
  while (not(select_num == "1" or select_num == "2" or select_num == "3" or select_num == "4")):
    select_num = input("입력 값이 잘못 되었습니다.\n잔액확인: 1, 입금: 2, 출금: 3, 종료: 4 -> ")
  # 숫자 선택 조건에 따른 함수 호출
  if select_num == "1":
    print(f"잔액: {balance}")
    return balance
  elif select_num == "2":
    deposit = input("입금할 금액을 입력하여 주세요: ")
    while (not(deposit.isdigit()) or deposit == "0"):
      deposit = input("입력값이 잘못 되었습니다. 입금할 금액을 입력해 주세요: ")
    deposit = int(deposit)
    balance += deposit
    return balance
  elif select_num == "3":
    while True:
      withdrawal = input("출금할 금액을 입력하여 주세요: ")
      while (not(withdrawal.isdigit())):
        withdrawal = input("입력값이 잘못 되었습니다. 출금할 금액을 입력해 주세요: ")
      if (int(withdrawal) > balance):
        print("계좌 잔액이 부족합니다.")
        continue
      else:
        withdrawal = int(withdrawal)
        balance -= withdrawal
        break
    return balance
  else:
    print("종료")
    return balance

balance = 1000
if __name__ == "__main__":
  balance = main(balance)

print(balance)