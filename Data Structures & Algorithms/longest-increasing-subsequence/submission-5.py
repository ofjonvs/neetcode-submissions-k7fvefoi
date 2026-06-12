class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        import functools

        @functools.cache
        def recurse(i):
            if i == len(nums)-1:
                return 1
            
            return max((1 + recurse(j)) if nums[j] > nums[i] else 1 for j in range(i+1, len(nums)))
        return max(recurse(i) for i in range(len(nums)))