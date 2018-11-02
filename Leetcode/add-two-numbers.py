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

from Data_structure.Linked_lists import LinkedList

first = LinkedList()
first.append(2, 4, 3)

second = LinkedList()
second.append(5, 6, 4)


print(first.display())
print(second.display())


class Solution:

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: LinkedList
        :type l2: LinkedList
        :rtype: LinkedList
        """
        result = LinkedList()
        for index in range(l1.length()):
            if (l1.get(index) + l2.get(index)) < 10:
                result.append(
                    l1.get(index) + l2.get(index)
                )
            elif (l1.get(index) + l2.get(index)) >= 10:
                l1.set(index + 1, l1.get(index + 1) + 1)
                result.append(
                    (l1.get(index) + l2.get(index)) - 10
                )
            else:
                return "Negative value"
        return result.display()


attempt = Solution()
print(attempt.addTwoNumbers(first, second))
