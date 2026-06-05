class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        curPath = set()
        def recurse(i, row, col):
            if i == len(word):
                return True
            if row == len(board) or row == -1 or col == len(board[0]) or col == -1 or (row, col) in curPath:
                return False
            if word[i] == board[row][col]:
                curPath.add((row, col))
                res = any(recurse(i+1, newRow, newCol) for newRow, newCol in ((row+1, col), (row-1, col), (row, col+1), (row, col-1)))
                curPath.remove((row, col))
                return res
            return False
        return any(recurse(0, row, col) for row in range(len(board)) for col in range(len(board[0])))