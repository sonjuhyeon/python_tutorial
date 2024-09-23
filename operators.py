# 산술 연산자
x = 8
y = 5

print(f"{x} + {y} = {x + y}")
print(f"{x} - {y} = {x - y}")
print(f"{x} * {y} = {x * y}")
print(f"{x} / {y} = {x / y}")
print(f"{x} // {y} = {x // y}")
print(f"{x} % {y} = {x % y}")
print(f"{x} ** {y} = {x ** y}")


# 대입연산자
n = 10

n += 5 # 10 + 5
print(n) # 15

n -= 6 # 15 - 6
print(n) # 9

n *= 9 # 9 * 9
print(n) # 81

n /= 3 # 81 / 3
print(n) # 27.0

n //= 3 # 27 // 3
print(n) # 9

n %= 5 # 9 % 5
print(n) # 4

n **= 4 # 4 * 4
print(n) # 256


# 비교연산자
p = 10
q = 20
print(p == q) # False
print(p != q) # True
print(p <= q) # True
print(p >= q) # False
print(p < q) # True
print(p > q) # False


# 논리연산자
print(q > p and q != p) # True
print(q < p and q != p) # False
print(q < p or q != p) # True
print(q < p or q == p) # False
print(not(q == p)) # True