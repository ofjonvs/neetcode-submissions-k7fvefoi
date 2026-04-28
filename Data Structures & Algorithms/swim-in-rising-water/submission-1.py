class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        heap = [(grid[0][0], (0, 0), grid[0][0])]
        visited = set()
        while heap[0][1] != (len(grid)-1, len(grid)-1):
            height, (x, y), maxHeight = heapq.heappop(heap)
            visited.add((x, y))
            
            for xn, yn in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                if 0 <= xn < len(grid) and 0 <= yn < len(grid) and (xn, yn) not in visited:
                    heapq.heappush(heap, (grid[xn][yn], (xn, yn), max(grid[xn][yn], maxHeight)))
        return heap[0][2]
                