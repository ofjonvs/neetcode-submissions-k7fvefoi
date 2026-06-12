# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head.next is None:
            return
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        curr = head
        prev = None
        for i in range(length-1):
            if i >= (length+1)//2:
                curr.next, curr, prev = prev, curr.next, curr
            else:
                curr, prev = curr.next, curr
        curr.next = prev
        front, end = head, curr
        while front.val != front.next.next.val:
            front.next, front = end, front.next
            end.next, end = front, end.next
        end.next = None



