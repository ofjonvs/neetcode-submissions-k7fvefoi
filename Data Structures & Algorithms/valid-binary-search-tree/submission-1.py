# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from functools import cache
class Solution:

    @cache
    def maxMin(self, root):
        if root is None:
            return float('-inf'), float('inf')
        
        left, right = root.left, root.right
        maxLeft, minLeft = self.maxMin(root.left)
        maxRight, minRight = self.maxMin(root.right)
        max_ = max(root.val, maxLeft, maxRight)
        min_ = min(root.val, minLeft, minRight)
        return max_, min_

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if (root.left is not None and self.maxMin(root.left)[0] >= root.val) or (root.right is not None and self.maxMin(root.right)[1] <= root.val):
            return False
        return self.isValidBST(root.left) and self.isValidBST(root.right)

        left, right = root.left, root.right
        if (left is not None and left.val >= root.val) or right is not None and right.val <= root.val:
            return False
        return self.isValidBST(left) and self.isValidBST(right)
            