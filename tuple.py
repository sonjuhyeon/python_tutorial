# tuple : (a, b, c, ...)
# - 값을 변경할 수 없다
# - 중복 데이터를 허용한다
# - 순서를 가지고 있다
# - 데이터는 괄호를 사용한다(생략 가능)
# - 모든 타입을 요소로 지정할 수 있다

a = ("사과", "바나나", "포도", 1, True)
b = ("apple") # 요소가 하나일 때는 괄호가 없이 출력이 되며, 문자열로 인식
c = "배", "키위"

# print(a)
# print(b)
# print(c)
# print(type(a))
# print(type(b)) # 문자열
# print(type(c))

# 튜플의 접근
# print(a[0])

# 튜플의 길이
# print(len(a))

# 튜플의 생성자
d = tuple((1, 2, 'apple'))
# print(d)

# 튜플 범위 지정 접근
# print(a[1:3])

# 반복문으로 접근
for i in a:
  # print(i)
  pass

# if문으로 튜플에 값이 있는지 확인
if "사과" in a:
  # print("사과가 있습니다.")
  # print(True)
  pass

# 튜플의 값 변경 - 직접 변경은 오류가 발생한다. 리스트로 변경 후 다시 튜플로 변경한다.
# a[0] = "수박" # 에러 발생
# print(a) # 에러 발생

e = list(a)
# print(e)
pass

e[0] = "수박"
# print(e)
pass

f = tuple(e)
# print(f)
pass

# 증가 연산을 사용한 튜플 추가
a += ("체리", "키위", "수박")
# print(a)

# 구조분해 : unpacking
(a1, a2, a3, a4, a5, a6, a7, a8) = a
# print(a1)

# range() : 범위를 지정
# print(range(len(a)))

for i in range(len(a)):
  # print(a[i])
  pass

# 곱하기 연결 합치기
print(a * 2)