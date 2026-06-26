class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        for i, height in enumerate(heights):
            idx = i
            while stack and stack[-1][0] >= height:
                poppedHeight, idx = stack.pop()
                maxArea = max(maxArea, poppedHeight*(i-idx))
            stack.append((height, idx))
        return max(maxArea, max(height*(len(heights)-idx) for height, idx in stack))
