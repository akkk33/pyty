class ListNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = ListNode()

    def __getitem__(self, item):
        return self.get(item)

    def append(self, *args):
        for val in args:
            node = ListNode(val)  # Initialise node
            current = self.head  # First node by default is head
            while current.next is not None:  # Point to the last node
                current = current.next
            current.next = node

    # Get the length of linked list
    def length(self):
        length = 0  # First node index by default is 0 (refers to head)
        current = self.head  # First node by default is head
        while current.next is not None:
            length += 1
            current = current.next
        return length

    # Get a specific node data by its index
    def get(self, index):
        if 0 <= index < self.length():  # Checking if the given index is within the list length
            target = 0  # Head index
            current = self.head
            while True:  # Cycle through the list to reach the target node
                current = current.next
                if target == index:
                    return current.val  # This is the requested node
                target += 1
        else:
            return "Index out of range!"

    # Insert a new node with given index and data:
    def insert(self, index, data):
        if 0 < index < self.length():
            target = 0
            current = self.head
            parent = self.head
            while True:
                current = current.next
                if index == target:
                    baby = ListNode(data)  # The new node :)
                    parent.next = baby  # Previous node
                    baby.next = current  # Current node would become child node of baby
                    break
                target += 1
                parent = current
        else:
            self.append(data)

    # Modify a node using given index and given data
    def set(self, index, data):
        if 0 < index < self.length():
            current = self.head
            target = 0
            while True:
                current = current.next
                if target == index:
                    current.val = data
                    return self.display()
                target += 1
        else:
            return "Index out of range!"

    # Display the list nodes as a regular Python list
    def display(self):
        elements = []
        current = self.head
        while current.next is not None:
            current = current.next
            elements.append(current.val)
        return elements
