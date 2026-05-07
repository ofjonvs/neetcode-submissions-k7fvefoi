class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        totSum = sum(stones)
        halfSum = totSum//2 + 1
        dp = [0]*(halfSum)
        for i, stone in enumerate(stones):
            newDp = [0]*(halfSum)
            for j in range(halfSum):
                if j >= stone:
                    newDp[j] = max(dp[j], stone+dp[j-stone])
                else:
                    newDp[j] = dp[j]
            dp = newDp 
        return totSum - 2*dp[-1]