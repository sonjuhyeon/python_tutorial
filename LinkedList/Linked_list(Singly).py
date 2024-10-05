class s_list_node:
  def __init__(self, val, parent_list = None):
    self.val = val
    self.next = None
    self.parent_list = parent_list  # 노드가 속한 리스트를 추적

  # 노드 간 값 교환 메서드
  def swapWith(self, other_node):
    # next 값을 임시로 저장
    temp_next_self = self.next
    temp_next_other = other_node.next

    # 값과 속성을 교환
    self.__dict__, other_node.__dict__ = other_node.__dict__, self.__dict__

    # next 값을 복원
    self.next = temp_next_self
    other_node.next = temp_next_other


class s_linked_list:
  def __init__(self):
    self.head = None
    self.size = 0

  # 값으로 노드 찾기
  def findNodeByValue(self, value):
    current = self.head
    while current:
      if current.val == value:
        return current
      current = current.next
    print("Error: The value is not in the node")
    return None

  # 인덱스로 노드 찾기
  def findNodeByIndex(self, index):
    if index < 0 or index >= self.size:
      print("Error: Index out of bounds")
      return None

    current = self.head
    for _ in range(index):
      current = current.next
    return current
  
  # 값으로 인덱스 찾기
  def indexOf(self, value):
    current = self.head
    index = 0
    while current:
      if current.val == value:
        return index
      current = current.next
      index += 1
    return -1  # 값을 찾지 못한 경우

  # 인덱스로 값 찾기
  def valueAt(self, index):
    if index < 0 or index >= self.size:
      print("Error: Index out of bounds")
      return None
    current = self.head
    for _ in range(index):
      current = current.next
    return current.val

  # 마지막 노드 탐색
  def getLastNode(self):
    current = self.head
    if (current == None):
      return None
    while (current.next != None):
      current = current.next
    return current  # 마지막 노드 반환

  # 가장 앞에 노드 삽입
  def addHead(self, val):
    new_node = s_list_node(val, self)
    new_node.next = self.head  # 새로운 노드를 현재 헤드로 설정
    self.head = new_node  # 새로운 노드를 헤드로 설정
    self.size += 1

  # 가장 뒤에 노드 삽입
  def addLast(self, val):
    new_node = s_list_node(val, self)
    if (self.head == None):
      self.head = new_node  # 리스트가 비어있다면 새 노드가 헤드가 됨
    else:
      last_node = self.getLastNode()
      last_node.next = new_node  # 마지막 노드에 새 노드 연결
    self.size += 1

  # 특정 노드 뒤에 노드 삽입
  def addAfter(self, node, val):
    if self.head is None:
      print("Error: The list is empty.")
      return
    if (node == None):
      print("Error: Given node is None")
      return
    if (node.parent_list != self):
      print("Error: Node does not belong to this linked list")
      return
    new_node = s_list_node(val, self)
    new_node.next = node.next  # 새로운 노드의 다음을 현재 노드의 다음으로 설정
    node.next = new_node  # 현재 노드의 다음을 새로운 노드로 설정
    self.size += 1

  # 특정 노드의 다음 노드 삭제
  def deleteAfter(self, node):
    if self.head is None:
      print("Error: The list is empty.")
      return
    if ((node == None) or (node.next == None)):
      print("Error: Given node is None or has no next node")
      return
    if (node.parent_list != self):
      print("Error: Node does not belong to this linked list")
      return
    node.next = node.next.next  # 특정 노드의 다음 노드를 건너뛰어 삭제
    self.size -= 1

  # 처음 노드 삭제
  def deleteHead(self):
    if (self.head == None):
      print("Error: The list is empty. Cannot delete.")
      return
    self.head = self.head.next  # 헤드를 다음 노드로 변경
    self.size -= 1
    if self.size < 0:  # 안전한 사이즈 관리
      self.size = 0  # 사이즈가 음수가 되는 것을 방지

  # 마지막 노드 삭제
  def deleteLast(self):
    if (self.head == None):  # 리스트가 비어 있을 경우
      return
    if (self.head.next == None):  # 노드가 하나일 경우
      self.head = None
      self.size -= 1
      return
    current = self.head
    while (current.next.next != None):
      current = current.next
    current.next = None  # 마지막 노드의 이전 노드가 마지막이 됨
    self.size -= 1

  # linked list 전체 삭제
  def ll_clear(self):
    self.head = None  # head를 None으로 설정하여 리스트 전체 삭제
    self.size = 0

  # 특정 위치에 노드 삽입
  def insertAt(self, index, val):
    if index < 0 or index > self.size:
      print(f"Error: Index {index} out of bounds. Cannot insert.")
      return
    if index == 0:
      self.addHead(val)
      return
    current = self.head
    for _ in range(index - 1):
      current = current.next
    new_node = s_list_node(val, self)
    new_node.next = current.next
    current.next = new_node
    self.size += 1

  # 특정 위치의 노드 삭제
  def deleteAt(self, index):
    if self.head is None:
      print("Error: The list is empty. Cannot delete.")
      return
    if index < 0 or index >= self.size:
      print(f"Error: Index {index} out of bounds. Cannot delete.")
      return
    if index == 0:
        self.deleteHead()
        return
    current = self.head
    for _ in range(index - 1):
      current = current.next
    current.next = current.next.next
    self.size -= 1

  # 리스트 반전
  def reverse(self):
    prev = None
    current = self.head
    while (current != None):
      next_node = current.next
      current.next = prev
      prev = current
      current = next_node
    self.head = prev

  # 리스트 내 중복 값 제거
  def removeDuplicates(self):
    current = self.head
    seen_values = set()
    prev = None
    while (current != None):
      if current.val in seen_values:
        prev.next = current.next  # 중복일 경우 삭제
        self.size -= 1
      else:
        seen_values.add(current.val)
        prev = current
      current = current.next

  # 두 인덱스의 노드 값 교환
  def swapNodes(self, index1, index2):
    if index1 == index2:
      print("The two indices are the same. No need to swap.")
      return

    # 인덱스가 유효한지 확인
    if index1 < 0 or index2 < 0 or index1 >= self.size or index2 >= self.size:
      print("Error: One or both indices are out of range.")
      return

    node1 = self.findNodeByIndex(index1)
    node2 = self.findNodeByIndex(index2)

    if node1 and node2:
      node1.swapWith(node2)  # 노드 자체에 값 교환 책임을 위임

  # 리스트 길이 반환
  def getLength(self):
    return self.size
    
  # 모든 노드 출력
  def print_ll(self):
    current = self.head
    while current is not None:
      print(current.val, end=" -> ")
      current = current.next
    print(f"None, size:{self.size}")


# 리스트 생성 및 노드 추가
ll = s_linked_list()
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
ll = s_linked_list()

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
test_ll = s_linked_list()
test_ll.addLast(50)
ll.addAfter(test_ll.head, 40)  # 출력: Error: Node does not belong to this linked list

# 삭제 시도 (노드가 없거나 연결리스트에 속하지 않음)
ll.deleteAfter(test_ll.head)  # 출력: Error: Node does not belong to this linked list
