# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # TC --> O(N), SC --> O(1) using iteration
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head:  # Handling edge cases
            return head

        length, tail = 1, head

        while tail.next:  # calculating the total length
            tail = tail.next
            length += 1

        k = k % length  # if k == length, return the same
        if k == 0:
            return head

        cur = head
        for i in range(length - k - 1):
            cur = cur.next  # iteration break before k

        newhead = cur.next  # new head starts after 'cur'
        cur.next = None  # break the list
        tail.next = head  # connect old tail to old head

        return newhead
