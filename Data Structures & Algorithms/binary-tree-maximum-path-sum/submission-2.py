# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        from functools import cache

        @cache
        def helper(root):
            if root is None:
                return float('-inf')
            leftMax, rightMax = helper(root.right), helper(root.left)
            return max(root.val, root.val+leftMax, root.val+rightMax)

        def recurseAll(root):
            if root is None:
                return float('-inf')
            maxLeft, maxRight = helper(root.left), helper(root.right)
            yield max(root.val, root.val+maxLeft, root.val+maxRight, root.val+maxLeft+maxRight)
            yield from recurseAll(root.left)
            yield from recurseAll(root.right)
        return max(recurseAll(root))

        
        