from Singly_Linked_list import s_linked_list as sll

# 리스트 생성 및 노드 추가
ll = sll()
ll.addLast(10)
ll.addLast(20)
ll.addLast(30)
ll.addHead(5)

# 리스트 출력
ll.print_ll()  # 출력: 5 -> 10 -> 20 -> 30 -> None

# 특정 위치에 노드 삽입
ll.insertAt(2, 15)
ll.print_ll()  # 출력: 5 -> 10 -> 15 -> 20 -> 30 -> None

# 특정 위치의 노드 삭제
ll.deleteAt(3)
ll.print_ll()  # 출력: 5 -> 10 -> 15 -> 30 -> None

# 값으로 인덱스 찾기
index = ll.indexOf(15)
print(f"값 15의 인덱스: {index}")  # 출력: 값 15의 인덱스: 2

# 인덱스로 값 찾기
value = ll.valueAt(1)
print(f"인덱스 1의 값: {value}")  # 출력: 인덱스 1의 값: 10

# 값으로 노드 찾기
node = ll.findNodeByValue(10)
print(f"찾은 노드 값: {node.val}")  # 출력: 찾은 노드 값: 10

# 인덱스의 노드 값 교환
ll.swapNodes(1, 3)
ll.print_ll()  # 출력: 5 -> 30 -> 15 -> 10 -> None

# 특정 노드 뒤에 노드 삽입
node = ll.findNodeByValue(30)
ll.addAfter(node, 35)
ll.print_ll()  # 출력: 5 -> 30 -> 35 -> 15 -> 10 -> None

# 처음 노드 삭제
ll.deleteHead()
ll.print_ll()  # 출력: 30 -> 35 -> 15 -> 10 -> None

# 마지막 노드 삭제
ll.deleteLast()
ll.print_ll()  # 출력: 30 -> 35 -> 15 -> None

# 리스트 반전
ll.reverse()
ll.print_ll()  # 출력: 15 -> 35 -> 30 -> None

# 중복 값 추가 및 중복 제거
ll.addLast(35)
ll.addLast(35)
ll.print_ll()  # 출력: 15 -> 35 -> 30 -> 35 -> 35 -> None
ll.removeDuplicates()
ll.print_ll()  # 출력: 15 -> 35 -> 30 -> None

# 리스트 길이 확인
print(f"리스트 길이: {ll.getLength()}")  # 출력: 리스트 길이: 3

# 리스트 전체 삭제
ll.ll_clear()
ll.print_ll()  # 출력: None, size:0


# 리스트 생성
ll = sll()

# 빈 리스트에서 삭제 시도 (예외 처리 확인)
ll.deleteHead()  # 출력: Error: The list is empty. Cannot delete.
ll.deleteLast()  # 정상 작동 (빈 리스트에서는 아무 동작도 하지 않음)

# 유효하지 않은 인덱스에서 삽입/삭제 시도 (예외 처리 확인)
ll.insertAt(5, 100)  # 인덱스가 길이를 벗어났기 때문에 아무 동작도 하지 않음
ll.deleteAt(3)  # 인덱스가 유효하지 않음 (리스트가 비어 있음)

# 값이 없는 경우 인덱스 검색
index = ll.indexOf(999)
print(f"값 999의 인덱스: {index}")  # 출력: 값 999의 인덱스: -1

# 빈 리스트에 인덱스로 노드 찾기 시도 (예외 처리 확인)
value = ll.valueAt(0)  # 출력: Error: Index out of bounds

# 값을 가진 노드를 찾고 삭제 후의 상태 확인
ll.addLast(10)
ll.addLast(20)
ll.addLast(30)
ll.addAfter(ll.head, 15)  # 헤드 뒤에 15 삽입
ll.print_ll()  # 출력: 10 -> 15 -> 20 -> 30 -> None

# 다른 리스트의 노드를 조작하려는 시도 (예외 처리 확인)
test_ll = sll()
test_ll.addLast(50)
ll.addAfter(test_ll.head, 40)  # 출력: Error: Node does not belong to this linked list

# 삭제 시도 (노드가 없거나 연결리스트에 속하지 않음)
ll.deleteAfter(test_ll.head)  # 출력: Error: Node does not belong to this linked list
