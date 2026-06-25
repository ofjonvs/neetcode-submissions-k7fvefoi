"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return head
        cur = head
        newHead = Node(head.val)
        newCur = newHead
        oldToNew = {head: newHead}
        while cur.next is not None:
            newCur.next = Node(cur.next.val)
            cur = cur.next
            newCur = newCur.next
            oldToNew[cur] = newCur

        cur = head
        newCur = newHead
        while cur is not None:
            newCur.random = cur.random and oldToNew[cur.random]
            newCur = newCur.next
            cur = cur.next
        return newHead