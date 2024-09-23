name, age, add = "Juhyeon", 27, "Seoul"

txt1 = "이름: {}, 나이: {}"
intro1 = txt1.format(name, age)
print(intro1)

txt2 = "이름: {name}, 나이: {age}"
intro2 = txt2.format(name = "Juhyeon", age = 20)
print(intro2)

s1 = "저는 {:>5} 마리의 닭을 기릅니다."
print(s1.format(5))
print(s1.format(50))
print(s1.format(500))
print(s1.format(5000))
print(s1.format(50000))
print(s1.format(5000000))

s2 = "저는 {:^5} 마리의 닭을 기릅니다."
print(s2.format(5))
print(s2.format(50))
print(s2.format(500))
print(s2.format(5000))
print(s2.format(50000))
print(s2.format(500000))

s3 = "저는 {:=6} 마리의 닭을 기릅니다."
print(s3.format(-5))
print(s3.format(50))
print(s3.format(-500))

s4 = "최고기온: {:+}, 최저기온: {:+}"
print(s4.format(10, -5))

s5 = "통장잔고: {:,}"
print(s5.format(100000000000000))

s6 = "확률: {:.2%}"
print(s6.format(0.1))