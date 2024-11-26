
# List

# 일련의 값이 모인 집합을 다루기 위한 자료형. 
# 일반적인 프로그래밍 언어와 다르게 길이를 동적으로 조절할 수 있어 list 라고 부른다.

fruits = ['orange', 'apple', 'pear', 'kiwi', 'apple']

print(fruits)
print(fruits[0])

# List 유용한 메소드

# 1. count() : 해당 리스트에 인자로 준 값이 몇 개 존재하는 지 확인하여 그 수를 반환한다.
print("apple : " , fruits.count('apple'))

# 2. index() : 인자로 준 값이 몇 번째 인덱스에 존재하는지 확인하여 그 인덱스를 반환한다.
# 같은 값이 리스트 내에 여러 개 존재하면 가장 처음에 존재하는 값의 인덱스를 반환한다.
print("index : " , fruits.index('apple'))

print("index : " , fruits.index('apple',3))


# 3. reverse() : list 값을 역으로 정렬한다. 원본 list에 영향을 준다.
fruits.reverse()
print(fruits)


# 4. append() : list 끝에 값을 덧붙여 추가한다.
fruits.append('pineapple')
print(fruits)

# sort() : 요소를 정렬하는 메소드로 원본 list 에 영향을 준다.
# 기본적으로 알파벳 첫 글자를 기준으로 오름차순 정렬한다.

fruits.sort()
print(fruits)

fruits.sort(reverse=True)
print(fruits)

fruits.sort(key=len)
print(fruits)



# del 키워드

# 원본 배열 일부 요소 혹은 전체 목록을 제거할 수 있다.

abclist = ['A','B','C','D','E','F']
print(abclist)

del abclist[0]
print(abclist)

del abclist[1:3]
print(abclist)

del abclist


