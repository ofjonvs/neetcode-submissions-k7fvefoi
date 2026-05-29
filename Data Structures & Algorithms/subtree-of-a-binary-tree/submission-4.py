# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def checkTree(root, subRoot):
            if root is None or subRoot is None:
                return root == subRoot
            if root.val == subRoot.val:
                return checkTree(root.left, subRoot.left) and checkTree(root.right, subRoot.right)
            return False

        if root is None or subRoot is None:
            return root == subRoot
        
        curSameRoot = False
        if root.val == subRoot.val:
            curSameRoot = checkTree(root, subRoot)
        return curSameRoot or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)