class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curMin = prices[0]
        res = 0
        for p in prices:
            res = max(res, p-curMin)
            curMin = min(curMin, p)
        return res