class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = [set() for _ in range(9)], [set() for _ in range(9)]
        boxs = [[set() for _ in range(3)] for _ in range(3)]
        for r in range(9):
            for c in range(9):
                if (val := board[r][c]) == '.':
                    continue
                if val in rows[r] or val in cols[c] or val in boxs[r//3][c//3]:
                    return False
                rows[r].add(val), cols[c].add(val), boxs[r//3][c//3].add(val)
        return True
