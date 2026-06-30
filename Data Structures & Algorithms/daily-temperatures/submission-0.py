class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack, out = [], [0]*len(temperatures)
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                poppedIdx, _ = stack.pop()
                out[poppedIdx] = i - poppedIdx
            stack.append((i, temp))
        return out