# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Brute Force Approach 
    # TC --> O(n + m + (n+m)log(n+m)), SC --> O(n+m)
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        arr = []
        temp1 = list1
        temp2 = list2
        # adding elements from list1 to the array
        while temp1:
            arr.append(temp1.val)
            temp1 = temp1.next
        # adding elements from the list2 to the array
        while temp2:
            arr.append(temp2.val)
            temp2 = temp2.next
        arr.sort()  # sorting it
        # sorted array into linkedlist
        dummynode = ListNode(-1)
        temp = dummynode
        for val in arr:
            temp.next = ListNode(val)
            temp = temp.next
        # returning the head of merge sorted linkedlist
        return dummynode.next
    
    # Optimal Approch
    # TC --> O(n1+n2), SC --> O(1)
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # Create a dummy node to serve as 
        # the head of the merged list
        dummynode = ListNode(-1)
        temp = dummynode
        # traverse both the list simultaneously
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            # Move the temporary pointer 
            # to the next node
            temp = temp.next
        '''If any list still 
        has remaining elements, 
        append them to the merged list'''
        if list1 is not None:
            temp.next = list1
        else:
            temp.next = list2
        return dummynode.next
    def printLinkedList(head: ListNode):
        temp = head
        while temp is not None:
            # Print the data of the current node
            print(temp.val, end=" ")
            # Move to the next node
            temp = temp.next
        print()