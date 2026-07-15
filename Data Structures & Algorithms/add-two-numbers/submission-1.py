# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1, cur2 = l1, l2
        carry = 0
        resHead = curRes = ListNode()
        while cur1 and cur2:
            val = cur1.val + cur2.val + carry
            carry, val = (1, val-10) if val >= 10 else (0, val)
            curRes.next = ListNode(val)
            curRes = curRes.next
            cur1 = cur1.next
            cur2 = cur2.next
        for node in (cur1, cur2):
            while node:
                val = node.val + carry
                carry, val = (1, val-10) if val >= 10 else (0, val)
                curRes.next = ListNode(val)
                curRes = curRes.next
                node = node.next
        if carry:
            curRes.next = ListNode(1) 

        return resHead.next
