class dc_list_node:
  def __init__(self, val):
    self.val = val
    self.prev = val
    self.next = val

class dc_linked_list:
  def __init__(self):
    self.head = None