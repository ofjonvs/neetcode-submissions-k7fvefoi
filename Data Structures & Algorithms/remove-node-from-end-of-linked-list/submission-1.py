# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            return
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        curr = head
        if length == n:
            return head.next
        for i in range(length-n-1):
            curr = curr.next
        curr.next = curr.next.next
        return head