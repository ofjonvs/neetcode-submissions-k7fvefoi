class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canFit(cap):
            totWeight, day = 0, 1
            for weight in weights:
                if weight + totWeight > cap:
                    totWeight = weight
                    day += 1
                else:
                    totWeight += weight
            print(cap, day)
            return day <= days
        l, r = max(weights), sum(weights)
        while l < r:
            m = (l+r)//2
            if canFit(m):
                r = m
            else:
                l = m + 1
        return l
        

