class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
            
        maxLeft, maxRight = deque(), deque()
        currMaxLeft = currMaxRight = 0
        for i in range(len(height)):
            maxLeft.append(currMaxLeft)
            currMaxLeft = max(currMaxLeft, height[i])
            maxRight.append(currMaxRight)
            currMaxRight = max(currMaxRight, height[-i-1])
        return sum(max(0, min(maxLeft.popleft(), maxRight.pop())-h) for h in height)
        
