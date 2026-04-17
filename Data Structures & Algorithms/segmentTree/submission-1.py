class Node:
    def __init__(self, range):
        self.range = range
        self.val = 0
        self.left = self.right = None

class SegmentTree:
    
    def __init__(self, nums: List[int]):
        def initialize(node):
            l, r = node.range
            if l == r:
                node.val = nums[l]
                return node
            m = (r-l)//2 + l
            node.left = initialize(Node((l, m)))
            node.right = initialize(Node((m+1, r)))
            node.val = node.left.val + node.right.val
            return node

        self.root = Node((0, len(nums)-1))
        initialize(self.root)
            
    def update(self, index: int, val: int) -> None:
        path = []
        cur = self.root
        while cur.range != (index, index):
            path.append(cur)
            l, r = cur.range
            m = (r-l)//2 + l
            if index <= m:
                cur = cur.left
            else: 
                cur = cur.right
        cur.val = val
        while path:
            cur = path.pop()
            cur.val = cur.left.val + cur.right.val

    
    def query(self, L: int, R: int) -> int:
        def helper(node, L, R):
            if (L, R) == node.range:
                return node.val
            cur = node
            l, r = cur.range
            m = (r-l)//2 + l
            if L > m:
                return helper(cur.right, L, R)
            elif R <= m:
                return helper(cur.left, L, R)
            else:
                return helper(cur.left, L, m) + helper(cur.right, m+1, R)
        return helper(self.root, L, R)