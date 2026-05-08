class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        from functools import lru_cache

        @lru_cache(len(coins)*amount)
        def recurse(i, total):
            if total == amount:
                return 0
            if i >= len(coins) or total > amount:
                return -1
            
            skip = recurse(i+1, total)
            include = recurse(i, total+coins[i])
            return skip if include == -1 else include+1 if skip == -1 else min(skip, 1+include)
            
        return recurse(0, 0)            