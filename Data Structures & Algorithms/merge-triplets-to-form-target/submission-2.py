class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        satisfied = [False]*3
        for triplet in triplets:
            for i in range(3):
                satisfied[i] |= triplet[i] == target[i] and all(triplet[j] <= target[j] for j in range(3))
        return all(satisfied)
                                