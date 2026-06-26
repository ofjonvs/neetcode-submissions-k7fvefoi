class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def search(x, y):
            if 0 < x < len(board)-1 and 0 < y < len(board[0])-1 and board[x][y] == 'O':
                board[x][y] = 'OO'
                for nx, ny in zip((x+1, x-1, x, x), (y, y, y+1, y-1)):
                    search(nx, ny)

        for row in (0, len(board)-1):
            for col in range(1, len(board[0])-1):
                if board[row][col] == "O":
                    for nr, nc in zip((row+1, row-1, row, row), (col, col, col+1, col-1)):
                        search(nr, nc) 
        
        for col in (0, len(board[0])-1):
            for row in range(1, len(board)-1):
                if board[row][col] == 'O':
                    for nr, nc in zip((row+1, row-1, row, row), (col, col, col+1, col-1)):
                        search(nr, nc) 

        for row in range(1, len(board)-1):
            for col in range(1, len(board[0])-1):
                board[row][col] = 'O' if board[row][col] == 'OO' else 'X'
