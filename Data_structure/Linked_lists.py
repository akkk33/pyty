
class ListNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = ListNode()

    def append(self, *args):
        for val in args:
            node = ListNode(val)
            current = self.head
            while current.next is not None:  # Point to the last node
                current = current.next
            current.next = node

    def length(self):
        length = 0
        current = self.head
        while current.next is not None:
            length += 1
            current = current.next
        return length

    def get(self, index):
        if 0 <= index < self.length():
            target = 0
            current = self.head
            while True:
                current = current.next
                if target == index:
                    return current.val
                target += 1
        else:
            return "Index out of range!"

    def display(self):
        elements = []
        current = self.head
        while current.next is not None:
            current = current.next
            elements.append(current.val)
        return elements


newlist = LinkedList()
newlist.append(3,5,23,1)
newlist.display()
newlist.length()
print(newlist.get(2))
