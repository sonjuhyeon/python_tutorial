# specail sequences

import re
a = "Juhyeon lives in Korea, Seoul 142"

b = re.findall(r"\AJuhye", a) # 문자열의 시작이 Juhye인 문자열
c = re.findall(r"hyeon\B", a) # hyeon 문자열이 뒤에 오지 않는 문자열
d = re.findall(r"\Bhyeon", a) # hyeon 문자열이 앞에 오지 않는 문자열

print(b)
print(c)
print(d)

e = re.findall(r"\bJuhye", a) # Juhye 문자열이 단어의 시작에 오면 매칭
print(e)

f = re.findall(r"\d", a) # 숫자가 있는 문자를 리스트로 반환
g = re.findall(r"\D", a) # 숫자가 아닌 문자열을 리스트로 반환: 공백, 특수문자 포함
h = re.findall(r"\s", a) # 공백 문자를 반환
i = re.findall(r"\w", a) # 문자와 숫자를 반환

print(f)
print(g)
print(h)
print(i)

j = re.findall(r"42$", a) # 문자열 문장의 끝이 42
print(j)