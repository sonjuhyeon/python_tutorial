# 변수: 변수 타입 지정 안함
x = 10
print(x, type(x))

zero = "0"
print(zero, type(zero))

pi = 3.14
print(pi, type(pi))


# type casting
a = "3"
print(a, type(a))
b = int(a)
print(b, type(b))

# 변수 여러개 선언
name, age, add = "Juhyeon", 27, "Seoul"
print(name, age, add)

# 여러 변수에 하나의 값 지정
x = y = z = 10
print(x, y, z)

# list 구조분해 할당
fruits = ["apple", "banana", "cherry"]
a, b, c = fruits
print(fruits, a, b, c)
