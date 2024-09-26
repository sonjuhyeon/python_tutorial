# 람다 함수란 이름이 없는 함수를 의미함
# lambda a: a * 10


y = lambda a: a * 2  # 인수 a를 받아서 2를 곱하는 람다 함수
# print(y(5))  # y 함수에 5를 전달하면 10을 반환


# 인수가 여러개인 람다 함수
z = lambda a, b: a * b  # 인수 a와 b를 받아서 곱하는 람다 함수
# print(z(2, 3))  # z 함수에 2와 3을 전달하면 6을 반환


# 람다 함수를 다른 함수에 사용
def func1(n):
  return lambda a: a * n  # 인수 n을 받아서, 인수 a를 n과 곱하는 람다 함수를 반환


my1 = func1(5)  # func1에 5를 전달하면, a에 5를 곱하는 람다 함수가 반환됨
my2 = func1(10)  # func1에 10을 전달하면, a에 10을 곱하는 람다 함수가 반환됨
print(my1(2))  # my1 함수에 2를 전달하면 10을 반환
print(my2(3))  # my2 함수에 3을 전달하면 30을 반환


# 리스트 생성
mylist = list(filter(lambda x : x % 2, range(10)))  # 0부터 9까지의 숫자 중 홀수만 필터링하여 리스트로 반환
print(mylist)  # [1, 3, 5, 7, 9] 출력
