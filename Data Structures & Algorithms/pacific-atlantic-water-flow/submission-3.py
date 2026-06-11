class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        inBounds = lambda row, col: 0 <= row < len(heights) and 0 <= col < len(heights[0])
        pacificNodes = set()
        for c in range(len(heights[0])):
            stack = [(0, c)]
            while stack:
                row, col = stack.pop()
                pacificNodes.add((row, col))
                for r, c in ((row+1, col), (row-1, col), (row, col+1), (row, col-1)):
                    inBounds(r, c) and (r, c) not in pacificNodes and heights[row][col] <= heights[r][c] and stack.append((r, c))

        for r in range(len(heights)):
            stack = [(r, 0)]
            while stack:
                row, col = stack.pop()
                pacificNodes.add((row, col))
                for r, c in ((row+1, col), (row-1, col), (row, col+1), (row, col-1)):
                    inBounds(r, c) and (r, c) not in pacificNodes and heights[row][col] <= heights[r][c] and stack.append((r, c))

        atlanticNodes = set()
        for c in range(len(heights[0])):
            stack = [(len(heights)-1, c)]
            while stack:
                row, col = stack.pop()
                atlanticNodes.add((row, col))
                for r, c in ((row+1, col), (row-1, col), (row, col+1), (row, col-1)):
                    inBounds(r, c) and (r, c) not in atlanticNodes and heights[row][col] <= heights[r][c] and stack.append((r, c))

        for r in range(len(heights)):
            stack = [(r, len(heights[0])-1)]
            while stack:
                row, col = stack.pop()
                atlanticNodes.add((row, col))
                for r, c in ((row+1, col), (row-1, col), (row, col+1), (row, col-1)):
                    inBounds(r, c) and (r, c) not in atlanticNodes and heights[row][col] <= heights[r][c] and stack.append((r, c))
        
        return [[row, col] for row in range(len(heights)) for col in range(len(heights[0])) if (row, col) in pacificNodes and (row, col) in atlanticNodes]

