class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')]*(amount+1)
        dp[0] = 0
        for i in range(len(coins)):
            for j in range(amount+1):
                if coins[i] <= j:
                    dp[j] = min(1+dp[j-coins[i]], dp[j])
        return -1 if dp[-1] == float('inf') else dp[-1]