class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        vis = set()
        queue = deque([next((i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 1)])
        perim = 0
        while queue:
            if (sq:=queue.popleft()) in vis:
                continue
            vis.add(sq)
            x, y = sq
            for nx, ny in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 1:
                    queue.append((nx, ny))
                else:
                    perim += 1
        return perim
