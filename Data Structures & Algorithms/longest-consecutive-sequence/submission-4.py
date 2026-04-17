class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seqLen = {}
        maxSeqLen = 0
        for num in nums:
            if num in seqLen:
                continue
            
            seqLen[num] = 1 + seqLen.get(num-1, 0) + seqLen.get(num+1, 0)
            if num-1 in seqLen:
                seqLen[num-seqLen[num-1]] = seqLen[num]
            if num+1 in seqLen:
                seqLen[num+seqLen[num+1]] = seqLen[num]
            maxSeqLen = max(seqLen[num], maxSeqLen)
        return maxSeqLen
