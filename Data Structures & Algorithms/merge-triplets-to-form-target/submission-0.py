class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        currTriplet = [0, 0, 0]
        for triplet in triplets:
            for i in range(3):
                if currTriplet[i] != target[i] and triplet[i] == target[i]:
                    currTriplet = [max(currTriplet[j], triplet[j]) for j in range(3)] if all (triplet[j] <= target[j] for j in range(3)) else currTriplet
        return currTriplet == target
                                