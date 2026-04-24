class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        def recurse(i, curSum, path):
            if curSum == target:
                res.append(path.copy())
                return
            if i >= len(nums) or curSum > target:
                return

            recurse(i+1, curSum, path)

            path.append(nums[i])
            recurse(i, curSum+nums[i], path)
            path.pop()
            
        recurse(0, 0, [])
        return res
            
            