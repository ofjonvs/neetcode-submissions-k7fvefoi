# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        cur=mid=head
        while cur:
            cur = cur.next.next
            mid = mid.next     

        cur = mid.next
        mid.next = None
        prev = mid
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        cur1, cur2 = prev, head
        res = 0
        while cur1:
            res = max(res, cur1.val+cur2.val)
            cur1, cur2 = cur1.next, cur2.next
        return res
        