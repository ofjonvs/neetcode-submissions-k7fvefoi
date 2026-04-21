# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        po = []
        def poTrav(node):
            if node is None:
                return
            poTrav(node.left), poTrav(node.right)
            po.append(node.val)
            
        poTrav(root)
        return po