# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from functools import cache
class Solution:

    @cache
    def maxSub(self, root):
        if root is None:
            return float('-inf')
        return max(root.val, self.maxSub(root.right), self.maxSub(root.left))

    @cache
    def minSub(self, root):
        if root is None:
            return float('inf')
        return min(root.val, self.minSub(root.right), self.minSub(root.left))

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if self.maxSub(root.left) >= root.val or self.minSub(root.right) <= root.val:
            return False
        return self.isValidBST(root.left) and self.isValidBST(root.right)
            