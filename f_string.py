# f-string 포멧팅

name, age, add = "Juhyeon", 27, "Seoul"
print("이름: " + name + ", 나이: " + str(age))

txt1 = "이름: {}, 나이: {}".format(name, age)
txt2 = f"이름: {name}, 나이: {age}"
txt3 = "이름: %s, 나이: %d" % (name, age)

txt4 = f"이름: {name}\n나이: {age}"
txt5 = fr"이름: {name}\n나이: {age}"

print(txt1)
print(txt2)
print(txt3)
print(txt4)
print(txt5)

x, y = 10, 20
print(f"{x} + {y} = {x + y}")

alphabet = "abcdefghijklmnopqrstuvwxyz"
print(f"{alphabet[:5]}")
print(f"{alphabet.upper()}")

from datetime import date
print(f"오늘은 {date.today()}일 입니다.")