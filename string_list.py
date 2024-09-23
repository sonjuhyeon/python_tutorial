# 문자열은 자체적으로 리스트 형태로 사용 가능, 따라서 인덱싱으로 컨트롤 가능

import lorem

s = lorem.sentence()  # 'Eius dolorem dolorem labore neque.'
p = lorem.paragraph()
t = lorem.text()
print(s)
# print(p)
# print(t)

print(s[0], s[1], s[-1], s[-2])
# 인덱스 -1은 가장 마지막 요소


# slicing
print(s[:]) #전체
print(s[:5]) # 처음(인덱스 0)부터 인덱스 4까지
print(s[5:]) # 인덱스 5 부터 끝까지
print(s[-5:-1]) # 마지막에서 5번째 문자열 부터 마지막 2번째 문자열까지
print(s[-1:-5])
print(s[-1:-5:-1]) #마지막 인덱스부터 마지막에서 4번째 인덱스까지 역으로
print(s[1:-10]) # 인덱스 1 번부터 마지막 인덱스에서 11번째 까지

test = "LoremIpsumissimplydummytext"
w1 = test[:5]
w2 = test[5:10]
w3 = test[10:12]
w4 = test[12:18]
w5 = test[18:23]
w6 = test[23:]
print(w1, w2, w3, w4, w5, w6)
print("{} {} {} {} {} {}".format(w1, w2, w3, w4, w5, w6))

print(test[::2])
print(test[::-1])

sentence = " Juhyeon Son "
print(sentence.strip()) # 양쪽 공백제거
print(sentence.upper()) # 모든문자 대문자로 변환
print(sentence.lower()) # 모든문자 소문자로 변환
