# 1. 문자열을 난수로 암호화 한다.
# 2. 암호화된 문자열을 입력하여 원래 문자열로 되돌린다.
# 3. 모든 암복호화 되는 문자열을 보면서 확인한다.

# shuffle() : 리스트의 요소를 무작위로 섞는다.

import random

a = "abcd"
a = list(a)
key = a.copy()

# a[0] = "k"
random.shuffle(key)

print(f"a: {a}")
print(f"key: {key}")

plain = "bc"
cipher = ""

for i in plain:
  index = a.index(i)
  # print(f"index: {i}")
  cipher += key[index]
  # print(f"cipher: {cipher}")

print(f"plain: {plain}")
print(f"cipher: {cipher}")

print("--- decrypt ---")

cipher_text = input("비밀키를 입력해 주세요: ")
plain_text = ""

for i in cipher_text:
  index = key.index(i)
  # print(f"index: {i}")
  plain_text += a[index]
  # print(f"cipher: {cipher}")

print(f"plain: {plain_text}")
print(f"cipher: {cipher_text}")