class s_list_node:
  def __init__(self, val):
    self.val = val
    self.next = None

class s_linked_list:
  def __init__(self):
    self.head = None

  # 새로운 linked list 생성
  def new_ll(self, val):
    self.head = s_list_node(val)  # 새로운 리스트의 헤드에 값 삽입

  # 특정 값 탐색
  def findNode(self, val):
    current = self.head
    while current is not None:
      if current.val == val:
        return current  # 값이 일치하는 노드 반환
      current = current.next
    return None  # 값이 없을 경우 None 반환

  # 마지막 값 탐색
  def getLastNode(self):
    current = self.head
    if current is None:
      return None
    while current.next is not None:
      current = current.next
    return current  # 마지막 노드 반환

  # 가장 앞에 노드 삽입
  def addHead(self, val):
    new_node = s_list_node(val)
    new_node.next = self.head  # 새로운 노드를 현재 헤드로 설정
    self.head = new_node  # 새로운 노드를 헤드로 설정

  # 가장 뒤에 노드 삽입
  def addLast(self, val):
    new_node = s_list_node(val)
    if self.head is None:
      self.head = new_node  # 리스트가 비어있다면 새 노드가 헤드가 됨
    else:
      last_node = self.getLastNode()
      last_node.next = new_node  # 마지막 노드에 새 노드 연결

  # 특정 노드 뒤에 노드 삽입
  def addAfter(self, node, val):
    if node is None:
        return
    new_node = s_list_node(val)
    new_node.next = node.next  # 새로운 노드의 다음을 현재 노드의 다음으로 설정
    node.next = new_node  # 현재 노드의 다음을 새로운 노드로 설정

  # 특정 노드의 다음 노드 삭제
  def deleteAfter(self, node):
    if node is None or node.next is None:
      return
    node.next = node.next.next  # 특정 노드의 다음 노드를 건너뛰어 삭제

  # 처음 노드 삭제
  def deleteHead(self):
    if self.head is not None:
      self.head = self.head.next  # 헤드를 다음 노드로 변경

  # 마지막 노드 삭제
  def deleteLast(self):
    if self.head is None:  # 리스트가 비어 있을 경우
      return
    if self.head.next is None:  # 노드가 하나일 경우
      self.head = None
      return
    current = self.head
    while current.next.next is not None:
      current = current.next
    current.next = None  # 마지막 노드의 이전 노드가 마지막이 됨

  # linked list 전체 삭제
  def ll_clear(self):
    self.head = None  # head를 None으로 설정하여 리스트 전체 삭제

  # 특정 위치에 노드 삽입
  def insertAt(self, index, val):
    if index == 0:
      self.addHead(val)
      return
    current = self.head
    for _ in range(index - 1):
      if current is None:
        return  # 인덱스가 길이를 벗어났을 경우
      current = current.next
    new_node = s_list_node(val)
    new_node.next = current.next
    current.next = new_node

  # 특정 위치의 노드 삭제
  def deleteAt(self, index):
    if index == 0:
        self.deleteHead()
        return
    current = self.head
    for _ in range(index - 1):
      if current is None or current.next is None:
        return  # 인덱스가 유효하지 않을 경우
      current = current.next
    current.next = current.next.next

  # 리스트 반전
  def reverse(self):
    prev = None
    current = self.head
    while current is not None:
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
    while current is not None:
      if current.val in seen_values:
        prev.next = current.next  # 중복일 경우 삭제
      else:
        seen_values.add(current.val)
        prev = current
      current = current.next
    
  # 모든 노드 출력
  def print_ll(self):
    current = self.head
    while current is not None:
      print(current.val, end=" -> ")
      current = current.next
    print("None")

# 예시 사용법
ll = s_linked_list()
ll.new_ll(1)
ll.addLast(2)
ll.addLast(3)
ll.addHead(0)
ll.print_ll()  # 출력: 0 -> 1 -> 2 -> 3 -> None

node = ll.findNode(2)
ll.addAfter(node, 2.5)
ll.print_ll()  # 출력: 0 -> 1 -> 2 -> 2.5 -> 3 -> None

ll.deleteAfter(node)
ll.print_ll()  # 출력: 0 -> 1 -> 2 -> 3 -> None

ll.deleteLast()
ll.print_ll()  # 출력: 0 -> 1 -> 2 -> None

ll.deleteHead()
ll.print_ll()  # 출력: 1 -> 2 -> None

ll.ll_clear()
ll.print_ll()  # 출력: None
