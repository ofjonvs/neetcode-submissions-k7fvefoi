class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = [0]*(amount+1)
        cache[0] = 1
        for coin in coins:
            for amt in range(coin, amount+1):
                cache[amt] += cache[amt-coin]
        return cache[-1]
            
