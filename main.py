class Node:

  def __init__(self, val, next=None):
    self.val = val
    self.next = next


def displayNodes(node):
  pointer = node
  while pointer:
    print(pointer.val, end=" ")
    pointer = pointer.next


def reverseList(node):
  current = node
  prev = None

  def helperRec(current, prev):
    if not current:
      return prev
    next = current.next
    current.next = prev
    prev = current
    current = next
    return helperRec(current, prev)

  return helperRec(current, prev)


#Define LinkedList
head = Node(1, Node(2, Node(3, Node(4))))

displayNodes(head)
print("")
displayNodes(reverseList(head))
