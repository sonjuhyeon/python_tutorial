# center - 문자열을 중앙에 위치

a = "abbbbcdefghij"
b = a.center(20)
c = a.center(20, "*")
d = a.center(21, "*")
print(b)
print(c)
print(d)

# count
e = a.count("b") # 변수 a에 문자 "b"가 몇개 들어있는가?
print(e)

# endswith - 문자열이 특정 문자열로 끝나는지 확인
print(a.endswith("ij"))
print(a.endswith("ij."))

# startswith - 문자열이 특정 문자열로 끝나는지 확인
print(a.startswith("ab"))
print(a.startswith("abc"))

# replace
print(a.replace("b", "v"))

# split
s = "asdfgpisaf sadf sagdfsadf asrtasdfasdf asrgasfg alugoufas"
print(s.split(" "))
print(s.split(" ", 3))
