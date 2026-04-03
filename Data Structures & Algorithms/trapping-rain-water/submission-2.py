class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        area = 0
        maxl=maxr=0
        while l < r:
            if height[l] < height[r]:
                area += max(0, maxl-height[l])
                maxl = max(height[l], maxl)
                l += 1
            else:
                area += max(0, maxr-height[r])
                maxr = max(height[r], maxr)
                r -= 1
        return area
        
