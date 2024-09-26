# 정규표현식 (Regular Expression)

import re

# 시작과 끝
a = "I live in Koresadfa, Seoul 42 Koreaffff Korea"

b = re.search("^I.*42$", a) # I로 시작하고 42로 끝나는 문자열
if b:
  print(b)
else:
  print("매칭되지 않았습니다.")

# findall() -> 매칭되는 모든 문자열을 리스트로 반환
# search() -> 매칭되는 첫번째 문자열을 반환
# split() -> 매칭되는 문자열을 기준으로 문자열을 나누어 리스트로 반환
# sub() -> 매칭되는 문자열을 다른 문자열로 치환

c = re.findall("[a-dA-Z0-9]", a) # a부터 d, A부터 Z, 0부터 9의 문자열을 찾아 리스트로 반환
d = re.findall("\d", a) # 숫자만 찾아 리스트로 반환
print(c)
print(d)

e = re.findall("K...a", a) # K로 시작하고 a로 끝나는 5글자 문자열
f = re.findall("K.*a", a) # K로 시작하고 a로 끝나는 모든 문자열
g = re.findall("Kore.+a", a) # K로 시작하고 a로 끝나는 모든 문자열(사이의 문자가 하나 이상 있어야 함)
print(e)
print(f)
print(g)

h = re.findall("Kore.?a", a)
print(h)

i = re.findall("K.{3}a", a) # K로 시작하고 a로 끝나며 중간에 3글자가 있는 문자열
print(i)

j = re.findall("live|Korea", a)
print(j)