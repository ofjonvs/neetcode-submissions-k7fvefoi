class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        from functools import cache
        @cache
        def search(i, j):
            if (i, j) == (len(grid)-1, len(grid[0])-1):
                return grid[-1][-1]
            if i >= len(grid) or j >= len(grid[0]):
                return float('inf')
            return grid[i][j] + min(search(i+1, j), search(i, j+1))

        return search(0, 0)