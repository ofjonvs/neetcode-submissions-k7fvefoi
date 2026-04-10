# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodeSet = set()
        node = head
        while node:
            if node in nodeSet:
                return True
            nodeSet.add(node)
            node = node.next
        return False