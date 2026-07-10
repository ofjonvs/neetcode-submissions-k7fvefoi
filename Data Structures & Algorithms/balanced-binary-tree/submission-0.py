# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if node is None:
                return 0, True
            (hl, bl), (hr, br) = dfs(node.left), dfs(node.right)
            return max(hl, hr)+1, bl and br and abs(hl-hr) <= 1
        return dfs(root)[1]