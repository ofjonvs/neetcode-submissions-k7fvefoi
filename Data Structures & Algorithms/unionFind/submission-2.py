class Node:
    def __init__(self, val):
        self.val = val
        self.parent = None

class UnionFind:
    
    def __init__(self, n: int):
        self.nodes = [Node(i) for i in range(n)]
        self.numComponents = n

    def find(self, x: int) -> int:
        node = self.nodes[x]
        while node.parent is not None:
            node = node.parent
        return node

    def isSameComponent(self, x: int, y: int) -> bool:
        print(self.find(x).val , self.find(y).val)
        return self.find(x).val == self.find(y).val

    def union(self, x: int, y: int) -> bool:
        if self.isSameComponent(x, y):
            return False
        self.find(y).parent = self.find(x)
        self.numComponents -= 1
        return True

    def getNumComponents(self) -> int:
        return self.numComponents
