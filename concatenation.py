# 문자열 조합

a = "hello"
b = "world"
c = a + b
print(c)


# format
name, age, add = "Juhyeon", 27, "Seoul"

txt1 = "이름: {}, 나이: {}".format(name, age)
txt2 = f"이름: {name}, 나이: {age}"
txt3 = "이름: %s, 나이: %d" % (name, age)

print(txt1)
print(txt2)
print(txt3)

a=123
b=2/3
print(f"a:{a} b:{b}")
print(f"a:{a:012d} b:{b:.2f}")
print("a:{:12d} b:{:.2f}".format(a, b))

# 문자열 개행 -> \n
# 문자열 탭 -> \t
# 문자열 백스페이스 -> \b