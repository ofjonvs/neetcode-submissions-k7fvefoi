# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def search(node, curMax):
            if node is None:
                return 0
            newMax = max(curMax, node.val)
            return int(node.val >= curMax) + search(node.left, newMax) + search(node.right, newMax)
        return search(root, -100)