# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(x, y):
            return next(div for div in range(min(x, y), 0, -1) if not x % div and not y % div)

        cur = head
        while cur.next:
            newNode = ListNode(gcd(cur.val, cur.next.val))
            newNode.next, cur.next = cur.next, newNode
            cur = newNode.next
        return head