# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(x, y):
            x, y = (x, y) if x > y else (y, x)
            while x % y:
                x, y = y, x % y
            return y
        cur = head
        while cur.next:
            newNode = ListNode(gcd(cur.val, cur.next.val))
            newNode.next, cur.next = cur.next, newNode
            cur = newNode.next
        return head