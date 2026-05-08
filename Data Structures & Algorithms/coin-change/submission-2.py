class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')]*(amount+1)
        dp[0] = 0
        for coin in coins:
            for j in range(coin, amount+1):
                dp[j] = min(1+dp[j-coin], dp[j])
        return -1 if dp[-1] == float('inf') else dp[-1]