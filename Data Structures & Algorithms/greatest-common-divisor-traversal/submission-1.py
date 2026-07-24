class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        from functools import cache

        @cache
        def gcd(x, y):
            if not x % y:
                return y
            return gcd(y, x % y)
        
        numSets = len(nums)
        uf = [[None, 1] for _ in range(len(nums))]
        def getParent(i):
            if uf[i][0] is None:
                return i
            uf[i][0] = getParent(uf[i][0])
            return uf[i][0]

        def union(i, j):
            p1, p2 = getParent(i), getParent(j)
            if p1 == p2:
                return
            big, small = (p1, p2) if uf[p1][1] > uf[p2][1] else (p2, p1)
            uf[small][0] = big
            uf[big][1] += uf[small][1]
            nonlocal numSets
            numSets -= 1
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                gcd(nums[i], nums[j]) != 1 and union(i, j)
        
        return numSets == 1
            
            