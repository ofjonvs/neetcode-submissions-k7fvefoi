# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head.next is None:
            return head
        curr, length = head, 0
        while curr is not None:
            length += 1
            curr = curr.next
        curr = head
        for i in range(length//k):
            iterHead = curr
            prev = None
            for j in range(k):
                curr.next, curr, prev = prev, curr.next, curr
            if i == 0:
                head = prev
            else:
                iterHeadPrev.next = prev 
            iterHeadPrev = iterHead
        if length % k:
            iterHead.next = curr
        return head
