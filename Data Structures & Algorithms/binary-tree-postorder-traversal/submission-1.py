# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [[root, False]]
        po = []
        while stack:
            if stack[-1][0] is None:
                stack.pop()
                while stack and stack[-1][1]:
                    po.append(stack.pop()[0].val)
                if stack:
                    stack[-1][1] = True
                    stack.append([stack[-1][0].right, False])
            else:
                stack.append([stack[-1][0].left, False])
        return po