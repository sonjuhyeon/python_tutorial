# isalpha() -> 문자열이 모두 알파벳인지 확인
a = "abc"
b = "ABC"
c = "a b c"
d = "abc1"

print(a, a.isalpha())
print(b, b.isalpha())
print(c, c.isalpha())
print(d, d.isalpha())


# isnumeric() -> 문자열이 모두 숫자인지 확인
# isdigit() == isnumeric
e = "1234"
f = "aa4"

print(e, e.isnumeric())
print(f, f.isnumeric())


# isalnum() -> 알파벳과 숫자로 이루어진 문자열인지 확인
g = "abac"
h = "1234"
i = "abaw451"
j = "asd a46q"

print(g, g.isalnum())
print(h, h.isalnum())
print(i, i.isalnum())
print(j, j.isalnum())


# isspace() -> 문자열이 모두 공백인지 확인
k = "       "
l = "   asd   "
print(k, k.isspace())
print(l, l.isspace())


# isdecimal() -> 10진수 문자 확인
# islower() -> 소문자로만 이루어진 문자열인지 확인
# isupper() -> 대문자로만 이루어진 문자열인지 확인
# swapcase() -> 대문자는 소문자로, 소문자는 대문자로



# join()
lst = ["aa", "bb", "cc"]
tup = ("aa", "bb", "cc")

print(" ".join(lst))
print("/".join(lst))
print("-".join(tup))

# splitlines() -> 개행을 기준으로 분리하여 리스트 반환
s = "Hello\nWorld"
print(s.splitlines())