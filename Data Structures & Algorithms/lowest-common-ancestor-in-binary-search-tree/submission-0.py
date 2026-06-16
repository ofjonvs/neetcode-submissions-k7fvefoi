# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root
        small, big = (p.val, q.val) if p.val < q.val else (q.val, p.val)
        while not small <= curr.val <= big:
            curr = curr.left if curr.val > big else curr.right
        return curr