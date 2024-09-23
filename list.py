lst = ["사과", "망고", "배", "복숭아", "오렌지"]

# append -> 리스트 끝에 데이터 추가
lst.append("바나나")
print(lst)

# insert -> 특정 index에 데이터 추가
lst.insert(2, "감")
print(lst)

lst[1] = "파인애플"
print(lst)

lst[2: 4] = ["체리", "딸기"]
print(lst)

# index 3에 자두가 들어가고, 부족한 4, 5는 삭제
lst[3:6] = ["자두"]
print(lst)

# index 1에 두리안이 들어가고 그 뒤로 키위, 수박, 멜론이 차례로 들어감 (기존 index 2였던 체리는 멜론 뒤로 밀림)
lst[1:2] = ["두리안", "키위", "수박", "멜론"]
print(lst)

# remove -> 삭제(중복된 값이 있으면 앞의 index 우선 삭제)
lst.append("두리안")
print(lst)
lst.remove("두리안")
print(lst)

# pop -> 리스트이 마지막 데이터를 삭제하고 가져옴 (인덱스 지정도 가능)
last_value = lst.pop()
print(lst)
print(last_value)

second_value = lst.pop(1)
print(lst)
print(second_value)

# del -> 리스트의 method는 아님
del lst[0]
print(lst)

# clear -> 리스트 전체 삭제
lst.clear()
print(lst)