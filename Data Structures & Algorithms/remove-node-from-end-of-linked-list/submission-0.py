# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # Reverse the list
        prev = None
        curr = head

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        # prev is now the head of the reversed list
        head = prev

        # If we need to remove the first node
        if n == 1:
            head = head.next

        else:
            curr = head

            # Move to the node before the one we want to remove
            for i in range(n - 2):
                curr = curr.next

            # Remove the node
            curr.next = curr.next.next

        # Reverse the list again
        prev = None
        curr = head

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        return prev

