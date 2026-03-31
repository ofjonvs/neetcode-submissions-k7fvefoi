class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        if k > len(arr):
            return 0
        threshold *= k
        currAvg = sum(arr[i] for i in range(k))
        res = int(currAvg >= threshold)

        for i in range(len(arr)-k):
            currAvg = currAvg + arr[i+k] - arr[i]
            res += 1 if currAvg >= threshold else 0
        return res

