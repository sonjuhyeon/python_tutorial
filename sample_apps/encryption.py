import random
import string # 특정 분류에 따른 문자 집합을 제공하는 모듈

# punctuation : 특수문자
# digits : 숫자
# ascii_letters : 영문자
char = " " + string.punctuation + string.digits + string.ascii_letters
char = list(char)
key = char.copy()

random.shuffle(key)
# print(key)

# encrypt
plain_text = input("암호화할 문자를 입력해 주세요: ")
cipher_text = ""

for letter in plain_text:
  index = char.index(letter)
  cipher_text += key[index]

print(f"암호화되기 전 비밀키: {plain_text}")
print(f"암호화된 비밀키: {cipher_text}")

# decrypt
cipher_text = input("복호화할 문자를 입력해 주세요: ")
plain_text = ""

for letter in cipher_text:
  index = key.index(letter)
  plain_text += char[index]

print(f"암호화되기 전 비밀키: {cipher_text}")
print(f"암호화된 비밀키: {plain_text}")

