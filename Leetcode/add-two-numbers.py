"""
https://leetcode.com/problems/add-two-numbers/

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse
order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ListNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = ListNode()

    def append(self, val):
        node = ListNode(val)
        current = self.head
        while current.next != None:  # Point to the last node
            current = current.next
        current.next = node

    def length(self):
        length = 0
        current = self.head
        while current.next != None:
            length += 1
            current = current.next
        return length

    def get(self, index):
        if 0 <= index <= self.length():
            target = 0
            current = self.head
            while True:
                current = current.next
                if target == index:
                    return current.val
                target += 1

    def display(self):
        elements = []
        current = self.head
        while current.next != None:
            current = current.next
            elements.append(current.val)
        return elements


newlist = LinkedList()
newlist.append(3)
newlist.append(4)
newlist.append(9)
newlist.append(71)
newlist.display()
newlist.length()
print(newlist.get(2))
# class Solution:
#     def addTwoNumbers(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         result = []
#         for key, value in enumerate(l1):
#             result.append(l1[key] + l2[key])
#         return result


# print(Solution().addTwoNumbers([5, 3, 7], [4, 2, 6]))
