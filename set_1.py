# set은 중복되지 않은 요소들로만 구성된 집합 자료형이다.
# - 인덱스로 접근할 수 없다.
# - 내부 요소를 수정할 수 없다.
# - 중복된 요소를 포함할 수 없다.
# - 중복 데이터가 있을 경우 오류가 나지는 않지만 중복 데이터는 표현되지 않는다.
# - 중괄호를 사용한다. 
# - 순서가 없다.

a = {"apple", "banana", "cherry", 0, True, False}
# 실행 할때마다 순서가 바뀜
# True가 없어짐 : 1하고 중복되기 때문
# print(type(a))
# print(a)

# 셋의 길이
# print(len(a)) # 중복 데이터는 하나로 표현

# 생성자를 사용한 셋 생성
c = set(("a", "b", "c")) # 생성시 중괄호, 괄호 모두 사용 가능하며, 타입 역시 set으로 지정된다.
# print(c)
# print(type(c))

# 반복문으로 요소 확인
for i in a:
  # print(i)
  pass

# 요소 존재 여부 확인
if "apple" in a:
  # print(True)
  pass

# 존재 여부 변수 저장
d = "apple" in a
# print(d)

# add(): 요소를 추가하는 함수
a.add("orange")
# print(a)

# update(): 여러 요소를 한거번에 추가
b = {"kiwi", "melon", "grape"}
a.update(b)
# print(a)

# remove(): 요소를 삭제하는 함수
# a.remove("mango") # 없는 요소를 삭제하면 에러가 발생
# print(a)

# discard(): 요소를 삭제하는 함수
a.discard("mango") # 없는 요소를 삭제해도 에러가 발생하지 않는다.
# print(a)

# pop: 마지막 요소가 삭제되나, 순서가 없기 때문에 랜덤한 요소가 삭제된다고 봐야 한다.
a.pop()
print(a)