class Node:
    def __init__(self):
        self.children = {}

class PrefixTree:

    def __init__(self):
        self.root = Node()


    def insert(self, word: str) -> None:
        currNode = self.root
        for c in word:
            if c not in currNode.children:
                currNode.children[c] = Node()
            currNode = currNode.children[c]
        currNode.children[-1] = None

    def search(self, word: str) -> bool:
        currNode = self.root
        for c in word:
            if c not in currNode.children:
                return False
            currNode = currNode.children[c]
        return -1 in currNode.children

    def startsWith(self, prefix: str) -> bool:
        currNode = self.root
        for c in prefix:
            if c not in currNode.children:
                return False
            currNode = currNode.children[c]
        return True
    
        