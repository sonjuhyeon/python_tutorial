import re
a = "Juhyeon lives in Korea, Seoul 142"

b = re.findall("[img]", a) # i, m, g 문자를 찾아 리스트로 반환
c = re.findall("[^a-zA-Z]", a) # 알파벳이 아닌 문자를 리스트로 반환
d = re.findall("[0-9][0-9]", a) # 두자리 숫자를 반환
print(b)
print(c)
print(d)


# search() - 객체를 반환
e = re.search(r"\s", a) # 첫번째 공백 문자 매칭
f = re.search(r"live", a) # live 문자열 매칭

print(e)
print(f.start())
print(f.end())


# split 
i = re.split(r"\s", a) # 공백 문자를 기준으로 나누기, 3번째 파라미터를 넣으면 나눈 횟수 지정
j = re.split(r"\s", a, 3) # 공백 문자를 기준으로 나누기, 3번째 파라미터를 넣으면 나눈 횟수 지정
print(i)
print(j)


# sub
k = re.sub(r"\s", ":", a) # 공백을 :으로 대체
print(k)