class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        tot = 0
        def recurse(i, curXor):
            nonlocal tot
            if i >= len(nums):
                tot += curXor
                return
            recurse(i+1, curXor)
            recurse(i+1, curXor^nums[i])
            
        recurse(0, 0)
        return tot