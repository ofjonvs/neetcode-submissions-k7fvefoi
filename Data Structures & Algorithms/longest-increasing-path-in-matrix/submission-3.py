class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        import functools, itertools
        @functools.cache
        def dfs(row, col):
            return max(itertools.chain((1+dfs(nRow, nCol) for nRow, nCol in ((row+1, col), (row-1, col), (row, col+1), (row, col-1)) if 0 <= nRow < len(matrix) and 0 <= nCol < len(matrix[0]) and matrix[nRow][nCol] > matrix[row][col]), (1,)))
        return max(dfs(row, col) for row in range(len(matrix)) for col in range(len(matrix[0])))