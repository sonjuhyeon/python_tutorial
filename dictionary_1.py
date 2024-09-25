# dictionary: 키와 값으로 이루어진 자료형으로 자바스크립트의 객체와 비슷하다.
# - 중복을 허용하지 않는다.
# - 순서가 없다.
# - key, value로 구성된다.

a = {
  "name": "marshall",
  "age": 20,
  "address": "Incheon",
  # "address": "Seoul",
  "gu": ["namgu", "bupyeunggu"]
}

# print(a)
# print(type(a))

# 요소의 접근은 키로 접근한다.
# print(a["name"])

# print(a["address"]) # 중복된 키가 있을 경우 마지막 값이 출력된다.

# 딕셔너리의 길이
# print(len(a)) # 중복된 키는 무시하고 계산한다.

# 리스트 값 멤버 요소 접근
# print(a["gu"][1])

# 생성자로 딕셔너리 생성
b = dict(name="marshall", age=20)
# print(b)
# print(type(b))

# get을 이용한 맴버 요소 접근
# print(a.get("name"))

# key값만 출력
# print(a.keys()) # 키 값을 리스트 형태로 반환

# 요소의 변경
a["age"] = 30
a.update({"name": "james"})
# print(a)

# 요소의 추가
a["color"] = ["red", "green", "blue"]
a.update({"height": 180})

# print(a)

# 요소의 삭제
b = a.popitem() # 마지막 요소 삭제
# print(b)
# print(a)

# 전체 삭제
# a.clear()
# print(a) # 객체 형태는 유지된다.

# print(a)

for x in a:
  print("key: " + x + ", value: " + str(a.get(x)))
  # print(f"key: {x}, value: {a.get(x)}") # f-string
