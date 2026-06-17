class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        queue = deque([(row, col) for row in range(len(grid)) for col in range(len(grid[0])) if not grid[row][col]])
        visited = set()
        i = 0
        while queue:
            i += 1
            for row, col in (queue.popleft() for _ in range(len(queue))):
                for r, c in ((row+1, col), (row-1, col), (row, col+1), (row, col-1)):
                    if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and (r, c) not in visited and grid[r][c] == INF:
                        grid[r][c] = i
                        visited.add((r, c))
                        queue.append((r, c))

