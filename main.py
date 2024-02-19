
class Node:

  def __init__(self, key, data):
    self.key = key
    self.data = data
    self.next = None
    self.prev = None

class DoublyLinkedList:

  def __init__(self):
    self.head = None
    self.last = None

  def is_empty(self):
    return self.head is None

  def display_forward(self):
    ptr = self.head
    print('[',end=' ')
    while ptr:
      print('({}, {})'.format(ptr.key, ptr.data), end=' ')
      ptr = ptr.next
    print(']')

  def display_backward(self):
    ptr = self.last
    print('[', end=' ')
    while ptr:
      print('({}, {})'.format(ptr.key, ptr.data), end=' ')
      ptr = ptr.prev
    print(']')

  def insert_first(self, key, data):
    link = Node(key, data)
    if(self.is_empty()):
      self.last = link
    else:
      self.head.prev = link
    link.next = self.head
    self.head = link

  def insert_last(self, key, data):
    link = Node(key, data)
    if(self.is_empty()):
      self.last = link
    else:
      self.last.next = link
    link.prev = self.last
    self.last = link  

  def insert_after(self, key, new_key, data):
    current = self.head
    while(current and current.key != key):
      current = current.next
    if(current is None):
      return False
    new_link = Node(new_key, data)
    if(current == self.last):
      new_link.next = None
      self.last = new_link
    else:
      new_link.next = current.next
      current.next.prev = new_link
    new_link.prev = current
    current.next = new_link
    return True

pointer = DoublyLinkedList()
pointer.insert_first(1,10)
pointer.insert_first(2,20)
pointer.insert_first(3,30)
pointer.insert_first(4,1)
pointer.insert_first(6,56)

pointer.display_forward()
print('============')
pointer.display_backward()
print('============')
pointer.insert_after(4,7,12)
pointer.display_forward()














    






























