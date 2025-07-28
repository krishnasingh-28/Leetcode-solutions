# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # TC --> O(1), SC --> O(1)
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # overwriting data of next node on the current node
        node.val = node.next.val
        # making the current node to point to the next node
        node.next = node.next.next
