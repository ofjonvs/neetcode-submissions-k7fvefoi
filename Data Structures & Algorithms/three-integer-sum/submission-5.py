class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if (i and nums[i] == nums[i-1]):
                continue
            
            l, r = i+1, len(nums)-1
            while l < r:
                grp = [nums[i], nums[l], nums[r]]
                tot = sum(grp)
                if tot == 0:
                    result.append(grp)
                    r -= 1
                    l += 1
                    while l < len(nums) and nums[l-1] == nums[l]:
                        l += 1
                elif tot > 0:
                    r -= 1
                else: 
                    l += 1
        return result

            

