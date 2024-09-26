class dc_list_node:
  def __init__(self, val):
    self.val = val
    self.prev = None
    self.next = None

class dc_linked_list:
  def __init__(self):
    self.head = None