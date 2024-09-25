a = {"사과", "바나나"}
b = {"사과", "체리", "바나나"}

# union(): 합집합 반환
c = a.union(b)
# print(c)

# difference(): 차집합 반환 - 좌측 집합에서 우측 집합을 차감한 요소 반환
d = a.difference(b)
# print(d)

# difference_update(): a와 b의 차집합을 a에 저장
# a.difference_update(b)
# print(a)

# intersection(): 교집합 반환
e = a.intersection(b)
# print(e)

# isdisjoint(): a와 b가 교집합이 없는지 확인 : 겹치는게 있으면 False, 없으면 True
# print(a.isdisjoint(b)) # 사과가 겹침

# issubset(): a가 b의 부분집합인지 확인
f = a.issubset(b)
# print(f)

# symetric_difference(): a와 b의 합집합에서 교집합을 제거한 것
print(a.symmetric_difference(b))