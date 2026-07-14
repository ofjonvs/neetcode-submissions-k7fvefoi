class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.']*n for _ in range(n)]
        res = []
        def helper(row):
            if row == n:
                res.append([''.join(r) for r in board])
            
            for c in range(n):
                valid = True
                for i, r in enumerate(range(row-1, -1, -1), start=1):
                    diagR, diagL = c + i, c - i
                    if board[r][c] == 'Q' or 0 <= diagL and board[r][diagL] == 'Q' or diagR < n and board[r][diagR] == 'Q':
                        valid = False
                        break
                if valid:
                    board[row][c] = 'Q'
                    helper(row + 1)
                    board[row][c] = '.'

        helper(0)
        return res