# 1. 문자열
x = "hello"

# 2. int, float, complex
a = 10
print(type(a))
b = 10.5
print(type(b))
c = 1 + 1j
d = 1 - 1j
print(type(c), type(d))
print(c * d)


# list, tuple, dictionary, set

# list: 배열, [] 사용
lst = ["a", "b", "c"]
print(lst, type(lst))

# tuple: 리스트와 다르게 값을 변경 및 삭제가 불가능 ,() 사용
tp = ("a", "b", "c", "c")
print(tp, type(tp))

# dictionary: 객체, 키와 값
dic = {"naem":"Juhyeon", "age":28}
print(dic, type(dic))

# set: 중복이 허용되지 않음
s = {1, 2, 3, 1, 4, 5, 5, 3, 5, 7, 6, 100, 50, 40, 30, 100}
print(s, type(s))


# 여러줄 문자열 표기
# import lorem

# s = lorem.sentence()  # 'Eius dolorem dolorem labore neque.'
# p = lorem.paragraph()
# t = lorem.text()

p1 = """aaaaaaaaaaaaaaaaaa
bbbbbbbbbbbbbbbbbbbbbbbb c
 ccccccccccccccccccccccc"""
p2 = "aaaaaaaaa\nabbbbbbbbbbbbbbbbb\ncsssss"
print(p1, "\n", p2)