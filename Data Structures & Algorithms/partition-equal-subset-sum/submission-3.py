class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if (targSum:=sum(nums)) % 2:
            return False
        targSum //= 2

        row = [True]+[False]*targSum
        for num in nums:
            newRow = [True]+[False]*targSum
            for i in range(num, targSum+1):
                newRow[i] = row[i-num] or row[i]
            row = newRow
        return row[-1]
            

            
            