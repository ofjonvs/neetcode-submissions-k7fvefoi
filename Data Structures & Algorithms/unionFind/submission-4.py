class Node:
    def __init__(self, val):
        self.val = val
        self.parent = None
        self.size = 1

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
        return self.find(x).val == self.find(y).val

    def union(self, x: int, y: int) -> bool:
        xPar, yPar = self.find(x), self.find(y)
        if xPar.val == yPar.val:
            return False
        big, small = (xPar, yPar) if xPar.size > yPar.size else (yPar, xPar)
        small.parent = big
        big.size += small.size
        self.numComponents -= 1
        return True

    def getNumComponents(self) -> int:
        return self.numComponents
