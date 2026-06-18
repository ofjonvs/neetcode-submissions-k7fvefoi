class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        twoBack, oneBack = cost[:2]
        for i in range(2, len(cost)):
            oneBack, twoBack = cost[i] + min(oneBack, twoBack), oneBack
        return min(oneBack, twoBack)