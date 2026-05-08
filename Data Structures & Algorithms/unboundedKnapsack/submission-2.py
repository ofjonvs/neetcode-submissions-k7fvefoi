class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        dp = [0]*(capacity+1)
        for i in range(len(profit)):
            for j in range(1, capacity+1):
                if weight[i] <= j:
                    dp[j] = max(dp[j], profit[i]+dp[j-weight[i]])
        return dp[-1]