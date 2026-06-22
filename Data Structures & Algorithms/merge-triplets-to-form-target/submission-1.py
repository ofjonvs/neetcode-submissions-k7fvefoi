class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        a=b=c = False
        for ai, bi, ci in triplets:
            a |= ai == target[0] and bi <= target[1] and ci <= target[2]
            b |= ai <= target[0] and bi == target[1] and ci <= target[2]
            c |= ai <= target[0] and bi <= target[1] and ci == target[2]
        return a and b and c
                                