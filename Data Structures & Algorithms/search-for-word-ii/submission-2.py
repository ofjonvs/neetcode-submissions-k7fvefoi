class Trie:
    def __init__(self):
        self.root = {}
    
    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur[None] = None

    def search(self, word):
        cur = self.root
        for c in word:
            if c not in cur:
                return False
            cur = cur[c]
        return True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = set()
        trie = Trie()
        R, C = len(board), len(board[0])

        def search(r, c, trieChar, word, vis):
            if None in trieChar:
                res.add(word)
            
            for i in (-1, 1):
                hn, vn = (r, c+i), (r+i, c)
                if hn not in vis and 0 <= hn[1] < C and (ch:=board[hn[0]][hn[1]]) in trieChar:
                    vis.add(hn)
                    search(*hn, trieChar[ch], word+ch, vis)
                    vis.remove(hn)
                if vn not in vis and 0 <= vn[0] < R and (ch:=board[vn[0]][vn[1]]) in trieChar:
                    vis.add(vn)
                    search(*vn, trieChar[ch], word+ch, vis)
                    vis.remove(vn)

        for word in words:
            trie.insert(word)
        for r in range(R):
            for c in range(C):
                if board[r][c] in trie.root:
                    search(r, c, trie.root[board[r][c]], board[r][c], {(r, c)})

        return list(res)
            
        