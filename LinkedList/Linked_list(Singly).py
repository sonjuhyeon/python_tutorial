class s_list_node:
  def __init__(self, val, parent_list = None):
    self.val = val
    self.next = None
    self.parent_list = parent_list  # 노드가 속한 리스트를 추적

class s_linked_list:
  def __init__(self):
    self.head = None
    self.size = 0

  # 특정 노드 탐색
  def findNode(self, val):
    current = self.head
    while (current != None):
      if current.val == val:
        return current  # 값이 일치하는 노드 반환
      current = current.next
    return None  # 값이 없을 경우 None 반환

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
    if (self.head != None):
      self.head = self.head.next  # 헤드를 다음 노드로 변경
    self.size -= 1

  # 마지막 노드 삭제
  def deleteLast(self):
    if (self.head == None):  # 리스트가 비어 있을 경우
      return
    if (self.head.next == None):  # 노드가 하나일 경우
      self.head = None
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
    if index == 0:
      self.addHead(val)
      return
    current = self.head
    for _ in range(index - 1):
      if (current == None):
        return  # 인덱스가 길이를 벗어났을 경우
      current = current.next
    new_node = s_list_node(val, self)
    new_node.next = current.next
    current.next = new_node
    self.size += 1

  # 특정 위치의 노드 삭제
  def deleteAt(self, index):
    if index == 0:
        self.deleteHead()
        return
    current = self.head
    for _ in range(index - 1):
      if ((current == None) or (current.next == None)):
        return  # 인덱스가 유효하지 않을 경우
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


# 예시 사용법
ll = s_linked_list()
ll.addLast(1)
ll.addLast(2)
ll.addLast(3)
ll.addHead(0)
ll.print_ll()  # 출력: 0 -> 1 -> 2 -> 3 -> None

ll.insertAt(2, 1.5)
ll.print_ll()  # 출력: 0 -> 1 -> 1.5 -> 2 -> 3 -> None

ll.deleteAt(3)
ll.print_ll()  # 출력: 0 -> 1 -> 1.5 -> 3 -> None

ll.reverse()
ll.print_ll()  # 출력: 3 -> 1.5 -> 1 -> 0 -> None

ll.addLast(1)
ll.addLast(1)
ll.print_ll()  # 출력: 3 -> 1.5 -> 1 -> 0 -> 1 -> 1 -> None
ll.removeDuplicates()
ll.print_ll()  # 출력: 3 -> 1.5 -> 1 -> 0 -> None

new_ll = ll.findNode(1.5)
cur = new_ll
while cur:
  print(cur.val)
  cur = cur.next

test_ll = s_linked_list()
test_ll.addLast(3)

print("-" * 100)
ll.print_ll()

# ll에 새로운 노드 삽입 (정상 동작)
ll.addAfter(new_ll, 2)
ll.print_ll()  # 출력: 3 -> 1.5 -> 2 -> 1 -> 0 -> None

print("-" * 100)

# 다른 리스트 test_ll의 노드를 ll에 삽입하려는 시도 (예외 발생)
ll.addAfter(test_ll.head, 1)  # Error: Node does not belong to this linked list
ll.print_ll()

# 다른 리스트 test_ll의 노드 삭제 시도 (예외 발생)
ll.deleteAfter(test_ll.head)  # Error: Node does not belong to this linked list
ll.print_ll()

ll.ll_clear()
ll.print_ll()  # 출력: None, size:0
