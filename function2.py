# default parameter values

def default_func(country="Korea"):
  print(f"I'm from {country}")

default_func()
default_func("Canada")
default_func(country = "USA")


# collection paraeter

def collection_func(numbers):
  for i in numbers:
    print(i)

collection_func([1, 2, 3]) # list
collection_func((2, 4, 8)) # tuple
collection_func({2, 3, 5}) # set


# positional only - 모든 매게변수가 위치 인수로만 전달되어야 함
def prevent_func(a, /):
  print(a)

prevent_func(3)
# prevent_func(a = 3) # error: 키워드 인수를 사용하면 에러가 발생함