class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = r = 0
        curr = nums[0]
        res = float('inf')
        while r < len(nums) and l <= r:
            if curr >= target:
                res = min(res, r - l + 1)
                curr -= nums[l]
                l += 1
            else:
                r += 1
                curr += nums[r] if r < len(nums) else 0
        return res if res != float('inf') else 0