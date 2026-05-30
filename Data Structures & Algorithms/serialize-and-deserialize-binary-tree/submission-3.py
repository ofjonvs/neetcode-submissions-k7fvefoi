# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''
        queue = deque([root])
        s = []
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                s.append(node and node.val)
                if node is not None:
                    queue.append(node.left), queue.append(node.right)
            
        return ','.join(map(str, s))
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        data = deque(data.split(','))
        root = TreeNode(int(data.popleft()))
        queue = deque([root])
        while queue and data:
            for i in range(len(queue)):
                par = queue.popleft()
                left, right = data.popleft(), data.popleft()
                left, right = TreeNode(int(left)) if left != 'None' else None, TreeNode(int(right)) if right != 'None' else None
                par.left, par.right = left, right
                left and queue.append(left), right and queue.append(right)
        return root
