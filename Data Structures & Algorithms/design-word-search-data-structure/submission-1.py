class Node:
    def __init__(self):
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        cur.children[None] = None

    def search(self, word: str) -> bool:
        def helper(i, node):
            if i >= len(word):
                return None in node.children
            if (c:=word[i]) == '.':
                return any(helper(i+1, child) for child in node.children.values() if child is not None)
            if c not in node.children:
                return False
            return helper(i+1, node.children[c])

        return helper(0, self.root)

