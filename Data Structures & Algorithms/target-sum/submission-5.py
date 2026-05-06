class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if sum(nums) < target:
            return 0
        posSums = [0]*(sum(nums)*2+1)
        zero = len(posSums)//2
        posSums[zero] = 1
        for i, n in enumerate(nums):
            newRow = [0]*(sum(nums)*2+1)
            for j, s in enumerate(posSums):
                if j + n < len(newRow):
                    newRow[j + n] += s
                if j - n >= 0:
                    newRow[j - n] += s
            posSums = newRow
        return posSums[target+zero]

            