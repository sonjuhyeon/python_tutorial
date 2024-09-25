# 세계에서 가장 큰 대륙은
# a. 아시아
# b. 아프리카
# c. 유럽
# d. 남아메리카

# 인류 역사상 가장 오래된 문명은
# a. 이집트 문명
# b. 메소포타미아 문명
# c. 인도 문명
# d. 중국 문명

# 미국 대통령 중 가장 오랫동안 역임한 대통령은
# a. 조지 워싱턴
# b. 루즈벨트
# c. 링컨
# d. 프랭클린 피어스

# 레바논의 수도는
# a. 다마스쿠스
# b. 베이루트
# c. 아부다비
# d. 아마만

# 태양계의 행성 갯수는
# a. 6개
# b. 7개
# c. 8개
# d. 9개

# 정답 [a, b, b, b, c]

questions = ("세계에서 가장 큰 대륙은",
             "인류 역사상 가장 오래된 문명은",
             "미국 대통령 중 가장 오랫동안 역임한 대통령은",
             "레바논의 수도는",
             "태양계의 행성 갯수는")

options = (("a. 아시아", "b. 아프리카", "c. 유럽", "d. 남아메리카"),
           ("a. 이집트 문명", "b. 메소포타미아 문명", "c. 인도 문명", "d. 중국 문명"),
           ("a. 조지 워싱턴", "b. 루즈벨트", "c. 링컨", "d. 프랭클린 피어스"),
           ("a. 다마스쿠스", "b. 베이루트", "c. 아부다비", "d. 아마만"),
           ("a. 6개", "b. 7개", "c. 8개", "d. 9개"))

answers = ("a", "b", "b", "b", "c")
guesses = []
score = 0

num = 0

for question in questions:
  print("---------------------")
  print(question)
  for option in options[num]:
    print(option)
  
  guess = input("정답을 입력해 주세요. (a, b, c, d): ").lower()
  guesses.append(guess)

  if guess == answers[num]:
    score += 1
    print("정답 입니다!!")
  else:
    print("틀렸습니다.")
    print(f"정답은 {answers[num]}입니다.")

  num += 1

print("-------- 결과 --------")
print(f"당신은 {score}개의 문제를 맞췄습니다.")