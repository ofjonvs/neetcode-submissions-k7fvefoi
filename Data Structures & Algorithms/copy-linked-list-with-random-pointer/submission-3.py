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
        nodeMap = {}
        cur = head
        while cur is not None:
            nodeMap[cur] = newNode = nodeMap.get(cur, Node(cur.val))
            if cur.random:
                newNode.random = nodeMap[cur.random] = nodeMap.get(cur.random, Node(cur.random.val))
            if cur.next:
                newNode.next = nodeMap[cur.next] = nodeMap.get(cur.next, Node(cur.next.val))
            cur = cur.next
        return nodeMap.get(head)