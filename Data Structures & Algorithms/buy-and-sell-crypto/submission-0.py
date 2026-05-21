class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curMin = prices[0]
        res = 0
        for i in range(1, len(prices)):
            res = max(res, prices[i]-curMin)
            curMin = min(curMin, prices[i])
        return res