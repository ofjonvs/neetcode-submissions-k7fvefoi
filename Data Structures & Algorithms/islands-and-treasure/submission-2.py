class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        def bfs(row, col):
            i = 0
            queue = deque([(row, col)])
            visited = set()
            while queue:
                for j in range(len(queue)):
                    r, c = queue.popleft()
                    visited.add((r, c))
                    if grid[r][c] == 0:
                        grid[row][col] = i
                        return
                    for nr, nc in ((r+1, c), (r-1, c), (r, c-1), (r, c+1)):
                        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and (nr, nc) not in visited and grid[nr][nc] != -1:
                            queue.append((nr, nc))
                i += 1

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                grid[row][col] == INF and bfs(row, col)           
        
        
    
        
