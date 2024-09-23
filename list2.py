lst = ["강아지", "고양이", "햄스터", "토끼", "고슴도치", "앵무새"]
prime = [31, 3, 11, 29, 13, 19, 17, 23, 2, 7, 5]

for i in lst:
  print(i)

lst.sort()
print(lst)

prime.sort(reverse=1)
print(prime)


# copy
c_lst = lst.copy()
print(c_lst)
lst[0] = "도마뱀"
print(lst)
print(c_lst)


# list()
s = "abcdefghijklmnopqrstuvwxyz"
alphabet = list(s)
print(alphabet)

# extend
prime2 = [83, 89, 97, 47]
prime3 = [59, 61, 71]
prime.extend(prime2)
print(prime)

prime += prime3
print(prime)